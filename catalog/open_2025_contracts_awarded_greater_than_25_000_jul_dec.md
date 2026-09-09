# 2025 Contracts Awarded greater than 25,000 Jul - Dec

`open_2025_contracts_awarded_greater_than_25_000_jul_dec` · shape **arcgis-hub**

- origin: <https://open.ottawa.ca/datasets/ottawa::2025-contracts-awarded-greater-than-25000-jul-dec>
- fetched 2026-09-09 · **917 rows** · 10 columns
- geojson · licence: https://ottawa.ca/en/city-hall/open-transparent-and-accountable-government/open-

## Columns

| column | kind | non-null | distinct | summary |
| --- | --- | --- | --- | --- |
| `Item` | num | 100% | 917 | 1.00 · p25 230 · p50 459 · p95 871 · max 917  █▇▇█▇▇▇█▇▇▇█▇▇▇█ |
| `Contract` | id/text | 100% | 906 | e.g. 00124-74512-S01, 00124-91347-T02, 00125-15000-T01 |
| `Department` | cat | 100% | 14 | Infrastructure & Water S 45%, Finance and Corporate Se 12%, Transit Services 11%, Recreation, Cultural & F 9%, Public Works 7%, Emergency & Protective S 4% |
| `Description` | id/text | 100% | 913 | e.g. Standing offer to prov, All labour, equipment , All labour, material a |
| `Professional_Consulting_Services` | cat | 39% | 2 | PE = Specialized Experti 100%, PR = Regulatory Requirem 0% |
| `Contract_Approval_Request_Type` | cat | 99% | 8 | Initial 65%, Amendment 22%, Extension 7%, Extension & Amendment 2%, Extension ( As per Secti 1%, Follow-On 1% |
| `Amount` | id/text | 100% | 897 | e.g. $1,155,962.71 , $125,492.29 , $227,755.00  |
| `Vendor` | text | 100% | 506 | e.g. P MUNRO GROUP INC.,B G, IN DEPTH CONTRACTING, ELIOT ROOFING LTD. |
| `Non_Competitive_Rationale` | cat | 19% | 9 | Section 22 (1) (D) 48%, Section 22 (1) (A) 17%, Section 22 (1) (C) 11%, Section 22 (1) (H) 11%, Section 22 (1) (J) 7%, Section 23 2% |
| `ObjectId` | num | 100% | 917 | 1.00 · p25 230 · p50 459 · p95 871 · max 917  █▇▇█▇▇▇█▇▇▇█▇▇▇█ |

## Candidate questions

- Concentration in `Vendor` — which actors dominate? (join entity spine)

_profiled 2026-09-09 · `python3 tools/profile.py open_2025_contracts_awarded_greater_than_25_000_jul_dec`_
