# Public Health Inspection Data - Personal Services — inspections.csv

`open_public_health_inspection_data_personal_services__inspections` · shape **arcgis-hub** · source `ottawa-public-health`

- origin: <https://open.ottawa.ca/documents/ottawa::public-health-inspection-data-personal-services>
- fetched 2026-09-09 · **7,685 rows** · 7 columns
- from zip · licence: https://ottawa.ca/en/city-hall/get-know-your-city/open-data#open-data-licence-ve

## Columns

| column | kind | non-null | distinct | summary |
| --- | --- | --- | --- | --- |
| `inspection_id` | id/text | 100% | 7,685 | e.g. 0000EA42-1D77-4714-8C8, 0005CD11-CA01-44CB-8C7, 0017FB48-FA1B-4F1E-88A |
| `business_id` | text | 100% | 1,701 | e.g. D4BA3E64-7A39-4C8B-AF8, 8CB5BFA1-3B33-41CD-ABC, 88B0CEA2-B68C-41B1-A3D |
| `date` | date | 100% | 7,670 | 2015-01-06 → 2026-09-08, 2 gaps >30d |
| `score` | num | 100% | 2 | 0.00 · p25 100 · p50 100 · p95 100 · max 100  ▂▁▁▁▁▁▁▁▁▁▁▁▁▁▁█ |
| `result` | text | 0% | 0 | e.g.  |
| `description` | text | 0% | 0 | e.g.  |
| `type` | cat | 100% | 4 | RE 79%, FU 12%, DE 6%, CO 3% |

## Candidate questions

- Trend / seasonality of open_public_health_inspection_data_personal_services__inspections over `date`; structural breaks?

_profiled 2026-09-09 · `python3 tools/profile.py open_public_health_inspection_data_personal_services__inspections`_
