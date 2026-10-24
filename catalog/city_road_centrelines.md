# City of Ottawa — road centrelines (Road_Detail layer 3)

`city_road_centrelines` · shape **arcgis-hub** · source `road-network` · **spatial**

- origin: <https://maps.ottawa.ca/arcgis/rest/services/Road_Detail/MapServer/3>
- fetched 2026-10-24 · **29,457 rows** · 41 columns
- paged by OBJECTID via arcgis_layers.py; 29,457 rows

## Columns

| column | kind | non-null | distinct | summary |
| --- | --- | --- | --- | --- |
| `OBJECTID` | num | 100% | 29,457 | 249 · p25 51,288 · p50 62,928 · p95 80,913 · max 82,452  ▁▁▁▁▂▁▁▁▅▆▆▆▆▆▇█ |
| `GLOBALID` | id/text | 100% | 29,457 | e.g. {2B82E1DC-5BAE-4D13-98, {644B7812-E406-4DFF-A3, {CF2FF1CB-6E2F-4DE2-B1 |
| `SUBTYPE_TEXT` | cat | 100% | 9 | Local Road 64%, Collector Road 16%, Arterial Road 14%, Major Collector Road 3%, Provincial Highway 2%, Federally Owned Road 1% |
| `SUBCLASS` | cat | 100% | 15 | Local 64%, Collector 16%, Arterial 13%, Majcollector 3%, Ramp 1%, Roundabout 1% |
| `OWNERSHIP` | cat | 100% | 5 | Public 90%, Private 7%, Provincial 2%, Federal 1%, Other 0% |
| `FLOW` | cat | 8% | 2 | From-To 66%, To-From 34% |
| `GRADE_SEPARATED` | cat | 24% | 4 | No 96%, Under 2%, Over 2%, Yes 0% |
| `GEOMETRY_CREATED_DATE` | date | 99% | 4,045 | 1970-01-01 → 1970-01-01 |
| `GEOMETRY_MODIFIED_DATE` | date | 100% | 3,739 | 1970-01-01 → 1970-01-01 |
| `CURRENT_STATUS` | cat | 100% | 5 | Operational 92%, Open to Traffic 8%, Commence Work Issued 1%, Closed to Traffic 0%, Removed from Service 0% |
| `STATUS_CREATED_DATE` | date | 99% | 4,173 | 1970-01-01 → 1970-01-01 |
| `STATUS_MODIFIED_DATE` | date | 21% | 4,571 | 1970-01-01 → 1970-01-01 |
| `MAINT_SUBCLASS` | cat | 69% | 12 | 5A 51%, 3A 12%, 2A 11%, 3B 8%, 4A 6%, 4B 5% |
| `MAINTCLASS` | num | 69% | 5 | 1.00 · p25 3.00 · p50 5.00 · p95 5.00 · max 5.00  ▁▁▁▂▁▁▁▃▁▁▁▂▁▁▁█ |
| `MC_CREATED_DATE` | date | 83% | 1 | 1970-01-01 → 1970-01-01 |
| `MC_MODIFIED_DATE` | text | 0% | 0 | e.g.  |
| `BOUNDARY_RD` | cat | 99% | 2 | No 99%, Yes 1% |
| `FULL_ROADNAME_EN` | text | 99% | 9,068 | e.g. Riverside Dr, Uplands Dr, Cosanti Dr |
| `FULL_ROADNAME_FR` | text | 96% | 8,755 | e.g. prom Riverside, prom Uplands, prom Cosanti |
| `SUFFIX_FR` | text | 96% | 30 | e.g. prom, voie, côte |
| `ARTICLE_FR` | cat | 1% | 7 | de 32%, du 20%, de la 18%, des 16%, d' 8%, de l' 4% |
| `ROAD_NAME` | text | 99% | 8,754 | e.g. Riverside, Uplands, Cosanti |
| `SUFFIX_EN` | text | 96% | 38 | e.g. Dr, Way, Ridge |
| `DIRECTION` | cat | 2% | 4 | N. 30%, S. 26%, O./W. 25%, E. 19% |
| `ROAD_SIGN_TEXT` | text | 97% | 8,775 | e.g. prom. Riverside Dr., prom. Uplands Dr., prom. Cosanti Dr. |
| `LEFT_FROM` | num | 69% | 4,215 | 1.00 · p25 87.00 · p50 427 · p95 5,825 · max 9,859  █▂▂▁▁▁▁▁▁▁▁▁▁▁▁▁ |
| `LEFT_TO` | num | 69% | 4,227 | 1.00 · p25 92.75 · p50 437 · p95 5,869 · max 9,999  █▂▂▁▁▁▁▁▁▁▁▁▁▁▁▁ |
| `RIGHT_FROM` | num | 69% | 4,194 | 0.00 · p25 90.00 · p50 424 · p95 5,836 · max 9,500  █▂▂▁▁▁▁▁▁▁▁▁▁▁▁▁ |
| `RIGHT_TO` | num | 69% | 4,193 | 0.00 · p25 94.00 · p50 436 · p95 5,872 · max 9,710  █▂▂▁▁▁▁▁▁▁▁▁▁▁▁▁ |
| `ROAD_NAME_ID_ODD` | text | 99% | 9,218 | e.g. ___2SSWR, ___2STBQ, __0F5I2U |
| `ROAD_NAME_ID_EVEN` | text | 99% | 9,222 | e.g. ___2SSWR, ___2STBQ, __0F5I2U |
| `OT_ROAD_NAME_ID` | text | 99% | 9,068 | e.g. RN005403, RN010969, RN011997 |
| `FROM_RD_NAME` | text | 95% | 8,666 | e.g. Riverside Dr, Ocala St, Uplands Dr |
| `TO_RD_NAME` | text | 94% | 8,708 | e.g. Malhotra Crt, North Bowesville Rd, Shea Rd |
| `FROM_RD_ID` | text | 95% | 8,794 | e.g. ___2SSWR, __0F9Q9R, ___2STBQ |
| `TO_RD_ID` | text | 94% | 8,844 | e.g. ___2SUW3, __3AH0ZY, ___2SUDW |
| `ADD_CREATED_DATE` | date | 99% | 4,562 | 1970-01-01 → 1970-01-01 |
| `ADD_MODIFIED_DATE` | date | 60% | 6,427 | 1970-01-01 → 1970-01-01 |
| `RD_SEGMENT_ID` | id/text | 100% | 29,457 | e.g. __3Z09SY, __3Z0EAA, e___2IXC |
| `SHAPE_Length` | num | 100% | 29,457 | 5.24 · p25 110 · p50 173 · p95 1,095 · max 14,723  █▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁ |
| `geometry` | id/text | 100% | 29,457 | e.g. {"type": "LineString",, {"type": "LineString",, {"type": "LineString", |

## Candidate questions

- Trend / seasonality of city_road_centrelines over `GEOMETRY_CREATED_DATE`; structural breaks?
- Spatial clustering of city_road_centrelines; overlay wards + the decision timeline

_profiled 2026-10-24 · `python3 tools/profile.py city_road_centrelines`_
