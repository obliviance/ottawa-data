# Confirmed Drug Overdose ED Visits by ONS Neighbourhood of Patient 

`open_confirmed_drug_overdose_ed_visits_by_ons_neighbourhood_of_patient` · shape **arcgis-hub** · source `open-ottawa`

- origin: <https://open.ottawa.ca/datasets/ottawa::confirmed-drug-overdose-ed-visits-by-ons-neighbourhood-of-patient->
- fetched 2026-09-09 · **113 rows** · 7 columns
- csv · licence: 

## Columns

| column | kind | non-null | distinct | summary |
| --- | --- | --- | --- | --- |
| `ONS_neighbourhood_ID` | num | 100% | 113 | 3,001 · p25 3,029 · p50 3,058 · p95 3,111 · max 3,117  █▇▇▇▇▇▇█▆▇▇█▇▅▇█ |
| `ONS_neighbourhood_name` | id/text | 100% | 113 | e.g. Airport, Alta Vista, Bayshore |
| `Cumulative_number_of_overdose_ED_visits_in_Ottawa_hospitals` | num | 100% | 90 | 0.00 · p25 6.00 · p50 13.20 · p95 93.60 · max 630  █▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁ |
| `Yearly_average_of_overdose_ED_visits_in_Ottawa_hospitals` | date | 100% | 63 | 1970-01-01 → 1970-01-01 |
| `Average_yearly_rate__per_100_000_population__of_overdose_ED_visits_in_Ottawa_hospitals` | date | 56% | 64 | 1970-01-01 → 1970-01-01 |
| `Years` | cat | 100% | 1 | 2020-2024 100% |
| `ObjectId` | num | 100% | 113 | 1.00 · p25 29.00 · p50 57.00 · p95 107 · max 113  █▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇ |

## Candidate questions

- (none templated)

_profiled 2026-09-09 · `python3 tools/profile.py open_confirmed_drug_overdose_ed_visits_by_ons_neighbourhood_of_patient`_
