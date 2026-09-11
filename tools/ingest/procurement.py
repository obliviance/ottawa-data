#!/usr/bin/env python3
"""Normalise the city's contract-award releases into one table: `procurement_awards`.

    python3 tools/ingest/procurement.py            # rebuild from what's in the warehouse
    python3 tools/ingest/procurement.py --list     # just show what it found

Unlike the other modules in this folder this one fetches nothing. Open Ottawa
publishes contract awards as a *new dataset every six months* -- already pulled
in by `arcgis_hub.py` -- and each drop is the same table with different column
spellings, because ArcGIS mangles field names differently every time:

    Amount / F_Amount_ / $ Amount          Item / Item_ / Item__
    Professional_Consulting_Service        Professional__Consulting_Servic
    Professional_Consulting_Services       Professional_Services_Designati
    Contract_Approval_Request_Type         Contract_Approval__Request_Type

So this discovers the releases by pattern rather than by a hard-coded list, maps
whatever spelling arrived onto a stable schema, and registers the union. When
the next half-year lands, re-run `arcgis_hub.py` then this, and nothing here
needs editing.

Two streams are published in parallel and both are kept:
  * all-departments delegated-authority / >$25k awards
  * Transit Commission delegated-authority awards
They are near-disjoint (2-3 shared contract numbers per period, deduped below),
so the union is the whole picture rather than a double count.
"""
from __future__ import annotations

import argparse
import pathlib
import re
import sys

sys.path.insert(0, str(pathlib.Path(__file__).parent.parent))
import warehouse  # noqa: E402

# A contract-award release, as opposed to any other dataset with "contract" in
# the title (e.g. a construction project list).
IS_AWARD_RELEASE = re.compile(r"contracts?[ _](awarded|for)", re.I)

H2_MARKERS = ("jul", "aug", "sep", "oct", "nov", "dec", "q3", "q4")
H1_MARKERS = ("jan", "feb", "mar", "apr", "may", "jun", "q1", "q2")


def canonical(column: str) -> str | None:
    """Map one release's column name onto the stable schema, or None to drop it."""
    c = column.lower().strip("_").replace("__", "_")
    if c.startswith("item"):
        return "item_no"
    # Must precede the bare "contract" test: the approval-type column also
    # starts with "contract".
    if c.startswith("contract_approval") or "request_type" in c:
        return "approval_type"
    if c.startswith("contract"):
        return "contract_no"
    if c.startswith("professional"):
        return "professional_service"
    if c in ("amount", "f_amount"):
        return "amount_raw"
    if c.startswith("non_competitive"):
        return "noncompetitive_clause"
    if c in ("department", "description", "vendor", "service"):
        return c
    return None  # ObjectId, FID, geometry and friends


def parse_period(*texts: str) -> tuple[int | None, str | None]:
    """(year, 'H1'|'H2') from a dataset title or id.

    Titles are inconsistent enough that this reads them all: "2025 Contracts
    Awarded greater than 25,000 Jul - Dec", "Contracts awarded under DA January
    1 2023 to June 30 2023", "Transit Contracts awarded under DOA Q3 and Q4
    2022". Note the en-dash in one of the 2024 titles.
    """
    blob = " ".join(t for t in texts if t).lower()
    years = [int(y) for y in re.findall(r"\b((?:19|20)\d{2})\b", blob)]
    year = max(years) if years else None

    h1 = any(m in blob for m in H1_MARKERS)
    h2 = any(m in blob for m in H2_MARKERS)
    half = "H1" if h1 and not h2 else "H2" if h2 and not h1 else None
    return year, half


def clean(series):
    """Collapse the newlines ArcGIS leaves inside cell values."""
    return (series.astype(str)
            .str.replace(r"\s+", " ", regex=True)
            .str.strip()
            .replace({"nan": "", "None": "", "<NA>": ""}))


def find_releases() -> list[dict]:
    manifest = warehouse._load_manifest()
    datasets = manifest["datasets"]
    items = datasets.items() if isinstance(datasets, dict) else \
        ((d["dataset_id"], d) for d in datasets)

    found = []
    for dataset_id, meta in items:
        title = meta.get("title", "")
        if not IS_AWARD_RELEASE.search(f"{dataset_id} {title}"):
            continue
        year, half = parse_period(title, dataset_id)
        found.append({
            "dataset_id": dataset_id,
            "title": title.strip(),
            "year": year,
            "half": half,
            "rows": meta.get("rows"),
            "transit": bool(re.search(r"transit", f"{dataset_id} {title}", re.I)),
        })
    return sorted(found, key=lambda r: (r["year"] or 0, r["half"] or "", r["dataset_id"]))


def build(releases: list[dict]):
    import pandas as pd

    con = warehouse.con()
    frames = []
    for rel in releases:
        df = con.execute(f'SELECT * FROM {warehouse._view_name(rel["dataset_id"])}').df()
        mapping = {c: canonical(c) for c in df.columns}
        df = df[[c for c, v in mapping.items() if v]].rename(columns=mapping)
        df["period_year"] = rel["year"]
        df["period_half"] = rel["half"]
        df["stream"] = "transit-commission" if rel["transit"] else "all-departments"
        df["source_dataset"] = rel["dataset_id"]
        frames.append(df)
    con.close()

    awards = pd.concat(frames, ignore_index=True)

    for col in ("contract_no", "vendor", "department", "description",
                "approval_type", "noncompetitive_clause", "professional_service",
                "service", "item_no"):
        if col in awards.columns:
            awards[col] = clean(awards[col])

    # "Follow?On" is a mojibake'd en-dash; "Initial and Amendment" and
    # "Initial & Amendment" are the same thing typed twice.
    awards["approval_type"] = (awards["approval_type"]
                               .str.replace("?", "-", regex=False)
                               .str.replace(" and ", " & ", regex=False))

    awards["amount"] = pd.to_numeric(
        awards["amount_raw"].astype(str).str.replace(r"[^0-9.\-]", "", regex=True),
        errors="coerce")
    awards = awards.drop(columns=["amount_raw"])

    # Every non-competitive award cites a clause of Procurement By-law s.22(1).
    awards["is_noncompetitive"] = awards["noncompetitive_clause"].str.match(
        r"section\s*22", case=False, na=False)
    awards["clause"] = (awards["noncompetitive_clause"]
                        .str.extract(r"\(\s*([A-Za-z])\s*\)\s*$", expand=False)
                        .str.upper())

    awards["period"] = (awards["period_year"].astype("Int64").astype(str)
                        + " " + awards["period_half"].fillna("?"))

    # The two streams share 2-3 contracts per period. Identical rows are the
    # same award reported twice, not two awards of the same value.
    before = len(awards)
    awards = awards.drop_duplicates(
        subset=["contract_no", "approval_type", "vendor", "amount"], keep="first")
    deduped = before - len(awards)

    awards = awards.sort_values(["period_year", "period_half", "contract_no"],
                                na_position="last").reset_index(drop=True)
    return awards, deduped


def main() -> None:
    ap = argparse.ArgumentParser(description=__doc__,
                                 formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("--list", action="store_true",
                    help="show the releases found and exit")
    args = ap.parse_args()

    releases = find_releases()
    if not releases:
        sys.exit("no contract-award releases in the warehouse -- run "
                 "tools/ingest/arcgis_hub.py first")

    print(f"{len(releases)} contract-award releases:")
    for r in releases:
        period = f'{r["year"]} {r["half"]}' if r["year"] else "period unknown"
        print(f'  {period:<14} {str(r["rows"]):>6} rows  '
              f'{"transit" if r["transit"] else "all-depts":<10} {r["title"][:56]}')
    if args.list:
        return

    awards, deduped = build(releases)
    unknown = awards["period_half"].isna().sum()

    warehouse.register(
        "procurement_awards", awards, shape="derived",
        source_id="procurement",
        title="Ottawa contract awards, normalised across half-year releases",
        origin_url="https://open.ottawa.ca/search?q=contracts%20awarded",
        notes=("union of the half-year contract-award releases with column "
               "names normalised; amount parsed to numeric; s.22(1) clause "
               "extracted. One row = one award action (initial, amendment or "
               "extension), so a contract amended twice appears three times."))

    print(f"\nprocurement_awards: {len(awards):,} award actions, "
          f"{awards.contract_no.nunique():,} distinct contracts, "
          f"${awards.amount.sum()/1e9:.2f}B")
    print(f"  {awards.is_noncompetitive.sum():,} non-competitive "
          f"({awards.is_noncompetitive.mean():.1%}), "
          f"{awards.vendor.nunique():,} vendors, "
          f"periods {awards.period_year.min()}-{awards.period_year.max()}")
    if deduped:
        print(f"  {deduped} duplicate row(s) dropped across the two streams")
    if unknown:
        print(f"  WARNING: {unknown} rows have no parseable period")


if __name__ == "__main__":
    main()
