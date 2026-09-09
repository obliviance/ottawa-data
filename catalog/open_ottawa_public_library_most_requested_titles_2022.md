# Ottawa Public Library Most Requested Titles 2022

`open_ottawa_public_library_most_requested_titles_2022` · shape **arcgis-hub** · source `open-ottawa`

- origin: <https://open.ottawa.ca/datasets/ottawa::ottawa-public-library-most-requested-titles-2022>
- fetched 2026-09-09 · **57,050 rows** · 14 columns
- csv · licence: https://ottawa.ca/en/city-hall/get-know-your-city/open-data#open-data-licence-ve

## Columns

| column | kind | non-null | distinct | summary |
| --- | --- | --- | --- | --- |
| `Collection` | cat | 100% | 16 | AENF 53%, AEF 15%, JEF 6%, AFNF 5%, AEM 5%, TEENEF 4% |
| `Catalogue` | num | 100% | 57,032 | 10.00 · p25 670,594 · p50 1,079,354 · p95 1,382,292 · max 1,462,972  ▁▂▂▁▂▂▃▃▃▁▃▄▅▆█▄ |
| `Title` | id/text | 100% | 57,032 | e.g. BC. 1035012, BC. 1335090, BC. 1334733 |
| `Item_Title` | id/text | 99% | 55,584 | e.g. The seven husbands of , Lessons in chemistry /, The myth of normal : t |
| `URL` | id/text | 100% | 57,032 | e.g. https://ottawa.biblioc, https://ottawa.biblioc, https://ottawa.biblioc |
| `ISBN` | id/text | 100% | 57,034 | e.g. 1501139231, 9780385697378, 0735278369 |
| `Author` | text | 92% | 33,781 | e.g. Reid, Taylor Jenkins,, Garmus, Bonnie,, Maté, Gabor, |
| `Holds` | num | 100% | 325 | 1.00 · p25 1.00 · p50 2.00 · p95 24.00 · max 1,314  █▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁ |
| `Hold_Year` | num | 100% | 1 | 2,022 · p25 2,022 · p50 2,022 · p95 2,022 · max 2,022   |
| `Audience` | cat | 100% | 3 | Adult 87%, Children 9%, Teen 5% |
| `Language` | cat | 100% | 2 | eng 89%, fra 11% |
| `Format` | cat | 100% | 3 | Print 97%, DVD 2%, CD 0% |
| `Genre` | cat | 100% | 6 | Nonfiction 58%, Fiction 32%, Mystery 5%, Science Fiction 3%, Movies 2%, Music 0% |
| `FID` | num | 100% | 57,050 | 1.00 · p25 14,263 · p50 28,526 · p95 54,198 · max 57,050  ██▇█▇█▇██▇█▇█▇██ |

## Candidate questions

- Trend / seasonality of open_ottawa_public_library_most_requested_titles_2022 over `Hold_Year`; structural breaks?

_profiled 2026-09-09 · `python3 tools/profile.py open_ottawa_public_library_most_requested_titles_2022`_
