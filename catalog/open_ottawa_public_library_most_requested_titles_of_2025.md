# Ottawa Public Library Most Requested Titles of 2025

`open_ottawa_public_library_most_requested_titles_of_2025` · shape **arcgis-hub** · source `open-ottawa`

- origin: <https://open.ottawa.ca/datasets/ottawa::ottawa-public-library-most-requested-titles-of-2025>
- fetched 2026-09-09 · **126,969 rows** · 15 columns
- csv · licence: https://ottawa.ca/en/city-hall/open-transparent-and-accountable-government/open-

## Columns

| column | kind | non-null | distinct | summary |
| --- | --- | --- | --- | --- |
| `Item_Collection` | text | 100% | 100 | e.g. JEGR, AEDVD, AEF |
| `Catalog_Id` | num | 100% | 126,504 | 34.00 · p25 776,380 · p50 1,212,189 · p95 1,669,687 · max 1,699,585  ▁▁▁▂▂▂▃▂▂▃▄▅▅▂▆█ |
| `Title` | id/text | 100% | 126,504 | e.g. BC.1619643, BC.1637591, BC.1611589 |
| `Item_Title` | id/text | 99% | 111,929 | e.g. The Cartoonists Club /, Yellowstone., The bright years : a n |
| `URL` | id/text | 100% | 126,504 | e.g. https://ottawa.biblioc, https://ottawa.biblioc, https://ottawa.biblioc |
| `ISBN` | id/text | 100% | 126,605 | e.g. 1338777211, 6319389001, 9781668061442 (hardcov |
| `Author` | text | 93% | 57,907 | e.g. Telgemeier, Raina., Damoff, Sarah,, Rawle, Aisling, |
| `Holds` | num | 100% | 415 | 1.00 · p25 1.00 · p50 2.00 · p95 21.00 · max 2,500  █▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁ |
| `Hold_Created_Year` | num | 100% | 1 | 2,025 · p25 2,025 · p50 2,025 · p95 2,025 · max 2,025   |
| `Audience` | cat | 99% | 2 | Adult 64%, Children/Teen 36% |
| `Language` | cat | 100% | 12 | English 83%, French 14%, Chinese 1%, Other 1%, Russian 0%, Spanish 0% |
| `Catalog_Format` | cat | 100% | 3 | Print 96%, AV 4%, Other 0% |
| `Genre` | cat | 100% | 4 | Non-Fiction 41%, Other 34%, Fiction 22%, Mystery 3% |
| `Object_ID` | num | 100% | 126,969 | 1.00 · p25 31,743 · p50 63,485 · p95 120,621 · max 126,969  ██▇█▇█▇█▇█▇█▇█▇█ |
| `ObjectId` | num | 100% | 126,969 | 1.00 · p25 31,743 · p50 63,485 · p95 120,621 · max 126,969  ██▇█▇█▇█▇█▇█▇█▇█ |

## Candidate questions

- Trend / seasonality of open_ottawa_public_library_most_requested_titles_of_2025 over `Hold_Created_Year`; structural breaks?

_profiled 2026-09-09 · `python3 tools/profile.py open_ottawa_public_library_most_requested_titles_of_2025`_
