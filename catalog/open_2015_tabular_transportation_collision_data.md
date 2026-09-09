# 2015 Tabular Transportation Collision Data

`open_2015_tabular_transportation_collision_data` · shape **arcgis-hub** · source `open-ottawa` · **spatial**

- origin: <https://open.ottawa.ca/datasets/ottawa::2015-tabular-transportation-collision-data>
- fetched 2026-09-09 · **15,077 rows** · 28 columns
- csv · licence: https://ottawa.ca/en/city-hall/get-know-your-city/open-data#open-data-licence-ve

## Columns

| column | kind | non-null | distinct | summary |
| --- | --- | --- | --- | --- |
| `Anom_ID` | id/text | 100% | 15,077 | e.g. 15--1, 15--2, 15--3 |
| `Accident_Date` | date | 100% | 365 | 2015-01-01 → 2015-12-31 |
| `Accident_Time` | date | 100% | 1,340 | 2026-09-09 → 2026-09-09 |
| `Location` | text | 100% | 5,719 | e.g. KING EDWARD AVE @ RIDE, BEATRICE DR @ STRANDHE, HIGHWAY 417 btwn HWY41 |
| `Geo_ID` | text | 100% | 5,719 | e.g. 2121, 5447, __3ZA283 |
| `Accident_Location` | cat | 100% | 7 | 01 - Non intersection 37%, 02 - Intersection relate 32%, 03 - At intersection 21%, 04 - At/near private dri 9%, 07 - Overpass or bridge 0%, 06 - Underpass or tunnel 0% |
| `Classification_of_Accident` | cat | 100% | 3 | 03 - P.D. only 81%, 02 - Non-fatal injury 19%, 01 - Fatal injury 0% |
| `Initial_Impact_Type` | cat | 100% | 8 | 03 - Rear end 35%, 07 - SMV other 16%, 02 - Angle 14%, 04 - Sideswipe 13%, 05 - Turning movement 11%, 06 - SMV unattended vehi 8% |
| `Environment_Condition` | cat | 100% | 9 | 01 - Clear 80%, 03 - Snow 9%, 02 - Rain 9%, 04 - Freezing Rain 1%, 05 - Drifting Snow 0%, 07 - Fog, mist, smoke, d 0% |
| `Light` | cat | 100% | 5 | 01 - Daylight 70%, 07 - Dark 22%, 05 - Dusk 4%, 03 - Dawn 2%, 00 - Unknown 2% |
| `Road_Surface_Condition` | cat | 100% | 10 | 01 - Dry 67%, 02 - Wet 16%, 03 - Loose snow 6%, 06 - Ice 5%, 04 - Slush 3%, 05 - Packed snow 3% |
| `Traffic_Control` | cat | 100% | 6 | 10 - No control 47%, 01 - Traffic signal 41%, 02 - Stop sign 10%, 11 - Roundabout 1%, 03 - Yield sign 1%, 08 - Traffic gate 0% |
| `Traffic_Control_Condition` | cat | 52% | 5 | 01 - Functioning 91%, 00 - Unknown 8%, 02 - Not functioning 0%, 04 - Missing/Damaged 0%, 03 - Obscured 0% |
| `No__of_Vehicles` | num | 100% | 7 | 1.00 · p25 2.00 · p50 2.00 · p95 3.00 · max 7.00  ▃▁█▁▁▁▁▁▁▁▁▁▁▁▁▁ |
| `No__of_Bicycles` | num | 100% | 3 | 0.00 · p25 0.00 · p50 0.00 · p95 0.00 · max 2.00  █▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁ |
| `No__of_Motorcycles` | num | 100% | 3 | 0.00 · p25 0.00 · p50 0.00 · p95 0.00 · max 2.00  █▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁ |
| `No__of_Pedestrians` | num | 100% | 4 | 0.00 · p25 0.00 · p50 0.00 · p95 0.00 · max 3.00  █▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁ |
| `Max_Injury` | cat | 19% | 4 | 02 - Minor 52%, 01 - Minimal 42%, 03 - Major 4%, 04 - Fatal 1% |
| `No__of_Injuries` | num | 100% | 10 | 0.00 · p25 0.00 · p50 0.00 · p95 1.00 · max 17.00  █▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁ |
| `No__of_Minimal` | num | 9% | 7 | 1.00 · p25 1.00 · p50 1.00 · p95 2.00 · max 9.00  █▂▁▁▁▁▁▁▁▁▁▁▁▁▁▁ |
| `No__of_Minor` | num | 10% | 6 | 1.00 · p25 1.00 · p50 1.00 · p95 2.00 · max 12.00  █▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁ |
| `No__of_Major` | num | 0% | 3 | 1.00 · p25 1.00 · p50 1.00 · p95 2.00 · max 3.00  █▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁ |
| `No__of_Fatal` | num | 0% | 2 | 1.00 · p25 1.00 · p50 1.00 · p95 2.00 · max 2.00  █▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁ |
| `X` | num | 100% | 12,608 | 318,678 · p25 363,723 · p50 368,010 · p95 383,113 · max 401,809  ▁▁▁▁▁▁▂▂▄█▅▂▂▁▁▁ |
| `Y` | num | 100% | 13,176 | 4,981,006 · p25 5,022,298 · p50 5,027,899 · p95 5,036,257 · max 5,043,413  ▁▁▁▁▁▁▁▁▂▃▄▅█▅▂▁ |
| `Latitude` | num | 100% | 14,302 | 44.97 · p25 45.34 · p50 45.39 · p95 45.46 · max 45.52  ▁▁▁▁▁▁▁▁▂▃▄▅█▅▂▁ |
| `Longitude` | num | 100% | 14,306 | -76.32 · p25 -75.75 · p50 -75.69 · p95 -75.50 · max -75.26  ▁▁▁▁▁▁▂▂▄█▅▁▂▁▁▁ |
| `ObjectId` | num | 100% | 15,077 | 1.00 · p25 3,770 · p50 7,539 · p95 14,323 · max 15,077  █▇▇█▇▇▇█▇▇▇█▇▇▇█ |

## Candidate questions

- Trend / seasonality of open_2015_tabular_transportation_collision_data over `Accident_Date`; structural breaks?
- Spatial clustering of open_2015_tabular_transportation_collision_data; overlay wards + the decision timeline

_profiled 2026-09-09 · `python3 tools/profile.py open_2015_tabular_transportation_collision_data`_
