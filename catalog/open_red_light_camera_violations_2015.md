# Red Light Camera Violations 2015

`open_red_light_camera_violations_2015` · shape **arcgis-hub** · source `open-ottawa` · **spatial**

- origin: <https://open.ottawa.ca/datasets/ottawa::red-light-camera-violations-2015>
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
| `JANUARY` | num | 56% | 24 | 0.00 · p25 17.00 · p50 26.00 · p95 50.00 · max 71.00  ▃▃▂▆█▃▃▆▅▅▂▁▂▁▁▂ |
| `FEBRUARY` | num | 54% | 23 | 0.00 · p25 6.75 · p50 18.50 · p95 42.55 · max 48.00  █▅▂▁▃▆▆▅▂▁▅▂▁▂▂▂ |
| `MARCH` | num | 54% | 23 | 0.00 · p25 9.50 · p50 22.00 · p95 42.65 · max 49.00  █▄▄▄▂▄▂█▄▁▄▆▂▄▂▂ |
| `APRIL` | num | 54% | 23 | 0.00 · p25 8.75 · p50 19.50 · p95 54.30 · max 88.00  █▄▃█▃▃▂▄▃▂▂▁▁▁▁▂ |
| `MAY` | num | 52% | 27 | 11.00 · p25 28.00 · p50 44.00 · p95 128 · max 186  ▃█▆▄▆▂▁▂▃▂▁▂▁▁▁▂ |
| `JUNE` | num | 52% | 27 | 24.00 · p25 34.00 · p50 50.00 · p95 192 · max 245  █▅▃▄▂▁▁▁▁▁▁▁▁▁▁▁ |
| `JULY` | num | 52% | 26 | 26.00 · p25 41.00 · p50 54.00 · p95 219 · max 282  ██▄▁▃▁▂▁▁▁▁▁▁▁▁▂ |
| `AUGUST` | num | 54% | 27 | 14.00 · p25 35.00 · p50 56.50 · p95 211 · max 329  ▇█▇▆▄▂▁▁▁▁▁▁▁▂▁▂ |
| `SEPTEMBER` | num | 52% | 27 | 4.00 · p25 44.00 · p50 53.00 · p95 172 · max 236  ▂▄▄█▃▁▂▁▁▁▁▁▁▁▁▁ |
| `OCTOBER` | num | 47% | 23 | 15.00 · p25 38.50 · p50 58.00 · p95 145 · max 152  ▂▆▆█▂█▆▄▂▁▂▁▁▁▂▄ |
| `NOVEMBER` | num | 54% | 25 | 10.00 · p25 35.00 · p50 51.50 · p95 129 · max 165  ▂██▅▃█▂▃▅▂▁▁▁▁▂▂ |
| `DECEMBER` | num | 54% | 25 | 14.00 · p25 25.00 · p50 44.50 · p95 141 · max 237  █▄▆▅▁▁▁▁▁▁▁▁▁▁▁▁ |
| `TOTAL_VIOLATIONS` | num | 100% | 33 | 0.00 · p25 0.00 · p50 222 · p95 927 · max 1,796  █▂▁▂▁▂▁▁▁▁▁▁▁▁▁▁ |
| `HIGHEST_MONTHLY_TOTAL` | num | 100% | 32 | 0.00 · p25 0.00 · p50 43.00 · p95 145 · max 329  █▂▃▃▁▁▁▁▁▁▁▁▁▁▁▁ |
| `FID` | num | 100% | 55 | 1.00 · p25 14.50 · p50 28.00 · p95 52.30 · max 55.00  █▆█▆▆█▆█▆▆█▆▆█▆█ |

## Candidate questions

- (none templated)

_profiled 2026-09-09 · `python3 tools/profile.py open_red_light_camera_violations_2015`_
