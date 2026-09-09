# Red Light Camera Violations 2018

`open_red_light_camera_violations_2018` · shape **arcgis-hub** · source `open-ottawa` · **spatial**

- origin: <https://open.ottawa.ca/datasets/ottawa::red-light-camera-violations-2018>
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
| `JANUARY` | num | 81% | 36 | 0.00 · p25 21.00 · p50 30.00 · p95 76.60 · max 195  ▂▅█▃▂▂▂▁▁▁▁▁▁▁▁▁ |
| `FEBRUARY` | num | 80% | 36 | 5.00 · p25 23.50 · p50 35.50 · p95 99.55 · max 143  ▆▅█▅▇▃▃▂▂▁▁▁▁▁▁▁ |
| `MARCH` | num | 80% | 36 | 3.00 · p25 25.25 · p50 39.00 · p95 129 · max 139  ▄▄▄█▆▅▄▃▁▁▁▁▁▁▁▃ |
| `APRIL` | num | 83% | 40 | 2.00 · p25 22.25 · p50 39.00 · p95 114 · max 213  ▆█▅█▂▂▁▂▂▁▁▁▁▁▁▁ |
| `MAY` | num | 85% | 42 | 7.00 · p25 33.50 · p50 59.00 · p95 207 · max 367  ▅█▅▂▄▁▂▁▁▁▁▁▁▁▁▁ |
| `JUNE` | num | 85% | 36 | 8.00 · p25 34.00 · p50 53.00 · p95 220 · max 338  ▃█▄▃▃▁▁▁▁▁▁▁▁▁▁▁ |
| `JULY` | num | 87% | 45 | 3.00 · p25 43.50 · p50 69.50 · p95 319 · max 597  ▆█▆▃▂▁▁▁▁▂▁▁▁▁▁▁ |
| `AUGUST` | num | 85% | 40 | 6.00 · p25 39.50 · p50 72.00 · p95 368 · max 616  █▄▆▁▁▁▁▁▁▁▁▁▁▁▁▁ |
| `SEPTEMBER` | num | 89% | 44 | 7.00 · p25 34.00 · p50 59.00 · p95 302 · max 557  █▅▄▂▁▂▁▁▁▁▁▁▁▁▁▁ |
| `OCTOBER` | num | 89% | 45 | 7.00 · p25 36.00 · p50 62.00 · p95 325 · max 549  ▇█▅▁▂▁▁▁▁▁▁▁▁▁▁▁ |
| `NOVEMBER` | num | 92% | 39 | 5.00 · p25 30.50 · p50 48.00 · p95 246 · max 465  ▆█▃▂▁▁▁▁▁▁▁▁▁▁▁▁ |
| `DECEMBER` | num | 92% | 39 | 4.00 · p25 31.00 · p50 46.00 · p95 179 · max 370  ▄█▄▃▁▁▁▁▁▁▁▁▁▁▁▁ |
| `TOTAL_VIOLATIONS` | num | 100% | 52 | 0.00 · p25 318 · p50 501 · p95 2,392 · max 4,154  ▄█▄▄▁▁▁▁▁▁▁▁▁▁▁▁ |
| `HIGHEST_MONTHLY_TOTAL` | num | 94% | 42 | 14.00 · p25 52.50 · p50 85.50 · p95 345 · max 616  ▇▇█▁▁▂▁▁▁▁▁▁▁▁▁▁ |
| `FID` | num | 100% | 55 | 1.00 · p25 14.50 · p50 28.00 · p95 52.30 · max 55.00  █▆█▆▆█▆█▆▆█▆▆█▆█ |

## Candidate questions

- (none templated)

_profiled 2026-09-09 · `python3 tools/profile.py open_red_light_camera_violations_2018`_
