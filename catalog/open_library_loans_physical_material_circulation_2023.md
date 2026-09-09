# Library Loans Physical Material Circulation 2023

`open_library_loans_physical_material_circulation_2023` · shape **arcgis-hub** · source `open-ottawa`

- origin: <https://open.ottawa.ca/datasets/ottawa::library-loans-physical-material-circulation-2023>
- fetched 2026-09-09 · **1,139 rows** · 8 columns
- csv · licence: https://ottawa.ca/en/city-hall/get-know-your-city/open-data#open-data-licence-ve

## Columns

| column | kind | non-null | distinct | summary |
| --- | --- | --- | --- | --- |
| `Branch_Code` | text | 100% | 37 | e.g. BH, CA, EA |
| `Branch` | text | 100% | 37 | e.g. Blackburn Hamlet, Carlingwood, Elmvale Acres |
| `Profile_Code` | cat | 100% | 3 | ADULT 45%, J 35%, YA_17 20% |
| `Profile` | cat | 100% | 3 | Adult 45%, Juvenile 35%, Young Adult 20% |
| `Collection_Code` | cat | 100% | 17 | AEF 9%, AENF 9%, TEENEF 9%, JEF 8%, JENF 8%, AEM 8% |
| `Collection` | cat | 100% | 16 | Adult French Fiction 14%, Adult English Fiction 9%, Adult English Non-Fictio 9%, Teen English Fiction 9%, Juvenile Fiction 8%, Juvenile Non-Fiction 8% |
| `Number_of_Loan_Transactions` | num | 100% | 513 | 1.00 · p25 6.00 · p50 45.00 · p95 8,061 · max 48,778  █▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁ |
| `ObjectId` | num | 100% | 1,139 | 1.00 · p25 286 · p50 570 · p95 1,082 · max 1,139  █▇▇▇▇▇▇█▇▇▇▇▇▇▇█ |

## Candidate questions

- (none templated)

_profiled 2026-09-09 · `python3 tools/profile.py open_library_loans_physical_material_circulation_2023`_
