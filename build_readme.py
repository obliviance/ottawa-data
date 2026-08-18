#!/usr/bin/env python3
"""Regenerate README.md from sources.json.

sources.json is the source of truth. Edit it, then run:

    python3 build_readme.py
"""
import json
import pathlib

ROOT = pathlib.Path(__file__).parent
DATA = json.loads((ROOT / "sources.json").read_text())

TAG = {
    "api": "`API`",
    "bulk": "`Bulk`",
    "html": "`HTML`",
    "request": "`Request`",
}

HEADER = """# ottawa-data

A catalogue of public data and information sources for the governance of Ottawa, Ontario —
electoral, legislative, financial, spatial, operational — grouped by domain and tagged by how
machine-readable each source actually is.

**[`sources.json`](sources.json) is the source of truth.** This README is generated from it by
[`build_readme.py`](build_readme.py). Edit the JSON, then run `python3 build_readme.py`.

## Status: unverified

Every entry was compiled from web search result metadata. The environment used to compile it
blocked all outbound HTTP, so **no URL in this catalogue has been opened and read**. Treat URLs,
and especially the access tags, as leads to verify rather than confirmed facts.

Entries with `"verify": true` in the JSON are ones with specific known doubts; they are marked
with a **[verify]** flag below.

Verifying these is the obvious first contribution.

## Access tags

| Tag | Meaning |
| --- | --- |
| `API` | Live queryable endpoint — REST, GTFS-RT, ArcGIS GeoServices, Open311. |
| `Bulk` | Downloadable CSV / GeoJSON / shapefile / XLS. |
| `HTML` | Web pages or PDFs only; requires scraping or parsing. |
| `Request` | On-site, by freedom-of-information request, or by written request. |

"""

GAPS = """
## Where the gaps are

Patterns worth noting when deciding what to build.

1. **Recorded votes are not published as data.** Ontario does not require municipalities to
   publish councillor voting records. Ottawa's votes exist only as prose inside eScribe minutes.
   Every vote tracker in the catalogue is a volunteer or advocacy group re-keying them by hand —
   the clearest unmet need here.

2. **eScribe is a corpus, not an API.** Fourteen years of agendas, minutes and staff reports sit
   behind sequential `DocumentId` integers with no search API, no bulk export, and no structured
   metadata. Everything downstream — votes, spending decisions, planning history — is locked in
   PDFs.

3. **Nothing links the accountability datasets to each other.** The lobbyist registry,
   development applications, campaign contributions and council votes are four separate systems
   with no common identifiers. Joining them is the highest-value and hardest work available.

4. **Spatial data is excellent; textual and financial data is not.** Anything with coordinates
   has a clean GeoJSON endpoint. Anything expressed in prose or dollars is a PDF. That asymmetry
   shapes what is currently easy to build.

5. **Candidate platforms exist nowhere structured.** The city publishes who is running; nobody
   publishes what they propose. There is no comparable-positions dataset for the 2026 election.

## Licence

The catalogue itself (`sources.json`, this README) is offered under CC0 — do what you like with
it. The sources it points at carry their own licences; most City of Ottawa data is under the
Open Government Licence, but check each one.
"""


def main() -> None:
    lines = [HEADER]
    counts = {}
    for src in DATA["sources"]:
        counts[src["category"]] = counts.get(src["category"], 0) + 1

    lines.append("## Contents\n")
    for i, (key, label) in enumerate(DATA["categories"].items(), start=1):
        anchor = label.lower().replace(" ", "-").replace(",", "").replace("&", "")
        lines.append(f"{i}. [{label}](#{i}-{anchor}) — {counts.get(key, 0)} sources")
    lines.append("")

    for i, (key, label) in enumerate(DATA["categories"].items(), start=1):
        lines.append(f"\n## {i}. {label}\n")
        for src in (s for s in DATA["sources"] if s["category"] == key):
            tags = " ".join(TAG[a] for a in src["access"])
            flag = " **[verify]**" if src.get("verify") else ""
            lines.append(f"### {src['name']}{flag}\n")
            lines.append(f"{tags} · *{src['operator']}*\n")
            lines.append(f"{src['description']}\n")
            if src.get("verify_note"):
                lines.append(f"> **Verify:** {src['verify_note']}\n")
            for url in src["urls"]:
                lines.append(f"- <{url}>")
            lines.append("")

    lines.append(GAPS)

    out = "\n".join(lines).rstrip() + "\n"
    (ROOT / "README.md").write_text(out)
    print(f"wrote README.md — {len(DATA['sources'])} sources across {len(DATA['categories'])} categories")


if __name__ == "__main__":
    main()
