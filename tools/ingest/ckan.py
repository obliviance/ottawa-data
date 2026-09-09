#!/usr/bin/env python3
"""Ingest datasets from a CKAN portal (data.ontario.ca, open.canada.ca) into the warehouse.

CKAN holds thousands of datasets; always narrow with --query. Each CSV / XLSX / GeoJSON
resource becomes one warehouse table.

    python3 tools/ingest/ckan.py --query "ottawa" --list
    python3 tools/ingest/ckan.py --query "financial information return" --limit 5
    python3 tools/ingest/ckan.py --portal open.canada.ca --query "national capital" --limit 10
"""
from __future__ import annotations

import argparse
import pathlib
import re
import sys
import tempfile
import time

sys.path.insert(0, str(pathlib.Path(__file__).parent.parent))
import warehouse  # noqa: E402
from _http import download, get_json  # noqa: E402

LOADABLE = {"csv", "xlsx", "xls", "geojson", "json"}


def slugify(s: str, maxlen: int = 60) -> str:
    return re.sub(r"_+", "_", re.sub(r"[^a-z0-9]+", "_", s.lower())).strip("_")[:maxlen].strip("_")


def read_any(path: pathlib.Path, fmt: str):
    import pandas as pd
    head = path.read_bytes()[:512].lstrip().lower()
    if head.startswith((b"<!doctype", b"<html", b"<?xml")):
        raise ValueError("resource is a web page, not tabular data (mislabelled on the portal)")
    if fmt in ("xlsx", "xls"):
        return pd.read_excel(path)
    if fmt in ("geojson", "json"):
        return warehouse._read_geojson(path)
    for kw in ({"sep": None, "engine": "python", "on_bad_lines": "skip", "encoding": "utf-8-sig"},
               {"low_memory": False, "on_bad_lines": "skip", "encoding": "utf-8-sig"},
               {"sep": None, "engine": "python", "encoding": "latin-1", "on_bad_lines": "skip"}):
        try:
            df = pd.read_csv(path, **kw)
            if len(df.columns) > 1 or len(df) > 1:
                return df
        except Exception:  # noqa: BLE001 - try the next strategy
            continue
    raise ValueError("could not parse as a delimited table")


def main() -> None:
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("--portal", default="data.ontario.ca")
    ap.add_argument("--query", required=True)
    ap.add_argument("--limit", type=int, default=10, help="max packages (default 10)")
    ap.add_argument("--resources", type=int, default=3, help="max resources per package (default 3)")
    ap.add_argument("--delay", type=float, default=1.5)
    ap.add_argument("--list", action="store_true")
    ap.add_argument("--source-id", default=None)
    args = ap.parse_args()

    prefix = slugify(args.portal.split(".")[1] if args.portal.count(".") > 1 else args.portal.split(".")[0])
    base = f"https://{args.portal}/api/3/action"
    res = get_json(f"{base}/package_search?q={args.query.replace(' ', '+')}&rows={args.limit}")
    pkgs = res["result"]["results"]
    print(f"{args.portal}: {res['result']['count']} packages match {args.query!r}; taking {len(pkgs)}\n")

    if args.list:
        for p in pkgs:
            fmts = sorted({(r.get("format") or "?").lower() for r in p.get("resources", [])})
            print(f"  {p['title'][:66]:66}  {fmts}")
        return

    done = fail = 0
    for p in pkgs:
        resources = [r for r in p.get("resources", [])
                     if (r.get("format") or "").lower() in LOADABLE and r.get("url")][: args.resources]
        multi = len(resources) > 1
        for i, r in enumerate(resources):
            fmt = r["format"].lower()
            rslug = slugify(r.get("name") or "", 24) or f"r{i}"
            did = f"{prefix}_{slugify(p['name'], 44)}" + (f"__{rslug}" if multi else "")
            try:
                with tempfile.NamedTemporaryFile(suffix=f".{fmt}", delete=False) as tf:
                    tmp = pathlib.Path(tf.name)
                download(r["url"], tmp)
                warehouse.register(
                    did, read_any(tmp, fmt), source_id=args.source_id, shape="ckan",
                    title=(p["title"] + (f" — {r.get('name')}" if multi else ""))[:120],
                    origin_url=f"https://{args.portal}/dataset/{p['name']}",
                    notes=f"{fmt} · licence: {p.get('license_title') or p.get('license_id') or '?'}")
                tmp.unlink(missing_ok=True)
                done += 1
            except Exception as e:  # noqa: BLE001
                print(f"  FAIL  {did[:55]}  {type(e).__name__}: {str(e)[:80]}")
                fail += 1
            time.sleep(args.delay)

    print(f"\n{done} ingested, {fail} failed — `python3 tools/warehouse.py list`")


if __name__ == "__main__":
    main()
