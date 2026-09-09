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
import json
import pathlib
import re
import sys
import tempfile
import time

sys.path.insert(0, str(pathlib.Path(__file__).parent.parent))
import warehouse  # noqa: E402
from _http import TooLarge, download, get_json  # noqa: E402

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


def geoservices_url(dists: list[dict]) -> str | None:
    for d in dists:
        if "geoservices" in (d.get("format") or "").lower():
            return d.get("accessURL") or d.get("downloadURL")
    return None


def fetch_featureserver(api_url: str, dest: pathlib.Path, *, page: int = 2000,
                        max_records: int = 200_000) -> int:
    """Page a Feature/MapServer layer to a GeoJSON FeatureCollection file. Returns row count."""
    base = api_url.rstrip("/")
    if not base.rsplit("/", 1)[-1].isdigit():
        base += "/0"
    feats, offset = [], 0
    while offset < max_records:
        q = (f"{base}/query?where=1%3D1&outFields=*&returnGeometry=true&f=geojson"
             f"&resultOffset={offset}&resultRecordCount={page}")
        j = get_json(q)
        batch = j.get("features", [])
        feats.extend(batch)
        if not j.get("properties", {}).get("exceededTransferLimit") and not j.get("exceededTransferLimit"):
            break
        if not batch:
            break
        offset += len(batch)
    dest.write_text(json.dumps({"type": "FeatureCollection", "features": feats}))
    return len(feats)


def _register_zip_csvs(did: str, zippath: pathlib.Path, source_id, title, origin, lic) -> int:
    import io
    import zipfile

    import pandas as pd
    total = 0
    with zipfile.ZipFile(zippath) as zf:
        csvs = [n for n in zf.namelist() if n.lower().endswith(".csv")]
        for name in csvs:
            try:
                df = pd.read_csv(io.BytesIO(zf.read(name)), low_memory=False, on_bad_lines="skip")
            except Exception:  # noqa: BLE001
                continue
            sub = did if len(csvs) == 1 else f"{did}__{slugify(name.rsplit('.', 1)[0], 24)}"
            warehouse.register(sub, df, source_id=source_id, shape="arcgis-hub",
                               title=title + ("" if len(csvs) == 1 else f" — {name}"),
                               origin_url=origin, notes=f"from zip · licence: {lic}")
            total += len(df)
    return total


def main() -> None:
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("--hub", default="open.ottawa.ca")
    ap.add_argument("--prefix", default="", help="dataset_id prefix (default: derived from hub)")
    ap.add_argument("--filter", default="", help="only titles containing this substring")
    ap.add_argument("--limit", type=int, default=0)
    ap.add_argument("--max-mb", type=float, default=80, help="skip datasets larger than this")
    ap.add_argument("--delay", type=float, default=1.5)
    ap.add_argument("--skip-existing", action="store_true", help="skip dataset_ids already in the warehouse")
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

    have = set(warehouse._load_manifest()["datasets"]) if args.skip_existing else set()
    done = fail = skip = big = 0
    for n, d in enumerate(datasets[: args.limit or None], 1):
        title = d["title"]
        did = warehouse._sanitize_id(f"{prefix}_{slugify(title)}")
        if did in have:
            skip += 1
            continue
        dists = d.get("distribution", [])
        pick = pick_distribution(dists, title)
        api = geoservices_url(dists)
        if not pick and not api:
            print(f"  [{n}] skip (web page / doc)  {title[:56]}")
            skip += 1
            continue
        lic = re.sub("<[^>]+>", "", d.get("license") or "").strip()[:80]
        origin = d.get("landingPage", f"https://{args.hub}/")
        tmp = None
        try:
            if pick:
                fmt, url = pick
                with tempfile.NamedTemporaryFile(suffix=f".{fmt}", delete=False) as tf:
                    tmp = pathlib.Path(tf.name)
                download(url, tmp, max_bytes=int(args.max_mb * 1e6))
                warehouse.register(did, tmp, source_id=args.source_id, shape="arcgis-hub",
                                   title=title, origin_url=origin, notes=f"{fmt} · licence: {lic}")
            elif api.lower().split("?")[0].endswith(".zip"):  # mislabelled: it's a zip of CSVs
                with tempfile.NamedTemporaryFile(suffix=".zip", delete=False) as tf:
                    tmp = pathlib.Path(tf.name)
                download(api, tmp, max_bytes=int(args.max_mb * 1e6))
                nrows = _register_zip_csvs(did, tmp, args.source_id, title, origin, lic)
                if not nrows:
                    raise ValueError("zip had no loadable CSV")
            else:  # FeatureServer fallback — no download link, query the API
                with tempfile.NamedTemporaryFile(suffix=".geojson", delete=False) as tf:
                    tmp = pathlib.Path(tf.name)
                nrows = fetch_featureserver(api, tmp)
                if nrows == 0:
                    raise ValueError("FeatureServer query returned 0 rows")
                warehouse.register(did, tmp, source_id=args.source_id, shape="arcgis-hub",
                                   title=title, origin_url=origin,
                                   notes=f"FeatureServer query ({nrows} rows) · licence: {lic}")
            done += 1
        except TooLarge as e:
            print(f"  [{n}] BIG  {title[:52]}  ({e}) — ingest individually")
            big += 1
        except Exception as e:  # noqa: BLE001 - one bad dataset shouldn't stop the run
            print(f"  [{n}] FAIL {title[:52]}  {type(e).__name__}: {str(e)[:70]}")
            fail += 1
        finally:
            if tmp:
                tmp.unlink(missing_ok=True)
        time.sleep(args.delay)

    print(f"\n{done} ingested · {fail} failed · {big} too-large · {skip} skipped"
          f" — `python3 tools/warehouse.py list`")


if __name__ == "__main__":
    main()
