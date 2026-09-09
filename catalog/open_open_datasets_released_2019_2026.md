# Open Datasets Released 2019-2026

`open_open_datasets_released_2019_2026` · shape **arcgis-hub** · source `open-ottawa`

- origin: <https://open.ottawa.ca/datasets/ottawa::open-datasets-released-2019-2026>
- fetched 2026-09-09 · **251 rows** · 11 columns
- csv · licence: https://ottawa.ca/en/city-hall/open-transparent-and-accountable-government/open-

## Columns

| column | kind | non-null | distinct | summary |
| --- | --- | --- | --- | --- |
| `Dataset_Name` | id/text | 100% | 250 | e.g. Red Light Camera Viola, Red Light Camera Viola, Electric Vehicle Charg |
| `Nom_de_l_ensemble_de_données` | id/text | 99% | 233 | e.g. Infractions relatives , Infractions relatives , Données relatives à l' |
| `Organization` | cat | 100% | 11 | City of Ottawa 73%, Ottawa Public Health 14%, Ottawa Public Library 6%, Ottawa Police Service 4%, OC Transpo 1%, Ottawa Neighbourhood Stu 0% |
| `Organisme` | cat | 100% | 11 | Ville d'Ottawa 78%, Santé publique Ottawa 9%, Bibliothèque publique d' 6%, Ottawa Police 4%, OC Transpo 1%, L’étude de quartiers d’O 0% |
| `Department` | cat | 99% | 17 | Finance and Corporate Se 18%, Public Works 18%, Ottawa Public Health 14%, Planning Real Estate and 11%, Community and Social Ser 10%, Office of the City Clerk 7% |
| `Direction_générale` | cat | 98% | 17 | Finances et Services org 19%, Services des travaux pub 18%, Santé publique Ottawa 14%, Services de la planifica 11%, Services sociaux et comm 10%, Bureau du greffier munic 7% |
| `Year` | num | 100% | 11 | 2,019 · p25 2,020 · p50 2,022 · p95 2,026 · max 2,026  ▄▁█▁▅▁▇▁▁▆▁▂▁▁▁▄ |
| `Month` | num | 100% | 15 | 1.00 · p25 2.00 · p50 4.00 · p95 11.00 · max 2,026  █▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁ |
| `Day` | num | 100% | 33 | 1.00 · p25 9.00 · p50 17.00 · p95 29.00 · max 2,026  █▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁ |
| `ObjectId` | text | 0% | 0 | e.g.  |
| `ObjectId2` | num | 100% | 251 | 1.00 · p25 63.50 · p50 126 · p95 238 · max 251  ██▇██▇██▇█▇██▇██ |

## Candidate questions

- Concentration in `Organization` — which actors dominate? (join entity spine)

_profiled 2026-09-09 · `python3 tools/profile.py open_open_datasets_released_2019_2026`_
