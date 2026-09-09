# 311 service requests — current year (rolling)

`311-current` · shape **rolling-csv** · source `open311`

- origin: <https://311opendatastorage.blob.core.windows.net/311data/311opendata_currentyear.csv>
- fetched 2026-09-09 · **266,424 rows** · 11 columns
- rolling file — re-ingest to refresh

## Columns

| column | kind | non-null | distinct | summary |
| --- | --- | --- | --- | --- |
| `Service Request ID | Numéro de demande` | num | 100% | 266,424 | 20,255,013,231 · p25 202,658,050,244 · p50 202,658,118,104 · p95 202,658,241,304 · max 202,658,254,942  ▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁█ |
| `Status | État` | cat | 100% | 3 | Resolved 89%, Active 9%, Cancelled 1% |
| `Type | Type` | cat | 100% | 11 | Garbage and Recycling 28%, Roads and Transportation 18%, Water and the Environmen 18%, Bylaw Services 17%, Parking Control Enforcem 15%, Recreation and Culture 2% |
| `Description | Description` | text | 100% | 787 | e.g. Road Maintenance - Ope, Road and Sidewalks | R, Property Standards - B |
| `Opened Date | Date d'ouverture` | date | 100% | 252 | 2026-01-01 → 2026-09-09 |
| `Closed Date | Date de fermeture` | date | 100% | 253 | 2026-01-01 → 2026-09-09 |
| `Address | Adresse` | text | 100% | 24,061 | e.g. 42 - 1958 Maple Run Av, \N, 40 Hearst Way |
| `Latitude | Latitude` | text | 100% | 36,155 | e.g. 45.452106832700295, \N, 45.318378580839 |
| `Longitude | Longitude` | text | 100% | 35,877 | e.g. -75.53062458418931, \N, -75.88497663808299 |
| `Ward | Quartier` | cat | 100% | 25 | \N 11%, 8 6%, 12 5%, 7 5%, 14 5%, 3 5% |
| `Channel | Voie de service` | cat | 100% | 8 | Web 51%, Dispatch 40%, Data In 7%, Walk-In 1%, Phone 1%, Email 1% |

## Candidate questions

- `Service Request ID | Numéro de demande` by `Ward | Quartier` — equity gradient? (join ONS income)
- Trend / seasonality of 311-current over `Opened Date | Date d'ouverture`; structural breaks?

_profiled 2026-09-09 · `python3 tools/profile.py 311-current`_
