# Ottawa Public Library Most Requested Titles 2023

`open_ottawa_public_library_most_requested_titles_2023` · shape **arcgis-hub** · source `open-ottawa`

- origin: <https://open.ottawa.ca/datasets/ottawa::ottawa-public-library-most-requested-titles-2023>
- fetched 2026-09-09 · **96,113 rows** · 14 columns
- csv · licence: https://ottawa.ca/en/city-hall/get-know-your-city/open-data#open-data-licence-ve

## Columns

| column | kind | non-null | distinct | summary |
| --- | --- | --- | --- | --- |
| `Item_Collection` | text | 100% | 105 | e.g. AEF, AENF, AESF |
| `Catalog_Id` | num | 100% | 95,680 | 10.00 · p25 716,777 · p50 1,137,836 · p95 1,530,845 · max 1,562,183  ▁▂▂▂▃▃▃▄▂▃▄▅▆▇▄█ |
| `Title` | id/text | 100% | 95,680 | e.g. BC. 1335090, BC. 1373611, BC. 1500302 |
| `Item_Title` | id/text | 100% | 86,021 | e.g. Lessons in chemistry /, Demon Copperhead : a n, The covenant of water  |
| `URL` | id/text | 100% | 95,680 | e.g. https://ottawa.biblioc, https://ottawa.biblioc, https://ottawa.biblioc |
| `ISBN` | text | 100% | 62,285 | e.g. 9.78E+12, 63251922, 9780802162175 (hardcov |
| `Author` | text | 93% | 46,755 | e.g. Garmus, Bonnie,, Kingsolver, Barbara,, Verghese, Abraham, |
| `Holds` | num | 100% | 343 | 1.00 · p25 1.00 · p50 2.00 · p95 19.00 · max 2,081  █▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁ |
| `Hold_Created_Year` | num | 100% | 1 | 2,023 · p25 2,023 · p50 2,023 · p95 2,023 · max 2,023   |
| `Audience` | cat | 100% | 3 | Adult 65%, Teen 30%, Children 5% |
| `Language` | cat | 100% | 11 | English 85%, French 13%, Chinese 1%, Spanish 0%, Russian 0%, Ukrainian 0% |
| `Catalog_Format` | cat | 100% | 3 | Print 95%, CD 3%, DVD 2% |
| `Genre` | cat | 100% | 5 | Fiction 58%, Nonfiction 34%, Mystery 3%, Music 3%, Movies 2% |
| `ObjectId` | num | 100% | 96,113 | 1.00 · p25 24,029 · p50 48,057 · p95 91,307 · max 96,113  █▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇ |

## Candidate questions

- Trend / seasonality of open_ottawa_public_library_most_requested_titles_2023 over `Hold_Created_Year`; structural breaks?

_profiled 2026-09-09 · `python3 tools/profile.py open_ottawa_public_library_most_requested_titles_2023`_
