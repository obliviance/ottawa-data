# Pathways

`open_pathways` · shape **arcgis-hub** · source `open-ottawa` · **spatial**

- origin: <https://open.ottawa.ca/datasets/ottawa::pathways>
- fetched 2026-09-09 · **295 rows** · 5 columns
- geojson · licence: https://ottawa.ca/en/city-hall/get-know-your-city/open-data#open-data-licence-ve

## Columns

| column | kind | non-null | distinct | summary |
| --- | --- | --- | --- | --- |
| `OBJECTID` | num | 100% | 295 | 1.00 · p25 74.50 · p50 148 · p95 280 · max 295  █▇█▇▇█▇█▇▇█▇▇█▇█ |
| `Shape_Length` | num | 100% | 295 | 11.46 · p25 148 · p50 435 · p95 3,016 · max 23,978  █▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁ |
| `Shape_Area` | num | 100% | 295 | 6.25 · p25 205 · p50 613 · p95 6,749 · max 125,590  █▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁ |
| `GlobalID` | id/text | 100% | 295 | e.g. {C4E5A130-3AE6-4B0B-BA, {80AB4310-7D5F-44E2-AE, {CB9D491F-4202-49EF-9E |
| `geometry` | id/text | 100% | 295 | e.g. {"type": "Polygon", "c, {"type": "Polygon", "c, {"type": "Polygon", "c |

## Candidate questions

- Spatial clustering of open_pathways; overlay wards + the decision timeline

_profiled 2026-09-09 · `python3 tools/profile.py open_pathways`_
