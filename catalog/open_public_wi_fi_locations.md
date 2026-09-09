# Public Wi-Fi Locations

`open_public_wi_fi_locations` · shape **arcgis-hub** · source `open-ottawa` · **spatial**

- origin: <https://open.ottawa.ca/datasets/ottawa::public-wi-fi-locations>
- fetched 2026-09-09 · **53 rows** · 13 columns
- geojson · licence: https://ottawa.ca/en/city-hall/get-know-your-city/open-data#open-data-licence-ve

## Columns

| column | kind | non-null | distinct | summary |
| --- | --- | --- | --- | --- |
| `X` | num | 100% | 52 | -76.04 · p25 -75.76 · p50 -75.68 · p95 -75.46 · max -75.40  ▂▁▂▁▁▄▄▅▅█▅▂▁▁▃▂ |
| `Y` | num | 100% | 52 | 45.15 · p25 45.35 · p50 45.37 · p95 45.46 · max 45.51  ▁▁▁▁▂▁▁▂██▃▆▆▃▁▁ |
| `Name` | id/text | 100% | 50 | e.g. Albion-Heatherington R, Alexander Community Ce, Banff Ledbury Pavillio |
| `Phase` | cat | 100% | 3 | Phase 1 55%, Phase 2 25%, Phase 3 21% |
| `Status` | cat | 100% | 2 | Completed 81%, Fall 2023 19% |
| `Address` | id/text | 100% | 53 | e.g. 1560 Heatherington Rd, 960 Silver St, 2084 Banff Ave |
| `City` | cat | 100% | 1 | Ottawa 100% |
| `Province` | cat | 100% | 1 | Ontario 100% |
| `ObjectId` | text | 0% | 0 | e.g.  |
| `ObjectId2` | num | 100% | 53 | 1.00 · p25 14.00 · p50 27.00 · p95 50.40 · max 53.00  █▆▆█▆▆▆█▆▆▆█▆▆▆█ |
| `geometry` | id/text | 100% | 52 | e.g. {"type": "Point", "coo, {"type": "Point", "coo, {"type": "Point", "coo |
| `longitude` | num | 100% | 52 | -76.04 · p25 -75.76 · p50 -75.68 · p95 -75.46 · max -75.40  ▂▁▂▁▁▄▄▅▅█▅▂▁▁▃▂ |
| `latitude` | num | 100% | 52 | 45.15 · p25 45.35 · p50 45.37 · p95 45.46 · max 45.51  ▁▁▁▁▂▁▁▂██▃▆▆▃▁▁ |

## Candidate questions

- (none templated)

_profiled 2026-09-09 · `python3 tools/profile.py open_public_wi_fi_locations`_
