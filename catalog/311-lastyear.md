# 311 service requests — previous year

`311-lastyear` · shape **rolling-csv** · source `open311`

- origin: <https://311opendatastorage.blob.core.windows.net/311data/311opendata_lastyear.csv>
- fetched 2026-09-09 · **372,026 rows** · 11 columns
- rolling file — re-ingest to refresh

## Columns

| column | kind | non-null | distinct | summary |
| --- | --- | --- | --- | --- |
| `Service Request ID | Numéro de demande` | num | 100% | 372,026 | 20,245,071,371 · p25 202,557,067,782 · p50 202,557,162,994 · p95 202,557,334,305 · max 202,558,029,642  ▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁█ |
| `Status | État` | cat | 100% | 3 | Resolved 96%, Active 2%, Cancelled 2% |
| `Type | Type` | cat | 100% | 12 | Garbage and Recycling 36%, Roads and Transportation 16%, Bylaw Services 16%, Water and the Environmen 14%, Parking Control Enforcem 14%, Recreation and Culture 2% |
| `Description | Description` | text | 100% | 815 | e.g. Blue Box - SWC | Colle, Vacant Property - Fail, SW - Green bins additi |
| `Opened Date | Date d'ouverture` | date | 100% | 365 | 2025-01-01 → 2025-12-31 |
| `Closed Date | Date de fermeture` | date | 100% | 603 | 2025-01-01 → 2026-09-08 |
| `Address | Adresse` | text | 100% | 28,356 | e.g. \N, 6267 Garlandside Rd, 733 Morewood Cres |
| `Latitude | Latitude` | text | 100% | 42,547 | e.g. \N, 45.356292509424456, 45.47756027349929 |
| `Longitude | Longitude` | text | 100% | 42,392 | e.g. \N, -75.27620915028346, -75.48171839259821 |
| `Ward | Quartier` | num | 100% | 25 | 1.00 · p25 7.00 · p50 13.00 · p95 23.00 · max 24.00  ▅▄▄▃▆▃▅▄▃█▃▆▄▄▃▆ |
| `Channel | Voie de service` | cat | 100% | 10 | Web 46%, Dispatch 44%, Data In 7%, Walk-In 1%, Phone 1%, Voice In 1% |

## Candidate questions

- `Service Request ID | Numéro de demande` by `Ward | Quartier` — equity gradient? (join ONS income)
- Trend / seasonality of 311-lastyear over `Opened Date | Date d'ouverture`; structural breaks?

_profiled 2026-09-09 · `python3 tools/profile.py 311-lastyear`_
