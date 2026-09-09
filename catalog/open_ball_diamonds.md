# Ball Diamonds

`open_ball_diamonds` · shape **arcgis-hub** · source `open-ottawa`

- origin: <https://open.ottawa.ca/datasets/ottawa::ball-diamonds>
- fetched 2026-09-09 · **281 rows** · 31 columns
- csv · licence: https://ottawa.ca/en/city-hall/get-know-your-city/open-data#open-data-licence-ve

## Columns

| column | kind | non-null | distinct | summary |
| --- | --- | --- | --- | --- |
| `X` | num | 100% | 281 | -8,483,346 · p25 -8,435,484 · p50 -8,425,761 · p95 -8,400,590 · max -8,386,438  ▁▁▁▁▁▃▃▅█▆▇▄▃▃▁▁ |
| `Y` | num | 100% | 281 | 5,632,254 · p25 5,668,961 · p50 5,678,377 · p95 5,695,847 · max 5,702,959  ▁▁▁▁▁▁▂▃▂▄█▄▄▃▃▁ |
| `OBJECTID` | num | 100% | 281 | 1.00 · p25 71.00 · p50 141 · p95 267 · max 281  ██▇█▇█▇█▇█▇█▇█▇█ |
| `PARK_ID` | num | 100% | 208 | 4.00 · p25 300 · p50 589 · p95 1,331 · max 2,612  ▇▇▇█▆▅▅▅▂▁▁▁▁▁▁▁ |
| `FACILITYID` | num | 100% | 281 | 3,742 · p25 4,059 · p50 33,072 · p95 33,216 · max 53,539  ▃▁▁▁▁▁▁▁▁█▁▁▁▁▁▁ |
| `DIAMOND_TYPE` | cat | 100% | 3 | softball 78%, baseball 12%, T-Ball 10% |
| `DIAMOND_TYPE_FR` | cat | 100% | 3 | balle molle 78%, baseball 12%, tee ball 10% |
| `FIELD_NAME` | text | 100% | 92 | e.g. Ronald Warren Ball Dia, Ball Diamond, Ball Diamond 01 |
| `FIELD_NAME_FR` | text | 100% | 88 | e.g. Terrain de balle Ronal, Terrain de balle, Terrain de balle 01 |
| `BACKSTOP` | cat | 100% | 4 | baseball 81%, standard 15%, other 4%, none 0% |
| `CENTREFIELD_LENGTH` | num | 100% | 58 | 20.00 · p25 64.00 · p50 70.00 · p95 100 · max 135  ▁▁▁▁▂▃█▇▂▂▁▁▁▁▁▁ |
| `RIGHTFIELD_LENGTH` | num | 100% | 50 | 20.00 · p25 60.00 · p50 65.00 · p95 90.00 · max 105  ▁▁▁▁▁▂▃▆▅█▃▂▁▁▁▁ |
| `WARNING_TRACK` | cat | 100% | 2 | no/non 74%, yes/oui 26% |
| `OUTFIELD_FENCE` | cat | 100% | 2 | no/non 57%, yes/oui 43% |
| `LINE_FENCE` | cat | 100% | 2 | no/non 58%, yes/oui 42% |
| `FENCED_DUGOUT` | cat | 100% | 2 | yes/oui 81%, no/non 19% |
| `SCOREBOARD` | cat | 100% | 2 | no/non 90%, yes/oui 10% |
| `IRRIGATION` | cat | 100% | 2 | no/non 93%, yes/oui 7% |
| `BLEACHERS` | cat | 100% | 2 | yes/oui 54%, no/non 46% |
| `SAFETY_NETTING` | cat | 99% | 2 | no/non 89%, yes/oui 11% |
| `PLAYERS_BENCHES` | cat | 100% | 2 | yes/oui 90%, no/non 10% |
| `LIGHTS` | cat | 100% | 2 | no/non 68%, yes/oui 32% |
| `BULL_PEN` | cat | 100% | 2 | no/non 92%, yes/oui 8% |
| `ACCESSIBLE` | cat | 100% | 2 | no/non 100%, yes/oui 0% |
| `OPEN` | cat | 0% | 1 | no/non 100% |
| `MODIFIED_DATE` | date | 100% | 187 | 2015-12-15 → 2022-09-02, 6 gaps >30d |
| `CREATED_DATE` | date | 1% | 4 | 2016-03-09 → 2021-08-16, 2 gaps >30d |
| `PARKNAME` | text | 0% | 0 | e.g.  |
| `PARKNAME_FR` | text | 0% | 0 | e.g.  |
| `PARKADDRESS` | text | 0% | 0 | e.g.  |
| `PARKADDRESS_FR` | text | 0% | 0 | e.g.  |

## Candidate questions

- (none templated)

_profiled 2026-09-09 · `python3 tools/profile.py open_ball_diamonds`_
