# COVID-19 Traffic Volume Monitoring at Intersections

`open_covid_19_traffic_volume_monitoring_at_intersections` · shape **arcgis-hub** · source `open-ottawa`

- origin: <https://open.ottawa.ca/datasets/ottawa::covid-19-traffic-volume-monitoring-at-intersections-1>
- fetched 2026-09-09 · **196 rows** · 12 columns
- csv · licence: https://ottawa.ca/en/city-hall/get-know-your-city/open-data#open-data-licence-ve

## Columns

| column | kind | non-null | distinct | summary |
| --- | --- | --- | --- | --- |
| `YEAR` | num | 100% | 3 | 2,020 · p25 2,020 · p50 2,021 · p95 2,022 · max 2,022  ▆▁▁▁▁▁▁█▁▁▁▁▁▁▁▄ |
| `MONTH` | cat | 100% | 13 | March 11%, April 11%, September 11%, June 10%, May 7%, July 7% |
| `AVERAGE` | cat | 100% | 2 | Y 64%, N 36% |
| `INTERSECTION` | cat | 100% | 7 | Eagleson at Hazeldean 14%, Innes at Tenth 14%, Airport Pkwy at Hunt Clu 14%, Prince of Wales at Hunt  14%, Laurier at Nicholas 14%, Riverside at Heron 14% |
| `AM` | text | 98% | 69 | e.g. 33%, 47%, 39% |
| `PM` | text | 98% | 59 | e.g. 42%, 58%, 53% |
| `F8HR` | text | 98% | 62 | e.g. 42%, 59%, 49% |
| `X` | num | 100% | 7 | 353,674 · p25 366,106 · p50 368,121 · p95 383,952 · max 383,952  ▃▁▁▁▁▁▃█▁▃▁▁▁▁▁▃ |
| `Y` | num | 100% | 7 | 5,015,395 · p25 5,018,424 · p50 5,023,703 · p95 5,036,160 · max 5,036,160  █▁█▁▁██▁█▁▁▁█▁▁█ |
| `LAT` | num | 100% | 7 | 45.28 · p25 45.30 · p50 45.35 · p95 45.46 · max 45.46  █▁█▁▁██▁█▁▁▁█▁▁█ |
| `LONG` | num | 100% | 7 | -75.88 · p25 -75.72 · p50 -75.69 · p95 -75.49 · max -75.49  ▃▁▁▁▁▁▃█▁▃▁▁▁▁▁▃ |
| `ObjectId` | num | 100% | 196 | 1.00 · p25 49.75 · p50 98.50 · p95 186 · max 196  █▇▇▇▇█▇▇▇▇█▇▇▇▇█ |

## Candidate questions

- (none templated)

_profiled 2026-09-09 · `python3 tools/profile.py open_covid_19_traffic_volume_monitoring_at_intersections`_
