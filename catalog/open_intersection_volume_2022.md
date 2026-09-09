# Intersection Volume 2022

`open_intersection_volume_2022` · shape **arcgis-hub** · source `open-ottawa`

- origin: <https://open.ottawa.ca/datasets/ottawa::intersection-volume-2022>
- fetched 2026-09-09 · **500 rows** · 11 columns
- csv · licence: https://ottawa.ca/en/city-hall/get-know-your-city/open-data#open-data-licence-ve

## Columns

| column | kind | non-null | distinct | summary |
| --- | --- | --- | --- | --- |
| `Intersection` | text | 100% | 390 | e.g. ALTHA AVE @ LEVIS AVE, LAURIER AVE @ WALLER S, HAZELDEAN RD @ WEST RI |
| `All_Motorized_Vehicles_AADT_24_` | num | 100% | 386 | 0.00 · p25 876 · p50 9,662 · p95 31,244 · max 47,392  █▂▃▄▂▃▂▂▁▁▁▁▁▁▁▁ |
| `Truck_Percent` | num | 100% | 292 | 0.00 · p25 0.01 · p50 0.03 · p95 0.08 · max 0.32  ▆█▄▁▁▁▁▁▁▁▁▁▁▁▁▁ |
| `Pedestrians_Not_Factored` | num | 100% | 372 | 0.00 · p25 58.50 · p50 230 · p95 3,643 · max 12,196  █▂▁▁▁▁▁▁▁▁▁▁▁▁▁▁ |
| `Bicycles_Not_Factored` | num | 100% | 226 | 0.00 · p25 4.00 · p50 33.00 · p95 571 · max 2,388  █▂▁▁▁▁▁▁▁▁▁▁▁▁▁▁ |
| `Date` | date | 100% | 79 | 2022-01-11 → 2022-10-14, 1 gaps >30d |
| `X` | num | 100% | 389 | 334,081 · p25 364,138 · p50 368,095 · p95 380,755 · max 388,149  ▁▁▁▁▁▁▁▁▂▄█▂▁▁▁▁ |
| `Y` | num | 100% | 389 | 4,993,224 · p25 5,023,186 · p50 5,027,979 · p95 5,033,723 · max 5,039,901  ▁▁▁▁▁▁▁▂▁▂▃▄█▃▁▁ |
| `Lat` | num | 100% | 390 | 45.08 · p25 45.35 · p50 45.39 · p95 45.44 · max 45.49  ▁▁▁▁▁▁▁▂▂▂▃▄█▃▁▁ |
| `Long` | num | 100% | 390 | -76.13 · p25 -75.74 · p50 -75.69 · p95 -75.53 · max -75.44  ▁▁▁▁▁▁▁▁▂▄█▂▁▁▁▁ |
| `ObjectId` | num | 100% | 500 | 1.00 · p25 126 · p50 250 · p95 475 · max 500  █▇▇▇▇█▇▇▇▇█▇▇▇▇█ |

## Candidate questions

- (none templated)

_profiled 2026-09-09 · `python3 tools/profile.py open_intersection_volume_2022`_
