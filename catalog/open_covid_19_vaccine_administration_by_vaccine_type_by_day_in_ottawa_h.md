# COVID-19 Vaccine Administration by Vaccine Type by Day in Ottawa (Historical data)

`open_covid_19_vaccine_administration_by_vaccine_type_by_day_in_ottawa_h` · shape **arcgis-hub** · source `open-ottawa`

- origin: <https://open.ottawa.ca/datasets/ottawa::covid-19-vaccine-administration-by-vaccine-type-by-day-in-ottawa-historical-data>
- fetched 2026-09-09 · **3,710 rows** · 4 columns
- csv · licence: https://ottawa.ca/en/city-hall/get-know-your-city/open-data#open-data-licence-ve

## Columns

| column | kind | non-null | distinct | summary |
| --- | --- | --- | --- | --- |
| `Date` | date | 100% | 1,290 | 2020-12-15 → 2024-07-07 |
| `Type_of_Vaccine` | cat | 100% | 9 | Pfizer monovalent 26%, Moderna monovalent 24%, Moderna bivalent 13%, Pfizer bivalent 12%, Moderna XBB 7%, Pfizer XBB 7% |
| `Number_of_doses_administered_in` | num | 100% | 1,441 | 1.00 · p25 14.00 · p50 136 · p95 4,381 · max 16,393  █▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁ |
| `ObjectId` | num | 100% | 3,710 | 1.00 · p25 928 · p50 1,856 · p95 3,525 · max 3,710  █████▇████▇█████ |

## Candidate questions

- Trend / seasonality of open_covid_19_vaccine_administration_by_vaccine_type_by_day_in_ottawa_h over `Date`; structural breaks?

_profiled 2026-09-09 · `python3 tools/profile.py open_covid_19_vaccine_administration_by_vaccine_type_by_day_in_ottawa_h`_
