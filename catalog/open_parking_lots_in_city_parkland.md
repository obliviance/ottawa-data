# Parking Lots in City Parkland

`open_parking_lots_in_city_parkland` · shape **arcgis-hub** · source `open-ottawa` · **spatial**

- origin: <https://open.ottawa.ca/datasets/ottawa::parking-lots-in-city-parkland>
- fetched 2026-09-09 · **410 rows** · 23 columns
- geojson · licence: https://ottawa.ca/en/city-hall/get-know-your-city/open-data#open-data-licence-ve

## Columns

| column | kind | non-null | distinct | summary |
| --- | --- | --- | --- | --- |
| `OBJECTID` | num | 100% | 410 | 1.00 · p25 103 · p50 206 · p95 390 · max 410  ██▇█▇█▇██▇█▇█▇██ |
| `PARK_ID` | num | 100% | 308 | 5.00 · p25 387 · p50 854 · p95 2,435 · max 2,633  ▆█▆▅▆▆▆▅▂▅▄▁▂▁▃▂ |
| `FACILITYID` | num | 100% | 410 | 114 · p25 25,066 · p50 25,174 · p95 55,012 · max 58,871  ▁▂▁▁▁▁█▁▁▂▁▁▁▁▁▁ |
| `ADDRESS` | text | 100% | 316 | e.g. 5650 Scobie Crescent, , 201 Donald Street, Ott, 3500 Cambrian Road |
| `ADDRESS_FR` | text | 100% | 318 | e.g. 5650, croissant Scobie, 201, rue Donald, Ottaw, 3500, chemin Cambrian |
| `SURFACE` | cat | 100% | 3 | asphalt 71%, gravel 28%, paved 1% |
| `CAPACITY` | num | 100% | 113 | 0.00 · p25 17.00 · p50 30.00 · p95 189 · max 1,300  █▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁ |
| `ACCESSIBLE_PARKING_CAPACITY` | num | 100% | 17 | 0.00 · p25 0.00 · p50 1.00 · p95 6.00 · max 25.00  █▃▁▁▁▁▁▁▁▁▁▁▁▁▁▁ |
| `PAID_PARKING` | cat | 99% | 3 | no/non 93%,   4%, yes/oui 3% |
| `PAID_PARKING_TYPE` | cat | 100% | 6 | none 90%,   6%, meters 2%, permit 0%, attendants 0%, None 0% |
| `LIGHTING` | cat | 98% | 3 | no/non 54%, yes/oui 43%,   3% |
| `FENCED` | cat | 99% | 3 | no/non 83%, yes/oui 14%,   3% |
| `ACCESSIBLE` | cat | 56% | 2 | yes/oui 90%, no/non 10% |
| `OPEN` | text | 0% | 0 | e.g.  |
| `MODIFIED_DATE` | date | 100% | 240 | 2016-02-09 → 2022-09-07, 16 gaps >30d |
| `CREATED_DATE` | date | 19% | 78 | 2014-10-28 → 2022-09-07, 20 gaps >30d |
| `PARKNAME` | text | 100% | 308 | e.g. Harold Barnhart Park, Gil-O-Julien Park, Minto Recreation Compl |
| `PARKNAME_FR` | text | 100% | 308 | e.g. Parc Harold-Barnhart, Parc Gil-O-Julien, Complexe récréatif Min |
| `PARKADDRESS` | text | 100% | 307 | e.g. 5650 Scobie Crescent, , 201 Donald Street, Ott, 3500 Cambrian Road, Ne |
| `PARKADDRESS_FR` | text | 100% | 307 | e.g. 5650, croissant Scobie, 201, rue Donald, Ottaw, 3500, chemin Cambrian, |
| `geometry` | id/text | 99% | 409 | e.g. {"type": "Point", "coo, {"type": "Point", "coo, {"type": "Point", "coo |
| `longitude` | num | 99% | 409 | -76.26 · p25 -75.82 · p50 -75.71 · p95 -75.46 · max -75.34  ▁▁▁▁▁▄▃▄▄█▆▄▃▄▂▁ |
| `latitude` | num | 99% | 409 | 45.07 · p25 45.28 · p50 45.35 · p95 45.48 · max 45.52  ▁▁▁▁▁▁▅▅▃▅█▅▄▅▄▂ |

## Candidate questions

- Spatial clustering of open_parking_lots_in_city_parkland; overlay wards + the decision timeline

_profiled 2026-09-09 · `python3 tools/profile.py open_parking_lots_in_city_parkland`_
