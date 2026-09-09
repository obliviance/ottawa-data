# Library Loans Physical Material Circulation 2025

`open_library_loans_physical_material_circulation_2025` · shape **arcgis-hub** · source `open-ottawa`

- origin: <https://open.ottawa.ca/datasets/ottawa::library-loans-physical-material-circulation-2025>
- fetched 2026-09-09 · **1,112 rows** · 9 columns
- csv · licence: https://ottawa.ca/en/city-hall/open-transparent-and-accountable-government/open-

## Columns

| column | kind | non-null | distinct | summary |
| --- | --- | --- | --- | --- |
| `Branch_Code` | text | 100% | 37 | e.g. AL, BE, EP |
| `Branch` | text | 97% | 36 | e.g. Alta Vista, Beaverbrook, Emerald Plaza |
| `Profile_Code` | cat | 100% | 3 | ADULT 46%, J 35%, YA_17 19% |
| `Profile` | cat | 100% | 3 | Adult 46%, Juvenile 35%, Young Adult 19% |
| `Collection_Code` | cat | 100% | 17 | AEF 9%, TEENEF 9%, AENF 9%, JEF 8%, JENF 8%, AEM 8% |
| `Collection` | cat | 100% | 17 | Adult eng fiction 9%, Teen eng fiction 9%, Adult eng non-fiction 9%, Juv eng fiction 8%, Juv eng non-fiction 8%, Adult eng mystery 8% |
| `Number_of_Loan_Transactions` | num | 100% | 511 | 1.00 · p25 6.00 · p50 45.50 · p95 7,598 · max 44,379  █▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁ |
| `ObjectID` | num | 100% | 1,112 | 1.00 · p25 279 · p50 556 · p95 1,056 · max 1,112  █▇█▇█▇█▇▇█▇█▇█▇█ |
| `ObjectId2` | num | 100% | 1,112 | 1.00 · p25 279 · p50 556 · p95 1,056 · max 1,112  █▇█▇█▇█▇▇█▇█▇█▇█ |

## Candidate questions

- (none templated)

_profiled 2026-09-09 · `python3 tools/profile.py open_library_loans_physical_material_circulation_2025`_
