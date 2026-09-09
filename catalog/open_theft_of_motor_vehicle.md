# Theft of Motor Vehicle

`open_theft_of_motor_vehicle` · shape **arcgis-hub** · source `open-ottawa`

- origin: <https://open.ottawa.ca/datasets/ottawa::theft-of-motor-vehicle>
- fetched 2026-09-09 · **11,720 rows** · 24 columns
- csv · licence: https://data.ottawapolice.ca/pages/open-data-licence

## Columns

| column | kind | non-null | distinct | summary |
| --- | --- | --- | --- | --- |
| `OBJECTID` | num | 100% | 11,720 | 1.00 · p25 2,931 · p50 5,860 · p95 11,134 · max 11,720  █▇█▇█▇█▇▇█▇█▇█▇█ |
| `Vehicle Year` | num | 91% | 59 | 1,934 · p25 2,013 · p50 2,018 · p95 2,023 · max 2,026  ▁▁▁▁▁▁▁▁▁▁▁▁▂▄█▆ |
| `Vehicle Make` | text | 91% | 112 | e.g. HONDA/AMERICAN HONDA M, INTERNATIONAL HARVESTE, CHEVROLET |
| `Vehicle Model` | text | 60% | 329 | e.g. CIVIC (AND CRX), PILOT, SILVERADO |
| `Vehicle Style` | cat | 95% | 11 | Automobile 60%, Suv 19%, Truck 9%, Other 5%, Motorcycle 2%, Van 2% |
| `Vehicle Colour` | text | 96% | 106 | e.g. DGR, BLU, ONG |
| `Vehicle Value` | num | 20% | 290 | 30.00 · p25 12,000 · p50 40,000 · p95 90,170 · max 7,000,014  █▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁ |
| `Weekday` | cat | 100% | 7 | Friday 15%, Wednesday 15%, Tuesday 15%, Thursday 15%, Monday 14%, Saturday 13% |
| `Recovered` | cat | 95% | 2 | Y 59%, N 41% |
| `Neighbourhood` | text | 95% | 112 | e.g. Carson Grove - Carson , Orléans Avalon - Notti, East Industrial |
| `Ward` | cat | 95% | 25 | Ward 10 - Gloucester-Sou 8%, Ward 12 - Rideau-Vanier 7%, Ward 18 - Alta Vista 6%, Ward 19 - Orléans South- 5%, Ward 13 - Rideau-Rockcli 5%, Ward 14 - Somerset 5% |
| `Sector` | cat | 95% | 20 | Sector 31 12%, Sector 35 9%, Sector 13 8%, Sector 16 8%, Sector 33 7%, Sector 32 6% |
| `Reported Date` | date | 100% | 2,756 | 2018-01-01 → 2025-12-31 |
| `Occurred Date` | date | 100% | 2,782 | 2011-06-01 → 2025-12-31, 4 gaps >30d |
| `Year` | num | 100% | 8 | 2,018 · p25 2,020 · p50 2,022 · p95 2,025 · max 2,025  ▄▁▄▁▃▁▄▁▁█▁▇▁▆▁▅ |
| `Intersection` | text | 95% | 5,654 | e.g. CARVER PL, CARVER PL, LICHEN AVE, SCALA AVE, LIVERPOOL CRT, NEWMARK |
| `Division` | cat | 95% | 4 | East 42%, West 34%, Central 23%, <Data Quality> 0% |
| `Census Tract` | num | 95% | 219 | 5,050,001 · p25 5,050,032 · p50 5,050,123 · p95 5,050,190 · max 5,050,302  ▇▄▄▁▁▁█▆▃▂▂▁▁▁▁▁ |
| `Time of Day` | cat | 100% | 4 | Evening 39%, Night 23%, Afternoon 22%, Morning 16% |
| `Councillor` | cat | 95% | 24 | Jessica Bradley 8%, Stéphanie Plante 7%, Marty Carr 6%, Catherine Kitts 5%, Rawlson King 5%, Ariel Troster 5% |
| `Reported Hour` | num | 100% | 24 | 0.00 · p25 700 · p50 1,000 · p95 2,100 · max 2,300  ▂▁▂▂█▅▇▄▃▅▂▄▂▃▂▂ |
| `Occurred Hour` | num | 100% | 24 | 0.00 · p25 600 · p50 1,500 · p95 2,300 · max 2,300  ▆▂▄▂▃▂▃▂▃▃▂▅▃▇▄█ |
| `x` | num | 95% | 5,703 | 318,896 · p25 364,170 · p50 368,691 · p95 384,721 · max 401,234  ▁▁▁▁▁▁▂▂▅█▆▂▃▁▁▁ |
| `y` | num | 95% | 5,698 | 4,985,327 · p25 5,020,748 · p50 5,026,586 · p95 5,036,770 · max 5,043,124  ▁▁▁▁▁▁▁▂▅▃▆▆█▇▃▁ |

## Candidate questions

- `Census Tract` by `Neighbourhood` — equity gradient? (join ONS income)
- Trend / seasonality of open_theft_of_motor_vehicle over `Vehicle Year`; structural breaks?

_profiled 2026-09-09 · `python3 tools/profile.py open_theft_of_motor_vehicle`_
