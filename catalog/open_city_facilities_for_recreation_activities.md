# City Facilities for Recreation Activities

`open_city_facilities_for_recreation_activities` · shape **arcgis-hub** · source `open-ottawa` · **spatial**

- origin: <https://open.ottawa.ca/datasets/ottawa::city-facilities-for-recreation-activities>
- fetched 2026-09-09 · **369 rows** · 21 columns
- geojson · licence: https://ottawa.ca/en/city-hall/get-know-your-city/open-data#open-data-licence-ve

## Columns

| column | kind | non-null | distinct | summary |
| --- | --- | --- | --- | --- |
| `OBJECTID` | num | 100% | 369 | 5.00 · p25 170 · p50 371 · p95 725 · max 757  ▆▆▅▆▇▆▂▄▃▅█▄▄▅▇▅ |
| `BUSINESS_ENTITY_DESC` | text | 100% | 251 | e.g. Blackburn Park, Goldridge Park, Richelieu Park |
| `BUSINESS_ENTITY_DESC_FR` | text | 99% | 250 | e.g. Parc Blackburn, Parc Goldridge, Parc Richelieu |
| `BUILDING_DESC` | id/text | 100% | 297 | e.g. Lois Kemp Arena, Historical School Hous, Richelieu-Vanier Commu |
| `BUILDING_DESC_FR` | id/text | 97% | 290 | e.g. Aréna Lois-Kemp, École historique no 1 , Centre communautaire R |
| `BUILDING_TYPE` | cat | 100% | 15 | Recreation Complex 21%, Field House 21%, Community Centre 17%, Community Building 11%, Arena 9%, Comfort Station 7% |
| `BUILDING_TYPE_FR` | cat | 100% | 15 | Complexe récréatif 21%, Pavillon 21%, Centre communautaire 17%, Édifice communautaire 11%, Aréna 9%, Bloc sanitaire 7% |
| `BUILDING_ELEMENT_DESC` | id/text | 35% | 128 | e.g. Richelieu-Vanier Commu, Jim Tubman Chevrolet R, J.G. Mlacak Centre |
| `BUILDING_ELEMENT_DESC_FR` | id/text | 34% | 122 | e.g. Centre communautaire R, Patinoire Jim Tubman C, Centre John G Mlacak  |
| `BUILDING_ELEMENT_TYPE` | cat | 100% | 16 | Community Center 22%, Field House 21%, Arena 15%, Community Building 11%, Comfort Station 7%, Recreation Complex 6% |
| `BUILDING_ELEMENT_TYPE_FR` | cat | 100% | 15 | Centre communautaire 33%, Pavillon 21%, Aréna 15%, Bloc sanitaire 7%, Complexe récréatif 6%, Piscine intérieure 5% |
| `FACILITY_GROUP_NAME` | cat | 100% | 2 | RECREATION 100%, SOCIAL SERVICES 0% |
| `FACILITY_GROUP_NAME_FR` | cat | 100% | 2 | INSTALLATIONS DE LOISIRS 100%, SERVICES SOCIAUX 0% |
| `SUBTYPE` | cat | 100% | 2 | Building 80%, Element 20% |
| `ADDRNUM` | num | 100% | 235 | 1.00 · p25 175 · p50 960 · p95 4,479 · max 8,930  █▃▃▂▂▂▁▁▁▁▁▁▁▁▁▁ |
| `FULLNAME` | text | 100% | 242 | e.g. Glen Park Dr, Goldridge Dr, Des Peres Blancs Ave |
| `LINK` | text | 65% | 97 | e.g. https://ottawa.ca/en/r, https://ottawa.ca/en/r, https://ottawa.ca/en/r |
| `LINK_FR` | text | 65% | 97 | e.g. https://ottawa.ca/fr/l, https://ottawa.ca/fr/l, https://ottawa.ca/fr/l |
| `geometry` | id/text | 100% | 369 | e.g. {"type": "Point", "coo, {"type": "Point", "coo, {"type": "Point", "coo |
| `longitude` | num | 100% | 369 | -76.26 · p25 -75.77 · p50 -75.69 · p95 -75.47 · max -75.34  ▁▁▁▁▁▂▃▃▅▇█▃▂▃▁▁ |
| `latitude` | num | 100% | 369 | 45.09 · p25 45.33 · p50 45.37 · p95 45.47 · max 45.52  ▁▁▂▁▁▁▃▃▅▇█▇▇▅▄▁ |

## Candidate questions

- Spatial clustering of open_city_facilities_for_recreation_activities; overlay wards + the decision timeline

_profiled 2026-09-09 · `python3 tools/profile.py open_city_facilities_for_recreation_activities`_
