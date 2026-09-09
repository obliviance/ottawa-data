# Grit Box Locations

`open_grit_box_locations` · shape **arcgis-hub** · source `open-ottawa` · **spatial**

- origin: <https://open.ottawa.ca/datasets/ottawa::grit-box-locations>
- fetched 2026-09-09 · **81 rows** · 8 columns
- geojson · licence: https://ottawa.ca/en/city-hall/get-know-your-city/open-data#open-data-licence-ve

## Columns

| column | kind | non-null | distinct | summary |
| --- | --- | --- | --- | --- |
| `CREATED_DA` | date | 100% | 4 | 1970-01-01 → 2015-11-04, 1 gaps >30d |
| `FID` | num | 100% | 81 | 1.00 · p25 21.00 · p50 41.00 · p95 77.00 · max 81.00  █▆▆▆▆▆▆▆▆▆▆▆▆▆▆▆ |
| `ID` | num | 100% | 81 | 1.00 · p25 21.00 · p50 41.00 · p95 77.00 · max 81.00  █▆▆▆▆▆▆▆▆▆▆▆▆▆▆▆ |
| `LOCATION` | id/text | 100% | 81 | e.g. Laurier and Metcalfe (, Britannia at Carling, 905 Springland at Flan |
| `LOCATION_F` | id/text | 100% | 80 | e.g. Laurier et Metcalfe (B, Britannia à Carling
, 905, Springland à tunn |
| `geometry` | id/text | 100% | 81 | e.g. {"type": "Point", "coo, {"type": "Point", "coo, {"type": "Point", "coo |
| `longitude` | num | 100% | 81 | -75.93 · p25 -75.72 · p50 -75.69 · p95 -75.64 · max -75.40  ▁▁▁▁▂▁▂█▁▁▁▁▁▁▁▁ |
| `latitude` | num | 100% | 81 | 45.15 · p25 45.37 · p50 45.41 · p95 45.44 · max 45.52  ▁▁▁▁▁▁▁▁▂▅▄█▆▁▁▁ |

## Candidate questions

- (none templated)

_profiled 2026-09-09 · `python3 tools/profile.py open_grit_box_locations`_
