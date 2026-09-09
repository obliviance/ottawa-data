# Confirmed opioid toxicity deaths of Ottawa residents by ONS neighbourhood of incident

`open_confirmed_opioid_toxicity_deaths_of_ottawa_residents_by_ons_neighb` · shape **arcgis-hub** · source `open-ottawa`

- origin: <https://open.ottawa.ca/datasets/ottawa::confirmed-opioid-toxicity-deaths-of-ottawa-residents-by-ons-neighbourhood-of-incident>
- fetched 2026-09-09 · **96 rows** · 7 columns
- csv · licence: 

## Columns

| column | kind | non-null | distinct | summary |
| --- | --- | --- | --- | --- |
| `ONS_Neighbourhood_ID` | num | 100% | 96 | 3,001 · p25 3,026 · p50 3,054 · p95 3,111 · max 3,117  █▇▆▆▄▇▇▇▅▆▆▇▆▃▅▆ |
| `ONS_Neighbourhood_Name` | id/text | 100% | 96 | e.g. Airport, Alta Vista, Bayshore |
| `Cumulative_number_of_confirmed_opioid_toxicity_deaths` | num | 100% | 42 | 0.00 · p25 1.00 · p50 2.15 · p95 41.45 · max 98.00  █▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁ |
| `Yearly_average_of_confirmed_opioid_toxicity_deaths` | date | 100% | 36 | 1970-01-01 → 1970-01-01 |
| `Average_yearly_rate__per_100_000_population__of_confirmed_opioid_toxicity_deaths` | date | 14% | 14 | 1970-01-01 → 1970-01-01 |
| `Years` | cat | 100% | 1 | 2020-2024 100% |
| `ObjectId` | num | 100% | 96 | 1.00 · p25 24.75 · p50 48.50 · p95 91.25 · max 96.00  ████████████████ |

## Candidate questions

- (none templated)

_profiled 2026-09-09 · `python3 tools/profile.py open_confirmed_opioid_toxicity_deaths_of_ottawa_residents_by_ons_neighb`_
