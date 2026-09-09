# Sense of community belonging

`open_sense_of_community_belonging` · shape **arcgis-hub** · source `open-ottawa`

- origin: <https://open.ottawa.ca/datasets/ottawa::sense-of-community-belonging>
- fetched 2026-09-09 · **102 rows** · 13 columns
- csv · licence: https://ottawa.ca/en/city-hall/open-transparent-and-accountable-government/open-

## Columns

| column | kind | non-null | distinct | summary |
| --- | --- | --- | --- | --- |
| `Year_Année` | num | 100% | 1 | 2,024 · p25 2,024 · p50 2,024 · p95 2,024 · max 2,024   |
| `Region_Région` | cat | 100% | 2 | Ottawa-Gatineau, Ontario 50%, Ottawa-Gatineau, partie  50% |
| `Question` | cat | 100% | 2 | How would you describe y 50%, Comment décririez-vous v 50% |
| `Response_Réponse` | cat | 100% | 6 | Very weak or somewhat we 17%, Très faible ou plus ou m 17%, Très fort ou plus ou moi 17%, Aucune opinion 17%, Very strong or somewhat  17%, No opinion 17% |
| `Group_Groupe` | cat | 100% | 12 | Age 18%, Âge 18%, Niveau de scolarité le p 12%, Education level 12%, Genre 6%, Gender 6% |
| `Sub_group_Sous_groupe` | text | 100% | 34 | e.g. 65 to 74 years old, 65 à 74 ans, 75 ans et plus |
| `Percent_Pourcent` | num | 100% | 45 | 4.80 · p25 13.32 · p50 40.50 · p95 53.40 · max 60.80  ▂█▅▂▁▁▁▁▃▄▇█▇▂▁▁ |
| `F95lcl` | num | 100% | 49 | 2.60 · p25 9.85 · p50 34.10 · p95 48.29 · max 51.40  ▂▅█▁▁▁▁▁▂▄▃█▆▃▁▃ |
| `F95ucl` | num | 100% | 48 | 8.70 · p25 18.65 · p50 46.60 · p95 60.29 · max 69.40  ▃▅▄▃▁▁▁▁▁▅▅█▅▂▁▁ |
| `Data_quality_Qualité_des_données` | text | 0% | 0 | e.g.  |
| `Notes_Remarques` | text | 0% | 0 | e.g.  |
| `Language_Langue` | cat | 100% | 2 | English 50%, Français 50% |
| `ObjectId` | num | 100% | 102 | 1.00 · p25 26.25 · p50 51.50 · p95 96.95 · max 102  █▇▇█▇▇█▇▇█▇▇█▇▇█ |

## Candidate questions

- (none templated)

_profiled 2026-09-09 · `python3 tools/profile.py open_sense_of_community_belonging`_
