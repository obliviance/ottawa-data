# City of Ottawa — development applications (keyless MapServer)

`city_devapps_mapserver` · shape **arcgis-hub** · source `devapps` · **spatial**

- origin: <https://maps.ottawa.ca/arcgis/rest/services/Development_Applications/MapServer/0>
- fetched 2026-10-24 · **3,445 rows** · 16 columns
- paged by OBJECTID via arcgis_layers.py; 3,445 rows

## Columns

| column | kind | non-null | distinct | summary |
| --- | --- | --- | --- | --- |
| `OBJECTID` | num | 100% | 3,445 | 1.00 · p25 862 · p50 1,723 · p95 3,273 · max 3,445  █▇▇█▇▇▇█▇▇▇█▇▇▇█ |
| `LATITUDE` | num | 100% | 1,676 | 44.98 · p25 45.30 · p50 45.40 · p95 45.45 · max 45.52  ▁▁▁▁▁▁▂▁▄▂▂▃▇█▂▁ |
| `LONGITUDE` | num | 100% | 1,682 | -76.30 · p25 -75.77 · p50 -75.70 · p95 -75.49 · max -75.34  ▁▁▁▁▁▂▃▁▂▆█▃▂▂▁▁ |
| `DT_APP_ID` | text | 100% | 1,570 | e.g. __CK1E5I, __BGBJAI, __C3YEXB |
| `APPLICATION_NUMBER` | text | 99% | 1,569 | e.g. D07-12-22-0071        , D07-16-21-0027        , D07-16-26-0014         |
| `APPLICATION_DATE` | date | 99% | 1,566 | 1970-01-01 → 1970-01-01 |
| `APPLICATION_TYPE_EN` | cat | 99% | 7 | Site Plan Control        39%, Zoning By-law Amendment  38%, Official Plan Amendment  10%, Plan of Subdivision      8%, Ontario Heritage Act     3%, Plan of Condominium      1% |
| `APPLICATION_TYPE_FR` | cat | 99% | 7 | Réglementation du plan d 39%, Modification au Règlemen 38%, Modification au Plan off 10%, Plan de lotissement 8%, Loi sur le patrimoine de 3%, Plans de condominium 1% |
| `OBJECT_CURRENT_STATUS_EN` | text | 99% | 69 | e.g. Agreement Registered -, Comment Period has End, Application File Pendi |
| `OBJECT_CURRENT_STATUS_FR` | text | 99% | 70 | e.g. Entente Enregistrée - , Période de Commentaire, Dossier en cours d'exa |
| `OBJECT_CURRENT_STATUS_DATE` | date | 99% | 1,564 | 1970-01-01 → 1970-01-01 |
| `ADDRESS_NUMBER_ROAD_NAME` | text | 100% | 1,709 | e.g. 315 MIWATE, 3053 NAVAN, 900 GEOGRAPHE, TSSE DU |
| `WARD_NUMBER_EN` | cat | 99% | 24 | Ward 14                  10%, Ward 15                  9%, Ward 12                  8%, Ward 21                  8%, Ward 17                  7%, Ward 19                  7% |
| `WARD_NUMBER_FR` | cat | 99% | 24 | Quartier 14 10%, Quartier 15 9%, Quartier 12 8%, Quartier 21 8%, Quartier 17 7%, Quartier 19 7% |
| `longitude` | num | 100% | 1,682 | -76.30 · p25 -75.77 · p50 -75.70 · p95 -75.49 · max -75.34  ▁▁▁▁▁▂▃▁▂▆█▃▂▂▁▁ |
| `latitude` | num | 100% | 1,676 | 44.98 · p25 45.30 · p50 45.40 · p95 45.45 · max 45.52  ▁▁▁▁▁▁▂▁▄▂▂▃▇█▂▁ |

## Candidate questions

- Trend / seasonality of city_devapps_mapserver over `APPLICATION_DATE`; structural breaks?
- Spatial clustering of city_devapps_mapserver; overlay wards + the decision timeline

_profiled 2026-10-24 · `python3 tools/profile.py city_devapps_mapserver`_
