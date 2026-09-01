#!/usr/bin/env python3
"""Stage 0-1 verification harness for sources.json.

The catalogue was compiled from search-result metadata with no outbound HTTP, so every
access tag is a guess. This script does the cheap, automatable part of checking them:

  Stage 0  liveness     GET every URL; record status, redirects, content-type, size, timing.
  Stage 1  fingerprint  probe for a machine-readable surface behind the page:
                          - ArcGIS REST services            (?f=pjson)
                          - ArcGIS Hub / open-data portal    (DCAT / data.json feed)
                          - CKAN                             (/api/3/action/status_show)
                          - Socrata                          (/api/catalog/v1)
                          - Open311 GeoReport v2             (/discovery.json, /services.json)
                          - GTFS / GTFS-Realtime             (zip payload / protobuf feed)
                          - PDF                              (content-type)
                          - single-page app                 (HTML shell, no text -> needs browser)

It does NOT judge the access tag or the licence. That is Stage 2 (headless browser to see
what a SPA actually renders and which XHR it calls) and Stage 3 (human/LLM: is "Bulk" a real
CSV or a Tableau embed, is the licence OGL). URLs this script can't resolve are marked
`needs_browser` or `reachable_html` so a person knows exactly what is left to do.

Output: verification.json  (checked into the repo as the verification record).

Usage:
    python3 verify.py                     # check every URL
    python3 verify.py --only escribe fir  # only these source ids
    python3 verify.py --stale 30          # skip URLs verified OK within the last 30 days
    python3 verify.py --jobs 8            # domains checked in parallel (default 6)
    python3 verify.py --delay 2.0         # seconds between hits on the same domain (default 1.5)
"""
from __future__ import annotations

import argparse
import concurrent.futures
import datetime as dt
import gzip
import io
import json
import pathlib
import random
import re
import ssl
import sys
import time
import urllib.error
import urllib.parse
import urllib.request
import zipfile

ROOT = pathlib.Path(__file__).parent
SOURCES = ROOT / "sources.json"
OUT = ROOT / "verification.json"

UA = "ottawa-data-verify/0.1 (+https://github.com/obliviance/ottawa-data; catalogue verification)"
TIMEOUT = 25
MAX_BODY = 300_000  # bytes read for fingerprinting
CTX = ssl.create_default_context()

NOW = dt.datetime.now(dt.timezone.utc).replace(microsecond=0)


# --------------------------------------------------------------------------- fetch

def fetch(url: str, method: str = "GET", max_body: int = MAX_BODY) -> dict:
    """One HTTP request. Returns a result dict; never raises."""
    req = urllib.request.Request(url, method=method, headers={
        "User-Agent": UA,
        "Accept": "*/*",
        "Accept-Language": "en-CA,en;q=0.9,fr-CA;q=0.5",
    })
    started = time.monotonic()
    try:
        with urllib.request.urlopen(req, timeout=TIMEOUT, context=CTX) as resp:
            raw = resp.read(max_body + 1)
            elapsed = round((time.monotonic() - started) * 1000)
            if resp.headers.get("Content-Encoding", "").lower() == "gzip":
                try:
                    raw = gzip.decompress(raw)
                except OSError:
                    pass
            truncated = len(raw) > max_body
            return {
                "ok": True,
                "status": resp.status,
                "final_url": resp.geturl(),
                "headers": {k.lower(): v for k, v in resp.headers.items()},
                "body": raw[:max_body],
                "truncated": truncated,
                "elapsed_ms": elapsed,
                "error": None,
            }
    except urllib.error.HTTPError as e:
        elapsed = round((time.monotonic() - started) * 1000)
        body = b""
        try:
            body = e.read(max_body)
        except Exception:
            pass
        return {
            "ok": False, "status": e.code, "final_url": e.url or url,
            "headers": {k.lower(): v for k, v in (e.headers or {}).items()},
            "body": body, "truncated": False, "elapsed_ms": elapsed,
            "error": f"HTTP {e.code} {e.reason}",
        }
    except (urllib.error.URLError, TimeoutError, ssl.SSLError, ConnectionError, OSError) as e:
        elapsed = round((time.monotonic() - started) * 1000)
        reason = getattr(e, "reason", e)
        return {
            "ok": False, "status": None, "final_url": url, "headers": {},
            "body": b"", "truncated": False, "elapsed_ms": elapsed,
            "error": f"{type(e).__name__}: {reason}",
        }


def fetch_retry(url: str, **kw) -> dict:
    r = fetch(url, **kw)
    transient = r["error"] and (r["status"] in (429, 500, 502, 503, 504) or r["status"] is None)
    if transient:
        time.sleep(2.5)
        r2 = fetch(url, **kw)
        r2["retried"] = True
        return r2
    return r


# ----------------------------------------------------------------- html helpers

_TAG = re.compile(rb"<[^>]+>")
_SCRIPT = re.compile(rb"<script\b", re.I)
_TITLE = re.compile(rb"<title[^>]*>(.*?)</title>", re.I | re.S)
_WS = re.compile(rb"\s+")


def visible_text_len(body: bytes) -> int:
    body = re.sub(rb"<(script|style|noscript)\b.*?</\1>", b" ", body, flags=re.I | re.S)
    return len(_WS.sub(b" ", _TAG.sub(b" ", body)).strip())


def title_of(body: bytes) -> str | None:
    m = _TITLE.search(body)
    if not m:
        return None
    t = _WS.sub(b" ", _TAG.sub(b" ", m.group(1))).strip().decode("utf-8", "replace")
    return t[:160] or None


def looks_like_spa(body: bytes, content_type: str) -> list[str]:
    if "html" not in content_type:
        return []
    signals = []
    if _SCRIPT.findall(body).__len__() >= 3:
        signals.append("3+ script tags")
    if visible_text_len(body) < 600:
        signals.append("<600 chars visible text")
    for marker in (b'id="root"', b'id="app"', b'__NEXT_DATA__', b'ng-version',
                   b'window.__', b'data-reactroot', b'<app-root'):
        if marker in body:
            signals.append(f"marker {marker.decode()}")
            break
    return signals if len(signals) >= 2 else []


# ------------------------------------------------------------------ fingerprint

def _with_query(url: str, **params) -> str:
    parts = urllib.parse.urlparse(url)
    q = dict(urllib.parse.parse_qsl(parts.query))
    q.update(params)
    return urllib.parse.urlunparse(parts._replace(query=urllib.parse.urlencode(q)))


def _origin(url: str) -> str:
    p = urllib.parse.urlparse(url)
    return f"{p.scheme}://{p.netloc}"


def _probe_fetch(url: str, max_body: int = 400_000) -> dict:
    time.sleep(0.8 + random.uniform(0, 0.3))  # keep probes polite too
    return fetch_retry(url, max_body=max_body)


def _hit(probe: str, r: dict, result: str, matched: bool) -> dict:
    return {"probe": probe, "status": r["status"], "result": result, "matched": matched}


def _json(r: dict):
    ct = r["headers"].get("content-type", "")
    head = r["body"].lstrip()[:1]
    if "json" not in ct and head not in (b"{", b"["):
        return None
    try:
        return json.loads(r["body"].decode("utf-8", "replace"))
    except (ValueError, UnicodeDecodeError):
        return None  # may be a large truncated catalogue - callers fall back to a substring check


def probe_arcgis(url: str) -> dict | None:
    if not re.search(r"/(rest/services|MapServer|FeatureServer|ImageServer)(/|$|\?)", url):
        return None
    target = _with_query(url.split("?")[0], f="pjson")
    r = _probe_fetch(target, max_body=1_500_000)
    j = _json(r)
    if not isinstance(j, dict):
        return _hit(target, r, "no ArcGIS JSON response", False)
    if "services" in j or "folders" in j:
        ns, nf = len(j.get("services", [])), len(j.get("folders", []))
        return _hit(target, r, f"ArcGIS REST catalogue: {ns} service{'s' * (ns != 1)}, "
                    f"{nf} folder{'s' * (nf != 1)}, v{j.get('currentVersion')}", True)
    if "layers" in j or j.get("type") in ("Feature Layer", "Table"):
        return _hit(target, r, f"ArcGIS service '{j.get('name', j.get('mapName', '?'))}': "
                    f"{len(j.get('layers', []))} layers, formats {j.get('supportedQueryFormats', '?')}", True)
    return _hit(target, r, "JSON, but not a recognised ArcGIS shape", False)


def probe_hub(url: str, body: bytes = b"") -> dict | None:
    host = urllib.parse.urlparse(url).netloc
    low = body.lower()
    hub_hint = (b"arcgis" in low and (b"hub" in low or b"opendata" in low)) or b"@esri/hub" in low
    if not (host.startswith("open.") or host.startswith("ouverte.") or host.startswith("data.")
            or "hub.arcgis" in host or "opendata" in host or hub_hint):
        return None
    for feed in ("/api/feed/dcat-us/1.1.json", "/data.json"):
        r = _probe_fetch(_origin(url) + feed, max_body=4_000_000)
        ok = r["status"] == 200 and "json" in r["headers"].get("content-type", "") \
            and b'"dataset"' in r["body"]
        if ok:
            j = _json(r)
            n = len(j["dataset"]) if isinstance(j, dict) and isinstance(j.get("dataset"), list) else None
            return _hit(_origin(url) + feed, r,
                        "ArcGIS Hub DCAT feed present" + (f" ({n} datasets)" if n else " (large catalogue)"),
                        True)
    return _hit(_origin(url) + "/data.json", r, "no DCAT feed", False)


def probe_ckan(url: str) -> dict | None:
    r = _probe_fetch(_origin(url) + "/api/3/action/status_show", max_body=20_000)
    j = _json(r)
    if not (isinstance(j, dict) and j.get("success")):
        return None
    ver = (j.get("result") or {}).get("ckan_version", "?")
    jc = _json(_probe_fetch(_origin(url) + "/api/3/action/package_search?rows=0", max_body=20_000))
    n = (jc or {}).get("result", {}).get("count") if isinstance(jc, dict) else None
    return _hit(_origin(url) + "/api/3/action/", r,
                f"CKAN API v{ver}" + (f", {n} datasets" if n is not None else ""), True)


def probe_socrata(url: str) -> dict | None:
    r = _probe_fetch(_origin(url) + "/api/catalog/v1?limit=0", max_body=20_000)
    j = _json(r)
    if isinstance(j, dict) and "resultSetSize" in j:
        return _hit(_origin(url) + "/api/catalog/v1", r,
                    f"Socrata catalogue API: {j['resultSetSize']} assets", True)
    return None


def probe_open311(url: str) -> dict | None:
    if not re.search(r"(311|open311|georeport)", url, re.I):
        return None
    bases = [url.rstrip("/"), _origin(url) + "/open311/v2", _origin(url) + "/georeport/v2"]
    for base in bases:
        r = _probe_fetch(base + "/discovery.json", max_body=60_000)
        j = _json(r)
        if isinstance(j, (dict, list)):
            s = _probe_fetch(base + "/services.json", max_body=200_000)
            js = _json(s)
            n = len(js) if isinstance(js, list) else "?"
            return _hit(base + "/discovery.json", r,
                        f"Open311 GeoReport v2: discovery ok, {n} service types", True)
    return _hit(url + "/discovery.json", r, "no Open311 discovery endpoint answered", False)


def probe_gtfs(url: str) -> dict | None:
    low = url.lower()
    if not (low.endswith(".zip") or "gtfs" in low):
        return None
    r = _probe_fetch(url, max_body=3_000_000)
    if r["body"][:2] == b"PK":
        try:
            names = set(zipfile.ZipFile(io.BytesIO(r["body"])).namelist())
            core = {"agency.txt", "stops.txt", "routes.txt", "trips.txt", "stop_times.txt"}
            if core & names:
                return _hit(url, r, f"GTFS zip: {len(names)} files, core {sorted(core & names)}", True)
        except zipfile.BadZipFile:
            pass
    ct = r["headers"].get("content-type", "")
    if "protobuf" in ct or "octet-stream" in ct:
        return _hit(url, r, f"binary feed ({ct}) - likely GTFS-Realtime", True)
    return None


NOTE_ONLY = {
    "youtube.com": "video platform - captions via the timedtext API or yt-dlp --write-auto-sub",
    "youtu.be": "video platform - captions via the timedtext API or yt-dlp --write-auto-sub",
    "wikipedia.org": "MediaWiki Action + REST API; text is CC BY-SA",
    "canlii.org": "CanLII REST API exists (free key on request); otherwise HTML",
    "transit.land": "Transitland v2 REST API (feed + operator endpoints)",
}


def fingerprint(url: str, r: dict) -> dict:
    ct = r["headers"].get("content-type", "").lower().split(";")[0].strip()
    fp: dict = {"content_type": ct, "kind": None, "needs_browser": False, "signals": [], "probes": []}

    if ct == "application/pdf" or url.lower().endswith(".pdf"):
        fp["kind"] = "pdf"
        return fp
    if ct in ("application/json", "application/geo+json") or ct.endswith("+json"):
        fp["kind"] = "json-endpoint"

    host = urllib.parse.urlparse(url).netloc
    is_note_host = False
    for suffix, note in NOTE_ONLY.items():
        if host == suffix or host.endswith("." + suffix):
            is_note_host = True
            fp["kind"] = fp["kind"] or "note"
            fp["signals"].append(note)

    for probe in (probe_arcgis, probe_hub, probe_ckan, probe_socrata, probe_open311, probe_gtfs):
        try:
            got = probe(url, r["body"]) if probe is probe_hub else probe(url)
        except Exception as e:  # a probe must never sink the run
            got = {"probe": probe.__name__, "status": None,
                   "result": f"probe error: {e!r}", "matched": False}
        if got:
            fp["probes"].append(got)
            if got.get("matched"):
                fp["kind"] = "machine-readable"

    if fp["kind"] in (None, "html") and "html" in ct and not is_note_host:
        spa = looks_like_spa(r["body"], ct)
        if spa:
            fp["kind"] = "spa"
            fp["needs_browser"] = True
            fp["signals"] += spa
        else:
            fp["kind"] = fp["kind"] or "html"
    fp["kind"] = fp["kind"] or "html"
    return fp


# ------------------------------------------------------------------- per source

ROLLUP_RANK = ["dead", "error", "needs_browser", "reachable_html", "pdf", "machine-readable"]


def check_url(url: str) -> dict:
    r = fetch_retry(url)
    rec = {
        "url": url,
        "checked_at": NOW.isoformat(),
        "http_status": r["status"],
        "final_url": r["final_url"],
        "redirected": r["final_url"].rstrip("/") != url.rstrip("/"),
        "content_type": r["headers"].get("content-type", "").split(";")[0].strip() or None,
        "bytes": int(r["headers"].get("content-length") or len(r["body"])) or None,
        "elapsed_ms": r["elapsed_ms"],
        "server": r["headers"].get("server"),
        "title": title_of(r["body"]) if "html" in r["headers"].get("content-type", "") else None,
        "error": r["error"],
        "retried": r.get("retried", False),
    }
    if r["status"] is None:
        rec["outcome"] = "dead"
        rec["fingerprint"] = None
        return rec
    if r["status"] >= 400:
        rec["outcome"] = "error"
        rec["fingerprint"] = None
        return rec

    fp = fingerprint(r["final_url"], r)
    rec["fingerprint"] = fp
    if fp["kind"] == "machine-readable" or fp["kind"] == "json-endpoint":
        rec["outcome"] = "machine-readable"
    elif fp["kind"] == "pdf":
        rec["outcome"] = "pdf"
    elif fp["needs_browser"]:
        rec["outcome"] = "needs_browser"
    else:
        rec["outcome"] = "reachable_html"
    return rec


def rollup(url_recs: list[dict]) -> str:
    best = "dead"
    for rec in url_recs:
        o = rec["outcome"]
        if ROLLUP_RANK.index(o) > ROLLUP_RANK.index(best):
            best = o
    return best


# ------------------------------------------------------------------------ main

def load_prev() -> dict:
    if OUT.exists():
        try:
            return json.loads(OUT.read_text())
        except ValueError:
            pass
    return {"sources": {}}


def domain_worker(jobs: list[tuple], delay: float) -> list[tuple]:
    out = []
    for i, (sid, url) in enumerate(jobs):
        if i:
            time.sleep(delay + random.uniform(0, 0.4))
        out.append((sid, check_url(url)))
    return out


def main() -> None:
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("--only", nargs="+", metavar="ID", help="only these source ids")
    ap.add_argument("--stale", type=int, metavar="DAYS", help="skip URLs that passed within DAYS")
    ap.add_argument("--jobs", type=int, default=6, help="domains checked in parallel (default 6)")
    ap.add_argument("--delay", type=float, default=1.5, help="seconds between same-domain hits (default 1.5)")
    args = ap.parse_args()

    data = json.loads(SOURCES.read_text())
    prev = load_prev()
    prev_ok: dict[str, str] = {}
    if args.stale:
        cutoff = NOW - dt.timedelta(days=args.stale)
        for s in prev.get("sources", {}).values():
            for u in s.get("urls", []):
                if u.get("outcome") in ("machine-readable", "pdf", "reachable_html") \
                   and dt.datetime.fromisoformat(u["checked_at"]) > cutoff:
                    prev_ok[u["url"]] = u["outcome"]

    by_domain: dict[str, list[tuple]] = {}
    catalogue: dict[str, dict] = {}
    skipped = 0
    for src in data["sources"]:
        if args.only and src["id"] not in args.only:
            continue
        catalogue[src["id"]] = {
            "name": src["name"],
            "claimed_access": src["access"],
            "verify_flag": bool(src.get("verify")),
            "urls": [],
        }
        for url in src["urls"]:
            if url in prev_ok:
                skipped += 1
                old = next(u for u in prev["sources"][src["id"]]["urls"] if u["url"] == url)
                catalogue[src["id"]]["urls"].append(old)
                continue
            by_domain.setdefault(urllib.parse.urlparse(url).netloc, []).append((src["id"], url))

    total = sum(len(v) for v in by_domain.values())
    print(f"checking {total} URLs across {len(by_domain)} domains "
          f"({skipped} skipped as fresh){' - ' + ', '.join(args.only) if args.only else ''}\n")

    with concurrent.futures.ThreadPoolExecutor(max_workers=args.jobs) as ex:
        futs = [ex.submit(domain_worker, jobs, args.delay) for jobs in by_domain.values()]
        done = 0
        for fut in concurrent.futures.as_completed(futs):
            for sid, rec in fut.result():
                catalogue[sid]["urls"].append(rec)
                done += 1
                mark = {"machine-readable": "API ", "pdf": "PDF ", "reachable_html": "html",
                        "needs_browser": "SPA ", "error": "ERR ", "dead": "DEAD"}[rec["outcome"]]
                print(f"  [{done:>3}/{total}] {mark}  {rec['http_status'] or '---'}  {rec['url'][:88]}")

    for sid, entry in catalogue.items():
        entry["urls"].sort(key=lambda u: u["url"])
        entry["rollup"] = rollup(entry["urls"])

    outcomes = [u["outcome"] for e in catalogue.values() for u in e["urls"]]
    summary = {k: outcomes.count(k) for k in ROLLUP_RANK}
    summary["urls"] = len(outcomes)
    summary["sources"] = len(catalogue)
    rollups = [e["rollup"] for e in catalogue.values()]
    summary["sources_by_rollup"] = {k: rollups.count(k) for k in ROLLUP_RANK if rollups.count(k)}

    result = {
        "generated_at": NOW.isoformat(),
        "tool": "verify.py 0.1 (stage 0-1: liveness + fingerprint)",
        "note": "Automated. Confirms reachability and machine-readable surface only. "
                "'needs_browser' and 'reachable_html' rows still need Stage 2 (headless "
                "browser) and Stage 3 (human: access tag + licence).",
        "summary": summary,
        "sources": (prev["sources"] | catalogue) if args.only else catalogue,
    }
    OUT.write_text(json.dumps(result, indent=2, ensure_ascii=False) + "\n")

    print("\n" + "-" * 60)
    for k in ROLLUP_RANK:
        if summary[k]:
            print(f"  {k:>16} : {summary[k]:>3} URLs")
    print(f"  {'TOTAL':>16} : {summary['urls']:>3} URLs / {summary['sources']} sources")
    print(f"\n  sources by best outcome: {summary['sources_by_rollup']}")
    print(f"\nwrote {OUT.name}")


if __name__ == "__main__":
    main()
