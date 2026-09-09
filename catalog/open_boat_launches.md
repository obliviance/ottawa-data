# Boat Launches

`open_boat_launches` · shape **arcgis-hub** · source `open-ottawa`

- origin: <https://open.ottawa.ca/datasets/ottawa::boat-launches>
- fetched 2026-09-09 · **30 rows** · 19 columns
- csv · licence: https://ottawa.ca/en/city-hall/get-know-your-city/open-data#open-data-licence-ve

## Columns

| column | kind | non-null | distinct | summary |
| --- | --- | --- | --- | --- |
| `X` | num | 100% | 29 | -8,455,021 · p25 -8,426,740 · p50 -8,425,499 · p95 -8,410,010 · max -8,396,907  ▁▁▁▃▁▁▁██▃▁▁▂▁▁▁ |
| `Y` | num | 100% | 29 | 5,633,086 · p25 5,659,821 · p50 5,671,218 · p95 5,697,931 · max 5,703,331  ▂▁▃▁▁▆█▃▃▁▆▃▃▃▅▂ |
| `OBJECTID` | num | 100% | 30 | 1.00 · p25 8.25 · p50 15.50 · p95 28.55 · max 30.00  █████▄████▄█████ |
| `PARK_ID` | num | 93% | 23 | 66.00 · p25 234 · p50 926 · p95 1,616 · max 1,674  ▆▆▁▁▂▁▁▃█▃▃▂▂▁▆▃ |
| `FACILITYID` | num | 93% | 26 | 7,586 · p25 20,005 · p50 20,012 · p95 55,019 · max 57,483  ▁▁▁█▁▁▁▁▁▁▁▁▁▁▁▃ |
| `NAME` | id/text | 100% | 27 | e.g. Roslyn Park Boat Launc, Mahogany Harbour Landi, Dick Bell Park Boat La |
| `NAME_FR` | cat | 6% | 2 | Havre Mahogany 50%, Rampe de mise à l'eau du 50% |
| `LAUNCH_TYPE` | cat | 100% | 5 | dock 43%, boat launch 23%, canoe launch 23%, Boat Launch 7%, Joe Messner Boat Launch 3% |
| `LAUNCH_TYPE_FR` | cat | 96% | 5 | quai 45%, rampe de mise à l'eau 24%, aire de mise à l'eau des 24%, rampe de mise a leau 3%, rampe d’accès à l’eau Jo 3% |
| `SURFACE` | cat | 100% | 4 | wood 43%, gravel 40%, dirt 10%, paved 7% |
| `SURFACE_FR` | cat | 96% | 4 | bois 45%, gravier 38%, terre 10%, asphalte 7% |
| `ACCESSIBLE` | cat | 13% | 2 | no/non 50%, yes/oui 50% |
| `OPEN` | cat | 100% | 1 | yes/oui 100% |
| `MODIFIED_DATE` | date | 96% | 28 | 2021-11-01 → 2024-06-17, 1 gaps >30d |
| `CREATED_DATE` | date | 30% | 9 | 2018-12-04 → 2022-06-09, 3 gaps >30d |
| `PARKNAME` | text | 0% | 0 | e.g.  |
| `PARKNAME_FR` | text | 0% | 0 | e.g.  |
| `PARKADDRESS` | text | 0% | 0 | e.g.  |
| `PARKADDRESS_FR` | text | 0% | 0 | e.g.  |

## Candidate questions

- (none templated)

_profiled 2026-09-09 · `python3 tools/profile.py open_boat_launches`_
