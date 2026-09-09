# 2016 Tabular Transportation Collision Data

`open_2016_tabular_transportation_collision_data` · shape **arcgis-hub** · source `open-ottawa` · **spatial**

- origin: <https://open.ottawa.ca/datasets/ottawa::2016-tabular-transportation-collision-data>
- fetched 2026-09-09 · **14,028 rows** · 28 columns
- csv · licence: https://ottawa.ca/en/city-hall/get-know-your-city/open-data#open-data-licence-ve

## Columns

| column | kind | non-null | distinct | summary |
| --- | --- | --- | --- | --- |
| `Anom_ID` | id/text | 100% | 14,028 | e.g. 16--1, 16--2, 16--3 |
| `Accident_Date` | date | 100% | 366 | 2016-01-01 → 2016-12-31 |
| `Accident_Time` | date | 100% | 1,339 | 2026-09-09 → 2026-09-09 |
| `Location` | text | 100% | 5,717 | e.g. PARKDALE AVE @ HWY 417, COLDWATER CRES btwn ME, NORTOBA CRES btwn STIK |
| `Geo_ID` | text | 100% | 5,717 | e.g. 2363, __807KIY, __4TZHEH |
| `Accident_Location` | cat | 100% | 9 | 01 - Non intersection 39%, 02 - Intersection relate 30%, 03 - At intersection 22%, 04 - At/near private dri 9%, 07 - Overpass or bridge 0%, 05 - At railway crossing 0% |
| `Classification_of_Accident` | cat | 100% | 3 | 03 - P.D. only 80%, 02 - Non-fatal injury 20%, 01 - Fatal injury 0% |
| `Initial_Impact_Type` | cat | 100% | 8 | 03 - Rear end 33%, 07 - SMV other 17%, 04 - Sideswipe 14%, 02 - Angle 14%, 05 - Turning movement 11%, 06 - SMV unattended vehi 8% |
| `Environment_Condition` | cat | 100% | 9 | 01 - Clear 79%, 03 - Snow 12%, 02 - Rain 7%, 04 - Freezing Rain 1%, 05 - Drifting Snow 1%, 07 - Fog, mist, smoke, d 0% |
| `Light` | cat | 100% | 10 | 01 - Daylight 68%, 07 - Dark 23%, 05 - Dusk 5%, 03 - Dawn 2%, 00 - Unknown 2%, 08 - Dark, artificial 1% |
| `Road_Surface_Condition` | cat | 100% | 10 | 01 - Dry 65%, 02 - Wet 16%, 03 - Loose snow 7%, 06 - Ice 5%, 04 - Slush 4%, 05 - Packed snow 3% |
| `Traffic_Control` | cat | 100% | 6 | 10 - No control 49%, 01 - Traffic signal 39%, 02 - Stop sign 10%, 11 - Roundabout 1%, 03 - Yield sign 0%, 04 - Ped. crossover 0% |
| `Traffic_Control_Condition` | cat | 51% | 4 | 01 - Functioning 94%, 00 - Unknown 6%, 02 - Not functioning 0%, 03 - Obscured 0% |
| `No__of_Vehicles` | num | 100% | 8 | 1.00 · p25 2.00 · p50 2.00 · p95 3.00 · max 8.00  ▃▁█▁▁▁▁▁▁▁▁▁▁▁▁▁ |
| `No__of_Bicycles` | num | 100% | 2 | 0.00 · p25 0.00 · p50 0.00 · p95 0.00 · max 1.00  █▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁ |
| `No__of_Motorcycles` | num | 100% | 4 | 0.00 · p25 0.00 · p50 0.00 · p95 0.00 · max 4.00  █▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁ |
| `No__of_Pedestrians` | num | 100% | 4 | 0.00 · p25 0.00 · p50 0.00 · p95 0.00 · max 3.00  █▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁ |
| `Max_Injury` | cat | 19% | 4 | 02 - Minor 52%, 01 - Minimal 42%, 03 - Major 5%, 04 - Fatal 1% |
| `No__of_Injuries` | num | 100% | 9 | 0.00 · p25 0.00 · p50 0.00 · p95 1.00 · max 9.00  █▂▁▁▁▁▁▁▁▁▁▁▁▁▁▁ |
| `No__of_Minimal` | num | 9% | 6 | 1.00 · p25 1.00 · p50 1.00 · p95 2.00 · max 6.00  █▁▁▂▁▁▁▁▁▁▁▁▁▁▁▁ |
| `No__of_Minor` | num | 10% | 7 | 1.00 · p25 1.00 · p50 1.00 · p95 2.00 · max 9.00  █▂▁▁▁▁▁▁▁▁▁▁▁▁▁▁ |
| `No__of_Major` | num | 0% | 3 | 1.00 · p25 1.00 · p50 1.00 · p95 1.00 · max 3.00  █▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁ |
| `No__of_Fatal` | num | 0% | 2 | 1.00 · p25 1.00 · p50 1.00 · p95 2.00 · max 2.00  █▁▁▁▁▁▁▁▁▁▁▁▁▁▁▂ |
| `X` | num | 100% | 13,309 | 318,617 · p25 363,419 · p50 367,890 · p95 383,185 · max 401,606  ▁▁▁▁▁▁▂▂▄█▄▂▂▁▁▁ |
| `Y` | num | 100% | 13,347 | 4,982,829 · p25 5,022,156 · p50 5,027,521 · p95 5,036,471 · max 5,043,440  ▁▁▁▁▁▁▁▁▃▃▅▅█▄▂▁ |
| `Latitude` | num | 100% | 13,774 | 44.98 · p25 45.34 · p50 45.38 · p95 45.46 · max 45.52  ▁▁▁▁▁▁▁▁▃▃▅▅█▅▂▁ |
| `Longitude` | num | 100% | 13,775 | -76.32 · p25 -75.75 · p50 -75.69 · p95 -75.50 · max -75.26  ▁▁▁▁▁▁▂▂▄█▄▂▂▁▁▁ |
| `ObjectId` | num | 100% | 14,028 | 1.00 · p25 3,508 · p50 7,014 · p95 13,327 · max 14,028  ███▇██▇██▇██▇███ |

## Candidate questions

- Trend / seasonality of open_2016_tabular_transportation_collision_data over `Accident_Date`; structural breaks?
- Spatial clustering of open_2016_tabular_transportation_collision_data; overlay wards + the decision timeline

_profiled 2026-09-09 · `python3 tools/profile.py open_2016_tabular_transportation_collision_data`_
