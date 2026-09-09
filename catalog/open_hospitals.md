# Hospitals

`open_hospitals` · shape **arcgis-hub** · source `open-ottawa`

- origin: <https://open.ottawa.ca/datasets/ottawa::hospitals>
- fetched 2026-09-09 · **10 rows** · 15 columns
- csv · licence: https://ottawa.ca/en/city-hall/get-know-your-city/open-data#open-data-licence-ve

## Columns

| column | kind | non-null | distinct | summary |
| --- | --- | --- | --- | --- |
| `X` | num | 100% | 10 | -8,438,858 · p25 -8,428,906 · p50 -8,424,961 · p95 -8,420,515 · max -8,420,071  ▄▁▁▁▁▁▁▄▄▄▄▁▁▄██ |
| `Y` | num | 100% | 10 | 5,674,412 · p25 5,683,714 · p50 5,684,874 · p95 5,690,994 · max 5,691,992  ▃▁▁▁▁▁▁▃▅█▁▃▁▃▁▃ |
| `OBJECTID` | num | 100% | 10 | 1.00 · p25 3.25 · p50 5.50 · p95 9.55 · max 10.00  ██▁█▁█▁██▁█▁█▁██ |
| `ID` | num | 100% | 10 | 1.00 · p25 3.25 · p50 5.50 · p95 9.55 · max 10.00  ██▁█▁█▁██▁█▁█▁██ |
| `NAME` | cat | 100% | 10 | Royal Ottawa Hospital 10%, Ottawa Hospital - Civic  10%, Ottawa Hospital - Rivers 10%, Children's Hospital of E 10%, Ottawa Hospital - Genera 10%, Montfort Hospital 10% |
| `ADDRESS` | cat | 100% | 10 | 1145 Carling Avenue 10%, 1053 Carling Avenue 10%, 1967 Riverside Drive 10%, 401 Smyth Road 10%, 501 Smyth Road 10%, 713 Montreal Road 10% |
| `PHONE` | cat | 100% | 10 | 722-6521 10%, 761-4000 10%, 738-7100 10%, 737-7600 10%, 737-7777 10%, 746-4621 10% |
| `LINK_LABEL_EN` | text | 0% | 0 | e.g.  |
| `LINK_EN` | cat | 100% | 7 | https://www.ottawahospit 40%, http://www.theroyal.ca/ 10%, http://www.cheo.on.ca/ 10%, http://www.hopitalmontfo 10%, http://www.qch.on.ca/ 10%, https://www.bruyere.org/ 10% |
| `LINK_DESCRIPTION_EN` | text | 0% | 0 | e.g.  |
| `LINK_LABEL_FR` | text | 0% | 0 | e.g.  |
| `LINK_FR` | cat | 100% | 7 | https://www.ottawahospit 40%, http://www.leroyal.ca/ 10%, http://www.cheo.on.ca/fr 10%, http://www.hopitalmontfo 10%, http://www.qch.on.ca/ 10%, https://www.bruyere.org/ 10% |
| `GLOBALID` | cat | 100% | 10 | {E279DD71-C8D3-4C76-B317 10%, {C1661EEA-B6C5-4C11-9789 10%, {7A30AEC4-D042-41D6-9CF1 10%, {93E3EACA-FB11-49E9-A914 10%, {CC861544-A63C-4A64-89DA 10%, {D394D8AA-B8B6-4C7E-B4A8 10% |
| `ADDRESS_FR` | cat | 100% | 10 | 1145, avenue Carling 10%, 1053, avenue Carling 10%, 1967, promenade Riversid 10%, 401, chemin Smyth 10%, 501, chemin Smyth 10%, 713, chemin Montréal 10% |
| `NAME_FR` | cat | 100% | 10 | Hôpital Royal Ottawa 10%, Hôpital d’Ottawa – Campu 10%, Hôpital d’Ottawa, campus 10%, Centre hospitalier pour  10%, Hôpital d’Ottawa – Campu 10%, Hôpital Montfort 10% |

## Candidate questions

- (none templated)

_profiled 2026-09-09 · `python3 tools/profile.py open_hospitals`_
