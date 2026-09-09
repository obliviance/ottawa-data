# Housing Services monthly HIFIS data

`open_housing_services_monthly_hifis_data` · shape **arcgis-hub** · source `open-ottawa`

- origin: <https://open.ottawa.ca/datasets/ottawa::housing-services-monthly-hifis-data>
- fetched 2026-09-09 · **2,616 rows** · 5 columns
- csv · licence: https://ottawa.ca/en/city-hall/open-transparent-and-accountable-government/open-

## Columns

| column | kind | non-null | distinct | summary |
| --- | --- | --- | --- | --- |
| `Date` | date | 100% | 150 | 2014-01-01 → 2026-06-01, 87 gaps >30d |
| `Count_` | num | 100% | 1,248 | 15.00 · p25 126 · p50 422 · p95 2,428 · max 4,641  █▄▃▂▂▁▁▁▁▁▁▁▁▁▁▁ |
| `TotalLengthOfStay` | num | 100% | 2,066 | 330 · p25 2,630 · p50 15,178 · p95 62,774 · max 123,142  █▂▃▂▂▂▁▁▁▁▁▁▁▁▁▁ |
| `Category` | cat | 100% | 23 | Single Adult Females 6%, Single Youth 18 Under 6%, Family Units 6%, Family Households 6%, All Clients 6%, All Singles 6% |
| `ObjectId` | num | 100% | 2,616 | 1.00 · p25 655 · p50 1,308 · p95 2,485 · max 2,616  █▇█▇█▇█▇▇█▇█▇█▇█ |

## Candidate questions

- Trend / seasonality of open_housing_services_monthly_hifis_data over `Date`; structural breaks?

_profiled 2026-09-09 · `python3 tools/profile.py open_housing_services_monthly_hifis_data`_
