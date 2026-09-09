# Red Light Camera Violations 2025

`open_red_light_camera_violations_2025` · shape **arcgis-hub** · source `open-ottawa` · **spatial**

- origin: <https://open.ottawa.ca/datasets/ottawa::red-light-camera-violations-2025>
- fetched 2026-09-09 · **86 rows** · 22 columns
- csv · licence: https://ottawa.ca/en/city-hall/open-transparent-and-accountable-government/open-

## Columns

| column | kind | non-null | distinct | summary |
| --- | --- | --- | --- | --- |
| `INTERSECTION` | id/text | 100% | 83 | e.g. WALKEY @ HAWTHORNE  / , ST LAURENT @ BELFAST, CAMPEAU @ HWY 417 WB |
| `CAMERA_INSTALL_YEAR` | num | 100% | 13 | 2,001 · p25 2,010 · p50 2,017 · p95 2,022 · max 2,025  ▃▁▁▁▃▄▂▁▁▁▄▃▂█▁▁ |
| `LATITUDE` | num | 100% | 80 | 45.27 · p25 45.37 · p50 45.39 · p95 45.48 · max 45.48  ▃▃▁▁▁▂▄▆█▄█▆▃▁▁▄ |
| `LONGITUDE` | num | 100% | 80 | -76.02 · p25 -75.73 · p50 -75.69 · p95 -75.51 · max -75.49  ▁▁▁▁▁▁▁▂▄█▄▅▂▁▁▂ |
| `X` | num | 100% | 80 | 342,165 · p25 365,375 · p50 368,213 · p95 381,952 · max 384,073  ▁▁▁▁▁▁▁▂▄█▄▅▂▁▁▂ |
| `Y` | num | 100% | 80 | 5,014,578 · p25 5,025,418 · p50 5,028,249 · p95 5,037,827 · max 5,038,786  ▃▂▁▁▁▂▄▆▇▄█▅▄▁▁▄ |
| `CAMERA_FACING` | cat | 100% | 4 | Eastbound 29%, Northbound 27%, Southbound 24%, Westbound 20% |
| `JANUARY` | num | 87% | 55 | 1.00 · p25 16.00 · p50 35.00 · p95 83.40 · max 146  ▅█▅█▄▄▄▃▂▁▁▁▁▁▁▁ |
| `FEBRUARY` | num | 86% | 52 | 2.00 · p25 19.25 · p50 32.00 · p95 89.15 · max 135  ▅▅█▇▆▂▂▂▃▂▁▂▁▁▁▁ |
| `MARCH` | num | 87% | 52 | 4.00 · p25 23.00 · p50 40.00 · p95 122 · max 160  ▅▄▄█▄▃▃▁▁▂▁▁▁▁▁▁ |
| `APRIL` | num | 87% | 57 | 5.00 · p25 22.50 · p50 38.00 · p95 118 · max 183  ▇██▅▆▃▂▃▁▂▂▁▁▁▁▂ |
| `MAY` | num | 86% | 54 | 3.00 · p25 25.25 · p50 43.00 · p95 139 · max 245  ▅▆█▃▃▂▁▂▂▁▁▁▁▁▁▁ |
| `JUNE` | num | 83% | 53 | 9.00 · p25 28.75 · p50 44.50 · p95 152 · max 278  ▆█▄▅▂▁▂▁▂▁▁▁▁▁▁▁ |
| `JULY` | num | 82% | 56 | 8.00 · p25 28.00 · p50 46.00 · p95 174 · max 220  ▆▆█▄▃▃▁▂▂▁▁▁▁▁▁▂ |
| `AUGUST` | num | 81% | 52 | 7.00 · p25 32.00 · p50 44.50 · p95 155 · max 242  ▆▆█▄▃▂▁▁▁▃▁▁▁▁▁▁ |
| `SEPTEMBER` | num | 82% | 49 | 5.00 · p25 20.50 · p50 34.00 · p95 108 · max 188  ▇▆█▆▂▂▃▁▁▁▁▁▁▁▁▁ |
| `OCTOBER` | num | 83% | 53 | 5.00 · p25 29.00 · p50 46.00 · p95 163 · max 233  ▅▆█▄▄▂▂▁▁▁▁▁▁▁▁▁ |
| `NOVEMBER` | num | 83% | 43 | 11.00 · p25 21.75 · p50 35.00 · p95 110 · max 174  █▆▅▂▃▂▂▂▁▁▁▁▁▁▁▁ |
| `DECEMBER` | num | 89% | 53 | 2.00 · p25 20.00 · p50 35.00 · p95 109 · max 163  ▅▇█▆▅▄▂▂▃▂▁▁▁▁▁▂ |
| `TOTAL_VIOLATIONS` | num | 100% | 78 | 0.00 · p25 207 · p50 433 · p95 1,378 · max 2,226  █▅▅▇▅▂▃▁▂▁▁▁▁▁▁▁ |
| `HIGHEST_MONTHLY_TOTAL` | num | 100% | 67 | 0.00 · p25 32.25 · p50 55.50 · p95 188 · max 278  ▅▇█▇▄▃▁▃▁▂▁▁▁▁▁▁ |
| `ObjectId` | num | 100% | 86 | 1.00 · p25 22.25 · p50 43.50 · p95 81.75 · max 86.00  █▆▆█▆▆█▆▆█▆▆█▆▆█ |

## Candidate questions

- (none templated)

_profiled 2026-09-09 · `python3 tools/profile.py open_red_light_camera_violations_2025`_
