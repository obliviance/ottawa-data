# Red Light Camera Violations 2026

`open_red_light_camera_violations_2026` · shape **arcgis-hub** · source `open-ottawa` · **spatial**

- origin: <https://open.ottawa.ca/datasets/ottawa::red-light-camera-violations-2026>
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
| `JANUARY` | num | 88% | 52 | 2.00 · p25 22.00 · p50 37.50 · p95 116 · max 227  ▃█▇▆▃▁▂▁▂▁▁▁▁▁▁▁ |
| `FEBRUARY` | num | 87% | 47 | 1.00 · p25 19.50 · p50 31.00 · p95 110 · max 175  ▃█▆▅▅▁▂▂▁▁▁▁▁▁▁▁ |
| `MARCH` | num | 89% | 54 | 5.00 · p25 23.00 · p50 38.00 · p95 125 · max 228  ▆▇█▅▃▂▁▁▂▁▁▁▁▁▁▁ |
| `APRIL` | num | 89% | 55 | 8.00 · p25 26.00 · p50 41.00 · p95 145 · max 265  ▇█▇▃▂▃▁▁▁▁▁▁▁▁▁▁ |
| `MAY` | num | 89% | 57 | 4.00 · p25 34.00 · p50 50.00 · p95 169 · max 371  ▄█▆▃▂▁▁▂▁▁▁▁▁▁▁▁ |
| `JUNE` | num | 89% | 62 | 1.00 · p25 35.00 · p50 50.00 · p95 177 · max 315  ▄▆█▄▂▂▃▁▁▁▁▁▁▁▁▁ |
| `JULY` | num | 87% | 60 | 10.00 · p25 35.50 · p50 58.00 · p95 225 · max 322  ▆█▇▃▂▁▂▂▁▁▁▁▁▁▁▁ |
| `AUGUST` | text | 0% | 0 | e.g.  |
| `SEPTEMBER` | text | 0% | 0 | e.g.  |
| `OCTOBER` | text | 0% | 0 | e.g.  |
| `NOVEMBER` | text | 0% | 0 | e.g.  |
| `DECEMBER` | text | 0% | 0 | e.g.  |
| `TOTAL_VIOLATIONS` | num | 100% | 76 | 0.00 · p25 175 · p50 278 · p95 975 · max 1,903  ▅▆█▃▃▁▁▁▁▁▁▁▁▁▁▁ |
| `HIGHEST_MONTHLY_TOTAL` | num | 100% | 59 | 0.00 · p25 38.25 · p50 58.50 · p95 214 · max 371  ▄▄█▂▂▁▁▁▁▁▁▁▁▁▁▁ |
| `ObjectId` | num | 100% | 86 | 1.00 · p25 22.25 · p50 43.50 · p95 81.75 · max 86.00  █▆▆█▆▆█▆▆█▆▆█▆▆█ |

## Candidate questions

- (none templated)

_profiled 2026-09-09 · `python3 tools/profile.py open_red_light_camera_violations_2026`_
