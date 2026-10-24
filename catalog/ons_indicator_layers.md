# Ottawa Neighbourhood Study — indicator metadata

`ons_indicator_layers` · shape **json-api** · source `ons`

- origin: <https://ons-sqo.ca/wp-json/ons/v1/get-data/layers>
- fetched 2026-10-24 · **386 rows** · 25 columns
- `Polygon attribute` = indicator_id in ons_indicator_values

## Columns

| column | kind | non-null | distinct | summary |
| --- | --- | --- | --- | --- |
| `Category1` | cat | 100% | 9 | People 28%, Health and care 18%, Money and work 14%, Getting around 10%, Housing 8%, Food 8% |
| `Category2` | text | 100% | 37 | e.g. Alcohol and cannabis s, Banks and money servic, Mental health supports |
| `Category3` | id/text | 100% | 368 | e.g. # of cannabis stores, # of cannabis stores p, Average distance to th |
| `Category4` | cat | 100% | 1 |  100% |
| `Category1_fr` | cat | 100% | 9 | Les gens 28%, Santé et soins 18%, Argent et travail 14%, Se déplacer 10%, Logement 8%, Alimentation 8% |
| `Category2_fr` | text | 100% | 36 | e.g. Magasins d'alcool et d, Banques et services fi, Soutiens à la santé me |
| `Category3_fr` | id/text | 100% | 362 | e.g. # de magasins de canna, # de magasins de canna, Distance moyenne des 3 |
| `Category4_fr` | cat | 100% | 1 |  100% |
| `Date represented` | date | 100% | 37 | 2017-01-01 → 2026-01-01, 12 gaps >30d |
| `Date published` | date | 100% | 23 | 2024-01-03 → 2026-09-02, 6 gaps >30d |
| `Date represented_fr` | text | 100% | 37 | e.g. Le 6 septembre, 2023, Le 12 janvier, 2024, Le 18 septembre, 2023 |
| `Date published_fr` | text | 100% | 56 | e.g. Le 3 janvier, 2024, Le 23 janvier, 2024, Le 1 mars, 2024 |
| `Description` | text | 100% | 270 | e.g. # of cannabis stores., # of cannabis stores p, Average distance to th |
| `Source` | cat | 100% | 24 | 2021 Statistics Canada C 54%, ONS Mental Health Suppor 7%, ONS Food Environment Dat 6%, OpenStreetMap 5%, Ottawa Police Service 4%, City of Ottawa via Open  4% |
| `Description_fr` | text | 100% | 271 | e.g. # de magasins de canna, # de magasins de canna, Distance moyenne des 3 |
| `Source_fr` | cat | 100% | 25 | 2021 Recensement de la p 54%, Base de données du SQO s 7%, Base de données du SQO s 6%, OpenStreetMap 5%, Service de police d'Otta 4%, Ville d'Ottawa via Ottaw 4% |
| `More_Info` | text | 100% | 50 | e.g. , <a href="https://open., <a href="https://open. |
| `More_Info_fr` | text | 100% | 51 | e.g. , <a href="https://ouver, <a href="https://ouver |
| `Notes (internal)` | cat | 100% | 2 |  98%, Derived by uOttawa heat  2% |
| `Polygon attribute` | id/text | 100% | 355 | e.g. cannabis_num_region, cannabis_num_per_1000_, cannabis_dist_closest_ |
| `Polygon Layer` | cat | 100% | 1 | Yes 100% |
| `Point Layer` | cat | 100% | 1 |  100% |
| `Choropleth` | cat | 100% | 1 | Yes 100% |
| `nodata_en` | cat | 100% | 1 | Data not available 100% |
| `nodata_fr` | cat | 100% | 1 | Données non disponibles 100% |

## Candidate questions

- (none templated)

_profiled 2026-10-24 · `python3 tools/profile.py ons_indicator_layers`_
