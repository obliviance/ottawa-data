#  Transit Contracts awarded under DOA Q3 and Q4 2022

`open_transit_contracts_awarded_under_doa_q3_and_q4_2022` · shape **arcgis-hub** · source `open-ottawa`

- origin: <https://open.ottawa.ca/datasets/ottawa::-transit-contracts-awarded-under-doa-q3-and-q4-2022>
- fetched 2026-09-09 · **70 rows** · 11 columns
- geojson · licence: https://ottawa.ca/en/city-hall/open-transparent-and-accountable-government/open-

## Columns

| column | kind | non-null | distinct | summary |
| --- | --- | --- | --- | --- |
| `Item__` | num | 100% | 70 | 1.00 · p25 18.25 · p50 35.50 · p95 66.55 · max 70.00  █▆▆█▆▆█▆▆█▆▆█▆▆█ |
| `Contract` | id/text | 100% | 69 | e.g. 34819-96618-T01, 26813-98386-T01, 30921-91051-T03 |
| `Department` | cat | 100% | 1 | Transit Services 100% |
| `Service` | cat | 100% | 9 | Transit Bus Operations & 49%, Transit Customer Systems 34%, Transit Strat Comm and E 6%, Safety, Regulatory, Trai 3%, Transit Service Delivery 3%, Transit Bus Operations a 1% |
| `Description` | id/text | 100% | 70 | e.g. Supply and deliver pad, Lease, washing and rep, All labour, equipment  |
| `Professional_Consulting_Service` | cat | 31% | 1 | PE = Specialized Experti 100% |
| `Contract_Approval_Request_Type` | cat | 100% | 6 | Initial 41%, Amendment 30%, Extension 13%, Extension ( As per Secti 7%, Initial and Amendment 6%, Extension & Amendment 3% |
| `Amount` | id/text | 100% | 70 | e.g. $       35,000.00, $     383,155.56, $       38,111.48 |
| `Vendor` | text | 100% | 54 | e.g. TRICO PACKAGING & PRIN, UNIFIRST CANADA LTD, ROYAL CROWN CONSTRUCTI |
| `Non_Competitive_Rationale` | cat | 32% | 4 | Section 22 (1) (D) 43%, Section 22 (1) (A) 35%, Section 22 (1) (C) 13%, Section 22 (1) (H) 9% |
| `ObjectId` | num | 100% | 70 | 1.00 · p25 18.25 · p50 35.50 · p95 66.55 · max 70.00  █▆▆█▆▆█▆▆█▆▆█▆▆█ |

## Candidate questions

- (none templated)

_profiled 2026-09-09 · `python3 tools/profile.py open_transit_contracts_awarded_under_doa_q3_and_q4_2022`_
