# Someone to depend on

`open_someone_to_depend_on` · shape **arcgis-hub** · source `open-ottawa`

- origin: <https://open.ottawa.ca/datasets/ottawa::someone-to-depend-on>
- fetched 2026-09-09 · **256 rows** · 13 columns
- csv · licence: https://ottawa.ca/en/city-hall/open-transparent-and-accountable-government/open-

## Columns

| column | kind | non-null | distinct | summary |
| --- | --- | --- | --- | --- |
| `Year_Année` | date | 100% | 2 | 2024-01-01 → 2024-01-01 |
| `Region_Région` | cat | 100% | 2 | Ottawa-Gatineau, partie  50%, Ottawa-Gatineau, Ontario 50% |
| `Question` | cat | 100% | 2 | À quelle fréquence dirie 50%, How often would you say  50% |
| `Response_Réponse` | cat | 100% | 8 | Toujours 12%, Parfois 12%, Souvent 12%, Rarement ou jamais 12%, Sometimes 12%, Often 12% |
| `Group_Groupe` | cat | 100% | 12 | Age 19%, Âge 19%, Niveau de scolarité le p 12%, Education level 12%, Genre 6%, Gender 6% |
| `Sub_group_Sous_groupe` | text | 100% | 40 | e.g. Diplôme d'études secon, Femmes+, High school diploma or |
| `Percent_Pourcent` | num | 100% | 113 | 2.10 · p25 11.25 · p50 28.55 · p95 45.20 · max 57.60  ▄▇▂▃▅▃▁▂▃█▄▅▃▁▁▁ |
| `F95lcl` | num | 100% | 104 | 1.00 · p25 7.22 · p50 21.00 · p95 39.60 · max 49.00  ▇▄▂▄▄▂▂▂▃█▂▄▂▁▁▁ |
| `F95ucl` | num | 100% | 114 | 4.30 · p25 17.62 · p50 35.45 · p95 51.80 · max 65.70  ▃▆▃▄▄▅▁▁▅▇█▄▄▁▁▁ |
| `Data_quality_Qualité_des_données` | cat | 1% | 1 | E 100% |
| `Notes_Remarques` | cat | 3% | 2 | Use estimate with cautio 50%, Utiliser les estimations 50% |
| `Language_Langue` | cat | 100% | 2 | Français 50%, English 50% |
| `ObjectId` | num | 100% | 256 | 1.00 · p25 64.75 · p50 128 · p95 243 · max 256  ████████████████ |

## Candidate questions

- (none templated)

_profiled 2026-09-09 · `python3 tools/profile.py open_someone_to_depend_on`_
