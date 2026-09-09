# Library Loans Physical Material Circulation 2024

`open_library_loans_physical_material_circulation_2024` · shape **arcgis-hub** · source `open-ottawa`

- origin: <https://open.ottawa.ca/datasets/ottawa::library-loans-physical-material-circulation-2024>
- fetched 2026-09-09 · **1,111 rows** · 9 columns
- csv · licence: https://ottawa.ca/en/city-hall/open-transparent-and-accountable-government/open-

## Columns

| column | kind | non-null | distinct | summary |
| --- | --- | --- | --- | --- |
| `Branch_Code` | text | 100% | 37 | e.g. BH, CA, BE |
| `Branch` | text | 100% | 37 | e.g. Blackburn Hamlet, Carlingwood, Beaverbrook |
| `Profile_Code` | cat | 100% | 3 | ADULT 45%, J 35%, YA_17 19% |
| `Profile` | cat | 100% | 3 | Adult 45%, Juvenile 35%, Young Adult 19% |
| `Collection_Code` | cat | 100% | 17 | AEF 9%, AENF 9%, TEENEF 9%, JENF 8%, JEF 8%, AEM 8% |
| `Collection` | cat | 100% | 15 | Adult English Books On C 15%, Adult French Fiction 14%, Adult English Non-Fictio 9%, Teen English Fiction 9%, Juvenile Non-Fiction 8%, Juvenile Fiction 8% |
| `Number_of_Loan_Transactions` | num | 100% | 524 | 1.00 · p25 7.00 · p50 50.00 · p95 8,342 · max 47,111  █▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁ |
| `ObjectId` | text | 0% | 0 | e.g.  |
| `ObjectId2` | num | 100% | 1,111 | 1.00 · p25 278 · p50 556 · p95 1,056 · max 1,111  █▇█▇▇█▇█▇▇█▇▇█▇█ |

## Candidate questions

- (none templated)

_profiled 2026-09-09 · `python3 tools/profile.py open_library_loans_physical_material_circulation_2024`_
