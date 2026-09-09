# Elections 2010 Voting Places

`open_elections_2010_voting_places` · shape **arcgis-hub** · source `open-ottawa`

- origin: <https://open.ottawa.ca/datasets/ottawa::elections-2010-voting-places>
- fetched 2026-09-09 · **554 rows** · 11 columns
- csv · licence: https://ottawa.ca/en/city-hall/get-know-your-city/open-data#open-data-licence-ve

## Columns

| column | kind | non-null | distinct | summary |
| --- | --- | --- | --- | --- |
| `FID` | num | 100% | 554 | 1.00 · p25 139 · p50 278 · p95 526 · max 554  ██▇█▇█▇██▇█▇█▇██ |
| `LOC_EN` | id/text | 100% | 497 | e.g. Ron Kolbus Lakeside Ce, Woodroffe High School, Brewer Pool |
| `LOC_FR` | id/text | 100% | 490 | e.g. Centre Ron-Kolbus-Lake, École secondaire Woodr, Piscine Brewer |
| `ADDR_EN` | id/text | 100% | 501 | e.g. 102 Greenview Avenue, 2410 Georgina Drive, 100 Brewer Way |
| `ADDR_FR` | id/text | 100% | 501 | e.g. 102, avenue Greenview, 2410, promenade Georgi, 100, voie Brewer |
| `WARD_NUM` | num | 100% | 23 | 1.00 · p25 8.00 · p50 13.00 · p95 22.00 · max 23.00  ▅▂▄▂▆▇▃█▅▄▇▄▅▅▃▅ |
| `VOT_AREA` | num | 100% | 29 | 0.00 · p25 3.00 · p50 6.00 · p95 18.00 · max 28.00  ▇█▆▅▃▅▄▃▂▂▂▁▁▁▁▁ |
| `DAY_EN` | cat | 100% | 3 | Voting Day 59%, ADV Day 1 21%, ADV Day 2 20% |
| `DAY_FR` | cat | 100% | 3 | Jour de scrutin 59%, Jour par anticipation 1 21%, Jour par anticipation 2 20% |
| `WARD_EN` | cat | 100% | 23 | BAY 9%, RIDEAU-VANIER 7%, ALTA VISTA 7%, RIDEAU-ROCKCLIFFE 7%, COLLEGE 7%, SOMERSET 6% |
| `WARD_FR` | cat | 100% | 23 | BAIE 9%, RIDEAU-VANIER 7%, ALTA VISTA 7%, RIDEAU-ROCKCLIFFE 7%, COLLÈGE 7%, SOMERSET 6% |

## Candidate questions

- (none templated)

_profiled 2026-09-09 · `python3 tools/profile.py open_elections_2010_voting_places`_
