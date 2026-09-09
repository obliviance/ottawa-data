# 2025 Contracts Awarded greater than 25,000 Jan - Jun

`open_2025_contracts_awarded_greater_than_25_000_jan_jun` · shape **arcgis-hub**

- origin: <https://open.ottawa.ca/datasets/ottawa::2025-contracts-awarded-greater-than-25000-jan-jun>
- fetched 2026-09-09 · **963 rows** · 10 columns
- geojson · licence: https://ottawa.ca/en/city-hall/open-transparent-and-accountable-government/open-

## Columns

| column | kind | non-null | distinct | summary |
| --- | --- | --- | --- | --- |
| `Item__` | num | 100% | 963 | 1.00 · p25 242 · p50 482 · p95 915 · max 963  █▇▇▇▇▇▇█▇▇▇▇▇▇▇█ |
| `Contract` | id/text | 100% | 953 | e.g. 00123-91842-C02, 00123-92500-C08, 00123-92593-C03 |
| `Department` | cat | 100% | 14 | Infrastructure & Water S 44%, Finance and Corporate Se 13%, Transit Services 11%, Public Works 11%, Recreation, Cultural & F 7%, Planning, Development an 4% |
| `Description` | id/text | 100% | 960 | e.g. Professional engineeri, Professional engineeri, Professional engineeri |
| `Professional_Consulting_Services` | cat | 41% | 2 | PE = Specialized Experti 100%, CE = Specialized Experti 0% |
| `Contract_Approval_Request_Type` | cat | 99% | 8 | Initial 66%, Amendment 23%, Extension 6%, Extension & Amendment 3%, Extension ( As per Secti 1%, Follow-On 1% |
| `Amount` | num | 100% | 943 | 25,000 · p25 52,242 · p50 108,263 · p95 2,958,240 · max 214,170,900  █▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁ |
| `Vendor` | text | 100% | 516 | e.g. J L RICHARDS AND ASSOC, EXP SERVICES INC, ARCADIS PROFESSIONAL S |
| `Non_Competitive_Rationale` | cat | 17% | 12 | Section 22 (1) (D) 46%, Section 22 (1) (A) 18%, Section 22 (1) (H) 16%, Section 22 (1) (J) 6%, Section 22 (1) (C) 5%, Section 22 (1) (B) 3% |
| `FID` | num | 100% | 963 | 1.00 · p25 242 · p50 482 · p95 915 · max 963  █▇▇▇▇▇▇█▇▇▇▇▇▇▇█ |

## Candidate questions

- Concentration in `Vendor` — which actors dominate? (join entity spine)

_profiled 2026-09-09 · `python3 tools/profile.py open_2025_contracts_awarded_greater_than_25_000_jan_jun`_
