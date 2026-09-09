# Parks and Greenspace

`open_parks_and_greenspace` · shape **arcgis-hub** · source `open-ottawa` · **spatial**

- origin: <https://open.ottawa.ca/datasets/ottawa::parks-and-greenspace>
- fetched 2026-09-09 · **1,370 rows** · 33 columns
- geojson · licence: https://ottawa.ca/en/city-hall/get-know-your-city/open-data#open-data-licence-ve

## Columns

| column | kind | non-null | distinct | summary |
| --- | --- | --- | --- | --- |
| `OBJECTID` | num | 100% | 1,370 | 1.00 · p25 343 · p50 686 · p95 1,302 · max 1,370  ██▇█▇█▇██▇█▇█▇██ |
| `PARK_ID` | num | 100% | 1,370 | 2.00 · p25 587 · p50 1,275 · p95 2,658 · max 2,731  ▅▄▅▅▅▄▄▂▂▆▃▂▂▃▇█ |
| `NAME` | id/text | 100% | 1,246 | e.g. Whiterock Park, Dr. John Hopps Park, Upper Duck Island |
| `NAME_FR` | id/text | 99% | 1,240 | e.g. Parc Whiterock, Parc du Dr-John-Hopps, Île Upper Duck |
| `ADDRESS` | id/text | 99% | 1,351 | e.g. 1245 Matheson Road, Gl, 300 Den Haag Drive, Ot, 2001 Rockcliffe Parkwa |
| `ADDRESS_FR` | id/text | 99% | 1,344 | e.g. 1245, chemin Matheson,, 300, promenade Den-Haa, 2001, promenade Rockcl |
| `PARK_TYPE` | cat | 98% | 6 | Active Recreation 64%, Passive Recreation 36%, Unknown 0%, Active recreation 0%, Linear Park 0%, <Null> 0% |
| `PARK_TYPE_FR` | cat | 98% | 5 | Loisirs dynamiques 64%, Loisirs passifs 36%, Parc linear 0%, <Null> 0%, Unknow 0% |
| `DOG_DESIGNATION` | num | 98% | 5 | 0.00 · p25 1.00 · p50 3.00 · p95 4.00 · max 4.00  ▂▁▁▄▁▁▁▁▁▁▁▂▁▁▁█ |
| `DOG_DESIGNATION_FR` | num | 98% | 5 | 0.00 · p25 1.00 · p50 3.00 · p95 4.00 · max 4.00  ▂▁▁▄▁▁▁▁▁▁▁▂▁▁▁█ |
| `WATERBODY_ACCESS` | cat | 97% | 2 | no/non 83%, yes/oui 17% |
| `WARD` | num | 99% | 25 | 1.00 · p25 5.00 · p50 11.00 · p95 23.00 · max 31.00  ▆█▆▅▅▄▃▄▂▅▇▆▃▁▁▁ |
| `WARD_NAME` | text | 99% | 31 | e.g. Beacon Hill-Cyrville, Rideau-Rockcliffe, Rideau-Vanier |
| `WARD_NAME_FR` | text | 99% | 31 | e.g. Beacon Hill-Cyrville, Rideau-Rockcliffe, Rideau-Vanier |
| `PARK_DEDICATION_STATUS` | num | 99% | 11 | 0.00 · p25 0.00 · p50 0.00 · p95 9.00 · max 11.00  █▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁ |
| `ACCESSIBLE` | cat | 97% | 2 | no/non 80%, yes/oui 20% |
| `OPEN` | cat | 3% | 2 | yes/oui 67%, no/non 33% |
| `LATITUDE` | num | 97% | 1,333 | 45.03 · p25 45.28 · p50 45.35 · p95 45.48 · max 45.52  ▁▁▁▁▁▁▂▆▇▆█▅▅▆▅▂ |
| `LONGITUDE` | num | 97% | 1,322 | -76.26 · p25 -75.83 · p50 -75.71 · p95 -75.47 · max -75.34  ▁▁▁▁▁▄▄▃▅█▇▄▃▄▁▁ |
| `SAP_FLOC` | id/text | 94% | 1,257 | e.g. R-PKS-023-1011, R-PKS-004-0259, R-PKS-021-0958 |
| `MODIFIED_DATE` | date | 98% | 1,352 | 2022-11-15 → 2026-07-16, 11 gaps >30d |
| `CREATED_DATE` | date | 14% | 194 | 2013-12-16 → 2025-12-08, 38 gaps >30d |
| `DOG_DESIGNATION_DETAILS` | text | 97% | 71 | e.g. Dogs are allowed but m, Dogs are not allowed i, Dogs may be off leash. |
| `DOG_DESIGNATION_DETAILS_FR` | text | 97% | 79 | e.g. Les chiens sont permis, Les chiens ne sont pas, Signifie que les chien |
| `Shape_Length` | num | 100% | 1,370 | 56.55 · p25 485 · p50 845 · p95 4,096 · max 72,713  █▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁ |
| `Shape_Area` | num | 100% | 1,370 | 97.73 · p25 5,054 · p50 12,905 · p95 120,880 · max 3,055,012  █▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁ |
| `SAP_ID` | num | 93% | 1,255 | 1.00 · p25 319 · p50 646 · p95 1,423 · max 1,509  ▇▇▇▇▇▇▇▇█▇▇▂▃▆▅▆ |
| `PARK_CATEGORY` | cat | 98% | 12 | Neighbourhood Park 22%, Parkette 21%, Greenspace 17%, Community Park 12%, Urban Plaza 9%, Urban Parkette 8% |
| `PARK_CATEGORY_FR` | cat | 98% | 14 | Parc de quartier 22%, Miniparc 21%, Espace vert 17%, Parc communautaire 12%, Place urbaine 9%, Miniparc urbain 8% |
| `ADOPTION_STATUS` | cat | 0% | 1 | Available 100% |
| `DEVELOPER_MAINTAINED` | cat | 0% | 1 | no/non 100% |
| `ADOPTION_STATUS_FR` | cat | 0% | 1 | Disponible 100% |
| `geometry` | id/text | 100% | 1,370 | e.g. {"type": "Polygon", "c, {"type": "Polygon", "c, {"type": "Polygon", "c |

## Candidate questions

- `PARK_ID` by `WARD` — equity gradient? (join ONS income)
- Trend / seasonality of open_parks_and_greenspace over `MODIFIED_DATE`; structural breaks?
- Spatial clustering of open_parks_and_greenspace; overlay wards + the decision timeline

_profiled 2026-09-09 · `python3 tools/profile.py open_parks_and_greenspace`_
