# Hate Crime Open Data

`ops_hate_crime_open_data` · shape **arcgis-hub** · source `ops-data-portal`

- origin: <https://data.ottawapolice.ca/datasets/51835c5404674036ac03a119c2e590cd_0>
- fetched 2026-09-09 · **1,574 rows** · 16 columns
- csv · licence: https://data.ottawapolice.ca/pages/about#termsofuse

## Columns

| column | kind | non-null | distinct | summary |
| --- | --- | --- | --- | --- |
| `OBJECTID` | num | 100% | 1,574 | 1.00 · p25 394 · p50 788 · p95 1,495 · max 1,574  █▇▇█▇▇█▇▇█▇▇█▇▇█ |
| `ID` | num | 100% | 1,574 | 1.00 · p25 394 · p50 788 · p95 1,495 · max 1,574  █▇▇█▇▇█▇▇█▇▇█▇▇█ |
| `Year` | num | 100% | 5 | 2,021 · p25 2,022 · p50 2,023 · p95 2,025 · max 2,025  ▅▁▁▆▁▁▁▇▁▁▁█▁▁▁▇ |
| `Reported Date` | date | 100% | 962 | 2021-01-07 → 2025-12-27 |
| `Occurred Date` | date | 100% | 996 | 2019-04-19 → 2025-12-27, 2 gaps >30d |
| `Weekday` | cat | 100% | 7 | Friday 17%, Wednesday 15%, Thursday 14%, Tuesday 14%, Monday 14%, Sunday 13% |
| `Hate Crime Type` | cat | 100% | 10 | Race/Ethnicity 39%, Religion 36%, Sexual Orientation 13%, Combination (More than 2 4%, Gender 3%, Immigrants/Newcomers to  3% |
| `Hate Crime Motivation` | text | 100% | 40 | e.g. Black, Jewish, Multiple Races/Ethnici |
| `Offence Category` | text | 100% | 66 | e.g. Mischief To Property, Assault With Weapon Or, Mischief With Data |
| `Neighbourhood` | text | 99% | 104 | e.g. Hunt Club Upper -Bloss, Stittsville, Centretown |
| `Sector` | cat | 99% | 19 | Sector 23 12%, Sector 13 11%, Sector 24 9%, Sector 22 9%, Sector 16 7%, Sector 31 6% |
| `Division` | cat | 99% | 3 | Central 39%, West 33%, East 28% |
| `Census Tract` | num | 100% | 208 | 5,050,001 · p25 5,050,034 · p50 5,050,054 · p95 5,050,171 · max 5,050,302  ▆▆█▁▁▁▄▇▃▁▂▁▁▁▁▁ |
| `Ward` | cat | 100% | 24 | Ward 14 - Somerset 13%, Ward 12 - Rideau-Vanier 12%, Ward 17 - Capital 7%, Ward 16 - River 5%, Ward 8 - College 5%, Ward 18 - Alta Vista 5% |
| `Councillor` | cat | 100% | 24 | Ariel Troster 13%, Stéphanie Plante 12%, Shawn Menard 7%, Riley Brockington 5%, Laine Johnson 5%, Marty Carr 5% |
| `Offence Type` | cat | 100% | 2 | Criminal 89%, Non-Criminal 11% |

## Candidate questions

- `Census Tract` by `Neighbourhood` — equity gradient? (join ONS income)
- Trend / seasonality of ops_hate_crime_open_data over `Year`; structural breaks?

_profiled 2026-09-09 · `python3 tools/profile.py ops_hate_crime_open_data`_
