# Automated Speed Enforcement Camera Violations 2024

`open_automated_speed_enforcement_camera_violations_2024` · shape **arcgis-hub** · source `open-ottawa` · **spatial**

- origin: <https://open.ottawa.ca/datasets/ottawa::automated-speed-enforcement-camera-violations-2024>
- fetched 2026-09-09 · **60 rows** · 21 columns
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
| `January` | num | 48% | 29 | 107 · p25 268 · p50 502 · p95 1,444 · max 1,785  █▆▃█▂▂▃▁▃▂▂▅▁▂▁▂ |
| `February` | num | 66% | 37 | 0.00 · p25 234 · p50 398 · p95 1,629 · max 2,021  ▇█▇▅▄▅▅▁▁▂▃▁▂▁▁▃ |
| `March` | num | 66% | 39 | 126 · p25 339 · p50 756 · p95 2,483 · max 7,569  █▅▅▁▁▁▁▁▁▁▁▁▁▁▁▁ |
| `April` | num | 66% | 39 | 88.00 · p25 281 · p50 634 · p95 2,253 · max 5,803  █▄▂▄▁▁▁▁▁▁▁▁▁▁▁▁ |
| `May` | num | 66% | 37 | 71.00 · p25 296 · p50 524 · p95 1,973 · max 4,778  █▃▃▄▁▁▁▁▁▁▁▁▁▁▁▁ |
| `June` | num | 66% | 40 | 63.00 · p25 244 · p50 550 · p95 2,423 · max 10,592  █▃▂▁▁▁▁▁▁▁▁▁▁▁▁▁ |
| `July` | num | 66% | 38 | 0.00 · p25 83.25 · p50 407 · p95 2,253 · max 7,096  █▃▂▂▁▁▁▁▁▁▁▁▁▁▁▁ |
| `August` | num | 66% | 37 | 0.00 · p25 78.00 · p50 441 · p95 1,898 · max 6,337  █▂▂▃▂▁▁▁▁▁▁▁▁▁▁▁ |
| `September` | num | 66% | 39 | 0.00 · p25 216 · p50 480 · p95 1,653 · max 5,382  █▄▂▃▁▁▁▁▁▁▁▁▁▁▁▁ |
| `October` | num | 66% | 40 | 55.00 · p25 288 · p50 530 · p95 1,807 · max 4,963  █▄▂▄▁▁▁▁▁▁▁▁▁▁▁▁ |
| `November` | num | 81% | 47 | 19.00 · p25 168 · p50 330 · p95 1,213 · max 3,234  █▄▂▃▂▂▁▁▁▁▁▁▁▁▁▁ |
| `December` | num | 95% | 56 | 39.00 · p25 221 · p50 391 · p95 1,615 · max 3,530  █▇▃▃▁▂▂▁▁▁▁▁▁▁▁▁ |
| `Total_Violations` | num | 100% | 58 | 0.00 · p25 1,018 · p50 2,916 · p95 16,345 · max 59,656  █▂▂▂▁▁▁▁▁▁▁▁▁▁▁▁ |
| `Highest_Monthly_Total` | num | 100% | 58 | 0.00 · p25 332 · p50 690 · p95 2,328 · max 10,592  █▄▃▁▁▁▁▁▁▁▁▁▁▁▁▁ |
| `ObjectId` | num | 100% | 60 | 1.00 · p25 15.75 · p50 30.50 · p95 57.05 · max 60.00  ███▆██▆██▆██▆███ |

## Candidate questions

- (none templated)

_profiled 2026-09-09 · `python3 tools/profile.py open_automated_speed_enforcement_camera_violations_2024`_
