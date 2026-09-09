# 2019 Pedestrian Crossover Locations

`open_2019_pedestrian_crossover_locations` · shape **arcgis-hub** · source `open-ottawa` · **spatial**

- origin: <https://open.ottawa.ca/datasets/ottawa::2019-pedestrian-crossover-locations>
- fetched 2026-09-09 · **159 rows** · 9 columns
- geojson · licence: https://ottawa.ca/en/city-hall/get-know-your-city/open-data#open-data-licence-ve

## Columns

| column | kind | non-null | distinct | summary |
| --- | --- | --- | --- | --- |
| `OBJECTID_1` | num | 100% | 159 | 1.00 · p25 40.50 · p50 80.00 · p95 151 · max 159  ████████▇███████ |
| `INSTALLATION_YEAR` | num | 100% | 4 | 2,016 · p25 2,016 · p50 2,017 · p95 2,019 · max 2,019  █▁▁▁▁▄▁▁▁▁▆▁▁▁▁▃ |
| `LOCATION_X` | num | 100% | 159 | 329,172 · p25 362,579 · p50 368,468 · p95 385,554 · max 389,127  ▁▁▁▁▁▃▂▂▂▅█▂▂▁▃▂ |
| `LOCATION_Y` | num | 100% | 159 | 5,000,811 · p25 5,017,843 · p50 5,028,145 · p95 5,037,296 · max 5,039,598  ▁▁▁▁▂▅▆▃▂▄▃█▆▇▆▃ |
| `LAT` | num | 100% | 159 | 45.14 · p25 45.30 · p50 45.39 · p95 45.47 · max 45.49  ▁▁▁▁▁▅▆▂▃▄▂█▅▇▅▃ |
| `LONG` | num | 100% | 159 | -76.19 · p25 -75.76 · p50 -75.69 · p95 -75.47 · max -75.42  ▁▁▁▁▁▃▂▂▂▅█▂▂▁▃▂ |
| `geometry` | id/text | 100% | 159 | e.g. {"type": "Point", "coo, {"type": "Point", "coo, {"type": "Point", "coo |
| `longitude` | num | 100% | 159 | -76.19 · p25 -75.76 · p50 -75.69 · p95 -75.47 · max -75.42  ▁▁▁▁▁▃▂▂▂▅█▂▂▁▃▂ |
| `latitude` | num | 100% | 159 | 45.14 · p25 45.30 · p50 45.39 · p95 45.47 · max 45.49  ▁▁▁▁▁▅▆▂▃▄▂█▅▇▅▃ |

## Candidate questions

- (none templated)

_profiled 2026-09-09 · `python3 tools/profile.py open_2019_pedestrian_crossover_locations`_
