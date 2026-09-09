# Skateboard Parks

`open_skateboard_parks` · shape **arcgis-hub** · source `open-ottawa` · **spatial**

- origin: <https://open.ottawa.ca/datasets/ottawa::skateboard-parks>
- fetched 2026-09-09 · **32 rows** · 28 columns
- geojson · licence: https://ottawa.ca/en/city-hall/get-know-your-city/open-data#open-data-licence-ve

## Columns

| column | kind | non-null | distinct | summary |
| --- | --- | --- | --- | --- |
| `OBJECTID` | num | 100% | 32 | 1.00 · p25 8.75 · p50 16.50 · p95 30.45 · max 32.00  ████████████████ |
| `PARK_ID` | num | 100% | 30 | 9.00 · p25 684 · p50 974 · p95 2,569 · max 2,633  ▅▂▃▃▆█▃▃▂▁▃▁▂▂▃▆ |
| `FACILITYID` | num | 100% | 32 | 28,000 · p25 28,009 · p50 28,020 · p95 59,124 · max 59,126  █▁▁▃▁▁▁▁▁▁▁▁▂▁▁▂ |
| `NAME` | id/text | 100% | 27 | e.g. Osgoode Community Cent, Roving Skateboard Park, Lansdowne Skateboard P |
| `NAME_FR` | id/text | 100% | 27 | e.g. Planchodrome du Centre, Lieu de planchodrome i, Planchodrome Lansdowne |
| `ADDRESS` | id/text | 100% | 30 | e.g. 5660 Osgoode Main Stre, 100 Clifford Campbell , 450 Queen Elizabeth Dr |
| `ADDRESS_FR` | id/text | 100% | 30 | e.g. 5660, ru Osgoode Main, 100, rue Clifford-Camp, 450, promenade Queen E |
| `FACILITY_TYPE` | cat | 90% | 3 | flat 66%, other 21%, bowl 14% |
| `FACILITY_TYPE_FR` | cat | 90% | 3 | plat 66%, autre 21%, bol 14% |
| `ACCESSCTRL` | cat | 90% | 2 | no/non 93%, yes/oui 7% |
| `ACCESSIBLE` | cat | 90% | 2 | no/non 72%, yes/oui 28% |
| `OPEN` | text | 0% | 0 | e.g.  |
| `MODIFIED_DATE` | date | 90% | 21 | 2017-07-11 → 2025-07-21, 10 gaps >30d |
| `CREATED_DATE` | date | 46% | 15 | 2015-05-20 → 2025-07-17, 10 gaps >30d |
| `FACILITY` | cat | 87% | 12 | Neighbourhood : smaller  46%, Community: mid size faci 11%, District: larger facilit 11%, Fitzroy Harbour Communit 4%, A series of skateboard r 4%, Eccolands Park - Roving  4% |
| `FACILITY_FR` | cat | 87% | 11 | De voisinage : petite in 46%, Communautaire : installa 14%, De district : grande ins 11%, Centre communautaire de  4%, Une série de rampes adap 4%, Parc Eccolands - Lieu de 4% |
| `DESCRIPTION` | cat | 90% | 13 | Flat surface, 5 componen 38%, Flat asphalt surface, 5  24%, Flat asphalt surface 3%, Flat concrete surface, 5 3%, Flat concrete surface, 1 3%, Flat asphalt surface, 8  3% |
| `DESCRIPTION_FR` | cat | 90% | 13 | Surface plane, 5 modules 38%, Surface d'asphalte plane 24%, Survace d'asphalte plane 3%, Surface de béton plane,  3%, Surface de béton plane,  3%, Surface d'asphalte plane 3% |
| `PICTURE_LINK` | text | 0% | 0 | e.g.  |
| `PICTURE_DESCRIPTION` | text | 0% | 0 | e.g.  |
| `PICTURE_DESCRIPTION_FR` | text | 0% | 0 | e.g.  |
| `PARKNAME` | id/text | 96% | 29 | e.g. Osgoode Community Cent, Fitzroy Harbour Commun, Lansdowne Park |
| `PARKNAME_FR` | id/text | 96% | 29 | e.g. Centre communautaire d, Centre communautaire d, Parc Lansdowne |
| `PARKADDRESS` | id/text | 96% | 29 | e.g. 5660 Osgoode Main Stre, 100 Clifford Campbell , 450 Queen Elizabeth Dr |
| `PARKADDRESS_FR` | id/text | 96% | 29 | e.g. 5660, rue Osgoode Main, 100, rue Clifford-Camp, 450, promenade Queen E |
| `geometry` | id/text | 100% | 32 | e.g. {"type": "Point", "coo, {"type": "Point", "coo, {"type": "Point", "coo |
| `longitude` | num | 100% | 32 | -76.21 · p25 -75.78 · p50 -75.68 · p95 -75.41 · max -75.34  ▂▁▂▁▁█▂▁▆█▆█▃▃▁▃ |
| `latitude` | num | 100% | 32 | 45.14 · p25 45.27 · p50 45.34 · p95 45.47 · max 45.50  ▃▁▁▃▁█▄▃▂▂▅▃▃▅▃▂ |

## Candidate questions

- (none templated)

_profiled 2026-09-09 · `python3 tools/profile.py open_skateboard_parks`_
