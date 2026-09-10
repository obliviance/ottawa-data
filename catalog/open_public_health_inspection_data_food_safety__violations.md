# Public Health Inspection Data - Food Safety — violations.csv

`open_public_health_inspection_data_food_safety__violations` · shape **arcgis-hub** · source `ottawa-public-health`

- origin: <https://open.ottawa.ca/documents/ottawa::public-health-inspection-data-food-safety-1>
- fetched 2026-09-09 · **89,419 rows** · 8 columns
- from zip · licence: https://ottawa.ca/en/city-hall/get-know-your-city/open-data#open-data-licence-ve

## Columns

| column | kind | non-null | distinct | summary |
| --- | --- | --- | --- | --- |
| `violation_id` | id/text | 100% | 89,419 | e.g. 7D0FA685-CDBB-4A82-B32, 7CEAD3DE-9FB5-4639-856, 8DC55F38-E1D8-4E52-8B9 |
| `inspection_id` | text | 100% | 39,533 | e.g. BCEC4B8E-838C-4C84-98C, 9ABC90DC-FA51-4C73-AE5, 8483A5E1-E195-4F17-BF2 |
| `business_id` | text | 100% | 6,676 | e.g. 00080D0C-1786-4246-BCC, 00132732-6F41-4E2B-871, 002156B3-06D7-41E6-AC9 |
| `date` | date | 100% | 39,333 | 2000-01-04 → 2026-09-08, 4 gaps >30d |
| `description` | text | 100% | 168 | e.g. Utensils shall be sani, All equipment, utensil, Hand washing basin wit |
| `code` | text | 99% | 404 | e.g. M15C126Q427, M15C125Q443, M15C116Q370 |
| `critical` | cat | 100% | 2 | False 73%, True 27% |
| `CDI` | cat | 100% | 2 | False 62%, True 38% |

## Candidate questions

- Trend / seasonality of open_public_health_inspection_data_food_safety__violations over `date`; structural breaks?

_profiled 2026-09-09 · `python3 tools/profile.py open_public_health_inspection_data_food_safety__violations`_
