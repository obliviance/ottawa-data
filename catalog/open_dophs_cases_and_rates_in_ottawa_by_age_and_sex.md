# DOPHS Cases and Rates in Ottawa by Age and Sex

`open_dophs_cases_and_rates_in_ottawa_by_age_and_sex` · shape **arcgis-hub** · source `open-ottawa`

- origin: <https://open.ottawa.ca/datasets/ottawa::dophs-cases-and-rates-in-ottawa-by-age-and-sex>
- fetched 2026-09-09 · **23,430 rows** · 7 columns
- csv · licence: https://ottawa.ca/en/city-hall/get-know-your-city/open-data#open-data-licence-ve

## Columns

| column | kind | non-null | distinct | summary |
| --- | --- | --- | --- | --- |
| `Year` | num | 100% | 11 | 2,014 · p25 2,016 · p50 2,019 · p95 2,024 · max 2,024  ██▁██▁██▁█▁██▁██ |
| `Age` | cat | 100% | 10 | 00 to 04 Years 10%, 05 to 09 Years 10%, 10 to 14 Years 10%, 15 to 19 Years 10%, 20 to 24 Years 10%, 25 to 29 Years 10% |
| `Sex` | cat | 100% | 3 | Other/Unknown 33%, Male 33%, Female 33% |
| `DPHS` | text | 100% | 71 | e.g. Acute Flaccid Paralysi, AIDS, Amebiasis |
| `Ottawa_Cases` | num | 100% | 206 | 0.00 · p25 0.00 · p50 0.00 · p95 6.00 · max 987  █▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁ |
| `Ottawa_Rates` | num | 66% | 1,990 | 0.00 · p25 0.00 · p50 0.00 · p95 18.97 · max 2,608  █▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁ |
| `ObjectId` | num | 100% | 23,430 | 1.00 · p25 5,858 · p50 11,716 · p95 22,259 · max 23,430  █▇▇█▇▇█▇▇█▇▇█▇▇█ |

## Candidate questions

- Trend / seasonality of open_dophs_cases_and_rates_in_ottawa_by_age_and_sex over `Year`; structural breaks?

_profiled 2026-09-09 · `python3 tools/profile.py open_dophs_cases_and_rates_in_ottawa_by_age_and_sex`_
