#!/usr/bin/env python3
"""Ingest historical municipal election results (poll-by-poll Statement of Votes Cast)
from Open Ottawa's ArcGIS Hub into `election_results_<year>` + `election_results_totals`.

    python3 tools/ingest/election_results.py            # 2022 (the only year wired up so far)
    python3 tools/ingest/election_results.py --list      # sheet names + row counts, no registration

Where this comes from: `sources.json`'s `election-results-history` is tagged `api,bulk`
because the *voting-place and boundary* datasets on the hub genuinely are (GeoServices +
CSV/GeoJSON/KML). The **results themselves** are not -- the DCAT feed lists "2022 Elections
Official Results" etc. as `Web Page` only, and the landing page is a client-rendered ArcGIS
Hub SPA with nothing in the served HTML (checked: no embedded JSON, no `__NEXT_DATA__`).
Rendered it in a real headless Chromium instead and watched the network requests, which
turned up the item's real id and confirmed it is an ordinary public ArcGIS "Document" item
-- `StatementOfVotesCast_Oct28_Final.xlsx`, 776,237 bytes, downloadable at the standard
`.../sharing/rest/content/items/<id>/data` endpoint with no auth. `sources.json`'s own
`verify` note undersold this: it was written against the boundary/places datasets, not
checked against the results item specifically. Worth fixing there too.

**Workbook shape, and why the parser keys off the header row rather than fixed offsets.**
One sheet per race (`Mayor_Maire`, `Ward_quartier_1`..`24`, plus OCDSB/OCSB/CEPEO/CECCE
school-board trustee zones and Declined/Rejected Ballots -- not ingested yet, see below).
Each sheet's header row has a genuine column for every meta field (Precinct, Times Cast,
Registered Voters, Undervotes, Overvotes) and one for every candidate, but Excel's merged
cells give the un-merged reader a *different* number of trailing blank columns after each
candidate's name depending on how the sheet's original authors merged it -- there is no
fixed stride. Every data row has `None` in exactly the same slots the header does, so
zipping header labels to row values and dropping `None` header positions recovers the
right value for the right candidate regardless of merge width, with no guessing.

**Precinct rows vs. the ward-wide total row are the same shape, deliberately not split.**
"01-001 - Divine Infant School" and "City / Ville - Total" both carry a real integer in
Times Cast; the two purely-hierarchical label rows above them ("City / Ville", "City of
Ottawa / Ville d'Ottawa") carry `''` there instead. So `isinstance(times_cast, (int, float))`
is the one test needed to keep a row; `is_total` is set by name-matching "- Total" so a
caller can pull ward-level margins without re-deriving them from 60+ precinct rows.

**Not yet ingested: school-board trustee zones, Declined/Rejected Ballots sheets, and any
year before 2022.** The roadmap's actual question ("2022 margins -> which races are
competitive") only needs Mayor + the 24 ward races. Extending to trustee zones needs a
zone->ward crosswalk that does not obviously exist (unlike `election_trustee_zones`, which
crosswalks the *2026 candidate* zones); extending to earlier years needs finding each
year's own item id the same way this one was found -- the DCAT feed lists "Elections 2010
results poll by poll" and "Ottawa 2018 Election Results" as `Web Page` too, un-investigated.
"""
from __future__ import annotations

import argparse
import io
import pathlib
import re
import sys

sys.path.insert(0, str(pathlib.Path(__file__).parent.parent))
import warehouse  # noqa: E402
from _http import get  # noqa: E402

ARCGIS_ITEM_DATA = "https://www.arcgis.com/sharing/rest/content/items/{item_id}/data"

# One entry per election year wired up. Each item id was found by rendering the hub's
# landing page in a real browser and reading the resulting item-metadata XHR -- not
# guessed, not derived from a pattern (ArcGIS item ids are opaque GUIDs).
ELECTIONS = {
    2022: {
        "item_id": "ec1423ac43254bff8692fabd5d47772b",
        "source_url": "https://open.ottawa.ca/documents/ottawa::2022-elections-official-results",
    },
}

# Header labels recognized as meta fields rather than a candidate name. Matched
# case-insensitively against the first line of the (possibly multi-line, bilingual) header
# cell, since openpyxl returns the literal cell text including the embedded newline before
# the French translation.
META_LABELS = {
    "precinct": "precinct",
    "times cast": "times_cast",
    "registered voters": "registered_voters",
    "undervotes": "undervotes",
    "overvotes": "overvotes",
    "total votes": "total_votes",
}


def _label_key(cell) -> str | None:
    """The English half of a bilingual header cell ("Times Cast /\\nNombre de votes
    exprimés" -> "times cast"), lowercased. Split on "/" first, not "\\n" first -- the
    French half sometimes starts on the same line ("Precinct / Circonscription") and
    sometimes after a newline, but the "/" separator is always there."""
    if not cell:
        return None
    english = str(cell).split("/")[0].strip().lower()
    return english or None


def _sheet_races(sheet_names: list[str]) -> list[tuple[str, str, int | None]]:
    """(sheet_name, race, ward_number) for every sheet this ingester handles."""
    out = []
    for name in sheet_names:
        if name == "Mayor_Maire":
            out.append((name, "Mayor", None))
            continue
        m = re.match(r"Ward_quartier_(\d+)$", name)
        if m:
            out.append((name, "Councillor", int(m.group(1))))
    return out


def parse_workbook(data: bytes, year: int) -> tuple[list[dict], list[dict]]:
    """Returns (poll_rows, total_rows) -- see the module docs on why they share a schema."""
    import openpyxl

    wb = openpyxl.load_workbook(io.BytesIO(data), read_only=True, data_only=True)
    races = _sheet_races(wb.sheetnames)
    if not races:
        raise RuntimeError(f"no Mayor/Ward sheets found among {wb.sheetnames}")

    polls, totals = [], []
    for sheet_name, race, ward in races:
        ws = wb[sheet_name]
        rows = ws.iter_rows(values_only=True)
        header = None
        for row in rows:
            if _label_key(row[0]) == "precinct":
                header = row
                break
        if header is None:
            raise RuntimeError(f"{sheet_name}: no header row found (looked for 'Precinct')")

        # column index -> field name. Meta columns win their canonical name; the first
        # "precinct" duplicate (col 6 in the ward sheets) is dropped as a repeat, not a
        # second field, by relying on dict overwrite semantics never applying here (real
        # candidate columns never collide with a meta label).
        col_field: dict[int, str] = {}
        candidate_cols: list[int] = []
        seen_precinct = False
        for i, cell in enumerate(header):
            key = _label_key(cell)
            if key is None:
                continue
            if key in META_LABELS:
                if key == "precinct":
                    if seen_precinct:
                        continue  # the repeated "Precinct" column before the candidates
                    seen_precinct = True
                col_field[i] = META_LABELS[key]
            else:
                col_field[i] = str(cell).split("\n")[0].strip()
                candidate_cols.append(i)

        for row in rows:
            times_cast = row[[c for c, f in col_field.items() if f == "times_cast"][0]]
            if not isinstance(times_cast, (int, float)):
                continue  # a hierarchy label row ("City / Ville"), not a real data row
            precinct_col = [c for c, f in col_field.items() if f == "precinct"][0]
            precinct = str(row[precinct_col])
            is_total = bool(re.search(r"-\s*Total\s*$", precinct, re.I))
            base = {
                "year": year,
                "race": race,
                "ward": ward,
                "precinct": precinct,
                "is_total": is_total,
            }
            for c, field in col_field.items():
                if c in candidate_cols or field == "precinct":
                    continue  # candidates stay in the long-format candidate/votes pair below
                base[field] = row[c] if c < len(row) else None
            (totals if is_total else polls).extend(
                [
                    {**base, "candidate": str(header[c]).split("\n")[0].strip(), "votes": row[c]}
                    for c in candidate_cols
                    if c < len(row) and row[c] is not None
                ]
            )
    return polls, totals


def main() -> None:
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("--year", type=int, default=2022, choices=sorted(ELECTIONS))
    ap.add_argument("--list", action="store_true", help="parse and summarize, register nothing")
    args = ap.parse_args()

    spec = ELECTIONS[args.year]
    print(f"downloading item {spec['item_id']} ({args.year} Statement of Votes Cast)...")
    data = get(ARCGIS_ITEM_DATA.format(item_id=spec["item_id"]))
    print(f"  {len(data):,} bytes")

    polls, totals = parse_workbook(data, args.year)
    print(f"  {len(polls):,} poll x candidate rows, {len(totals):,} ward/mayor-total x candidate rows")

    if args.list:
        races = sorted({(r["race"], r["ward"]) for r in totals})
        for race, ward in races:
            label = race if ward is None else f"{race} ward {ward}"
            print(f"    {label}")
        return

    import pandas as pd

    warehouse.register(
        f"election_results_{args.year}_polls",
        pd.DataFrame(polls),
        source_id="election-results-history",
        shape="arcgis-hub",
        title=f"{args.year} municipal election — poll-by-poll results",
        origin_url=spec["source_url"],
        notes="One row per (precinct, candidate). Mayor + 24 ward Councillor races only -- "
        "not school-board trustee zones or Declined/Rejected Ballots. See module docstring.",
    )
    warehouse.register(
        f"election_results_{args.year}_totals",
        pd.DataFrame(totals),
        source_id="election-results-history",
        shape="arcgis-hub",
        title=f"{args.year} municipal election — race totals by candidate",
        origin_url=spec["source_url"],
        notes="One row per (race, candidate) -- the city-wide total for Mayor, or the "
        "ward-wide total for each Councillor race. Derived from the same file's own "
        "'- Total' rows, not re-summed here.",
    )


if __name__ == "__main__":
    main()
