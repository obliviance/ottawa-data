# Rail Stations

`open_rail_stations` · shape **arcgis-hub** · source `open-ottawa` · **spatial**

- origin: <https://open.ottawa.ca/datasets/ottawa::rail-stations>
- fetched 2026-09-09 · **2 rows** · 9 columns
- geojson · licence: https://ottawa.ca/en/city-hall/get-know-your-city/open-data#open-data-licence-ve

## Columns

| column | kind | non-null | distinct | summary |
| --- | --- | --- | --- | --- |
| `OBJECTID` | num | 100% | 2 | 1.00 · p25 1.25 · p50 1.50 · p95 1.95 · max 2.00  █▁▁▁▁▁▁▁▁▁▁▁▁▁▁█ |
| `NAME` | cat | 100% | 2 | Fallowfield VIA Rail Tra 50%, Tremblay VIA Rail Train  50% |
| `GIS_UNIQUE_ID` | text | 0% | 0 | e.g.  |
| `GLOBALID` | cat | 100% | 2 | {DA912185-C4C2-455F-AD17 50%, {5DE4DAAF-6755-46F3-80CD 50% |
| `CREATED_DATE` | date | 50% | 1 | 2017-04-04 → 2017-04-04 |
| `LAST_EDITED_DATE` | date | 50% | 1 | 2017-04-04 → 2017-04-04 |
| `Shape_Length` | num | 100% | 2 | 715 · p25 1,432 · p50 2,148 · p95 3,438 · max 3,582  █▁▁▁▁▁▁▁▁▁▁▁▁▁▁█ |
| `Shape_Area` | num | 100% | 2 | 2,492 · p25 23,724 · p50 44,957 · p95 83,175 · max 87,421  █▁▁▁▁▁▁▁▁▁▁▁▁▁▁█ |
| `geometry` | cat | 100% | 2 | {"type": "Polygon", "coo 50%, {"type": "Polygon", "coo 50% |

## Candidate questions

- (none templated)

_profiled 2026-09-09 · `python3 tools/profile.py open_rail_stations`_
