# Financial security

`open_financial_security` · shape **arcgis-hub** · source `open-ottawa`

- origin: <https://open.ottawa.ca/datasets/ottawa::financial-security>
- fetched 2026-09-09 · **384 rows** · 13 columns
- csv · licence: https://ottawa.ca/en/city-hall/open-transparent-and-accountable-government/open-

## Columns

| column | kind | non-null | distinct | summary |
| --- | --- | --- | --- | --- |
| `Year_Année` | num | 100% | 4 | 2,021 · p25 2,022 · p50 2,022 · p95 2,024 · max 2,024  █▁▁▁▁█▁▁▁▁█▁▁▁▁█ |
| `Region_Région` | cat | 100% | 2 | Ottawa-Gatineau- Ontario 50%, Ottawa-Gatineau- partie  50% |
| `Question` | cat | 100% | 2 | In the past 12 months- h 50%, Au cours des 12 derniers 50% |
| `Response_Réponse` | cat | 100% | 6 | (2) Neither difficult no 17%, (2) Ni difficile ni faci 17%, (1) Very easy or easy 17%, (1) Très facile ou facil 17%, (3) Très difficile ou di 17%, (3) Very difficult or di 17% |
| `Group_Groupe` | text | 100% | 32 | e.g. 15 to 34 years old, 15 à 34 ans, 35 to 44 years old |
| `Subgroup_Sous_groupe` | cat | 100% | 12 | Age 16%, Âge 16%, Niveau de scolarité le p 12%, Education level 12%, Genre 6%, Gender 6% |
| `Percent_Pourcent` | num | 100% | 147 | 7.60 · p25 27.38 · p50 33.40 · p95 50.57 · max 67.70  ▁▂▂▃▃▅▆█▃▂▂▂▁▁▁▁ |
| `F95lcl` | num | 100% | 149 | 3.70 · p25 20.45 · p50 25.35 · p95 41.57 · max 57.30  ▁▃▂▃▃▆██▄▃▂▂▁▁▁▁ |
| `F95ucl` | num | 100% | 140 | 14.90 · p25 35.33 · p50 41.35 · p95 59.84 · max 77.60  ▁▂▁▂▄▄▇█▄▂▃▂▁▁▁▁ |
| `Data_quality_Qualité_des_données` | cat | 25% | 1 | E 100% |
| `Notes_Remarques` | cat | 25% | 2 | Utiliser les estimations 50%, Please use estimate with 50% |
| `Language_Langue` | cat | 100% | 2 | English 50%, Français 50% |
| `ObjectId` | num | 100% | 384 | 1.00 · p25 96.75 · p50 192 · p95 365 · max 384  ████████████████ |

## Candidate questions

- (none templated)

_profiled 2026-09-09 · `python3 tools/profile.py open_financial_security`_
