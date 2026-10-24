#!/usr/bin/env python3
"""Ingest named ArcGIS Feature/MapServer layers (not whole hubs) into the warehouse.

    python3 tools/ingest/arcgis_layers.py --list                    # the registry, no network
    python3 tools/ingest/arcgis_layers.py ops_traffic_stops trees   # ingest these
    python3 tools/ingest/arcgis_layers.py --all --cache <dir>

Why this exists: `arcgis_hub.py` works from a hub's DCAT feed and caps a layer at 200k
rows held in one GeoJSON string. The survey found large keyless layers that are not reached
that way (Ottawa Police portal: 1.1M calls for service; the 304k-point tree inventory; the
Development_Applications MapServer). This pages a layer by OBJECTID in 2,000-row pages,
caches each page on disk (so a killed run resumes instead of restarting), and registers one
parquet. Points become longitude/latitude columns; other geometries become a JSON string.

Where the Hub offers a CSV export for the layer (`csv_item`), that is used instead of paging:
the export redirects to a prebuilt replica file and 1.1M rows download in ~7 s, versus ~10 s
per 2,000-row page when paging. Paging stays as the fallback and the only path for MapServer
layers. CSV exports carry x/y in Web Mercator (EPSG:3857) for point layers; they are converted
to longitude/latitude here.

Politeness: 1 s between pages, descriptive User-Agent, hard per-layer deadline (--deadline).
"""
from __future__ import annotations

import argparse
import json
import pathlib
import sys
import time

sys.path.insert(0, str(pathlib.Path(__file__).parent.parent))
import warehouse  # noqa: E402
from _http import get_json  # noqa: E402

OPS_HUB = "https://data.ottawapolice.ca/api/download/v1/items/{}/csv?layers=0"
OPS = "https://services7.arcgis.com/2vhcNzw0NfUwAD3d/arcgis/rest/services"
MAPS = "https://maps.ottawa.ca/arcgis/rest/services"
RVCA = "https://gis.rvca.ca/arcgis/rest/services/RVCA_Hazards_publicService/MapServer"

# dataset_id -> spec. Every URL was queried for its count on 2026-10-16 (see
# explorations/survey/survey-log.md); counts are what the layer reported then.
LAYERS = {
    "ops_criminal_offences": dict(
        csv_item="0356deb79cfd4488956116fda366df38",
        url=f"{OPS}/Criminal_Offences_Open_Data/FeatureServer/0", source_id="ops-data-portal",
        title="Ottawa Police — Criminal Offences (open data)", expect=344_290),
    "ops_calls_for_service": dict(
        csv_item="d2b02f00078943379bc1f439a07bd64d",
        url=f"{OPS}/Calls_For_Service/FeatureServer/0", source_id="ops-data-portal",
        title="Ottawa Police — Dispatched Calls For Service", expect=1_108_780),
    "ops_traffic_stops": dict(
        csv_item="76a54b7f7ef44ab1b78dd96f3061c7cb",
        url=f"{OPS}/TSRDCP_TrafficStops_v1/FeatureServer/0", source_id="ops-data-portal",
        title="Ottawa Police — Traffic Stops (Race Data Collection Program)", expect=455_717),
    "ops_crime_map_ytd": dict(
        url=f"{OPS}/CrimeMap_YTD/FeatureServer/8", source_id="crime-map",
        title="Ottawa Police — Crime Map, year to date", expect=30_349),
    "city_tree_inventory": dict(
        url=f"{MAPS}/Forestry/MapServer/0", source_id="trees-parks",
        title="City of Ottawa — tree inventory (Forestry MapServer layer 0)", expect=304_207),
    "city_devapps_mapserver": dict(
        url=f"{MAPS}/Development_Applications/MapServer/0", source_id="devapps",
        title="City of Ottawa — development applications (keyless MapServer)", expect=3_455),
    "rvca_regulation_limit": dict(
        page=25,
        url=f"{RVCA}/6", source_id="conservation-authorities",
        title="RVCA — Regulation Limit (O.Reg 174/06 hazard extent)", expect=503),
    "rvca_regulated_wetlands": dict(
        url=f"{RVCA}/7", source_id="conservation-authorities",
        title="RVCA — Regulated Wetlands", expect=82),
    "rvca_100yr_floodline": dict(
        page=25,
        url=f"{RVCA}/5", source_id="conservation-authorities",
        title="RVCA — 100-year floodline", expect=657),
    "city_road_centrelines": dict(
        url=f"{MAPS}/Road_Detail/MapServer/3", source_id="road-network",
        title="City of Ottawa — road centrelines (Road_Detail layer 3)", expect=29_457),
}


def _page_size(url: str) -> int:
    try:
        meta = get_json(url + "?f=json")
        return max(100, min(int(meta.get("maxRecordCount") or 1000), 2000))
    except Exception:  # noqa: BLE001
        return 1000


def fetch_layer(url: str, cache: pathlib.Path, *, delay: float, deadline: float, page_size: int = 0) -> list[dict]:
    """Page by OBJECTID order. Returns GeoJSON features; pages cached under `cache`."""
    cache.mkdir(parents=True, exist_ok=True)
    size = page_size or _page_size(url)  # heavy polygon layers need small pages (HTTP 500 otherwise)
    feats: list[dict] = []
    offset = 0
    while True:
        if time.time() > deadline:
            raise TimeoutError(f"deadline hit at offset {offset} (cache kept; re-run to resume)")
        page = cache / f"{offset:09d}.json"
        if page.exists():
            j = json.loads(page.read_text())
        else:
            q = (f"{url}/query?where=1%3D1&outFields=*&returnGeometry=true&outSR=4326"
                 f"&orderByFields=OBJECTID&f=geojson&resultOffset={offset}&resultRecordCount={size}")
            j = get_json(q)
            if "error" in j:
                raise RuntimeError(str(j["error"])[:200])
            page.write_text(json.dumps(j))
            time.sleep(delay)
        batch = j.get("features", [])
        feats.extend(batch)
        offset += len(batch)
        more = j.get("exceededTransferLimit") or j.get("properties", {}).get("exceededTransferLimit")
        if not batch or not more:
            return feats


def _mtm9_to_lonlat(x, y):
    """Inverse transverse Mercator (Kruger series, GRS80) for the City of Ottawa projection:
    central meridian -76.5, scale 0.9999, false easting 304800 (the layer's own WKT).
    Accurate to well under a metre; avoids a pyproj dependency for one projection."""
    import numpy as np
    a, f = 6378137.0, 1 / 298.257222101
    k0, x0, lon0 = 0.9999, 304800.0, np.radians(-76.5)
    n = f / (2 - f)
    A = a / (1 + n) * (1 + n**2 / 4 + n**4 / 64)
    beta = [n / 2 - 2 * n**2 / 3 + 37 * n**3 / 96, n**2 / 48 + n**3 / 15, 17 * n**3 / 480]
    delta = [2 * n - 2 * n**2 / 3 - 2 * n**3, 7 * n**2 / 3 - 8 * n**3 / 5, 56 * n**3 / 15]
    xi, eta = y / (k0 * A), (x - x0) / (k0 * A)
    xi_p = xi - sum(b * np.sin(2 * j * xi) * np.cosh(2 * j * eta) for j, b in enumerate(beta, 1))
    eta_p = eta - sum(b * np.cos(2 * j * xi) * np.sinh(2 * j * eta) for j, b in enumerate(beta, 1))
    chi = np.arcsin(np.sin(xi_p) / np.cosh(eta_p))
    lat = chi + sum(d * np.sin(2 * j * chi) for j, d in enumerate(delta, 1))
    lon = lon0 + np.arctan2(np.sinh(eta_p), np.cos(xi_p))
    return np.degrees(lon), np.degrees(lat)


def fetch_csv(item: str, dest: pathlib.Path):
    """Hub CSV export (302 -> replica file). A tiny body means 'still generating'."""
    import pandas as pd

    from _http import download
    for attempt in range(4):
        download(OPS_HUB.format(item), dest, max_bytes=int(1.5e9))
        if dest.stat().st_size > 600:
            break
        time.sleep(5 * (attempt + 1))
    else:
        raise ValueError("Hub CSV export still pending (stub body)")
    df = pd.read_csv(dest, low_memory=False, encoding="utf-8-sig")
    if {"x", "y"} <= set(df.columns) and df["x"].abs().max() > 180:
        import numpy as np
        if df["x"].abs().max() < 1_000_000:  # City of Ottawa MTM zone 9 (NAD83), metres
            df["longitude"], df["latitude"] = _mtm9_to_lonlat(df["x"].to_numpy(), df["y"].to_numpy())
        else:  # Web Mercator metres
            R = 6378137.0
            df["longitude"] = np.degrees(df["x"] / R)
            df["latitude"] = np.degrees(2 * np.arctan(np.exp(df["y"] / R)) - np.pi / 2)
        df = df.drop(columns=["x", "y"])
    return df


def to_frame(feats: list[dict]):
    import pandas as pd

    rows = []
    for f in feats:
        row = dict(f.get("properties") or {})
        g = f.get("geometry")
        if g:
            if g.get("type") == "Point":
                row["longitude"], row["latitude"] = g["coordinates"][:2]
            else:
                row["geometry"] = json.dumps(g)
        rows.append(row)
    return pd.DataFrame(rows)


def main() -> None:
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("ids", nargs="*", help=f"dataset ids: {', '.join(LAYERS)}")
    ap.add_argument("--all", action="store_true")
    ap.add_argument("--list", action="store_true")
    ap.add_argument("--cache", default="warehouse/_pages", help="page cache dir (gitignored)")
    ap.add_argument("--delay", type=float, default=1.0)
    ap.add_argument("--deadline", type=int, default=1500, help="seconds allowed per layer")
    a = ap.parse_args()

    if a.list:
        for k, v in LAYERS.items():
            print(f"{k:26} {v['expect']:>10,}  {v['url']}")
        return
    ids = list(LAYERS) if a.all else a.ids
    if not ids:
        ap.error("give dataset ids, --all, or --list")
    for did in ids:
        spec = LAYERS[did]
        t0 = time.time()
        print(f"{did}: fetching {spec['url']}", flush=True)
        try:
            if spec.get("csv_item"):
                df = fetch_csv(spec["csv_item"], pathlib.Path(a.cache) / f"{did}.csv")
            else:
                feats = fetch_layer(spec["url"], pathlib.Path(a.cache) / did,
                                    delay=a.delay, deadline=t0 + a.deadline,
                                    page_size=spec.get("page", 0))
                df = to_frame(feats)
        except Exception as e:  # noqa: BLE001
            print(f"  FAIL {did}: {type(e).__name__}: {e}", flush=True)
            continue
        drift = "" if abs(len(df) - spec["expect"]) <= max(5, 0.02 * spec["expect"]) else \
            f" (expected ~{spec['expect']:,} on 2026-10-16)"
        warehouse.register(did, df, source_id=spec["source_id"], shape="arcgis-hub",
                           title=spec["title"], origin_url=spec["url"],
                           notes=f"{'Hub CSV export' if spec.get('csv_item') else 'paged by OBJECTID'} via arcgis_layers.py; {len(df):,} rows{drift}")
        print(f"  {did}: {len(df):,} rows in {time.time() - t0:.0f}s{drift}", flush=True)


if __name__ == "__main__":
    main()
