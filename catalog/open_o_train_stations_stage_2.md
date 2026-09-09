# O-Train Stations - Stage 2

`open_o_train_stations_stage_2` · shape **arcgis-hub** · source `open-ottawa` · **spatial**

- origin: <https://open.ottawa.ca/datasets/ottawa::o-train-stations-stage-2>
- fetched 2026-09-09 · **47 rows** · 9 columns
- geojson · licence: https://ottawa.ca/en/city-hall/get-know-your-city/open-data#open-data-licence-ve

## Columns

| column | kind | non-null | distinct | summary |
| --- | --- | --- | --- | --- |
| `OBJECTID` | num | 100% | 47 | 2,643 · p25 2,654 · p50 2,963 · p95 2,986 · max 2,988  █▁▁▁▁▁▁▁▁▁▁▁▁▁▂▇ |
| `LAYER` | cat | 100% | 3 | STATION PLATFORM 49%, T-DRF-STATION PLATFORM 43%, T-DRF-STATION PLATFORM2 9% |
| `GLOBALID` | id/text | 100% | 47 | e.g. {6D481AA8-B870-48D8-88, {18F45CD1-1248-433B-96, {B4398D4B-8342-4FCF-8F |
| `REFNAME` | text | 100% | 29 | e.g. QUEENSVIEW, WESTBORO, KÌCHÌ SÌBÌ |
| `Shape_Length` | num | 100% | 47 | 114 · p25 184 · p50 243 · p95 316 · max 365  ▅▄▁▁▁▁▁█▁▃▇▂▄▁▁▂ |
| `Shape_Area` | num | 100% | 47 | 357 · p25 516 · p50 811 · p95 2,033 · max 2,262  ▇▁▁█▁▂▁▄▁▁▁▁▂▂▂▁ |
| `CREATED_DATE` | date | 100% | 2 | 2020-05-21 → 2021-01-22, 1 gaps >30d |
| `LAST_EDITED_DATE` | date | 100% | 47 | 2020-05-21 → 2021-11-02, 2 gaps >30d |
| `geometry` | id/text | 100% | 47 | e.g. {"type": "Polygon", "c, {"type": "Polygon", "c, {"type": "Polygon", "c |

## Candidate questions

- (none templated)

_profiled 2026-09-09 · `python3 tools/profile.py open_o_train_stations_stage_2`_
