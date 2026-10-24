# RVCA — 100-year floodline

`rvca_100yr_floodline` · shape **arcgis-hub** · source `conservation-authorities` · **spatial**

- origin: <https://gis.rvca.ca/arcgis/rest/services/RVCA_Hazards_publicService/MapServer/5>
- fetched 2026-10-24 · **657 rows** · 12 columns
- paged by OBJECTID via arcgis_layers.py; 657 rows

## Columns

| column | kind | non-null | distinct | summary |
| --- | --- | --- | --- | --- |
| `OBJECTID` | num | 100% | 657 | 7,749 · p25 7,921 · p50 8,087 · p95 11,222 · max 16,365  █▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁ |
| `Group_` | cat | 0% | 1 |  100% |
| `CON_AUTH` | cat | 100% | 1 | RVCA 100% |
| `TYPE` | cat | 100% | 3 | FLOODPLAIN 99%, SHALLOW FLOODING 1%, REDUCED FLOOD RISK 0% |
| `AREA_M_SQ` | num | 100% | 654 | 0.00 · p25 291 · p50 3,036 · p95 1,246,998 · max 20,207,684  █▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁ |
| `created_user` | cat | 100% | 1 | GIS_ADMIN 100% |
| `created_date` | date | 100% | 15 | 1970-01-01 → 1970-01-01 |
| `last_edited_user` | cat | 100% | 1 | GIS_ADMIN 100% |
| `last_edited_date` | date | 100% | 12 | 1970-01-01 → 1970-01-01 |
| `Shape.STArea()` | num | 100% | 657 | 0.00 · p25 292 · p50 3,092 · p95 1,246,998 · max 20,207,684  █▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁ |
| `Shape.STLength()` | num | 100% | 657 | 0.55 · p25 116 · p50 443 · p95 14,916 · max 157,690  █▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁ |
| `geometry` | id/text | 100% | 657 | e.g. {"type": "Polygon", "c, {"type": "Polygon", "c, {"type": "Polygon", "c |

## Candidate questions

- Trend / seasonality of rvca_100yr_floodline over `created_user`; structural breaks?
- Spatial clustering of rvca_100yr_floodline; overlay wards + the decision timeline

_profiled 2026-10-24 · `python3 tools/profile.py rvca_100yr_floodline`_
