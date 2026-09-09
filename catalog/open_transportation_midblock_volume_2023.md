# Transportation Midblock Volume 2023

`open_transportation_midblock_volume_2023` · shape **arcgis-hub** · source `open-ottawa`

- origin: <https://open.ottawa.ca/datasets/ottawa::transportation-midblock-volume-2023>
- fetched 2026-09-09 · **418 rows** · 9 columns
- csv · licence: https://ottawa.ca/en/city-hall/get-know-your-city/open-data#open-data-licence-ve

## Columns

| column | kind | non-null | distinct | summary |
| --- | --- | --- | --- | --- |
| `Geo_ID` | id/text | 100% | 418 | e.g. __3Z0BKQ, __3Z0BF5, __3Z0CHT |
| `Midblock` | id/text | 100% | 418 | e.g. PRESTONE DR btwn RIVER, RAMSAYVILLE RD btwn LE, PARKWAY RD btwn GOOD S |
| `Year` | num | 100% | 1 | 2,023 · p25 2,023 · p50 2,023 · p95 2,023 · max 2,023   |
| `All_Motorized_Vehicles_AADT_24_` | num | 100% | 399 | 14.00 · p25 640 · p50 1,670 · p95 14,055 · max 30,808  █▄▁▁▁▁▁▁▁▁▁▁▁▁▁▁ |
| `X` | num | 100% | 418 | 323,801 · p25 363,042 · p50 368,110 · p95 384,906 · max 395,338  ▁▁▁▁▁▁▁▂▆█▆▃▂▃▁▁ |
| `Y` | num | 100% | 418 | 4,983,446 · p25 5,022,533 · p50 5,027,741 · p95 5,037,500 · max 5,043,289  ▁▁▁▁▁▁▁▁▃▃▇▆█▆▄▁ |
| `Lat` | num | 100% | 418 | 44.99 · p25 45.34 · p50 45.39 · p95 45.47 · max 45.52  ▁▁▁▁▁▁▁▁▃▂▇▆█▇▄▁ |
| `Long` | num | 100% | 418 | -76.26 · p25 -75.76 · p50 -75.69 · p95 -75.48 · max -75.34  ▁▁▁▁▁▁▁▂▆█▆▃▂▃▁▁ |
| `FID` | num | 100% | 418 | 1.00 · p25 105 · p50 210 · p95 397 · max 418  █▇▇▇▇▇▇▇▇▇▇▇▇▇▇█ |

## Candidate questions

- (none templated)

_profiled 2026-09-09 · `python3 tools/profile.py open_transportation_midblock_volume_2023`_
