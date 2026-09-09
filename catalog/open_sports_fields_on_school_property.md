# Sports Fields on School Property

`open_sports_fields_on_school_property` · shape **arcgis-hub** · source `open-ottawa`

- origin: <https://open.ottawa.ca/datasets/ottawa::sports-fields-on-school-property>
- fetched 2026-09-09 · **119 rows** · 26 columns
- csv · licence: https://ottawa.ca/en/city-hall/get-know-your-city/open-data#open-data-licence-ve

## Columns

| column | kind | non-null | distinct | summary |
| --- | --- | --- | --- | --- |
| `X` | num | 100% | 119 | -8,473,192 · p25 -8,437,296 · p50 -8,431,298 · p95 -8,403,568 · max -8,395,215  ▁▂▁▁▂▃▃▅█▃▆▃▁▂▃▁ |
| `Y` | num | 100% | 119 | 5,644,571 · p25 5,670,499 · p50 5,678,009 · p95 5,695,102 · max 5,697,968  ▂▂▁▂▁▂▄▂▃█▆▄▂▆▄▃ |
| `OBJECTID` | num | 100% | 119 | 1.00 · p25 30.50 · p50 60.00 · p95 113 · max 119  █▇█▇▇█▇█▇▇█▇▇█▇█ |
| `FACILITYID` | num | 100% | 119 | 36,275 · p25 36,304 · p50 36,336 · p95 36,392 · max 59,013  █▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁ |
| `BOARD` | cat | 100% | 3 | OCDSB 88%, OCCSB 11%, CÉCLFCE 1% |
| `SCHOOL_NAME` | text | 100% | 84 | e.g. Ridgemont High School, South Carleton High Sc, St. Paul High School |
| `ADDRESS` | text | 100% | 84 | e.g. 2597 prom. Alta Vista , 3673 rue McBean St, 2675 av. Draper Av |
| `FIELD_NAME` | text | 100% | 59 | e.g. Sports Field, Sports Field 03 (East), Sports Field 01 |
| `FIELD_NAME_FR` | text | 100% | 58 | e.g. Terrain de sport, Terrain de sport  03 (, Terrain de sport 01 |
| `REGULAR_USE_TYPE` | cat | 98% | 4 | soccer 57%, sportsfield 41%, soccer
 1%, sportfield 1% |
| `REGULAR_USE_TYPE_FR` | cat | 99% | 2 | terrain de sport 54%, soccer 46% |
| `FIELD_SIZE` | cat | 98% | 4 | full 56%, mini 43%, full
 1%, mini
 1% |
| `WIDTH` | num | 68% | 4 | 0.00 · p25 0.00 · p50 0.00 · p95 0.00 · max 60.00  █▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁ |
| `LENGTH` | num | 68% | 4 | 0.00 · p25 0.00 · p50 0.00 · p95 0.00 · max 100  █▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁ |
| `SHARED` | cat | 57% | 2 |   83%, yes/oui 17% |
| `SHAREDTYPE` | cat | 56% | 3 |   82%, softball 12%, soccer 6% |
| `POST_TYPE` | cat | 68% | 3 |   96%, none 2%, soccer 1% |
| `SCOREBOARD` | cat | 68% | 3 | no/non 59%,   40%, yes/oui 1% |
| `BLEACHERS` | cat | 68% | 3 | no/non 73%, yes/oui 16%,   11% |
| `PLAYERS_BENCHES` | cat | 68% | 2 | no/non 80%,   20% |
| `RUNNING_TRACK` | cat | 68% | 4 | no/non 60%, yes/oui 23%,   16%,  n 1% |
| `LIGHTS` | cat | 68% | 3 | no/non 83%, yes/oui 10%,   7% |
| `ACCESSIBLE` | cat | 2% | 1 | no/non 100% |
| `OPEN` | text | 0% | 0 | e.g.  |
| `MODIFIED_DATE` | date | 8% | 10 | 2014-05-29 → 2023-03-01, 3 gaps >30d |
| `CREATED_DATE` | date | 2% | 2 | 2023-03-01 → 2023-03-01 |

## Candidate questions

- (none templated)

_profiled 2026-09-09 · `python3 tools/profile.py open_sports_fields_on_school_property`_
