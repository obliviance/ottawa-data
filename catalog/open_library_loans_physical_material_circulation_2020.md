# Library Loans Physical Material Circulation 2020

`open_library_loans_physical_material_circulation_2020` · shape **arcgis-hub** · source `open-ottawa`

- origin: <https://open.ottawa.ca/datasets/ottawa::library-loans-physical-material-circulation-2020>
- fetched 2026-09-09 · **1,069 rows** · 8 columns
- csv · licence: https://ottawa.ca/en/city-hall/get-know-your-city/open-data#open-data-licence-ve

## Columns

| column | kind | non-null | distinct | summary |
| --- | --- | --- | --- | --- |
| `Trans_Stat_Station_Library` | text | 100% | 37 | e.g. AL, BE, CP |
| `Station_Library_Name` | text | 100% | 37 | e.g. Alta Vista, Beaverbrook, Carp |
| `Trans_Stat_User_Profile_Name` | cat | 100% | 3 | ADULT 48%, J 38%, YA_17 14% |
| `User_Profile_Name` | cat | 100% | 3 | Adult 48%, Juvenile 38%, Young Adult 14% |
| `Trans_Stat_Home_Location` | cat | 100% | 17 | AENF 9%, AEF 9%, TEENEF 8%, JEF 8%, JENF 8%, AEM 8% |
| `column5` | cat | 100% | 17 | Adult English Non-Fictio 9%, Adult English Fiction 9%, Teen English Fiction 8%, Juvenile Fiction 8%, Juvenile Non-Fiction 8%, Adult English Mystery 8% |
| `Number_of_Statistical_Transacti` | num | 100% | 462 | 1.00 · p25 5.00 · p50 38.00 · p95 5,584 · max 44,754  █▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁ |
| `FID` | num | 100% | 1,069 | 1.00 · p25 268 · p50 535 · p95 1,016 · max 1,069  ████▇███▇███▇███ |

## Candidate questions

- (none templated)

_profiled 2026-09-09 · `python3 tools/profile.py open_library_loans_physical_material_circulation_2020`_
