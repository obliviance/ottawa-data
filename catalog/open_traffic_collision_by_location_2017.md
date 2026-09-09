# Traffic Collision by Location 2017

`open_traffic_collision_by_location_2017` · shape **arcgis-hub** · source `open-ottawa` · **spatial**

- origin: <https://open.ottawa.ca/datasets/ottawa::traffic-collision-by-location-2017>
- fetched 2026-09-09 · **5,472 rows** · 13 columns
- geojson · licence: https://ottawa.ca/en/city-hall/get-know-your-city/open-data#open-data-licence-ve

## Columns

| column | kind | non-null | distinct | summary |
| --- | --- | --- | --- | --- |
| `LOCATION` | id/text | 100% | 5,472 | e.g. 210 W OF MERIVALE RD @, 225 E OF RIVERSIDE DR , 2ND LINE RD @ CABIN RD |
| `GEO_ID` | id/text | 100% | 5,472 | e.g. 4688, 13516, 5821 |
| `TOTAL_COLLISIONS` | num | 100% | 41 | 1.00 · p25 1.00 · p50 1.00 · p95 9.00 · max 54.00  █▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁ |
| `CYCLIST_COLLISIONS` | num | 100% | 4 | 0.00 · p25 0.00 · p50 0.00 · p95 0.00 · max 3.00  █▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁ |
| `PEDESTRIAN_COLLISIONS` | num | 100% | 4 | 0.00 · p25 0.00 · p50 0.00 · p95 1.00 · max 3.00  █▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁ |
| `X` | num | 100% | 5,387 | 317,850 · p25 362,746 · p50 367,664 · p95 384,399 · max 400,270  ▁▁▁▁▁▁▂▁▃█▅▂▂▁▁▁ |
| `Y` | num | 100% | 5,158 | 4,982,098 · p25 5,020,951 · p50 5,026,961 · p95 5,036,354 · max 5,043,414  ▁▁▁▁▁▁▁▁▃▃▅▅█▅▂▁ |
| `LONGITUDE` | num | 100% | 5,155 | -76.33 · p25 -75.76 · p50 -75.70 · p95 -75.48 · max -75.28  ▁▁▁▁▁▁▂▁▃█▅▂▂▁▁▁ |
| `LATITUDE` | num | 100% | 5,260 | 44.98 · p25 45.33 · p50 45.38 · p95 45.46 · max 45.52  ▁▁▁▁▁▁▁▁▃▃▅▅█▅▂▁ |
| `FID` | num | 100% | 5,472 | 1.00 · p25 1,369 · p50 2,736 · p95 5,198 · max 5,472  ████████████████ |
| `geometry` | id/text | 100% | 5,471 | e.g. {"type": "Point", "coo, {"type": "Point", "coo, {"type": "Point", "coo |
| `longitude` | num | 100% | 5,155 | -76.33 · p25 -75.76 · p50 -75.70 · p95 -75.48 · max -75.28  ▁▁▁▁▁▁▂▁▃█▅▂▂▁▁▁ |
| `latitude` | num | 100% | 5,260 | 44.98 · p25 45.33 · p50 45.38 · p95 45.46 · max 45.52  ▁▁▁▁▁▁▁▁▃▃▅▅█▅▂▁ |

## Candidate questions

- Spatial clustering of open_traffic_collision_by_location_2017; overlay wards + the decision timeline

_profiled 2026-09-09 · `python3 tools/profile.py open_traffic_collision_by_location_2017`_
