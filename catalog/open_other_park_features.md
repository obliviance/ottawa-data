# Other Park Features

`open_other_park_features` · shape **arcgis-hub** · source `open-ottawa` · **spatial**

- origin: <https://open.ottawa.ca/datasets/ottawa::other-park-features>
- fetched 2026-09-09 · **645 rows** · 17 columns
- geojson · licence: https://ottawa.ca/en/city-hall/get-know-your-city/open-data#open-data-licence-ve

## Columns

| column | kind | non-null | distinct | summary |
| --- | --- | --- | --- | --- |
| `OBJECTID` | num | 100% | 645 | 1.00 · p25 162 · p50 323 · p95 613 · max 645  █▇▇█▇▇▇█▇▇▇█▇▇▇█ |
| `PARK_ID` | num | 100% | 389 | 2.00 · p25 386 · p50 1,028 · p95 2,586 · max 2,904  ▅▆▄▃▅▅▃▂▃▄▁▁▁█▄▁ |
| `FACILITYID` | num | 100% | 645 | 1,349 · p25 29,176 · p50 34,741 · p95 58,157 · max 59,118  ▁▁▁▁▁▁▁█▁▃▁▁▁▂▂▃ |
| `NAME` | text | 100% | 104 | e.g. Bridge, Ball Hockey Court, Kiwanis Bandshell |
| `NAME_FR` | text | 100% | 102 | e.g. Pont, Cour de hockey, Kiwanis Bandshell |
| `PARK_FEATURE_TYPE` | text | 100% | 32 | e.g. bridge, ball hockey court, amphitheatre-stage |
| `PARK_FEATURE_TYPE_FR` | text | 100% | 36 | e.g. pont, cour de hockey, amphithéâtre - scène |
| `ACCESSIBLE` | cat | 24% | 2 | yes/oui 86%, no/non 14% |
| `MODIFIED_DATE` | date | 99% | 417 | 2014-09-26 → 2025-03-17, 19 gaps >30d |
| `CREATED_DATE` | date | 45% | 293 | 2014-05-21 → 2022-09-07, 29 gaps >30d |
| `PARKNAME` | text | 93% | 369 | e.g. Amberwood Pathway, Pine Bluff Park, Wyldwood Park |
| `PARKNAME_FR` | text | 93% | 369 | e.g. Sentier Amberwood, Parc Pine Bluff, Parc Wyldwood |
| `PARKADDRESS` | text | 93% | 369 | e.g. 72 Trailway Circle, Go, 46P Hesse Crescent, Go, 24 Wintergreen Drive,  |
| `PARKADDRESS_FR` | text | 93% | 369 | e.g. 72, cercle Trailway, G, 46P, croissant Hesse, , 24, promenade Wintergr |
| `geometry` | id/text | 100% | 645 | e.g. {"type": "Point", "coo, {"type": "Point", "coo, {"type": "Point", "coo |
| `longitude` | num | 100% | 645 | -76.21 · p25 -75.75 · p50 -75.69 · p95 -75.46 · max -75.34  ▁▁▁▁▁▃▂▂▅█▅▂▃▃▁▁ |
| `latitude` | num | 100% | 645 | 45.13 · p25 45.29 · p50 45.36 · p95 45.48 · max 45.52  ▁▁▁▁▄▆▄▄▄█▄▆▆▄▃▂ |

## Candidate questions

- Trend / seasonality of open_other_park_features over `MODIFIED_DATE`; structural breaks?
- Spatial clustering of open_other_park_features; overlay wards + the decision timeline
- Concentration in `NAME` — which actors dominate? (join entity spine)

_profiled 2026-09-09 · `python3 tools/profile.py open_other_park_features`_
