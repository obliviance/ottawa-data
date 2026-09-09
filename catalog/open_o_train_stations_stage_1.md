# O-Train Stations - Stage 1

`open_o_train_stations_stage_1` · shape **arcgis-hub** · source `open-ottawa` · **spatial**

- origin: <https://open.ottawa.ca/datasets/ottawa::o-train-stations-stage-1>
- fetched 2026-09-09 · **21 rows** · 9 columns
- geojson · licence: https://ottawa.ca/en/city-hall/get-know-your-city/open-data#open-data-licence-ve

## Columns

| column | kind | non-null | distinct | summary |
| --- | --- | --- | --- | --- |
| `OBJECTID` | num | 100% | 21 | 46.00 · p25 51.00 · p50 56.00 · p95 65.00 · max 66.00  █▄▄█▄▄▄█▄▄▄█▄▄▄█ |
| `GLOBALID` | cat | 100% | 21 | {AF0B66E2-2803-4B6A-96B2 5%, {6AE41118-B96C-40AE-B292 5%, {77C03E8B-7A11-4648-A6E6 5%, {33177F01-CED6-41D1-9A85 5%, {51DE06AC-A03D-4012-962C 5%, {8A403F47-3949-4F6A-A58E 5% |
| `REFNAME` | cat | 100% | 13 | Bayview 10%, Lees 10%, Rideau 10%, Tunney's Pasture 10%, uOttawa 10%, Lyon 10% |
| `LAYER` | cat | 100% | 1 | T-DRF-STATION PLATFORM 100% |
| `Shape_Length` | num | 100% | 21 | 266 · p25 272 · p50 285 · p95 530 · max 533  █▃▁▁▁▅▁▁▁▁▁▁▁▁▁▂ |
| `Shape_Area` | num | 100% | 21 | 609 · p25 998 · p50 1,156 · p95 1,837 · max 1,919  ▃▃▁▁█▁▆▁▁▄▁▁▁▁▂▃ |
| `CREATED_DATE` | date | 100% | 1 | 2018-09-04 → 2018-09-04 |
| `LAST_EDITED_DATE` | date | 100% | 1 | 2018-09-04 → 2018-09-04 |
| `geometry` | cat | 100% | 21 | {"type": "Polygon", "coo 5%, {"type": "Polygon", "coo 5%, {"type": "Polygon", "coo 5%, {"type": "Polygon", "coo 5%, {"type": "Polygon", "coo 5%, {"type": "Polygon", "coo 5% |

## Candidate questions

- (none templated)

_profiled 2026-09-09 · `python3 tools/profile.py open_o_train_stations_stage_1`_
