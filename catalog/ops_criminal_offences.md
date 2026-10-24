# Ottawa Police — Criminal Offences (open data)

`ops_criminal_offences` · shape **arcgis-hub** · source `ops-data-portal` · **spatial**

- origin: <https://services7.arcgis.com/2vhcNzw0NfUwAD3d/arcgis/rest/services/Criminal_Offences_Open_Data/FeatureServer/0>
- fetched 2026-10-24 · **344,290 rows** · 19 columns
- Hub CSV export via arcgis_layers.py; 344,290 rows

## Columns

| column | kind | non-null | distinct | summary |
| --- | --- | --- | --- | --- |
| `OBJECTID` | num | 100% | 344,290 | 1.00 · p25 86,073 · p50 172,146 · p95 327,076 · max 344,290  █▇▇▇▇▇▇▇▇▇▇▇▇▇▇█ |
| `Year` | num | 100% | 8 | 2,018 · p25 2,020 · p50 2,022 · p95 2,025 · max 2,025  ▆▁▆▁▅▁▅▁▁▆▁▇▁▇▁█ |
| `Reported Date` | date | 100% | 2,922 | 2018-01-01 → 2025-12-31 |
| `Reported Hour` | num | 100% | 24 | 0.00 · p25 1,000 · p50 1,400 · p95 2,100 · max 2,300  ▂▁▁▁▂▂▆▄▄█▄▇▃▅▂▃ |
| `Occurred Date` | date | 100% | 3,753 | 1948-01-01 → 2025-12-31, 162 gaps >30d |
| `Occurred Hour` | num | 100% | 24 | 0.00 · p25 1,000 · p50 1,400 · p95 2,200 · max 2,300  ▆▁▂▁▂▂▆▃▄▇▄█▄▇▃▄ |
| `Weekday` | cat | 100% | 7 | Tuesday 16%, Friday 16%, Wednesday 16%, Thursday 15%, Monday 14%, Saturday 13% |
| `Offence Summary` | cat | 100% | 3 | Crimes Against Property  68%, Crimes Against The Perso 18%, Other Criminal Code Viol 14% |
| `Offence Category` | cat | 100% | 18 | Theft $5000 and Under 36%, Other Criminal Code 14%, Fraud 14%, Assaults 9%, Mischief 8%, Other Violations Involvi 6% |
| `Neighbourhood Name` | text | 99% | 114 | e.g. Ledbury - Heron Gate -, Centretown, Byward Market |
| `Sector` | cat | 99% | 19 | Sector 23 14%, Sector 24 12%, Sector 25 8%, Sector 21 7%, Sector 31 7%, Sector 13 6% |
| `Division` | cat | 99% | 3 | Central 47%, East 27%, West 26% |
| `Census Tract` | num | 99% | 227 | 5,050,001 · p25 5,050,033 · p50 5,050,053 · p95 5,050,170 · max 5,052,001  █▃▁▁▁▁▁▁▁▁▁▁▁▁▁▁ |
| `Time of Day` | cat | 100% | 4 | Afternoon 37%, Evening 27%, Morning 21%, Night 15% |
| `Ward` | cat | 99% | 25 | Ward 12 - Rideau-Vanier 17%, Ward 14 - Somerset 16%, Ward 17 - Capital 5%, Ward 15 - Kitchissippi 5%, Ward 7 - Bay 5%, Ward 8 - College 5% |
| `Councillor` | cat | 99% | 24 | Stéphanie Plante 17%, Ariel Troster 16%, Shawn Menard 5%, Jeff Leiper 5%, Theresa Kavanagh 5%, Laine Johnson 5% |
| `Intersection` | text | 99% | 14,692 | e.g. WALKLEY RD, HEATHERING, ELGIN ST, LAURIER AVE , RIDEAU ST, 88 W OF WIL |
| `longitude` | num | 97% | 14,956 | -76.34 · p25 -75.73 · p50 -75.69 · p95 -75.52 · max -75.26  ▁▁▁▁▁▁▁▁▃█▃▁▁▁▁▁ |
| `latitude` | num | 97% | 14,956 | 44.97 · p25 45.36 · p50 45.41 · p95 45.45 · max 45.53  ▁▁▁▁▁▁▁▁▂▂▂▄▇█▁▁ |

## Candidate questions

- `Reported Hour` by `Neighbourhood Name` — equity gradient? (join ONS income)
- Trend / seasonality of ops_criminal_offences over `Year`; structural breaks?
- Spatial clustering of ops_criminal_offences; overlay wards + the decision timeline
- Concentration in `Neighbourhood Name` — which actors dominate? (join entity spine)

_profiled 2026-10-24 · `python3 tools/profile.py ops_criminal_offences`_
