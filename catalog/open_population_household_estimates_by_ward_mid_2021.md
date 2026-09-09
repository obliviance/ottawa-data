# Population & Household Estimates by Ward – Mid 2021

`open_population_household_estimates_by_ward_mid_2021` · shape **arcgis-hub** · source `open-ottawa` · **spatial**

- origin: <https://open.ottawa.ca/datasets/ottawa::population-household-estimates-by-ward-mid-2021>
- fetched 2026-09-09 · **23 rows** · 9 columns
- geojson · licence: https://ottawa.ca/en/city-hall/get-know-your-city/open-data#open-data-licence-ve

## Columns

| column | kind | non-null | distinct | summary |
| --- | --- | --- | --- | --- |
| `OBJECTID` | num | 100% | 23 | 1.00 · p25 6.50 · p50 12.00 · p95 21.90 · max 23.00  █▄█▄▄█▄█▄▄█▄▄█▄█ |
| `WARD_NUM` | num | 100% | 23 | 1.00 · p25 6.50 · p50 12.00 · p95 21.90 · max 23.00  █▄█▄▄█▄█▄▄█▄▄█▄█ |
| `NAME_EN` | cat | 100% | 23 | Ward 23 4%, Ward 7 4%, Ward 20 4%, Ward 11 4%, Ward 8 4%, Ward 22 4% |
| `NAME_FR` | cat | 100% | 23 | Quartier 23 4%, Quartier 7 4%, Quartier 20 4%, Quartier 11 4%, Quartier 8 4%, Quartier 22 4% |
| `WARD_EN` | cat | 100% | 23 | KANATA SOUTH 4%, BAY 4%, OSGOODE 4%, BEACON HILL-CYRVILLE 4%, COLLEGE 4%, GLOUCESTER-SOUTH NEPEAN 4% |
| `WARD_FR` | cat | 100% | 23 | KANATA-SUD 4%, BAIE 4%, OSGOODE 4%, BEACON HILL-CYRVILLE 4%, COLLÈGE 4%, GLOUCESTER-NEPEAN-SUD 4% |
| `POPULATION` | num | 100% | 23 | 26,430 · p25 39,600 · p50 45,580 · p95 60,420 · max 66,540  ▂▂▁▄▂▆▂██▄▂▂▁▂▁▂ |
| `HOUSEHOLDS_M_NAGE` | num | 100% | 23 | 9,480 · p25 16,295 · p50 19,550 · p95 25,589 · max 28,890  ▂▂▂▁▂▆▂▄▆█▆▁▂▂▁▂ |
| `geometry` | cat | 100% | 23 | {"type": "Polygon", "coo 4%, {"type": "Polygon", "coo 4%, {"type": "Polygon", "coo 4%, {"type": "Polygon", "coo 4%, {"type": "Polygon", "coo 4%, {"type": "Polygon", "coo 4% |

## Candidate questions

- (none templated)

_profiled 2026-09-09 · `python3 tools/profile.py open_population_household_estimates_by_ward_mid_2021`_
