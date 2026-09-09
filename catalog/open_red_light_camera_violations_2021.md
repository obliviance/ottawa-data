# Red Light Camera Violations 2021

`open_red_light_camera_violations_2021` · shape **arcgis-hub** · source `open-ottawa` · **spatial**

- origin: <https://open.ottawa.ca/datasets/ottawa::red-light-camera-violations-2021>
- fetched 2026-09-09 · **68 rows** · 22 columns
- csv · licence: https://ottawa.ca/en/city-hall/get-know-your-city/open-data#open-data-licence-ve

## Columns

| column | kind | non-null | distinct | summary |
| --- | --- | --- | --- | --- |
| `INTERSECTION` | id/text | 100% | 65 | e.g. WALKEY @ HAWTHORNE  / , ST LAURENT @ BELFAST, CAMPEAU @ HWY 417 WB |
| `CAMERA_INSTALL_YEAR` | num | 100% | 11 | 2,001 · p25 2,009 · p50 2,014 · p95 2,021 · max 2,021  ▄▁▁▁▁▅▁█▁▁▁▁▇▄▁▇ |
| `LATITUDE` | num | 100% | 65 | 45.27 · p25 45.37 · p50 45.40 · p95 45.48 · max 45.48  ▃▁▁▁▁▂▃▃▆▃█▄▃▁▁▃ |
| `LONGITUDE` | num | 100% | 65 | -76.02 · p25 -75.71 · p50 -75.69 · p95 -75.51 · max -75.49  ▁▁▁▁▂▁▁▁▄█▃▅▂▁▁▂ |
| `X` | num | 100% | 65 | 342,165 · p25 366,386 · p50 368,213 · p95 382,578 · max 384,073  ▁▁▁▁▂▁▁▁▄█▃▅▂▁▁▂ |
| `Y` | num | 100% | 65 | 5,014,578 · p25 5,025,827 · p50 5,029,321 · p95 5,037,990 · max 5,038,786  ▃▁▁▁▁▂▃▄▆▃█▄▃▁▁▃ |
| `CAMERA_FACING` | cat | 100% | 4 | Eastbound 31%, Northbound 25%, Southbound 24%, Westbound 21% |
| `JANUARY` | num | 100% | 42 | 0.00 · p25 9.75 · p50 26.50 · p95 121 · max 208  █▆▄▅▂▁▂▁▁▁▁▁▁▁▁▁ |
| `FEBRUARY` | num | 100% | 43 | 0.00 · p25 11.50 · p50 31.50 · p95 179 · max 560  █▄▂▁▁▁▁▁▁▁▁▁▁▁▁▁ |
| `MARCH` | num | 100% | 48 | 0.00 · p25 11.75 · p50 37.00 · p95 228 · max 476  █▆▂▂▁▁▁▁▁▁▁▁▁▁▁▁ |
| `APRIL` | num | 100% | 48 | 0.00 · p25 13.75 · p50 34.50 · p95 171 · max 343  █▆▅▁▁▁▁▁▁▁▁▁▁▁▁▁ |
| `MAY` | num | 100% | 48 | 0.00 · p25 17.50 · p50 42.50 · p95 200 · max 485  █▇▄▁▁▁▁▁▁▁▁▁▁▁▁▁ |
| `JUNE` | num | 100% | 50 | 0.00 · p25 24.75 · p50 48.50 · p95 298 · max 583  █▆▃▁▁▁▁▁▁▁▁▁▁▁▁▁ |
| `JULY` | num | 100% | 51 | 0.00 · p25 29.00 · p50 55.00 · p95 293 · max 698  █▆▃▂▁▁▁▁▁▁▁▁▁▁▁▁ |
| `AUGUST` | num | 100% | 52 | 0.00 · p25 34.75 · p50 52.50 · p95 315 · max 793  █▄▃▁▁▁▁▁▁▁▁▁▁▁▁▁ |
| `SEPTEMBER` | num | 100% | 53 | 0.00 · p25 32.75 · p50 57.50 · p95 287 · max 626  █▇▄▂▁▁▁▁▁▁▁▁▁▁▁▁ |
| `OCTOBER` | num | 98% | 46 | 0.00 · p25 29.50 · p50 48.00 · p95 201 · max 582  █▇▄▁▁▁▁▁▁▁▁▁▁▁▁▁ |
| `NOVEMBER` | num | 98% | 52 | 0.00 · p25 24.50 · p50 46.00 · p95 213 · max 511  ▇█▃▂▁▁▁▁▁▁▁▁▁▁▁▁ |
| `DECEMBER` | num | 88% | 48 | 8.00 · p25 32.75 · p50 53.00 · p95 234 · max 474  █▆▅▁▂▁▁▁▁▁▁▁▁▁▁▁ |
| `TOTAL_VIOLATIONS` | num | 100% | 66 | 0.00 · p25 306 · p50 540 · p95 2,534 · max 5,868  ▇█▄▂▁▁▁▁▁▁▁▁▁▁▁▁ |
| `HIGHEST_MONTHLY_TOTAL` | num | 100% | 51 | 0.00 · p25 44.75 · p50 77.00 · p95 402 · max 793  ▆█▄▃▁▁▁▁▁▁▁▁▁▁▁▁ |
| `ObjectId` | num | 100% | 68 | 1.00 · p25 17.75 · p50 34.50 · p95 64.65 · max 68.00  █▆▆▆▆█▆▆▆▆█▆▆▆▆█ |

## Candidate questions

- (none templated)

_profiled 2026-09-09 · `python3 tools/profile.py open_red_light_camera_violations_2021`_
