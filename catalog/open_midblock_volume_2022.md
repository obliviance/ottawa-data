# Midblock Volume 2022

`open_midblock_volume_2022` · shape **arcgis-hub** · source `open-ottawa`

- origin: <https://open.ottawa.ca/datasets/ottawa::midblock-volume-2022>
- fetched 2026-09-09 · **618 rows** · 9 columns
- csv · licence: https://ottawa.ca/en/city-hall/get-know-your-city/open-data#open-data-licence-ve

## Columns

| column | kind | non-null | distinct | summary |
| --- | --- | --- | --- | --- |
| `Geo_ID` | id/text | 100% | 618 | e.g. __3ZA3M5, __3ZA1D8, __3ZA5N6 |
| `Midblock` | id/text | 100% | 618 | e.g. TRIM RD btwn HENN DR &, TRIM RD btwn NAVAN RD , EDEN AVE btwn LINCOLN  |
| `Year` | num | 100% | 1 | 2,022 · p25 2,022 · p50 2,022 · p95 2,022 · max 2,022   |
| `All_Motorized_Vehicles_AADT_24_` | num | 100% | 548 | 38.00 · p25 407 · p50 967 · p95 11,898 · max 33,083  █▂▁▁▁▁▁▁▁▁▁▁▁▁▁▁ |
| `X` | num | 98% | 606 | 318,889 · p25 363,505 · p50 368,551 · p95 385,962 · max 401,542  ▁▁▁▁▁▁▂▁▅█▄▂▃▁▁▁ |
| `Y` | num | 98% | 606 | 4,999,163 · p25 5,023,393 · p50 5,028,284 · p95 5,037,533 · max 5,043,264  ▁▁▁▁▂▃▂▂▄▇█▅▆▅▂▁ |
| `Lat` | num | 98% | 605 | 45.13 · p25 45.35 · p50 45.39 · p95 45.47 · max 45.52  ▁▁▁▁▁▃▂▂▄▇█▆▆▅▂▁ |
| `Long` | num | 98% | 605 | -76.32 · p25 -75.75 · p50 -75.69 · p95 -75.46 · max -75.27  ▁▁▁▁▁▁▂▁▅█▄▂▃▂▁▁ |
| `ObjectId` | num | 100% | 618 | 1.00 · p25 155 · p50 310 · p95 587 · max 618  ██▇█▇█▇██▇█▇█▇██ |

## Candidate questions

- Trend / seasonality of open_midblock_volume_2022 over `Year`; structural breaks?

_profiled 2026-09-09 · `python3 tools/profile.py open_midblock_volume_2022`_
