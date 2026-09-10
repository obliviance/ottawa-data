# Public Health Inspection Data - Recreational Water — violations.csv

`open_public_health_inspection_data_recreational_water__violations` · shape **arcgis-hub** · source `ottawa-public-health`

- origin: <https://open.ottawa.ca/documents/ottawa::public-health-inspection-data-recreational-water>
- fetched 2026-09-09 · **9,870 rows** · 8 columns
- from zip · licence: https://ottawa.ca/en/city-hall/get-know-your-city/open-data#open-data-licence-ve

## Columns

| column | kind | non-null | distinct | summary |
| --- | --- | --- | --- | --- |
| `violation_id` | id/text | 100% | 9,870 | e.g. 035D1D04-24B9-417F-905, DB49135B-CBE0-4D6A-A54, EA8B75A6-2EDA-409E-BF4 |
| `inspection_id` | text | 100% | 5,247 | e.g. D7CDF45F-5599-431A-A3B, 5111C196-F3A4-4D49-B37, D434608E-B9E7-457B-876 |
| `business_id` | text | 100% | 715 | e.g. 00326868-650B-4B24-A91, 00E8C558-B07C-45D1-917, 01004685-2089-4F08-ACD |
| `date` | date | 100% | 5,222 | 2015-01-12 → 2026-09-08, 4 gaps >30d |
| `description` | text | 100% | 162 | e.g. Spray/splash pad rules, Facility completes dai, Facility completes and |
| `code` | text | 100% | 342 | e.g. M36C165Q563, M36C543Q2066, M1C178Q608 |
| `critical` | cat | 100% | 2 | False 65%, True 35% |
| `CDI` | cat | 100% | 2 | False 75%, True 25% |

## Candidate questions

- Trend / seasonality of open_public_health_inspection_data_recreational_water__violations over `date`; structural breaks?

_profiled 2026-09-09 · `python3 tools/profile.py open_public_health_inspection_data_recreational_water__violations`_
