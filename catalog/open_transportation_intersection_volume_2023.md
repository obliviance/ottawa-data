# Transportation Intersection Volume 2023

`open_transportation_intersection_volume_2023` · shape **arcgis-hub** · source `open-ottawa`

- origin: <https://open.ottawa.ca/datasets/ottawa::transportation-intersection-volume-2023>
- fetched 2026-09-09 · **483 rows** · 11 columns
- csv · licence: https://ottawa.ca/en/city-hall/get-know-your-city/open-data#open-data-licence-ve

## Columns

| column | kind | non-null | distinct | summary |
| --- | --- | --- | --- | --- |
| `Intersection` | id/text | 100% | 441 | e.g. RUSSELL RD @ RUSSELL R, PORTOBELLO BLVD @ CAPR, HALL RD S @ RUSSELL RD |
| `All_Motorized_Vehicles_AADT_24_` | num | 100% | 478 | 32.00 · p25 3,832 · p50 10,296 · p95 41,867 · max 80,553  █▅▅▃▂▂▁▁▁▁▁▁▁▁▁▁ |
| `Truck_Percent` | num | 100% | 343 | 0.00 · p25 0.02 · p50 0.03 · p95 0.10 · max 0.28  ▂█▄▂▁▁▁▁▁▁▁▁▁▁▁▁ |
| `Pedestrians_Not_Factored` | num | 100% | 297 | 0.00 · p25 20.00 · p50 114 · p95 2,920 · max 14,299  █▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁ |
| `Bicycles_Not_Factored` | num | 100% | 158 | 0.00 · p25 3.00 · p50 17.00 · p95 319 · max 1,338  █▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁ |
| `Date` | date | 100% | 104 | 2023-01-10 → 2023-12-21 |
| `X` | num | 100% | 441 | 322,194 · p25 363,737 · p50 367,736 · p95 384,829 · max 397,770  ▁▁▁▁▁▁▂▁▃█▄▂▂▂▁▁ |
| `Y` | num | 100% | 441 | 4,991,102 · p25 5,016,273 · p50 5,026,635 · p95 5,036,368 · max 5,041,605  ▁▁▁▁▁▂▂▅▂▃▅▅█▅▃▁ |
| `Lat` | num | 100% | 441 | 45.06 · p25 45.28 · p50 45.38 · p95 45.46 · max 45.51  ▁▁▁▁▁▂▂▅▂▃▄▅█▄▂▁ |
| `Long` | num | 100% | 440 | -76.28 · p25 -75.75 · p50 -75.70 · p95 -75.48 · max -75.31  ▁▁▁▁▁▁▂▁▃█▄▂▂▂▁▁ |
| `FID` | num | 100% | 483 | 1.00 · p25 122 · p50 242 · p95 459 · max 483  █▇▇▇▇▇▇█▇▇▇▇▇▇▇█ |

## Candidate questions

- (none templated)

_profiled 2026-09-09 · `python3 tools/profile.py open_transportation_intersection_volume_2023`_
