#!/usr/bin/env python3
"""Build the geography spine: spine_wards (24, current — dissolved from the 2022 election
voting-subdivision map) and spine_neighbourhoods (ONS, ~116). Point datasets join to
these for "by ward" / "by neighbourhood" analysis.

    python3 spine/geography.py

v0.1: no ward<->neighbourhood crosswalk yet (needs ST_Intersects area weighting).
"""
from __future__ import annotations

import pathlib
import sys
import tempfile

sys.path.insert(0, str(pathlib.Path(__file__).parent.parent / "tools"))
sys.path.insert(0, str(pathlib.Path(__file__).parent.parent / "tools" / "ingest"))
import warehouse  # noqa: E402
from arcgis_hub import fetch_featureserver  # noqa: E402

VOTING_SUBDIV_FS = ("https://services.arcgis.com/G6F8XLCl5KtAlZ2G/arcgis/rest/services/"
                    "2022_Elections_Voting_Subdivision_Map/FeatureServer/0")
ONS_SRC = "d_open_ottawa_neighbourhood_study_ons_neighbourhood_boundaries_gen_3"


def main() -> None:
    with tempfile.NamedTemporaryFile(suffix=".geojson", delete=False) as tf:
        tmp = pathlib.Path(tf.name)
    n = fetch_featureserver(VOTING_SUBDIV_FS, tmp)
    warehouse.register("vs_staging", tmp, shape="derived", title="voting subdivisions (staging)")
    tmp.unlink(missing_ok=True)

    c = warehouse.con()
    wards = c.execute("""
        SELECT CAST(WARD_NUM AS INT)                                   AS ward_num,
               any_value(WARD)                                          AS ward_name,
               any_value(QUARTIER)                                      AS ward_name_fr,
               count(*)                                                 AS voting_subdivisions,
               ST_AsText(ST_Union_Agg(ST_GeomFromGeoJSON(geometry)))    AS geometry_wkt
        FROM d_vs_staging WHERE WARD_NUM IS NOT NULL
        GROUP BY 1 ORDER BY 1
    """).df()
    warehouse.register("spine_wards", wards, shape="spine",
                       title="spine — Ottawa wards (24, current)",
                       origin_url="https://open.ottawa.ca/datasets/ottawa::2022-elections-voting-subdivision-map",
                       notes="dissolved from the 2022 election voting-subdivision map; geometry as WKT")

    have = {r[0] for r in c.execute("SELECT table_name FROM information_schema.tables").fetchall()}
    n_ons = 0
    if ONS_SRC in have:
        ons = c.execute(f"SELECT * FROM {ONS_SRC}").df()
        nc = next((x for x in ons.columns if x.upper() in
                   ("NAME", "ONS_NAME", "NEIGHBOURHOOD", "NAME_ENGLISH", "NAME1")), None)
        if nc:
            ons = ons.rename(columns={nc: "neighbourhood_name"})
        warehouse.register("spine_neighbourhoods", ons, shape="spine",
                           title="spine — ONS neighbourhoods",
                           origin_url="https://www.neighbourhoodstudy.ca/",
                           notes="Ottawa Neighbourhood Study boundaries (gen 3)")
        n_ons = len(ons)
    c.close()
    warehouse._cmd_drop(type("A", (), {"dataset_id": "vs_staging"}))
    print(f"\nspine_wards: {len(wards)} (fetched {n} subdivisions) · spine_neighbourhoods: {n_ons}")
    print("next: spine/timeline.py, then spine/entities.py")


if __name__ == "__main__":
    main()
