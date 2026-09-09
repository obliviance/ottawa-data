# Red Light Camera Violations 2019

`open_red_light_camera_violations_2019` · shape **arcgis-hub** · source `open-ottawa` · **spatial**

- origin: <https://open.ottawa.ca/datasets/ottawa::red-light-camera-violations-2019>
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
| `JANUARY` | num | 90% | 38 | 7.00 · p25 27.25 · p50 35.50 · p95 102 · max 280  ▄█▄▂▁▂▁▁▁▁▁▁▁▁▁▁ |
| `FEBRUARY` | num | 90% | 39 | 4.00 · p25 19.25 · p50 31.50 · p95 100 · max 205  ██▅▅▃▂▁▁▁▁▁▁▁▁▁▁ |
| `MARCH` | num | 90% | 37 | 2.00 · p25 20.25 · p50 32.50 · p95 104 · max 183  ▃▇█▅▃▂▁▁▁▁▁▁▁▁▁▁ |
| `APRIL` | num | 92% | 39 | 2.00 · p25 22.50 · p50 36.00 · p95 106 · max 187  ▆▄█▆▄▃▁▁▂▁▁▁▁▁▁▁ |
| `MAY` | num | 92% | 41 | 6.00 · p25 31.00 · p50 42.00 · p95 180 · max 234  ▄▅█▃▃▃▁▁▂▁▁▁▁▂▁▁ |
| `JUNE` | num | 92% | 44 | 3.00 · p25 42.50 · p50 63.00 · p95 290 · max 606  ▅█▄▂▁▁▁▁▁▁▁▁▁▁▁▁ |
| `JULY` | num | 92% | 47 | 12.00 · p25 45.50 · p50 70.00 · p95 324 · max 674  █▆▃▂▁▁▂▁▁▁▁▁▁▁▁▁ |
| `AUGUST` | num | 94% | 42 | 6.00 · p25 36.25 · p50 58.50 · p95 343 · max 665  █▇▃▂▁▁▁▁▁▁▁▁▁▁▁▁ |
| `SEPTEMBER` | num | 89% | 43 | 8.00 · p25 34.00 · p50 63.00 · p95 331 · max 498  █▇▄▃▁▁▁▁▁▁▁▁▁▁▁▁ |
| `OCTOBER` | num | 85% | 44 | 10.00 · p25 36.50 · p50 64.00 · p95 274 · max 487  █▇▅▁▁▂▁▁▁▁▁▁▁▁▁▁ |
| `NOVEMBER` | num | 89% | 41 | 0.00 · p25 34.00 · p50 49.00 · p95 194 · max 393  ▄█▇▁▁▁▁▁▁▁▁▁▁▁▁▁ |
| `DECEMBER` | num | 87% | 40 | 1.00 · p25 29.75 · p50 39.50 · p95 186 · max 413  ▃█▂▁▁▁▁▁▁▁▁▁▁▁▁▁ |
| `TOTAL_VIOLATIONS` | num | 94% | 50 | 113 · p25 392 · p50 606 · p95 2,325 · max 4,739  ▆█▄▁▂▁▁▁▁▁▁▁▁▁▁▁ |
| `HIGHEST_MONTHLY_TOTAL` | num | 100% | 45 | 0.00 · p25 58.50 · p50 89.00 · p95 331 · max 674  ▃█▆▂▂▁▂▁▁▁▁▁▁▁▁▁ |
| `FID` | num | 100% | 55 | 1.00 · p25 14.50 · p50 28.00 · p95 52.30 · max 55.00  █▆█▆▆█▆█▆▆█▆▆█▆█ |

## Candidate questions

- (none templated)

_profiled 2026-09-09 · `python3 tools/profile.py open_red_light_camera_violations_2019`_
