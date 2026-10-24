# RVCA — Regulated Wetlands

`rvca_regulated_wetlands` · shape **arcgis-hub** · source `conservation-authorities` · **spatial**

- origin: <https://gis.rvca.ca/arcgis/rest/services/RVCA_Hazards_publicService/MapServer/7>
- fetched 2026-10-24 · **82 rows** · 11 columns
- paged by OBJECTID via arcgis_layers.py; 82 rows

## Columns

| column | kind | non-null | distinct | summary |
| --- | --- | --- | --- | --- |
| `OBJECTID` | num | 100% | 82 | 1,385 · p25 1,423 · p50 1,450 · p95 8,974 · max 9,733  █▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁ |
| `NAME` | id/text | 100% | 82 | e.g. Bacchus Mud Lake Compl, Barber's Creek Marsh, Bellamys Lake Wetland |
| `SIGNIF` | cat | 100% | 2 | Provincial 87%, Other 13% |
| `created_user` | cat | 100% | 1 | GIS_ADMIN 100% |
| `created_date` | date | 100% | 30 | 1970-01-01 → 1970-01-01 |
| `last_edited_user` | cat | 100% | 1 | GIS_ADMIN 100% |
| `last_edited_date` | date | 100% | 39 | 1970-01-01 → 1970-01-01 |
| `Shape.STArea()` | num | 100% | 82 | 9,563 · p25 1,458,270 · p50 3,927,373 · p95 22,395,101 · max 40,631,033  █▅▂▁▁▂▁▁▁▁▁▁▁▁▁▁ |
| `Shape.STLength()` | num | 100% | 82 | 767 · p25 14,914 · p50 36,719 · p95 164,060 · max 461,139  █▅▃▂▁▁▁▁▁▁▁▁▁▁▁▁ |
| `regsDate` | date | 2% | 1 | 1970-01-01 → 1970-01-01 |
| `geometry` | id/text | 100% | 82 | e.g. {"type": "MultiPolygon, {"type": "Polygon", "c, {"type": "MultiPolygon |

## Candidate questions

- (none templated)

_profiled 2026-10-24 · `python3 tools/profile.py rvca_regulated_wetlands`_
