# Ottawa Police — Crime Map, year to date

`ops_crime_map_ytd` · shape **arcgis-hub** · source `crime-map` · **spatial**

- origin: <https://services7.arcgis.com/2vhcNzw0NfUwAD3d/arcgis/rest/services/CrimeMap_YTD/FeatureServer/8>
- fetched 2026-10-24 · **31,201 rows** · 27 columns
- paged by OBJECTID via arcgis_layers.py; 31,201 rows (expected ~30,349 on 2026-10-16)

## Columns

| column | kind | non-null | distinct | summary |
| --- | --- | --- | --- | --- |
| `OBJECTID` | num | 100% | 31,201 | 1.00 · p25 7,801 · p50 15,601 · p95 29,641 · max 31,201  █▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇ |
| `GO_Number` | num | 100% | 31,199 | 202,620 · p25 2,026,170,766 · p50 2,026,802,010 · p95 2,026,825,983 · max 2,026,828,574  ▁▂▁▁▁▁▁▁▁▁▁▁▁▁▁█ |
| `Offence_Summary` | cat | 100% | 2 | Crime Against Property 80%, Crime Against Persons 20% |
| `Offence_Category` | cat | 100% | 13 | Theft $5000 and Under 61%, Assaults 12%, Mischief 10%, Break and Enter 5%, Uttering Threats 4%, Theft of Motor Vehicle 3% |
| `Reported_Date` | date | 100% | 296 | 1970-01-01 → 1970-01-01 |
| `Reported_Year` | num | 100% | 1 | 2,026 · p25 2,026 · p50 2,026 · p95 2,026 · max 2,026   |
| `Reported_Hour` | num | 100% | 24 | 0.00 · p25 1,100 · p50 1,400 · p95 2,100 · max 2,300  ▂▁▁▁▁▂▅▄▄▇▄█▃▅▂▃ |
| `Occurred_Date` | date | 100% | 511 | 1970-01-01 → 1970-01-01 |
| `Occurred_Year` | num | 100% | 14 | 1,998 · p25 2,026 · p50 2,026 · p95 2,026 · max 2,026  ▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁█ |
| `Occurred_Hour` | num | 100% | 24 | 0.00 · p25 1,100 · p50 1,500 · p95 2,200 · max 2,300  ▃▁▂▁▂▂▄▃▃▇▄█▄▆▃▃ |
| `Time_of_Day` | cat | 100% | 4 | Afternoon 41%, Evening 29%, Morning 19%, Night 11% |
| `Week_Day` | cat | 100% | 7 | Friday 15%, Thursday 15%, Wednesday 15%, Tuesday 14%, Saturday 14%, Monday 14% |
| `Day_of_Week` | num | 100% | 7 | 1.00 · p25 2.00 · p50 4.00 · p95 7.00 · max 7.00  ▆▁▇▁▁▇▁▇▁▁▇▁▁█▁▇ |
| `Intersection` | text | 99% | 5,981 | e.g. KING EDWARD AVE, ST. P, CUMBERLAND ST, YORK ST, CLARENCE ST, CUMBERLAN |
| `Neighbourhood` | text | 99% | 111 | e.g. Byward Market, Ledbury - Heron Gate -, Convent Glen - Orléans |
| `Sector` | cat | 100% | 19 | Sector 24 16%, Sector 23 9%, Sector 21 7%, Sector 25 7%, Sector 14 6%, Sector 32 6% |
| `Division` | cat | 100% | 3 | Central 45%, West 27%, East 27% |
| `Ward` | cat | 100% | 25 | Ward 12 - Rideau-Vanier 20%, Ward 14 - Somerset 11%, Ward 15 - Kitchissippi 6%, Ward 7 - Bay 6%, Ward 10 - Gloucester-Sou 5%, Ward 17 - Capital 5% |
| `Councillor` | cat | 99% | 24 | Stéphanie Plante 20%, Ariel Troster 11%, Jeff Leiper 6%, Theresa Kavanagh 6%, Jessica Bradley 5%, Shawn Menard 5% |
| `Reported_Date_str` | date | 100% | 296 | 2026-01-01 → 2026-10-23 |
| `Reported_Year_str` | num | 100% | 1 | 2,026 · p25 2,026 · p50 2,026 · p95 2,026 · max 2,026   |
| `Reported_Hour_str` | cat | 100% | 24 | 15:00 8%, 16:00 8%, 14:00 8%, 17:00 8%, 13:00 7%, 12:00 7% |
| `Occurred_Date_str` | date | 100% | 511 | 1998-06-27 → 2026-10-23, 30 gaps >30d |
| `Occurred_Year_str` | num | 100% | 14 | 1,998 · p25 2,026 · p50 2,026 · p95 2,026 · max 2,026  ▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁█ |
| `Occurred_Hour_str` | cat | 100% | 24 | 16:00 8%, 17:00 7%, 15:00 7%, 18:00 7%, 14:00 7%, 12:00 6% |
| `longitude` | num | 99% | 6,043 | -76.32 · p25 -75.74 · p50 -75.69 · p95 -75.54 · max -75.27  ▁▁▁▁▁▁▁▁▄█▄▁▁▁▁▁ |
| `latitude` | num | 99% | 6,043 | 45.01 · p25 45.35 · p50 45.40 · p95 45.45 · max 45.52  ▁▁▁▁▁▁▁▁▂▂▄▄█▆▁▁ |

## Candidate questions

- `GO_Number` by `Neighbourhood` — equity gradient? (join ONS income)
- Trend / seasonality of ops_crime_map_ytd over `Reported_Date`; structural breaks?
- Spatial clustering of ops_crime_map_ytd; overlay wards + the decision timeline

_profiled 2026-10-24 · `python3 tools/profile.py ops_crime_map_ytd`_
