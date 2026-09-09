# Transportation Intersection Volumes 2017

`open_transportation_intersection_volumes_2017` · shape **arcgis-hub** · source `open-ottawa`

- origin: <https://open.ottawa.ca/datasets/ottawa::transportation-intersection-volumes-2017>
- fetched 2026-09-09 · **584 rows** · 8 columns
- csv · licence: https://ottawa.ca/en/city-hall/get-know-your-city/open-data#open-data-licence-ve

## Columns

| column | kind | non-null | distinct | summary |
| --- | --- | --- | --- | --- |
| `FID` | num | 100% | 584 | 1.00 · p25 147 · p50 292 · p95 555 · max 584  █▇█▇█▇█▇▇█▇█▇█▇█ |
| `OBJECTID` | num | 100% | 584 | 1.00 · p25 147 · p50 292 · p95 555 · max 584  █▇█▇█▇█▇▇█▇█▇█▇█ |
| `Intersecti` | id/text | 100% | 538 | e.g. 240 S OF CHARLEMAGNE B, 2ND LINE RD @ OSGOODE , 8TH LINE RD @ PARKWAY  |
| `All_Motori` | num | 100% | 577 | 117 · p25 7,402 · p50 14,680 · p95 41,267 · max 65,632  ▇▄▆█▅▄▃▂▂▂▁▁▁▁▁▁ |
| `F__Truck` | text | 100% | 378 | e.g. 2.35%, 4.88%, 4.68% |
| `Pedestrian` | num | 100% | 389 | 0.00 · p25 46.00 · p50 170 · p95 5,316 · max 18,113  █▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁ |
| `Bicycles_N` | num | 100% | 173 | 0.00 · p25 4.00 · p50 14.50 · p95 438 · max 1,041  █▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁ |
| `Data_Colle` | text | 100% | 91 | e.g. 2017-Apr-19, 2017-Jan-17, 2017-Oct-11 |

## Candidate questions

- (none templated)

_profiled 2026-09-09 · `python3 tools/profile.py open_transportation_intersection_volumes_2017`_
