# Red Light Camera Violations 2024

`open_red_light_camera_violations_2024` · shape **arcgis-hub** · source `open-ottawa` · **spatial**

- origin: <https://open.ottawa.ca/datasets/ottawa::red-light-camera-violations-2024>
- fetched 2026-09-09 · **85 rows** · 22 columns
- csv · licence: https://ottawa.ca/en/city-hall/get-know-your-city/open-data#open-data-licence-ve

## Columns

| column | kind | non-null | distinct | summary |
| --- | --- | --- | --- | --- |
| `INTERSECTION` | id/text | 100% | 82 | e.g. WALKEY @ HAWTHORNE  / , ST LAURENT @ BELFAST, CAMPEAU @ HWY 417 WB |
| `CAMERA_INSTALL_YEAR` | num | 100% | 12 | 2,001 · p25 2,010 · p50 2,017 · p95 2,022 · max 2,022  ▃▁▁▁▁▃▄▂▁▁▁▁▆▁▂█ |
| `LATITUDE` | num | 100% | 79 | 45.27 · p25 45.37 · p50 45.39 · p95 45.48 · max 45.48  ▃▃▁▁▁▂▄▅█▄█▆▃▁▁▄ |
| `LONGITUDE` | num | 100% | 79 | -76.02 · p25 -75.73 · p50 -75.69 · p95 -75.51 · max -75.49  ▁▁▁▁▁▁▁▂▄█▄▅▂▁▁▂ |
| `X` | num | 100% | 79 | 342,165 · p25 365,426 · p50 368,244 · p95 381,961 · max 384,073  ▁▁▁▁▁▁▁▂▄█▄▅▂▁▁▂ |
| `Y` | num | 100% | 79 | 5,014,578 · p25 5,025,693 · p50 5,028,500 · p95 5,037,857 · max 5,038,786  ▃▂▁▁▁▂▄▆▇▄█▅▄▁▁▄ |
| `CAMERA_FACING` | cat | 100% | 4 | Eastbound 29%, Northbound 26%, Southbound 25%, Westbound 20% |
| `JANUARY` | num | 100% | 47 | 0.00 · p25 14.00 · p50 26.00 · p95 101 · max 330  ▇█▂▂▁▁▁▁▁▁▁▁▁▁▁▁ |
| `FEBRUARY` | num | 100% | 52 | 0.00 · p25 18.00 · p50 29.00 · p95 97.00 · max 293  ▆█▅▂▂▁▁▁▁▁▁▁▁▁▁▁ |
| `MARCH` | num | 100% | 57 | 0.00 · p25 18.00 · p50 34.00 · p95 131 · max 361  ▇█▃▂▂▁▁▁▁▁▁▁▁▁▁▁ |
| `APRIL` | num | 100% | 51 | 0.00 · p25 17.00 · p50 35.00 · p95 129 · max 362  █▆▃▂▂▁▁▁▁▁▁▁▁▁▁▁ |
| `MAY` | num | 100% | 51 | 0.00 · p25 24.00 · p50 37.00 · p95 152 · max 391  ▇█▄▂▁▂▁▁▁▁▁▁▁▁▁▁ |
| `JUNE` | num | 100% | 60 | 0.00 · p25 20.00 · p50 39.00 · p95 146 · max 328  ▇█▄▄▂▂▂▁▁▁▁▁▁▁▁▁ |
| `JULY` | num | 100% | 60 | 0.00 · p25 17.00 · p50 40.00 · p95 186 · max 385  █▇▄▂▂▂▁▁▁▁▁▁▁▁▁▁ |
| `AUGUST` | num | 84% | 52 | 1.00 · p25 23.00 · p50 42.50 · p95 164 · max 185  ▃█▄▅▄▂▃▂▂▂▁▁▁▁▁▂ |
| `SEPTEMBER` | num | 67% | 48 | 6.00 · p25 30.00 · p50 52.00 · p95 158 · max 194  ▅▅▄█▅▃▄▃▂▁▃▁▁▁▁▁ |
| `OCTOBER` | num | 85% | 58 | 6.00 · p25 26.00 · p50 46.00 · p95 145 · max 237  █▇▇▇▃▂▃▁▁▂▁▁▁▁▁▁ |
| `NOVEMBER` | num | 85% | 30 | 0.00 · p25 6.00 · p50 12.00 · p95 32.60 · max 59.00  ▇▆▇█▇▅▁▂▂▂▁▁▁▁▁▁ |
| `DECEMBER` | num | 87% | 49 | 2.00 · p25 17.50 · p50 31.00 · p95 96.95 · max 166  ▆▆██▃▂▁▂▂▁▁▁▁▁▁▁ |
| `TOTAL_VIOLATIONS` | num | 100% | 77 | 0.00 · p25 218 · p50 397 · p95 1,437 · max 3,003  ▆█▆▄▁▂▁▁▁▁▁▁▁▁▁▁ |
| `HIGHEST_MONTHLY_TOTAL` | num | 100% | 63 | 0.00 · p25 30.00 · p50 58.00 · p95 207 · max 391  ▆█▅▅▂▂▁▁▁▁▁▁▁▁▁▁ |
| `ObjectId` | num | 100% | 85 | 1.00 · p25 22.00 · p50 43.00 · p95 80.80 · max 85.00  █▆▆█▆▆▆█▆▆▆█▆▆▆█ |

## Candidate questions

- (none templated)

_profiled 2026-09-09 · `python3 tools/profile.py open_red_light_camera_violations_2024`_
