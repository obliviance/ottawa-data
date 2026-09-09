# COVID-19 Vaccine Coverage by Day and Location of Vaccination for Ottawa Residents (Historical data)

`open_covid_19_vaccine_coverage_by_day_and_location_of_vaccination_for_o` · shape **arcgis-hub** · source `open-ottawa`

- origin: <https://open.ottawa.ca/datasets/ottawa::covid-19-vaccine-coverage-by-day-and-location-of-vaccination-for-ottawa-residents-historical-data>
- fetched 2026-09-09 · **1,212 rows** · 11 columns
- geojson · licence: https://ottawa.ca/en/city-hall/get-know-your-city/open-data#open-data-licence-ve

## Columns

| column | kind | non-null | distinct | summary |
| --- | --- | --- | --- | --- |
| `Date` | date | 100% | 1,212 | 2020-12-01 → 2024-04-01 |
| `Number_of_Ottawa_residents_rece` | num | 100% | 1,015 | 0.00 · p25 306 · p50 1,178 · p95 10,858 · max 19,611  █▃▂▁▁▁▁▁▁▁▁▁▁▁▁▁ |
| `Number_of_Ottawa_residents_re_1` | num | 100% | 418 | 0.00 · p25 17.00 · p50 66.00 · p95 1,002 · max 2,479  █▂▁▁▁▁▁▁▁▁▁▁▁▁▁▁ |
| `Number_of_Ottawa_residents_re_2` | num | 100% | 445 | 0.00 · p25 8.00 · p50 39.00 · p95 3,070 · max 17,268  █▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁ |
| `Number_of_Ottawa_residents_re_3` | num | 100% | 206 | 0.00 · p25 0.00 · p50 3.00 · p95 340 · max 2,065  █▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁ |
| `Number_of_Ottawa_residents_re_4` | num | 100% | 379 | 0.00 · p25 2.00 · p50 24.00 · p95 1,818 · max 17,723  █▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁ |
| `Number_of_Ottawa_residents_re_5` | num | 100% | 142 | 0.00 · p25 0.00 · p50 2.00 · p95 135 · max 2,337  █▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁ |
| `Percent_of_Ottawa_residents__5_` | text | 100% | 90 | e.g. 0%, 1%, 68% |
| `Percent_of_Ottawa_residents__51` | text | 100% | 73 | e.g. 0%, 23%, 25% |
| `Percent_of_Ottawa_residents__52` | text | 0% | 0 | e.g.  |
| `ObjectId` | num | 100% | 1,212 | 1.00 · p25 304 · p50 606 · p95 1,151 · max 1,212  ███▇██▇██▇██▇███ |

## Candidate questions

- Trend / seasonality of open_covid_19_vaccine_coverage_by_day_and_location_of_vaccination_for_o over `Date`; structural breaks?

_profiled 2026-09-09 · `python3 tools/profile.py open_covid_19_vaccine_coverage_by_day_and_location_of_vaccination_for_o`_
