# 2024 Contracts Awarded greater than 25,000 Jul – Dec

`open_2024_contracts_awarded_greater_than_25_000_jul_dec` · shape **arcgis-hub** · source `open-ottawa`

- origin: <https://open.ottawa.ca/datasets/ottawa::2024-contracts-awarded-greater-than-25000-jul-dec-2024>
- fetched 2026-09-09 · **904 rows** · 10 columns
- geojson · licence: https://ottawa.ca/en/city-hall/get-know-your-city/open-data#open-data-licence-ve

## Columns

| column | kind | non-null | distinct | summary |
| --- | --- | --- | --- | --- |
| `Item_` | num | 99% | 903 | 1.00 · p25 226 · p50 452 · p95 858 · max 903  █▇█▇▇█▇█▇▇█▇▇█▇█ |
| `Contract` | id/text | 100% | 876 | e.g. 24424-91842-C07, 24424-91843-G02, 24424-92587-P03 |
| `Department` | cat | 99% | 12 | Infrastructure & Water S 47%, Finance and Corporate Se 12%, Transit Services 11%, Public Works 9%, Recreation, Cultural & F 7%, Emergency & Protective S 4% |
| `Description` | id/text | 99% | 895 | e.g. Professional engineeri, Professional engineeri, Professional engineeri |
| `Professional_Consulting_Service` | cat | 40% | 3 | PE = Specialized Experti 99%, CE = Specialized Experti 0%, PR = Regulatory Requirem 0% |
| `Contract_Approval_Request_Type` | cat | 99% | 8 | Initial 63%, Amendment 24%, Extension 7%, Extension & Amendment 3%, Extension ( As per Secti 2%, Follow-On 1% |
| `Amount` | id/text | 99% | 879 | e.g. $25,124.00 , $46,791.80 , $1,530,951.40  |
| `Vendor` | text | 99% | 505 | e.g. STANTEC CONSULTING LTD, SIMPSON GUMPERTZ & HEG, PARSONS INC |
| `Non_Competitive_Rationale` | cat | 20% | 11 | Section 22 (1) (D) 50%, Section 22 (1) (A) 14%, Section 22 (1) (H) 11%, Section 22 (1) (C) 7%, Section 22 (1) (J) 6%, Section 22 (1) (F) 5% |
| `ObjectId` | num | 100% | 904 | 1.00 · p25 227 · p50 452 · p95 859 · max 904  █▇█▇█▇█▇▇█▇█▇█▇█ |

## Candidate questions

- Concentration in `Vendor` — which actors dominate? (join entity spine)

_profiled 2026-09-09 · `python3 tools/profile.py open_2024_contracts_awarded_greater_than_25_000_jul_dec`_
