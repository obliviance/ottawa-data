# Transportation Intersection Volume 2025

`open_transportation_intersection_volume_2025` · shape **arcgis-hub** · source `open-ottawa`

- origin: <https://open.ottawa.ca/datasets/ottawa::transportation-intersection-volume-2025>
- fetched 2026-09-09 · **655 rows** · 17 columns
- csv · licence: https://ottawa.ca/en/city-hall/get-know-your-city/open-data#open-data-licence-ve

## Columns

| column | kind | non-null | distinct | summary |
| --- | --- | --- | --- | --- |
| `X` | num | 97% | 533 | 555,397 · p25 597,043 · p50 602,150 · p95 621,115 · max 632,411  ▁▁▁▁▁▁▃▁▂█▄▂▂▁▁▁ |
| `Y` | num | 97% | 533 | 4,992,937 · p25 5,023,516 · p50 5,033,371 · p95 5,043,223 · max 5,050,980  ▁▁▁▁▁▁▂▄▃▂▄▄█▃▂▁ |
| `OBJECTID` | num | 100% | 655 | 1.00 · p25 164 · p50 328 · p95 622 · max 655  ████████▇███████ |
| `Geo_ID` | num | 97% | 533 | 52.00 · p25 3,331 · p50 7,176 · p95 18,084 · max 21,335  ▄█▄▅▃▆▅▄▅▄▂▁▁▁▂▁ |
| `X_Coord` | num | 97% | 533 | 320,665 · p25 361,797 · p50 367,116 · p95 385,553 · max 397,878  ▁▁▁▁▁▁▃▁▃█▄▂▂▁▁▁ |
| `Y_Coord` | num | 97% | 533 | 4,986,660 · p25 5,017,545 · p50 5,026,968 · p95 5,036,323 · max 5,043,414  ▁▁▁▁▁▁▁▄▃▂▄▄█▃▂▁ |
| `Intersection` | id/text | 97% | 533 | e.g. HAZELDEAN RD @ JOHNWOO, ABBOTT ST @ CRANESBILL, ABBOTT ST @ TRIANGLE S |
| `Study_Date` | date | 97% | 135 | 2025-01-07 → 2025-12-10 |
| `Day_Of_Week` | cat | 97% | 7 | Wednesday 35%, Thursday 29%, Tuesday 28%, Saturday 5%, Sunday 2%, Friday 1% |
| `Duration` | num | 97% | 7 | 3.00 · p25 8.00 · p50 8.00 · p95 16.00 · max 24.00  ▁▁▁█▁▁▁▁▁▁▁▁▁▁▁▁ |
| `Total_Vehicles` | num | 97% | 624 | 21.00 · p25 1,653 · p50 6,355 · p95 26,112 · max 42,231  █▄▄▃▂▂▂▁▁▁▁▁▁▁▁▁ |
| `Total_Pedestrians` | num | 97% | 348 | 0.00 · p25 15.00 · p50 102 · p95 2,476 · max 12,655  █▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁ |
| `Total_Cyclists` | num | 97% | 204 | 0.00 · p25 5.00 · p50 25.00 · p95 357 · max 1,534  █▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁ |
| `Total_Trucks` | num | 97% | 403 | 0.00 · p25 62.00 · p50 175 · p95 964 · max 2,683  █▄▂▁▁▁▁▁▁▁▁▁▁▁▁▁ |
| `Total_Truck__` | num | 97% | 636 | 0.00 · p25 0.02 · p50 0.03 · p95 0.10 · max 0.46  ▇█▃▁▁▁▁▁▁▁▁▁▁▁▁▁ |
| `AADT_Calculated` | num | 97% | 2 | 0.00 · p25 1.00 · p50 1.00 · p95 1.00 · max 1.00  ▂▁▁▁▁▁▁▁▁▁▁▁▁▁▁█ |
| `Total_Adjusted_Volume__24h_` | num | 97% | 528 | 0.00 · p25 689 · p50 6,219 · p95 37,179 · max 76,899  █▂▃▂▁▁▁▁▁▁▁▁▁▁▁▁ |

## Candidate questions

- Trend / seasonality of open_transportation_intersection_volume_2025 over `Study_Date`; structural breaks?

_profiled 2026-09-09 · `python3 tools/profile.py open_transportation_intersection_volume_2025`_
