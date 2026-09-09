# Life satisfaction

`open_life_satisfaction` · shape **arcgis-hub** · source `open-ottawa`

- origin: <https://open.ottawa.ca/datasets/ottawa::life-satisfaction>
- fetched 2026-09-09 · **96 rows** · 13 columns
- csv · licence: https://ottawa.ca/en/city-hall/open-transparent-and-accountable-government/open-

## Columns

| column | kind | non-null | distinct | summary |
| --- | --- | --- | --- | --- |
| `Year_Année` | num | 100% | 1 | 2,024 · p25 2,024 · p50 2,024 · p95 2,024 · max 2,024   |
| `Region_Région` | cat | 100% | 2 | Ottawa-Gatineau- Ontario 50%, Ottawa-Gatineau- partie  50% |
| `Question` | cat | 100% | 2 | Using a scale of 0 to 10 50%, Sur une échelle de 0 à 1 50% |
| `Response_Réponse` | cat | 100% | 6 | Strong (8-10) 17%, Modérée (5-7) 17%, Forte (8-10) 17%, Moderate (5-7) 17%, Faible (0-4) 17%, Weak (0-4) 17% |
| `Group_Groupe` | cat | 100% | 12 | Age 16%, Âge 16%, Niveau de scolarité le p 12%, Education level 12%, Genre 6%, Gender 6% |
| `Sub_group_Sous_groupe` | text | 100% | 32 | e.g. 15 to 34 years old, 15 à 34 ans, 35 to 44 years old |
| `Percent_Pourcent` | num | 100% | 46 | 4.60 · p25 15.80 · p50 39.55 · p95 47.70 · max 59.50  ▂▂▄▄▃▁▁▁▁▄██▅▁▁▁ |
| `F95lcl` | num | 100% | 43 | 2.60 · p25 11.90 · p50 33.45 · p95 42.20 · max 53.00  ▂▃█▁▂▁▁▁▃▇██▄▁▁▁ |
| `F95ucl` | num | 100% | 44 | 8.30 · p25 23.70 · p50 46.20 · p95 55.80 · max 65.70  ▁▂▄▄▁▃▁▁▁▄██▅▂▁▁ |
| `Data_quality_Qualité_des_données` | text | 0% | 0 | e.g.  |
| `Notes_Remarques` | text | 0% | 0 | e.g.  |
| `Language_Langue` | cat | 100% | 2 | English 50%, Français 50% |
| `ObjectId` | num | 100% | 96 | 1.00 · p25 24.75 · p50 48.50 · p95 91.25 · max 96.00  ████████████████ |

## Candidate questions

- (none templated)

_profiled 2026-09-09 · `python3 tools/profile.py open_life_satisfaction`_
