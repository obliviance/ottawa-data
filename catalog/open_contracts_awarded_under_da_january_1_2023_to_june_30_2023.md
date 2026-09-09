# Contracts awarded under DA  January 1 2023 to June 30 2023

`open_contracts_awarded_under_da_january_1_2023_to_june_30_2023` · shape **arcgis-hub** · source `open-ottawa`

- origin: <https://open.ottawa.ca/datasets/ottawa::contracts-awarded-under-da-january-1-2023-to-june-30-2023>
- fetched 2026-09-09 · **892 rows** · 10 columns
- geojson · licence: https://ottawa.ca/en/city-hall/open-transparent-and-accountable-government/open-

## Columns

| column | kind | non-null | distinct | summary |
| --- | --- | --- | --- | --- |
| `Item__` | num | 100% | 892 | 1.00 · p25 224 · p50 446 · p95 847 · max 892  ███▇██▇██▇██▇███ |
| `Contract` | id/text | 100% | 830 | e.g. 30023-92500-C01, 32123-91804-C01, 19423-98856-G01 |
| `Department` | cat | 100% | 14 | Infrastructure & Water S 40%, Public Works 17%, Finance and Corporate Se 16%, Planning, Real Estate &  9%, Emergency & Protective S 5%, Recreation, Cultural & F 5% |
| `Description` | id/text | 100% | 861 | e.g. Advisory services rela, Professional auditing , All labour, equipment  |
| `Professional__Consulting_Servic` | cat | 42% | 3 | PE = Specialized Experti 99%, CE = Specialized Experti 1%, CE = Consulting Expertis 0% |
| `Contract_Approval_Request_Type` | cat | 99% | 11 | Initial 63%, Amendment 21%, Extension 6%, Extension & Amendment 5%, Extension ( As per Secti 2%, Initial & Amendment 1% |
| `Amount` | id/text | 100% | 861 | e.g. $50,045.00 , $71,370.00 , $5,706,511.63  |
| `Vendor` | text | 100% | 502 | e.g. DILLON CONSULTING LIMI, BDO CANADA LLP, GEMMA PROPERTY SERVICE |
| `Non_Competitive_Rationale` | cat | 19% | 11 | Section 22 (1) (D) 50%, Section 22 (1) (B) 14%, Section 22 (1) (A) 10%, Section 22 (1) (H) 9%, Section 22 (1) (C) 8%, Section 22 (1) (E) 2% |
| `ObjectId` | num | 100% | 892 | 1.00 · p25 224 · p50 446 · p95 847 · max 892  ███▇██▇██▇██▇███ |

## Candidate questions

- Concentration in `Vendor` — which actors dominate? (join entity spine)

_profiled 2026-09-09 · `python3 tools/profile.py open_contracts_awarded_under_da_january_1_2023_to_june_30_2023`_
