# Public Health Inspection Data - Food Safety — inspections.csv

`open_public_health_inspection_data_food_safety__inspections` · shape **arcgis-hub** · source `ottawa-public-health`

- origin: <https://open.ottawa.ca/documents/ottawa::public-health-inspection-data-food-safety-1>
- fetched 2026-09-09 · **96,157 rows** · 7 columns
- from zip · licence: https://ottawa.ca/en/city-hall/get-know-your-city/open-data#open-data-licence-ve

## Columns

| column | kind | non-null | distinct | summary |
| --- | --- | --- | --- | --- |
| `inspection_id` | id/text | 100% | 96,157 | e.g. 00017751-6E60-4995-A87, 00023B29-31B7-43C6-A0E, 00027613-8D0A-4346-A5E |
| `business_id` | text | 100% | 9,425 | e.g. 23648E71-2D42-4572-B02, C9E2EBAF-91B1-4A40-A8E, 6932401E-AA54-4192-941 |
| `date` | date | 100% | 94,970 | 2000-01-09 → 2026-09-08, 4 gaps >30d |
| `score` | num | 99% | 3 | 0.00 · p25 100 · p50 100 · p95 100 · max 100  ▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁█ |
| `result` | text | 0% | 0 | e.g.  |
| `description` | text | 0% | 0 | e.g.  |
| `type` | cat | 100% | 4 | RE 75%, FU 19%, CO 5%, DE 1% |

## Candidate questions

- Trend / seasonality of open_public_health_inspection_data_food_safety__inspections over `date`; structural breaks?

_profiled 2026-09-09 · `python3 tools/profile.py open_public_health_inspection_data_food_safety__inspections`_
