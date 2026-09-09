# Transportation Midblock Volumes 2024

`open_transportation_midblock_volumes_2024` · shape **arcgis-hub** · source `open-ottawa`

- origin: <https://open.ottawa.ca/datasets/ottawa::transportation-midblock-volumes-2024>
- fetched 2026-09-09 · **895 rows** · 11 columns
- csv · licence: https://ottawa.ca/en/city-hall/open-transparent-and-accountable-government/open-

## Columns

| column | kind | non-null | distinct | summary |
| --- | --- | --- | --- | --- |
| `OBJECTID__` | num | 100% | 895 | 1.00 · p25 224 · p50 448 · p95 850 · max 895  ████████▇███████ |
| `Shape__` | cat | 100% | 1 | Point 100% |
| `Geo_ID` | id/text | 100% | 895 | e.g. __3Z0086, __3AHCFH, __3Z0CXK |
| `Midblock` | id/text | 100% | 895 | e.g. CRICHTON ST btwn THE M, CROWNHILL ST btwn APPL, CROWNHILL ST btwn BLAI |
| `AADT_Year` | num | 100% | 1 | 2,024 · p25 2,024 · p50 2,024 · p95 2,024 · max 2,024   |
| `Volume` | num | 100% | 760 | 17.00 · p25 371 · p50 1,025 · p95 10,355 · max 31,785  █▂▁▁▁▁▁▁▁▁▁▁▁▁▁▁ |
| `x` | num | 100% | 892 | 318,576 · p25 362,663 · p50 367,056 · p95 385,545 · max 397,965  ▁▁▁▁▁▁▂▂▄█▇▃▂▃▁▁ |
| `y` | num | 100% | 886 | 4,982,848 · p25 5,020,264 · p50 5,026,590 · p95 5,037,592 · max 5,042,572  ▁▁▁▁▁▁▁▂▄▃▅█▇▅▄▁ |
| `Lat` | num | 100% | 869 | 44.98 · p25 45.32 · p50 45.38 · p95 45.47 · max 45.52  ▁▁▁▁▁▁▁▂▄▃▄█▇▅▄▁ |
| `Long` | num | 100% | 884 | -76.32 · p25 -75.76 · p50 -75.71 · p95 -75.47 · max -75.31  ▁▁▁▁▁▁▂▂▄█▇▃▂▃▁▁ |
| `FID` | num | 100% | 895 | 1.00 · p25 224 · p50 448 · p95 850 · max 895  ████████▇███████ |

## Candidate questions

- Trend / seasonality of open_transportation_midblock_volumes_2024 over `AADT_Year`; structural breaks?

_profiled 2026-09-09 · `python3 tools/profile.py open_transportation_midblock_volumes_2024`_
