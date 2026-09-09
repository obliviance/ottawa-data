# Library Loans Physical Material Circulation 2021

`open_library_loans_physical_material_circulation_2021` · shape **arcgis-hub** · source `open-ottawa`

- origin: <https://open.ottawa.ca/datasets/ottawa::library-loans-physical-material-circulation-2021>
- fetched 2026-09-09 · **1,083 rows** · 8 columns
- csv · licence: https://ottawa.ca/en/city-hall/get-know-your-city/open-data#open-data-licence-ve

## Columns

| column | kind | non-null | distinct | summary |
| --- | --- | --- | --- | --- |
| `Branch_Code` | text | 100% | 37 | e.g. AL, BE, BH |
| `Branch` | text | 100% | 37 | e.g. Alta Vista, Beaverbrook, Blackburn Hamlet |
| `Profile_Code` | cat | 100% | 3 | ADULT 47%, J 36%, YA_17 18% |
| `Profile` | cat | 100% | 3 | Adult 47%, Juvenile 36%, Young Adult 18% |
| `Collection_Code` | cat | 100% | 17 | AENF 9%, TEENEF 9%, AEF 9%, JEF 8%, JENF 8%, AEM 8% |
| `Collection` | cat | 100% | 17 | Adult English Non-Fictio 9%, Teen English Fiction 9%, Adult English Fiction 9%, Juvenile Fiction 8%, Juvenile Non-Fiction 8%, Adult English Mystery 8% |
| `Number_of_Loan_Transactions` | num | 100% | 504 | 1.00 · p25 7.00 · p50 50.00 · p95 7,872 · max 50,017  █▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁ |
| `FID` | num | 100% | 1,083 | 1.00 · p25 272 · p50 542 · p95 1,029 · max 1,083  ██▇██▇██▇█▇██▇██ |

## Candidate questions

- (none templated)

_profiled 2026-09-09 · `python3 tools/profile.py open_library_loans_physical_material_circulation_2021`_
