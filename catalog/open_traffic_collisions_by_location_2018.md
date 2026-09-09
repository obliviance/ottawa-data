# Traffic Collisions by Location 2018

`open_traffic_collisions_by_location_2018` · shape **arcgis-hub** · source `open-ottawa` · **spatial**

- origin: <https://open.ottawa.ca/datasets/ottawa::traffic-collisions-by-location-2018>
- fetched 2026-09-09 · **5,585 rows** · 13 columns
- geojson · licence: https://ottawa.ca/en/city-hall/get-know-your-city/open-data#open-data-licence-ve

## Columns

| column | kind | non-null | distinct | summary |
| --- | --- | --- | --- | --- |
| `LOCATION` | id/text | 100% | 5,585 | e.g. 130 W OF PRESTON ST @ , 210 W OF MERIVALE RD @, 225 E OF RIVERSIDE DR  |
| `GEO_ID` | id/text | 100% | 5,585 | e.g. 16879, 4688, 13516 |
| `TOTAL_COLLISIONS` | num | 100% | 39 | 1.00 · p25 1.00 · p50 1.00 · p95 9.00 · max 59.00  █▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁ |
| `CYCLIST_COLLISIONS` | num | 100% | 5 | 0.00 · p25 0.00 · p50 0.00 · p95 0.00 · max 4.00  █▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁ |
| `PEDESTRIAN_COLLISIONS` | num | 100% | 4 | 0.00 · p25 0.00 · p50 0.00 · p95 1.00 · max 3.00  █▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁ |
| `X` | num | 100% | 5,550 | 317,753 · p25 362,671 · p50 367,641 · p95 383,933 · max 401,475  ▁▁▁▁▁▁▂▂▄█▄▂▂▁▁▁ |
| `Y` | num | 100% | 5,541 | 4,982,098 · p25 5,020,569 · p50 5,026,894 · p95 5,036,602 · max 5,043,428  ▁▁▁▁▁▁▁▁▃▃▅▅█▅▂▁ |
| `LONGITUDE` | num | 100% | 5,584 | -76.33 · p25 -75.76 · p50 -75.70 · p95 -75.49 · max -75.27  ▁▁▁▁▁▁▂▂▄█▄▂▂▁▁▁ |
| `LATITUDE` | num | 100% | 5,582 | 44.98 · p25 45.32 · p50 45.38 · p95 45.47 · max 45.52  ▁▁▁▁▁▁▁▁▃▃▄▅█▅▂▁ |
| `ObjectId` | num | 100% | 5,585 | 1.00 · p25 1,397 · p50 2,793 · p95 5,306 · max 5,585  █▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇ |
| `geometry` | id/text | 100% | 5,584 | e.g. {"type": "Point", "coo, {"type": "Point", "coo, {"type": "Point", "coo |
| `longitude` | num | 100% | 5,584 | -76.33 · p25 -75.76 · p50 -75.70 · p95 -75.49 · max -75.27  ▁▁▁▁▁▁▂▂▄█▄▂▂▁▁▁ |
| `latitude` | num | 100% | 5,582 | 44.98 · p25 45.32 · p50 45.38 · p95 45.47 · max 45.52  ▁▁▁▁▁▁▁▁▃▃▄▅█▅▂▁ |

## Candidate questions

- Spatial clustering of open_traffic_collisions_by_location_2018; overlay wards + the decision timeline

_profiled 2026-09-09 · `python3 tools/profile.py open_traffic_collisions_by_location_2018`_
