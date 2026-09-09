# Self-rated mental health

`open_self_rated_mental_health` · shape **arcgis-hub** · source `open-ottawa`

- origin: <https://open.ottawa.ca/datasets/ottawa::self-rated-mental-health>
- fetched 2026-09-09 · **272 rows** · 13 columns
- csv · licence: https://ottawa.ca/en/city-hall/open-transparent-and-accountable-government/open-

## Columns

| column | kind | non-null | distinct | summary |
| --- | --- | --- | --- | --- |
| `Year_Année` | date | 100% | 2 | 2024-01-01 → 2024-01-01 |
| `Region_Région` | cat | 100% | 2 | Ottawa-Gatineau- partie  50%, Ottawa - Gatineau (Ontar 50% |
| `Question` | cat | 100% | 2 | En général- comment est  50%, In general- how is your  50% |
| `Response_Réponse` | cat | 100% | 8 | Excellente 12%, Bonne 12%, Très bonne 12%, Passable ou mauvaise 12%, Very good 12%, Good 12% |
| `Group_Groupe` | cat | 100% | 12 | Age 21%, Âge 21%, Niveau de scolarité le p 12%, Education level 12%, Genre 6%, Gender 6% |
| `Sub_group_Sous_groupe` | text | 100% | 36 | e.g. Certificat, diplôme ou, Diplôme d'études secon, Femmes+ |
| `Percent_Pourcent` | num | 100% | 101 | 7.00 · p25 20.05 · p50 26.40 · p95 34.65 · max 39.70  ▁▁▁▂▄▂▃▃▃▄▃█▄▃▁▁ |
| `F95lcl` | num | 100% | 104 | 4.60 · p25 14.80 · p50 20.80 · p95 28.29 · max 34.60  ▂▂▂▄▃▆▅▄▄▆█▇▄▂▁▁ |
| `F95ucl` | num | 100% | 114 | 10.10 · p25 25.18 · p50 32.90 · p95 42.15 · max 46.40  ▁▁▁▂▃▃▃▃▃▄█▃▅▄▁▂ |
| `Data_quality_Qualité_des_données` | cat | 5% | 1 | E 100% |
| `Notes_Remarques` | cat | 5% | 2 | Please use estimate with 50%, Utiliser les estimations 50% |
| `Language_Langue` | cat | 100% | 2 | Français 50%, English 50% |
| `ObjectId` | num | 100% | 272 | 1.00 · p25 68.75 · p50 136 · p95 258 · max 272  ████████████████ |

## Candidate questions

- (none templated)

_profiled 2026-09-09 · `python3 tools/profile.py open_self_rated_mental_health`_
