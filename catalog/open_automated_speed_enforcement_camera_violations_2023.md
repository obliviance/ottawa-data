# Automated Speed Enforcement Camera Violations 2023

`open_automated_speed_enforcement_camera_violations_2023` · shape **arcgis-hub** · source `open-ottawa` · **spatial**

- origin: <https://open.ottawa.ca/datasets/ottawa::automated-speed-enforcement-camera-violations-2023>
- fetched 2026-09-09 · **28 rows** · 21 columns
- csv · licence: https://ottawa.ca/en/city-hall/get-know-your-city/open-data#open-data-licence-ve

## Columns

| column | kind | non-null | distinct | summary |
| --- | --- | --- | --- | --- |
| `Location` | id/text | 100% | 28 | e.g. E001 - Longfields Dr. , E002 - Innes Rd. betwe, E003 - Bayshore Dr. ne |
| `Camera_Install_Year` | num | 100% | 4 | 2,020 · p25 2,020 · p50 2,022 · p95 2,023 · max 2,023  ▆▁▁▁▁▄▁▁▁▁▃▁▁▁▁█ |
| `Latitude` | num | 100% | 28 | 45.25 · p25 45.28 · p50 45.35 · p95 45.47 · max 45.48  ▅█▃▂▂▂▃▃▃▁▃▁▂▃▂▅ |
| `Longitude` | num | 100% | 28 | -75.93 · p25 -75.79 · p50 -75.74 · p95 -75.47 · max -75.46  ▆▄▂▁▄▆██▁▄▂▂▂▁▂▆ |
| `X` | num | 100% | 28 | 349,431 · p25 360,489 · p50 364,647 · p95 385,324 · max 386,179  ▆▄▂▁▂███▁▄▂▂▂▁▂▆ |
| `Y` | num | 100% | 28 | 5,012,976 · p25 5,015,900 · p50 5,023,332 · p95 5,037,273 · max 5,038,179  ▅█▃▂▂▂▃▃▃▁▃▁▂▃▂▅ |
| `January` | num | 100% | 17 | 0.00 · p25 0.00 · p50 230 · p95 859 · max 1,160  █▁▂▂▂▂▁▂▁▁▁▁▁▁▁▁ |
| `February` | num | 60% | 17 | 160 · p25 199 · p50 341 · p95 1,450 · max 1,585  █▅▅▃▂▂▁▁▁▁▁▁▁▁▂▂ |
| `March` | num | 60% | 16 | 161 · p25 249 · p50 511 · p95 1,830 · max 2,358  █▃▃▅▂▂▂▁▁▁▁▂▁▁▁▂ |
| `April` | cat | 64% | 18 | 240 6%, 262 6%, 672 6%, 662 6%, 279 6%, 1,230 6% |
| `May` | num | 64% | 18 | 116 · p25 244 · p50 471 · p95 1,900 · max 2,237  █▅▂▅▁▂▂▁▃▁▁▁▁▂▁▂ |
| `June` | num | 71% | 20 | 124 · p25 242 · p50 359 · p95 1,199 · max 1,689  █▃▆▂▂▃▂▁▃▁▂▁▁▁▁▂ |
| `July` | num | 78% | 22 | 4.00 · p25 403 · p50 749 · p95 3,194 · max 3,977  ██▆▂▁▄▂▄▁▁▆▁▂▁▁▂ |
| `August` | num | 82% | 23 | 5.00 · p25 409 · p50 844 · p95 3,482 · max 3,905  ▅█▅▂▃▂▁▂▃▁▃▂▁▁▂▂ |
| `September` | num | 82% | 23 | 167 · p25 409 · p50 778 · p95 2,453 · max 4,434  █▅▄▄▂▄▂▁▂▁▁▁▁▁▁▂ |
| `October` | num | 96% | 27 | 102 · p25 246 · p50 554 · p95 2,003 · max 2,586  █▃▇▃▄▃▁▃▁▂▁▁▁▂▁▂ |
| `November` | num | 100% | 28 | 151 · p25 430 · p50 848 · p95 2,672 · max 3,022  █▅▅▅▃▃▁▅▃▁▂▁▂▂▂▂ |
| `December` | num | 100% | 28 | 146 · p25 434 · p50 632 · p95 2,169 · max 2,667  █▆▆▃▃▅▂▃▅▁▁▁▁▁▂▂ |
| `Total_Violations` | num | 100% | 28 | 1,405 · p25 3,294 · p50 4,746 · p95 21,138 · max 26,428  ▄█▂▂▁▁▄▁▂▁▁▁▁▁▁▁ |
| `Highest_Monthly_Total` | num | 100% | 28 | 399 · p25 770 · p50 1,464 · p95 3,825 · max 4,434  █▅▂▄▂▄▃▂▄▂▁▁▂▁▂▂ |
| `ObjectId` | num | 100% | 28 | 1.00 · p25 7.75 · p50 14.50 · p95 26.65 · max 28.00  ███▄██▄██▄██▄███ |

## Candidate questions

- (none templated)

_profiled 2026-09-09 · `python3 tools/profile.py open_automated_speed_enforcement_camera_violations_2023`_
