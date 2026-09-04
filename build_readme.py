#!/usr/bin/env python3
"""Regenerate README.md from sources.json (+ verification.json if present).

sources.json is the source of truth. Edit it, then run:

    python3 build_readme.py

If verification.json exists (written by verify.py), each entry also gets a one-line
Stage 0-1 check result and the status section is regenerated from it.
"""
import datetime as dt
import json
import pathlib

ROOT = pathlib.Path(__file__).parent
DATA = json.loads((ROOT / "sources.json").read_text())
VERIFY_PATH = ROOT / "verification.json"
VERIFY = json.loads(VERIFY_PATH.read_text()) if VERIFY_PATH.exists() else None

TAG = {
    "api": "`API`",
    "bulk": "`Bulk`",
    "html": "`HTML`",
    "request": "`Request`",
}

ROLLUP_PHRASE = {
    "machine-readable": "reachable — machine-readable surface confirmed",
    "pdf": "reachable — PDF",
    "reachable_html": "reachable (HTML); access tag & licence still need a human check",
    "needs_browser": "reachable but JavaScript-rendered — needs a Stage 2 browser check",
    "blocked": "server refused our client (401/403/429) — check in a browser",
    "error": "every catalogued link is dead or erroring",
    "dead": "every catalogued link is dead or erroring",
}

HEADER_TOP = """# ottawa-data

A catalogue of public data and information sources for the governance of Ottawa, Ontario —
electoral, legislative, financial, spatial, operational — grouped by domain and tagged by how
machine-readable each source actually is.

**[`sources.json`](sources.json) is the source of truth.** This README is generated from it by
[`build_readme.py`](build_readme.py). Edit the JSON, then run `python3 build_readme.py`.

**[`hierarchy.md`](hierarchy.md)** is the companion map: every institution that produces
information about Ottawa's governance and community, arranged as a tree and tagged open / closed /
unknown — including the branches not yet in this catalogue.
"""

STATUS_UNVERIFIED = """
## Status: unverified

Every entry was compiled from web search result metadata. The environment used to compile it
blocked all outbound HTTP, so **no URL in this catalogue has been opened and read**. Treat URLs,
and especially the access tags, as leads to verify rather than confirmed facts.

Entries with `"verify": true` in the JSON are ones with specific known doubts; they are marked
with a **[verify]** flag below.

Verifying these is the obvious first contribution.
"""

ACCESS_TAGS = """
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


def status_section() -> str:
    """The '## Status' block: regenerated from verification.json when it exists."""
    if not VERIFY:
        return STATUS_UNVERIFIED
    s = VERIFY["summary"]
    when = VERIFY["generated_at"][:10]
    by = s.get("sources_by_rollup", {})
    return f"""
## Status: Stage 0–1 checked, {when}

Every entry was first compiled from search-result metadata with no outbound HTTP. A
liveness-and-fingerprint pass ([`verify.py`](verify.py), written to
[`verification.json`](verification.json)) has since **opened every URL** and probed for a
machine-readable surface. It does **not** confirm the access tag or the licence — a page that
loads is not the same as a dataset you can use — so those still need Stage 2 (headless browser)
and Stage 3 (human judgement).

Last run **{when}** over {s['urls']} URLs across {s['sources']} sources:

| Best result for the source | Sources |
| --- | --- |
| Machine-readable surface confirmed (API / bulk / catalogue feed) | {by.get('machine-readable', 0)} |
| Reachable, plain HTML/PDF — tag & licence unverified | {by.get('reachable_html', 0) + by.get('pdf', 0)} |
| Reachable but needs a browser (JavaScript-rendered, or bot-blocked) | {by.get('needs_browser', 0) + by.get('blocked', 0)} |
| Every catalogued link dead or erroring | {by.get('error', 0) + by.get('dead', 0)} |

URL-level totals: {s['machine-readable']} machine-readable · {s['reachable_html']} HTML ·
{s['needs_browser']} JavaScript-rendered · {s.get('blocked', 0)} bot-blocked ·
{s['pdf']} PDF · {s['dead']} dead · {s['error']} erroring.

Entries with `"verify": true` in the JSON carry a specific known doubt and are marked
**[verify]** below.
"""


def verify_line(src_id: str) -> list[str]:
    if not VERIFY:
        return []
    entry = VERIFY["sources"].get(src_id)
    if not entry:
        return []
    when = entry["urls"][0]["checked_at"][:10] if entry["urls"] else VERIFY["generated_at"][:10]
    rollup = entry["rollup"]
    phrase = ROLLUP_PHRASE.get(rollup, rollup)

    detail = ""
    probes = [p["result"] for u in entry["urls"] for p in (u.get("fingerprint") or {}).get("probes", [])
              if p.get("matched")]
    if rollup in ("machine-readable", "pdf") and probes:
        detail = f" — {probes[0]}"

    broken = [u for u in entry["urls"] if u["outcome"] in ("dead", "error")]
    blocked = [u for u in entry["urls"] if u["outcome"] == "blocked"]
    if broken and rollup not in ("dead", "error"):
        detail += (f". {len(broken)} of {len(entry['urls'])} links broken: "
                   + "; ".join(f"{u['url']} → {u['http_status'] or 'no DNS'}" for u in broken))
    if blocked and rollup != "blocked":
        detail += (f". {len(blocked)} link{'s' * (len(blocked) != 1)} bot-blocked "
                   f"(fine in a browser): " + "; ".join(u["url"] for u in blocked))

    out = [f"> _Checked {when} (stage 0–1): {phrase}{detail}_"]
    if broken and rollup in ("dead", "error"):
        for u in broken:
            out.append(">")
            out.append(f"> - `{u['url']}` → {u['error']}")
    return out


def main() -> None:
    lines = [HEADER_TOP, status_section(), ACCESS_TAGS]

    counts = {}
    for src in DATA["sources"]:
        counts[src["category"]] = counts.get(src["category"], 0) + 1

    lines.append("\n## Contents\n")
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
            lines.extend(verify_line(src["id"]))
            for url in src["urls"]:
                lines.append(f"- <{url}>")
            lines.append("")

    lines.append(GAPS)

    out = "\n".join(lines).rstrip() + "\n"
    (ROOT / "README.md").write_text(out)
    extra = f" (+ verification.json, {VERIFY['generated_at'][:10]})" if VERIFY else ""
    print(f"wrote README.md — {len(DATA['sources'])} sources across "
          f"{len(DATA['categories'])} categories{extra}")


if __name__ == "__main__":
    main()
