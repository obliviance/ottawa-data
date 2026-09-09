# Electric Vehicle Charging Stations Usage Data

`open_electric_vehicle_charging_stations_usage_data` · shape **arcgis-hub** · source `open-ottawa` · **spatial**

- origin: <https://open.ottawa.ca/datasets/ottawa::electric-vehicle-charging-stations-usage-data>
- fetched 2026-09-09 · **22,455 rows** · 28 columns
- geojson · licence: https://ottawa.ca/en/city-hall/get-know-your-city/open-data#open-data-licence-ve

## Columns

| column | kind | non-null | distinct | summary |
| --- | --- | --- | --- | --- |
| `X` | num | 100% | 17 | -75.75 · p25 -75.69 · p50 -75.69 · p95 -75.56 · max -75.49  ▂▂▃█▆▁▁▁▁▁▁▁▁▁▁▁ |
| `Y` | num | 100% | 17 | 45.09 · p25 45.41 · p50 45.42 · p95 45.44 · max 45.44  ▂▁▁▁▁▁▁▁▁▁▁▁▁▁▆█ |
| `Transaction_ID` | num | 100% | 22,455 | 7,967,074 · p25 11,651,218 · p50 14,646,383 · p95 19,450,270 · max 19,929,408  ▂▅▆▇▆▅▆▇▆▇▇▆▆▆▇█ |
| `Session_ID` | id/text | 100% | 22,455 | e.g. ce499016-c0fe-4b76-922, daeaa8b8-2528-4b2a-a1e, 5e4d5163-2c67-4049-ac1 |
| `Session_start_date` | date | 100% | 22,446 | 2021-12-31 → 2024-06-30 |
| `Session_end_date` | date | 100% | 22,451 | 2021-12-31 → 2024-06-30 |
| `Connect_Start_Date` | date | 100% | 906 | 2021-12-31 → 2024-06-30 |
| `Connect_Start_Time` | date | 100% | 17,383 | 2026-09-09 → 2026-09-09 |
| `F24_Hour_Start_Time_Format` | date | 100% | 18,543 | 2026-09-09 → 2026-09-09 |
| `Connect_End_Date` | date | 100% | 906 | 2021-12-31 → 2024-06-30 |
| `Connect_End_Time` | date | 100% | 17,520 | 2026-09-09 → 2026-09-09 |
| `F24_Hour_Connect_End_Time` | date | 100% | 18,796 | 2026-09-09 → 2026-09-09 |
| `Charging_Time` | date | 100% | 14,127 | 2026-09-09 → 2026-09-09 |
| `Province_or_state` | cat | 100% | 1 | ON 100% |
| `Owner` | cat | 100% | 1 | City of Ottawa 100% |
| `Site` | cat | 100% | 19 | City of Ottawa - 118 Car 11%, City Hall - Ottawa 11%, City of Ottawa - 301 Lau 9%, City of Ottawa - 122 Dal 8%, City of Ottawa - 6 Oak S 7%, City of Ottawa - 186 Mai 7% |
| `Address` | cat | 100% | 19 | 118 Cartier St. 11%, 110 Laurier Ave. W 11%, 301 Laurier Ave. E 9%, 122 Daly Ave. 8%, 6 Oak St. 7%, 186 Main St. 7% |
| `POINT_X` | num | 100% | 17 | -75.75 · p25 -75.69 · p50 -75.69 · p95 -75.56 · max -75.49  ▂▂▃█▆▁▁▁▁▁▁▁▁▁▁▁ |
| `POINT_Y` | num | 100% | 17 | 45.39 · p25 45.41 · p50 45.42 · p95 45.44 · max 45.44  ▃▁▃▁▇▅▁▅▅▁▂█▂▂▁▄ |
| `Station` | text | 100% | 36 | e.g. AAA-14533, AAA-14506, AAA-14503 |
| `Card_number` | text | 100% | 5,700 | e.g. 1.10E+12, RC01086626836246, MA01090921821958 |
| `ObjectId` | text | 0% | 0 | e.g.  |
| `End_Reason` | cat | 100% | 5 | The charging cable was d 61%, Charging ended by vehicl 39%, Stopped by operator 1%, Unknown reason 0%, Charging stopped followi 0% |
| `Total_kWh` | num | 100% | 22,055 | 0.00 · p25 4.87 · p50 10.28 · p95 48.95 · max 122  █▅▃▂▁▁▁▁▁▁▁▁▁▁▁▁ |
| `ObjectId2` | num | 100% | 22,455 | 1.00 · p25 5,614 · p50 11,228 · p95 21,332 · max 22,455  █▇█▇▇█▇█▇▇█▇▇█▇█ |
| `geometry` | cat | 100% | 17 | {"type": "Point", "coord 11%, {"type": "Point", "coord 11%, {"type": "Point", "coord 11%, {"type": "Point", "coord 9%, {"type": "Point", "coord 8%, {"type": "Point", "coord 7% |
| `longitude` | num | 100% | 17 | -75.75 · p25 -75.69 · p50 -75.69 · p95 -75.56 · max -75.49  ▂▂▃█▆▁▁▁▁▁▁▁▁▁▁▁ |
| `latitude` | num | 100% | 17 | 45.09 · p25 45.41 · p50 45.42 · p95 45.44 · max 45.44  ▂▁▁▁▁▁▁▁▁▁▁▁▁▁▆█ |

## Candidate questions

- Trend / seasonality of open_electric_vehicle_charging_stations_usage_data over `Session_start_date`; structural breaks?
- Spatial clustering of open_electric_vehicle_charging_stations_usage_data; overlay wards + the decision timeline
- Concentration in `Owner` — which actors dominate? (join entity spine)

_profiled 2026-09-09 · `python3 tools/profile.py open_electric_vehicle_charging_stations_usage_data`_
