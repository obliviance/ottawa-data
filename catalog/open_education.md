# Education

`open_education` · shape **arcgis-hub** · source `open-ottawa`

- origin: <https://open.ottawa.ca/datasets/ottawa::education>
- fetched 2026-09-09 · **648 rows** · 8 columns
- csv · licence: https://ottawa.ca/en/city-hall/open-transparent-and-accountable-government/open-

## Columns

| column | kind | non-null | distinct | summary |
| --- | --- | --- | --- | --- |
| `Year_Année` | num | 100% | 4 | 2,006 · p25 2,010 · p50 2,014 · p95 2,021 · max 2,021  █▁▁▁▁█▁▁▁▁█▁▁▁▁█ |
| `Region_Région` | cat | 100% | 2 | Ottawa - Gatineau (Ontar 50%, Ottawa-Gatineau, partie  50% |
| `Group_Groupe` | cat | 100% | 5 | Race 35%, Identité raciale 35%, Immigration 19%, Genre 6%, Gender 6% |
| `Sub_group_Sous_groupe` | text | 100% | 37 | e.g. Latin American, Femmes+, Latino-Américain |
| `Education_level_Niveau_d_éducation` | cat | 100% | 10 | No certificate, diploma  12%, Certificat ou diplôme d' 12%, Postsecondary certificat 12%, Bachelor’s degree or hig 12%, High (secondary) school  12%, Aucun certificat, diplôm 12% |
| `Percent_Pourcent` | num | 100% | 211 | 0.00 · p25 17.27 · p50 23.80 · p95 100 · max 100  ▁▃▆█▅▄▂▂▁▁▁▁▁▁▁▂ |
| `Language_Langue` | cat | 100% | 2 | English 50%, Français 50% |
| `ObjectId` | num | 100% | 648 | 1.00 · p25 163 · p50 324 · p95 616 · max 648  █▇█▇█▇█▇▇█▇█▇█▇█ |

## Candidate questions

- Trend / seasonality of open_education over `Year_Année`; structural breaks?

_profiled 2026-09-09 · `python3 tools/profile.py open_education`_
