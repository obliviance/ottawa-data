# Lawn Bowling

`open_lawn_bowling` · shape **arcgis-hub** · source `open-ottawa`

- origin: <https://open.ottawa.ca/datasets/ottawa::lawn-bowling>
- fetched 2026-09-09 · **4 rows** · 19 columns
- csv · licence: https://ottawa.ca/en/city-hall/get-know-your-city/open-data#open-data-licence-ve

## Columns

| column | kind | non-null | distinct | summary |
| --- | --- | --- | --- | --- |
| `X` | num | 100% | 4 | -8,489,251 · p25 -8,459,368 · p50 -8,440,738 · p95 -8,430,022 · max -8,429,661  ▄▁▁▁▁▁▁▁▁▁▄▁▁▁▁█ |
| `Y` | num | 100% | 4 | 5,658,210 · p25 5,669,314 · p50 5,678,642 · p95 5,687,954 · max 5,688,604  █▁▁▁▁▁▁█▁▁▁▁▁█▁█ |
| `OBJECTID` | num | 100% | 4 | 1.00 · p25 1.75 · p50 2.50 · p95 3.85 · max 4.00  █▁▁▁▁█▁▁▁▁█▁▁▁▁█ |
| `PARK_ID` | num | 100% | 4 | 310 · p25 745 · p50 1,048 · p95 1,476 · max 1,523  █▁▁▁▁▁▁█▁▁▁█▁▁▁█ |
| `FACILITYID` | num | 100% | 4 | 4,953 · p25 21,515 · p50 27,046 · p95 27,060 · max 27,060  ▃▁▁▁▁▁▁▁▁▁▁▁▁▁▁█ |
| `NAME` | cat | 100% | 4 | Lawn Bowling 25%, Nepean Lawn Bowls 25%, Elmdale Lawn Bowling Clu 25%, Goulbourn Lawn Bowling C 25% |
| `NAME_FR` | cat | 100% | 4 | boulingrin 25%, Club de boulingrin de Ne 25%, Club de boulingrin d'Elm 25%, Club de boulingrin de Go 25% |
| `LANES` | num | 100% | 3 | 7.00 · p25 7.75 · p50 8.00 · p95 14.80 · max 16.00  ▄█▁▁▁▁▁▁▁▁▁▁▁▁▁▄ |
| `LIGHTS` | cat | 100% | 1 | yes/oui 100% |
| `CLUBHOUSE` | cat | 100% | 2 | yes/oui 75%, no/non 25% |
| `BENCHES` | cat | 100% | 2 | yes/oui 75%, no/non 25% |
| `ACCESSIBLE` | cat | 100% | 1 | no/non 100% |
| `OPEN` | text | 0% | 0 | e.g.  |
| `MODIFIED_DATE` | date | 100% | 4 | 2018-01-18 → 2018-01-18 |
| `CREATED_DATE` | text | 0% | 0 | e.g.  |
| `PARKNAME` | text | 0% | 0 | e.g.  |
| `PARKNAME_FR` | text | 0% | 0 | e.g.  |
| `PARKADDRESS` | text | 0% | 0 | e.g.  |
| `PARKADDRESS_FR` | text | 0% | 0 | e.g.  |

## Candidate questions

- (none templated)

_profiled 2026-09-09 · `python3 tools/profile.py open_lawn_bowling`_
