# Automated Speed Enforcement Camera - Speed Data

`open_automated_speed_enforcement_camera_speed_data` · shape **arcgis-hub** · source `open-ottawa` · **spatial**

- origin: <https://open.ottawa.ca/datasets/ottawa::automated-speed-enforcement-camera-speed-data>
- fetched 2026-09-09 · **1,720 rows** · 12 columns
- csv · licence: https://ottawa.ca/en/city-hall/get-know-your-city/open-data#open-data-licence-ve

## Columns

| column | kind | non-null | distinct | summary |
| --- | --- | --- | --- | --- |
| `Location` | text | 100% | 60 | e.g. E012 - Abbott St. E be, E013 - St-Laurent Blvd, E014 - Tenth Line Rd.  |
| `Camera_Install_Year` | num | 100% | 5 | 2,020 · p25 2,020 · p50 2,022 · p95 2,024 · max 2,025  █▁▁▁▁▁▆▁▁▅▁▁▇▁▁▁ |
| `Latitude` | num | 100% | 60 | 45.19 · p25 45.29 · p50 45.36 · p95 45.47 · max 45.48  ▁▁▁▁▅█▃▃▄▆▄▃▁▆▂▆ |
| `Longitude` | num | 100% | 60 | -75.94 · p25 -75.78 · p50 -75.71 · p95 -75.47 · max -75.42  ▅▅▂▁▆█▇▇▄▆▅▂▁▂▆▁ |
| `X` | num | 100% | 60 | 348,685 · p25 360,933 · p50 366,806 · p95 385,671 · max 389,547  ▄▄▂▁▅▄█▆▅▄▄▂▁▂▅▁ |
| `Y` | num | 100% | 60 | 5,005,291 · p25 5,016,842 · p50 5,024,854 · p95 5,037,365 · max 5,038,179  ▁▁▁▁▆█▃▄▆▅▄▄▁▆▂▆ |
| `Date` | date | 100% | 65 | 2020-07-01 → 2025-11-01, 38 gaps >30d |
| `AvgSpeed` | num | 97% | 214 | 27.50 · p25 35.90 · p50 38.00 · p95 55.00 · max 62.00  ▁▁▂█▇▃▂▂▂▂▁▂▂▁▁▁ |
| `Pct85th` | num | 100% | 37 | 0.00 · p25 40.00 · p50 44.00 · p95 61.00 · max 71.00  ▁▁▁▁▁▁▁▁▂█▃▃▁▂▁▁ |
| `PctCompliance` | num | 97% | 252 | 30.00 · p25 78.03 · p50 86.40 · p95 95.50 · max 100  ▁▁▁▁▁▁▁▁▂▂▃▃▅█▆▂ |
| `PctHighEndSpeeders` | num | 100% | 191 | 0.00 · p25 0.15 · p50 0.31 · p95 2.70 · max 12.20  █▂▁▁▁▁▁▁▁▁▁▁▁▁▁▁ |
| `ObjectId` | num | 100% | 1,720 | 1.00 · p25 431 · p50 860 · p95 1,634 · max 1,720  █▇█▇█▇█▇▇█▇█▇█▇█ |

## Candidate questions

- Trend / seasonality of open_automated_speed_enforcement_camera_speed_data over `Camera_Install_Year`; structural breaks?
- Spatial clustering of open_automated_speed_enforcement_camera_speed_data; overlay wards + the decision timeline

_profiled 2026-09-09 · `python3 tools/profile.py open_automated_speed_enforcement_camera_speed_data`_
