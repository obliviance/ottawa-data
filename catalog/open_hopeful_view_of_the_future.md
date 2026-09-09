# Hopeful view of the future

`open_hopeful_view_of_the_future` · shape **arcgis-hub** · source `open-ottawa`

- origin: <https://open.ottawa.ca/datasets/ottawa::hopeful-view-of-the-future>
- fetched 2026-09-09 · **264 rows** · 13 columns
- csv · licence: https://ottawa.ca/en/city-hall/open-transparent-and-accountable-government/open-

## Columns

| column | kind | non-null | distinct | summary |
| --- | --- | --- | --- | --- |
| `Year_Année` | date | 100% | 2 | 2024-01-01 → 2024-01-01 |
| `Region_Région` | cat | 100% | 2 | Ottawa-Gatineau, Ontario 50%, Ottawa-Gatineau, partie  50% |
| `Question` | cat | 100% | 2 | Thinking about your life 50%, En pensant à votre vie e 50% |
| `Response_Réponse` | cat | 100% | 8 | Always 12%, Rarely or never 12%, Rarement ou jamais 12%, Toujours 12%, Souvent 12%, Sometimes 12% |
| `Group_Groupe` | cat | 100% | 12 | Age 20%, Âge 20%, Niveau de scolarité le p 12%, Education level 12%, Genre 6%, Gender 6% |
| `Sub_group_Sous_groupe` | text | 100% | 38 | e.g. 15 to 24 years old, 15 to 34 years old, 15 à 24 ans |
| `Percent_Pourcent` | num | 100% | 108 | 4.70 · p25 17.60 · p50 24.00 · p95 44.92 · max 53.60  ▄▆▃▃█▆█▇▄▂▂▆▃▃▁▁ |
| `F95lcl` | num | 100% | 119 | 2.30 · p25 10.82 · p50 18.05 · p95 39.19 · max 43.70  ▆▆▄▆▅▆█▇▅▂▃▂▄▂▃▂ |
| `F95ucl` | num | 100% | 120 | 7.80 · p25 24.38 · p50 31.85 · p95 54.18 · max 63.80  ▃▄▂▃▄▅▆█▃▁▄▅▂▂▁▁ |
| `Data_quality_Qualité_des_données` | cat | 30% | 1 | E 100% |
| `Notes_Remarques` | cat | 30% | 2 | Please use estimate with 50%, Utiliser les estimations 50% |
| `Language_Langue` | cat | 100% | 2 | English 50%, Français 50% |
| `ObjectId` | num | 100% | 264 | 1.00 · p25 66.75 · p50 132 · p95 251 · max 264  █▇█▇█▇█▇▇█▇█▇█▇█ |

## Candidate questions

- (none templated)

_profiled 2026-09-09 · `python3 tools/profile.py open_hopeful_view_of_the_future`_
