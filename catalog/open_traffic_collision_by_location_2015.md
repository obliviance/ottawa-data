# Traffic Collision by Location 2015

`open_traffic_collision_by_location_2015` · shape **arcgis-hub** · source `open-ottawa` · **spatial**

- origin: <https://open.ottawa.ca/datasets/ottawa::traffic-collision-by-location-2015>
- fetched 2026-09-09 · **5,727 rows** · 13 columns
- geojson · licence: https://ottawa.ca/en/city-hall/get-know-your-city/open-data#open-data-licence-ve

## Columns

| column | kind | non-null | distinct | summary |
| --- | --- | --- | --- | --- |
| `LOCATION` | id/text | 100% | 5,727 | e.g. 210 W OF MERIVALE RD @, 225 E OF RIVERSIDE DR , 240 S OF CHARLEMAGNE B |
| `GEO_ID` | id/text | 100% | 5,727 | e.g. 4688, 13516, 14362 |
| `TOTAL_COLLISIONS` | num | 100% | 39 | 1.00 · p25 1.00 · p50 1.00 · p95 9.00 · max 60.00  █▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁ |
| `CYCLIST_COLLISIONS` | num | 100% | 5 | 0.00 · p25 0.00 · p50 0.00 · p95 0.00 · max 4.00  █▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁ |
| `PEDESTRIAN_COLLISIONS` | num | 100% | 4 | 0.00 · p25 0.00 · p50 0.00 · p95 1.00 · max 3.00  █▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁ |
| `X` | num | 100% | 5,637 | 319,470 · p25 362,920 · p50 367,746 · p95 384,103 · max 401,822  ▁▁▁▁▁▁▂▂▅█▄▂▂▁▁▁ |
| `Y` | num | 100% | 5,389 | 4,981,006 · p25 5,021,208 · p50 5,027,082 · p95 5,036,788 · max 5,043,414  ▁▁▁▁▁▁▁▁▃▃▄▆█▅▂▁ |
| `LONGITUDE` | num | 100% | 5,365 | -76.31 · p25 -75.76 · p50 -75.70 · p95 -75.49 · max -75.26  ▁▁▁▁▁▁▂▂▅█▄▂▂▁▁▁ |
| `LATITUDE` | num | 100% | 5,462 | 44.97 · p25 45.33 · p50 45.38 · p95 45.47 · max 45.52  ▁▁▁▁▁▁▁▁▃▃▄▆█▆▃▁ |
| `FID` | num | 100% | 5,727 | 1.00 · p25 1,432 · p50 2,864 · p95 5,441 · max 5,727  ████████▇███████ |
| `geometry` | id/text | 100% | 5,726 | e.g. {"type": "Point", "coo, {"type": "Point", "coo, {"type": "Point", "coo |
| `longitude` | num | 100% | 5,365 | -76.31 · p25 -75.76 · p50 -75.70 · p95 -75.49 · max -75.26  ▁▁▁▁▁▁▂▂▅█▄▂▂▁▁▁ |
| `latitude` | num | 100% | 5,462 | 44.97 · p25 45.33 · p50 45.38 · p95 45.47 · max 45.52  ▁▁▁▁▁▁▁▁▃▃▄▆█▆▃▁ |

## Candidate questions

- Spatial clustering of open_traffic_collision_by_location_2015; overlay wards + the decision timeline

_profiled 2026-09-09 · `python3 tools/profile.py open_traffic_collision_by_location_2015`_
