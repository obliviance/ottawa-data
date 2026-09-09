#!/usr/bin/env python3
"""Stage 3 verification: confirm the access tag and the licence for each source.

Stages 0-2 established that a URL resolves and whether a machine-readable surface exists.
Stage 3 answers the two questions the access tag actually encodes:

  1. Licence - what may you do with the data? Resolved by operator: fetch each umbrella
     licence page once, confirm what it says, then attach it to every source that operator
     runs. Sources with no open licence (advocacy sites, newsrooms, CanLII) are marked so.

  2. Access - is `Bulk` a real download, is `API` a real endpoint? Signals combined:
       - the Stage 0-1 fingerprint (an ArcGIS / CKAN / GTFS probe that matched)
       - the Stage 2 discovered_apis (an XHR that returned data)
       - for ArcGIS Hub datasets: the DCAT feed's per-dataset `distribution` list, which
         names the exact formats (CSV / GeoJSON / Shapefile / KML / GeoServices API)
       - for plain pages: download links in the HTML (.csv .xlsx .zip .geojson .kml ...)
     The observed set is compared with the claimed `access`; mismatches are flagged.

`Request` (FOI / in-person / written) cannot be checked automatically and is passed through.

    python3 verify_stage3.py                 # every source
    python3 verify_stage3.py --only fir ncc

Output: verification_stage3.json
"""
from __future__ import annotations

import argparse
import datetime as dt
import json
import pathlib
import re
import sys

sys.path.insert(0, str(pathlib.Path(__file__).parent))
from verify import fetch_retry, _json, _origin  # noqa: E402
from verify_stage2 import redact  # noqa: E402  (query-string credential redaction)

ROOT = pathlib.Path(__file__).parent
REPO = ROOT.parent
NOW = dt.datetime.now(dt.timezone.utc).replace(microsecond=0)

# operator name fragment  ->  licence key
OPERATOR_LICENCE = [
    ("City of Ottawa", "ogl-ottawa"),
    ("Ottawa Police", "ogl-ottawa"),
    ("OC Transpo", "ogl-ottawa"),
    ("ServiceOttawa", "ogl-ottawa"),
    ("Ottawa Public Health", "ogl-ottawa"),
    ("Ottawa Public Library", "ogl-ottawa"),
    ("Ottawa Neighbourhood Study", "ons-terms"),
    ("Ottawa Riverkeeper", "site-terms"),
    ("Municipal Property Assessment", "mpac-terms"),
    ("Government of Ontario", "ogl-ontario"),
    ("Ontario Ministry", "ogl-ontario"),
    ("Ontario Land Tribunal", "ogl-ontario"),
    ("Ontario", "ogl-ontario"),
    ("Statistics Canada", "statcan-licence"),
    ("Government of Canada", "ogl-canada"),
    ("National Capital Commission", "ogl-canada"),
    ("Wikipedia", "cc-by-sa"),
    ("CanLII", "canlii-terms"),
    ("Alliance to End Homelessness", "site-terms"),
    ("Horizon Ottawa", "site-terms"),
    ("ACORN", "site-terms"),
    ("Ottawa Lookout", "copyright-reserved"),
    ("Independent", "site-terms"),
    ("Volunteer community", "varies"),
]

# licence key -> (name, url to confirm, keyword that must appear on that page)
LICENCES = {
    "ogl-ottawa": ("Open Government Licence – City of Ottawa",
                   "https://open.ottawa.ca/pages/licence", "licen"),
    "ogl-ontario": ("Open Government Licence – Ontario",
                    "https://www.ontario.ca/page/open-government-licence-ontario", "licen"),
    "ogl-canada": ("Open Government Licence – Canada",
                   "https://open.canada.ca/en/open-government-licence-canada", "licen"),
    "statcan-licence": ("Statistics Canada Open Licence",
                        "https://www.statcan.gc.ca/en/reference/licence", "licen"),
    "cc-by-sa": ("CC BY-SA 4.0 (text)", "https://creativecommons.org/licenses/by-sa/4.0/", "attribution"),
    "canlii-terms": ("CanLII Terms of Use – reproduction restricted",
                     "https://www.canlii.org/en/info/terms.html", "terms"),
    "ons-terms": ("Ottawa Neighbourhood Study – terms of use",
                  "https://www.neighbourhoodstudy.ca/", ""),
    "mpac-terms": ("MPAC – access-restricted; aggregate roll only", "https://www.mpac.ca/", ""),
    "site-terms": ("Site terms – no open-data licence stated", "", ""),
    "copyright-reserved": ("All rights reserved (journalism)", "", ""),
    "varies": ("Varies by project", "", ""),
}

DOWNLOAD_RE = re.compile(
    r'href=["\']([^"\']+\.(?:csv|xlsx?|zip|geojson|json|kml|kmz|shp|gml|xml|txt|ods|rdf))["\']', re.I)
DOWNLOAD_WORD_RE = re.compile(r'\b(download|télécharger|export|\.csv|geojson|shapefile)\b', re.I)


def confirm_licences() -> dict:
    out = {}
    for key, (name, url, kw) in LICENCES.items():
        rec = {"name": name, "url": url, "confirmed": None, "evidence": None}
        if url and kw:
            r = fetch_retry(url, max_body=120_000)
            body = r["body"].decode("utf-8", "replace").lower()
            if r["status"] in (401, 403, 429):
                rec["confirmed"] = None
                rec["evidence"] = f"page bot-blocked (HTTP {r['status']}); licence name is well-known"
            else:
                rec["confirmed"] = r["status"] == 200 and kw in body
                m = re.search(r"(open government licence|licence ouverte)[^<\n]{0,60}", body)
                rec["evidence"] = (m.group(0) if m else f"HTTP {r['status']}")[:120]
        out[key] = rec
    return out


def licence_for(operator: str) -> str:
    for frag, key in OPERATOR_LICENCE:
        if frag.lower() in operator.lower():
            return key
    return "site-terms"


def hub_distributions(dcat: dict) -> dict:
    """title (lowered) -> sorted set of distribution formats, from a DCAT feed."""
    out = {}
    for ds in dcat.get("dataset", []):
        fmts = sorted({x.get("format") for x in ds.get("distribution", []) if x.get("format")})
        out[ds["title"].lower().strip()] = fmts
    return out


DCAT_CACHE: dict[str, dict] = {}


def dcat_for(url: str) -> dict | None:
    origin = _origin(url)
    if origin not in DCAT_CACHE:
        r = fetch_retry(origin + "/api/feed/dcat-us/1.1.json", max_body=6_000_000)
        j = _json(r)
        DCAT_CACHE[origin] = hub_distributions(j) if isinstance(j, dict) else {}
    return DCAT_CACHE[origin] or None


def observe_access(src: dict, fp01: dict, s2: dict | None) -> tuple[list[str], list[str]]:
    """Return (observed access tags, evidence lines)."""
    obs, ev = set(), []

    # Stage 0-1: a probe that matched a machine-readable surface
    for u in fp01.get("urls", []):
        for p in (u.get("fingerprint") or {}).get("probes", []):
            if p.get("matched"):
                obs.add("api")
                if any(w in p["result"] for w in ("CKAN", "Socrata", "DCAT", "catalogue")):
                    obs.add("bulk")
                ev.append(f"stage0-1 probe: {p['result']}")

    # Stage 2: a discovered data endpoint
    if s2:
        for u in s2.get("url_results", []):
            for a in u.get("discovered_apis", []):
                obs.add("api")
                ev.append(f"stage2 XHR: {a['method']} {redact(a['url'])[:130]}")

    # ArcGIS Hub: read the real distribution list for this source's datasets
    reached = {u["url"] for u in fp01.get("urls", [])
               if u.get("outcome") not in ("dead", "error")}
    for url in src["urls"]:
        is_dataset = "/datasets/" in url or "hub.arcgis.com" in url
        if ("open.ottawa.ca" in url or "hub.arcgis.com" in url) and url in reached:
            dists = dcat_for(url)
            if dists:
                slug = re.sub(r"[^a-z0-9]+", " ", src["name"].lower()).strip()
                hits = [f for t, fs in dists.items()
                        if slug[:18] in t or t in slug for f in fs]
                fmts = sorted(set(hits))
                if fmts:
                    ev.append(f"DCAT distributions: {fmts}")
                    if any("API" in f or "GeoServices" in f for f in fmts):
                        obs.add("api")
                    if any(f in ("CSV", "GeoJSON", "ZIP", "KML", "Shapefile") for f in fmts):
                        obs.add("bulk")
                elif is_dataset:
                    obs.update({"api", "bulk"})
                    ev.append("ArcGIS Hub dataset page (CSV/GeoJSON/Shapefile/KML + GeoServices API by default)")

    # plain HTML: look for download links
    rollup01 = fp01.get("rollup")
    if not obs and rollup01 in ("reachable_html", "pdf"):
        r = fetch_retry(src["urls"][0], max_body=400_000)
        body = r["body"].decode("utf-8", "replace")
        ct = r["headers"].get("content-type", "")
        dls = DOWNLOAD_RE.findall(body)
        if dls:
            obs.add("bulk")
            ev.append(f"download links: {sorted({d.split('.')[-1].lower() for d in dls})}")
        elif ct.startswith("application/pdf"):
            obs.add("html")
            ev.append("serves a PDF")
        else:
            obs.add("html")
            if DOWNLOAD_WORD_RE.search(body):
                ev.append("page mentions 'download' but no direct data link found")

    # any reachable web page satisfies "html"; backfill it so its absence isn't flagged
    if "html" not in obs:
        for u in fp01.get("urls", []):
            if u.get("outcome") in ("reachable_html", "needs_browser", "blocked", "pdf"):
                obs.add("html")
                break
    if not obs:
        obs.add("html")
    return sorted(obs), ev


def verdict(claimed: list[str], observed: list[str]) -> str:
    c, o = set(claimed), set(observed)
    missing = c - o - {"html"}          # "html" is satisfiable by any reachable page
    extra = o - c - {"html"}
    if "request" in c and missing <= {"request"} and not extra:
        return "unconfirmed (Request / FOI / in-person — not auto-verifiable)"
    if o == {"html"} and missing:
        return ("unconfirmed — page is HTML; claimed " + ", ".join(f"`{x}`" for x in sorted(missing))
                + " needs a key / login / manual check")
    if not missing and not extra:
        return "confirmed"
    if extra and not missing:
        return "understated — also found " + ", ".join(f"`{x}`" for x in sorted(extra))
    if missing and not extra:
        if missing <= {"request"}:
            return "confirmed (Request part not auto-verifiable)"
        return "overstated — claimed " + ", ".join(f"`{x}`" for x in sorted(missing)) + " not observed"
    return "mixed — claimed " + "/".join(sorted(c)) + ", observed " + "/".join(sorted(o))


def main() -> None:
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("--only", nargs="+", metavar="ID")
    args = ap.parse_args()

    data = json.loads((REPO / "sources.json").read_text())
    stage01 = json.loads((REPO / "verification" / "verification.json").read_text())["sources"]
    s2path = REPO / "verification" / "verification_stage2.json"
    stage2 = json.loads(s2path.read_text())["sources"] if s2path.exists() else {}

    print("confirming umbrella licences ...")
    licences = confirm_licences()
    for k, v in licences.items():
        flag = {True: "ok", False: "FAIL", None: "-"}[v["confirmed"]]
        print(f"  [{flag:>4}] {k:18} {v['name']}")

    sources = {}
    todo = [s for s in data["sources"] if not args.only or s["id"] in args.only]
    print(f"\nchecking access + licence for {len(todo)} sources ...\n")
    for src in todo:
        sid = src["id"]
        lkey = licence_for(src["operator"])
        observed, ev = observe_access(src, stage01.get(sid, {}), stage2.get(sid))
        v = verdict(src["access"], observed)
        sources[sid] = {
            "name": src["name"],
            "operator": src["operator"],
            "claimed_access": src["access"],
            "observed_access": observed,
            "access_verdict": v,
            "licence_key": lkey,
            "licence": licences[lkey]["name"],
            "evidence": ev[:6],
        }
        mark = "  " if v == "confirmed" or v.startswith("confirmed") else "**"
        print(f" {mark} {sid:26} claim {src['access']} -> {observed:}  [{v}]")

    out = {
        "generated_at": NOW.isoformat(),
        "tool": "verify_stage3.py 0.1 (access-tag + licence confirmation)",
        "licences": licences,
        "sources": sources,
    }
    (REPO / "verification" / "verification_stage3.json").write_text(json.dumps(out, indent=2, ensure_ascii=False) + "\n")

    verdicts = [s["access_verdict"] for s in sources.values()]
    print("\n" + "-" * 60)
    for kind in ("confirmed", "understated", "overstated", "unconfirmed"):
        n = sum(1 for x in verdicts if x.startswith(kind) or (kind == "confirmed" and x.startswith("confirmed")))
        if n:
            print(f"  {kind:14}: {n}")
    print("\nwrote verification_stage3.json")


if __name__ == "__main__":
    main()
