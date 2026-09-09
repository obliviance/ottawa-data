# COVID-19 Reproduction Number (R(t))

`open_covid_19_reproduction_number_r_t` · shape **arcgis-hub** · source `open-ottawa`

- origin: <https://open.ottawa.ca/datasets/ottawa::covid-19-reproduction-number-rt>
- fetched 2026-09-09 · **737 rows** · 6 columns
- csv · licence: https://ottawa.ca/en/city-hall/get-know-your-city/open-data#open-data-licence-ve

## Columns

| column | kind | non-null | distinct | summary |
| --- | --- | --- | --- | --- |
| `Date` | date | 100% | 737 | 2020-03-01 → 2022-03-07 |
| `Lower_Bound___95__Confidence_Interval` | num | 98% | 729 | 0.40 · p25 0.77 · p50 0.88 · p95 1.29 · max 1.82  ▁▂▂▅▇█▅▄▄▂▁▁▁▁▁▁ |
| `Upper_Bounds___95__Confidence_Interval` | num | 98% | 729 | 0.59 · p25 0.96 · p50 1.11 · p95 1.70 · max 3.33  ▁▆█▆▅▂▁▁▁▁▁▁▁▁▁▁ |
| `Estimate_of_R_t___7_Day_Average_` | num | 98% | 729 | 0.52 · p25 0.86 · p50 1.00 · p95 1.47 · max 2.53  ▁▃▇█▆▅▂▁▁▁▁▁▁▁▁▁ |
| `Nowcasting_Adjusted_Cases_by_Episode_Date` | date | 100% | 210 | 1970-01-01 → 1970-01-01 |
| `ObjectId` | num | 100% | 737 | 1.00 · p25 185 · p50 369 · p95 700 · max 737  █▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇ |

## Candidate questions

- Trend / seasonality of open_covid_19_reproduction_number_r_t over `Date`; structural breaks?

_profiled 2026-09-09 · `python3 tools/profile.py open_covid_19_reproduction_number_r_t`_
