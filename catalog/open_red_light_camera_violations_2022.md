# Red Light Camera Violations 2022

`open_red_light_camera_violations_2022` · shape **arcgis-hub** · source `open-ottawa` · **spatial**

- origin: <https://open.ottawa.ca/datasets/ottawa::red-light-camera-violations-2022>
- fetched 2026-09-09 · **85 rows** · 22 columns
- csv · licence: https://ottawa.ca/en/city-hall/get-know-your-city/open-data#open-data-licence-ve

## Columns

| column | kind | non-null | distinct | summary |
| --- | --- | --- | --- | --- |
| `INTERSECTION` | id/text | 100% | 82 | e.g. WALKEY @ HAWTHORNE  / , ST LAURENT @ BELFAST, CAMPEAU @ HWY 417 WB |
| `CAMERA_INSTALL_YEAR` | num | 100% | 12 | 2,001 · p25 2,010 · p50 2,017 · p95 2,022 · max 2,022  ▃▁▁▁▁▃▄▂▁▁▁▁▆▁▂█ |
| `LATITUDE` | num | 100% | 82 | 45.27 · p25 45.37 · p50 45.39 · p95 45.48 · max 45.48  ▃▃▁▁▁▂▄▅█▄█▆▃▁▁▄ |
| `LONGITUDE` | num | 100% | 82 | -76.02 · p25 -75.73 · p50 -75.69 · p95 -75.51 · max -75.49  ▁▁▁▁▁▁▁▂▄█▄▅▂▁▁▂ |
| `X` | num | 100% | 79 | 342,165 · p25 365,426 · p50 368,244 · p95 381,961 · max 384,073  ▁▁▁▁▁▁▁▂▄█▄▅▂▁▁▂ |
| `Y` | num | 100% | 80 | 5,014,578 · p25 5,025,693 · p50 5,028,500 · p95 5,037,857 · max 5,038,786  ▃▂▁▁▁▂▄▆▇▄█▅▄▁▁▄ |
| `CAMERA_FACING` | cat | 100% | 4 | Eastbound 28%, Southbound 26%, Northbound 26%, Westbound 20% |
| `JANUARY` | num | 100% | 43 | 0.00 · p25 0.00 · p50 14.00 · p95 75.20 · max 138  █▃▂▃▁▁▁▁▁▁▁▁▁▁▁▁ |
| `FEBRUARY` | num | 100% | 41 | 0.00 · p25 0.00 · p50 13.00 · p95 107 · max 192  █▃▃▁▁▁▁▁▁▁▁▁▁▁▁▁ |
| `MARCH` | num | 100% | 47 | 0.00 · p25 0.00 · p50 18.00 · p95 104 · max 192  █▄▃▁▁▁▁▁▁▁▁▁▁▁▁▁ |
| `APRIL` | num | 100% | 44 | 0.00 · p25 0.00 · p50 19.00 · p95 109 · max 145  █▂▂▃▂▁▁▁▁▁▁▁▁▁▁▁ |
| `MAY` | num | 100% | 48 | 0.00 · p25 0.00 · p50 29.00 · p95 145 · max 304  █▅▃▂▁▁▁▁▁▁▁▁▁▁▁▁ |
| `JUNE` | num | 100% | 54 | 0.00 · p25 0.00 · p50 31.00 · p95 163 · max 345  █▅▂▂▁▁▁▁▁▁▁▁▁▁▁▁ |
| `JULY` | num | 100% | 56 | 0.00 · p25 8.00 · p50 33.00 · p95 216 · max 565  █▄▂▁▁▁▁▁▁▁▁▁▁▁▁▁ |
| `AUGUST` | num | 100% | 52 | 0.00 · p25 5.00 · p50 38.00 · p95 233 · max 589  █▄▂▁▁▁▁▁▁▁▁▁▁▁▁▁ |
| `SEPTEMBER` | num | 100% | 51 | 0.00 · p25 7.00 · p50 37.00 · p95 203 · max 577  █▅▂▁▁▁▁▁▁▁▁▁▁▁▁▁ |
| `OCTOBER` | num | 100% | 61 | 0.00 · p25 13.00 · p50 42.00 · p95 207 · max 593  █▅▂▁▁▁▁▁▁▁▁▁▁▁▁▁ |
| `NOVEMBER` | num | 100% | 52 | 0.00 · p25 15.00 · p50 32.00 · p95 157 · max 425  █▅▂▂▁▁▁▁▁▁▁▁▁▁▁▁ |
| `DECEMBER` | num | 100% | 56 | 0.00 · p25 17.00 · p50 32.00 · p95 131 · max 381  ▇█▄▂▁▁▁▁▁▁▁▁▁▁▁▁ |
| `TOTAL_VIOLATIONS` | num | 100% | 77 | 0.00 · p25 152 · p50 358 · p95 1,821 · max 3,997  █▇▃▂▁▁▁▁▁▁▁▁▁▁▁▁ |
| `HIGHEST_MONTHLY_TOTAL` | num | 100% | 61 | 0.00 · p25 30.00 · p50 55.00 · p95 248 · max 593  ▇█▃▂▁▁▂▁▁▁▁▁▁▁▁▁ |
| `FID` | num | 100% | 85 | 1.00 · p25 22.00 · p50 43.00 · p95 80.80 · max 85.00  █▆▆█▆▆▆█▆▆▆█▆▆▆█ |

## Candidate questions

- (none templated)

_profiled 2026-09-09 · `python3 tools/profile.py open_red_light_camera_violations_2022`_
