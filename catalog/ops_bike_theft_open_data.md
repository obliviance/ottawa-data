# Bike Theft Open Data

`ops_bike_theft_open_data` · shape **arcgis-hub** · source `ops-data-portal`

- origin: <https://data.ottawapolice.ca/datasets/eff8a6410ec74136b5f611017e244a4e_0>
- fetched 2026-09-09 · **15,676 rows** · 28 columns
- csv · licence: https://data.ottawapolice.ca/pages/about#termsofuse

## Columns

| column | kind | non-null | distinct | summary |
| --- | --- | --- | --- | --- |
| `OBJECTID` | num | 100% | 15,676 | 1.00 · p25 3,920 · p50 7,838 · p95 14,892 · max 15,676  ███▇██▇██▇██▇███ |
| `ID` | num | 100% | 15,676 | 1.00 · p25 3,920 · p50 7,838 · p95 14,892 · max 15,676  ███▇██▇██▇██▇███ |
| `Year` | num | 100% | 8 | 2,018 · p25 2,019 · p50 2,021 · p95 2,025 · max 2,025  ▇▁▇▁█▁▇▁▁▇▁▇▁▆▁▆ |
| `Reported Date` | date | 100% | 2,483 | 2018-01-05 → 2025-12-31 |
| `Occurred Date` | date | 100% | 2,491 | 2010-09-01 → 2025-12-31, 4 gaps >30d |
| `Day of Week` | cat | 100% | 7 | Tuesday 18%, Wednesday 17%, Friday 15%, Monday 14%, Thursday 14%, Saturday 11% |
| `Offence Category` | text | 100% | 125 | e.g. Theft< Bicycle, Prop Found/ Rec, Credit Card Data |
| `Bicycle Style` | cat | 100% | 6 | Men's 52%, Unisex 23%, Women's 17%, Child's 7%, Nodata 1%, Escooter (Esc) 1% |
| `Bicycle Value` | num | 56% | 666 | 0.00 · p25 350 · p50 609 · p95 3,000 · max 20,000  █▂▁▁▁▁▁▁▁▁▁▁▁▁▁▁ |
| `Bicycle Make` | text | 99% | 1,654 | e.g. DIVINCI, KAZOOM, PECCO |
| `Bicycle Model` | text | 73% | 5,351 | e.g. SILVERSTONE, DASH, XTRAIL |
| `Bicycle Type` | cat | 100% | 10 | Mountain 42%, Hybrid 25%, Regular 11%, Other 9%, Racer 7%, Touring 4% |
| `Bicycle Frame Size` | num | 3% | 42 | 0.00 · p25 18.00 · p50 20.00 · p95 56.00 · max 5,253  █▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁ |
| `Bicycle Colour` | text | 99% | 414 | e.g. RED, PURPLE, BLU |
| `Bicycle Speed` | num | 93% | 45 | 0.00 · p25 1.00 · p50 18.00 · p95 24.00 · max 247  ▇█▁▁▁▁▁▁▁▁▁▁▁▁▁▁ |
| `Neighbourhood` | text | 100% | 107 | e.g. Centretown, Lowertown, Byward Market |
| `Sector` | cat | 100% | 19 | Sector 24 16%, Sector 23 16%, Sector 33 15%, Sector 22 13%, Sector 21 9%, Sector 25 7% |
| `Division` | cat | 100% | 3 | Central 60%, East 24%, West 15% |
| `Census Tract` | num | 100% | 217 | 5,050,001 · p25 5,050,019 · p50 5,050,042 · p95 5,050,151 · max 5,050,302  ▆▄█▁▁▁▁▂▁▁▁▁▁▁▁▁ |
| `Status` | cat | 100% | 10 | Stolen 62%, Found 22%, Seized 7%, Disposal 6%, Recovered 3%, Lost 0% |
| `Intersection` | text | 99% | 3,675 | e.g. MACLAREN ST, METCALFE , BAY ST, COOPER ST, CUMBERLAND ST, GEORGE  |
| `Time of Day` | cat | 100% | 4 | Afternoon 34%, Morning 31%, Evening 24%, Night 11% |
| `Ward` | cat | 100% | 24 | Ward 12 - Rideau-Vanier 20%, Ward 14 - Somerset 19%, Ward 10 - Gloucester-Sou 13%, Ward 17 - Capital 10%, Ward 15 - Kitchissippi 8%, Ward 13 - Rideau-Rockcli 4% |
| `Councillor` | cat | 100% | 24 | Stéphanie Plante 20%, Ariel Troster 19%, Jessica Bradley 13%, Shawn Menard 10%, Jeff Leiper 8%, Rawlson King 4% |
| `Reported Hour` | num | 100% | 24 | 0.00 · p25 1,000 · p50 1,300 · p95 2,100 · max 2,300  ▁▁▁▁▃▂▇▅▄█▃▆▃▄▂▂ |
| `Occurred Hour` | num | 100% | 24 | 0.00 · p25 900 · p50 1,300 · p95 2,200 · max 2,300  ▄▁▂▁▅▃█▄▅▇▃▇▃▅▃▄ |
| `x` | num | 99% | 3,701 | 327,233 · p25 366,593 · p50 368,231 · p95 374,135 · max 397,385  ▁▁▁▁▁▁▁▁▃█▃▁▁▁▁▁ |
| `y` | num | 99% | 3,689 | 4,990,678 · p25 5,027,120 · p50 5,030,014 · p95 5,034,039 · max 5,042,705  ▁▁▁▁▁▁▁▁▁▁▂▅█▂▁▁ |

## Candidate questions

- `Bicycle Speed` by `Neighbourhood` — equity gradient? (join ONS income)
- Trend / seasonality of ops_bike_theft_open_data over `Year`; structural breaks?

_profiled 2026-09-09 · `python3 tools/profile.py ops_bike_theft_open_data`_
