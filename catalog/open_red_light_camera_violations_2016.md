# Red Light Camera Violations 2016

`open_red_light_camera_violations_2016` · shape **arcgis-hub** · source `open-ottawa` · **spatial**

- origin: <https://open.ottawa.ca/datasets/ottawa::red-light-camera-violations-2016>
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
| `JANUARY` | num | 54% | 24 | 5.00 · p25 20.50 · p50 33.00 · p95 72.10 · max 77.00  ▂▆▂▆▃▃▃█▂▃▂▂▂▁▂▃ |
| `FEBRUARY` | num | 54% | 25 | 4.00 · p25 14.00 · p50 26.00 · p95 50.10 · max 74.00  █▄█▂▆█▄█▄▂▄▁▁▁▁▂ |
| `MARCH` | num | 52% | 23 | 0.00 · p25 20.00 · p50 25.00 · p95 47.80 · max 96.00  ▃▄▁█▆▅▅▃▂▁▁▁▁▁▁▂ |
| `APRIL` | num | 54% | 23 | 2.00 · p25 16.50 · p50 28.50 · p95 70.65 · max 80.00  ▁▄▃▃▁█▂▂▁▁▁▁▁▁▁▁ |
| `MAY` | num | 54% | 26 | 21.00 · p25 38.00 · p50 57.00 · p95 190 · max 357  █▅▅▂▂▁▁▁▁▁▁▁▁▁▁▁ |
| `JUNE` | num | 56% | 23 | 0.00 · p25 18.00 · p50 27.00 · p95 77.50 · max 95.00  ▃▃▅▆▄█▂▃▁▂▂▂▁▁▂▂ |
| `JULY` | num | 54% | 28 | 11.00 · p25 31.00 · p50 46.00 · p95 105 · max 241  ▇█▇▄▄▃▃▁▁▁▁▁▁▁▁▂ |
| `AUGUST` | num | 54% | 24 | 22.00 · p25 37.50 · p50 58.00 · p95 135 · max 249  █▆█▄▄▂▃▁▂▁▁▁▁▁▁▂ |
| `SEPTEMBER` | num | 56% | 26 | 6.00 · p25 39.00 · p50 58.00 · p95 150 · max 255  ▄▁█▅▇▃▁▁▁▁▁▁▁▁▁▁ |
| `OCTOBER` | num | 54% | 25 | 4.00 · p25 31.00 · p50 53.00 · p95 125 · max 240  ▁█▄▄▅▂▁▁▁▁▁▁▁▁▁▁ |
| `NOVEMBER` | num | 54% | 26 | 14.00 · p25 34.00 · p50 47.00 · p95 100 · max 164  ▄▄█▅▄▂▆▃▁▁▂▁▁▁▁▂ |
| `DECEMBER` | num | 56% | 28 | 3.00 · p25 24.50 · p50 42.00 · p95 84.50 · max 91.00  ▂▂▅▆▃▂▅█▃▅▁▂▁▅▁▃ |
| `TOTAL_VIOLATIONS` | num | 100% | 34 | 0.00 · p25 0.00 · p50 262 · p95 843 · max 1,884  █▁▂▂▃▂▂▁▁▁▁▁▁▁▁▁ |
| `HIGHEST_MONTHLY_TOTAL` | num | 100% | 31 | 0.00 · p25 0.00 · p50 39.00 · p95 152 · max 357  █▂▂▄▂▁▁▁▁▁▁▁▁▁▁▁ |
| `FID` | num | 100% | 55 | 1.00 · p25 14.50 · p50 28.00 · p95 52.30 · max 55.00  █▆█▆▆█▆█▆▆█▆▆█▆█ |

## Candidate questions

- (none templated)

_profiled 2026-09-09 · `python3 tools/profile.py open_red_light_camera_violations_2016`_
