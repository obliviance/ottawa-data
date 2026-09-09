# All causes and respiratory related ED visits in Ottawa by age and week

`open_all_causes_and_respiratory_related_ed_visits_in_ottawa_by_age_and` · shape **arcgis-hub** · source `open-ottawa`

- origin: <https://open.ottawa.ca/datasets/ottawa::all-causes-and-respiratory-related-ed-visits-in-ottawa-by-age-and-week>
- fetched 2026-09-09 · **318 rows** · 8 columns
- csv · licence: https://ottawa.ca/en/city-hall/get-know-your-city/open-data#open-data-licence-ve

## Columns

| column | kind | non-null | distinct | summary |
| --- | --- | --- | --- | --- |
| `Epidemiological_Week` | text | 100% | 53 | e.g. 2025/08/24, 2025/08/31, 2025/09/07 |
| `Age_Category` | cat | 100% | 6 | 00 to 03 Years 17%, 04 to 11 Years 17%, 12 to 17 Years 17%, 18 to 54 Years 17%, 55 to 79 Years 17%, 80+ Years 17% |
| `All_Causes_ED_Visits_to_Ottawa_Hospitals` | num | 100% | 260 | 236 · p25 465 · p50 690 · p95 3,290 · max 3,492  ▅█▅▁▁▁▁▁▃▁▁▁▁▁▂▂ |
| `Respiratory_related_ED_Visits_to_Ottawa_Hospitals` | num | 100% | 193 | 13.00 · p25 73.00 · p50 144 · p95 304 · max 603  ▆█▄▄▆▆▃▁▁▁▁▁▁▁▁▁ |
| `F__ED_Visits_Respiratory_related_in_Ottawa_Hospitals` | text | 0% | 0 | e.g.  |
| `ObjectId` | text | 0% | 0 | e.g.  |
| `ObjectId2` | text | 0% | 0 | e.g.  |
| `ObjectId3` | num | 100% | 318 | 1.00 · p25 80.25 · p50 160 · p95 302 · max 318  █████▇████▇█████ |

## Candidate questions

- (none templated)

_profiled 2026-09-09 · `python3 tools/profile.py open_all_causes_and_respiratory_related_ed_visits_in_ottawa_by_age_and`_
