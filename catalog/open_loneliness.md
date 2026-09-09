# Loneliness

`open_loneliness` · shape **arcgis-hub** · source `open-ottawa`

- origin: <https://open.ottawa.ca/datasets/ottawa::loneliness>
- fetched 2026-09-09 · **272 rows** · 13 columns
- csv · licence: https://ottawa.ca/en/city-hall/open-transparent-and-accountable-government/open-

## Columns

| column | kind | non-null | distinct | summary |
| --- | --- | --- | --- | --- |
| `Year_Année` | date | 100% | 2 | 2024-01-01 → 2024-01-01 |
| `Region_Région` | cat | 100% | 2 | Ottawa-Gatineau, partie  50%, Ottawa-Gatineau, Ontario 50% |
| `Question` | cat | 100% | 2 | À quelle fréquence vous  50%, How often do you feel lo 50% |
| `Response_Réponse` | cat | 100% | 8 | Jamais 12%, Parfois 12%, Toujours ou souvent 12%, Rarement 12%, Rarely 12%, Always or often 12% |
| `Group_Groupe` | cat | 100% | 12 | Age 21%, Âge 21%, Niveau de scolarité le p 12%, Education level 12%, Genre 6%, Gender 6% |
| `Sub_group_Sous_groupe` | text | 100% | 36 | e.g. Certificat, diplôme ou, Diplôme d'études secon, Femmes+ |
| `Percent_Pourcent` | num | 100% | 112 | 5.00 · p25 16.10 · p50 26.70 · p95 39.25 · max 45.60  ▁▂▃▅▆▃▃▁▂▃▅█▄▂▂▁ |
| `F95lcl` | num | 100% | 107 | 2.40 · p25 12.15 · p50 20.15 · p95 32.60 · max 35.30  ▂▂▄▆▆▆▄▂▄▂▄▄▅█▅▃ |
| `F95ucl` | num | 100% | 101 | 10.20 · p25 21.00 · p50 33.45 · p95 47.39 · max 56.20  ▂▃▂▅▅▂▂▁▁█▆▄▂▂▁▁ |
| `Data_quality_Qualité_des_données` | cat | 4% | 1 | E 100% |
| `Notes_Remarques` | cat | 5% | 3 | Utiliser les estimations 50%, Please use estimate with 25%, Use estimate with cautio 25% |
| `Language_Langue` | cat | 100% | 2 | Français 50%, English 50% |
| `ObjectId` | num | 100% | 272 | 1.00 · p25 68.75 · p50 136 · p95 258 · max 272  ████████████████ |

## Candidate questions

- (none templated)

_profiled 2026-09-09 · `python3 tools/profile.py open_loneliness`_
