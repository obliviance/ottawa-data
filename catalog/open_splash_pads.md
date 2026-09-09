# Splash Pads

`open_splash_pads` · shape **arcgis-hub** · source `open-ottawa`

- origin: <https://open.ottawa.ca/datasets/ottawa::splash-pads>
- fetched 2026-09-09 · **161 rows** · 25 columns
- csv · licence: https://ottawa.ca/en/city-hall/get-know-your-city/open-data#open-data-licence-ve

## Columns

| column | kind | non-null | distinct | summary |
| --- | --- | --- | --- | --- |
| `X` | num | 100% | 161 | -8,464,509 · p25 -8,431,185 · p50 -8,422,263 · p95 -8,401,624 · max -8,398,660  ▁▁▂▃▂▁▃▃▇▆▆█▂▄▄▃ |
| `Y` | num | 100% | 161 | 5,659,302 · p25 5,672,110 · p50 5,681,028 · p95 5,696,446 · max 5,700,791  ▂▃▅▁▃▃▄▄▂▂▃▅█▃▃▁ |
| `OBJECTID` | num | 100% | 161 | 1.00 · p25 41.00 · p50 81.00 · p95 153 · max 161  █▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇ |
| `PARK_ID` | num | 100% | 160 | 2.00 · p25 430 · p50 964 · p95 2,625 · max 2,671  █▄▆▅▄▄▅▂▁▃▂▁▁▁▆█ |
| `FACILITYID` | num | 100% | 161 | 31,014 · p25 31,918 · p50 35,273 · p95 59,106 · max 59,115  █▁▆▂▁▁▁▁▁▁▂▁▁▁▁▂ |
| `NAME` | text | 100% | 40 | e.g. Splash Pad, Miikana Park Splash Pa, Maze Park Splash Pad |
| `NAME_FR` | text | 100% | 39 | e.g. Aire de jeux d'eau, Parc Miikana Aire de j, Parc Maize Aire de jeu |
| `ADDRESS` | id/text | 100% | 161 | e.g. 220 Stoneway Drive, Ne, 75 Glendale Avenue, Ot, 3525 Cambrian Road, Ne |
| `ADDRESS_FR` | id/text | 100% | 161 | e.g. 220, promenade Stonewa, 75, avenue Glendale, O, 3525, chemin Cambrian, |
| `SHORTNAME` | id/text | 100% | 161 | e.g. Stonecrest Park, Glebe Memorial Park, Half Moon Bay Park |
| `OPEN` | cat | 99% | 2 | yes/oui 95%, no/non 5% |
| `CLASS` | text | 0% | 0 | e.g.  |
| `ACCESSIBLE` | cat | 100% | 2 | no/non 57%, yes/oui 43% |
| `MODIFIED_DATE` | date | 100% | 78 | 2022-05-13 → 2025-09-02, 3 gaps >30d |
| `CREATED_DATE` | date | 33% | 52 | 2014-06-23 → 2024-05-24, 19 gaps >30d |
| `LINK` | cat | 77% | 1 | http://ottawa.ca/en/resi 100% |
| `LINK_FR` | cat | 77% | 1 | http://ottawa.ca/fr/resi 100% |
| `LINK_LABEL` | cat | 77% | 1 | Splash Pads 100% |
| `LINK_LABEL_FR` | cat | 77% | 1 | Aires de jets d'eau 100% |
| `LINK_DESCRIPTION` | text | 0% | 0 | e.g.  |
| `LINK_DESCRIPTION_FR` | text | 0% | 0 | e.g.  |
| `PARKNAME` | id/text | 100% | 160 | e.g. Stonecrest Park, Glebe Memorial Park, Half Moon Bay Park |
| `PARKNAME_FR` | id/text | 100% | 160 | e.g. Parc Stonecrest, Parc commémoratif du G, Parc Half Moon Bay |
| `PARKADDRESS` | id/text | 100% | 160 | e.g. 220 Stoneway Drive, 75 Glendale Avenue, Ot, 3525 Cambrian Road |
| `PARKADDRESS_FR` | id/text | 100% | 160 | e.g. 220 promenade Stoneway, 75, avenue Glendale, O, 3525 chemin Cambrian |

## Candidate questions

- Concentration in `NAME` — which actors dominate? (join entity spine)

_profiled 2026-09-09 · `python3 tools/profile.py open_splash_pads`_
