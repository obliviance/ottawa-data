# Public Health Inspection Data - Recreational Water — inspections.csv

`open_public_health_inspection_data_recreational_water__inspections` · shape **arcgis-hub** · source `ottawa-public-health`

- origin: <https://open.ottawa.ca/documents/ottawa::public-health-inspection-data-recreational-water>
- fetched 2026-09-09 · **14,766 rows** · 7 columns
- from zip · licence: https://ottawa.ca/en/city-hall/get-know-your-city/open-data#open-data-licence-ve

## Columns

| column | kind | non-null | distinct | summary |
| --- | --- | --- | --- | --- |
| `inspection_id` | id/text | 100% | 14,766 | e.g. 00096516-DDB9-4871-86B, 001F7453-8D86-4595-964, 0020F4BE-BA57-48E2-89C |
| `business_id` | text | 100% | 819 | e.g. BA46E20A-591A-4A3C-B31, 3E63B9F6-05CF-4B4C-8B7, 91C398DF-F87C-4900-AE5 |
| `date` | date | 100% | 14,639 | 2000-08-16 → 2026-09-08, 6 gaps >30d |
| `score` | num | 99% | 2 | 0.00 · p25 0.00 · p50 100 · p95 100 · max 100  ▃▁▁▁▁▁▁▁▁▁▁▁▁▁▁█ |
| `result` | text | 0% | 0 | e.g.  |
| `description` | text | 0% | 0 | e.g.  |
| `type` | cat | 100% | 4 | RE 88%, FU 11%, CO 1%, DE 0% |

## Candidate questions

- Trend / seasonality of open_public_health_inspection_data_recreational_water__inspections over `date`; structural breaks?

_profiled 2026-09-09 · `python3 tools/profile.py open_public_health_inspection_data_recreational_water__inspections`_
