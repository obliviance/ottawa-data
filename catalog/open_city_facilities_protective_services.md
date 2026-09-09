# City Facilities - Protective Services

`open_city_facilities_protective_services` · shape **arcgis-hub** · source `open-ottawa` · **spatial**

- origin: <https://open.ottawa.ca/datasets/ottawa::city-facilities-protective-services>
- fetched 2026-09-09 · **81 rows** · 21 columns
- geojson · licence: https://ottawa.ca/en/city-hall/get-know-your-city/open-data#open-data-licence-ve

## Columns

| column | kind | non-null | distinct | summary |
| --- | --- | --- | --- | --- |
| `OBJECTID` | num | 100% | 81 | 60.00 · p25 420 · p50 539 · p95 718 · max 759  ▃▁▁▁▁▁▁█▆▃▆█▅▄▅▅ |
| `BUSINESS_ENTITY_DESC` | id/text | 100% | 71 | e.g. Leitrim Prk Cmplx/Poli, 26 Concourse Gate, Police East Headquarte |
| `BUSINESS_ENTITY_DESC_FR` | id/text | 98% | 70 | e.g. Complexe du parc Leitr, 26, porte Concourse, Police – Bureaux de la |
| `BUILDING_DESC` | id/text | 100% | 71 | e.g. Police: East Division , Spay Neuter Clinic, Police East Division H |
| `BUILDING_DESC_FR` | id/text | 98% | 70 | e.g. Police – Quartier géné, Clinique de stérilisat, Quartier général de la |
| `BUILDING_TYPE` | cat | 100% | 7 | Fire Station 67%, Ambulance Facility 15%, Police Station 10%, Community Centre 4%, Administration Building 2%, Veterinary Facility 1% |
| `BUILDING_TYPE_FR` | cat | 100% | 7 | Caserne de pompiers 67%, Poste d'ambulances 15%, Commissariat de police 10%, Centre communautaire 4%, Bâtiment administratif 2%, Clinique vétérinaire 1% |
| `BUILDING_ELEMENT_DESC` | cat | 30% | 24 | Fire Station 72 - Cumber 8%, Stittsville Paramedic Po 4%, Fire Station 64 - Carp 4%, Fire Station 71 - Navan 4%, Fire Station 81 - Stitts 4%, Fire Station 82 - Richmo 4% |
| `BUILDING_ELEMENT_DESC_FR` | cat | 29% | 23 | Caserne de pompiers 72 – 8%, Poste du Service  paramé 4%, Caserne de pompiers 64 – 4%, Caserne de pompiers 71 – 4%, Caserne de pompiers 81 - 4%, Caserne de pompiers 82 - 4% |
| `BUILDING_ELEMENT_TYPE` | cat | 100% | 6 | Fire Station 57%, Ambulance Facility 14%, Ambulance Depot 11%, Police Station 10%, Community Police Center 7%, Veterinary Facility 1% |
| `BUILDING_ELEMENT_TYPE_FR` | cat | 100% | 7 | Caserne de pompiers 57%, Poste d'ambulances 14%, Commissariat de police 10%, Garage pour ambulances 10%, Centre de services polic 7%, Clinique vétérinaire 1% |
| `FACILITY_GROUP_NAME` | cat | 100% | 3 | PROTECTIVE SERVICES 95%, RECREATION 2%, CIVIC ADMINISTRATION 2% |
| `FACILITY_GROUP_NAME_FR` | cat | 100% | 3 | SERVICES DE PROTECTION 95%, INSTALLATIONS DE LOISIRS 2%, ADMINISTRATION MUNICIPAL 2% |
| `SUBTYPE` | cat | 100% | 2 | Building 81%, Element 19% |
| `ADDRNUM` | num | 100% | 69 | 20.00 · p25 380 · p50 1,397 · p95 6,280 · max 8,011  █▃▃▂▂▁▃▁▁▁▁▂▂▁▁▁ |
| `FULLNAME` | id/text | 100% | 66 | e.g. Bank St, Concourse Gate, St. Joseph Blvd |
| `LINK` | cat | 80% | 4 | https://ottawa.ca/en/hea 82%, https://www.ottawapolice 11%, https://www.ottawapolice 6%, https://ottawa.ca/en/liv 2% |
| `LINK_FR` | cat | 80% | 4 | https://ottawa.ca/fr/san 82%, ottawapolice.ca/fr/conta 11%, https://www.ottawapolice 6%, https://ottawa.ca/fr/viv 2% |
| `geometry` | id/text | 100% | 81 | e.g. {"type": "Point", "coo, {"type": "Point", "coo, {"type": "Point", "coo |
| `longitude` | num | 100% | 81 | -76.22 · p25 -75.82 · p50 -75.69 · p95 -75.42 · max -75.35  ▁▁▁▁▁▃▂▂▃█▅▃▂▂▂▁ |
| `latitude` | num | 100% | 81 | 45.13 · p25 45.28 · p50 45.37 · p95 45.48 · max 45.52  ▂▁▂▂▂▅▄▂▇▃▅▆█▂▃▃ |

## Candidate questions

- (none templated)

_profiled 2026-09-09 · `python3 tools/profile.py open_city_facilities_protective_services`_
