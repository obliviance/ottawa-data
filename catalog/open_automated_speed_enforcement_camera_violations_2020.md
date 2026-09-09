# Automated Speed Enforcement Camera Violations 2020

`open_automated_speed_enforcement_camera_violations_2020` · shape **arcgis-hub** · source `open-ottawa` · **spatial**

- origin: <https://open.ottawa.ca/datasets/ottawa::automated-speed-enforcement-camera-violations-2020>
- fetched 2026-09-09 · **8 rows** · 21 columns
- csv · licence: https://ottawa.ca/en/city-hall/get-know-your-city/open-data#open-data-licence-ve

## Columns

| column | kind | non-null | distinct | summary |
| --- | --- | --- | --- | --- |
| `Location` | cat | 100% | 8 | E001 - Longfields Dr. be 12%, E002 - Innes Rd. between 12%, E003 - Bayshore Dr. near 12%, E004 - Katimavik Rd. bet 12%, E005 - Watters Dr. betwe 12%, E006 - Ogilvie Rd betwee 12% |
| `Camera_Install_Year` | num | 100% | 1 | 2,020 · p25 2,020 · p50 2,020 · p95 2,020 · max 2,020   |
| `Latitude` | num | 100% | 8 | 45.28 · p25 45.34 · p50 45.38 · p95 45.48 · max 45.48  ▄▁▄▁▁█▁▁▁▄▁▁▄▁▁█ |
| `Longitude` | num | 100% | 8 | -75.90 · p25 -75.76 · p50 -75.69 · p95 -75.47 · max -75.46  ▄▁▁▄▁█▁▁▁▄▄▁▁▁▁█ |
| `X` | num | 100% | 8 | 351,857 · p25 362,465 · p50 368,283 · p95 385,654 · max 386,179  ▄▁▁▄▁█▁▁▁▄▄▁▁▁▁█ |
| `Y` | num | 100% | 8 | 5,016,001 · p25 5,021,976 · p50 5,026,469 · p95 5,037,802 · max 5,038,179  ▄▁▄▁▁█▁▁▁▄▁▁▄▁▁█ |
| `January` | text | 0% | 0 | e.g.  |
| `February` | text | 0% | 0 | e.g.  |
| `March` | text | 0% | 0 | e.g.  |
| `April` | text | 0% | 0 | e.g.  |
| `May` | text | 0% | 0 | e.g.  |
| `June` | text | 0% | 0 | e.g.  |
| `July` | num | 50% | 4 | 997 · p25 2,317 · p50 2,862 · p95 3,777 · max 3,920  █▁▁▁▁▁▁▁▁██▁▁▁▁█ |
| `August` | num | 50% | 4 | 3,047 · p25 3,102 · p50 4,011 · p95 5,835 · max 6,000  █▁▁▁▁▁▁▁▁▁▄▁▁▁▁▄ |
| `September` | num | 50% | 4 | 1,017 · p25 1,862 · p50 2,326 · p95 3,475 · max 3,645  █▁▁▁▁▁█▁▁█▁▁▁▁▁█ |
| `October` | num | 50% | 4 | 753 · p25 1,086 · p50 1,534 · p95 2,468 · max 2,573  █▁▁█▁▁▁▁▁█▁▁▁▁▁█ |
| `November` | num | 50% | 4 | 397 · p25 682 · p50 804 · p95 1,133 · max 1,187  █▁▁▁▁▁▁██▁▁▁▁▁▁█ |
| `December` | num | 75% | 6 | 11.00 · p25 346 · p50 476 · p95 1,184 · max 1,245  █▁▁▁███▁▁▁▁▁█▁▁█ |
| `Total_Violations` | num | 100% | 8 | 1,325 · p25 3,052 · p50 6,416 · p95 11,914 · max 13,496  ▄▄▄▁▁▁█▁▄▁▄▁▁▁▁▄ |
| `Highest_Monthly_Total` | num | 100% | 8 | 777 · p25 1,905 · p50 3,346 · p95 5,616 · max 6,000  ██▁▁█▁█▁██▁▁█▁▁█ |
| `ObjectId` | num | 100% | 8 | 1.00 · p25 2.75 · p50 4.50 · p95 7.65 · max 8.00  █▁█▁█▁█▁▁█▁█▁█▁█ |

## Candidate questions

- (none templated)

_profiled 2026-09-09 · `python3 tools/profile.py open_automated_speed_enforcement_camera_violations_2020`_
