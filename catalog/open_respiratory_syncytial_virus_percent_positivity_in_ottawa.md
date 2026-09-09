# Respiratory Syncytial Virus Percent Positivity in Ottawa

`open_respiratory_syncytial_virus_percent_positivity_in_ottawa` · shape **arcgis-hub** · source `open-ottawa`

- origin: <https://open.ottawa.ca/datasets/ottawa::respiratory-syncytial-virus-percent-positivity-in-ottawa>
- fetched 2026-09-09 · **52 rows** · 7 columns
- csv · licence: https://ottawa.ca/en/city-hall/open-transparent-and-accountable-government/open-

## Columns

| column | kind | non-null | distinct | summary |
| --- | --- | --- | --- | --- |
| `Epidemiological_Week_Number` | num | 100% | 52 | 1.00 · p25 13.75 · p50 26.50 · p95 50.45 · max 53.00  █▆▆█▆▆▆█▆▆▄█▆▆▆█ |
| `Start_of_Week` | id/text | 100% | 52 | e.g. 2026/01/04, 2026/01/11, 2026/01/18 |
| `Total_Tests_for_Ottawa_Residents` | num | 44% | 23 | 325 · p25 540 · p50 597 · p95 1,407 · max 1,528  ▂▄▃█▁▁▃▃▁▃▁▁▁▃▂▂ |
| `RSV_Percent_Positivity_in_Ottawa` | cat | 100% | 20 | NA% 56%, 0.2% 8%, 0.0% 4%, 6.2% 2%, 10.2% 2%, 9.1% 2% |
| `Historical_Average_of_RSV_Percent_Positivity_in_Ottawa` | text | 100% | 34 | e.g. 5.8%, 4.6%, 4.3% |
| `Order_of_Weeks_in_Respiratory_Surveillance_Season` | num | 100% | 52 | 1.00 · p25 13.75 · p50 26.50 · p95 49.45 · max 52.00  █▆▆▆▆█▆▆▆▆█▆▆▆▆█ |
| `ObjectId` | num | 100% | 52 | 1.00 · p25 13.75 · p50 26.50 · p95 49.45 · max 52.00  █▆▆▆▆█▆▆▆▆█▆▆▆▆█ |

## Candidate questions

- (none templated)

_profiled 2026-09-09 · `python3 tools/profile.py open_respiratory_syncytial_virus_percent_positivity_in_ottawa`_
