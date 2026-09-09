# Trust in others

`open_trust_in_others` · shape **arcgis-hub** · source `open-ottawa`

- origin: <https://open.ottawa.ca/datasets/ottawa::trust-in-others>
- fetched 2026-09-09 · **68 rows** · 13 columns
- csv · licence: https://ottawa.ca/en/city-hall/open-transparent-and-accountable-government/open-

## Columns

| column | kind | non-null | distinct | summary |
| --- | --- | --- | --- | --- |
| `Year_Année` | num | 100% | 1 | 2,024 · p25 2,024 · p50 2,024 · p95 2,024 · max 2,024   |
| `Region_Région` | cat | 100% | 2 | Ottawa-Gatineau- Ontario 50%, Ottawa-Gatineau- partie  50% |
| `Question` | cat | 100% | 2 | Generally speaking- woul 50%, De façon générale- dirie 50% |
| `Response_Réponse` | cat | 100% | 4 | You cannot be too carefu 25%, On n’est jamais trop pru 25%, Most people can be trust 25%, On peut faire confiance  25% |
| `Group_Groupe` | cat | 100% | 12 | Age 18%, Âge 18%, Niveau de scolarité le p 12%, Education level 12%, Genre 6%, Gender 6% |
| `Sub_group_Sous_groupe` | text | 100% | 34 | e.g. 15 to 34 years old, 15 à 34 ans, 35 to 44 years old |
| `Percent_Pourcent` | text | 100% | 33 | e.g. 59.5, 33.5, 56.6 |
| `F95lcl` | num | 100% | 38 | 22.70 · p25 34.05 · p50 42.40 · p95 54.79 · max 61.20  ▂▂▄▆▄▄▆▃█▃▅▂█▃▁▂ |
| `F95ucl` | num | 100% | 38 | 31.30 · p25 48.10 · p50 57.40 · p95 72.38 · max 77.30  ▂▁▂▁▁█▄▄▃▄▅▃▅▄▃▂ |
| `Data_quality_Qualité_des_données` | cat | 67% | 9 | E 74%, 46.9 4%, 61.3 4%, 68.7 4%, 52.8 4%, 58.4 2% |
| `Notes_Remarques` | cat | 52% | 3 | Please use estimate with 50%, Utiliser les estimations 44%, E 6% |
| `Language_Langue` | cat | 85% | 3 | English 52%, Français 45%, Utiliser les estimations 3% |
| `ObjectId` | num | 100% | 68 | 1.00 · p25 17.75 · p50 34.50 · p95 64.65 · max 68.00  █▆▆▆▆█▆▆▆▆█▆▆▆▆█ |

## Candidate questions

- (none templated)

_profiled 2026-09-09 · `python3 tools/profile.py open_trust_in_others`_
