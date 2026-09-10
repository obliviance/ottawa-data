# Public Health Inspection Data - Personal Services — violations.csv

`open_public_health_inspection_data_personal_services__violations` · shape **arcgis-hub** · source `ottawa-public-health`

- origin: <https://open.ottawa.ca/documents/ottawa::public-health-inspection-data-personal-services>
- fetched 2026-09-09 · **6,520 rows** · 8 columns
- from zip · licence: https://ottawa.ca/en/city-hall/get-know-your-city/open-data#open-data-licence-ve

## Columns

| column | kind | non-null | distinct | summary |
| --- | --- | --- | --- | --- |
| `violation_id` | id/text | 100% | 6,520 | e.g. 2EE75C31-2594-40D6-A3B, 129819EE-83A8-4BF4-B86, 4EC7CF99-34BC-4F83-BCE |
| `inspection_id` | text | 100% | 2,327 | e.g. 3825BBC1-A9DB-42EE-8A9, C3E411C9-F456-41BF-96C, 3EBB8DED-0A67-4DCF-A5D |
| `business_id` | text | 100% | 962 | e.g. 00066F12-DB0E-4229-A66, 005392FA-4BA1-4512-914, 00BBD036-BFAC-470D-9CF |
| `date` | date | 100% | 2,323 | 2015-01-06 → 2026-09-03, 7 gaps >30d |
| `description` | text | 100% | 98 | e.g. Disinfectants are appr, Compliant with require, All equipment / items  |
| `code` | text | 100% | 106 | e.g. M42C629Q2370, M12C408Q1452, M12C409Q1466 |
| `critical` | cat | 100% | 2 | False 67%, True 33% |
| `CDI` | cat | 100% | 2 | False 62%, True 38% |

## Candidate questions

- Trend / seasonality of open_public_health_inspection_data_personal_services__violations over `date`; structural breaks?

_profiled 2026-09-09 · `python3 tools/profile.py open_public_health_inspection_data_personal_services__violations`_
