# Catch Basins

`open_catch_basins` · shape **arcgis-hub** · source `open-ottawa`

- origin: <https://open.ottawa.ca/datasets/ottawa::catch-basins>
- fetched 2026-09-09 · **147,262 rows** · 6 columns
- csv · licence: https://ottawa.ca/en/city-hall/get-know-your-city/open-data#open-data-licence-ve

## Columns

| column | kind | non-null | distinct | summary |
| --- | --- | --- | --- | --- |
| `X` | num | 100% | 147,212 | -8,484,613 · p25 -8,435,003 · p50 -8,426,960 · p95 -8,402,516 · max -8,386,925  ▁▁▁▁▁▄▂▂▆█▅▃▂▃▁▁ |
| `Y` | num | 100% | 147,211 | 5,618,435 · p25 5,668,447 · p50 5,678,725 · p95 5,695,768 · max 5,703,657  ▁▁▁▁▁▁▁▂▇▅▇▇█▇▅▁ |
| `OBJECTID` | num | 100% | 147,262 | 1.00 · p25 82,119 · p50 159,004 · p95 1,084,572 · max 1,326,899  ▇█▄▁▁▁▁▂▁▁▁▁▁▁▁▁ |
| `STRUCT_ID` | id/text | 100% | 147,262 | e.g. IN97232, IN15922, IN15891 |
| `ENABLED` | num | 100% | 2 | 0.00 · p25 1.00 · p50 1.00 · p95 1.00 · max 1.00  ▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁█ |
| `GLOBALID` | id/text | 100% | 147,262 | e.g. {FAC0E6D1-9413-432E-9A, {01917198-1BB7-4D13-84, {0DA8238A-A8AC-4C7C-B9 |

## Candidate questions

- (none templated)

_profiled 2026-09-09 · `python3 tools/profile.py open_catch_basins`_
