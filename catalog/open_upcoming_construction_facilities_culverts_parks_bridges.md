# Upcoming construction facilities, culverts, parks, bridges

`open_upcoming_construction_facilities_culverts_parks_bridges` · shape **arcgis-hub** · source `open-ottawa` · **spatial**

- origin: <https://open.ottawa.ca/datasets/ottawa::upcoming-construction-facilities-culverts-parks-bridges>
- fetched 2026-09-09 · **629 rows** · 15 columns
- geojson · licence: https://ottawa.ca/en/city-hall/get-know-your-city/open-data#open-data-licence-ve

## Columns

| column | kind | non-null | distinct | summary |
| --- | --- | --- | --- | --- |
| `OBJECTID` | num | 100% | 629 | 81.00 · p25 34,573 · p50 35,090 · p95 35,455 · max 35,488  ▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁█ |
| `FEATURE_TYPE` | cat | 100% | 23 | OBLDG 55%, OPARKS 9%, WBO 8%, GNP 7%, MIM 4%, RWPS 4% |
| `FEATURE_TYPE_FR` | cat | 100% | 23 | OBLDG 55%, OPARKS 9%, WBO 8%, GNP 7%, MIM 4%, RWPS 4% |
| `STATUS` | cat | 100% | 4 | PLANNED 91%, INPROGRESS 8%, DEVELOPER 1%, APPROVED 0% |
| `STATUS_FR` | cat | 100% | 4 | PLANNED 91%, INPROGRESS 8%, DEVELOPER 1%, APPROVED 0% |
| `TARGETED_START` | cat | 100% | 4 | This Year 88%, 1-2 Years 7%, 2-3 Years 4%, 3-5 Years 0% |
| `TARGETED_START_FR` | cat | 100% | 4 | Cette année 88%, 1 à 2 ans 7%, 2 à 3 ans 4%, 3 à 5 ans 0% |
| `PROJECT_MANAGER` | text | 94% | 80 | e.g. Amor, Jonathan, Ogilvie, Chris, Smith, Fraser |
| `PROJECTWEBPAGE` | cat | 1% | 1 | WCC 100% |
| `PROJECTWEBPAGE_FR` | cat | 4% | 1 | AAC 100% |
| `TRAFFICIMPACTS` | text | 19% | 50 | e.g. None, None., N/A |
| `Coordination` | cat | 0% | 3 | This project is only rel 67%, This project will design 17%, This project will design 17% |
| `geometry` | id/text | 100% | 624 | e.g. {"type": "Point", "coo, {"type": "Point", "coo, {"type": "Point", "coo |
| `longitude` | num | 100% | 624 | -76.21 · p25 -75.77 · p50 -75.69 · p95 -75.49 · max -75.32  ▁▁▁▁▁▃▂▃▇█▅▃▂▁▁▁ |
| `latitude` | num | 100% | 624 | 45.09 · p25 45.33 · p50 45.38 · p95 45.47 · max 45.52  ▁▁▁▁▁▂▃▃▃▅▅▅█▅▂▁ |

## Candidate questions

- Spatial clustering of open_upcoming_construction_facilities_culverts_parks_bridges; overlay wards + the decision timeline

_profiled 2026-09-09 · `python3 tools/profile.py open_upcoming_construction_facilities_culverts_parks_bridges`_
