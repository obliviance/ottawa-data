# 2019 Tabular Transportation Collision Data

`open_2019_tabular_transportation_collision_data` · shape **arcgis-hub** · source `open-ottawa` · **spatial**

- origin: <https://open.ottawa.ca/datasets/ottawa::2019-tabular-transportation-collision-data>
- fetched 2026-09-09 · **16,399 rows** · 28 columns
- csv · licence: https://ottawa.ca/en/city-hall/get-know-your-city/open-data#open-data-licence-ve

## Columns

| column | kind | non-null | distinct | summary |
| --- | --- | --- | --- | --- |
| `Anom_ID` | id/text | 100% | 16,399 | e.g. 19--10709, 19--10079, 19--1071 |
| `Accident_Date` | date | 100% | 365 | 2019-01-01 → 2019-12-31 |
| `Accident_Time` | date | 100% | 1,338 | 2026-09-09 → 2026-09-09 |
| `Location` | text | 100% | 6,072 | e.g. HWY 417 WALKLEY IC110R, GREENBANK RD @ MARKETP, HUNT CLUB RD @ UPLANDS |
| `Geo_ID` | text | 100% | 6,072 | e.g. 4164, 10406, 10844 |
| `Accident_Location` | cat | 100% | 7 | 01 - Non intersection 38%, 02 - Intersection relate 33%, 03 - At intersection 21%, 04 - At/near private dri 8%, 07 - Overpass or bridge 0%, 05 - At railway crossing 0% |
| `Classification_of_Accident` | cat | 100% | 3 | 03 - P.D. only 83%, 02 - Non-fatal injury 16%, 01 - Fatal injury 0% |
| `Initial_Impact_Type` | cat | 100% | 8 | 03 - Rear end 34%, 04 - Sideswipe 16%, 02 - Angle 14%, 07 - SMV other 13%, 05 - Turning movement 10%, 06 - SMV unattended vehi 9% |
| `Environment_Condition` | cat | 100% | 8 | 01 - Clear 78%, 03 - Snow 10%, 02 - Rain 9%, 04 - Freezing Rain 2%, 05 - Drifting Snow 1%, 00 - Unknown 0% |
| `Light` | cat | 100% | 5 | 01 - Daylight 66%, 07 - Dark 22%, 05 - Dusk 5%, 00 - Unknown 4%, 03 - Dawn 3% |
| `Road_Surface_Condition` | cat | 100% | 11 | 01 - Dry 65%, 02 - Wet 17%, 03 - Loose snow 6%, 06 - Ice 4%, 05 - Packed snow 4%, 04 - Slush 4% |
| `Traffic_Control` | cat | 100% | 12 | 10 - No control 47%, 01 - Traffic signal 40%, 02 - Stop sign 11%, 11 - Roundabout 1%, 03 - Yield sign 0%, 12 - IPS 0% |
| `Traffic_Control_Condition` | cat | 53% | 5 | 01 - Functioning 93%, 00 - Unknown 7%, 02 - Not functioning 0%, 03 - Obscured 0%, 04 - Missing/Damaged 0% |
| `No__of_Vehicles` | num | 100% | 8 | 1.00 · p25 2.00 · p50 2.00 · p95 3.00 · max 8.00  ▃▁█▁▁▁▁▁▁▁▁▁▁▁▁▁ |
| `No__of_Bicycles` | num | 100% | 3 | 0.00 · p25 0.00 · p50 0.00 · p95 0.00 · max 2.00  █▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁ |
| `No__of_Motorcycles` | num | 100% | 3 | 0.00 · p25 0.00 · p50 0.00 · p95 0.00 · max 2.00  █▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁ |
| `No__of_Pedestrians` | num | 100% | 3 | 0.00 · p25 0.00 · p50 0.00 · p95 0.00 · max 2.00  █▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁ |
| `Max_Injury` | cat | 16% | 4 | 02 - Minor 57%, 01 - Minimal 38%, 03 - Major 4%, 04 - Fatal 1% |
| `No__of_Injuries` | num | 100% | 9 | 0.00 · p25 0.00 · p50 0.00 · p95 1.00 · max 38.00  █▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁ |
| `No__of_Minimal` | num | 7% | 6 | 1.00 · p25 1.00 · p50 1.00 · p95 2.00 · max 11.00  █▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁ |
| `No__of_Minor` | num | 9% | 8 | 1.00 · p25 1.00 · p50 1.00 · p95 2.00 · max 10.00  █▂▁▁▁▁▁▁▁▁▁▁▁▁▁▁ |
| `No__of_Major` | num | 0% | 4 | 1.00 · p25 1.00 · p50 1.00 · p95 2.00 · max 14.00  █▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁ |
| `No__of_Fatal` | num | 0% | 2 | 1.00 · p25 1.00 · p50 1.00 · p95 1.00 · max 3.00  █▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁ |
| `X` | num | 100% | 16,198 | 317,475 · p25 363,312 · p50 367,707 · p95 382,959 · max 401,223  ▁▁▁▁▁▁▂▁▄█▄▂▂▁▁▁ |
| `Y` | num | 100% | 16,082 | 4,981,110 · p25 5,022,000 · p50 5,027,184 · p95 5,035,959 · max 5,043,414  ▁▁▁▁▁▁▁▁▃▂▄▅█▅▂▁ |
| `Latitude` | num | 100% | 16,059 | 44.97 · p25 45.34 · p50 45.38 · p95 45.46 · max 45.52  ▁▁▁▁▁▁▁▁▃▃▄▆█▅▂▁ |
| `Longitude` | num | 100% | 16,042 | -76.34 · p25 -75.75 · p50 -75.70 · p95 -75.50 · max -75.27  ▁▁▁▁▁▁▂▂▄█▄▂▂▁▁▁ |
| `ObjectId` | num | 100% | 16,399 | 1.00 · p25 4,100 · p50 8,200 · p95 15,579 · max 16,399  ████████▇███████ |

## Candidate questions

- Trend / seasonality of open_2019_tabular_transportation_collision_data over `Accident_Date`; structural breaks?
- Spatial clustering of open_2019_tabular_transportation_collision_data; overlay wards + the decision timeline

_profiled 2026-09-09 · `python3 tools/profile.py open_2019_tabular_transportation_collision_data`_
