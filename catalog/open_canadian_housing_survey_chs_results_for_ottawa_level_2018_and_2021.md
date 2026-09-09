# Canadian Housing Survey (CHS) results for Ottawa level 2018 and 2021 

`open_canadian_housing_survey_chs_results_for_ottawa_level_2018_and_2021` · shape **arcgis-hub** · source `open-ottawa`

- origin: <https://open.ottawa.ca/datasets/ottawa::canadian-housing-survey-chs-results-for-ottawa-level-2018-and-2021->
- fetched 2026-09-09 · **3,014 rows** · 14 columns
- csv · licence: https://ottawa.ca/en/city-hall/get-know-your-city/open-data#open-data-licence-ve

## Columns

| column | kind | non-null | distinct | summary |
| --- | --- | --- | --- | --- |
| `year` | num | 100% | 2 | 2,018 · p25 2,018 · p50 2,018 · p95 2,021 · max 2,021  █▁▁▁▁▁▁▁▁▁▁▁▁▁▁▅ |
| `theme` | cat | 100% | 6 | Perceptions of crime, so 32%, Financial pressures 19%, Satisfaction 17%, Other 13%, Housing quality & needs 12%, Trust & civic engagement 7% |
| `qid_key` | num | 100% | 61 | 1.00 · p25 17.00 · p50 34.00 · p95 55.00 · max 61.00  ▇▂▄▄▃▄▄▃▄▅█▆▄▅▂▂ |
| `qid` | num | 100% | 54 | 1.00 · p25 13.00 · p50 23.00 · p95 48.00 · max 54.00  ▇▃▄▄▅▅█▅▄▇▃▃▃▂▂▂ |
| `qheader` | text | 100% | 28 | e.g. [Among those who skipp, Is any member of your , In the past 12 months, |
| `qsub` | text | 61% | 38 | e.g. [Among those who respo, [Among those who respo, [Among those who respo |
| `socio_group` | cat | 94% | 5 | Education 39%, Racial identity 19%, Sexual orientation 19%, Sex 19%, Overall 4% |
| `group_` | cat | 100% | 11 | University certificate 9%, Racialized 9%, LGBTQ2S+ 9%, Female 9%, Heterosexual 9%, High school diploma or a 9% |
| `response` | text | 100% | 38 | e.g. No, Easy, Very easy |
| `num` | num | 97% | 1,223 | 0.00 · p25 8,000 · p50 23,100 · p95 318,665 · max 1,078,000  █▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁ |
| `denom` | num | 100% | 173 | 1,000 · p25 68,300 · p50 208,400 · p95 543,600 · max 1,093,500  █▅▁▅▃▃▂▁▁▁▁▁▁▁▁▁ |
| `percent_` | num | 97% | 828 | 0.00 · p25 8.20 · p50 18.30 · p95 91.20 · max 100  ▇█▅▃▂▂▂▂▁▁▂▂▂▂▂▂ |
| `Quality` | cat | 83% | 4 | Good 77%, Use with caution 11%, Acceptable 10%, Suppressed 3% |
| `ObjectId` | num | 100% | 3,014 | 1.00 · p25 754 · p50 1,508 · p95 2,863 · max 3,014  █▇▇█▇▇█▇▇█▇▇█▇▇█ |

## Candidate questions

- Trend / seasonality of open_canadian_housing_survey_chs_results_for_ottawa_level_2018_and_2021 over `year`; structural breaks?

_profiled 2026-09-09 · `python3 tools/profile.py open_canadian_housing_survey_chs_results_for_ottawa_level_2018_and_2021`_
