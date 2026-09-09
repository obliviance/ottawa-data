# Overdose Calls

`open_overdose_calls` · shape **arcgis-hub** · source `open-ottawa`

- origin: <https://open.ottawa.ca/datasets/ottawa::overdose-calls>
- fetched 2026-09-09 · **6,824 rows** · 5 columns
- csv · licence: https://data.ottawapolice.ca/pages/open-data-licence

## Columns

| column | kind | non-null | distinct | summary |
| --- | --- | --- | --- | --- |
| `OBJECTID` | num | 100% | 6,824 | 1.00 · p25 1,707 · p50 3,412 · p95 6,483 · max 6,824  █▇█▇█▇█▇▇█▇█▇█▇█ |
| `Reported Date` | date | 100% | 2,394 | 2017-03-02 → 2025-12-31 |
| `Day of Week` | cat | 100% | 7 | Friday 15%, Wednesday 15%, Thursday 14%, Saturday 14%, Sunday 14%, Monday 14% |
| `Year` | num | 100% | 9 | 2,017 · p25 2,021 · p50 2,023 · p95 2,025 · max 2,025  ▁▁▁▂▁▃▁▃▁▃▁█▁▆▁▄ |
| `Narcan Administered` | cat | 61% | 2 | Yes 96%, No 4% |

## Candidate questions

- Trend / seasonality of open_overdose_calls over `Reported Date`; structural breaks?

_profiled 2026-09-09 · `python3 tools/profile.py open_overdose_calls`_
