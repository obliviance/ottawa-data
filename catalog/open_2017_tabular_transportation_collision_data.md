# 2017 Tabular Transportation Collision Data

`open_2017_tabular_transportation_collision_data` · shape **arcgis-hub** · source `open-ottawa` · **spatial**

- origin: <https://open.ottawa.ca/datasets/ottawa::2017-tabular-transportation-collision-data>
- fetched 2026-09-09 · **14,398 rows** · 28 columns
- csv · licence: https://ottawa.ca/en/city-hall/get-know-your-city/open-data#open-data-licence-ve

## Columns

| column | kind | non-null | distinct | summary |
| --- | --- | --- | --- | --- |
| `Anom_ID` | id/text | 100% | 14,398 | e.g. 17--1, 17--10169, 17--108 |
| `Accident_Date` | date | 100% | 365 | 2017-01-01 → 2017-12-31 |
| `Accident_Time` | date | 100% | 1,362 | 2026-09-09 → 2026-09-09 |
| `Location` | text | 100% | 5,460 | e.g. WEST RIDGE DR btwn PAR, INDUSTRIAL AVE/INNES R, ALBERT ST @ PRESTON ST |
| `Geo_ID` | text | 100% | 5,460 | e.g. __5RG32R, 2203, 2217 |
| `Accident_Location` | cat | 100% | 8 | 01 - Non intersection 36%, 02 - Intersection relate 33%, 03 - At intersection 22%, 04 - At/near private dri 8%, 07 - Overpass or bridge 0%, 05 - At railway crossing 0% |
| `Classification_of_Accident` | cat | 100% | 3 | 03 - P.D. only 81%, 02 - Non-fatal injury 19%, 01 - Fatal injury 0% |
| `Initial_Impact_Type` | cat | 100% | 8 | 03 - Rear end 33%, 07 - SMV other 17%, 04 - Sideswipe 13%, 02 - Angle 13%, 05 - Turning movement 11%, 06 - SMV unattended vehi 8% |
| `Environment_Condition` | cat | 100% | 9 | 01 - Clear 76%, 03 - Snow 11%, 02 - Rain 11%, 04 - Freezing Rain 1%, 05 - Drifting Snow 0%, 07 - Fog, mist, smoke, d 0% |
| `Light` | cat | 100% | 6 | 01 - Daylight 67%, 07 - Dark 24%, 05 - Dusk 4%, 00 - Unknown 3%, 03 - Dawn 2%, 99 - Other 0% |
| `Road_Surface_Condition` | cat | 100% | 10 | 01 - Dry 64%, 02 - Wet 19%, 03 - Loose snow 7%, 06 - Ice 4%, 04 - Slush 3%, 05 - Packed snow 3% |
| `Traffic_Control` | cat | 100% | 7 | 10 - No control 46%, 01 - Traffic signal 41%, 02 - Stop sign 11%, 11 - Roundabout 1%, 03 - Yield sign 1%, 09 - Traffic controller 0% |
| `Traffic_Control_Condition` | cat | 55% | 5 | 01 - Functioning 85%, 00 - Unknown 14%, 02 - Not functioning 0%, 03 - Obscured 0%, 04 - Missing/Damaged 0% |
| `No__of_Vehicles` | num | 100% | 7 | 1.00 · p25 1.00 · p50 2.00 · p95 3.00 · max 7.00  ▃▁█▁▁▁▁▁▁▁▁▁▁▁▁▁ |
| `No__of_Bicycles` | num | 100% | 2 | 0.00 · p25 0.00 · p50 0.00 · p95 0.00 · max 1.00  █▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁ |
| `No__of_Motorcycles` | num | 100% | 3 | 0.00 · p25 0.00 · p50 0.00 · p95 0.00 · max 2.00  █▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁ |
| `No__of_Pedestrians` | num | 100% | 4 | 0.00 · p25 0.00 · p50 0.00 · p95 0.00 · max 3.00  █▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁ |
| `Max_Injury` | cat | 19% | 4 | 02 - Minor 56%, 01 - Minimal 39%, 03 - Major 5%, 04 - Fatal 1% |
| `No__of_Injuries` | num | 100% | 9 | 0.00 · p25 0.00 · p50 0.00 · p95 1.00 · max 8.00  █▂▁▁▁▁▁▁▁▁▁▁▁▁▁▁ |
| `No__of_Minimal` | num | 8% | 7 | 1.00 · p25 1.00 · p50 1.00 · p95 2.00 · max 8.00  █▁▂▁▁▁▁▁▁▁▁▁▁▁▁▁ |
| `No__of_Minor` | num | 10% | 6 | 1.00 · p25 1.00 · p50 1.00 · p95 2.00 · max 6.00  █▁▁▂▁▁▁▁▁▁▁▁▁▁▁▁ |
| `No__of_Major` | num | 0% | 3 | 1.00 · p25 1.00 · p50 1.00 · p95 1.40 · max 3.00  █▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁ |
| `No__of_Fatal` | num | 0% | 2 | 1.00 · p25 1.00 · p50 1.00 · p95 2.00 · max 2.00  █▁▁▁▁▁▁▁▁▁▁▁▁▁▁▂ |
| `X` | num | 100% | 13,124 | 0.00 · p25 363,081 · p50 367,645 · p95 383,184 · max 400,271  ▁▁▁▁▁▁▁▁▁▁▁▁▁▁█▂ |
| `Y` | num | 100% | 13,270 | 0.00 · p25 5,021,837 · p50 5,026,991 · p95 5,036,159 · max 5,043,414  ▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁█ |
| `Latitude` | num | 100% | 13,982 | 0.00 · p25 45.33 · p50 45.38 · p95 45.46 · max 45.52  ▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁█ |
| `Longitude` | num | 100% | 13,978 | -79.24 · p25 -75.76 · p50 -75.70 · p95 -75.50 · max -75.28  ▁▁▁▁▁▁▁▁▁▁▁▁▁▂█▁ |
| `ObjectId` | num | 100% | 14,398 | 1.00 · p25 3,600 · p50 7,200 · p95 13,678 · max 14,398  █████▇████▇█████ |

## Candidate questions

- Trend / seasonality of open_2017_tabular_transportation_collision_data over `Accident_Date`; structural breaks?
- Spatial clustering of open_2017_tabular_transportation_collision_data; overlay wards + the decision timeline

_profiled 2026-09-09 · `python3 tools/profile.py open_2017_tabular_transportation_collision_data`_
