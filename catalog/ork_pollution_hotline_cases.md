# Pollution Hotline Cases

`ork_pollution_hotline_cases` · shape **arcgis-hub** · source `riverkeeper`

- origin: <https://ottawa-riverkeeper-open-data-ork-so.hub.arcgis.com/datasets/ork-so::pollution-hotline-cases>
- fetched 2026-09-09 · **404 rows** · 8 columns
- csv · licence: 

## Columns

| column | kind | non-null | distinct | summary |
| --- | --- | --- | --- | --- |
| `X` | num | 100% | 384 | -8,855,759 · p25 -8,472,008 · p50 -8,431,508 · p95 -8,340,558 · max -8,253,004  ▁▁▁▁▁▁▁▁▂▂▃█▂▁▁▁ |
| `Y` | num | 100% | 378 | 5,596,230 · p25 5,685,302 · p50 5,694,834 · p95 5,761,526 · max 6,079,931  ▁▁▄█▁▁▁▁▁▁▁▁▁▁▁▁ |
| `Year` | num | 100% | 11 | 2,015 · p25 2,018 · p50 2,021 · p95 2,025 · max 2,025  ▄▆▁▃▆▁▄▆▁▇▁█▅▁▄▇ |
| `Lat` | num | 100% | 378 | 44.84 · p25 45.40 · p50 45.46 · p95 45.88 · max 47.84  ▁▁▃█▂▁▁▁▁▁▁▁▁▁▁▁ |
| `Lon` | num | 100% | 384 | -79.55 · p25 -76.11 · p50 -75.74 · p95 -74.92 · max -74.14  ▁▁▁▁▁▁▁▁▂▂▃█▂▁▁▁ |
| `Category` | cat | 100% | 7 | Pollution // Pollution 34%, Biodiversity // Biodiver 20%, Garbage // Déchets 14%, Shoreline // Rivage 11%, Quantity // Quantité 10%, Development // Développe 8% |
| `Description` | id/text | 100% | 363 | e.g. Sale of Sturgeon and S, Abandoned kayakwith ta, Gas or another chemica |
| `ObjectId` | num | 100% | 404 | 1.00 · p25 102 · p50 202 · p95 384 · max 404  █▇▇▇▇█▇▇▇▇█▇▇▇▇█ |

## Candidate questions

- (none templated)

_profiled 2026-09-09 · `python3 tools/profile.py ork_pollution_hotline_cases`_
