# Ottawa Police — Dispatched Calls For Service

`ops_calls_for_service` · shape **arcgis-hub** · source `ops-data-portal` · **spatial**

- origin: <https://services7.arcgis.com/2vhcNzw0NfUwAD3d/arcgis/rest/services/Calls_For_Service/FeatureServer/0>
- fetched 2026-10-24 · **1,108,780 rows** · 14 columns
- Hub CSV export via arcgis_layers.py; 1,108,780 rows

## Columns

| column | kind | non-null | distinct | summary |
| --- | --- | --- | --- | --- |
| `OBJECTID` | num | 100% | 1,108,780 | 1.00 · p25 277,196 · p50 554,390 · p95 1,053,341 · max 1,108,780  ███▇██▇██▇██▇███ |
| `Priority` | num | 100% | 7 | 1.00 · p25 3.00 · p50 4.00 · p95 6.00 · max 7.00  ▁▁▃▁▁▅▁█▁▁▁▁▁▂▁▁ |
| `Initiated By` | cat | 100% | 2 | C 70%, O 30% |
| `Year` | num | 100% | 5 | 2,021 · p25 2,022 · p50 2,023 · p95 2,025 · max 2,025  ▇▁▁▇▁▁▁▇▁▁▁▇▁▁▁█ |
| `Received Date` | date | 100% | 1,826 | 2021-01-01 → 2025-12-31 |
| `Neighbourhood ONS ID` | num | 99% | 111 | 3.00 · p25 51.00 · p50 912 · p95 954 · max 958  ▄▂▁▁▁▁▁▁▁▁▁▁▁▁▁█ |
| `Time of Day` | cat | 100% | 4 | A 34%, E 27%, M 26%, N 14% |
| `Received Hour` | date | 100% | 24 | 1970-01-01 → 1970-01-01 |
| `Day of Week` | num | 100% | 7 | 0.00 · p25 1.00 · p50 3.00 · p95 6.00 · max 6.00  ▆▁▇▁▁▇▁▇▁▁▇▁▁█▁▇ |
| `Intersection` | text | 99% | 16,059 | e.g. HEATHERINGTON RD,ALBIO, ECCLES ST, PRESTON ST, CHESTERTON DR, SOUTHVI |
| `Neighbourhood` | text | 99% | 111 | e.g. Ledbury - Heron Gate -, West Centretown, Parkwood Hills - Stewa |
| `Ward` | num | 99% | 24 | 1.00 · p25 9.00 · p50 12.00 · p95 22.00 · max 24.00  ▃▂▂▂▄▂▅█▃▇▃▄▂▂▁▂ |
| `longitude` | num | 99% | 16,387 | -76.34 · p25 -75.74 · p50 -75.69 · p95 -75.50 · max -75.26  ▁▁▁▁▁▁▁▁▃█▄▁▁▁▁▁ |
| `latitude` | num | 99% | 16,387 | 44.97 · p25 45.35 · p50 45.40 · p95 45.46 · max 45.53  ▁▁▁▁▁▁▁▁▂▂▃▅▆█▂▁ |

## Candidate questions

- `Neighbourhood ONS ID` by `Neighbourhood ONS ID` — equity gradient? (join ONS income)
- Trend / seasonality of ops_calls_for_service over `Year`; structural breaks?
- Spatial clustering of ops_calls_for_service; overlay wards + the decision timeline

_profiled 2026-10-24 · `python3 tools/profile.py ops_calls_for_service`_
