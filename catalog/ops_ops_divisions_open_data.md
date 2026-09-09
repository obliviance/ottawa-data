# OPS Divisions Open Data

`ops_ops_divisions_open_data` · shape **arcgis-hub** · source `ops-data-portal`

- origin: <https://data.ottawapolice.ca/datasets/db13b683d274484e8220bb0fc60d77d9_0>
- fetched 2026-09-09 · **3 rows** · 5 columns
- csv · licence: https://data.ottawapolice.ca/pages/about#termsofuse

## Columns

| column | kind | non-null | distinct | summary |
| --- | --- | --- | --- | --- |
| `OBJECTID` | num | 100% | 3 | 1.00 · p25 1.50 · p50 2.00 · p95 2.90 · max 3.00  █▁▁▁▁▁▁█▁▁▁▁▁▁▁█ |
| `DIVISION_N_EN` | cat | 100% | 3 | West 33%, Central 33%, East 33% |
| `DIVISION_N_FR` | cat | 100% | 3 | Ouest 33%, Central 33%, Est 33% |
| `Shape__Area` | num | 100% | 3 | 106,449,950 · p25 1,145,230,213 · p50 2,184,010,477 · p95 3,429,828,113 · max 3,568,252,295  █▁▁▁▁▁▁▁▁█▁▁▁▁▁█ |
| `Shape__Length` | num | 100% | 3 | 61,386 · p25 143,425 · p50 225,463 · p95 284,069 · max 290,580  █▁▁▁▁▁▁▁▁▁▁█▁▁▁█ |

## Candidate questions

- (none templated)

_profiled 2026-09-09 · `python3 tools/profile.py ops_ops_divisions_open_data`_
