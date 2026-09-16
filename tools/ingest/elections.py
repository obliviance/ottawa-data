#!/usr/bin/env python3
"""The 2026 municipal election roster, from the city's own election web service.

    python3 tools/ingest/elections.py           # fetch and register
    python3 tools/ingest/elections.py --list    # preview, write nothing

`elections.ottawa.ca` runs an unauthenticated JSON web service at `/ws/api/`.
The recon sweep recorded `candidate-list` as html-only with "no backing data
API" -- that render happened *before nominations opened*, so the page was an
empty shell and no XHR ever fired. The endpoint is discoverable in the page
source as `var dataWebServiceURI`.

Two lessons worth keeping: a source sampled at a dead moment gets classified
wrong, and re-probing costs seconds where writing a parser costs a day. Re-probe
before you parse.

Registers five tables:

    election_candidates       one row per candidate (mayor / councillor / trustee)
    election_candidate_links  one row per website or social link
    election_wards            ward reference, including 99 = City Wide
    election_school_boards    school board reference
    election_trustee_zones    zone -> ward crosswalk, exploded from ZoneWards

The crosswalk is the non-obvious one. Trustee zones cover several wards each
("05, 06, 21"), and the city publishes that only as a string inside each
candidate record -- so "which trustees is a voter in ward 6 choosing between"
is not answerable anywhere else without this explosion.

Nomination day was 2026-08-21 and voting day is 2026-10-26, so this roster is
final. After the election it becomes the historical record of who ran.
"""
from __future__ import annotations

import argparse
import pathlib
import re
import sys

sys.path.insert(0, str(pathlib.Path(__file__).parent.parent))
import warehouse  # noqa: E402
from _http import get_json  # noqa: E402

API = "https://elections.ottawa.ca/ws/api/"

# Offices, and the endpoint each is served from. The API splits them because
# they have different shapes -- councillors carry a ward, trustees carry a zone
# and a school board, mayors carry neither.
OFFICES = {
    "mayor": "Candidates/Mayors/",
    "councillor": "Candidates/Councillors/",
    "trustee": "Candidates/Trustees/",
}

# The API returns social links as an HTML anchor in the "Name" field rather than
# a bare URL, e.g. '<a href="https://..." target ="_blank">https://...</a>'.
HREF = re.compile(r'href\s*=\s*"([^"]+)"', re.I)

# Candidates who typed "facebook.com/myname" into a field the city's form then
# prefixes end up with a doubled domain and a dead link:
#   https://www.facebook.com/facebook.com/votechelseawalton
# Eight of the 268 filed links are broken this way. Repairing them matters
# because these render as clickable links under a named candidate.
DOUBLED = re.compile(r"(https?://(?:www\.)?([a-z0-9-]+\.[a-z]+))/(?:www\.)?\2/", re.I)


def clean(value) -> str:
    """Empty-ish API values arrive as None, '' or whitespace. Normalise to ''."""
    if value is None:
        return ""
    return re.sub(r"\s+", " ", str(value)).strip()


def link_url(entry: dict) -> str:
    """The URL out of a SocialMediaInfo entry, whether or not it is wrapped."""
    name = clean(entry.get("Name"))
    match = HREF.search(name)
    url = match.group(1).strip() if match else (name if name.startswith("http") else "")
    return DOUBLED.sub(r"\1/", url) if url else ""


def fetch() -> dict:
    return {
        "wards": get_json(API + "Wards/"),
        "school_boards": get_json(API + "SchoolBoards/"),
        **{office: get_json(API + path) for office, path in OFFICES.items()},
    }


def build(raw: dict):
    import pandas as pd

    candidates, links = [], []
    for office in OFFICES:
        for c in raw[office]:
            cid = c["Id"]
            candidates.append({
                "candidate_id": cid,
                "office": office,
                "name": clean(c.get("Name")),
                # Councillors only. Mayors are city-wide; trustees run by zone.
                "ward_number": c.get("WardNumber"),
                "ward_name": clean(c.get("WardName")),
                # Trustees only.
                "zone_number": c.get("ZoneNumber"),
                "zone_wards": clean(c.get("ZoneWards")),
                "school_board": clean(c.get("SchoolBoardName")),
                "school_board_full": clean(c.get("SchoolBoardNameExt")),
                "nomination_date": clean(c.get("NominationDate"))[:10] or None,
                # Whether the candidate opted into the contribution rebate
                # programme -- a public choice, and one of the few structured
                # signals about how a campaign is financed before filings exist.
                "rebate_program": bool(c.get("RebateProgram")),
                "phone": clean(c.get("TelephoneNumber")),
                "email": clean(c.get("EmailAddress")),
                "n_links": len(c.get("SocialMediaInfo") or []),
            })
            for entry in c.get("SocialMediaInfo") or []:
                url = link_url(entry)
                if url:
                    links.append({
                        "candidate_id": cid,
                        "candidate_name": clean(c.get("Name")),
                        "office": office,
                        "link_type": clean(entry.get("SocialMediaType")),
                        "url": url,
                    })

    cand = pd.DataFrame(candidates)
    cand["nomination_date"] = pd.to_datetime(cand["nomination_date"], errors="coerce")
    cand = cand.sort_values(
        ["office", "ward_number", "school_board", "zone_number", "name"],
        na_position="last").reset_index(drop=True)

    wards = pd.DataFrame([{
        "ward_number": w["WardNumber"],
        "ward_name": clean(w.get("Name")),
        "ward_label": clean(w.get("WardName")),
        # 99 is the pseudo-ward the API uses for the city-wide mayoral race.
        "is_city_wide": w["WardNumber"] == 99,
    } for w in raw["wards"]]).sort_values("ward_number").reset_index(drop=True)

    boards = pd.DataFrame([{
        "school_board": clean(b.get("Name")),
        "school_board_full": clean(b.get("SchoolBoardNameExt")),
    } for b in raw["school_boards"]]).sort_values("school_board").reset_index(drop=True)

    # Explode "05, 06, 21" into one row per (board, zone, ward).
    zones = []
    seen = set()
    for c in raw["trustee"]:
        key = (clean(c.get("SchoolBoardName")), c.get("ZoneNumber"))
        if key in seen or key[1] is None:
            continue
        seen.add(key)
        for part in clean(c.get("ZoneWards")).split(","):
            part = part.strip()
            if part.isdigit():
                zones.append({
                    "school_board": key[0],
                    "school_board_full": clean(c.get("SchoolBoardNameExt")),
                    "zone_number": key[1],
                    "ward_number": int(part),
                })
    zones = (pd.DataFrame(zones)
             .sort_values(["school_board", "zone_number", "ward_number"])
             .reset_index(drop=True))

    return cand, pd.DataFrame(links), wards, boards, zones


def main() -> None:
    ap = argparse.ArgumentParser(
        description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("--list", action="store_true",
                    help="print a summary and exit without registering anything")
    args = ap.parse_args()

    raw = fetch()
    cand, links, wards, boards, zones = build(raw)

    print(f"{len(cand)} candidates — " + ", ".join(
        f"{n} {office}" for office, n in cand.office.value_counts().items()))
    print(f"  {len(wards) - 1} wards + city-wide · {len(boards)} school boards · "
          f"{len(links)} links · {len(zones)} zone-ward pairs")

    contested = cand[cand.office == "councillor"].ward_name.value_counts()
    print(f"\n  most contested: " + " · ".join(
        f"{w.split(' - ')[-1]} ({n})" for w, n in contested.head(3).items()))
    acclaimed = [w for w, n in contested.items() if n == 1]
    if acclaimed:
        print(f"  single candidate (acclaimed): "
              + " · ".join(w.split(" - ")[-1] for w in acclaimed))
    print(f"  rebate programme opt-in: {cand.rebate_program.mean():.0%} of candidates")

    if args.list:
        return

    common = dict(source_id="candidate-list", shape="json-api",
                  origin_url="https://elections.ottawa.ca/CandidateList/CandidateList")
    warehouse.register(
        "election_candidates", cand, title="2026 municipal election — certified candidates",
        notes=("from the elections.ottawa.ca /ws/api/ JSON service. Nominations closed "
               "2026-08-21, so the roster is final. ward_number applies to councillors; "
               "trustees use zone_number + school_board; mayors are city-wide."),
        **common)
    warehouse.register(
        "election_candidate_links", links,
        title="2026 municipal election — candidate websites and social links",
        notes="URLs extracted from the HTML anchors the API returns in SocialMediaInfo.",
        **common)
    warehouse.register(
        "election_wards", wards, title="2026 municipal election — ward reference",
        notes="ward 99 is the city-wide pseudo-ward used for the mayoral race.",
        **common)
    warehouse.register(
        "election_school_boards", boards,
        title="2026 municipal election — school board reference", **common)
    warehouse.register(
        "election_trustee_zones", zones,
        title="2026 municipal election — trustee zone to ward crosswalk",
        notes=("exploded from the ZoneWards string on each trustee record; the city "
               "publishes no zone-to-ward table of its own."),
        **common)


if __name__ == "__main__":
    main()
