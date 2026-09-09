# Transportation Intersection Volumes 2018

`open_transportation_intersection_volumes_2018` · shape **arcgis-hub** · source `open-ottawa`

- origin: <https://open.ottawa.ca/datasets/ottawa::transportation-intersection-volumes-2018>
- fetched 2026-09-09 · **553 rows** · 8 columns
- csv · licence: https://ottawa.ca/en/city-hall/get-know-your-city/open-data#open-data-licence-ve

## Columns

| column | kind | non-null | distinct | summary |
| --- | --- | --- | --- | --- |
| `FID` | num | 100% | 553 | 1.00 · p25 139 · p50 277 · p95 525 · max 553  ██▇█▇█▇█▇█▇█▇█▇█ |
| `OBJECTID` | num | 100% | 553 | 1.00 · p25 139 · p50 277 · p95 525 · max 553  ██▇█▇█▇█▇█▇█▇█▇█ |
| `Intersecti` | id/text | 100% | 516 | e.g. 210 W OF MERIVALE RD @, 225 W OF LIMEBANK RD @, 250 N OF KLONDIKE RD @ |
| `All_Motori` | id/text | 100% | 548 | e.g. 29,564.00, 9,662.00, 20,551.00 |
| `F__Truck` | text | 100% | 366 | e.g. 4.00%, 2.59%, 2.15% |
| `Pedestrian` | num | 100% | 280 | 0.00 · p25 14.00 · p50 81.00 · p95 601 · max 954  █▃▂▂▁▁▁▁▁▁▁▁▁▁▁▁ |
| `Bicycles_N` | num | 100% | 121 | 0.00 · p25 3.00 · p50 11.00 · p95 131 · max 1,231  █▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁ |
| `Data_Colle` | text | 100% | 94 | e.g. 2018-Feb-07, 2018-Nov-21, 2018-Jan-25 |

## Candidate questions

- (none templated)

_profiled 2026-09-09 · `python3 tools/profile.py open_transportation_intersection_volumes_2018`_
