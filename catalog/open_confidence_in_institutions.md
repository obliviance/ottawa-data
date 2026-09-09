# Confidence in institutions

`open_confidence_in_institutions` · shape **arcgis-hub** · source `open-ottawa`

- origin: <https://open.ottawa.ca/datasets/ottawa::confidence-in-institutions>
- fetched 2026-09-09 · **680 rows** · 14 columns
- csv · licence: https://ottawa.ca/en/city-hall/open-transparent-and-accountable-government/open-

## Columns

| column | kind | non-null | distinct | summary |
| --- | --- | --- | --- | --- |
| `Year_Année` | num | 100% | 1 | 2,024 · p25 2,024 · p50 2,024 · p95 2,024 · max 2,024   |
| `Region_Région` | cat | 100% | 2 | Ottawa-Gatineau- Ontario 50%, Ottawa-Gatineau- partie  50% |
| `Question` | cat | 100% | 2 | Using a scale of 1 to 5  50%, Sur une échelle de 1 à 5 50% |
| `Category_Catégorie` | cat | 100% | 9 | Police 20%, Canadian media 10%, Système scolaire 10%, School system 10%, Système de justice 10%, Parliament 10% |
| `Response_Réponse` | cat | 100% | 11 | 3 25%, 4 15%, 2 10%, 1 - No confidence at all 8%, 5 - Une grande confiance 8%, 5 - A great deal of conf 8% |
| `Group_Groupe` | cat | 100% | 12 | Age 18%, Âge 18%, Niveau de scolarité le p 12%, Education level 12%, Genre 6%, Gender 6% |
| `Subgroup_Sous_groupe` | text | 100% | 34 | e.g. 15 to 34 years old, 15 à 34 ans, 35 to 44 years old |
| `Percent_Pourcent` | text | 98% | 213 | e.g. 29.5, 35.4, 21.4 |
| `F95lcl` | num | 98% | 228 | 2.20 · p25 11.50 · p50 18.40 · p95 34.90 · max 50.30  ▂▇▆█▇▆█▅▅▅▃▁▁▁▁▁ |
| `F95ucl` | num | 98% | 256 | 4.30 · p25 23.07 · p50 31.30 · p95 53.90 · max 66.50  ▂▂▃▅▇█▇▆▆▇▅▃▂▃▁▁ |
| `Data_quality_Qualité_des_données` | text | 66% | 76 | e.g. E, 22.1, 43.2 |
| `Notes_Remarques` | cat | 51% | 3 | Please use estimate with 50%, Utiliser les estimations 44%, E 6% |
| `Language_Langue` | cat | 85% | 3 | English 52%, Français 45%, Utiliser les estimations 3% |
| `ObjectId` | num | 100% | 680 | 1.00 · p25 171 · p50 340 · p95 646 · max 680  █▇█▇█▇█▇▇█▇█▇█▇█ |

## Candidate questions

- Trend / seasonality of open_confidence_in_institutions over `Year_Année`; structural breaks?

_profiled 2026-09-09 · `python3 tools/profile.py open_confidence_in_institutions`_
