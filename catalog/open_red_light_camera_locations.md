# Red Light Camera Locations

`open_red_light_camera_locations` · shape **arcgis-hub** · source `open-ottawa` · **spatial**

- origin: <https://open.ottawa.ca/datasets/ottawa::red-light-camera-locations>
- fetched 2026-09-09 · **88 rows** · 12 columns
- geojson · licence: https://ottawa.ca/en/city-hall/get-know-your-city/open-data#open-data-licence-ve

## Columns

| column | kind | non-null | distinct | summary |
| --- | --- | --- | --- | --- |
| `location_desc` | id/text | 100% | 81 | e.g. Walkley Road and Russe, St. Laurent Boulevard , March Road/Eaglson Roa |
| `location_desc_fr` | id/text | 100% | 81 | e.g. Chemin Walkley et Chem, Boulevard St. Laurent , Chemin March/Eaglson e |
| `CAMERA_INSTALL_YEAR` | num | 97% | 13 | 2,001 · p25 2,010 · p50 2,017 · p95 2,022 · max 2,025  ▃▁▁▁▃▄▂▁▁▁▄▃▂█▁▁ |
| `LATITUDE` | num | 97% | 80 | 45.27 · p25 45.37 · p50 45.39 · p95 45.48 · max 45.48  ▃▃▁▁▁▂▄▆█▄█▆▃▁▁▄ |
| `LONGITUDE` | num | 97% | 80 | -76.02 · p25 -75.73 · p50 -75.69 · p95 -75.51 · max -75.49  ▁▁▁▁▁▁▁▂▄█▄▅▂▁▁▂ |
| `X` | num | 97% | 80 | 342,165 · p25 365,375 · p50 368,213 · p95 381,952 · max 384,073  ▁▁▁▁▁▁▁▂▄█▄▅▂▁▁▂ |
| `Y` | num | 97% | 80 | 5,014,578 · p25 5,025,418 · p50 5,028,249 · p95 5,037,827 · max 5,038,786  ▃▂▁▁▁▂▄▆▇▄█▅▄▁▁▄ |
| `CAMERA_FACING` | cat | 97% | 4 | Eastbound 29%, Northbound 27%, Southbound 24%, Westbound 20% |
| `ObjectId` | num | 100% | 88 | 1.00 · p25 22.75 · p50 44.50 · p95 83.65 · max 88.00  █▆█▆█▆█▆▆█▆█▆█▆█ |
| `geometry` | id/text | 97% | 80 | e.g. {"type": "Point", "coo, {"type": "Point", "coo, {"type": "Point", "coo |
| `longitude` | num | 97% | 80 | -76.02 · p25 -75.73 · p50 -75.69 · p95 -75.51 · max -75.49  ▁▁▁▁▁▁▁▂▄█▄▅▂▁▁▂ |
| `latitude` | num | 97% | 80 | 45.27 · p25 45.37 · p50 45.39 · p95 45.48 · max 45.48  ▃▃▁▁▁▂▄▆█▄█▆▃▁▁▄ |

## Candidate questions

- (none templated)

_profiled 2026-09-09 · `python3 tools/profile.py open_red_light_camera_locations`_
