# Red Light Camera Violations 2017

`open_red_light_camera_violations_2017` · shape **arcgis-hub** · source `open-ottawa` · **spatial**

- origin: <https://open.ottawa.ca/datasets/ottawa::red-light-camera-violations-2017>
- fetched 2026-09-09 · **55 rows** · 22 columns
- csv · licence: https://ottawa.ca/en/city-hall/get-know-your-city/open-data#open-data-licence-ve

## Columns

| column | kind | non-null | distinct | summary |
| --- | --- | --- | --- | --- |
| `INTERSECTION` | id/text | 100% | 53 | e.g. WALKEY @ HAWTHORNE  / , ST LAURENT @ BELFAST, CAMPEAU @ HWY 417 WB |
| `CAMERA_INSTALL_YEAR` | num | 100% | 9 | 2,001 · p25 2,008 · p50 2,010 · p95 2,018 · max 2,018  ▃▁▁▁▁▁▄▁▄▂▁▁▁▁▁█ |
| `LATITUDE` | num | 100% | 53 | 45.27 · p25 45.37 · p50 45.41 · p95 45.48 · max 45.48  ▃▁▁▁▁▁▃▃▅▃█▄▃▁▁▃ |
| `LONGITUDE` | num | 100% | 53 | -75.89 · p25 -75.71 · p50 -75.69 · p95 -75.50 · max -75.49  ▁▁▁▁▁▂▃█▃▂▂▂▁▁▁▂ |
| `X` | num | 100% | 53 | 352,842 · p25 366,501 · p50 367,908 · p95 382,959 · max 384,073  ▁▁▁▁▁▂▃█▃▂▂▂▁▁▁▂ |
| `Y` | num | 100% | 53 | 5,014,578 · p25 5,025,875 · p50 5,029,788 · p95 5,037,983 · max 5,038,786  ▃▁▁▁▁▁▃▃▄▃█▃▃▁▁▃ |
| `CAMERA_FACING` | cat | 100% | 4 | Eastbound 31%, Northbound 27%, Southbound 24%, Westbound 18% |
| `JANUARY` | num | 56% | 26 | 7.00 · p25 20.00 · p50 28.00 · p95 74.50 · max 85.00  █▃▃█▅▅▅▃▁▃▂▁▁▂▂▂ |
| `FEBRUARY` | num | 56% | 23 | 1.00 · p25 16.50 · p50 25.00 · p95 66.00 · max 94.00  ▅▆▅█▃▃█▃▃▁▁▃▁▁▁▂ |
| `MARCH` | num | 60% | 24 | 0.00 · p25 17.00 · p50 28.00 · p95 78.40 · max 105  ▅▄▃▅█▂▅▃▃▂▁▃▂▁▁▂ |
| `APRIL` | num | 60% | 24 | 0.00 · p25 23.00 · p50 28.00 · p95 67.80 · max 87.00  ▂▁▂▂█▃▁▂▄▂▃▂▁▁▁▁ |
| `MAY` | num | 60% | 28 | 22.00 · p25 33.00 · p50 46.00 · p95 132 · max 251  █▄▅▃▁▁▁▁▁▁▁▁▁▁▁▁ |
| `JUNE` | num | 61% | 31 | 31.00 · p25 50.00 · p50 62.00 · p95 179 · max 309  ▆█▃▄▁▂▁▂▁▁▁▁▁▁▁▁ |
| `JULY` | num | 63% | 30 | 20.00 · p25 39.00 · p50 59.00 · p95 219 · max 331  █▇▇▂▃▁▁▁▁▁▁▁▁▁▁▂ |
| `AUGUST` | num | 60% | 28 | 27.00 · p25 44.00 · p50 61.00 · p95 226 · max 307  █▇▄▄▁▂▁▁▁▁▁▁▁▁▁▁ |
| `SEPTEMBER` | num | 63% | 31 | 0.00 · p25 46.50 · p50 60.00 · p95 202 · max 267  ▁▄▅█▄▃▁▁▁▁▁▂▁▁▁▁ |
| `OCTOBER` | num | 78% | 41 | 0.00 · p25 38.00 · p50 59.00 · p95 181 · max 217  ▄▃▅▇█▄▂▁▂▁▂▁▁▁▁▂ |
| `NOVEMBER` | num | 78% | 37 | 7.00 · p25 35.00 · p50 53.00 · p95 185 · max 379  ▅█▆▂▂▁▂▁▁▁▁▁▁▁▁▁ |
| `DECEMBER` | num | 81% | 37 | 7.00 · p25 27.00 · p50 48.00 · p95 146 · max 230  ▆█▃▆▂▂▂▁▁▁▂▁▁▁▁▁ |
| `TOTAL_VIOLATIONS` | num | 100% | 47 | 0.00 · p25 91.50 · p50 378 · p95 1,173 · max 2,039  █▂▅▃▂▃▄▁▁▁▁▁▁▁▁▁ |
| `HIGHEST_MONTHLY_TOTAL` | num | 83% | 41 | 7.00 · p25 50.75 · p50 71.00 · p95 287 · max 379  ▂▆█▅▂▁▂▁▂▁▁▁▁▂▁▁ |
| `FID` | num | 100% | 55 | 1.00 · p25 14.50 · p50 28.00 · p95 52.30 · max 55.00  █▆█▆▆█▆█▆▆█▆▆█▆█ |

## Candidate questions

- (none templated)

_profiled 2026-09-09 · `python3 tools/profile.py open_red_light_camera_violations_2017`_
