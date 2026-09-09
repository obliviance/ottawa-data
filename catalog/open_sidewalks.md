# Sidewalks

`open_sidewalks` · shape **arcgis-hub** · source `open-ottawa`

- origin: <https://open.ottawa.ca/datasets/ottawa::sidewalks>
- fetched 2026-09-09 · **100,975 rows** · 4 columns
- csv · licence: https://ottawa.ca/en/city-hall/get-know-your-city/open-data#open-data-licence-ve

## Columns

| column | kind | non-null | distinct | summary |
| --- | --- | --- | --- | --- |
| `OBJECTID` | num | 100% | 100,975 | 55,422 · p25 204,492 · p50 229,792 · p95 275,346 · max 280,406  ▁▁▁▁▁▁▁▁▁▇▇▇▇█▇▇ |
| `SHAPE_Length` | num | 100% | 100,969 | 0.00 · p25 16.27 · p50 31.13 · p95 696 · max 27,206  █▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁ |
| `SHAPE_Area` | num | 100% | 100,969 | 0.00 · p25 9.19 · p50 23.49 · p95 1,005 · max 109,756  █▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁ |
| `GLOBALID` | id/text | 100% | 100,975 | e.g. {CDAD2516-4DD0-461B-8D, {DA1DA381-0BAB-45B7-A3, {9159AB60-514E-4D22-8A |

## Candidate questions

- (none templated)

_profiled 2026-09-09 · `python3 tools/profile.py open_sidewalks`_
