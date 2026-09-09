# Public Health Inspection Data - Drinking Water — inspections.csv

`open_public_health_inspection_data_drinking_water__inspections` · shape **arcgis-hub** · source `ottawa-public-health`

- origin: <https://open.ottawa.ca/documents/ottawa::public-health-inspection-data-drinking-water>
- fetched 2026-09-09 · **1,061 rows** · 7 columns
- from zip · licence: https://ottawa.ca/en/city-hall/get-know-your-city/open-data#open-data-licence-ve

## Columns

| column | kind | non-null | distinct | summary |
| --- | --- | --- | --- | --- |
| `inspection_id` | id/text | 100% | 1,061 | e.g. 0076622C-654A-457A-B86, 00E888E1-2BA9-465E-A56, 01157471-E967-4D7B-BA7 |
| `business_id` | text | 100% | 256 | e.g. DD4C4D5A-8AC0-40EE-AAF, 3291DE02-2F18-4AE9-BFE, 6446CBE0-59FA-4B6F-A1C |
| `date` | date | 100% | 1,060 | 2015-02-20 → 2026-09-08, 23 gaps >30d |
| `score` | num | 100% | 2 | 0.00 · p25 100 · p50 100 · p95 100 · max 100  ▃▁▁▁▁▁▁▁▁▁▁▁▁▁▁█ |
| `result` | text | 0% | 0 | e.g.  |
| `description` | text | 0% | 0 | e.g.  |
| `type` | cat | 100% | 3 | RE 73%, FU 17%, DE 10% |

## Candidate questions

- Trend / seasonality of open_public_health_inspection_data_drinking_water__inspections over `date`; structural breaks?

_profiled 2026-09-09 · `python3 tools/profile.py open_public_health_inspection_data_drinking_water__inspections`_
