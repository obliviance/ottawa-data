# Traffic Collisions by Location 2013

`open_traffic_collisions_by_location_2013` · shape **arcgis-hub** · source `open-ottawa` · **spatial**

- origin: <https://open.ottawa.ca/datasets/ottawa::traffic-collisions-by-location-2013>
- fetched 2026-09-09 · **5,754 rows** · 13 columns
- geojson · licence: https://ottawa.ca/en/city-hall/get-know-your-city/open-data#open-data-licence-ve

## Columns

| column | kind | non-null | distinct | summary |
| --- | --- | --- | --- | --- |
| `RECORD` | num | 100% | 5,754 | 1.00 · p25 1,439 · p50 2,878 · p95 5,466 · max 5,754  ██▇█▇█▇██▇█▇█▇██ |
| `LOCATION___GEOID` | id/text | 100% | 5,754 | e.g. CARP RD @ RICHARDSON S, CARP RD @ ROTHBOURNE R, CARP RD @ STITTSVILLE  |
| `TOTAL_COLLISIONS` | num | 100% | 37 | 1.00 · p25 1.00 · p50 1.00 · p95 9.00 · max 64.00  █▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁ |
| `CYCLIST_COLLISIONS` | num | 100% | 4 | 0.00 · p25 0.00 · p50 0.00 · p95 1.00 · max 3.00  █▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁ |
| `PEDESTRIAN_COLLISIONS` | num | 100% | 5 | 0.00 · p25 0.00 · p50 0.00 · p95 1.00 · max 4.00  █▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁ |
| `XCOORD` | num | 100% | 5,722 | 317,822 · p25 362,772 · p50 367,561 · p95 384,065 · max 400,712  ▁▁▁▁▁▁▂▁▄█▄▂▂▁▁▁ |
| `YCOORD` | num | 100% | 5,710 | 4,981,942 · p25 5,021,018 · p50 5,026,960 · p95 5,036,700 · max 5,043,414  ▁▁▁▁▁▁▁▁▃▃▅▅█▅▂▁ |
| `LONGITUDE` | num | 100% | 5,754 | -76.33 · p25 -75.76 · p50 -75.70 · p95 -75.49 · max -75.27  ▁▁▁▁▁▁▂▁▄█▄▂▂▁▁▁ |
| `LATITUDE` | num | 100% | 5,754 | 44.98 · p25 45.33 · p50 45.38 · p95 45.47 · max 45.52  ▁▁▁▁▁▁▁▁▃▃▄▅█▅▂▁ |
| `ObjectId` | num | 100% | 5,754 | 1.00 · p25 1,439 · p50 2,878 · p95 5,466 · max 5,754  ██▇█▇█▇██▇█▇█▇██ |
| `geometry` | id/text | 100% | 5,754 | e.g. {"type": "Point", "coo, {"type": "Point", "coo, {"type": "Point", "coo |
| `longitude` | num | 100% | 5,754 | -76.33 · p25 -75.76 · p50 -75.70 · p95 -75.49 · max -75.27  ▁▁▁▁▁▁▂▁▄█▄▂▂▁▁▁ |
| `latitude` | num | 100% | 5,754 | 44.98 · p25 45.33 · p50 45.38 · p95 45.47 · max 45.52  ▁▁▁▁▁▁▁▁▃▃▄▅█▅▂▁ |

## Candidate questions

- Spatial clustering of open_traffic_collisions_by_location_2013; overlay wards + the decision timeline

_profiled 2026-09-09 · `python3 tools/profile.py open_traffic_collisions_by_location_2013`_
