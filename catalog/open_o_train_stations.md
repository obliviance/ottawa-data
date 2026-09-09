# O-Train Stations

`open_o_train_stations` · shape **arcgis-hub** · source `open-ottawa` · **spatial**

- origin: <https://open.ottawa.ca/datasets/ottawa::o-train-stations>
- fetched 2026-09-09 · **5 rows** · 6 columns
- geojson · licence: https://ottawa.ca/en/city-hall/get-know-your-city/open-data#open-data-licence-ve

## Columns

| column | kind | non-null | distinct | summary |
| --- | --- | --- | --- | --- |
| `OBJECTID` | num | 100% | 5 | 1.00 · p25 2.00 · p50 3.00 · p95 4.80 · max 5.00  █▁▁█▁▁▁█▁▁▁█▁▁▁█ |
| `STATIONNAME` | cat | 100% | 5 | Greenboro 20%, Bayview 20%, Carling 20%, Carleton 20%, Mooney's Bay 20% |
| `GlobalID` | cat | 100% | 5 | {E52B06E8-05EA-480A-8C35 20%, {BACDEDEE-BD0F-48AC-A56B 20%, {DB1B6911-979E-412D-8903 20%, {6FB4B270-C742-449F-A398 20%, {BE4F8B83-FCD2-4016-B804 20% |
| `geometry` | cat | 100% | 5 | {"type": "Point", "coord 20%, {"type": "Point", "coord 20%, {"type": "Point", "coord 20%, {"type": "Point", "coord 20%, {"type": "Point", "coord 20% |
| `longitude` | num | 100% | 5 | -75.72 · p25 -75.71 · p50 -75.70 · p95 -75.66 · max -75.66  █▁▁█▁▁█▁▁█▁▁▁▁▁█ |
| `latitude` | num | 100% | 5 | 45.36 · p25 45.38 · p50 45.39 · p95 45.41 · max 45.41  █▁▁▁▁█▁▁█▁▁▁█▁▁█ |

## Candidate questions

- (none templated)

_profiled 2026-09-09 · `python3 tools/profile.py open_o_train_stations`_
