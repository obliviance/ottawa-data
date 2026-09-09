# Ottawa Public Library Most Requested Titles 2024

`open_ottawa_public_library_most_requested_titles_2024` · shape **arcgis-hub** · source `open-ottawa`

- origin: <https://open.ottawa.ca/datasets/ottawa::ottawa-public-library-most-requested-titles-2024>
- fetched 2026-09-09 · **135,036 rows** · 15 columns
- csv · licence: https://ottawa.ca/en/city-hall/open-transparent-and-accountable-government/open-

## Columns

| column | kind | non-null | distinct | summary |
| --- | --- | --- | --- | --- |
| `Item_Collection` | text | 100% | 100 | e.g. AEF, AEM, AENF |
| `Catalog_Id` | num | 100% | 134,443 | 34.00 · p25 735,206 · p50 1,157,048 · p95 1,592,063 · max 1,623,985  ▁▁▁▂▂▂▃▃▁▃▄▅▅▄▂█ |
| `Title` | id/text | 100% | 134,443 | e.g. BC. 1546810, BC. 1589584, BC. 1548167 |
| `Item_Title` | id/text | 99% | 119,684 | e.g. The women /, The grey wolf /, The anxious generation |
| `URL` | id/text | 100% | 134,443 | e.g. https://ottawa.biblioc, https://ottawa.biblioc, https://ottawa.biblioc |
| `ISBN` | id/text | 100% | 134,582 | e.g. 9781250178633 (hardcov, 9781250328137 (hardcov, 0593655036 |
| `Author` | text | 93% | 61,423 | e.g. Hannah, Kristin,, Penny, Louise,, Haidt, Jonathan, |
| `Holds` | num | 100% | 400 | 1.00 · p25 1.00 · p50 2.00 · p95 22.00 · max 2,568  █▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁ |
| `Hold_Created_Year` | num | 100% | 1 | 2,024 · p25 2,024 · p50 2,024 · p95 2,024 · max 2,024   |
| `Audience` | cat | 100% | 3 | Adult 64%, Teen 31%, Children 5% |
| `Language` | cat | 100% | 11 | English 83%, French 14%, Chinese 1%, Spanish 0%, Russian 0%, Arabic 0% |
| `Catalog_Format` | cat | 100% | 3 | Print 96%, CD 2%, DVD 2% |
| `Genre` | cat | 100% | 5 | Fiction 57%, Nonfiction 36%, Mystery 3%, Music 2%, Movies 2% |
| `ObjectId` | text | 0% | 0 | e.g.  |
| `ObjectId2` | num | 100% | 135,036 | 1.00 · p25 33,760 · p50 67,518 · p95 128,284 · max 135,036  ███▇██▇██▇██▇███ |

## Candidate questions

- Trend / seasonality of open_ottawa_public_library_most_requested_titles_2024 over `Hold_Created_Year`; structural breaks?

_profiled 2026-09-09 · `python3 tools/profile.py open_ottawa_public_library_most_requested_titles_2024`_
