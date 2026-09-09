# Sports Fields

`open_sports_fields` · shape **arcgis-hub** · source `open-ottawa`

- origin: <https://open.ottawa.ca/datasets/ottawa::sports-fields>
- fetched 2026-09-09 · **526 rows** · 26 columns
- csv · licence: https://ottawa.ca/en/city-hall/get-know-your-city/open-data#open-data-licence-ve

## Columns

| column | kind | non-null | distinct | summary |
| --- | --- | --- | --- | --- |
| `X` | num | 100% | 526 | -8,484,162 · p25 -8,442,831 · p50 -8,429,684 · p95 -8,400,908 · max -8,393,594  ▂▁▁▂▁▄▄▄▆█▅▆▅▃▃▂ |
| `Y` | num | 100% | 526 | 5,632,243 · p25 5,665,626 · p50 5,674,409 · p95 5,695,974 · max 5,703,279  ▁▁▁▁▁▁▅▇▄█▅▄▃▅▅▁ |
| `OBJECTID` | num | 100% | 526 | 1.00 · p25 132 · p50 264 · p95 500 · max 526  █████▇████▇█████ |
| `PARK_ID` | num | 100% | 278 | 2.00 · p25 449 · p50 992 · p95 2,466 · max 2,657  ▅▅▅▅▅▄█▅▂▅▃▁▁▁▄▃ |
| `FACILITYID` | num | 100% | 526 | 3,851 · p25 34,106 · p50 34,246 · p95 36,272 · max 58,867  ▁▁▁▁▁▁▁▁█▂▁▁▁▁▁▁ |
| `REGULAR_USE_TYPE` | cat | 100% | 8 | soccer 83%, general open field 6%, football 6%, ultimate 2%, multi-use 1%, cricket 1% |
| `REGULAR_USE_TYPE_FR` | cat | 100% | 8 | soccer 83%, terrain ouvert général 6%, football 6%, ultime 2%, polyvalent 1%, cricket 1% |
| `FIELD_NAME` | text | 100% | 154 | e.g. Sports Field - Multi-u, Sports Field - Mini, Sports Field - Mini Ea |
| `FIELD_NAME_FR` | text | 100% | 155 | e.g. Terrain de sport - Pol, Terrain de sport - Min, Terrain de sport - Min |
| `POST_TYPE` | cat | 100% | 6 | soccer 80%, none 12%, both 7%, football 1%, field hockey 0%, rugby 0% |
| `FIELD_SIZE` | cat | 100% | 5 | full 45%, mini 45%, int 9%, interm 1%, Int 0% |
| `WIDTH` | num | 100% | 46 | 15.00 · p25 40.00 · p50 44.00 · p95 65.00 · max 155  ▁▂█▄▂▄▁▁▁▁▁▁▁▁▁▁ |
| `LENGTH` | num | 100% | 68 | 25.00 · p25 55.00 · p50 70.00 · p95 110 · max 142  ▁▁▂▃█▂▃▁▄▂▅▂▁▁▁▁ |
| `SCOREBOARD` | cat | 100% | 2 | no/non 97%, yes/oui 3% |
| `BLEACHERS` | cat | 100% | 2 | no/non 85%, yes/oui 15% |
| `PLAYERS_BENCHES` | cat | 100% | 2 | no/non 95%, yes/oui 5% |
| `RUNNING_TRACK` | cat | 100% | 2 | no/non 98%, yes/oui 2% |
| `LIGHTS` | cat | 100% | 2 | no/non 91%, yes/oui 9% |
| `ACCESSIBLE` | cat | 100% | 1 | no/non 100% |
| `OPEN` | text | 0% | 0 | e.g.  |
| `MODIFIED_DATE` | date | 100% | 206 | 2018-01-18 → 2022-09-07, 11 gaps >30d |
| `CREATED_DATE` | date | 14% | 74 | 2014-07-23 → 2022-09-07, 25 gaps >30d |
| `PARKNAME` | text | 100% | 278 | e.g. Ottawa Business Park, Watershield Park, Balena Park |
| `PARKNAME_FR` | text | 100% | 278 | e.g. Parc d'Affaires d'Otta, Parc Watershield, Parc Balena |
| `PARKADDRESS` | text | 100% | 278 | e.g. 3035 Conroy Road, Otta, 125 Watershield Ridge,, 1640 Devon Street, Ott |
| `PARKADDRESS_FR` | text | 100% | 278 | e.g. 3035, chemin Conroy, O, 125, côte Watershield,, 1640, rue Devon, Ottaw |

## Candidate questions

- Trend / seasonality of open_sports_fields over `MODIFIED_DATE`; structural breaks?

_profiled 2026-09-09 · `python3 tools/profile.py open_sports_fields`_
