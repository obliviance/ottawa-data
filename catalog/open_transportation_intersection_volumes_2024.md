# Transportation Intersection Volumes 2024

`open_transportation_intersection_volumes_2024` · shape **arcgis-hub**

- origin: <https://open.ottawa.ca/datasets/ottawa::transportation-intersection-volumes-2024>
- fetched 2026-09-09 · **703 rows** · 14 columns
- csv · licence: https://ottawa.ca/en/city-hall/open-transparent-and-accountable-government/open-

## Columns

| column | kind | non-null | distinct | summary |
| --- | --- | --- | --- | --- |
| `FID` | num | 100% | 703 | 0.00 · p25 176 · p50 351 · p95 667 · max 702  ████████▇███████ |
| `Shape__` | cat | 100% | 1 | Point 100% |
| `Intersection` | id/text | 100% | 646 | e.g. BASELINE RD @ CENTREPO, FISHER AVE @ NORMANDY , COBOURG ST @ ST. PATRI |
| `All_Motori` | num | 100% | 694 | 58.00 · p25 5,334 · p50 12,900 · p95 37,893 · max 69,772  █▄▅▄▃▂▃▂▂▁▁▁▁▁▁▁ |
| `Truck_Perc` | num | 100% | 648 | 0.38 · p25 2.37 · p50 3.21 · p95 9.58 · max 46.94  █▅▂▁▁▁▁▁▁▁▁▁▁▁▁▁ |
| `Pedestrian` | num | 100% | 394 | 0.00 · p25 22.00 · p50 134 · p95 2,356 · max 11,914  █▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁ |
| `Bicycles_N` | num | 100% | 184 | 0.00 · p25 6.00 · p50 25.00 · p95 249 · max 690  █▃▁▁▁▁▁▁▁▁▁▁▁▁▁▁ |
| `Study_Date` | date | 100% | 111 | 2024-01-09 → 2024-12-19 |
| `X` | num | 100% | 643 | 319,826 · p25 360,373 · p50 367,566 · p95 384,898 · max 396,290  ▁▁▁▁▁▁▄▂▄▇█▄▂▃▁▁ |
| `y` | num | 100% | 640 | 4,992,721 · p25 5,019,997 · p50 5,026,415 · p95 5,037,797 · max 5,043,453  ▁▁▁▁▁▁▃▃▄▅▅█▆▂▃▁ |
| `Lat` | num | 100% | 635 | 45.07 · p25 45.32 · p50 45.37 · p95 45.48 · max 45.53  ▁▁▁▁▁▁▃▄▄▅▆█▇▃▃▁ |
| `Long` | num | 100% | 641 | -76.31 · p25 -75.79 · p50 -75.70 · p95 -75.48 · max -75.33  ▁▁▁▁▁▁▃▂▄▆█▄▂▃▁▁ |
| `Geo_ID` | num | 100% | 646 | 21.00 · p25 3,140 · p50 6,984 · p95 13,567 · max 19,560  ▄█▇▅▄▇▆▅▄▆▅▁▁▁▁▁ |
| `FID2` | num | 100% | 703 | 1.00 · p25 176 · p50 352 · p95 668 · max 703  ████████▇███████ |

## Candidate questions

- Trend / seasonality of open_transportation_intersection_volumes_2024 over `Study_Date`; structural breaks?

_profiled 2026-09-09 · `python3 tools/profile.py open_transportation_intersection_volumes_2024`_
