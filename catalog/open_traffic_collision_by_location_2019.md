# Traffic Collision by Location 2019

`open_traffic_collision_by_location_2019` · shape **arcgis-hub** · source `open-ottawa` · **spatial**

- origin: <https://open.ottawa.ca/datasets/ottawa::traffic-collision-by-location-2019>
- fetched 2026-09-09 · **6,074 rows** · 13 columns
- geojson · licence: https://ottawa.ca/en/city-hall/get-know-your-city/open-data#open-data-licence-ve

## Columns

| column | kind | non-null | distinct | summary |
| --- | --- | --- | --- | --- |
| `Location` | id/text | 100% | 6,074 | e.g. HIGHWAY 417 btwn HIGHW, OTTAWA ROAD 29 btwn BI, MADAWASKA BLVD btwn CO |
| `Geo_ID` | id/text | 100% | 6,074 | e.g. __5SO7SU, __5SO6A3, __5SPK8W |
| `Total_Collisions` | num | 100% | 42 | 1.00 · p25 1.00 · p50 1.00 · p95 9.00 · max 61.00  █▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁ |
| `Cyclists_Collisions` | num | 100% | 4 | 0.00 · p25 0.00 · p50 0.00 · p95 0.00 · max 3.00  █▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁ |
| `Pedestrian_collisions` | num | 100% | 5 | 0.00 · p25 0.00 · p50 0.00 · p95 0.00 · max 4.00  █▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁ |
| `X` | num | 100% | 6,043 | 317,410 · p25 362,943 · p50 367,657 · p95 384,051 · max 400,712  ▁▁▁▁▁▁▂▁▃█▄▂▂▁▁▁ |
| `Y` | num | 100% | 6,028 | 4,982,098 · p25 5,020,800 · p50 5,026,938 · p95 5,036,260 · max 5,043,414  ▁▁▁▁▁▁▁▁▃▃▄▅█▅▂▁ |
| `Latitude` | num | 100% | 6,074 | 44.98 · p25 45.32 · p50 45.38 · p95 45.46 · max 45.52  ▁▁▁▁▁▁▁▁▃▃▄▅█▅▂▁ |
| `Longitude` | num | 100% | 6,074 | -76.34 · p25 -75.76 · p50 -75.70 · p95 -75.49 · max -75.27  ▁▁▁▁▁▁▂▁▃█▄▂▂▁▁▁ |
| `ObjectId` | num | 100% | 6,074 | 1.00 · p25 1,519 · p50 3,038 · p95 5,770 · max 6,074  ██▇█▇█▇██▇█▇█▇██ |
| `geometry` | id/text | 100% | 6,074 | e.g. {"type": "Point", "coo, {"type": "Point", "coo, {"type": "Point", "coo |
| `longitude` | num | 100% | 6,074 | -76.34 · p25 -75.76 · p50 -75.70 · p95 -75.49 · max -75.27  ▁▁▁▁▁▁▂▁▃█▄▂▂▁▁▁ |
| `latitude` | num | 100% | 6,074 | 44.98 · p25 45.32 · p50 45.38 · p95 45.46 · max 45.52  ▁▁▁▁▁▁▁▁▃▃▄▅█▅▂▁ |

## Candidate questions

- Spatial clustering of open_traffic_collision_by_location_2019; overlay wards + the decision timeline

_profiled 2026-09-09 · `python3 tools/profile.py open_traffic_collision_by_location_2019`_
