# Respiratory Outbreaks (Excluding COVID-19)

`open_respiratory_outbreaks_excluding_covid_19` · shape **arcgis-hub** · source `open-ottawa`

- origin: <https://open.ottawa.ca/datasets/ottawa::respiratory-outbreaks-excluding-covid-19>
- fetched 2026-09-09 · **27 rows** · 12 columns
- csv · licence: https://ottawa.ca/en/city-hall/open-transparent-and-accountable-government/open-

## Columns

| column | kind | non-null | distinct | summary |
| --- | --- | --- | --- | --- |
| `Week_Number` | num | 100% | 27 | 1.00 · p25 7.50 · p50 40.00 · p95 51.70 · max 53.00  █▆▂▁▁▁▁▁▁▁▄█▆▆▆█ |
| `Start_of_the_Week` | id/text | 100% | 27 | e.g. 2025/11/16, 2025/11/23, 2025/11/30 |
| `Number_of_Respiratory_Outbreaks__Excl__COVID_19__in_Schools__Camps__and_Licensed_Child_Care` | num | 100% | 2 | 0.00 · p25 0.00 · p50 0.00 · p95 0.00 · max 1.00  █▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁ |
| `Number_of_Respiratory_Outbreaks__Excl__COVID_19__in_Healthcare_Institutions` | num | 100% | 14 | 0.00 · p25 3.00 · p50 6.00 · p95 15.00 · max 16.00  ▃▄▅▃▃█▂▂▁▂▁▁▂▂▃▂ |
| `Number_of_Respiratory_Outbreaks__Excl__COVID_19__in_Congregate_Care` | num | 100% | 2 | 0.00 · p25 0.00 · p50 0.00 · p95 1.00 · max 1.00  █▁▁▁▁▁▁▁▁▁▁▁▁▁▁▂ |
| `Previous_3_Season_Average_of_Respiratory_Outbreaks__Excl__COVID_19__in_Schools__Camps__and_Child_Care` | num | 96% | 10 | 0.00 · p25 0.00 · p50 0.00 · p95 6.30 · max 10.70  █▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁ |
| `Previous_3_Season_Average_of_Respiratory_Outbreaks__Excl__COVID_19__in_Healthcare_Institutions` | num | 96% | 16 | 1.00 · p25 1.77 · p50 3.70 · p95 7.22 · max 10.00  ▆▆▂▂▆▂▁▅▁▂█▂▁▁▁▂ |
| `Previous_3_Season_Average_of_Respiratory_Outbreaks__Excl__COVID_19__in_Congregate_Care` | num | 96% | 2 | 0.00 · p25 0.00 · p50 0.00 · p95 0.30 · max 0.30  █▁▁▁▁▁▁▁▁▁▁▁▁▁▁▆ |
| `Prior_to_COVID_19_3_Season_Average_of_Respiratory_Outbreaks_in_Schools__Camps__and_Child_Care` | num | 96% | 7 | 0.00 · p25 0.00 · p50 0.15 · p95 2.15 · max 2.30  █▁▃▁▂▁▁▁▁▁▁▁▁▁▁▂ |
| `Prior_to_COVID_19_3_Season_Average_of_Respiratory_Outbreaks_in_Healthcare_Institutions` | num | 96% | 16 | 0.30 · p25 1.00 · p50 2.35 · p95 14.07 · max 17.00  █▂▁▂▁▁▁▁▂▁▂▁▁▁▁▁ |
| `Prior_to_COVID_19_3_Season_Average_of_Respiratory_Outbreaks_in_Congregate_Care` | num | 96% | 1 | 0.00 · p25 0.00 · p50 0.00 · p95 0.00 · max 0.00   |
| `ObjectId` | num | 100% | 27 | 1.00 · p25 7.50 · p50 14.00 · p95 25.70 · max 27.00  ██▄██▄██▄█▄██▄██ |

## Candidate questions

- (none templated)

_profiled 2026-09-09 · `python3 tools/profile.py open_respiratory_outbreaks_excluding_covid_19`_
