# DOPHS Cases in Ottawa by Month

`open_dophs_cases_in_ottawa_by_month` · shape **arcgis-hub** · source `open-ottawa`

- origin: <https://open.ottawa.ca/datasets/ottawa::dophs-cases-in-ottawa-by-month>
- fetched 2026-09-09 · **852 rows** · 8 columns
- csv · licence: https://ottawa.ca/en/city-hall/get-know-your-city/open-data#open-data-licence-ve

## Columns

| column | kind | non-null | distinct | summary |
| --- | --- | --- | --- | --- |
| `Month_Number` | num | 100% | 12 | 1.00 · p25 3.75 · p50 6.50 · p95 12.00 · max 12.00  ███▁██▁██▁██▁███ |
| `Month_Name` | cat | 100% | 12 | March 8%, May 8%, June 8%, January 8%, April 8%, February 8% |
| `DPHS` | text | 100% | 71 | e.g. Streptococcal Infectio, Tularemia, Streptococcus pneumoni |
| `Monthly_average_of_counts_from_` | num | 100% | 105 | 0.00 · p25 0.00 · p50 0.00 · p95 25.97 · max 350  █▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁ |
| `Ottawa_Cases_in_2021` | num | 100% | 59 | 0.00 · p25 0.00 · p50 0.00 · p95 23.45 · max 271  █▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁ |
| `Ottawa_Cases_in_2022` | num | 100% | 60 | 0.00 · p25 0.00 · p50 0.00 · p95 26.45 · max 321  █▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁ |
| `Ottawa_Cases_in_2023` | num | 100% | 66 | 0.00 · p25 0.00 · p50 0.00 · p95 25.00 · max 322  █▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁ |
| `ObjectId` | num | 100% | 852 | 1.00 · p25 214 · p50 426 · p95 809 · max 852  █▇▇▇▇█▇▇▇▇█▇▇▇▇█ |

## Candidate questions

- (none templated)

_profiled 2026-09-09 · `python3 tools/profile.py open_dophs_cases_in_ottawa_by_month`_
