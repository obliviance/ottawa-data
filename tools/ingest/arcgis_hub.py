#!/usr/bin/env python3
"""Ingest an ArcGIS Hub open-data portal: read its DCAT feed, then pull every dataset
as GeoJSON (spatial) or CSV (tabular) into the warehouse.

    python3 tools/ingest/arcgis_hub.py --list                    # catalogue only, no download
    python3 tools/ingest/arcgis_hub.py --filter collision        # titles matching a substring
    python3 tools/ingest/arcgis_hub.py --limit 20
    python3 tools/ingest/arcgis_hub.py --hub data.ottawapolice.ca --prefix ops

Hubs (see hierarchy.md): open.ottawa.ca (default, ~690 datasets), data.ottawapolice.ca,
ottawa-riverkeeper-open-data-ork-so.hub.arcgis.com.
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

SPATIAL_HINT = re.compile(r"(location|boundar|area|zone|route|park|road|ward|point|site|map|"
                          r"parcel|address|facilit|station|tree|path|trail|district)", re.I)


def slugify(s: str, maxlen: int = 66) -> str:
    return re.sub(r"_+", "_", re.sub(r"[^a-z0-9]+", "_", s.lower())).strip("_")[:maxlen].strip("_")


def pick_distribution(dists: list[dict], title: str) -> tuple[str, str] | None:
    """Return (format, url) - GeoJSON if the dataset looks spatial, else CSV."""
    by_fmt = {}
    for d in dists:
        f = (d.get("format") or "").lower()
        url = d.get("downloadURL") or d.get("accessURL")
        if url:
            by_fmt.setdefault(f, url)
    want = ["geojson", "csv"] if SPATIAL_HINT.search(title) else ["csv", "geojson"]
    for f in want:
        if f in by_fmt:
            return f, by_fmt[f]
    return None


def main() -> None:
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("--hub", default="open.ottawa.ca")
    ap.add_argument("--prefix", default="", help="dataset_id prefix (default: derived from hub)")
    ap.add_argument("--filter", default="", help="only titles containing this substring")
    ap.add_argument("--limit", type=int, default=0)
    ap.add_argument("--delay", type=float, default=1.5)
    ap.add_argument("--list", action="store_true", help="print the catalogue, download nothing")
    ap.add_argument("--source-id", default=None, help="tag every dataset with this sources.json id")
    args = ap.parse_args()

    prefix = args.prefix or slugify(args.hub.split(".")[0])
    feed = get_json(f"https://{args.hub}/api/feed/dcat-us/1.1.json")
    datasets = feed.get("dataset", [])
    if args.filter:
        datasets = [d for d in datasets if args.filter.lower() in d["title"].lower()]
    print(f"{args.hub}: {len(datasets)} datasets"
          f"{f' matching {args.filter!r}' if args.filter else ''}\n")

    if args.list:
        for d in datasets:
            fmts = sorted({(x.get('format') or '?') for x in d.get("distribution", [])})
            print(f"  {d['title'][:70]:70}  {fmts}")
        return

    done = fail = 0
    for d in datasets[: args.limit or None]:
        title = d["title"]
        did = f"{prefix}_{slugify(title)}"
        pick = pick_distribution(d.get("distribution", []), title)
        if not pick:
            print(f"  skip (no CSV/GeoJSON)  {title[:60]}")
            continue
        fmt, url = pick
        try:
            with tempfile.NamedTemporaryFile(suffix=f".{fmt}", delete=False) as tf:
                tmp = pathlib.Path(tf.name)
            download(url, tmp)
            warehouse.register(
                did, tmp, source_id=args.source_id, shape="arcgis-hub", title=title,
                origin_url=d.get("landingPage", f"https://{args.hub}/"),
                notes=f"{fmt} · licence: {re.sub('<[^>]+>', '', d.get('license') or '').strip()[:80]}")
            tmp.unlink(missing_ok=True)
            done += 1
        except Exception as e:  # noqa: BLE001 - one bad dataset shouldn't stop the run
            print(f"  FAIL  {title[:55]}  {type(e).__name__}: {str(e)[:80]}")
            fail += 1
        time.sleep(args.delay)

    print(f"\n{done} ingested, {fail} failed — `python3 tools/warehouse.py list`")


if __name__ == "__main__":
    main()
