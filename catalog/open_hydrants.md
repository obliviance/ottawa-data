# Hydrants

`open_hydrants` · shape **arcgis-hub** · source `open-ottawa`

- origin: <https://open.ottawa.ca/datasets/ottawa::hydrants>
- fetched 2026-09-09 · **28,555 rows** · 13 columns
- csv · licence: https://ottawa.ca/en/city-hall/get-know-your-city/open-data#open-data-licence-ve

## Columns

| column | kind | non-null | distinct | summary |
| --- | --- | --- | --- | --- |
| `X` | num | 100% | 28,554 | -8,465,264 · p25 -8,436,197 · p50 -8,427,401 · p95 -8,402,619 · max -8,384,798  ▁▁▅▄▂▃▇█▆▅▂▃▄▁▁▁ |
| `Y` | num | 100% | 28,553 | 5,646,711 · p25 5,667,581 · p50 5,677,633 · p95 5,696,022 · max 5,701,506  ▁▁▁▁▄█▃▅▆▅▄▄▅▆▄▁ |
| `OBJECTID` | num | 100% | 28,555 | 46,305 · p25 53,894 · p50 61,525 · p95 413,155 · max 513,482  █▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁ |
| `SUBTYPE` | num | 100% | 2 | 1.00 · p25 1.00 · p50 1.00 · p95 2.00 · max 2.00  █▁▁▁▁▁▁▁▁▁▁▁▁▁▁▂ |
| `STRUCT_ID` | id/text | 100% | 28,555 | e.g. 366030H309, 366030HP325, 366030H031 |
| `STRUCT_TYPE` | cat | 100% | 1 | WATH 100% |
| `LIFE_CYCLE_STATUS` | cat | 100% | 1 | IN_SERVICE 100% |
| `ADDRESS_QUALIFIER` | text | 0% | 0 | e.g.  |
| `MXSITEID` | cat | 62% | 1 | ESD 100% |
| `MXCREATIONSTATE` | num | 100% | 2 | 0.00 · p25 0.00 · p50 0.00 · p95 0.00 · max 1.00  █▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁ |
| `MXSTATUS` | cat | 99% | 3 | OPERATING 100%, ACTIVE 0%, LIMITEDUSE 0% |
| `MXISRUNNING` | num | 99% | 2 | 0.00 · p25 1.00 · p50 1.00 · p95 1.00 · max 1.00  ▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁█ |
| `HWYACCESSONLY` | text | 0% | 0 | e.g.  |

## Candidate questions

- (none templated)

_profiled 2026-09-09 · `python3 tools/profile.py open_hydrants`_
