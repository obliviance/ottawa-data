# COVID-19 Vaccine Coverage by Day by Age by Dose for Ottawa Residents (Historical data)

`open_covid_19_vaccine_coverage_by_day_by_age_by_dose_for_ottawa_residen` · shape **arcgis-hub** · source `open-ottawa`

- origin: <https://open.ottawa.ca/datasets/ottawa::covid-19-vaccine-coverage-by-day-by-age-by-dose-for-ottawa-residents-historical-data>
- fetched 2026-09-09 · **1,085 rows** · 20 columns
- csv · licence: https://ottawa.ca/en/city-hall/get-know-your-city/open-data#open-data-licence-ve

## Columns

| column | kind | non-null | distinct | summary |
| --- | --- | --- | --- | --- |
| `Date` | date | 100% | 1,085 | 2020-12-01 → 2023-11-26 |
| `Percent_of_Ottawa_residents_5_1` | text | 100% | 45 | e.g. 0%, 2%, 5% |
| `Percent_of_Ottawa_residents_12_` | text | 100% | 76 | e.g. 36%, 38%, 39% |
| `Percent_of_Ottawa_residents_18_` | text | 100% | 78 | e.g. 59%, 60%, 61% |
| `Percent_of_Ottawa_residents_30_` | text | 100% | 81 | e.g. 66%, 67%, 68% |
| `Percent_of_Ottawa_residents_40_` | text | 100% | 83 | e.g. 79%, 80%, 81% |
| `Percent_of_Ottawa_residents_50_` | text | 100% | 81 | e.g. 86%, 87%, 88% |
| `Percent_of_Ottawa_residents_60_` | text | 100% | 65 | e.g. 89%, 90%, 91% |
| `Percent_of_Ottawa_residents_70_` | text | 100% | 55 | e.g. 94%, 95%, 5% |
| `Percent_of_Ottawa_residents_80_` | text | 100% | 56 | e.g. 97%, 98%, 24% |
| `Percent_of_Ottawa_residents_5_2` | text | 100% | 46 | e.g. 0%, 1%, 2% |
| `Percent_of_Ottawa_residents_121` | text | 100% | 75 | e.g. 0%, 1%, 2% |
| `Percent_of_Ottawa_residents_181` | text | 100% | 66 | e.g. 9%, 10%, 11% |
| `Percent_of_Ottawa_residents_301` | text | 100% | 68 | e.g. 14%, 15%, 16% |
| `Percent_of_Ottawa_residents_401` | text | 100% | 69 | e.g. 21%, 22%, 23% |
| `Percent_of_Ottawa_residents_501` | text | 100% | 67 | e.g. 30%, 32%, 34% |
| `Percent_of_Ottawa_residents_601` | text | 100% | 63 | e.g. 43%, 46%, 49% |
| `Percent_of_Ottawa_residents_701` | text | 100% | 56 | e.g. 58%, 60%, 62% |
| `Percent_of_Ottawa_residents_801` | text | 100% | 64 | e.g. 67%, 69%, 71% |
| `ObjectId` | num | 100% | 1,085 | 1.00 · p25 272 · p50 543 · p95 1,031 · max 1,085  ████▇███▇███▇███ |

## Candidate questions

- Trend / seasonality of open_covid_19_vaccine_coverage_by_day_by_age_by_dose_for_ottawa_residen over `Date`; structural breaks?

_profiled 2026-09-09 · `python3 tools/profile.py open_covid_19_vaccine_coverage_by_day_by_age_by_dose_for_ottawa_residen`_
