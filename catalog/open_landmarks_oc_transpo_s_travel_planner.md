# Landmarks OC Transpo's Travel Planner

`open_landmarks_oc_transpo_s_travel_planner` · shape **arcgis-hub** · source `open-ottawa`

- origin: <https://open.ottawa.ca/datasets/ottawa::landmarks-oc-transpos-travel-planner>
- fetched 2026-09-09 · **3,888 rows** · 15 columns
- csv · licence: https://ottawa.ca/en/city-hall/get-know-your-city/open-data#open-data-licence-ve

## Columns

| column | kind | non-null | distinct | summary |
| --- | --- | --- | --- | --- |
| `X` | num | 100% | 3,605 | -76.21 · p25 -75.75 · p50 -75.70 · p95 -75.49 · max -75.34  ▁▁▁▁▁▂▂▂▆█▄▂▁▁▁▁ |
| `Y` | num | 100% | 3,605 | 45.12 · p25 45.36 · p50 45.41 · p95 45.50 · max 45.60  ▁▁▁▁▁▂▃▄▄▇█▄▃▁▁▁ |
| `OBJECTID` | num | 100% | 3,888 | 1.00 · p25 973 · p50 1,944 · p95 3,694 · max 3,888  ████████████████ |
| `LMKTYPE_ID` | text | 100% | 46 | e.g. WORSHIP, TRANSIT, DAYCARE |
| `DESCRIPTION` | text | 100% | 46 | e.g. Place of Worship,  _Transit Stations and, Day Care Centres and N |
| `UD_FRENCH_DESC` | text | 99% | 45 | e.g. Lieux de culte, Parc-o-bus et stations, Garderies |
| `DESCRIPTION_1` | id/text | 99% | 3,760 | e.g. St John the Evangelist, St Luke's Anglican, Fourth the Baptist |
| `DESC_SOUNDEX` | id/text | 99% | 3,760 | e.g. ST-JON TE EVENJELIS, EGLISE ENGLICANE ST-LU, AVE. FOUR BAPTISTE |
| `UD_FRENCH_DESC_1` | id/text | 98% | 3,732 | e.g. St-John the Evangelist, Église Anglicane St-Lu, Ave. Fourth Baptiste |
| `TELEPHONE` | id/text | 40% | 1,490 | e.g. 232-4500, 235-3416, 236-1804 |
| `PUBLIC_INFO` | id/text | 64% | 2,325 | e.g. 154 SOMERSET W., 760 SOMERSET W, 109-A 4 AVE. |
| `MUNICIP_NO` | num | 100% | 4 | 1.00 · p25 1.00 · p50 1.00 · p95 2.00 · max 4.00  █▁▁▁▁▃▁▁▁▁▁▁▁▁▁▁ |
| `City` | cat | 100% | 4 | OTTAWA 74%, GATINEAU 25%, CHELSEA 0%, CANTLEY 0% |
| `POINT_X` | num | 100% | 3,605 | -8,483,443 · p25 -8,432,880 · p50 -8,427,082 · p95 -8,403,384 · max -8,386,438  ▁▁▁▁▁▂▂▂▆█▄▂▁▁▁▁ |
| `POINT_Y` | num | 100% | 3,605 | 5,641,032 · p25 5,677,699 · p50 5,686,398 · p95 5,699,918 · max 5,716,900  ▁▁▁▁▁▂▃▄▅▇█▄▃▁▁▁ |

## Candidate questions

- (none templated)

_profiled 2026-09-09 · `python3 tools/profile.py open_landmarks_oc_transpo_s_travel_planner`_
