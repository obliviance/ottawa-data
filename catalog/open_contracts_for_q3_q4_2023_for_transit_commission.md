#  Contracts for Q3-Q4 2023 for Transit Commission

`open_contracts_for_q3_q4_2023_for_transit_commission` · shape **arcgis-hub** · source `open-ottawa`

- origin: <https://open.ottawa.ca/datasets/ottawa::-contracts-for-q3-q4-2023-for-transit-commission>
- fetched 2026-09-09 · **83 rows** · 11 columns
- csv · licence: https://ottawa.ca/en/city-hall/open-transparent-and-accountable-government/open-

## Columns

| column | kind | non-null | distinct | summary |
| --- | --- | --- | --- | --- |
| `Item__` | num | 100% | 83 | 1.00 · p25 21.50 · p50 42.00 · p95 78.90 · max 83.00  █▆▆▆▆▆▆█▆▆▆▆▆▆▆█ |
| `Contract` | id/text | 100% | 77 | e.g. 34923?55600?P02, 39623?05500?S01, 33522?55710?S01 |
| `Department` | cat | 100% | 1 | Transit Services 100% |
| `Service` | cat | 100% | 8 | Transit Bus Operations & 47%, Transit Customer Systems 33%, Transit Engineering Serv 6%, Transit Bus Operations & 5%, Transit Customer Systems 4%, Safety, Regulatory, Trai 2% |
| `Description` | id/text | 100% | 82 | e.g. Supply and deliver 51 , Standing offer to supp, Standing offer to supp |
| `Professional_Consulting_Service` | cat | 28% | 1 | PE = Specialized Experti 100% |
| `Contract_Approval_Request_Type` | cat | 100% | 5 | Initial 54%, Amendment 30%, Extension 12%, Extension ( As per Secti 2%, Extension & Amendment 1% |
| `Amount` | id/text | 100% | 81 | e.g. $     14,508,637.60, $       1,817,841.39, $          318,470.61 |
| `Vendor` | text | 100% | 61 | e.g. CREATIVE CARRIAGE LTD, NATSCO, THE AFTERMARKET PARTS  |
| `Non_Competitive_Rationale` | cat | 34% | 7 | Section 22 (1) (D) 55%, Section 22 (1) (A) 28%, Section 22 (1) (C) 3%, Section 22 (1) (J) 3%, Section 22 (1) (G) 3%, Section 22 (1) (B) 3% |
| `ObjectId` | num | 100% | 83 | 1.00 · p25 21.50 · p50 42.00 · p95 78.90 · max 83.00  █▆▆▆▆▆▆█▆▆▆▆▆▆▆█ |

## Candidate questions

- (none templated)

_profiled 2026-09-09 · `python3 tools/profile.py open_contracts_for_q3_q4_2023_for_transit_commission`_
