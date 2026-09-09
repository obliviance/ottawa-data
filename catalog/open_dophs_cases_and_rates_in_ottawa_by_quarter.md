# DOPHS Cases and Rates in Ottawa by Quarter

`open_dophs_cases_and_rates_in_ottawa_by_quarter` · shape **arcgis-hub** · source `open-ottawa`

- origin: <https://open.ottawa.ca/datasets/ottawa::dophs-cases-and-rates-in-ottawa-by-quarter>
- fetched 2026-09-09 · **426 rows** · 5 columns
- csv · licence: https://ottawa.ca/en/city-hall/get-know-your-city/open-data#open-data-licence-ve

## Columns

| column | kind | non-null | distinct | summary |
| --- | --- | --- | --- | --- |
| `Year_Quarter` | cat | 100% | 6 | 2023 Q1 17%, 2023 Q3 17%, 2023 Q2 17%, 2023 Q4 17%, 2024 Q1 17%, 2024 Q2 17% |
| `DPHS` | text | 100% | 71 | e.g. Acute Flaccid Paralysi, Streptococcal Infectio, AIDS |
| `Ottawa_Cases` | num | 100% | 73 | 0.00 · p25 0.00 · p50 0.00 · p95 71.00 · max 870  █▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁ |
| `Ottawa_Rates` | num | 100% | 56 | 0.00 · p25 0.00 · p50 0.00 · p95 4.46 · max 79.17  █▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁ |
| `ObjectId` | num | 100% | 426 | 1.00 · p25 107 · p50 214 · p95 405 · max 426  ██▇█▇█▇██▇█▇█▇██ |

## Candidate questions

- (none templated)

_profiled 2026-09-09 · `python3 tools/profile.py open_dophs_cases_and_rates_in_ottawa_by_quarter`_
