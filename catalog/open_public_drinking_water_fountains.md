# Public Drinking Water Fountains

`open_public_drinking_water_fountains` · shape **arcgis-hub** · source `open-ottawa`

- origin: <https://open.ottawa.ca/datasets/ottawa::public-drinking-water-fountains>
- fetched 2026-09-09 · **112 rows** · 22 columns
- csv · licence: https://ottawa.ca/en/city-hall/get-know-your-city/open-data#open-data-licence-ve

## Columns

| column | kind | non-null | distinct | summary |
| --- | --- | --- | --- | --- |
| `X` | num | 100% | 112 | -8,464,634 · p25 -8,431,417 · p50 -8,425,245 · p95 -8,404,006 · max -8,399,598  ▁▁▁▂▁▂▂▃▃█▄▄▂▂▂▂ |
| `Y` | num | 100% | 112 | 5,642,037 · p25 5,676,675 · p50 5,684,026 · p95 5,694,594 · max 5,701,153  ▁▁▁▁▁▂▂▂▃▆▄▇█▅▂▁ |
| `OBJECTID` | num | 100% | 112 | 1.00 · p25 30.75 · p50 60.50 · p95 113 · max 119  █▇▇▆▇█▅█▅▆█▇▇█▇█ |
| `BUILDING_NAME` | id/text | 100% | 112 | e.g. Ottawa Public Library , Ottawa Public Library , Ottawa Public Library  |
| `BUILDING_NAME_FR` | id/text | 100% | 112 | e.g. Succursale Hazeldean d, Succursale Centennial , Succursale Rideau de l |
| `ADDRESS` | id/text | 100% | 107 | e.g. 50 Castlefrank Rd, 3870 Old Richmond Rd, 377 Rideau St |
| `ADDRESS_FR` | id/text | 100% | 107 | e.g. 50, chemin Castlefrank, 3870, chemin Old Richm, 377, rue Rideau |
| `GLOBALID` | id/text | 100% | 112 | e.g. {85F99C5D-7393-4BEB-98, {EC20C337-2AED-412A-9A, {C417AC44-B538-4B09-AE |
| `CREATED_DATE` | date | 25% | 29 | 2023-10-25 → 2023-11-22 |
| `LAST_EDITED_DATE` | date | 100% | 112 | 2023-09-14 → 2023-11-24, 1 gaps >30d |
| `OPEN_YEAR_ROUND` | cat | 100% | 2 | Yes 70%, No 30% |
| `OPEN_YEAR_ROUND_FR` | cat | 99% | 2 | Oui 69%, Non 31% |
| `HOURS_OF_OPERATION` | cat | 100% | 3 | Open during facility bus 79%, Open during park busines 21%, Open during park busines 1% |
| `HOURS_OF_OPERATION_FR` | cat | 100% | 3 | Ouvert durant les heures 79%, Ouvert durant les heures 21%, Ouvert durant les heures 1% |
| `CLOSURES` | cat | 11% | 2 | Sundays 77%, Saturdays, Sundays 23% |
| `FERMETURE` | cat | 11% | 2 | Dimanche 77%, Samedi et dimanche 23% |
| `OPEN_SEASON` | cat | 30% | 4 | May - October 74%, October - March 18%, May - September 6%, September - June 3% |
| `OPEN_SEASON_FR` | cat | 30% | 4 | De mai à octobre 74%, D’octobre à mars 18%, De mai à septembre 6%, De septembre à juin 3% |
| `INSIDE_OUTSIDE` | cat | 100% | 2 | Inside 79%, Outside 21% |
| `INSIDE_OUTSIDE_FR` | cat | 100% | 2 | Intérieur 79%, Extérieur 21% |
| `URL` | text | 100% | 86 | e.g. https://biblioottawali, https://biblioottawali, https://biblioottawali |
| `URL_FR` | text | 100% | 86 | e.g. https://biblioottawali, https://biblioottawali, https://biblioottawali |

## Candidate questions

- (none templated)

_profiled 2026-09-09 · `python3 tools/profile.py open_public_drinking_water_fountains`_
