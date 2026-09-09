# Benches

`open_benches` · shape **arcgis-hub** · source `open-ottawa`

- origin: <https://open.ottawa.ca/datasets/ottawa::benches>
- fetched 2026-09-09 · **3,318 rows** · 19 columns
- csv · licence: https://ottawa.ca/en/city-hall/get-know-your-city/open-data#open-data-licence-ve

## Columns

| column | kind | non-null | distinct | summary |
| --- | --- | --- | --- | --- |
| `X` | num | 99% | 3,317 | -8,484,176 · p25 -8,435,248 · p50 -8,426,148 · p95 -8,402,580 · max -8,386,473  ▁▁▁▁▁▃▂▃▄█▃▂▂▂▁▁ |
| `Y` | num | 99% | 3,317 | 5,641,958 · p25 5,670,776 · p50 5,679,519 · p95 5,695,469 · max 5,702,969  ▁▁▁▁▂▃▄▃▃█▄▆▆▃▂▁ |
| `OBJECTID` | num | 100% | 3,318 | 1.00 · p25 885 · p50 11,676 · p95 13,311 · max 13,477  ▇▃▁▁▁▁▁▁▁▁▁▁▁▂▆█ |
| `PARK_ID` | num | 99% | 545 | 2.00 · p25 234 · p50 825 · p95 2,585 · max 2,904  █▆▃▃▄▄▃▂▂▃▁▁▁▄▃▁ |
| `FACILITYID` | num | 100% | 3,318 | 49,313 · p25 51,082 · p50 54,206 · p95 58,695 · max 59,104  ▇▇█▆▅▄▃▄▅▄▅▄▆▇▆▇ |
| `ACCESSIBLE` | cat | 98% | 4 | n 48%, y 32%, no/non 15%, yes/oui 5% |
| `BENCH_TYPE` | cat | 100% | 11 | Bench 86%, Commemorative Bench 8%, Players Bench 3%, Bleachers 2%, Older Adult Plan Bench 1%, Transfer bench 0% |
| `BENCH_TYPE_FR` | cat | 98% | 13 | Banc 86%, Banc commémoratif 8%, Banc des joueurs 3%, Gradins 2%, Plan relatif aux personn 1%, Banc de transfert 0% |
| `NAME` | id/text | 8% | 236 | e.g. Richard M. Zubrycki, Réal Cloutier, Astrid W. Graham |
| `NAME_FR` | id/text | 8% | 235 | e.g. Richard M. Zubrycki, Réal Cloutier, Astrid W. Graham |
| `YEAR_INSTALLED` | num | 54% | 27 | 1,958 · p25 1,999 · p50 2,011 · p95 2,020 · max 2,025  ▁▁▁▁▁▁▁▇▁▁▃▃▃█▆▂ |
| `LOCATION_DESCRIPTION` | text | 4% | 104 | e.g. Photo included, On pathway beside rive, Accessible stonedust p |
| `LOCATION_DESCRIPTION_FR` | cat | 0% | 15 | Parc Britania 31%, Parc Britania, regardant 15%, promenade Grant Carmen à 8%, rue Bank (Billings Bridg 4%, Conroy Pit 4%, 3100, avenue Carling 4% |
| `NOTES` | text | 49% | 41 | e.g. Located. Year installe, Located. Year installe, Year installed based o |
| `PLAQUE_TEXT` | id/text | 7% | 234 | e.g. January 31 1944 ~ May , In Memoriam
Réal Clou, Astrid W. Graham
Huma |
| `PLAQUE_TEXT_FR` | id/text | 7% | 233 | e.g. Richard M. Zubrycki
j, À la mémoire de
Réal , Astrid W. Graham
Huma |
| `GLOBALID` | id/text | 100% | 3,318 | e.g. {A6202DF4-B5AD-476D-B0, {42CCD6D5-BFF9-485A-BC, {A734D8D8-9665-408E-B1 |
| `CREATED_DATE` | date | 68% | 2,285 | 2019-05-14 → 2026-01-27, 15 gaps >30d |
| `LAST_EDITED_DATE` | date | 73% | 1,552 | 2019-05-14 → 2026-02-03, 15 gaps >30d |

## Candidate questions

- Trend / seasonality of open_benches over `YEAR_INSTALLED`; structural breaks?
- Concentration in `NAME` — which actors dominate? (join entity spine)

_profiled 2026-09-09 · `python3 tools/profile.py open_benches`_
