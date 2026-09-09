# Better Buildings Ottawa 2022

`open_better_buildings_ottawa_2022` · shape **arcgis-hub** · source `open-ottawa` · **spatial**

- origin: <https://open.ottawa.ca/datasets/ottawa::better-buildings-ottawa-2022>
- fetched 2026-09-09 · **452 rows** · 21 columns
- csv · licence: https://ottawa.ca/en/city-hall/get-know-your-city/open-data#open-data-licence-ve

## Columns

| column | kind | non-null | distinct | summary |
| --- | --- | --- | --- | --- |
| `X` | num | 100% | 405 | -8,481,854 · p25 -8,430,754 · p50 -8,426,131 · p95 -8,405,292 · max -8,384,531  ▁▁▁▁▁▂▁▂▅█▃▁▁▁▁▁ |
| `Y` | num | 100% | 407 | 5,625,958 · p25 5,677,554 · p50 5,684,416 · p95 5,692,356 · max 5,703,112  ▁▁▁▁▁▁▁▁▁▂▄▅█▅▁▁ |
| `state` | cat | 100% | 1 | Final: Disclosed (map, s 100% |
| `cycles` | cat | 100% | 6 | 2019 Calendar Year,2020  70%, 2022 Calendar Year 27%, 2020 Calendar Year,2022  3%, 2021 Calendar Year,2022  0%, 2020 Calendar Year,2021  0%, 2019 Calendar Year,2020  0% |
| `address` | id/text | 100% | 444 | e.g. 1000 Castle Hill Cres, 1000 Teron Rd, 1001 Farrar Road |
| `property_name` | id/text | 100% | 451 | e.g. 1000 Castlehill, 1821 BE- Elsie Staplef, 1001 Farrar Road |
| `property_type` | text | 100% | 29 | e.g. Multifamily Housing, Social/Meeting Hall, Office |
| `year_built` | num | 69% | 90 | 1,865 · p25 1,962 · p50 1,973 · p95 2,014 · max 2,021  ▁▁▁▁▁▁▂▁▂▆█▇▅▅▃▃ |
| `province` | cat | 100% | 1 | ON 100% |
| `city` | cat | 100% | 6 | Ottawa 97%, Kanata 1%, Nepean 1%, Navan 0%, Gloucester 0%, Kemptville 0% |
| `postal_code` | id/text | 100% | 382 | e.g. K2C 3L7, K2K1R1, K2K0B3 |
| `Longitude` | num | 100% | 405 | -76.19 · p25 -75.73 · p50 -75.69 · p95 -75.51 · max -75.32  ▁▁▁▁▁▂▁▂▅█▃▁▁▁▁▁ |
| `Latitude` | num | 100% | 407 | 45.03 · p25 45.35 · p50 45.40 · p95 45.45 · max 45.52  ▁▁▁▁▁▁▁▁▂▂▄▅█▅▁▁ |
| `primary_contact_organization` | cat | 94% | 21 | City of Ottawa 46%, Ottawa Community Housing 9%, Osgoode Properties 8%, Condominium Groups 7%, Colonnade Bridgeport 6%, Minto Group 5% |
| `energy_star` | num | 56% | 88 | 1.00 · p25 28.00 · p50 51.00 · p95 93.00 · max 100  ▄▇▃▃▅▅▄▆▆▃█▅▅▄▄▃ |
| `site_eui__ekWh_m__` | num | 100% | 168 | 8.33 · p25 197 · p50 250 · p95 682 · max 8,544  █▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁ |
| `source_eui__ekWh_m__` | num | 99% | 201 | 16.66 · p25 269 · p50 353 · p95 1,006 · max 16,750  █▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁ |
| `total_ghgs__tCO_e_` | num | 100% | 424 | 0.30 · p25 35.35 · p50 102 · p95 1,090 · max 3,809  █▂▁▁▁▁▁▁▁▁▁▁▁▁▁▁ |
| `ghg_intensity__kgCO_e_m__` | num | 100% | 325 | 0.20 · p25 19.75 · p50 29.90 · p95 68.45 · max 471  █▆▁▁▁▁▁▁▁▁▁▁▁▁▁▁ |
| `water_use_intensity__l_m__` | num | 55% | 161 | 0.00 · p25 308 · p50 765 · p95 3,264 · max 650,250  █▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁ |
| `ObjectId` | num | 100% | 452 | 1.00 · p25 114 · p50 226 · p95 429 · max 452  █▇▇▇▇█▇▇▇▇█▇▇▇▇█ |

## Candidate questions

- Spatial clustering of open_better_buildings_ottawa_2022; overlay wards + the decision timeline

_profiled 2026-09-09 · `python3 tools/profile.py open_better_buildings_ottawa_2022`_
