# Emergency shelter use

`open_emergency_shelter_use` · shape **arcgis-hub** · source `open-ottawa`

- origin: <https://open.ottawa.ca/datasets/ottawa::emergency-shelter-use>
- fetched 2026-09-09 · **120 rows** · 5 columns
- csv · licence: https://ottawa.ca/en/city-hall/open-transparent-and-accountable-government/open-

## Columns

| column | kind | non-null | distinct | summary |
| --- | --- | --- | --- | --- |
| `Year_Année` | num | 100% | 12 | 2,014 · p25 2,017 · p50 2,020 · p95 2,025 · max 2,025  ███▁██▁██▁██▁███ |
| `Category_Catégorie` | cat | 100% | 10 | Jeunes seuls de 18 ans e 10%, Tous les clients 10%, Hommes adultes seuls 10%, Membres d'une famille 10%, Femmes adultes seules 10%, Single youth under 18 ye 10% |
| `Count_Nombre` | num | 100% | 58 | 147 · p25 1,058 · p50 3,131 · p95 8,577 · max 9,493  █▆▁▁▄▇▃▁▂▂▁▂▂▁▃▁ |
| `Language_Langue` | cat | 100% | 2 | Français 50%, English 50% |
| `ObjectId` | num | 100% | 120 | 1.00 · p25 30.75 · p50 60.50 · p95 114 · max 120  █▇█▇█▇█▇▇█▇█▇█▇█ |

## Candidate questions

- (none templated)

_profiled 2026-09-09 · `python3 tools/profile.py open_emergency_shelter_use`_
