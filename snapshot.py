#!/usr/bin/env python3
"""Snapshot every catalogued URL to the Wayback Machine, so the verification evidence
doesn't rot.

Uses archive.org's Save Page Now. That service is anonymous-rate-limited and frequently
returns HTTP 429; this script backs off on 429, writes snapshots.json incrementally (so a
kill mid-run loses nothing), and flushes every line — check the log while it runs.

    python3 -u snapshot.py                  # all URLs not snapshotted in the last 30 days
    python3 -u snapshot.py --only escribe
    python3 -u snapshot.py --limit 20       # stop after 20 (good for a first pass)
    python3 -u snapshot.py --max-age 7 --delay 15

Run with `python3 -u` (unbuffered) so the progress log is live.
"""
from __future__ import annotations

import argparse
import datetime as dt
import json
import pathlib
import sys
import time
import urllib.error
import urllib.parse
import urllib.request

ROOT = pathlib.Path(__file__).parent
OUT = ROOT / "snapshots.json"
NOW = dt.datetime.now(dt.timezone.utc).replace(microsecond=0)
UA = "ottawa-data-verify/0.2 (+https://github.com/obliviance/ottawa-data)"


def log(msg: str) -> None:
    print(msg, flush=True)


def wayback_latest(url: str) -> tuple[str | None, int | None]:
    """(snapshot url, http status) for the most recent existing snapshot, if any."""
    api = "https://archive.org/wayback/available?url=" + urllib.parse.quote(url, safe="")
    try:
        r = urllib.request.urlopen(
            urllib.request.Request(api, headers={"User-Agent": UA}), timeout=20)
        snap = json.loads(r.read()).get("archived_snapshots", {}).get("closest")
        if snap and snap.get("available"):
            return snap["url"], snap.get("timestamp")
        return None, r.status
    except urllib.error.HTTPError as e:
        return None, e.code
    except (urllib.error.URLError, TimeoutError, ValueError):
        return None, None


def save_page_now(url: str) -> dict:
    req = urllib.request.Request("https://web.archive.org/save/" + url,
                                 headers={"User-Agent": UA}, method="GET")
    started = time.monotonic()
    try:
        r = urllib.request.urlopen(req, timeout=120)
        final = r.geturl()
        return {"saved_at": NOW.isoformat(),
                "snapshot": final if "/web/" in final else None,
                "status": r.status, "elapsed_s": round(time.monotonic() - started, 1),
                "error": None if "/web/" in final else f"redirected to {final[:80]}"}
    except urllib.error.HTTPError as e:
        return {"saved_at": NOW.isoformat(), "snapshot": None, "status": e.code,
                "error": f"HTTP {e.code}"}
    except (urllib.error.URLError, TimeoutError) as e:
        return {"saved_at": NOW.isoformat(), "snapshot": None, "status": None,
                "error": f"{type(e).__name__}: {getattr(e, 'reason', e)}"}


def write(urls: dict) -> None:
    saved = sum(1 for v in urls.values() if v.get("snapshot"))
    OUT.write_text(json.dumps({
        "generated_at": NOW.isoformat(),
        "tool": "snapshot.py 0.2 (Wayback Machine Save Page Now)",
        "summary": {"urls": len(urls), "with_snapshot": saved,
                    "rate_limited": sum(1 for v in urls.values() if v.get("status") == 429)},
        "urls": urls,
    }, indent=2, ensure_ascii=False) + "\n")


def main() -> None:
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("--only", nargs="+", metavar="ID")
    ap.add_argument("--limit", type=int, default=0, help="stop after N URLs (0 = no limit)")
    ap.add_argument("--max-age", type=int, default=30, help="skip URLs snapshotted within N days")
    ap.add_argument("--delay", type=float, default=10.0, help="seconds between saves (default 10)")
    args = ap.parse_args()

    data = json.loads((ROOT / "sources.json").read_text())
    prev = json.loads(OUT.read_text()) if OUT.exists() else {"urls": {}}
    cutoff = NOW - dt.timedelta(days=args.max_age)
    cutoff_ts = cutoff.strftime("%Y%m%d000000")

    jobs = []
    for src in data["sources"]:
        if args.only and src["id"] not in args.only:
            continue
        for url in src["urls"]:
            old = prev["urls"].get(url)
            if old and old.get("snapshot") and dt.datetime.fromisoformat(old["saved_at"]) > cutoff:
                continue
            jobs.append(url)
    if args.limit:
        jobs = jobs[:args.limit]

    log(f"snapshotting {len(jobs)} URLs · delay {args.delay}s · writing {OUT.name} after each\n")
    urls = dict(prev["urls"])
    consecutive_429 = 0

    for i, url in enumerate(jobs, 1):
        existing, ts = wayback_latest(url)
        if existing and (ts or "0") > cutoff_ts:
            urls[url] = {"saved_at": NOW.isoformat(), "snapshot": existing,
                         "status": 200, "note": "existing recent snapshot"}
            log(f"  [{i:>3}/{len(jobs)}] have    {url[:82]}")
            write(urls)
            continue

        res = save_page_now(url)
        urls[url] = res
        write(urls)

        if res["status"] == 429:
            consecutive_429 += 1
            backoff = min(args.delay * 2 ** consecutive_429, 300)
            log(f"  [{i:>3}/{len(jobs)}] 429     {url[:60]}  — backing off {backoff:.0f}s")
            time.sleep(backoff)
            if consecutive_429 >= 5:
                log("\narchive.org is rate-limiting hard — stopping. Re-run later to continue "
                    "(done URLs are recorded).")
                break
            continue

        consecutive_429 = 0
        mark = "saved  " if res.get("snapshot") else "MISS   "
        log(f"  [{i:>3}/{len(jobs)}] {mark} {url[:82]}  {res.get('error') or ''}")
        time.sleep(args.delay)

    write(urls)
    saved = sum(1 for v in urls.values() if v.get("snapshot"))
    log(f"\n{saved}/{len(urls)} URLs have a snapshot — wrote {OUT.name}")
    sys.exit(0)


if __name__ == "__main__":
    main()
