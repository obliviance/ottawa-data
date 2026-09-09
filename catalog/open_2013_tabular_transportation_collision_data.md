# 2013 Tabular Transportation Collision Data

`open_2013_tabular_transportation_collision_data` · shape **arcgis-hub** · source `open-ottawa` · **spatial**

- origin: <https://open.ottawa.ca/datasets/ottawa::2013-tabular-transportation-collision-data>
- fetched 2026-09-09 · **15,156 rows** · 28 columns
- csv · licence: https://ottawa.ca/en/city-hall/get-know-your-city/open-data#open-data-licence-ve

## Columns

| column | kind | non-null | distinct | summary |
| --- | --- | --- | --- | --- |
| `Anom_ID` | id/text | 100% | 15,156 | e.g. 13--1, 13--2, 13--3 |
| `Accident_Date` | date | 100% | 365 | 2013-01-01 → 2013-12-31 |
| `Accident_Time` | date | 100% | 1,360 | 2026-09-09 → 2026-09-09 |
| `Location` | text | 100% | 5,752 | e.g. INDUSTRIAL AVE btwn TR, MACLAREN ST btwn LYON , EAGLESON RD btwn EAGLE |
| `Geo_ID` | text | 100% | 5,752 | e.g. __3ZA3R9, __3ZBORE, __3ZA41JB |
| `Accident_Location` | cat | 100% | 7 | 01 - Non intersection 42%, 02 - Intersection relate 27%, 03 - At intersection 21%, 04 - At/near private dri 9%, 07 - Overpass or bridge 1%, 05 - At railway crossing 0% |
| `Classification_of_Accident` | cat | 100% | 3 | 03 - P.D. only 82%, 02 - Non-fatal injury 18%, 01 - Fatal injury 0% |
| `Initial_Impact_Type` | cat | 100% | 8 | 03 - Rear end 34%, 07 - SMV other 18%, 02 - Angle 14%, 04 - Sideswipe 12%, 05 - Turning movement 11%, 06 - SMV unattended vehi 8% |
| `Environment_Condition` | cat | 100% | 8 | 01 - Clear 76%, 03 - Snow 12%, 02 - Rain 9%, 04 - Freezing Rain 1%, 05 - Drifting Snow 1%, 07 - Fog, mist, smoke, d 0% |
| `Light` | cat | 100% | 5 | 01 - Daylight 70%, 07 - Dark 22%, 05 - Dusk 4%, 03 - Dawn 2%, 00 - Unknown 1% |
| `Road_Surface_Condition` | cat | 100% | 11 | 01 - Dry 63%, 02 - Wet 19%, 03 - Loose snow 8%, 06 - Ice 5%, 04 - Slush 3%, 05 - Packed snow 3% |
| `Traffic_Control` | cat | 99% | 8 | 10 - No control 52%, 01 - Traffic signal 37%, 02 - Stop sign 10%, 03 - Yield sign 1%, 08 - Traffic gate 0%, 09 - Traffic controller 0% |
| `Traffic_Control_Condition` | cat | 47% | 4 | 01 - Functioning 91%, 00 - Unknown 8%, 02 - Not functioning 0%, 03 - Obscured 0% |
| `No__of_Vehicles` | num | 100% | 6 | 1.00 · p25 1.00 · p50 2.00 · p95 3.00 · max 6.00  ▃▁▁█▁▁▁▁▁▁▁▁▁▁▁▁ |
| `No__of_Bicycles` | num | 100% | 3 | 0.00 · p25 0.00 · p50 0.00 · p95 0.00 · max 2.00  █▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁ |
| `No__of_Motorcycles` | num | 100% | 3 | 0.00 · p25 0.00 · p50 0.00 · p95 0.00 · max 2.00  █▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁ |
| `No__of_Pedestrians` | num | 100% | 4 | 0.00 · p25 0.00 · p50 0.00 · p95 0.00 · max 4.00  █▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁ |
| `Max_Injury` | cat | 18% | 4 | 02 - Minor 60%, 01 - Minimal 35%, 03 - Major 4%, 04 - Fatal 1% |
| `No__of_Injuries` | num | 100% | 9 | 0.00 · p25 0.00 · p50 0.00 · p95 1.00 · max 25.00  █▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁ |
| `No__of_Minimal` | num | 7% | 5 | 1.00 · p25 1.00 · p50 1.00 · p95 2.00 · max 5.00  █▁▁▂▁▁▁▁▁▁▁▁▁▁▁▁ |
| `No__of_Minor` | num | 11% | 7 | 1.00 · p25 1.00 · p50 1.00 · p95 2.00 · max 16.00  █▂▁▁▁▁▁▁▁▁▁▁▁▁▁▁ |
| `No__of_Major` | num | 0% | 3 | 1.00 · p25 1.00 · p50 1.00 · p95 2.00 · max 3.00  █▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁ |
| `No__of_Fatal` | num | 0% | 3 | 1.00 · p25 1.00 · p50 1.00 · p95 2.00 · max 6.00  █▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁ |
| `X` | num | 100% | 13,237 | 317,703 · p25 363,229 · p50 367,744 · p95 382,645 · max 401,040  ▁▁▁▁▁▁▂▂▄█▅▂▂▁▁▁ |
| `Y` | num | 100% | 13,480 | 4,981,259 · p25 5,022,062 · p50 5,027,402 · p95 5,036,160 · max 5,043,416  ▁▁▁▁▁▁▁▁▂▃▄▅█▄▂▁ |
| `Latitude` | num | 100% | 14,770 | 44.97 · p25 45.34 · p50 45.38 · p95 45.46 · max 45.52  ▁▁▁▁▁▁▁▁▂▃▄▅█▅▂▁ |
| `Longitude` | num | 100% | 14,776 | -76.34 · p25 -75.75 · p50 -75.70 · p95 -75.50 · max -75.27  ▁▁▁▁▁▁▂▂▄█▅▂▂▁▁▁ |
| `ObjectId` | num | 100% | 15,156 | 1.00 · p25 3,790 · p50 7,578 · p95 14,398 · max 15,156  █▇▇▇▇█▇▇▇▇█▇▇▇▇█ |

## Candidate questions

- Trend / seasonality of open_2013_tabular_transportation_collision_data over `Accident_Date`; structural breaks?
- Spatial clustering of open_2013_tabular_transportation_collision_data; overlay wards + the decision timeline

_profiled 2026-09-09 · `python3 tools/profile.py open_2013_tabular_transportation_collision_data`_
