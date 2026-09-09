# Traffic Collision by Location 2014

`open_traffic_collision_by_location_2014` · shape **arcgis-hub** · source `open-ottawa` · **spatial**

- origin: <https://open.ottawa.ca/datasets/ottawa::traffic-collision-by-location-2014>
- fetched 2026-09-09 · **5,694 rows** · 13 columns
- geojson · licence: https://ottawa.ca/en/city-hall/get-know-your-city/open-data#open-data-licence-ve

## Columns

| column | kind | non-null | distinct | summary |
| --- | --- | --- | --- | --- |
| `LOCATION` | id/text | 100% | 5,694 | e.g. 210 W OF MERIVALE RD @, 225 E OF RIVERSIDE DR , 2ND LINE RD btwn DALME |
| `GEO_ID` | id/text | 100% | 5,694 | e.g. 4688, 13516, __3ZBOYY |
| `TOTAL_COLLISIONS` | num | 100% | 40 | 1.00 · p25 1.00 · p50 1.00 · p95 9.00 · max 63.00  █▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁ |
| `CYCLIST_COLLISIONS` | num | 100% | 4 | 0.00 · p25 0.00 · p50 0.00 · p95 0.00 · max 3.00  █▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁ |
| `PEDESTRIAN_COLLISIONS` | num | 100% | 5 | 0.00 · p25 0.00 · p50 0.00 · p95 0.00 · max 4.00  █▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁ |
| `X` | num | 100% | 5,608 | 317,850 · p25 362,932 · p50 367,713 · p95 383,955 · max 401,542  ▁▁▁▁▁▁▂▂▄█▄▂▂▁▁▁ |
| `Y` | num | 100% | 5,379 | 4,982,098 · p25 5,021,079 · p50 5,026,828 · p95 5,036,701 · max 5,043,264  ▁▁▁▁▁▁▁▁▃▃▅▅█▅▂▁ |
| `LONGITUDE` | num | 100% | 5,364 | -76.33 · p25 -75.76 · p50 -75.70 · p95 -75.49 · max -75.27  ▁▁▁▁▁▁▂▂▄█▄▂▂▁▁▁ |
| `LATITUDE` | num | 100% | 5,446 | 44.98 · p25 45.33 · p50 45.38 · p95 45.47 · max 45.52  ▁▁▁▁▁▁▁▁▃▃▅▆█▆▂▁ |
| `FID` | num | 100% | 5,694 | 1.00 · p25 1,424 · p50 2,848 · p95 5,409 · max 5,694  █████▇████▇█████ |
| `geometry` | id/text | 100% | 5,694 | e.g. {"type": "Point", "coo, {"type": "Point", "coo, {"type": "Point", "coo |
| `longitude` | num | 100% | 5,364 | -76.33 · p25 -75.76 · p50 -75.70 · p95 -75.49 · max -75.27  ▁▁▁▁▁▁▂▂▄█▄▂▂▁▁▁ |
| `latitude` | num | 100% | 5,446 | 44.98 · p25 45.33 · p50 45.38 · p95 45.47 · max 45.52  ▁▁▁▁▁▁▁▁▃▃▅▆█▆▂▁ |

## Candidate questions

- Spatial clustering of open_traffic_collision_by_location_2014; overlay wards + the decision timeline

_profiled 2026-09-09 · `python3 tools/profile.py open_traffic_collision_by_location_2014`_
