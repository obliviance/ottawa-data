# Contracts awarded under delegation of authority for the period July-Dec 2023

`open_contracts_awarded_under_delegation_of_authority_for_the_period_jul` · shape **arcgis-hub** · source `open-ottawa`

- origin: <https://open.ottawa.ca/datasets/ottawa::contracts-awarded-under-delegation-of-authority-for-the-period-july-dec-2023>
- fetched 2026-09-09 · **843 rows** · 10 columns
- geojson · licence: https://ottawa.ca/en/city-hall/open-transparent-and-accountable-government/open-

## Columns

| column | kind | non-null | distinct | summary |
| --- | --- | --- | --- | --- |
| `Item__` | num | 100% | 843 | 1.00 · p25 212 · p50 422 · p95 801 · max 843  ██▇██▇██▇█▇██▇██ |
| `Contract` | id/text | 100% | 800 | e.g. 35821?91063?C01, 38823?03100?S01, 38023?92830?T01 |
| `Department` | cat | 100% | 17 | Infrastructure & Water S 47%, Finance and Corporate Se 14%, Public Works 13%, Planning, Real Estate &  7%, Recreation, Cultural & F 7%, Community and Social Ser 2% |
| `Description` | id/text | 100% | 832 | e.g. All labour, equipment , Standing offer to supp, All labour, equipment  |
| `Professional_Services_Designati` | cat | 42% | 3 | PE = Specialized Experti 99%, PR = Regulatory Requirem 0%, CE = Specialized Experti 0% |
| `Contract_Approval_Request_Type` | cat | 100% | 7 | Initial 60%, Amendment 26%, Extension 8%, Extension & Amendment 3%, Extension ( As per Secti 2%, Follow?On 1% |
| `Amount` | id/text | 100% | 812 | e.g. $            45,323.23, $          150,000.00, $          318,939.50 |
| `Vendor` | text | 100% | 472 | e.g. KCE CONSTRUCTION LTD, MASTER REFRIGERATION, BRUCE MECHANICAL LTD |
| `Non_Competitive_Rationale` | cat | 19% | 11 | Section 22 (1) (D) 48%, Section 22 (1) (H) 10%, Section 22 (1) (C) 10%, Section 22 (1) (A) 9%, Section 22 (1) (B) 9%, Section 22 (1) (F) 6% |
| `ObjectId` | num | 100% | 843 | 1.00 · p25 212 · p50 422 · p95 801 · max 843  ██▇██▇██▇█▇██▇██ |

## Candidate questions

- Concentration in `Vendor` — which actors dominate? (join entity spine)

_profiled 2026-09-09 · `python3 tools/profile.py open_contracts_awarded_under_delegation_of_authority_for_the_period_jul`_
