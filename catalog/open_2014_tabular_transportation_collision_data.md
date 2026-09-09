# 2014 Tabular Transportation Collision Data

`open_2014_tabular_transportation_collision_data` · shape **arcgis-hub** · source `open-ottawa` · **spatial**

- origin: <https://open.ottawa.ca/datasets/ottawa::2014-tabular-transportation-collision-data>
- fetched 2026-09-09 · **14,843 rows** · 28 columns
- csv · licence: https://ottawa.ca/en/city-hall/get-know-your-city/open-data#open-data-licence-ve

## Columns

| column | kind | non-null | distinct | summary |
| --- | --- | --- | --- | --- |
| `Anom_ID` | id/text | 100% | 14,843 | e.g. 14--1, 14--2, 14--3 |
| `Accident_Date` | date | 100% | 365 | 2014-01-01 → 2014-12-31 |
| `Accident_Time` | date | 100% | 1,352 | 2026-09-09 → 2026-09-09 |
| `Location` | text | 100% | 5,686 | e.g. DONALD ST @ ST. LAUREN, ST. JOSEPH BLVD @ TENT, BEATRICE DR btwn KILBA |
| `Geo_ID` | text | 100% | 5,686 | e.g. 8630, 9163, __4LT4QR |
| `Accident_Location` | cat | 100% | 7 | 01 - Non intersection 39%, 02 - Intersection relate 30%, 03 - At intersection 21%, 04 - At/near private dri 9%, 07 - Overpass or bridge 1%, 05 - At railway crossing 0% |
| `Classification_of_Accident` | cat | 100% | 3 | 03 - P.D. only 82%, 02 - Non-fatal injury 18%, 01 - Fatal injury 0% |
| `Initial_Impact_Type` | cat | 100% | 8 | 03 - Rear end 34%, 07 - SMV other 17%, 02 - Angle 14%, 04 - Sideswipe 12%, 05 - Turning movement 11%, 06 - SMV unattended vehi 8% |
| `Environment_Condition` | cat | 100% | 8 | 01 - Clear 80%, 02 - Rain 10%, 03 - Snow 7%, 04 - Freezing Rain 1%, 05 - Drifting Snow 1%, 07 - Fog, mist, smoke, d 0% |
| `Light` | cat | 100% | 5 | 01 - Daylight 69%, 07 - Dark 22%, 05 - Dusk 4%, 03 - Dawn 3%, 00 - Unknown 2% |
| `Road_Surface_Condition` | cat | 100% | 11 | 01 - Dry 66%, 02 - Wet 19%, 03 - Loose snow 5%, 06 - Ice 4%, 04 - Slush 2%, 05 - Packed snow 2% |
| `Traffic_Control` | cat | 100% | 8 | 10 - No control 50%, 01 - Traffic signal 39%, 02 - Stop sign 10%, 03 - Yield sign 1%, 11 - Roundabout 1%, 08 - Traffic gate 0% |
| `Traffic_Control_Condition` | cat | 50% | 5 | 01 - Functioning 89%, 00 - Unknown 10%, 02 - Not functioning 1%, 03 - Obscured 0%, 04 - Missing/Damaged 0% |
| `No__of_Vehicles` | num | 100% | 7 | 1.00 · p25 1.00 · p50 2.00 · p95 3.00 · max 9.00  ▃█▁▁▁▁▁▁▁▁▁▁▁▁▁▁ |
| `No__of_Bicycles` | num | 100% | 3 | 0.00 · p25 0.00 · p50 0.00 · p95 0.00 · max 2.00  █▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁ |
| `No__of_Motorcycles` | num | 100% | 3 | 0.00 · p25 0.00 · p50 0.00 · p95 0.00 · max 2.00  █▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁ |
| `No__of_Pedestrians` | num | 100% | 4 | 0.00 · p25 0.00 · p50 0.00 · p95 0.00 · max 3.00  █▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁ |
| `Max_Injury` | cat | 17% | 4 | 02 - Minor 55%, 01 - Minimal 40%, 03 - Major 4%, 04 - Fatal 1% |
| `No__of_Injuries` | num | 100% | 9 | 0.00 · p25 0.00 · p50 0.00 · p95 1.00 · max 10.00  █▂▁▁▁▁▁▁▁▁▁▁▁▁▁▁ |
| `No__of_Minimal` | num | 8% | 6 | 1.00 · p25 1.00 · p50 1.00 · p95 2.00 · max 8.00  █▁▂▁▁▁▁▁▁▁▁▁▁▁▁▁ |
| `No__of_Minor` | num | 10% | 6 | 1.00 · p25 1.00 · p50 1.00 · p95 2.00 · max 7.00  █▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁ |
| `No__of_Major` | num | 0% | 3 | 1.00 · p25 1.00 · p50 1.00 · p95 2.00 · max 3.00  █▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁ |
| `No__of_Fatal` | num | 0% | 2 | 1.00 · p25 1.00 · p50 1.00 · p95 1.00 · max 2.00  █▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁ |
| `X` | num | 100% | 12,973 | 317,666 · p25 363,300 · p50 367,859 · p95 382,891 · max 401,482  ▁▁▁▁▁▁▂▁▄█▅▂▂▁▁▁ |
| `Y` | num | 100% | 13,062 | 4,981,432 · p25 5,021,946 · p50 5,027,355 · p95 5,036,206 · max 5,043,363  ▁▁▁▁▁▁▁▁▂▃▅▅█▅▂▁ |
| `Latitude` | num | 100% | 14,217 | 44.97 · p25 45.33 · p50 45.38 · p95 45.46 · max 45.52  ▁▁▁▁▁▁▁▁▂▃▅▅█▅▂▁ |
| `Longitude` | num | 100% | 14,215 | -76.34 · p25 -75.75 · p50 -75.69 · p95 -75.50 · max -75.27  ▁▁▁▁▁▁▂▁▄█▅▂▂▁▁▁ |
| `ObjectId` | num | 100% | 14,843 | 1.00 · p25 3,712 · p50 7,422 · p95 14,101 · max 14,843  ██▇██▇██▇█▇██▇██ |

## Candidate questions

- Trend / seasonality of open_2014_tabular_transportation_collision_data over `Accident_Date`; structural breaks?
- Spatial clustering of open_2014_tabular_transportation_collision_data; overlay wards + the decision timeline

_profiled 2026-09-09 · `python3 tools/profile.py open_2014_tabular_transportation_collision_data`_
