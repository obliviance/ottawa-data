# Transit Contracts awarded under DOA for the period of Jan 1, 2024 - Jun 30, 2024

`open_transit_contracts_awarded_under_doa_for_the_period_of_jan_1_2024_j` · shape **arcgis-hub** · source `open-ottawa`

- origin: <https://open.ottawa.ca/datasets/ottawa::transit-contracts-awarded-under-doa-for-the-period-of-jan-1-2024-jun-30-2024>
- fetched 2026-09-09 · **84 rows** · 11 columns
- geojson · licence: https://ottawa.ca/en/city-hall/get-know-your-city/open-data#open-data-licence-ve

## Columns

| column | kind | non-null | distinct | summary |
| --- | --- | --- | --- | --- |
| `Item_` | num | 100% | 84 | 1.00 · p25 21.75 · p50 42.50 · p95 79.85 · max 84.00  █▆▆▆▆█▆▆▆▆█▆▆▆▆█ |
| `Contract` | id/text | 100% | 80 | e.g. 19223-91013-T01, 00121-55756-S01, 34924-91522-C01 |
| `Department` | cat | 100% | 1 | Transit Services 100% |
| `Service` | cat | 100% | 5 | Transit Bus Operations & 52%, Transit Customer Systems 39%, Transit Engineering Serv 4%, Transit Service Delivery 2%, Transit Strat Comm and E 2% |
| `Description` | id/text | 100% | 83 | e.g. Provision of maintenan, Standing offer to supp, Professional services  |
| `Professional_Consulting__Servic` | cat | 21% | 1 | PE = Specialized Experti 100% |
| `Contract_Approval_Request__Type` | cat | 100% | 5 | Initial 55%, Amendment 21%, Extension ( As per Secti 14%, Extension 8%, Extension & Amendment 1% |
| `F_Amount_` | id/text | 100% | 83 | e.g. $ 1,464,317.25, $ 267,152.00, $ 128,850.00 |
| `Vendor` | text | 100% | 66 | e.g. JEMCOR ELEVATING INC, CANCORE INDUSTRIES INC, NANOS RESEARCH |
| `Non_Competitive_Rationale` | cat | 27% | 6 | Section 22 (1) (A) 39%, Section 22 (1) (D) 30%, Section 22 (1) (H) 13%, Section 22 (1) (J) 9%, Section 22 (1) (G) 4%, Section 22 (1) (C) 4% |
| `ObjectId` | num | 100% | 84 | 1.00 · p25 21.75 · p50 42.50 · p95 79.85 · max 84.00  █▆▆▆▆█▆▆▆▆█▆▆▆▆█ |

## Candidate questions

- (none templated)

_profiled 2026-09-09 · `python3 tools/profile.py open_transit_contracts_awarded_under_doa_for_the_period_of_jan_1_2024_j`_
