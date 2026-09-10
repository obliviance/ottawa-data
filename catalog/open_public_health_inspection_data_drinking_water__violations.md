# Public Health Inspection Data - Drinking Water — violations.csv

`open_public_health_inspection_data_drinking_water__violations` · shape **arcgis-hub** · source `ottawa-public-health`

- origin: <https://open.ottawa.ca/documents/ottawa::public-health-inspection-data-drinking-water>
- fetched 2026-09-09 · **530 rows** · 8 columns
- from zip · licence: https://ottawa.ca/en/city-hall/get-know-your-city/open-data#open-data-licence-ve

## Columns

| column | kind | non-null | distinct | summary |
| --- | --- | --- | --- | --- |
| `violation_id` | id/text | 100% | 530 | e.g. 04DCB214-36D3-4A0F-BEE, F896E17E-94B0-4B14-902, BFB3D4ED-ECC9-49CA-8F8 |
| `inspection_id` | text | 100% | 317 | e.g. 49A3E6C6-30F8-4E6D-971, 0E89F401-1266-451B-8D9, 5CDFDB87-0B10-43BA-B9B |
| `business_id` | text | 100% | 142 | e.g. 0077388F-0737-465F-B97, 01053D6E-81EC-46D4-93F, 0221E4FC-15D6-4EE1-BE1 |
| `date` | date | 100% | 317 | 2015-02-26 → 2026-09-03, 28 gaps >30d |
| `description` | text | 100% | 47 | e.g. The sampling frequency, Create and maintain re, The small drinking wat |
| `code` | text | 100% | 49 | e.g. M19C276Q923, M19C276Q939, M19C190Q639 |
| `critical` | cat | 100% | 2 | False 56%, True 44% |
| `CDI` | cat | 100% | 2 | False 83%, True 17% |

## Candidate questions

- Trend / seasonality of open_public_health_inspection_data_drinking_water__violations over `date`; structural breaks?

_profiled 2026-09-09 · `python3 tools/profile.py open_public_health_inspection_data_drinking_water__violations`_
