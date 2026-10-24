#!/usr/bin/env python3
"""Inventory and ingest the Open Ottawa items that `arcgis_hub.py` cannot reach.

    python3 tools/ingest/arcgis_documents.py --inventory      # one request per item -> table
    python3 tools/ingest/arcgis_documents.py --ingest         # download csv/xlsx documents

The 2026-10-16 survey split the hub's 703 DCAT items: 288 have a CSV/GeoJSON/zip download plus a
real REST endpoint (what `arcgis_hub.py` ingests); the other 349 have neither - 291 "documents"
(files such as budget status-report spreadsheets and ward census tables), 58 "datasets", 46
apps and a few pages/maps. For documents the file sits behind the item id that DCAT carries in
`identifier` (`...item.html?id=<32 hex>`), at
`https://www.arcgis.com/sharing/rest/content/items/<id>/data`, which is how
`election_results.py` got the 2022 Statement of Votes Cast.

--inventory registers `open_ottawa_item_inventory`: id, title, landing page, item type, file name,
size in bytes, modified time. --ingest then downloads every document whose type is CSV or Microsoft
Excel and is under --max-mb, registering one table per sheet as `doc_<slug>[__<sheet>]`.
PDFs, Word files, dashboards and apps are listed in the inventory only.
"""
from __future__ import annotations

import argparse
import io
import json
import pathlib
import re
import sys
import time
import urllib.parse

sys.path.insert(0, str(pathlib.Path(__file__).parent.parent))
import warehouse  # noqa: E402
from _http import get, get_json  # noqa: E402

DCAT = "https://open.ottawa.ca/api/feed/dcat-us/1.1.json"
ITEM = "https://www.arcgis.com/sharing/rest/content/items/{}"
HAS_DOWNLOAD = ("csv", "geojson", "zip")
TABULAR = {"CSV", "Microsoft Excel"}


def candidates() -> list[dict]:
    """DCAT items with no CSV/GeoJSON/zip distribution (the ones arcgis_hub.py skips)."""
    out = []
    for d in get_json(DCAT)["dataset"]:
        fmts = [(q.get("format") or "").lower() for q in d.get("distribution", [])]
        if any(f in HAS_DOWNLOAD for f in fmts):
            continue
        m = re.search(r"id=([0-9a-f]{32})", d.get("identifier", ""))
        if m:
            out.append({"item_id": m.group(1), "title": d["title"], "landing_page": d.get("landingPage", ""),
                        "dcat_modified": d.get("modified")})
    return out


def inventory(delay: float) -> None:
    import pandas as pd

    rows = []
    for i, c in enumerate(candidates(), 1):
        try:
            j = get_json(ITEM.format(c["item_id"]) + "?f=json")
        except Exception as e:  # noqa: BLE001
            j = {"error": f"{type(e).__name__}: {e}"[:120]}
        rows.append({**c, "item_type": j.get("type"), "file_name": j.get("name"), "size_bytes": j.get("size"),
                     "item_modified_ms": j.get("modified"), "error": j.get("error") if "error" in j else None})
        if i % 50 == 0:
            print(f"  {i} items", flush=True)
        time.sleep(delay)
    df = pd.DataFrame(rows)
    df["item_modified"] = pd.to_datetime(df["item_modified_ms"], unit="ms", errors="coerce")
    df["kind"] = df["landing_page"].str.extract(r"open\.ottawa\.ca/([a-z]+)/", expand=False)
    warehouse.register("open_ottawa_item_inventory", df.drop(columns="item_modified_ms"),
                       source_id="open-ottawa", shape="arcgis-hub",
                       title="Open Ottawa items with no CSV/GeoJSON/zip download (inventory)",
                       origin_url=DCAT, notes="item type/size from the ArcGIS item API; see arcgis_documents.py")
    print(df["item_type"].value_counts(dropna=False).to_string())


def ingest(max_mb: float, delay: float, skip_existing: bool) -> None:
    import pandas as pd

    inv = warehouse.con().execute("SELECT * FROM d_open_ottawa_item_inventory").df()
    todo = inv[inv["item_type"].isin(TABULAR) & (inv["size_bytes"].fillna(0) <= max_mb * 1e6)]
    print(f"{len(todo)} tabular documents (of {len(inv)} items) under {max_mb} MB")
    have = set(warehouse._load_manifest()["datasets"])
    ok = fail = skipped = 0
    for r in todo.itertuples():
        base = "doc_" + re.sub(r"[^a-z0-9]+", "_", r.title.lower()).strip("_")[:60]
        if skip_existing and any(h == base or h.startswith(base + "__") for h in have):
            skipped += 1
            continue
        try:
            raw = get(ITEM.format(r.item_id) + "/data")
            name = (r.file_name or "").lower()
            if r.item_type == "CSV" or name.endswith(".csv"):
                try:
                    csv_df = pd.read_csv(io.BytesIO(raw), low_memory=False, encoding="utf-8-sig")
                except UnicodeDecodeError:  # older exports are Windows-1252
                    csv_df = pd.read_csv(io.BytesIO(raw), low_memory=False, encoding="cp1252", encoding_errors="replace")
                frames = {"": csv_df}
            else:
                frames = pd.read_excel(io.BytesIO(raw), sheet_name=None)
            for sheet, df in frames.items():
                if df.empty:
                    continue
                df.columns = [str(c) for c in df.columns]  # pivot-style sheets have date headers
                did = base if len(frames) == 1 else f"{base}__{re.sub(r'[^a-z0-9]+', '_', str(sheet).lower())[:20]}"
                warehouse.register(did, df, source_id="open-ottawa", shape="arcgis-hub", title=r.title,
                                   origin_url=r.landing_page,
                                   notes=f"document item {r.item_id}; sheet {sheet!r}" if sheet else f"document item {r.item_id}")
            ok += 1
        except Exception as e:  # noqa: BLE001
            print(f"  FAIL {r.title[:50]}: {type(e).__name__}: {str(e)[:70]}")
            fail += 1
        time.sleep(delay)
    print(f"{ok} ingested, {fail} failed, {skipped} already present")


def main() -> None:
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("--inventory", action="store_true")
    ap.add_argument("--ingest", action="store_true")
    ap.add_argument("--skip-existing", action="store_true", help="resume: skip documents already registered")
    ap.add_argument("--max-mb", type=float, default=25)
    ap.add_argument("--delay", type=float, default=1.0)
    a = ap.parse_args()
    if not (a.inventory or a.ingest):
        ap.error("choose --inventory and/or --ingest")
    if a.inventory:
        inventory(a.delay)
    if a.ingest:
        ingest(a.max_mb, a.delay, a.skip_existing)


if __name__ == "__main__":
    main()
