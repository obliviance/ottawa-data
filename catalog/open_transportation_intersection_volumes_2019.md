# Transportation Intersection Volumes 2019

`open_transportation_intersection_volumes_2019` · shape **arcgis-hub** · source `open-ottawa`

- origin: <https://open.ottawa.ca/datasets/ottawa::transportation-intersection-volumes-2019>
- fetched 2026-09-09 · **910 rows** · 11 columns
- csv · licence: https://ottawa.ca/en/city-hall/get-know-your-city/open-data#open-data-licence-ve

## Columns

| column | kind | non-null | distinct | summary |
| --- | --- | --- | --- | --- |
| `Intersection` | id/text | 100% | 869 | e.g. LAFONTAINE AVE @ MCART, LAPERRIERE AVE @ LARKI, LARMOURS RD @ SARSFIEL |
| `All_Motorized_Vehicles_AADT_24Hour_Volume` | num | 100% | 892 | 30.00 · p25 3,241 · p50 8,781 · p95 38,827 · max 77,595  █▄▃▂▂▂▁▁▁▁▁▁▁▁▁▁ |
| `Percent_Trucks` | num | 100% | 565 | 0.00 · p25 0.03 · p50 0.04 · p95 0.11 · max 0.28  ▂█▇▃▂▁▁▁▁▁▁▁▁▁▁▁ |
| `Pedestrians_Not_Factored` | num | 100% | 422 | 0.00 · p25 6.00 · p50 86.50 · p95 3,184 · max 25,500  █▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁ |
| `Bicycles_Not_Factored` | num | 100% | 186 | 0.00 · p25 1.00 · p50 8.00 · p95 245 · max 2,837  █▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁ |
| `Date_Collected` | date | 100% | 109 | 1970-01-01 → 1970-01-01 |
| `X` | num | 100% | 866 | 317,873 · p25 363,367 · p50 368,273 · p95 387,740 · max 401,822  ▁▁▁▁▁▁▁▂▄█▅▂▂▁▁▁ |
| `Y` | num | 100% | 862 | 4,982,833 · p25 5,020,025 · p50 5,027,170 · p95 5,037,563 · max 5,043,414  ▁▁▁▁▁▁▁▂▃▂▄▅█▅▂▁ |
| `LAT` | num | 100% | 868 | 44.98 · p25 45.32 · p50 45.38 · p95 45.47 · max 45.52  ▁▁▁▁▁▁▂▂▃▂▄▅█▅▂▁ |
| `LONG` | num | 100% | 868 | -76.33 · p25 -75.75 · p50 -75.69 · p95 -75.44 · max -75.26  ▁▁▁▁▁▁▁▂▄█▅▂▂▁▁▁ |
| `FID` | num | 100% | 910 | 1.00 · p25 228 · p50 456 · p95 865 · max 910  █████▇████▇█████ |

## Candidate questions

- Trend / seasonality of open_transportation_intersection_volumes_2019 over `Date_Collected`; structural breaks?

_profiled 2026-09-09 · `python3 tools/profile.py open_transportation_intersection_volumes_2019`_
