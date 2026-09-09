# Trust in media

`open_trust_in_media` · shape **arcgis-hub** · source `open-ottawa`

- origin: <https://open.ottawa.ca/datasets/ottawa::trust-in-media>
- fetched 2026-09-09 · **102 rows** · 13 columns
- csv · licence: https://ottawa.ca/en/city-hall/open-transparent-and-accountable-government/open-

## Columns

| column | kind | non-null | distinct | summary |
| --- | --- | --- | --- | --- |
| `Year_Année` | num | 100% | 1 | 2,024 · p25 2,024 · p50 2,024 · p95 2,024 · max 2,024   |
| `Region_Région` | cat | 100% | 2 | Ottawa-Gatineau, Ontario 50%, Ottawa-Gatineau, partie  50% |
| `Question` | cat | 100% | 2 | On a scale of 0 to 10- w 50%, Sur une échelle de 0 à 1 50% |
| `Response_Réponse` | cat | 100% | 6 | Strong (8-10) 17%, Modérée (5-7) 17%, Moderate (5-7) 17%, Forte (8-10) 17%, Weak (0-4) 17%, Faible (0-4) 17% |
| `Group_Groupe` | cat | 100% | 12 | Age 18%, Âge 18%, Niveau de scolarité le p 12%, Education level 12%, Genre 6%, Gender 6% |
| `Sub_group_Sous_groupe` | text | 100% | 34 | e.g. 15 to 34 years old, 15 à 34 ans, 35 to 44 years old |
| `Percent_Pourcent` | num | 100% | 49 | 6.80 · p25 16.12 · p50 33.90 · p95 55.15 · max 62.00  ▁▅█▂▁▁▅▃▅▃▁▂▅▆▂▁ |
| `F95lcl` | num | 100% | 49 | 4.20 · p25 12.62 · p50 28.80 · p95 48.96 · max 52.20  ▂▇█▄▂▁▅▄▇▄▂▃▂▇▆▃ |
| `F95ucl` | num | 100% | 50 | 10.90 · p25 22.15 · p50 39.90 · p95 61.93 · max 70.90  ▁█▄▃▁▂▄▄▆▁▁▅▇▄▁▁ |
| `Data_quality_Qualité_des_données` | text | 0% | 0 | e.g.  |
| `Notes_Remarques` | text | 0% | 0 | e.g.  |
| `Language_Langue` | cat | 100% | 2 | English 50%, Français 50% |
| `ObjectId` | num | 100% | 102 | 1.00 · p25 26.25 · p50 51.50 · p95 96.95 · max 102  █▇▇█▇▇█▇▇█▇▇█▇▇█ |

## Candidate questions

- (none templated)

_profiled 2026-09-09 · `python3 tools/profile.py open_trust_in_media`_
