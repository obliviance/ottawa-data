# Automated Speed Enforcement Camera Violations 2025

`open_automated_speed_enforcement_camera_violations_2025` · shape **arcgis-hub** · source `open-ottawa` · **spatial**

- origin: <https://open.ottawa.ca/datasets/ottawa::automated-speed-enforcement-camera-violations-2025>
- fetched 2026-09-09 · **60 rows** · 22 columns
- csv · licence: https://ottawa.ca/en/city-hall/get-know-your-city/open-data#open-data-licence-ve

## Columns

| column | kind | non-null | distinct | summary |
| --- | --- | --- | --- | --- |
| `Location` | id/text | 100% | 60 | e.g. E001 - Longfields Dr. , E002 - Innes Rd. betwe, E003 - Bayshore Dr. be |
| `Camera_Install_Year` | num | 100% | 5 | 2,020 · p25 2,022 · p50 2,024 · p95 2,024 · max 2,025  ▂▁▁▁▁▁▃▁▁▃▁▁█▁▁▁ |
| `Latitude` | num | 100% | 60 | 45.19 · p25 45.28 · p50 45.36 · p95 45.47 · max 45.48  ▁▁▁▁▅█▂▅▃▆▄▃▂▅▃▄ |
| `Longitude` | num | 100% | 60 | -75.94 · p25 -75.78 · p50 -75.70 · p95 -75.47 · max -75.42  ▄▃▂▂▃▄▆█▄▃▃▁▁▁▃▁ |
| `X` | num | 100% | 60 | 348,685 · p25 361,265 · p50 367,146 · p95 385,078 · max 389,547  ▄▃▂▂▃▃▇█▅▃▃▁▁▁▃▁ |
| `Y` | num | 100% | 60 | 5,005,291 · p25 5,016,372 · p50 5,024,205 · p95 5,037,115 · max 5,038,179  ▁▁▁▁▇█▂▆▄▆▅▃▂▆▃▅ |
| `January` | num | 100% | 58 | 0.00 · p25 163 · p50 333 · p95 1,868 · max 3,336  █▆▃▃▁▂▁▁▁▁▁▁▁▁▁▁ |
| `February` | num | 100% | 57 | 10.00 · p25 107 · p50 224 · p95 1,027 · max 1,885  █▅▄▂▂▂▁▁▁▁▁▁▁▁▁▁ |
| `March` | num | 100% | 58 | 36.00 · p25 154 · p50 360 · p95 1,447 · max 3,398  █▄▃▃▂▁▁▁▁▁▁▁▁▁▁▁ |
| `April` | num | 100% | 57 | 26.00 · p25 170 · p50 316 · p95 1,480 · max 3,543  █▅▃▃▁▁▁▁▁▁▁▁▁▁▁▁ |
| `May` | num | 100% | 58 | 19.00 · p25 131 · p50 267 · p95 1,305 · max 3,604  █▅▁▂▁▁▁▁▁▁▁▁▁▁▁▁ |
| `June` | num | 100% | 59 | 12.00 · p25 119 · p50 266 · p95 1,077 · max 3,481  █▅▂▂▂▁▁▁▁▁▁▁▁▁▁▁ |
| `July` | num | 100% | 55 | 0.00 · p25 46.50 · p50 212 · p95 1,524 · max 3,680  █▃▁▂▁▁▁▁▁▁▁▁▁▁▁▁ |
| `August` | num | 100% | 54 | 0.00 · p25 39.75 · p50 263 · p95 1,645 · max 3,335  █▄▂▂▂▁▁▁▁▁▁▁▁▁▁▁ |
| `September` | num | 100% | 59 | 11.00 · p25 114 · p50 243 · p95 1,433 · max 2,926  █▅▂▂▁▁▁▁▁▁▁▁▁▁▁▁ |
| `October` | num | 100% | 57 | 8.00 · p25 135 · p50 294 · p95 1,240 · max 3,198  █▅▂▂▁▁▁▁▁▁▁▁▁▁▁▁ |
| `November` | num | 100% | 57 | 0.00 · p25 39.75 · p50 83.00 · p95 300 · max 796  ▇█▃▄▂▁▁▁▁▁▁▁▁▁▁▁ |
| `December` | text | 0% | 0 | e.g.  |
| `Total_Violations` | num | 100% | 60 | 219 · p25 1,318 · p50 2,986 · p95 11,954 · max 33,144  █▄▂▂▁▂▁▁▁▁▁▁▁▁▁▁ |
| `Highest_Monthly_Total` | num | 100% | 58 | 43.00 · p25 204 · p50 427 · p95 1,986 · max 3,680  █▆▂▂▃▁▁▁▁▁▁▁▁▁▁▁ |
| `ObjectId` | text | 0% | 0 | e.g.  |
| `ObjectId2` | num | 100% | 60 | 1.00 · p25 15.75 · p50 30.50 · p95 57.05 · max 60.00  ███▆██▆██▆██▆███ |

## Candidate questions

- (none templated)

_profiled 2026-09-09 · `python3 tools/profile.py open_automated_speed_enforcement_camera_violations_2025`_
