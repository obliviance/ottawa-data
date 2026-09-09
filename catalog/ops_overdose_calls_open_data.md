# Overdose Calls Open Data

`ops_overdose_calls_open_data` · shape **arcgis-hub** · source `ops-data-portal`

- origin: <https://data.ottawapolice.ca/datasets/c27e0329d113468b8308a508b6e6f097_0>
- fetched 2026-09-09 · **6,824 rows** · 5 columns
- csv · licence: https://data.ottawapolice.ca/pages/about#termsofuse

## Columns

| column | kind | non-null | distinct | summary |
| --- | --- | --- | --- | --- |
| `OBJECTID` | num | 100% | 6,824 | 1.00 · p25 1,707 · p50 3,412 · p95 6,483 · max 6,824  █▇█▇█▇█▇▇█▇█▇█▇█ |
| `Reported Date` | date | 100% | 2,394 | 2017-03-02 → 2025-12-31 |
| `Day of Week` | cat | 100% | 7 | Friday 15%, Wednesday 15%, Thursday 14%, Saturday 14%, Sunday 14%, Monday 14% |
| `Year` | num | 100% | 9 | 2,017 · p25 2,021 · p50 2,023 · p95 2,025 · max 2,025  ▁▁▁▂▁▃▁▃▁▃▁█▁▆▁▄ |
| `Narcan Administered` | cat | 61% | 2 | Yes 96%, No 4% |

## Candidate questions

- Trend / seasonality of ops_overdose_calls_open_data over `Reported Date`; structural breaks?

_profiled 2026-09-09 · `python3 tools/profile.py ops_overdose_calls_open_data`_
