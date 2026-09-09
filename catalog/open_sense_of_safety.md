# Sense of safety

`open_sense_of_safety` · shape **arcgis-hub** · source `open-ottawa`

- origin: <https://open.ottawa.ca/datasets/ottawa::sense-of-safety>
- fetched 2026-09-09 · **40 rows** · 7 columns
- csv · licence: https://ottawa.ca/en/city-hall/open-transparent-and-accountable-government/open-

## Columns

| column | kind | non-null | distinct | summary |
| --- | --- | --- | --- | --- |
| `Year_Année` | num | 100% | 5 | 2,020 · p25 2,021 · p50 2,022 · p95 2,024 · max 2,024  █▁▁█▁▁▁█▁▁▁█▁▁▁█ |
| `Region_Région` | cat | 100% | 1 | Ottawa 100% |
| `Question` | cat | 100% | 2 | How safe do you feel wal 50%, À quel point vous sentez 50% |
| `Response_Réponse` | cat | 100% | 8 | Very safe 12%, Somewhat safe 12%, Not very safe 12%, Not at all safe 12%, Tout à fait en sécurité 12%, Un peu en sécurité 12% |
| `Percent_Pourcent` | num | 100% | 16 | 4.00 · p25 10.75 · p50 24.00 · p95 46.05 · max 47.00  █▂▄▄▂▁▁▁▁▁▂▄▂▂▂█ |
| `Language_Langue` | cat | 100% | 2 | English 50%, Français 50% |
| `ObjectId` | num | 100% | 40 | 1.00 · p25 10.75 · p50 20.50 · p95 38.05 · max 40.00  █▅█▅█▅█▅▅█▅█▅█▅█ |

## Candidate questions

- (none templated)

_profiled 2026-09-09 · `python3 tools/profile.py open_sense_of_safety`_
