# Youth not in employment, education or training

`open_youth_not_in_employment_education_or_training` · shape **arcgis-hub** · source `open-ottawa`

- origin: <https://open.ottawa.ca/datasets/ottawa::youth-not-in-employment-education-or-training>
- fetched 2026-09-09 · **36 rows** · 9 columns
- csv · licence: https://ottawa.ca/en/city-hall/open-transparent-and-accountable-government/open-

## Columns

| column | kind | non-null | distinct | summary |
| --- | --- | --- | --- | --- |
| `Year_Année` | num | 100% | 2 | 2,023 · p25 2,023 · p50 2,024 · p95 2,024 · max 2,024  █▁▁▁▁▁▁▁▁▁▁▁▁▁▁█ |
| `Region_Région` | cat | 100% | 2 | Ottawa-Gatineau, partie  50%, Ottawa-Gatineau, Ontario 50% |
| `Group_Groupe` | cat | 100% | 6 | Non racisé 17%, Racisé 17%, Population totale 17%, Not racialized 17%, Racialized 17%, Total population 17% |
| `Gender_Genre` | cat | 100% | 6 |   Femmes+ 17%,   Hommes+ 17%, Total, tous les genres 17%,   Men+ 17%,   Women+ 17%, Total, all genders 17% |
| `Percent_Pourcent` | num | 100% | 17 | 8.10 · p25 9.40 · p50 10.80 · p95 13.32 · max 13.70  ▄▁██▄▁█▄▄█▄█▁▄▄▄ |
| `l95` | num | 100% | 16 | 5.80 · p25 7.50 · p50 8.60 · p95 10.62 · max 11.00  ▄▁▁▄▁▂▁▆▄▁▁█▁▂▄▂ |
| `u95` | num | 100% | 18 | 10.60 · p25 11.70 · p50 12.95 · p95 16.80 · max 17.40  █▁▂▂▄▄▄▆▁▁▁▂▁▁▂▂ |
| `Language_Langue` | cat | 100% | 2 | Français 50%, English 50% |
| `ObjectId` | num | 100% | 36 | 1.00 · p25 9.75 · p50 18.50 · p95 34.25 · max 36.00  █▅▅▅▅█▅▅▅▅█▅▅▅▅█ |

## Candidate questions

- (none templated)

_profiled 2026-09-09 · `python3 tools/profile.py open_youth_not_in_employment_education_or_training`_
