# Public Health Inspection Data - Child Care — inspections.csv

`open_public_health_inspection_data_child_care__inspections` · shape **arcgis-hub** · source `ottawa-public-health`

- origin: <https://open.ottawa.ca/documents/ottawa::public-health-inspection-data-child-care>
- fetched 2026-09-09 · **3,840 rows** · 7 columns
- from zip · licence: https://ottawa.ca/en/city-hall/get-know-your-city/open-data#open-data-licence-ve

## Columns

| column | kind | non-null | distinct | summary |
| --- | --- | --- | --- | --- |
| `inspection_id` | id/text | 100% | 3,840 | e.g. 006841F4-11EC-4316-8D5, 008C1D4E-D080-4791-AD1, 00DA0335-FD1D-4913-AB4 |
| `business_id` | text | 100% | 605 | e.g. 4822615F-3446-48DD-BAE, AACA34B2-1A69-44CB-9C5, BFD1FE92-ADE3-4294-A6B |
| `date` | date | 100% | 3,833 | 2015-01-09 → 2026-09-04, 2 gaps >30d |
| `score` | num | 100% | 2 | 0.00 · p25 100 · p50 100 · p95 100 · max 100  ▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁█ |
| `result` | text | 0% | 0 | e.g.  |
| `description` | text | 0% | 0 | e.g.  |
| `type` | cat | 100% | 4 | RE 87%, FU 7%, DE 5%, CO 1% |

## Candidate questions

- Trend / seasonality of open_public_health_inspection_data_child_care__inspections over `date`; structural breaks?

_profiled 2026-09-09 · `python3 tools/profile.py open_public_health_inspection_data_child_care__inspections`_
