# Volleyball Courts

`open_volleyball_courts` · shape **arcgis-hub** · source `open-ottawa`

- origin: <https://open.ottawa.ca/datasets/ottawa::volleyball-courts>
- fetched 2026-09-09 · **39 rows** · 18 columns
- csv · licence: https://ottawa.ca/en/city-hall/get-know-your-city/open-data#open-data-licence-ve

## Columns

| column | kind | non-null | distinct | summary |
| --- | --- | --- | --- | --- |
| `X` | num | 100% | 39 | -8,483,186 · p25 -8,428,806 · p50 -8,416,196 · p95 -8,403,146 · max -8,395,398  ▁▁▁▁▁▁▁▂▁▃▂▃▄█▂▂ |
| `Y` | num | 100% | 39 | 5,644,973 · p25 5,676,229 · p50 5,687,863 · p95 5,698,651 · max 5,701,525  ▃▁▁▂▃▁▂▂▅▅▂▃▆▇█▄ |
| `OBJECTID` | num | 100% | 39 | 1.00 · p25 10.50 · p50 20.00 · p95 37.10 · max 39.00  █▅█▅▅█▅█▅▅█▅▅█▅█ |
| `PARK_ID` | num | 100% | 39 | 67.00 · p25 416 · p50 779 · p95 1,683 · max 2,458  ▅█▃▃█▅▆▄▅▁▂▁▁▁▁▃ |
| `FACILITYID` | num | 100% | 39 | 26,001 · p25 26,050 · p50 26,110 · p95 52,211 · max 58,433  █▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁ |
| `NAME` | cat | 100% | 7 | Volleyball - 1 Court 77%, Volleyball - 2 Courts 8%, Volleyball - 18 Courts 5%, CHEO BBQ COURTS 3%, Volleyball - 20 Courts 3%, Volleyball - 1 Courts 3% |
| `NAME_FR` | cat | 100% | 7 | Volleyball - 1 terrain 77%, Volleyball - 2 terrains 8%, Volleyball - 18 terrains 5%, TERRAINS CHEO BBQ 3%, Volleyball - 20 terrains 3%, Volleyball - 1 terrains 3% |
| `NO_COURTS` | num | 100% | 5 | 1.00 · p25 1.00 · p50 1.00 · p95 18.20 · max 24.00  █▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁ |
| `SURFACE_TYPE` | cat | 100% | 3 | sand 77%, grass 21%, gravel 3% |
| `SURFACE_TYPE_FR` | cat | 100% | 3 | sable 77%, herbe 21%, gravier 3% |
| `ACCESSIBLE` | cat | 100% | 1 | no/non 100% |
| `OPEN` | text | 0% | 0 | e.g.  |
| `MODIFIED_DATE` | date | 100% | 8 | 2018-01-18 → 2022-09-01, 4 gaps >30d |
| `CREATED_DATE` | date | 12% | 5 | 2016-03-08 → 2022-09-01, 2 gaps >30d |
| `PARKNAME` | text | 0% | 0 | e.g.  |
| `PARKNAME_FR` | text | 0% | 0 | e.g.  |
| `PARKADDRESS` | text | 0% | 0 | e.g.  |
| `PARKADDRESS_FR` | text | 0% | 0 | e.g.  |

## Candidate questions

- (none templated)

_profiled 2026-09-09 · `python3 tools/profile.py open_volleyball_courts`_
