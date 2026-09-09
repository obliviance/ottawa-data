# Bike Repair

`open_bike_repair` · shape **arcgis-hub** · source `open-ottawa`

- origin: <https://open.ottawa.ca/datasets/ottawa::bike-repair>
- fetched 2026-09-09 · **51 rows** · 14 columns
- csv · licence: https://ottawa.ca/en/city-hall/get-know-your-city/open-data#open-data-licence-ve

## Columns

| column | kind | non-null | distinct | summary |
| --- | --- | --- | --- | --- |
| `X` | num | 100% | 28 | -8,451,377 · p25 -8,430,904 · p50 -8,421,876 · p95 -8,410,474 · max -8,387,924  ▂▁▁▁▂▁▂█▂▁▁▁▁▁▁▁ |
| `Y` | num | 100% | 29 | 5,644,206 · p25 5,676,791 · p50 5,680,435 · p95 5,691,820 · max 5,696,176  ▁▁▁▁▁▁▁▁▁▂▁█▁▂▂▁ |
| `Long` | num | 100% | 28 | -75.92 · p25 -75.74 · p50 -75.66 · p95 -75.55 · max -75.35  ▂▁▁▁▂▁▂█▂▁▁▁▁▁▁▁ |
| `Lat` | num | 100% | 29 | 45.14 · p25 45.35 · p50 45.37 · p95 45.44 · max 45.47  ▁▁▁▁▁▁▁▁▁▂▁█▁▂▂▁ |
| `LOCATION_EN` | id/text | 100% | 50 | e.g. Bronson and Slater, Harold H. Dent Rest Ar, Kichi Zibi Station (Do |
| `LOCATION_FR` | id/text | 100% | 50 | e.g. Bronson et Slater, Aire de repos Harold H, Station Kichi Zibi (ga |
| `BUILDING_ADDRESS` | id/text | 100% | 51 | e.g. 482 Slater Ave, Presscott-Russell Tr &, 333 Dominion Avenue  |
| `PICTURES` | id/text | 90% | 46 | e.g. https://live.staticfli, https://live.staticfli, https://live.staticfli |
| `INSTALL_YR` | num | 98% | 10 | 2,015 · p25 2,017 · p50 2,017 · p95 2,023 · max 2,024  ▁▄▁█▁▄▁▁▁▁▁▁▃▁▁▁ |
| `DESCRIPTION_EN` | id/text | 100% | 45 | e.g. Transit station, Near front entrance, At the Kichi Zibi LRT  |
| `DESCRIPTION_FR` | id/text | 100% | 43 | e.g. Station de transport e, Près de l’entrée princ, À la station de transp |
| `ADDRESS_FR` | id/text | 98% | 50 | e.g. 482, av Slater, 333, av Dominion, 103, prom Benlea |
| `STATION_ID` | num | 92% | 47 | 1.00 · p25 12.50 · p50 26.00 · p95 46.70 · max 49.00  █▆▆▆▄▆▄▆▆▆▆▆▆▆▆▆ |
| `ObjectId` | num | 100% | 51 | 1.00 · p25 13.50 · p50 26.00 · p95 48.50 · max 51.00  █▆▆▆▆▆▆█▆▆▆▆▆▆▆█ |

## Candidate questions

- (none templated)

_profiled 2026-09-09 · `python3 tools/profile.py open_bike_repair`_
