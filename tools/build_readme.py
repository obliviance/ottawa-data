#!/usr/bin/env python3
"""Regenerate README.md from sources.json, folding in whatever verification has run.

sources.json is the source of truth. Edit it, then run:

    python3 build_readme.py

Optional inputs, each written by its stage's script:
    verification.json         verify.py         stage 0-1  liveness + fingerprint
    verification_stage2.json  verify_stage2.py  stage 2    headless-browser render + XHR
    verification_stage3.json  verify_stage3.py  stage 3    access-tag + licence confirmation
    snapshots.json            snapshot.py       Wayback Machine snapshot per URL
"""
import datetime as dt
import json
import pathlib
import re

ROOT = pathlib.Path(__file__).parent
REPO = ROOT.parent

_SECRET = re.compile(r"((?:access_?token|auth_?key|api_?key|apikey|key|token|sig|signature)=)"
                     r"[^&#`'\" ]+", re.I)


def _safe(s: str) -> str:
    return _SECRET.sub(r"\1<redacted>", s)
DATA = json.loads((REPO / "sources.json").read_text())


def _load(name):
    p = REPO / "verification" / name
    return json.loads(p.read_text()) if p.exists() else None


V1 = _load("verification.json")
V2 = _load("verification_stage2.json")
V3 = _load("verification_stage3.json")
SNAP = _load("snapshots.json")

TAG = {"api": "`API`", "bulk": "`Bulk`", "html": "`HTML`", "request": "`Request`"}

ROLLUP_PHRASE = {
    "machine-readable": "machine-readable surface confirmed",
    "pdf": "serves a PDF",
    "reachable_html": "reachable, server-rendered HTML",
    "needs_browser": "reachable but JavaScript-rendered",
    "blocked": "server refused our client (401/403/429)",
    "error": "every catalogued link dead or erroring",
    "dead": "every catalogued link dead or erroring",
}
S2_PHRASE = {
    "machine-readable": "a real backing data API turned up in the browser",
    "reachable_html": "renders fully — a headless scrape works",
    "needs_browser": "still would not yield content in a browser",
}

HEADER_TOP = """# ottawa-data

A catalogue of public data and information sources for the governance of Ottawa, Ontario —
electoral, legislative, financial, spatial, operational — grouped by domain and tagged by how
machine-readable each source actually is.

**[`sources.json`](sources.json) is the source of truth.** This README is generated from it by
[`tools/build_readme.py`](tools/build_readme.py). Edit the JSON, then run `python3 tools/build_readme.py`.

**[`hierarchy.md`](hierarchy.md)** is the companion map: every institution that produces
information about Ottawa's governance and community, arranged as a tree and tagged open / closed /
unknown — including the branches not yet in this catalogue.

Contributing: [`CLAUDE.md`](CLAUDE.md) for the layout and workflow, [`tools/VERIFYING.md`](tools/VERIFYING.md)
for how sources get verified, [`ROADMAP.md`](ROADMAP.md) for the plan to turn the catalogue into
public-facing work. Scripts in [`tools/`](tools/), verification records in [`verification/`](verification/).
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

Where verification has run, each entry below carries a **Verified** line: the access tag and
licence as confirmed (or corrected), and the stage-by-stage trail. See [`tools/VERIFYING.md`](tools/VERIFYING.md).
"""

GAPS = """
## Where the gaps are

Patterns worth noting when deciding what to build.

1. **Recorded votes are not published as data.** Ontario does not require municipalities to
   publish councillor voting records. Ottawa's votes exist only as prose inside eScribe minutes.
   Every vote tracker in the catalogue is a volunteer or advocacy group re-keying them by hand —
   the clearest unmet need here. (Stage 2 note: `howtheyvoted.ca` ships its compiled record as
   JSON at `/data/ottawa/…`, and is current — a usable secondary source.)

2. **eScribe is a corpus, not an API.** Fourteen years of agendas, minutes and staff reports sit
   behind sequential `DocumentId` integers with no search API, no bulk export, and no structured
   metadata. Everything downstream — votes, spending decisions, planning history — is locked in
   PDFs. (Stage 2 note: the meeting *index* is reachable via
   `MeetingsCalendarView.aspx/GetCalendarMeetings`; the documents still are not.)

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
Open Government Licence – City of Ottawa, but check each one.
"""


def _count(d, key):
    return sum(1 for v in d.values() if key(v))


def status_section() -> str:
    if not V1:
        return STATUS_UNVERIFIED

    s, when1 = V1["summary"], V1["generated_at"][:10]
    by = s.get("sources_by_rollup", {})
    out = [f"""
## Status: verified in stages, through {max(x['generated_at'][:10] for x in (V1, V2, V3) if x)}

Every entry was first compiled from search-result metadata with no outbound HTTP. Verification
runs in stages ([`tools/VERIFYING.md`](tools/VERIFYING.md)); each entry below shows how far it has got.

**Stage 0–1** ([`tools/verify.py`](tools/verify.py), {when1}) — opened every URL and probed for a
machine-readable surface. {s['urls']} URLs / {s['sources']} sources:
{by.get('machine-readable', 0)} machine-readable · {by.get('reachable_html', 0) + by.get('pdf', 0)} plain HTML/PDF ·
{by.get('needs_browser', 0) + by.get('blocked', 0)} JavaScript-rendered or bot-blocked ·
{by.get('error', 0) + by.get('dead', 0)} with a dead link.
"""]

    if V2:
        s2 = V2["sources"]
        mr = _count(s2, lambda v: v["rollup"] == "machine-readable")
        rh = _count(s2, lambda v: v["rollup"] == "reachable_html")
        nb = _count(s2, lambda v: v["rollup"] == "needs_browser")
        apis = sorted({a["url"] for v in s2.values() for u in v["url_results"]
                       for a in u.get("discovered_apis", [])})
        out.append(f"""
**Stage 2** ([`tools/verify_stage2.py`](tools/verify_stage2.py), {V2['generated_at'][:10]}) — rendered the
{len(s2)} JavaScript / interactive sources in a real headless Chromium and captured their XHR.
**{mr}** turned out to have a real backing API (council votes as JSON from `howtheyvoted.ca`,
a REST API behind `devapps`, an EngagementHQ API behind Engage Ottawa, an AJAX meeting index
behind eScribe); **{rh}** render fully and can be scraped headlessly; **{nb}** still would not
yield (ottawa.ca and CanLII intermittently serve a bot challenge to headless browsers).
""")

    if V3:
        s3 = V3["sources"]
        conf = _count(s3, lambda v: v["access_verdict"].startswith("confirmed"))
        under = _count(s3, lambda v: v["access_verdict"].startswith("understated"))
        over = _count(s3, lambda v: v["access_verdict"].startswith("overstated"))
        unc = _count(s3, lambda v: v["access_verdict"].startswith("unconfirmed"))
        ogl = _count(s3, lambda v: v["licence_key"].startswith("ogl") or v["licence_key"] == "statcan-licence")
        out.append(f"""
**Stage 3** ([`tools/verify_stage3.py`](tools/verify_stage3.py), {V3['generated_at'][:10]}) — confirmed the
access tag and resolved the licence. **{conf}** access tags confirmed as-is; **{under}** are
*understated* (more open than the tag claims — usually an ArcGIS/CKAN API behind a "Bulk" or
"HTML" tag); **{over}** overstated; **{unc}** could not be confirmed automatically (needs an API
key, a login, or is a genuine FOI request). Licence resolved by operator: **{ogl}** sources fall
under an Open Government Licence; the rest carry site terms or access restrictions, flagged per
entry.
""")

    if SNAP:
        sn = SNAP["summary"]
        out.append(f"\n**Snapshots** ([`tools/snapshot.py`](tools/snapshot.py), {SNAP['generated_at'][:10]}) — "
                   f"{sn['with_snapshot']}/{sn['urls']} URLs captured to the Wayback Machine.\n")

    out.append('\nEntries with `"verify": true` in the JSON carried a specific known doubt and '
               "are marked **[verify]** below.\n")
    return "".join(out)


def verify_line(src_id: str) -> list[str]:
    if not V1:
        return []
    e1 = V1["sources"].get(src_id)
    if not e1:
        return []
    e2 = V2["sources"].get(src_id) if V2 else None
    e3 = V3["sources"].get(src_id) if V3 else None

    out = []

    # headline: the stage-3 verdict, if we have one
    if e3:
        v = e3["access_verdict"]
        apis = [a["url"] for u in (e2 or {}).get("url_results", []) for a in u.get("discovered_apis", [])]
        hint = f" — e.g. `{_safe(apis[0])}`" if apis and "understated" in v and "api" in v else ""
        out.append(f"> **Verified** — access: {v}{hint}")
        out.append(f"> licence: *{e3['licence']}*")

    # trail: stage 0-1 phrase, stage 2 phrase, broken links
    when1 = e1["urls"][0]["checked_at"][:10] if e1["urls"] else V1["generated_at"][:10]
    bits = [f"stage 0–1 {when1}: {ROLLUP_PHRASE.get(e1['rollup'], e1['rollup'])}"]
    probes = [p["result"] for u in e1["urls"]
              for p in (u.get("fingerprint") or {}).get("probes", []) if p.get("matched")]
    if e1["rollup"] == "machine-readable" and probes:
        bits[0] += f" ({probes[0]})"
    if e2:
        bits.append(f"stage 2 {V2['generated_at'][:10]}: {S2_PHRASE.get(e2['rollup'], e2['rollup'])}")

    broken = [u for u in e1["urls"] if u["outcome"] in ("dead", "error")]
    blocked = [u for u in e1["urls"] if u["outcome"] == "blocked"]
    if broken:
        bits.append("broken — " + "; ".join(
            f"{u['url']} → {u['http_status'] or 'no DNS'}" for u in broken))
    if blocked:
        bits.append(f"{len(blocked)} link{'s' * (len(blocked) != 1)} bot-blocked (fine in a browser)")

    snap_n = 0
    if SNAP:
        snap_n = sum(1 for u in _src_urls(src_id) if SNAP["urls"].get(u, {}).get("snapshot"))
    if snap_n:
        bits.append(f"{snap_n} archived")

    out.append("> _" + " · ".join(bits) + "_")
    return out


def _src_urls(src_id):
    for s in DATA["sources"]:
        if s["id"] == src_id:
            return s["urls"]
    return []


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
    (REPO / "README.md").write_text(out)
    stamps = " + ".join(f"{n} {x['generated_at'][:10]}" for n, x in
                        (("s0-1", V1), ("s2", V2), ("s3", V3), ("snap", SNAP)) if x)
    print(f"wrote README.md — {len(DATA['sources'])} sources across "
          f"{len(DATA['categories'])} categories" + (f" ({stamps})" if stamps else ""))


if __name__ == "__main__":
    main()
