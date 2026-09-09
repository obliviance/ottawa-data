# Transit Stations

`open_transit_stations` · shape **arcgis-hub** · source `open-ottawa` · **spatial**

- origin: <https://open.ottawa.ca/datasets/ottawa::transit-stations>
- fetched 2026-09-09 · **40 rows** · 8 columns
- geojson · licence: https://ottawa.ca/en/city-hall/get-know-your-city/open-data#open-data-licence-ve

## Columns

| column | kind | non-null | distinct | summary |
| --- | --- | --- | --- | --- |
| `OBJECTID` | num | 100% | 40 | 1.00 · p25 10.75 · p50 20.50 · p95 38.05 · max 40.00  █▅█▅█▅█▅▅█▅█▅█▅█ |
| `LON` | num | 100% | 40 | 353,219 · p25 365,522 · p50 367,999 · p95 373,232 · max 381,514  ▁▁▁▁▄▂▂▅██▃▁▁▁▁▁ |
| `LAT` | num | 100% | 40 | 5,017,877 · p25 5,025,658 · p50 5,030,435 · p95 5,031,948 · max 5,038,111  ▁▁▁▁▂▃▁▁▂▂█▂▁▁▁▁ |
| `ID` | id/text | 100% | 40 | e.g. __4KSBNC, __4KSBNE, __4KSBNG |
| `NAME` | id/text | 100% | 40 | e.g. Tunney's Pasture, Westboro, Lebreton |
| `geometry` | id/text | 100% | 40 | e.g. {"type": "Point", "coo, {"type": "Point", "coo, {"type": "Point", "coo |
| `longitude` | num | 100% | 40 | -75.88 · p25 -75.72 · p50 -75.69 · p95 -75.63 · max -75.52  ▁▁▁▁▄▂▂▅██▃▁▁▁▁▁ |
| `latitude` | num | 100% | 40 | 45.30 · p25 45.37 · p50 45.41 · p95 45.42 · max 45.48  ▁▁▁▁▂▃▁▂▂▃█▃▁▁▁▁ |

## Candidate questions

- (none templated)

_profiled 2026-09-09 · `python3 tools/profile.py open_transit_stations`_
