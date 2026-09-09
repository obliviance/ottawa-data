# 2020 Tabular Transportation Collision Data

`open_2020_tabular_transportation_collision_data` · shape **arcgis-hub** · source `open-ottawa` · **spatial**

- origin: <https://open.ottawa.ca/datasets/ottawa::2020-tabular-transportation-collision-data>
- fetched 2026-09-09 · **10,047 rows** · 28 columns
- csv · licence: https://ottawa.ca/en/city-hall/get-know-your-city/open-data#open-data-licence-ve

## Columns

| column | kind | non-null | distinct | summary |
| --- | --- | --- | --- | --- |
| `Anom_ID` | id/text | 100% | 10,047 | e.g. 20--1127, 20--1128, 20--1129 |
| `Accident_Date` | date | 100% | 366 | 2020-01-01 → 2020-12-31 |
| `Accident_Time` | date | 100% | 1,298 | 2026-09-09 → 2026-09-09 |
| `Location` | text | 100% | 4,551 | e.g. GREENBANK RD @ WEST HU, HIGHWAY 417 btwn HWY41, LEMIEUX ST @ ST. LAURE |
| `Geo_ID` | text | 100% | 4,551 | e.g. 5167, __3ZA2W9, 2021 |
| `Accident_Location` | cat | 100% | 7 | 01 - Non intersection 42%, 02 - Intersection relate 31%, 03 - At intersection 20%, 04 - At/near private dri 7%, 07 - Overpass or bridge 0%, 06 - Underpass or tunnel 0% |
| `Classification_of_Accident` | cat | 100% | 3 | 03 - P.D. only 82%, 02 - Non-fatal injury 17%, 01 - Fatal injury 0% |
| `Initial_Impact_Type` | cat | 100% | 8 | 03 - Rear end 32%, 07 - SMV other 18%, 02 - Angle 14%, 04 - Sideswipe 13%, 05 - Turning movement 9%, 06 - SMV unattended vehi 9% |
| `Environment_Condition` | cat | 100% | 8 | 01 - Clear 80%, 03 - Snow 12%, 02 - Rain 7%, 04 - Freezing Rain 1%, 07 - Fog, mist, smoke, d 0%, 05 - Drifting Snow 0% |
| `Light` | cat | 100% | 5 | 01 - Daylight 64%, 07 - Dark 24%, 00 - Unknown 5%, 05 - Dusk 5%, 03 - Dawn 3% |
| `Road_Surface_Condition` | cat | 100% | 10 | 01 - Dry 65%, 02 - Wet 18%, 03 - Loose snow 6%, 04 - Slush 5%, 05 - Packed snow 3%, 06 - Ice 3% |
| `Traffic_Control` | cat | 100% | 9 | 10 - No control 50%, 01 - Traffic signal 38%, 02 - Stop sign 10%, 11 - Roundabout 1%, 03 - Yield sign 0%, 12 - IPS 0% |
| `Traffic_Control_Condition` | cat | 50% | 5 | 01 - Functioning 94%, 00 - Unknown 6%, 02 - Not functioning 0%, 03 - Obscured 0%, 04 - Missing/Damaged 0% |
| `No__of_Vehicles` | num | 100% | 8 | 1.00 · p25 1.00 · p50 2.00 · p95 3.00 · max 9.00  ▃█▁▁▁▁▁▁▁▁▁▁▁▁▁▁ |
| `No__of_Bicycles` | num | 100% | 3 | 0.00 · p25 0.00 · p50 0.00 · p95 0.00 · max 2.00  █▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁ |
| `No__of_Motorcycles` | num | 100% | 2 | 0.00 · p25 0.00 · p50 0.00 · p95 0.00 · max 1.00  █▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁ |
| `No__of_Pedestrians` | num | 100% | 4 | 0.00 · p25 0.00 · p50 0.00 · p95 0.00 · max 3.00  █▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁ |
| `Max_Injury` | cat | 17% | 4 | 02 - Minor 61%, 01 - Minimal 33%, 03 - Major 5%, 04 - Fatal 1% |
| `No__of_Injuries` | num | 100% | 7 | 0.00 · p25 0.00 · p50 0.00 · p95 1.00 · max 9.00  █▂▁▁▁▁▁▁▁▁▁▁▁▁▁▁ |
| `No__of_Minimal` | num | 6% | 5 | 1.00 · p25 1.00 · p50 1.00 · p95 2.00 · max 5.00  █▁▁▂▁▁▁▁▁▁▁▁▁▁▁▁ |
| `No__of_Minor` | num | 10% | 6 | 1.00 · p25 1.00 · p50 1.00 · p95 2.00 · max 9.00  █▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁ |
| `No__of_Major` | num | 0% | 4 | 1.00 · p25 1.00 · p50 1.00 · p95 2.00 · max 4.00  █▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁ |
| `No__of_Fatal` | num | 0% | 1 | 1.00 · p25 1.00 · p50 1.00 · p95 1.00 · max 1.00   |
| `X` | num | 100% | 9,869 | 317,813 · p25 363,186 · p50 367,639 · p95 383,219 · max 401,822  ▁▁▁▁▁▁▂▂▅█▅▂▂▁▁▁ |
| `Y` | num | 100% | 9,393 | 4,982,873 · p25 5,021,500 · p50 5,026,834 · p95 5,036,160 · max 5,043,439  ▁▁▁▁▁▁▁▁▃▃▅▅█▄▂▁ |
| `Latitude` | num | 100% | 9,328 | 44.98 · p25 45.33 · p50 45.38 · p95 45.46 · max 45.52  ▁▁▁▁▁▁▁▁▃▃▅▅█▅▂▁ |
| `Longitude` | num | 100% | 9,464 | -76.33 · p25 -75.75 · p50 -75.70 · p95 -75.50 · max -75.26  ▁▁▁▁▁▁▂▂▅█▅▂▂▁▁▁ |
| `ObjectId` | num | 100% | 10,047 | 1.00 · p25 2,512 · p50 5,024 · p95 9,545 · max 10,047  ████████▇███████ |

## Candidate questions

- Trend / seasonality of open_2020_tabular_transportation_collision_data over `Accident_Date`; structural breaks?
- Spatial clustering of open_2020_tabular_transportation_collision_data; overlay wards + the decision timeline

_profiled 2026-09-09 · `python3 tools/profile.py open_2020_tabular_transportation_collision_data`_
