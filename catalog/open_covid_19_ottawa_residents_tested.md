# COVID-19 Ottawa Residents Tested

`open_covid_19_ottawa_residents_tested` · shape **arcgis-hub** · source `open-ottawa`

- origin: <https://open.ottawa.ca/datasets/ottawa::covid-19-ottawa-residents-tested>
- fetched 2026-09-09 · **2,312 rows** · 8 columns
- csv · licence: https://ottawa.ca/en/city-hall/get-know-your-city/open-data#open-data-licence-ve

## Columns

| column | kind | non-null | distinct | summary |
| --- | --- | --- | --- | --- |
| `Date` | date | 100% | 2,312 | 2020-05-01 → 2026-08-29 |
| `Number_of_Tests__Excluding_LTCH` | num | 100% | 999 | -10.00 · p25 82.00 · p50 152 · p95 2,980 · max 5,376  █▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁ |
| `Daily___Positivity__Excluding_LTCH` | num | 100% | 1,631 | -0.02 · p25 0.02 · p50 0.06 · p95 0.22 · max 0.43  ▃█▄▃▃▃▂▂▂▁▁▁▁▁▁▁ |
| `F7_Day_Average_of___Positivity__Excluding_LTCH` | num | 100% | 2,256 | 0.00 · p25 0.03 · p50 0.07 · p95 0.20 · max 0.32  █▇▄▄▃▃▃▃▂▂▂▁▁▁▁▁ |
| `Number_of_Tests_in_LTCH` | num | 100% | 242 | 0.00 · p25 8.00 · p50 16.00 · p95 162 · max 810  █▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁ |
| `LTCH_Daily___Positivity` | num | 99% | 456 | 0.00 · p25 0.00 · p50 0.02 · p95 0.40 · max 1.00  █▂▁▁▁▁▁▁▁▁▁▁▁▁▁▁ |
| `F7_Day_Average_of_LTCH___Positivity` | num | 100% | 1,478 | 0.00 · p25 0.01 · p50 0.05 · p95 0.33 · max 0.54  █▃▂▁▂▁▁▁▁▁▁▁▁▁▁▁ |
| `ObjectId` | num | 100% | 2,312 | 1.00 · p25 579 · p50 1,156 · p95 2,196 · max 2,312  █▇█▇█▇█▇▇█▇█▇█▇█ |

## Candidate questions

- Trend / seasonality of open_covid_19_ottawa_residents_tested over `Date`; structural breaks?

_profiled 2026-09-09 · `python3 tools/profile.py open_covid_19_ottawa_residents_tested`_
