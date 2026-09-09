# Arts and Culture

`open_arts_and_culture` · shape **arcgis-hub** · source `open-ottawa`

- origin: <https://open.ottawa.ca/datasets/ottawa::arts-and-culture>
- fetched 2026-09-09 · **100 rows** · 20 columns
- csv · licence: https://ottawa.ca/en/city-hall/get-know-your-city/open-data#open-data-licence-ve

## Columns

| column | kind | non-null | distinct | summary |
| --- | --- | --- | --- | --- |
| `X` | num | 100% | 100 | -8,483,232 · p25 -8,432,270 · p50 -8,420,312 · p95 -8,392,332 · max -8,392,264  ▁▁▁▁▁▁▁▁▁▂▄▁▁▁▁█ |
| `Y` | num | 100% | 100 | 5,642,457 · p25 5,676,838 · p50 5,690,912 · p95 5,703,357 · max 5,703,408  ▁▁▁▁▁▁▁▁▂▂▂▁▃▁▁█ |
| `OBJECTID` | num | 100% | 100 | 12.00 · p25 215 · p50 324 · p95 633 · max 654  ▄▃▂▂▆▆▃█▄▅▃▂▃▃▂▇ |
| `BUSINESS_ENTITY_DESC` | text | 100% | 51 | e.g. Shenkman Arts Centre, Andy Shields Park/Gree, Billings Estate Museum |
| `BUSINESS_ENTITY_DESC_FR` | text | 100% | 51 | e.g. Centre des Arts Shenkm, Parc Andy-Shields et C, Musée du domaine Billi |
| `BUILDING_DESC` | id/text | 100% | 98 | e.g. Shenkman Arts Centre, Ottawa Public Library , Billings Estate Museum |
| `BUILDING_DESC_FR` | id/text | 100% | 97 | e.g. Centre des Arts Shenkm, Bibliothèque publique , Musée du domaine Billi |
| `BUILDING_TYPE` | cat | 100% | 8 | Museum 53%, Public Library 23%, Recreation Complex 6%, Community Centre 5%, Administration Building 5%, Performing Arts Facility 4% |
| `BUILDING_TYPE_FR` | cat | 100% | 8 | Musée 53%, Bibliothèque publique 23%, Complexe récréatif 6%, Centre communautaire 5%, Bâtiment administratif 5%, Installation scénique 4% |
| `BUILDING_ELEMENT_DESC` | cat | 21% | 21 | Shenkman Arts Centre 5%, Library: Ruth E. Dickins 5%, J.G. Mlacak Art Gallery 5%, Library: Beaverbrook 5%, Ron Maslin Playhouse 5%, Library: Constance Bay 5% |
| `BUILDING_ELEMENT_DESC_FR` | cat | 21% | 21 | Centre des Arts Shenkman 5%, Bibliothèque – Ruth E. D 5%, Centre John G Mlacak - G 5%, Bibliothèque – Beaverbro 5%, Théâtre Ron-Maslin 5%, Bibliothèque – Constance 5% |
| `BUILDING_ELEMENT_TYPE` | cat | 100% | 6 | Museum 53%, Public Library 34%, Performing Arts Facility 6%, Art Facility 3%, Cultural Facility 2%, Archives 2% |
| `BUILDING_ELEMENT_TYPE_FR` | cat | 100% | 6 | Musée 53%, Bibliothèque publique 34%, Installation scénique 6%, Installation artistique 3%, Installation culturelle 2%, Archives 2% |
| `FACILITY_GROUP_NAME` | cat | 100% | 3 | ARTS AND CULTURE 85%, RECREATION 10%, CIVIC ADMINISTRATION 5% |
| `FACILITY_GROUP_NAME_FR` | cat | 100% | 3 | ARTS ET CULTURE 85%, INSTALLATIONS DE LOISIRS 10%, ADMINISTRATION MUNICIPAL 5% |
| `SUBTYPE` | cat | 100% | 2 | Building 84%, Element 16% |
| `LINK` | text | 94% | 49 | e.g. https://shenkmanarts.c, https://biblioottawali, https://ottawa.ca/en/a |
| `LINK_FR` | text | 94% | 49 | e.g. https://shenkmanarts.c, https://biblioottawali, https://ottawa.ca/fr/a |
| `ADDRNUM` | num | 100% | 49 | 1.00 · p25 350 · p50 2,508 · p95 6,579 · max 8,682  ▆▁▁▃▁█▁▁▁▁▁▁▁▁▁▁ |
| `FULLNAME` | text | 100% | 48 | e.g. Centrum Blvd, Meadow Dr, Cabot St |

## Candidate questions

- (none templated)

_profiled 2026-09-09 · `python3 tools/profile.py open_arts_and_culture`_
