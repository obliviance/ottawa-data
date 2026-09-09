# Transportation Intersection Volumes 2021

`open_transportation_intersection_volumes_2021` · shape **arcgis-hub** · source `open-ottawa`

- origin: <https://open.ottawa.ca/datasets/ottawa::transportation-intersection-volumes-2021>
- fetched 2026-09-09 · **180 rows** · 12 columns
- csv · licence: https://ottawa.ca/en/city-hall/get-know-your-city/open-data#open-data-licence-ve

## Columns

| column | kind | non-null | distinct | summary |
| --- | --- | --- | --- | --- |
| `OBJECTID__` | num | 100% | 180 | 1.00 · p25 45.75 · p50 90.50 · p95 171 · max 180  █▇▇▇▇█▇▇▇▇█▇▇▇▇█ |
| `Intersection` | id/text | 100% | 168 | e.g. RAMSAYVILLE RD @ MITCH, HANNAH ST @ MARIER AVE, BEAVERWOOD RD @ MANOTI |
| `All_Motorized_Vehicles_AADT_24H` | num | 100% | 179 | 76.00 · p25 2,134 · p50 6,794 · p95 27,701 · max 49,471  █▄▅▂▂▁▂▁▁▁▁▁▁▁▁▁ |
| `Percent_Trucks` | num | 100% | 158 | 0.00 · p25 0.03 · p50 0.04 · p95 0.14 · max 0.37  ▅█▅▂▁▁▁▁▁▁▁▁▁▁▁▁ |
| `Pedestrians_Not_Factored` | num | 100% | 128 | 0.00 · p25 19.75 · p50 79.00 · p95 745 · max 1,721  █▂▂▁▁▁▁▁▁▁▁▁▁▁▁▁ |
| `Bicycles_Not_factored` | num | 100% | 83 | 0.00 · p25 8.00 · p50 21.50 · p95 165 · max 281  █▃▂▂▁▁▁▁▁▁▁▁▁▁▁▁ |
| `Date_Collected` | date | 100% | 72 | 2021-02-17 → 2021-12-15 |
| `X` | num | 100% | 168 | 318,077 · p25 363,149 · p50 367,878 · p95 385,923 · max 394,888  ▁▁▁▁▁▁▂▂▂█▆▃▂▄▂▁ |
| `Y` | num | 100% | 168 | 4,988,762 · p25 5,016,785 · p50 5,026,843 · p95 5,038,189 · max 5,041,582  ▁▁▁▁▁▁▂▄▅▃▃▅█▆▂▂ |
| `LAT` | num | 100% | 168 | 45.04 · p25 45.29 · p50 45.38 · p95 45.48 · max 45.51  ▁▁▁▁▁▁▁▄▅▃▃▄█▅▂▂ |
| `LONG` | num | 100% | 168 | -76.33 · p25 -75.76 · p50 -75.70 · p95 -75.46 · max -75.35  ▁▁▁▁▁▁▂▂▂█▆▃▂▄▂▁ |
| `ObjectId` | num | 100% | 180 | 1.00 · p25 45.75 · p50 90.50 · p95 171 · max 180  █▇▇▇▇█▇▇▇▇█▇▇▇▇█ |

## Candidate questions

- (none templated)

_profiled 2026-09-09 · `python3 tools/profile.py open_transportation_intersection_volumes_2021`_
