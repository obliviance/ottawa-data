# Pedestrian Network 

`open_pedestrian_network` · shape **arcgis-hub** · source `open-ottawa`

- origin: <https://open.ottawa.ca/datasets/ottawa::pedestrian-network->
- fetched 2026-09-09 · **20,298 rows** · 20 columns
- csv · licence: https://ottawa.ca/en/city-hall/get-know-your-city/open-data#open-data-licence-ve

## Columns

| column | kind | non-null | distinct | summary |
| --- | --- | --- | --- | --- |
| `OBJECTID` | num | 100% | 20,298 | 27,833 · p25 32,913 · p50 38,000 · p95 47,146 · max 52,081  ██▇▇▇▇▇▇█▇▇▇▇▂▁▂ |
| `WALK_TYPE` | cat | 100% | 3 | SIDEWALK 71%, MUP 14%, PATH 14% |
| `GLOBALID` | id/text | 100% | 20,298 | e.g. {9DDE210A-B57C-4074-82, {B30B38F0-7AF3-4C43-98, {A84FE16C-A063-45C0-9F |
| `SHAPE_Length` | num | 100% | 20,266 | 0.00 · p25 56.82 · p50 89.37 · p95 418 · max 6,176  █▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁ |
| `YEAR` | num | 0% | 7 | 2,011 · p25 2,015 · p50 2,016 · p95 2,017 · max 2,018  ▁▁▁▁▁▁▁▁▁▅▁▆▁█▁▁ |
| `DESCRIPTION_EN` | cat | 100% | 2 | Sidewalks and Paths 86%, Multi-Use Pathway 14% |
| `DESCRIPTION_FR` | cat | 100% | 2 | Trottoirs et sentiers 86%, Sentier polyvalent 14% |
| `SWK_PROJ_NO` | cat | 0% | 21 | 2016-5 18%, PTIF-2 11%, 2016-9 8%, 2016-10 8%, 2016-1 5%, 2016-4 5% |
| `SWK_PROJ_DESCR_FR` | cat | 0% | 21 | Rue Iris – du chemin Gre 18%, Promenade Sherway FITC – 11%, Boulevard Saint-Laurent  8%, Promenade Gardenway - du 8%, Chemin Teron – De la pro 5%, Chemin Cyrville (côté su 5% |
| `SWK_PROJ_DESCR_EN` | cat | 0% | 21 | Iris - Greenbank to Wood 18%, Sherway Drive PTIF - Fab 11%, St Laurent Blvd, east si 8%, Gardenway - Thicket to P 8%, Teron Road - Campeau to  5%, Cyrville Rd, south side  5% |
| `FINAL_COST` | date | 0% | 5 | 1970-01-01 → 1970-01-01 |
| `TYPE_EN` | cat | 0% | 4 | Concrete sidewalk 71%, Asphalt pathway 18%, Asphalt sidewalk 8%, Concrete / asphalt sidew 3% |
| `TYPE_FR` | cat | 0% | 4 | Trottoir en béton 71%, Sentier en asphalte 18%, Trottoir en asphalte 8%, Trottoir en béton / asph 3% |
| `SWK_PROJECT_FR` | cat | 0% | 1 | Projets achevés – Plan d 100% |
| `NOTES` | text | 0% | 0 | e.g.  |
| `SWK_PROJECT_EN` | cat | 0% | 1 | Completed Projects – Ott 100% |
| `CREATED_USER` | cat | 1% | 2 | RICHARDSSA 99%, EATONJO 1% |
| `CREATED_DATE` | date | 1% | 202 | 2017-10-31 → 2024-06-11, 11 gaps >30d |
| `LAST_EDITED_USER` | cat | 16% | 2 | RICHARDSSA 100%, EATONJO 0% |
| `LAST_EDITED_DATE` | date | 16% | 369 | 2018-01-23 → 2024-06-11, 10 gaps >30d |

## Candidate questions

- Trend / seasonality of open_pedestrian_network over `YEAR`; structural breaks?

_profiled 2026-09-09 · `python3 tools/profile.py open_pedestrian_network`_
