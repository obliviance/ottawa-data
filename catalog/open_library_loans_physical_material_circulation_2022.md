# Library Loans Physical Material Circulation 2022

`open_library_loans_physical_material_circulation_2022` · shape **arcgis-hub** · source `open-ottawa`

- origin: <https://open.ottawa.ca/datasets/ottawa::library-loans-physical-material-circulation-2022>
- fetched 2026-09-09 · **1,122 rows** · 9 columns
- csv · licence: https://ottawa.ca/en/city-hall/get-know-your-city/open-data#open-data-licence-ve

## Columns

| column | kind | non-null | distinct | summary |
| --- | --- | --- | --- | --- |
| `Branch_Code` | text | 100% | 37 | e.g. BH, BE, AL |
| `Branch` | text | 100% | 37 | e.g. Blackburn Hamlet, Beaverbrook, Alta Vista |
| `Profile_Code` | cat | 100% | 3 | ADULT 45%, J 36%, YA_17 18% |
| `Profile` | cat | 100% | 3 | Adult 45%, Juvenile 36%, Young Adult 18% |
| `Collection_Code` | cat | 100% | 17 | AEF 9%, TEENEF 9%, AENF 9%, JEF 8%, AEM 8%, JENF 8% |
| `Collection` | cat | 100% | 17 | Adult English Fiction 9%, Teen English Fiction 9%, Adult English Non-Fictio 9%, Juvenile Fiction 8%, Adult English Mystery 8%, Juvenile Non-Fiction 8% |
| `Number_of_Loan_Transactions` | num | 100% | 527 | 1.00 · p25 7.00 · p50 48.00 · p95 8,337 · max 48,635  █▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁ |
| `FID` | num | 100% | 1,122 | 1.00 · p25 281 · p50 562 · p95 1,066 · max 1,122  █▇▇▇▇▇▇▇▇▇▇▇▇▇▇█ |
| `FID2` | num | 100% | 1,122 | 1.00 · p25 281 · p50 562 · p95 1,066 · max 1,122  █▇▇▇▇▇▇▇▇▇▇▇▇▇▇█ |

## Candidate questions

- (none templated)

_profiled 2026-09-09 · `python3 tools/profile.py open_library_loans_physical_material_circulation_2022`_
