# Open Ottawa items with no CSV/GeoJSON/zip download (inventory)

`open_ottawa_item_inventory` · shape **arcgis-hub** · source `open-ottawa`

- origin: <https://open.ottawa.ca/api/feed/dcat-us/1.1.json>
- fetched 2026-10-24 · **414 rows** · 10 columns
- item type/size from the ArcGIS item API; see arcgis_documents.py

## Columns

| column | kind | non-null | distinct | summary |
| --- | --- | --- | --- | --- |
| `item_id` | id/text | 100% | 414 | e.g. 896486d9aaf04e0c87c8bf, cfd074505f914d7ca937c2, 630e06f4cfcf49caa0018f |
| `title` | id/text | 100% | 414 | e.g. Budget 2021 Operating , Budget 2021 Operating , Budget 2020 Transit Ca |
| `landing_page` | id/text | 100% | 414 | e.g. https://open.ottawa.ca, https://open.ottawa.ca, https://open.ottawa.ca |
| `dcat_modified` | id/text | 100% | 414 | e.g. 2026-08-10T20:24:17.00, 2026-08-10T20:24:16.00, 2026-08-10T20:24:14.00 |
| `item_type` | cat | 100% | 11 | Microsoft Excel 62%, Web Mapping Application 11%, CSV 9%, Document Link 7%, CSV Collection 5%, Hub Page 3% |
| `file_name` | id/text | 77% | 322 | e.g. Operating_Status_Repor, 2021_Q1_Operating_Stat, Budget_2020_Transit_Ca |
| `size_bytes` | num | 100% | 362 | 0.00 · p25 16,479 · p50 70,656 · p95 5,687,092 · max 744,171,954  █▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁ |
| `error` | text | 0% | 0 | e.g.  |
| `item_modified` | date | 100% | 414 | 2021-02-13 → 2026-10-23, 11 gaps >30d |
| `kind` | cat | 100% | 6 | documents 70%, datasets 14%, apps 11%, pages 3%, maps 1%, content 0% |

## Candidate questions

- (none templated)

_profiled 2026-10-24 · `python3 tools/profile.py open_ottawa_item_inventory`_
