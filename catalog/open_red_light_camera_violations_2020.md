# Red Light Camera Violations 2020

`open_red_light_camera_violations_2020` · shape **arcgis-hub** · source `open-ottawa` · **spatial**

- origin: <https://open.ottawa.ca/datasets/ottawa::red-light-camera-violations-2020>
- fetched 2026-09-09 · **61 rows** · 22 columns
- csv · licence: https://ottawa.ca/en/city-hall/get-know-your-city/open-data#open-data-licence-ve

## Columns

| column | kind | non-null | distinct | summary |
| --- | --- | --- | --- | --- |
| `INTERSECTION` | id/text | 100% | 58 | e.g. WALKEY @ HAWTHORNE  / , ST LAURENT @ BELFAST, CAMPEAU @ HWY 417 WB |
| `CAMERA_INSTALL_YEAR` | num | 100% | 10 | 2,001 · p25 2,008 · p50 2,011 · p95 2,020 · max 2,020  ▄▁▁▁▁▆▁▆▃▁▁▁▁█▄▄ |
| `LATITUDE` | num | 100% | 58 | 45.27 · p25 45.37 · p50 45.40 · p95 45.48 · max 45.48  ▃▁▁▁▁▁▃▃▅▃█▄▃▁▁▃ |
| `LONGITUDE` | num | 100% | 58 | -75.89 · p25 -75.71 · p50 -75.69 · p95 -75.50 · max -75.49  ▁▁▁▁▁▂▃█▃▂▃▂▁▁▁▂ |
| `X` | num | 100% | 58 | 352,842 · p25 366,575 · p50 368,183 · p95 382,891 · max 384,073  ▁▁▁▁▁▂▃█▃▂▃▂▁▁▁▂ |
| `Y` | num | 100% | 58 | 5,014,578 · p25 5,025,878 · p50 5,029,477 · p95 5,037,978 · max 5,038,786  ▃▁▁▁▁▁▃▄▅▃█▄▃▁▁▃ |
| `CAMERA_FACING` | cat | 100% | 4 | Eastbound 30%, Northbound 28%, Southbound 25%, Westbound 18% |
| `JANUARY` | num | 80% | 38 | 3.00 · p25 23.00 · p50 35.00 · p95 195 · max 377  █▆▄▂▁▁▁▁▁▁▁▁▁▁▁▁ |
| `FEBRUARY` | num | 78% | 36 | 4.00 · p25 20.00 · p50 36.00 · p95 170 · max 279  █▆▄▃▁▁▁▁▁▁▁▁▁▁▁▁ |
| `MARCH` | num | 78% | 41 | 0.00 · p25 18.75 · p50 33.50 · p95 130 · max 165  ▅▃▅█▄▂▁▁▁▁▁▁▁▁▁▂ |
| `APRIL` | num | 78% | 32 | 0.00 · p25 12.75 · p50 23.00 · p95 62.55 · max 103  ▄█▆█▇▃▅▂▁▁▂▁▁▁▁▁ |
| `MAY` | num | 80% | 42 | 1.00 · p25 26.00 · p50 40.00 · p95 167 · max 213  ▅▆█▄▅▄▁▁▁▁▁▁▂▁▁▁ |
| `JUNE` | num | 81% | 42 | 4.00 · p25 33.00 · p50 54.00 · p95 240 · max 327  ▆█▆▅▃▁▃▁▁▁▁▁▁▁▁▂ |
| `JULY` | num | 85% | 43 | 10.00 · p25 33.50 · p50 56.50 · p95 262 · max 466  █▅▅▂▂▂▁▁▁▁▁▁▁▁▁▁ |
| `AUGUST` | num | 100% | 46 | 0.00 · p25 26.00 · p50 54.00 · p95 302 · max 463  █▇▅▃▁▂▁▁▁▁▁▁▁▁▁▁ |
| `SEPTEMBER` | num | 100% | 46 | 0.00 · p25 22.00 · p50 40.00 · p95 247 · max 393  █▇▄▃▁▁▁▁▁▁▁▁▁▁▁▁ |
| `OCTOBER` | num | 100% | 42 | 0.00 · p25 19.00 · p50 34.00 · p95 158 · max 251  ▆█▇▄▁▂▁▁▁▁▁▁▁▁▁▁ |
| `NOVEMBER` | num | 100% | 45 | 0.00 · p25 17.00 · p50 33.00 · p95 127 · max 248  █▇▇▃▂▂▁▁▁▁▁▁▁▁▁▁ |
| `DECEMBER` | num | 100% | 40 | 0.00 · p25 11.00 · p50 26.00 · p95 109 · max 193  █▆▇▃▂▁▁▁▁▁▁▁▁▁▁▁ |
| `TOTAL_VIOLATIONS` | num | 100% | 57 | 0.00 · p25 274 · p50 434 · p95 1,935 · max 3,203  ▅██▄▁▂▁▁▁▁▁▁▁▁▁▁ |
| `HIGHEST_MONTHLY_TOTAL` | num | 100% | 49 | 0.00 · p25 37.00 · p50 71.00 · p95 314 · max 466  ██▆▅▃▂▁▁▁▁▂▁▁▁▁▁ |
| `ObjectId` | num | 100% | 61 | 1.00 · p25 16.00 · p50 31.00 · p95 58.00 · max 61.00  ████▆███▆███▆███ |

## Candidate questions

- (none templated)

_profiled 2026-09-09 · `python3 tools/profile.py open_red_light_camera_violations_2020`_
