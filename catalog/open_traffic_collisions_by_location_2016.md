# Traffic Collisions by Location 2016

`open_traffic_collisions_by_location_2016` · shape **arcgis-hub** · source `open-ottawa` · **spatial**

- origin: <https://open.ottawa.ca/datasets/ottawa::traffic-collisions-by-location-2016>
- fetched 2026-09-09 · **5,731 rows** · 13 columns
- geojson · licence: https://ottawa.ca/en/city-hall/get-know-your-city/open-data#open-data-licence-ve

## Columns

| column | kind | non-null | distinct | summary |
| --- | --- | --- | --- | --- |
| `LOCATION` | id/text | 100% | 5,731 | e.g. BEECHWOOD AVE @ STE. C, BEECHWOOD AVE btwn CHA, BEECHWOOD AVE btwn COR |
| `GEO_ID` | id/text | 100% | 5,731 | e.g. 5752, __3ZA3AY, __3ZBN9V |
| `TOTAL_COLLISIONS` | num | 100% | 35 | 1.00 · p25 1.00 · p50 1.00 · p95 8.00 · max 59.00  █▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁ |
| `CYCLIST_COLLISIONS` | num | 100% | 4 | 0.00 · p25 0.00 · p50 0.00 · p95 0.00 · max 5.00  █▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁ |
| `PEDESTRIAN_COLLISIONS` | num | 100% | 6 | 0.00 · p25 0.00 · p50 0.00 · p95 1.00 · max 6.00  █▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁ |
| `X` | num | 100% | 5,643 | 318,518 · p25 362,910 · p50 367,742 · p95 384,429 · max 401,542  ▁▁▁▁▁▁▂▂▄█▄▂▂▁▁▁ |
| `Y` | num | 100% | 5,389 | 4,982,810 · p25 5,020,957 · p50 5,027,052 · p95 5,036,666 · max 5,043,428  ▁▁▁▁▁▁▁▁▃▃▅▅█▅▂▁ |
| `LONGITUDE` | num | 100% | 5,379 | -76.32 · p25 -75.76 · p50 -75.70 · p95 -75.48 · max -75.27  ▁▁▁▁▁▁▂▂▄█▄▂▂▁▁▁ |
| `LATITUDE` | num | 100% | 5,466 | 44.98 · p25 45.33 · p50 45.38 · p95 45.47 · max 45.52  ▁▁▁▁▁▁▁▁▃▃▅▅█▅▂▁ |
| `FID` | num | 100% | 5,731 | 1.00 · p25 1,434 · p50 2,866 · p95 5,444 · max 5,731  █▇▇▇▇▇▇█▇▇▇▇▇▇▇█ |
| `geometry` | id/text | 100% | 5,730 | e.g. {"type": "Point", "coo, {"type": "Point", "coo, {"type": "Point", "coo |
| `longitude` | num | 100% | 5,379 | -76.32 · p25 -75.76 · p50 -75.70 · p95 -75.48 · max -75.27  ▁▁▁▁▁▁▂▂▄█▄▂▂▁▁▁ |
| `latitude` | num | 100% | 5,466 | 44.98 · p25 45.33 · p50 45.38 · p95 45.47 · max 45.52  ▁▁▁▁▁▁▁▁▃▃▅▅█▅▂▁ |

## Candidate questions

- Spatial clustering of open_traffic_collisions_by_location_2016; overlay wards + the decision timeline

_profiled 2026-09-09 · `python3 tools/profile.py open_traffic_collisions_by_location_2016`_
