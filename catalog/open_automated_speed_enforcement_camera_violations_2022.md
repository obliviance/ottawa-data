# Automated Speed Enforcement Camera Violations 2022

`open_automated_speed_enforcement_camera_violations_2022` · shape **arcgis-hub** · source `open-ottawa` · **spatial**

- origin: <https://open.ottawa.ca/datasets/ottawa::automated-speed-enforcement-camera-violations-2022>
- fetched 2026-09-09 · **17 rows** · 21 columns
- csv · licence: https://ottawa.ca/en/city-hall/get-know-your-city/open-data#open-data-licence-ve

## Columns

| column | kind | non-null | distinct | summary |
| --- | --- | --- | --- | --- |
| `Location` | cat | 100% | 17 | E001 - Longfields Dr. be 6%, E002 - Innes Rd. between 6%, E003 - Bayshore Dr. near 6%, E004 - Katimavik Rd. bet 6%, E005 - Watters Dr. betwe 6%, E006 - Ogilvie Rd betwee 6% |
| `Camera_Install_Year` | num | 100% | 3 | 2,020 · p25 2,020 · p50 2,021 · p95 2,022 · max 2,022  █▁▁▁▁▁▁▅▁▁▁▁▁▁▁▄ |
| `Latitude` | num | 100% | 17 | 45.27 · p25 45.32 · p50 45.36 · p95 45.47 · max 45.48  ▃▃▃▃▃▅▃▃▃▁▃▁▅▃▁█ |
| `Longitude` | num | 100% | 17 | -75.92 · p25 -75.81 · p50 -75.71 · p95 -75.47 · max -75.46  █▃▁▁▅▁▅▃▁█▁▃▃▁▃▅ |
| `X` | num | 100% | 17 | 349,900 · p25 359,157 · p50 366,497 · p95 384,978 · max 386,179  █▃▁▁▅▁▅▃▁█▁▃▃▁▃▅ |
| `Y` | num | 100% | 17 | 5,014,085 · p25 5,020,500 · p50 5,025,269 · p95 5,037,528 · max 5,038,179  ▃▃▃▃▃▅▃▃▃▁▃▁█▁▁█ |
| `January` | num | 47% | 8 | 233 · p25 242 · p50 362 · p95 564 · max 565  █▁▁▃▁▁▁▁▁▃▁▁▁▁▁█ |
| `February` | num | 52% | 9 | 218 · p25 298 · p50 337 · p95 590 · max 642  █▁▁█▄▁▁▁▁▁█▄▁▁▁▄ |
| `March` | num | 64% | 10 | 385 · p25 540 · p50 666 · p95 875 · max 914  ▄▁▁▁██▁▁█▁▄▄▁▄▁▄ |
| `April` | num | 76% | 13 | 171 · p25 518 · p50 601 · p95 1,083 · max 1,084  ▃▁▃▃▁▁█▃▅▃▁▁▃▁▁▅ |
| `May` | num | 76% | 13 | 224 · p25 324 · p50 459 · p95 1,919 · max 3,609  █▆▅▁▁▁▁▁▁▁▁▁▁▁▁▂ |
| `June` | num | 76% | 13 | 128 · p25 267 · p50 338 · p95 1,165 · max 2,082  ▃█▄▂▁▁▁▁▁▁▁▁▁▁▁▂ |
| `July` | cat | 82% | 14 | 859 7%, 986 7%, 2,430 7%, 2,618 7%, 830 7%, 2,996 7% |
| `August` | cat | 82% | 14 | 412 7%, 645 7%, 1,239 7%, 1,468 7%, 358 7%, 1,640 7% |
| `September` | cat | 82% | 14 | 311 7%, 468 7%, 1,121 7%, 1,242 7%, 215 7%, 1,871 7% |
| `October` | cat | 94% | 16 | 296 6%, 442 6%, 994 6%, 1,006 6%, 226 6%, 884 6% |
| `November` | cat | 100% | 17 | 205 6%, 361 6%, 829 6%, 598 6%, 236 6%, 978 6% |
| `December` | cat | 100% | 17 | 380 6%, 305 6%, 417 6%, 436 6%, 316 6%, 433 6% |
| `Total_Violations` | num | 100% | 17 | 744 · p25 5,003 · p50 5,575 · p95 14,875 · max 22,914  ▃▁▃█▂▂▃▃▂▁▁▁▁▁▁▂ |
| `Highest_Monthly_Total` | num | 100% | 17 | 471 · p25 859 · p50 2,009 · p95 3,645 · max 6,226  ██▅▁██▁▅▁▁▁▁▁▁▁▃ |
| `ObjectId` | num | 100% | 17 | 1.00 · p25 5.00 · p50 9.00 · p95 16.20 · max 17.00  █▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄ |

## Candidate questions

- (none templated)

_profiled 2026-09-09 · `python3 tools/profile.py open_automated_speed_enforcement_camera_violations_2022`_
