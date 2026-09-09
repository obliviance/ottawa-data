# Transportation Intersection Volumes 2016

`open_transportation_intersection_volumes_2016` · shape **arcgis-hub** · source `open-ottawa`

- origin: <https://open.ottawa.ca/datasets/ottawa::transportation-intersection-volumes-2016>
- fetched 2026-09-09 · **687 rows** · 8 columns
- csv · licence: https://ottawa.ca/en/city-hall/get-know-your-city/open-data#open-data-licence-ve

## Columns

| column | kind | non-null | distinct | summary |
| --- | --- | --- | --- | --- |
| `FID` | num | 100% | 687 | 1.00 · p25 172 · p50 344 · p95 653 · max 687  ████████▇███████ |
| `OBJECTID` | num | 100% | 687 | 1.00 · p25 172 · p50 344 · p95 653 · max 687  ████████▇███████ |
| `Intersecti` | id/text | 100% | 652 | e.g. 105 S OF COMMISSIONER , 130 W OF PRESTON ST @ , 225 E OF ORLEANS BLVD/ |
| `All_Motori` | num | 100% | 679 | 306 · p25 9,556 · p50 16,196 · p95 44,725 · max 66,685  ▆▄▇█▄▄▃▃▃▂▂▁▁▁▁▁ |
| `F__Truck` | text | 100% | 394 | e.g. 19.05%, 3.35%, 3.32% |
| `Pedestrian` | num | 100% | 442 | 0.00 · p25 51.00 · p50 169 · p95 2,473 · max 9,287  █▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁ |
| `Cyclist_No` | num | 100% | 223 | 0.00 · p25 5.00 · p50 21.00 · p95 424 · max 2,645  █▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁ |
| `Data_Colle` | text | 100% | 88 | e.g. 2016-Jul-13, 2016-Mar-09, 2016-Jan-29 |

## Candidate questions

- (none templated)

_profiled 2026-09-09 · `python3 tools/profile.py open_transportation_intersection_volumes_2016`_
