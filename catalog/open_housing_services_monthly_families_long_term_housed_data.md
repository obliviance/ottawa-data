# Housing Services monthly families long term housed data

`open_housing_services_monthly_families_long_term_housed_data` · shape **arcgis-hub** · source `open-ottawa`

- origin: <https://open.ottawa.ca/datasets/ottawa::housing-services-monthly-families-long-term-housed-data>
- fetched 2026-09-09 · **280 rows** · 4 columns
- csv · licence: 

## Columns

| column | kind | non-null | distinct | summary |
| --- | --- | --- | --- | --- |
| `Date` | date | 100% | 140 | 2014-01-01 → 2025-08-01, 81 gaps >30d |
| `Count_` | num | 100% | 131 | 11.00 · p25 48.00 · p50 65.50 · p95 179 · max 214  ▁▃█▇▃▂▂▃▂▂▃▃▂▂▁▁ |
| `Category` | cat | 100% | 2 | Family Household Members 50%, Family Households Housed 50% |
| `ObjectId` | num | 100% | 280 | 1.00 · p25 70.75 · p50 140 · p95 266 · max 280  █▇█▇█▇█▇▇█▇█▇█▇█ |

## Candidate questions

- (none templated)

_profiled 2026-09-09 · `python3 tools/profile.py open_housing_services_monthly_families_long_term_housed_data`_
