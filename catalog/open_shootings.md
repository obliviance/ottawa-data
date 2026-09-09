# Shootings

`open_shootings` · shape **arcgis-hub** · source `open-ottawa`

- origin: <https://open.ottawa.ca/datasets/ottawa::shootings>
- fetched 2026-09-09 · **505 rows** · 19 columns
- csv · licence: https://data.ottawapolice.ca/pages/open-data-licence

## Columns

| column | kind | non-null | distinct | summary |
| --- | --- | --- | --- | --- |
| `OBJECTID` | num | 100% | 505 | 1.00 · p25 127 · p50 253 · p95 480 · max 505  ██▇█▇█▇█▇█▇█▇█▇█ |
| `ID` | num | 100% | 505 | 1.00 · p25 127 · p50 253 · p95 480 · max 505  ██▇█▇█▇█▇█▇█▇█▇█ |
| `Reported Date` | date | 100% | 448 | 2018-01-03 → 2025-10-15, 5 gaps >30d |
| `Reported Hour` | num | 100% | 24 | 0.00 · p25 400 · p50 1,500 · p95 2,300 · max 2,300  ▇▃▄▂▃▁▃▁▂▃▂▅▃▆▄█ |
| `Reported Year` | num | 100% | 8 | 2,018 · p25 2,019 · p50 2,021 · p95 2,025 · max 2,025  ▇▁▇▁▄▁█▁▁▆▁▇▁▅▁▄ |
| `Occurred Date` | date | 100% | 446 | 2018-01-03 → 2025-10-15, 5 gaps >30d |
| `Occurred Hour` | num | 100% | 24 | 0.00 · p25 400 · p50 1,600 · p95 2,300 · max 2,300  ▆▃▄▂▂▁▂▁▁▃▂▄▃▆▄█ |
| `Occurred Year` | num | 100% | 8 | 2,018 · p25 2,019 · p50 2,021 · p95 2,025 · max 2,025  ▇▁▇▁▄▁█▁▁▆▁▇▁▅▁▄ |
| `Time of Day` | cat | 100% | 4 | Evening 42%, Night 30%, Afternoon 19%, Morning 9% |
| `Weekday` | cat | 100% | 7 | Saturday 19%, Monday 16%, Friday 14%, Wednesday 14%, Sunday 13%, Thursday 12% |
| `Day of Week` | num | 100% | 7 | 1.00 · p25 2.00 · p50 4.00 · p95 7.00 · max 7.00  ▆▁▄▁▁▅▁▅▁▁▆▁▁█▁▅ |
| `Neighbourhood` | text | 100% | 94 | e.g. Elmvale - Eastway - Ri, Overbrook - McArthur, West Centertown |
| `Sector` | num | 100% | 19 | 11.00 · p25 17.00 · p50 25.00 · p95 35.00 · max 37.00  ▁▅▂▄▁▁▄▆▅▁▁▁▅▄█▁ |
| `Division` | cat | 100% | 3 | East 40%, Central 34%, West 26% |
| `Ward` | cat | 100% | 24 | Ward 12 - Rideau-Vanier 15%, Ward 10 - Gloucester-Sou 13%, Ward 7 - Bay 8%, Ward 18 - Alta Vista 8%, Ward 16 - River 8%, Ward 13 - Rideau-Rockcli 7% |
| `Councillor` | cat | 100% | 24 | Stéphanie Plante 15%, Jessica Bradley 13%, Theresa Kavanagh 8%, Marty Carr 8%, Riley Brockington 8%, Rawlson King 7% |
| `Census Tract` | num | 100% | 139 | 5,050,001 · p25 5,050,012 · p50 5,050,043 · p95 5,050,162 · max 5,050,301  █▅▄▁▁▂▅▂▁▁▁▁▁▁▁▁ |
| `x` | num | 100% | 407 | 322,427 · p25 365,013 · p50 368,637 · p95 379,517 · max 385,921  ▁▁▁▁▁▁▁▁▁▃▃▆█▂▁▁ |
| `y` | num | 100% | 407 | 4,998,582 · p25 5,024,046 · p50 5,027,429 · p95 5,034,773 · max 5,040,944  ▁▁▁▁▁▁▁▁▂▆▆▄█▄▁▁ |

## Candidate questions

- `Reported Hour` by `Neighbourhood` — equity gradient? (join ONS income)
- Trend / seasonality of open_shootings over `Reported Date`; structural breaks?

_profiled 2026-09-09 · `python3 tools/profile.py open_shootings`_
