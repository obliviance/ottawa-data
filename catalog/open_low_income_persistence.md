# Low income persistence

`open_low_income_persistence` · shape **arcgis-hub** · source `open-ottawa`

- origin: <https://open.ottawa.ca/datasets/ottawa::low-income-persistence>
- fetched 2026-09-09 · **108 rows** · 7 columns
- csv · licence: https://ottawa.ca/en/city-hall/open-transparent-and-accountable-government/open-

## Columns

| column | kind | non-null | distinct | summary |
| --- | --- | --- | --- | --- |
| `Years_Années` | cat | 100% | 6 | 2017/2018 17%, 2018/2019 17%, 2019/2020 17%, 2020/2021 17%, 2021/2022 17%, 2022/2023 17% |
| `Region_Région` | cat | 100% | 2 | Ottawa-Gatineau- partie  50%, Ottawa-Gatineau- Ontario 50% |
| `Group_Groupe` | cat | 100% | 6 | Âge 22%, Age 22%, Composition de la famill 17%, Family composition 17%, Sexe 11%, Sex 11% |
| `Sub_group_Sous_groupe` | cat | 100% | 18 | Hommes 6%, Femmes 6%, 18 à 24 ans 6%, 25 à 54 ans 6%, 55 à 64 ans 6%, 65 ans et plus 6% |
| `Percent_Pourcent` | num | 100% | 50 | 46.30 · p25 62.90 · p50 68.35 · p95 79.46 · max 84.50  ▁▁▁▃▂▁▆▆▄▄█▂▅▄▁▁ |
| `Language_Langue` | cat | 100% | 2 | Français 50%, English 50% |
| `ObjectId` | num | 100% | 108 | 1.00 · p25 27.75 · p50 54.50 · p95 103 · max 108  ███▇██▇██▇██▇███ |

## Candidate questions

- (none templated)

_profiled 2026-09-09 · `python3 tools/profile.py open_low_income_persistence`_
