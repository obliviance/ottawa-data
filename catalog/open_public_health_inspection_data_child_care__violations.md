# Public Health Inspection Data - Child Care — violations.csv

`open_public_health_inspection_data_child_care__violations` · shape **arcgis-hub** · source `ottawa-public-health`

- origin: <https://open.ottawa.ca/documents/ottawa::public-health-inspection-data-child-care>
- fetched 2026-09-09 · **814 rows** · 8 columns
- from zip · licence: https://ottawa.ca/en/city-hall/get-know-your-city/open-data#open-data-licence-ve

## Columns

| column | kind | non-null | distinct | summary |
| --- | --- | --- | --- | --- |
| `violation_id` | id/text | 100% | 814 | e.g. 5B347419-A8BA-494E-881, 53E39B91-9ED9-4AB0-96E, BD5D8D90-7045-4317-965 |
| `inspection_id` | text | 100% | 529 | e.g. 631FFD76-9B70-44B9-869, 46A3202B-8174-4AE1-825, E437E365-C369-4515-AAC |
| `business_id` | text | 100% | 270 | e.g. 00BEC843-7823-4186-916, 0118C39C-AABA-49E8-985, 050F5D42-930B-4050-9AB |
| `date` | date | 100% | 529 | 2015-01-09 → 2026-09-01, 26 gaps >30d |
| `description` | text | 100% | 38 | e.g. Washrooms have adequat, Policies for exclusion, Change tables are main |
| `code` | text | 100% | 43 | e.g. M11C573Q2171, M11C272Q919, M11C271Q910 |
| `critical` | cat | 100% | 2 | True 51%, False 49% |
| `CDI` | cat | 100% | 2 | False 70%, True 30% |

## Candidate questions

- Trend / seasonality of open_public_health_inspection_data_child_care__violations over `date`; structural breaks?

_profiled 2026-09-09 · `python3 tools/profile.py open_public_health_inspection_data_child_care__violations`_
