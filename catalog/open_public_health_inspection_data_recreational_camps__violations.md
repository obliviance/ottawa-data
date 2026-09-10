# Public Health Inspection Data - Recreational Camps — violations.csv

`open_public_health_inspection_data_recreational_camps__violations` · shape **arcgis-hub** · source `ottawa-public-health`

- origin: <https://open.ottawa.ca/documents/ottawa::public-health-inspection-data-recreational-camps>
- fetched 2026-09-09 · **2 rows** · 8 columns
- from zip · licence: https://ottawa.ca/en/city-hall/get-know-your-city/open-data#open-data-licence-ve

## Columns

| column | kind | non-null | distinct | summary |
| --- | --- | --- | --- | --- |
| `violation_id` | cat | 100% | 2 | 2B8C6BBC-7F7D-4B92-A726- 50%, EB5B05D4-D775-4C02-BDDE- 50% |
| `inspection_id` | cat | 100% | 2 | 1586B8AC-329E-4323-9D32- 50%, CC555CD5-D2E7-43D8-BD64- 50% |
| `business_id` | cat | 100% | 1 | 4FB1575E-FDFB-42D5-BB04- 100% |
| `date` | date | 100% | 2 | 2024-07-05 → 2025-06-13, 1 gaps >30d |
| `description` | cat | 100% | 1 | Sleeping areas and other 100% |
| `code` | cat | 100% | 1 | M2C160Q549 100% |
| `critical` | cat | 100% | 1 | False 100% |
| `CDI` | cat | 100% | 1 | False 100% |

## Candidate questions

- (none templated)

_profiled 2026-09-09 · `python3 tools/profile.py open_public_health_inspection_data_recreational_camps__violations`_
