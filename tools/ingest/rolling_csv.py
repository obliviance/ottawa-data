#!/usr/bin/env python3
"""Ingest a plain CSV at a stable URL (a "rolling" file the publisher overwrites in place)
into the warehouse. Re-running replaces the dataset with the current contents.

    python3 tools/ingest/rolling_csv.py --all            # every source in SOURCES below
    python3 tools/ingest/rolling_csv.py --only 311-current
    python3 tools/ingest/rolling_csv.py --url https://.../file.csv --id my-dataset --source-id foo
"""
from __future__ import annotations

import argparse
import pathlib
import sys
import tempfile

sys.path.insert(0, str(pathlib.Path(__file__).parent.parent))
import warehouse  # noqa: E402
from _http import download  # noqa: E402

SOURCES = {
    "311-current": {
        "url": "https://311opendatastorage.blob.core.windows.net/311data/311opendata_currentyear.csv",
        "source_id": "open311", "title": "311 service requests — current year (rolling)"},
    "311-lastyear": {
        "url": "https://311opendatastorage.blob.core.windows.net/311data/311opendata_lastyear.csv",
        "source_id": "open311", "title": "311 service requests — previous year"},
}


def ingest_one(dataset_id: str, url: str, *, source_id: str | None, title: str) -> None:
    import pandas as pd
    with tempfile.NamedTemporaryFile(suffix=".csv", delete=False) as tf:
        tmp = pathlib.Path(tf.name)
    try:
        download(url, tmp, max_bytes=400_000_000)
        for kw in ({"low_memory": False, "encoding": "utf-8-sig", "on_bad_lines": "skip"},
                   {"sep": None, "engine": "python", "on_bad_lines": "skip"}):
            try:
                df = pd.read_csv(tmp, **kw)
                break
            except Exception:  # noqa: BLE001
                df = None
        if df is None:
            raise ValueError("could not parse CSV")
        warehouse.register(dataset_id, df, source_id=source_id, shape="rolling-csv",
                           title=title, origin_url=url, notes="rolling file — re-ingest to refresh")
    finally:
        tmp.unlink(missing_ok=True)


def main() -> None:
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("--all", action="store_true")
    ap.add_argument("--only", nargs="+", metavar="ID")
    ap.add_argument("--url"); ap.add_argument("--id"); ap.add_argument("--source-id")
    a = ap.parse_args()

    if a.url and a.id:
        ingest_one(a.id, a.url, source_id=a.source_id, title=a.id)
        return
    targets = list(SOURCES) if a.all else (a.only or [])
    if not targets:
        sys.exit("nothing to do — pass --all, --only <id>, or --url/--id")
    for tid in targets:
        s = SOURCES[tid]
        try:
            ingest_one(tid, s["url"], source_id=s["source_id"], title=s["title"])
        except Exception as e:  # noqa: BLE001
            print(f"  FAIL {tid}  {type(e).__name__}: {str(e)[:90]}")


if __name__ == "__main__":
    main()
