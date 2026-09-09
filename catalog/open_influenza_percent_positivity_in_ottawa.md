# Influenza Percent Positivity in Ottawa

`open_influenza_percent_positivity_in_ottawa` · shape **arcgis-hub** · source `open-ottawa`

- origin: <https://open.ottawa.ca/datasets/ottawa::influenza-percent-positivity-in-ottawa>
- fetched 2026-09-09 · **52 rows** · 9 columns
- csv · licence: https://ottawa.ca/en/city-hall/open-transparent-and-accountable-government/open-

## Columns

| column | kind | non-null | distinct | summary |
| --- | --- | --- | --- | --- |
| `Epidemiological_Week` | num | 100% | 52 | 1.00 · p25 13.75 · p50 26.50 · p95 50.45 · max 53.00  █▆▆█▆▆▆█▆▆▄█▆▆▆█ |
| `Start_of_Week` | id/text | 100% | 52 | e.g. 2025/08/24, 2025/08/31, 2025/09/07 |
| `Total_Tests_for_Ottawa_Residents` | num | 46% | 24 | 325 · p25 548 · p50 600 · p95 1,407 · max 1,560  ▂▄▄█▁▁▅▂▂▂▁▁▂▂▂▂ |
| `Flu_A_Percent_Positivity_in_Ottawa` | cat | 100% | 21 | NA% 54%, 0.2% 6%, 0.4% 4%, 0.5% 4%, 0.6% 2%, 1.1% 2% |
| `Flu_B_Percent_Positivity_in_Ottawa` | cat | 100% | 9 | NA% 54%, 0.0% 17%, 0.4% 10%, 0.2% 4%, 0.1% 4%, 0.3% 4% |
| `Total_Influenza_Percent_Positivity_in_Ottawa` | cat | 100% | 22 | NA% 54%, 0.2% 4%, 0.4% 4%, 0.5% 4%, 0.6% 2%, 0.7% 2% |
| `Historical_Average_of_Flu_Percent_Positivity_in_Ottawa` | text | 100% | 35 | e.g. 0.1%, 0.2%, 0.0% |
| `Seasonal_Order_for_Weeks` | num | 100% | 52 | 1.00 · p25 13.75 · p50 26.50 · p95 49.45 · max 52.00  █▆▆▆▆█▆▆▆▆█▆▆▆▆█ |
| `ObjectId` | num | 100% | 52 | 1.00 · p25 13.75 · p50 26.50 · p95 49.45 · max 52.00  █▆▆▆▆█▆▆▆▆█▆▆▆▆█ |

## Candidate questions

- (none templated)

_profiled 2026-09-09 · `python3 tools/profile.py open_influenza_percent_positivity_in_ottawa`_
