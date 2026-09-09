# Open Loop Geothermal Potential

`open_open_loop_geothermal_potential` · shape **arcgis-hub** · source `open-ottawa`

- origin: <https://open.ottawa.ca/datasets/ottawa::open-loop-geothermal-potential>
- fetched 2026-09-09 · **158 rows** · 9 columns
- csv · licence: https://ottawa.ca/en/city-hall/get-know-your-city/open-data#open-data-licence-ve

## Columns

| column | kind | non-null | distinct | summary |
| --- | --- | --- | --- | --- |
| `OBJECTID` | num | 100% | 158 | 1.00 · p25 40.25 · p50 79.50 · p95 150 · max 158  █████▇████▇█████ |
| `CRITERIA_P` | cat | 100% | 4 | YES 42%, NO 26%, Potential 16%, Unlikely 16% |
| `GLOBALID` | id/text | 100% | 158 | e.g. {CCF5632C-6D32-40EA-B7, {6636938C-EAED-4B41-AE, {F66E4AB1-437F-44C1-81 |
| `CREATED_DATE` | text | 0% | 0 | e.g.  |
| `LAST_EDITED_DATE` | text | 0% | 0 | e.g.  |
| `SHAPE_Length` | num | 100% | 158 | 68.71 · p25 1,539 · p50 3,544 · p95 24,049 · max 366,234  █▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁ |
| `SHAPE_Area` | num | 100% | 158 | 179 · p25 144,390 · p50 685,317 · p95 19,984,716 · max 380,300,406  █▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁ |
| `POTENTIAL_EN` | cat | 74% | 3 | High 57%, Average 21%, Low 21% |
| `POTENTIEL_FR` | cat | 100% | 4 | Haute 42%, Aucun 26%, Moyen 16%, Faible 16% |

## Candidate questions

- (none templated)

_profiled 2026-09-09 · `python3 tools/profile.py open_open_loop_geothermal_potential`_
