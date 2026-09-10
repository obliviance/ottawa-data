#!/usr/bin/env python3
"""The exploration warehouse: a DuckDB file plus one Parquet per dataset.

Every ingester lands its output through `register()`, which writes
`warehouse/<dataset_id>.parquet`, upserts a row into the `_datasets` table of
`warehouse/ottawa.duckdb`, and updates `warehouse/manifest.json` (the small,
committed, human-readable index; the .duckdb and .parquet files are gitignored).

    python3 tools/warehouse.py init                 # create an empty warehouse
    python3 tools/warehouse.py list                 # what's landed
    python3 tools/warehouse.py query "SELECT ..."   # ad-hoc SQL over every dataset
    python3 tools/warehouse.py drop <dataset_id>

In SQL, each dataset is a view named `d_<dataset_id>` (dashes -> underscores).
"""
from __future__ import annotations

import argparse
import datetime as dt
import json
import pathlib
import re
import sys

REPO = pathlib.Path(__file__).parent.parent
WH = REPO / "warehouse"
DB = WH / "ottawa.duckdb"
MANIFEST = WH / "manifest.json"

SHAPES = ("arcgis-hub", "ckan", "rolling-csv", "json-api", "pdf", "html", "manual", "spine", "derived")


def _duck(retries: int = 8):
    import time as _t

    import duckdb
    for i in range(retries):
        try:
            con = duckdb.connect(str(DB))
            break
        except (duckdb.IOException, duckdb.Error) as e:
            if "lock" not in str(e).lower() or i == retries - 1:
                raise
            _t.sleep(0.5 * (i + 1))  # another ingester holds it; back off
    con.execute("INSTALL spatial; LOAD spatial;")
    con.execute("""
        CREATE TABLE IF NOT EXISTS _datasets (
            dataset_id   VARCHAR PRIMARY KEY,
            source_id    VARCHAR,          -- sources.json id, if it maps to one
            shape        VARCHAR,
            title        VARCHAR,
            origin_url   VARCHAR,
            rows         BIGINT,
            columns      VARCHAR,          -- JSON list of {name,type}
            spatial      BOOLEAN,
            fetched_at   TIMESTAMP,
            parquet      VARCHAR,
            notes        VARCHAR
        );
    """)
    return con


def _view_name(dataset_id: str) -> str:
    return "d_" + re.sub(r"[^a-z0-9]+", "_", dataset_id.lower()).strip("_")


def _sanitize_id(dataset_id: str) -> str:
    did = re.sub(r"[^a-z0-9._-]+", "-", dataset_id.lower()).strip("-._") or "unnamed"
    if len(did) > 80:
        import hashlib
        did = did[:70].rstrip("-._") + "-" + hashlib.sha1(did.encode()).hexdigest()[:8]
    return did


def _load_manifest() -> dict:
    if MANIFEST.exists():
        return json.loads(MANIFEST.read_text())
    return {"updated_at": None, "datasets": {}}


def _save_manifest(m: dict) -> None:
    m["updated_at"] = dt.datetime.now(dt.timezone.utc).replace(microsecond=0).isoformat()
    MANIFEST.write_text(json.dumps(m, indent=2, ensure_ascii=False) + "\n")


def register(dataset_id: str, frame, *, source_id: str | None = None, shape: str = "derived",
             title: str = "", origin_url: str = "", notes: str = "") -> dict:
    """frame: a pandas DataFrame or a path to a parquet/csv/geojson file."""
    import pandas as pd

    assert shape in SHAPES, f"shape must be one of {SHAPES}"
    dataset_id = _sanitize_id(dataset_id)
    WH.mkdir(exist_ok=True)
    parquet = WH / f"{dataset_id}.parquet"

    if isinstance(frame, (str, pathlib.Path)):
        src = pathlib.Path(frame)
        if src.suffix == ".parquet":
            df = pd.read_parquet(src)
        elif src.suffix in (".geojson", ".json"):
            df = _read_geojson(src)
        else:
            df = pd.read_csv(src, low_memory=False)
    else:
        df = frame

    spatial = any(c.lower() in ("geometry", "the_geom", "wkt", "geom") for c in df.columns) or \
        {"latitude", "longitude"}.issubset({c.lower() for c in df.columns})
    # de-duplicate column names (some GeoJSON / CSV feeds repeat them)
    seen: dict[str, int] = {}
    cols = []
    for c in (str(x) for x in df.columns):
        seen[c] = seen.get(c, 0) + 1
        cols.append(c if seen[c] == 1 else f"{c}_{seen[c]}")
    df.columns = cols
    try:
        df.to_parquet(parquet, index=False)
    except Exception:  # mixed-type object columns - stringify every object column and retry
        for col in list(df.columns):
            if df[col].dtype == object:
                df[col] = df[col].astype("string")
        df.to_parquet(parquet, index=False)

    cols = [{"name": str(c), "type": str(t)} for c, t in df.dtypes.items()]
    rec = {
        "dataset_id": dataset_id, "source_id": source_id, "shape": shape,
        "title": title or dataset_id, "origin_url": origin_url, "rows": int(len(df)),
        "columns": cols, "spatial": bool(spatial),
        "fetched_at": dt.datetime.now(dt.timezone.utc).replace(microsecond=0).isoformat(),
        "parquet": parquet.name, "notes": notes,
    }

    con = _duck()
    con.execute("DELETE FROM _datasets WHERE dataset_id = ?", [dataset_id])
    con.execute(
        "INSERT INTO _datasets VALUES (?,?,?,?,?,?,?,?,?,?,?)",
        [dataset_id, source_id, shape, rec["title"], origin_url, rec["rows"],
         json.dumps(cols), rec["spatial"], rec["fetched_at"], parquet.name, notes],
    )
    con.execute(f"CREATE OR REPLACE VIEW {_view_name(dataset_id)} AS "
                f"SELECT * FROM read_parquet('{parquet.as_posix()}')")
    con.close()

    m = _load_manifest()
    m["datasets"][dataset_id] = {k: rec[k] for k in
                                 ("source_id", "shape", "title", "origin_url", "rows",
                                  "spatial", "fetched_at", "parquet", "notes")}
    _save_manifest(m)
    print(f"  registered {dataset_id}  ({rec['rows']:,} rows, {len(cols)} cols"
          f"{', spatial' if spatial else ''})")
    return rec


def _read_geojson(path: pathlib.Path):
    import pandas as pd
    gj = json.loads(pathlib.Path(path).read_text())
    rows = []
    for feat in gj.get("features", []):
        row = dict(feat.get("properties") or {})
        geom = feat.get("geometry")
        if geom:
            row["geometry"] = json.dumps(geom)
            if geom.get("type") == "Point":
                row["longitude"], row["latitude"] = geom["coordinates"][:2]
        rows.append(row)
    return pd.DataFrame(rows)


def con():
    """Open the warehouse with every dataset available as a view (for notebooks/scripts)."""
    c = _duck()
    for p in sorted(WH.glob("*.parquet")):
        c.execute(f"CREATE OR REPLACE VIEW {_view_name(p.stem)} AS "
                  f"SELECT * FROM read_parquet('{p.as_posix()}')")
    return c


def _cmd_init(_):
    WH.mkdir(exist_ok=True)
    _duck().close()
    if not MANIFEST.exists():
        _save_manifest(_load_manifest())
    print(f"warehouse ready at {DB.relative_to(REPO)}")


def _cmd_list(_):
    m = _load_manifest()
    if not m["datasets"]:
        print("(empty — run an ingester)")
        return
    print(f"{'dataset_id':32} {'shape':11} {'rows':>10}  title")
    for did, d in sorted(m["datasets"].items()):
        print(f"{did:32} {d['shape']:11} {d['rows']:>10,}  {d['title'][:60]}")
    print(f"\n{len(m['datasets'])} datasets · manifest {MANIFEST.relative_to(REPO)}")


def _cmd_query(a):
    c = con()
    try:
        c.sql(a.sql).show(max_rows=40)
    finally:
        c.close()


def _cmd_drop(a):
    (WH / f"{a.dataset_id}.parquet").unlink(missing_ok=True)
    c = _duck()
    c.execute("DELETE FROM _datasets WHERE dataset_id = ?", [a.dataset_id])
    c.close()
    m = _load_manifest()
    m["datasets"].pop(a.dataset_id, None)
    _save_manifest(m)
    print(f"dropped {a.dataset_id}")


def main() -> None:
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    sub = ap.add_subparsers(dest="cmd", required=True)
    sub.add_parser("init").set_defaults(fn=_cmd_init)
    sub.add_parser("list").set_defaults(fn=_cmd_list)
    q = sub.add_parser("query"); q.add_argument("sql"); q.set_defaults(fn=_cmd_query)
    d = sub.add_parser("drop"); d.add_argument("dataset_id"); d.set_defaults(fn=_cmd_drop)
    a = ap.parse_args()
    a.fn(a)


if __name__ == "__main__":
    sys.exit(main())
