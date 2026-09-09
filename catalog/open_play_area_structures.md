# Play Area - Structures

`open_play_area_structures` · shape **arcgis-hub** · source `open-ottawa` · **spatial**

- origin: <https://open.ottawa.ca/datasets/ottawa::play-area-structures>
- fetched 2026-09-09 · **1,719 rows** · 31 columns
- geojson · licence: https://ottawa.ca/en/city-hall/get-know-your-city/open-data#open-data-licence-ve

## Columns

| column | kind | non-null | distinct | summary |
| --- | --- | --- | --- | --- |
| `OBJECTID` | num | 100% | 1,719 | 1.00 · p25 430 · p50 860 · p95 1,633 · max 1,719  █▇█▇▇█▇█▇▇█▇▇█▇█ |
| `PARK_ID` | num | 100% | 706 | 2.00 · p25 385 · p50 914 · p95 2,519 · max 2,657  ▇▆█▅▆▆▆▄▁▅▃▁▁▁▅▅ |
| `FACILITYID` | num | 100% | 1,710 | 31,000 · p25 31,615 · p50 32,232 · p95 53,655 · max 58,879  █▁▂▁▁▁▁▁▁▁▁▁▁▁▁▁ |
| `NAME` | cat | 100% | 4 | play structure 54%, play area 45%, Children's Garden 0%, play strudture 0% |
| `NAME_FR` | cat | 100% | 4 | structure de jeux 54%, aire de jeux 46%, play structure 0%, Jardin et terrain de jeu 0% |
| `CLASS` | text | 100% | 28 | e.g. play structure, play area, swing |
| `CLASS_FR` | text | 100% | 33 | e.g. structure de jeux, aire de jeux, balançoire |
| `AGE_GROUP` | cat | 93% | 9 | junior 49%, toddler 23%, all 15%, senior 13%, All 1%,   0% |
| `CLIMBING` | cat | 80% | 3 |   73%, yes/oui 25%, no/non 2% |
| `TIRE_SWING` | cat | 75% | 3 |   90%, yes/oui 8%, no/non 2% |
| `SWINGS_PRESCHOOL_SEATS` | cat | 80% | 3 |   58%, yes/oui 41%, no/non 2% |
| `SWINGS_BELT_SEATS` | cat | 80% | 3 |   58%, yes/oui 40%, no/non 2% |
| `SLIDES` | cat | 79% | 3 |   74%, yes/oui 23%, no/non 3% |
| `SEE_SAW` | cat | 76% | 3 |   88%, yes/oui 10%, no/non 2% |
| `SAND_BOX` | cat | 78% | 3 |   89%, yes/oui 10%, no/non 1% |
| `HOPSCOTCH` | cat | 76% | 3 |   98%, no/non 2%, yes/oui 1% |
| `PLAYHOUSE` | cat | 76% | 3 |   87%, yes/oui 10%, no/non 3% |
| `SPRING_TOY` | cat | 77% | 3 |   69%, yes/oui 28%, no/non 2% |
| `OTHER` | cat | 80% | 3 |   74%, yes/oui 25%, no/non 2% |
| `FENCING` | cat | 76% | 3 |   85%, no/non 8%, yes/oui 7% |
| `ACCESSIBLE` | cat | 97% | 2 | no/non 82%, yes/oui 18% |
| `OPEN` | cat | 0% | 1 | yes/oui 100% |
| `MODIFIED_DATE` | date | 100% | 1,110 | 2016-01-08 → 2022-09-08, 12 gaps >30d |
| `CREATED_DATE` | date | 19% | 341 | 2015-01-29 → 2022-09-07, 26 gaps >30d |
| `PARKNAME` | text | 99% | 699 | e.g. Panda Park, Pebble Trail Park, Proudmore Romina Park |
| `PARKNAME_FR` | text | 99% | 699 | e.g. Parc Panda, Parc Pebble Trail, Parc Proudmore-Romina |
| `PARKADDRESS` | text | 99% | 698 | e.g. 105 Southam Way, 6860 Pebble Trail Way, 205 Romina Street, Gou |
| `PARKADDRESS_FR` | text | 99% | 698 | e.g. 105, voie Southam, 6860, voie Pebble Trai, 205, rue Romina, Goulb |
| `geometry` | id/text | 100% | 1,719 | e.g. {"type": "Point", "coo, {"type": "Point", "coo, {"type": "Point", "coo |
| `longitude` | num | 100% | 1,719 | -76.26 · p25 -75.77 · p50 -75.69 · p95 -75.47 · max -75.34  ▁▁▁▁▁▃▃▂▅▇█▄▃▄▁▁ |
| `latitude` | num | 100% | 1,719 | 45.03 · p25 45.29 · p50 45.36 · p95 45.47 · max 45.52  ▁▁▁▁▁▁▁▅▆▄█▆▅▇▄▂ |

## Candidate questions

- Trend / seasonality of open_play_area_structures over `MODIFIED_DATE`; structural breaks?
- Spatial clustering of open_play_area_structures; overlay wards + the decision timeline
- Concentration in `NAME` — which actors dominate? (join entity spine)

_profiled 2026-09-09 · `python3 tools/profile.py open_play_area_structures`_
