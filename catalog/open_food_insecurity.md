# Food insecurity

`open_food_insecurity` · shape **arcgis-hub** · source `open-ottawa`

- origin: <https://open.ottawa.ca/datasets/ottawa::food-insecurity>
- fetched 2026-09-09 · **24 rows** · 8 columns
- csv · licence: https://ottawa.ca/en/city-hall/open-transparent-and-accountable-government/open-

## Columns

| column | kind | non-null | distinct | summary |
| --- | --- | --- | --- | --- |
| `Year_Année` | num | 100% | 6 | 2,019 · p25 2,020 · p50 2,022 · p95 2,024 · max 2,024  █▁▁█▁▁█▁▁█▁▁█▁▁█ |
| `Region_Région` | cat | 100% | 2 | Ottawa 50%, Ontario 50% |
| `Indicator_Indicateur` | cat | 100% | 2 | Food insecure (household 50%, Ménages en situation d'i 50% |
| `Percent_Pourcent` | num | 100% | 11 | 11.60 · p25 15.18 · p50 17.10 · p95 25.64 · max 25.70  ▄▄▁▄▄▄█▁▄▁▁▁▁▄▄█ |
| `F95lcl` | num | 100% | 12 | 8.00 · p25 12.00 · p50 15.95 · p95 24.13 · max 24.30  █▁▁▄▄▁▄█▁▄▁▄▁▄▄▄ |
| `F95ucl` | num | 100% | 12 | 15.10 · p25 17.77 · p50 18.45 · p95 29.10 · max 29.40  ▂▁▄█▁▂▁▁▁▁▁▂▂▂▁▂ |
| `Language_Langue` | cat | 100% | 2 | English 50%, Français 50% |
| `ObjectId` | num | 100% | 24 | 1.00 · p25 6.75 · p50 12.50 · p95 22.85 · max 24.00  █▄█▄█▄█▄▄█▄█▄█▄█ |

## Candidate questions

- (none templated)

_profiled 2026-09-09 · `python3 tools/profile.py open_food_insecurity`_
