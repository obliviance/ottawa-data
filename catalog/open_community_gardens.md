# Community Gardens

`open_community_gardens` · shape **arcgis-hub** · source `open-ottawa`

- origin: <https://open.ottawa.ca/datasets/ottawa::community-gardens>
- fetched 2026-09-09 · **83 rows** · 13 columns
- csv · licence: https://ottawa.ca/en/city-hall/get-know-your-city/open-data#open-data-licence-ve

## Columns

| column | kind | non-null | distinct | summary |
| --- | --- | --- | --- | --- |
| `X` | num | 100% | 82 | -8,464,430 · p25 -8,432,309 · p50 -8,425,073 · p95 -8,411,336 · max -8,388,221  ▁▁▁▂▁▂▃▅█▅▁▁▁▁▁▁ |
| `Y` | num | 100% | 82 | 5,646,762 · p25 5,677,172 · p50 5,684,946 · p95 5,691,605 · max 5,698,003  ▁▁▁▁▁▁▂▁▂▄▃▄█▆▂▁ |
| `OBJECTID` | num | 100% | 83 | 1.00 · p25 55.50 · p50 1,001 · p95 1,662 · max 2,285  █▁▂▁▁▁▄▄▁▃▁▇▁▁▁▁ |
| `GARDEN` | id/text | 100% | 82 | e.g. Orleans Community Gard, Gloucester Allotment G, Michele Heights Commun |
| `STATUS` | cat | 100% | 3 | Existing 69%, New 28%, In Development 4% |
| `GARDEN_FR` | id/text | 100% | 82 | e.g. Jardin Communautaire d, Jardins collectifs de , Jardin Communautaire d |
| `STATUS_FR` | cat | 96% | 2 | Actuel 96%, En cours de développemen 4% |
| `LEGAL_ADDR` | id/text | 100% | 81 | e.g. 3350 St Joseph Blvd., Corner of Weir and And, 2955 Michèle Dr. |
| `NOTES` | text | 0% | 0 | e.g.  |
| `LINK_FR` | cat | 100% | 1 | http://www.alimentationj 100% |
| `LEGAL_ADDR_FR` | id/text | 100% | 82 | e.g. 3350, boul. St Joseph, À l'angle du ch. Weir , 2955, prom. Michèle |
| `LINK` | cat | 100% | 1 | http://justfood.ca/commu 100% |
| `GlobalID` | id/text | 100% | 83 | e.g. {A8AB3825-8D34-42B3-B1, {D19535E3-166D-4754-BF, {71C5B7F0-C3A4-4642-9B |

## Candidate questions

- (none templated)

_profiled 2026-09-09 · `python3 tools/profile.py open_community_gardens`_
