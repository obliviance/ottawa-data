# COVID-19 Vaccine Administration by Vaccine Type and Dose in Ottawa (Historical data)

`open_covid_19_vaccine_administration_by_vaccine_type_and_dose_in_ottawa` · shape **arcgis-hub** · source `open-ottawa`

- origin: <https://open.ottawa.ca/datasets/ottawa::covid-19-vaccine-administration-by-vaccine-type-and-dose-in-ottawa-historical-data>
- fetched 2026-09-09 · **9 rows** · 6 columns
- csv · licence: https://ottawa.ca/en/city-hall/get-know-your-city/open-data#open-data-licence-ve

## Columns

| column | kind | non-null | distinct | summary |
| --- | --- | --- | --- | --- |
| `Type_of_Vaccine` | cat | 100% | 9 | AstraZeneca 11%, Johnson & Johnson 11%, Moderna bivalent 11%, Moderna monovalent 11%, Moderna XBB 11%, Novavax 11% |
| `Number_of_first_vaccine_doses_a` | num | 100% | 9 | 276 · p25 1,370 · p50 3,109 · p95 488,345 · max 697,367  █▂▁▁▂▁▁▁▁▁▁▁▁▁▁▂ |
| `Number_of_second_vaccine_doses_` | num | 100% | 9 | 6.00 · p25 619 · p50 1,486 · p95 466,182 · max 540,322  █▁▁▁▁▁▁▁▁▁▂▁▁▁▁▂ |
| `Number_of_third_vaccine_doses_a` | num | 100% | 9 | 0.00 · p25 87.00 · p50 4,208 · p95 309,873 · max 338,671  █▁▁▁▁▁▁▁▁▁▁▁▂▁▁▂ |
| `Total_number_of_vaccine_doses_a` | num | 100% | 9 | 282 · p25 67,714 · p50 125,891 · p95 1,368,352 · max 1,675,294  █▄▂▁▁▁▁▁▂▁▁▁▁▁▁▂ |
| `ObjectId` | num | 100% | 9 | 1.00 · p25 3.00 · p50 5.00 · p95 8.60 · max 9.00  ██▁█▁█▁█▁█▁█▁█▁█ |

## Candidate questions

- (none templated)

_profiled 2026-09-09 · `python3 tools/profile.py open_covid_19_vaccine_administration_by_vaccine_type_and_dose_in_ottawa`_
