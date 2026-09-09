# 2018 Tabular Transportation Collision Data

`open_2018_tabular_transportation_collision_data` · shape **arcgis-hub** · source `open-ottawa` · **spatial**

- origin: <https://open.ottawa.ca/datasets/ottawa::2018-tabular-transportation-collision-data>
- fetched 2026-09-09 · **14,529 rows** · 28 columns
- csv · licence: https://ottawa.ca/en/city-hall/get-know-your-city/open-data#open-data-licence-ve

## Columns

| column | kind | non-null | distinct | summary |
| --- | --- | --- | --- | --- |
| `Anom_ID` | id/text | 100% | 14,529 | e.g. 18--10169, 18--1017, 18--10170 |
| `Accident_Date` | date | 100% | 365 | 2018-01-01 → 2018-12-31 |
| `Accident_Time` | date | 100% | 1,346 | 2026-09-09 → 2026-09-09 |
| `Location` | text | 100% | 5,596 | e.g. MARKETPLACE AVE @ RIOC, ALBION RD @ MITCH OWEN, INNES RD btwn BLACKBUR |
| `Geo_ID` | text | 100% | 5,596 | e.g. 10995, 4212, __3ZA3KN |
| `Accident_Location` | cat | 100% | 8 | 01 - Non intersection 39%, 02 - Intersection relate 32%, 03 - At intersection 21%, 04 - At/near private dri 7%, 07 - Overpass or bridge 0%, 05 - At railway crossing 0% |
| `Classification_of_Accident` | cat | 100% | 3 | 03 - P.D. only 81%, 02 - Non-fatal injury 18%, 01 - Fatal injury 0% |
| `Initial_Impact_Type` | cat | 100% | 8 | 03 - Rear end 33%, 07 - SMV other 17%, 02 - Angle 14%, 04 - Sideswipe 14%, 05 - Turning movement 11%, 06 - SMV unattended vehi 8% |
| `Environment_Condition` | cat | 100% | 9 | 01 - Clear 76%, 03 - Snow 11%, 02 - Rain 9%, 04 - Freezing Rain 2%, 07 - Fog, mist, smoke, d 0%, 05 - Drifting Snow 0% |
| `Light` | cat | 100% | 6 | 01 - Daylight 66%, 07 - Dark 24%, 05 - Dusk 5%, 00 - Unknown 3%, 03 - Dawn 2%, 99 - Other 0% |
| `Road_Surface_Condition` | cat | 100% | 11 | 01 - Dry 64%, 02 - Wet 19%, 03 - Loose snow 6%, 06 - Ice 5%, 04 - Slush 4%, 05 - Packed snow 2% |
| `Traffic_Control` | cat | 100% | 11 | 10 - No control 48%, 01 - Traffic signal 40%, 02 - Stop sign 11%, 11 - Roundabout 1%, 03 - Yield sign 1%, 04 - Ped. crossover 0% |
| `Traffic_Control_Condition` | cat | 52% | 5 | 01 - Functioning 94%, 00 - Unknown 5%, 02 - Not functioning 1%, 03 - Obscured 0%, 04 - Missing/Damaged 0% |
| `No__of_Vehicles` | num | 100% | 7 | 1.00 · p25 2.00 · p50 2.00 · p95 3.00 · max 7.00  ▃▁█▁▁▁▁▁▁▁▁▁▁▁▁▁ |
| `No__of_Bicycles` | num | 100% | 3 | 0.00 · p25 0.00 · p50 0.00 · p95 0.00 · max 2.00  █▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁ |
| `No__of_Motorcycles` | num | 100% | 4 | 0.00 · p25 0.00 · p50 0.00 · p95 0.00 · max 3.00  █▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁ |
| `No__of_Pedestrians` | num | 100% | 4 | 0.00 · p25 0.00 · p50 0.00 · p95 0.00 · max 3.00  █▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁ |
| `Max_Injury` | cat | 18% | 4 | 02 - Minor 53%, 01 - Minimal 41%, 03 - Major 5%, 04 - Fatal 1% |
| `No__of_Injuries` | num | 100% | 9 | 0.00 · p25 0.00 · p50 0.00 · p95 1.00 · max 8.00  █▂▁▁▁▁▁▁▁▁▁▁▁▁▁▁ |
| `No__of_Minimal` | num | 8% | 6 | 1.00 · p25 1.00 · p50 1.00 · p95 2.00 · max 8.00  █▁▂▁▁▁▁▁▁▁▁▁▁▁▁▁ |
| `No__of_Minor` | num | 10% | 7 | 1.00 · p25 1.00 · p50 1.00 · p95 2.00 · max 8.00  █▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁ |
| `No__of_Major` | num | 0% | 3 | 1.00 · p25 1.00 · p50 1.00 · p95 2.00 · max 3.00  █▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁ |
| `No__of_Fatal` | num | 0% | 2 | 1.00 · p25 1.00 · p50 1.00 · p95 1.00 · max 2.00  █▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁ |
| `X` | num | 100% | 13,902 | 317,371 · p25 363,079 · p50 367,603 · p95 382,728 · max 401,313  ▁▁▁▁▁▁▂▂▄█▅▂▂▁▁▁ |
| `Y` | num | 100% | 12,714 | 4,982,549 · p25 5,021,942 · p50 5,026,990 · p95 5,036,160 · max 5,043,420  ▁▁▁▁▁▁▁▁▃▃▅▅█▄▂▁ |
| `Latitude` | num | 100% | 12,834 | 44.98 · p25 45.33 · p50 45.38 · p95 45.46 · max 45.52  ▁▁▁▁▁▁▁▁▃▃▅▅█▅▂▁ |
| `Longitude` | num | 100% | 12,940 | -76.34 · p25 -75.76 · p50 -75.70 · p95 -75.50 · max -75.27  ▁▁▁▁▁▁▂▂▄█▅▂▂▁▁▁ |
| `ObjectId` | num | 100% | 14,529 | 1.00 · p25 3,633 · p50 7,265 · p95 13,803 · max 14,529  █▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇ |

## Candidate questions

- Trend / seasonality of open_2018_tabular_transportation_collision_data over `Accident_Date`; structural breaks?
- Spatial clustering of open_2018_tabular_transportation_collision_data; overlay wards + the decision timeline

_profiled 2026-09-09 · `python3 tools/profile.py open_2018_tabular_transportation_collision_data`_
