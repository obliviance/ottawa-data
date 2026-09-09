# Labour force

`open_labour_force` · shape **arcgis-hub** · source `open-ottawa`

- origin: <https://open.ottawa.ca/datasets/ottawa::labour-force>
- fetched 2026-09-09 · **180 rows** · 8 columns
- csv · licence: https://ottawa.ca/en/city-hall/open-transparent-and-accountable-government/open-

## Columns

| column | kind | non-null | distinct | summary |
| --- | --- | --- | --- | --- |
| `Year_Année` | num | 100% | 5 | 2,020 · p25 2,021 · p50 2,022 · p95 2,024 · max 2,024  █▁▁█▁▁▁█▁▁▁█▁▁▁█ |
| `Region_Région` | cat | 100% | 2 | Ottawa-Gatineau, Ontario 50%, Ottawa-Gatineau, partie  50% |
| `Indicator_Indicateur` | cat | 100% | 3 | Participation rate 33%, Employment rate 33%, Unemployment rate 33% |
| `Gender_Genre` | cat | 100% | 4 | Men+ 25%, Women+ 25%, Hommes+ 25%, Femmes+ 25% |
| `Age_Âge` | cat | 100% | 6 | 15 to 24 years 17%, 25 to 54 years 17%, 55 years and over 17%, 15 à 24 ans 17%, 25 à 54 ans 17%, 55 ans et plus 17% |
| `Percent_Pourcent` | num | 100% | 84 | 2.60 · p25 8.20 · p50 43.75 · p95 91.40 · max 93.50  █▁▁▁▁▃▁▄▁▂▃▂▁▁▃▄ |
| `Language_Langue` | cat | 100% | 2 | English 50%, Français 50% |
| `ObjectId` | num | 100% | 180 | 1.00 · p25 45.75 · p50 90.50 · p95 171 · max 180  █▇▇▇▇█▇▇▇▇█▇▇▇▇█ |

## Candidate questions

- (none templated)

_profiled 2026-09-09 · `python3 tools/profile.py open_labour_force`_
