# Ball Diamonds School

`open_ball_diamonds_school` · shape **arcgis-hub** · source `open-ottawa`

- origin: <https://open.ottawa.ca/datasets/ottawa::ball-diamonds-school>
- fetched 2026-09-09 · **74 rows** · 15 columns
- csv · licence: https://ottawa.ca/en/city-hall/get-know-your-city/open-data#open-data-licence-ve

## Columns

| column | kind | non-null | distinct | summary |
| --- | --- | --- | --- | --- |
| `X` | num | 100% | 74 | -8,483,987 · p25 -8,447,284 · p50 -8,433,474 · p95 -8,411,619 · max -8,406,521  ▁▁▁▁▁▁▂█▂▃▄▃▂▆▃▂ |
| `Y` | num | 100% | 74 | 5,641,555 · p25 5,668,670 · p50 5,677,503 · p95 5,693,870 · max 5,698,034  ▁▁▃▁▂▁▄▆▅▆█▇▃▅▆▂ |
| `OBJECTID` | num | 100% | 74 | 1.00 · p25 19.25 · p50 37.50 · p95 70.35 · max 74.00  ██▆█▆█▆██▆█▆█▆██ |
| `FACILITYID` | num | 100% | 74 | 36,002 · p25 36,020 · p50 36,038 · p95 36,071 · max 59,007  █▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁ |
| `BOARD` | cat | 100% | 5 | OCDSB 81%, OCCSB 11%, CÉCLFCE 5%, OCCSB
 1%, CECCE 1% |
| `SCHOOL_NAME` | text | 100% | 57 | e.g. Queen Elizabeth Public, Regina Street Public S, Robert Hopkins Public  |
| `ADDRESS` | text | 100% | 56 | e.g. 689 boul. St. Laurent , 2599 rue Regina St, 2011 av. Glenfern Ave |
| `DIAMOND_TYPE` | cat | 100% | 2 | softball 95%, baseball 5% |
| `DIAMOND_TYPE_FR` | cat | 100% | 2 | balle molle 95%, baseball 5% |
| `FIELD_NAME` | cat | 100% | 24 | Ball Diamond 38%, Ball Diamond 02 14%, Ball Diamond 01 11%, Ball Diamond - Softball 7%, Ball Diamond - West 3%, Ball Diamond - East 3% |
| `FIELD_NAME_FR` | cat | 100% | 22 | Terrain de balle 38%, Terrain de balle 02 14%, Terrain de balle 01 12%, Terrain de balle - Balle 8%, Terrain de balle - Ouest 3%, Terrain de balle - Est 3% |
| `ACCESSIBLE` | cat | 2% | 1 | no/non 100% |
| `OPEN` | text | 0% | 0 | e.g.  |
| `MODIFIED_DATE` | date | 6% | 5 | 2016-09-08 → 2023-03-01, 2 gaps >30d |
| `CREATED_DATE` | date | 2% | 2 | 2023-03-01 → 2023-03-01 |

## Candidate questions

- (none templated)

_profiled 2026-09-09 · `python3 tools/profile.py open_ball_diamonds_school`_
