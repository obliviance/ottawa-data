# RVCA — Regulation Limit (O.Reg 174/06 hazard extent)

`rvca_regulation_limit` · shape **arcgis-hub** · source `conservation-authorities` · **spatial**

- origin: <https://gis.rvca.ca/arcgis/rest/services/RVCA_Hazards_publicService/MapServer/6>
- fetched 2026-10-24 · **503 rows** · 10 columns
- paged by OBJECTID via arcgis_layers.py; 503 rows

## Columns

| column | kind | non-null | distinct | summary |
| --- | --- | --- | --- | --- |
| `OBJECTID_1` | num | 100% | 379 | 13,597 · p25 13,672 · p50 13,822 · p95 14,077 · max 18,902  █▄▁▁▁▁▁▁▁▁▁▁▁▁▁▁ |
| `OBJECTID` | text | 0% | 0 | e.g.  |
| `SHAPE_Leng` | num | 99% | 1 | 0.00 · p25 0.00 · p50 0.00 · p95 0.00 · max 0.00   |
| `created_user` | cat | 100% | 1 | GIS_ADMIN 100% |
| `created_date` | date | 100% | 7 | 1970-01-01 → 1970-01-01 |
| `last_edited_user` | cat | 100% | 1 | GIS_ADMIN 100% |
| `last_edited_date` | date | 100% | 11 | 1970-01-01 → 1970-01-01 |
| `Shape.area` | num | 100% | 379 | 8,193 · p25 52,534 · p50 104,598 · p95 4,363,201 · max 145,070,991  █▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁ |
| `Shape.len` | num | 100% | 379 | 385 · p25 1,048 · p50 1,651 · p95 26,167 · max 661,811  █▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁ |
| `geometry` | text | 100% | 379 | e.g. {"type": "Polygon", "c, {"type": "Polygon", "c, {"type": "Polygon", "c |

## Candidate questions

- Trend / seasonality of rvca_regulation_limit over `created_user`; structural breaks?
- Spatial clustering of rvca_regulation_limit; overlay wards + the decision timeline

_profiled 2026-10-24 · `python3 tools/profile.py rvca_regulation_limit`_
