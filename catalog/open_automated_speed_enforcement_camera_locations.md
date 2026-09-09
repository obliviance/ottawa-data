# Automated Speed Enforcement Camera Locations

`open_automated_speed_enforcement_camera_locations` · shape **arcgis-hub** · source `open-ottawa` · **spatial**

- origin: <https://open.ottawa.ca/datasets/ottawa::automated-speed-enforcement-camera-locations>
- fetched 2026-09-09 · **60 rows** · 11 columns
- geojson · licence: https://ottawa.ca/en/city-hall/get-know-your-city/open-data#open-data-licence-ve

## Columns

| column | kind | non-null | distinct | summary |
| --- | --- | --- | --- | --- |
| `ID` | id/text | 100% | 60 | e.g. E001, E002, E003 |
| `Location_Desc_EN` | id/text | 100% | 60 | e.g. Longfields Dr. between, Innes Rd. between Prov, Bayshore Dr. between W |
| `Location_Desc_FR` | id/text | 100% | 60 | e.g. Prom. Longfields entre, Ch. Innes entre Av. Pr, Prom. Bayshore entre C |
| `Latitude` | num | 100% | 60 | 45.19 · p25 45.28 · p50 45.36 · p95 45.47 · max 45.48  ▁▁▁▁▅█▂▅▃▆▄▃▂▅▃▄ |
| `Longitude` | num | 100% | 60 | -75.94 · p25 -75.78 · p50 -75.70 · p95 -75.47 · max -75.42  ▄▃▂▂▃▄▆█▄▃▃▁▁▁▃▁ |
| `X` | num | 100% | 60 | 348,685 · p25 361,265 · p50 367,146 · p95 385,078 · max 389,547  ▄▃▂▂▃▃▇█▅▃▃▁▁▁▃▁ |
| `Y` | num | 100% | 60 | 5,005,291 · p25 5,016,372 · p50 5,024,205 · p95 5,037,115 · max 5,038,179  ▁▁▁▁▇█▂▆▄▆▅▃▂▆▃▅ |
| `ObjectId` | num | 100% | 60 | 1.00 · p25 15.75 · p50 30.50 · p95 57.05 · max 60.00  ███▆██▆██▆██▆███ |
| `geometry` | id/text | 100% | 60 | e.g. {"type": "Point", "coo, {"type": "Point", "coo, {"type": "Point", "coo |
| `longitude` | num | 100% | 60 | -75.94 · p25 -75.78 · p50 -75.70 · p95 -75.47 · max -75.42  ▄▃▂▂▃▄▆█▄▃▃▁▁▁▃▁ |
| `latitude` | num | 100% | 60 | 45.19 · p25 45.28 · p50 45.36 · p95 45.47 · max 45.48  ▁▁▁▁▅█▂▅▃▆▄▃▂▅▃▄ |

## Candidate questions

- (none templated)

_profiled 2026-09-09 · `python3 tools/profile.py open_automated_speed_enforcement_camera_locations`_
