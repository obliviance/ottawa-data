#!/usr/bin/env python3
"""Snapshot every catalogued URL to the Wayback Machine, so the verification evidence
doesn't rot.

Uses archive.org's Save Page Now (anonymous, rate-limited to roughly one every few
seconds). Records the resulting snapshot URL + timestamp in snapshots.json. Re-running
skips URLs already snapshotted within --max-age days.

    python3 snapshot.py                 # all URLs, skip those snapshotted in the last 30 days
    python3 snapshot.py --only escribe
    python3 snapshot.py --max-age 7 --delay 8
"""
from __future__ import annotations

import argparse
import datetime as dt
import json
import pathlib
import time
import urllib.error
import urllib.parse
import urllib.request

ROOT = pathlib.Path(__file__).parent
OUT = ROOT / "snapshots.json"
NOW = dt.datetime.now(dt.timezone.utc).replace(microsecond=0)
UA = "ottawa-data-verify/0.2 (+https://github.com/obliviance/ottawa-data)"


def wayback_latest(url: str) -> dict | None:
    """Ask the availability API for the most recent existing snapshot."""
    api = "https://archive.org/wayback/available?url=" + urllib.parse.quote(url, safe="")
    try:
        r = urllib.request.urlopen(urllib.request.Request(api, headers={"User-Agent": UA}), timeout=20)
        snap = json.loads(r.read()).get("archived_snapshots", {}).get("closest")
        return snap if snap and snap.get("available") else None
    except (urllib.error.URLError, TimeoutError, ValueError):
        return None


def save_page_now(url: str, delay: float) -> dict:
    req = urllib.request.Request("https://web.archive.org/save/" + url,
                                 headers={"User-Agent": UA}, method="GET")
    started = time.monotonic()
    try:
        r = urllib.request.urlopen(req, timeout=90)
        final = r.geturl()
        snap = final if "/web/" in final else None
        out = {"saved_at": NOW.isoformat(), "snapshot": snap, "status": r.status,
               "elapsed_s": round(time.monotonic() - started, 1)}
    except urllib.error.HTTPError as e:
        out = {"saved_at": NOW.isoformat(), "snapshot": None, "status": e.code,
               "error": f"HTTP {e.code}"}
    except (urllib.error.URLError, TimeoutError) as e:
        out = {"saved_at": NOW.isoformat(), "snapshot": None, "status": None,
               "error": f"{type(e).__name__}: {getattr(e, 'reason', e)}"}
    time.sleep(delay)
    return out


def main() -> None:
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("--only", nargs="+", metavar="ID")
    ap.add_argument("--max-age", type=int, default=30, help="skip URLs snapshotted within N days (default 30)")
    ap.add_argument("--delay", type=float, default=6.0, help="seconds between saves (default 6)")
    args = ap.parse_args()

    data = json.loads((ROOT / "sources.json").read_text())
    prev = json.loads(OUT.read_text()) if OUT.exists() else {"urls": {}}
    cutoff = NOW - dt.timedelta(days=args.max_age)

    jobs = []
    for src in data["sources"]:
        if args.only and src["id"] not in args.only:
            continue
        for url in src["urls"]:
            old = prev["urls"].get(url)
            if old and old.get("snapshot") and \
               dt.datetime.fromisoformat(old["saved_at"]) > cutoff:
                continue
            jobs.append((src["id"], url))

    print(f"snapshotting {len(jobs)} URLs (delay {args.delay}s, ~{len(jobs) * args.delay / 60:.0f} min)\n")
    urls = dict(prev["urls"])
    for i, (sid, url) in enumerate(jobs, 1):
        # cheap check: a very recent snapshot already exists?
        latest = wayback_latest(url)
        if latest and latest.get("timestamp", "0") > (NOW - dt.timedelta(days=args.max_age)).strftime("%Y%m%d000000"):
            urls[url] = {"saved_at": NOW.isoformat(), "snapshot": latest["url"],
                         "status": 200, "note": "existing recent snapshot"}
            print(f"  [{i:>3}/{len(jobs)}] have   {url[:80]}")
            continue
        res = save_page_now(url, args.delay)
        urls[url] = res
        mark = "saved " if res.get("snapshot") else "MISS  "
        print(f"  [{i:>3}/{len(jobs)}] {mark} {url[:80]}  {res.get('error') or ''}")

    saved = sum(1 for v in urls.values() if v.get("snapshot"))
    OUT.write_text(json.dumps({
        "generated_at": NOW.isoformat(),
        "tool": "snapshot.py 0.1 (Wayback Machine Save Page Now)",
        "summary": {"urls": len(urls), "with_snapshot": saved},
        "urls": urls,
    }, indent=2, ensure_ascii=False) + "\n")
    print(f"\n{saved}/{len(urls)} URLs have a snapshot — wrote {OUT.name}")


if __name__ == "__main__":
    main()
