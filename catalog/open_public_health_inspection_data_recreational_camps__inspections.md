# Public Health Inspection Data - Recreational Camps — inspections.csv

`open_public_health_inspection_data_recreational_camps__inspections` · shape **arcgis-hub** · source `ottawa-public-health`

- origin: <https://open.ottawa.ca/documents/ottawa::public-health-inspection-data-recreational-camps>
- fetched 2026-09-09 · **12 rows** · 7 columns
- from zip · licence: https://ottawa.ca/en/city-hall/get-know-your-city/open-data#open-data-licence-ve

## Columns

| column | kind | non-null | distinct | summary |
| --- | --- | --- | --- | --- |
| `inspection_id` | cat | 100% | 12 | 1586B8AC-329E-4323-9D32- 8%, 1C401C74-E375-4F8C-B953- 8%, 6A9F099A-8790-41ED-92FB- 8%, 47A6321A-A3F8-4BF8-8104- 8%, 98AC9989-5C32-4A4D-92F7- 8%, BAEB3BE1-19A4-4B8E-AE37- 8% |
| `business_id` | cat | 100% | 4 | 4FB1575E-FDFB-42D5-BB04- 42%, B9C390EB-2F68-40AC-B97C- 33%, 9BF34837-2A01-4AB9-810D- 17%, 67994AD7-87C0-4366-9BFE- 8% |
| `date` | date | 100% | 12 | 2015-06-15 → 2026-06-15, 8 gaps >30d |
| `score` | num | 100% | 2 | 0.00 · p25 100 · p50 100 · p95 100 · max 100  ▂▁▁▁▁▁▁▁▁▁▁▁▁▁▁█ |
| `result` | text | 0% | 0 | e.g.  |
| `description` | text | 0% | 0 | e.g.  |
| `type` | cat | 100% | 1 | RE 100% |

## Candidate questions

- (none templated)

_profiled 2026-09-09 · `python3 tools/profile.py open_public_health_inspection_data_recreational_camps__inspections`_
