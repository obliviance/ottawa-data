# Contracts awarded under delegation of authority for Jan - June 2024 - All Departments

`open_contracts_awarded_under_delegation_of_authority_for_jan_june_2024` · shape **arcgis-hub** · source `open-ottawa`

- origin: <https://open.ottawa.ca/datasets/ottawa::contracts-awarded-under-delegation-of-authority-for-jan-june-2024-all-departments>
- fetched 2026-09-09 · **907 rows** · 10 columns
- geojson · licence: https://ottawa.ca/en/city-hall/get-know-your-city/open-data#open-data-licence-ve

## Columns

| column | kind | non-null | distinct | summary |
| --- | --- | --- | --- | --- |
| `Item_` | num | 100% | 907 | 1.00 · p25 228 · p50 454 · p95 862 · max 907  ██▇██▇██▇█▇██▇██ |
| `Contract_` | id/text | 100% | 877 | e.g. 41524-76028-C01, 35524-92500-P01, 38024-92500-T01 |
| `Department` | cat | 100% | 20 | Infrastructure & Water
S 34%, Infrastructure & Water S 19%, Public Works 11%, Finance and Corporate
Se 11%, Recreation, Cultural &
F 6%, Strategic Initiatives 3% |
| `Description` | id/text | 100% | 902 | e.g. Supply and deliver one, Professional engineeri, All labour, equipment  |
| `Professional_Consulting__Servic` | cat | 43% | 2 | PE = Specialized Experti 100%, NA 0% |
| `Contract_Approval__Request_Type` | cat | 100% | 9 | Initial 67%, Amendment 22%, Extension 6%, Extension & Amendment 2%, Extension ( As per Secti 1%, Extension ( As per Secti 1% |
| `F_Amount_` | id/text | 100% | 882 | e.g. $ 52,917.51, $ 3,300,000.00, $ 235,378.00 |
| `Vendor` | text | 100% | 461 | e.g. MYERS-ORLEANS CHEV-BUI, EGIS CANADA LTD, OTTAWA D SQUARED CONST |
| `Non_Competitive__Rationale` | cat | 17% | 8 | Section 22 (1) (D) 57%, Section 22 (1) (C) 12%, Section 22 (1) (A) 12%, Section 22 (1) (H) 11%, Section 22 (1) (F) 4%, Section 22 (1) (J) 2% |
| `ObjectId` | num | 100% | 907 | 1.00 · p25 228 · p50 454 · p95 862 · max 907  ██▇██▇██▇█▇██▇██ |

## Candidate questions

- Concentration in `Vendor` — which actors dominate? (join entity spine)

_profiled 2026-09-09 · `python3 tools/profile.py open_contracts_awarded_under_delegation_of_authority_for_jan_june_2024`_
