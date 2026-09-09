# Transportation Intersection Volumes 2015

`open_transportation_intersection_volumes_2015` · shape **arcgis-hub** · source `open-ottawa`

- origin: <https://open.ottawa.ca/datasets/ottawa::transportation-intersection-volumes-2015>
- fetched 2026-09-09 · **519 rows** · 10 columns
- csv · licence: https://ottawa.ca/en/city-hall/get-know-your-city/open-data#open-data-licence-ve

## Columns

| column | kind | non-null | distinct | summary |
| --- | --- | --- | --- | --- |
| `X` | num | 100% | 487 | -8,490,138 · p25 -8,433,170 · p50 -8,425,657 · p95 -8,402,438 · max -8,383,446  ▁▁▁▁▁▃▁▂▄█▅▂▃▂▁▁ |
| `Y` | num | 100% | 487 | 5,627,401 · p25 5,672,389 · p50 5,680,600 · p95 5,696,409 · max 5,704,508  ▁▁▁▁▁▁▁▅▃▄▇▇█▄▃▁ |
| `FID` | num | 100% | 519 | 1.00 · p25 130 · p50 260 · p95 493 · max 519  █▇█▇▇█▇█▇▇█▇▇█▇█ |
| `OBJECTID` | num | 100% | 519 | 1.00 · p25 130 · p50 260 · p95 493 · max 519  █▇█▇▇█▇█▇▇█▇▇█▇█ |
| `Intersecti` | id/text | 100% | 487 | e.g. ABBOTT ST W @ WEST RID, ACCEPTANCE PL @ HOPE S, ACTON ST/AVALON PL @ S |
| `All_Motori` | num | 100% | 511 | 98.00 · p25 5,444 · p50 13,818 · p95 47,874 · max 80,624  █▄▅▃▃▃▃▂▁▁▁▁▁▁▁▁ |
| `F__Trucks` | text | 100% | 359 | e.g. 1.72%, 5.48%, 1.62% |
| `Pedestrian` | num | 100% | 306 | 0.00 · p25 21.00 · p50 91.00 · p95 1,498 · max 10,107  █▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁ |
| `Bicycles_N` | num | 100% | 157 | 0.00 · p25 3.00 · p50 13.00 · p95 339 · max 933  █▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁ |
| `Data_Colle` | text | 100% | 99 | e.g. 15-Jul-15, 13-Aug-15, 14-May-15 |

## Candidate questions

- (none templated)

_profiled 2026-09-09 · `python3 tools/profile.py open_transportation_intersection_volumes_2015`_
