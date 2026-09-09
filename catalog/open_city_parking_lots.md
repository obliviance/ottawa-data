# City Parking Lots

`open_city_parking_lots` · shape **arcgis-hub** · source `open-ottawa` · **spatial**

- origin: <https://open.ottawa.ca/datasets/ottawa::city-parking-lots>
- fetched 2026-09-09 · **15 rows** · 17 columns
- geojson · licence: https://ottawa.ca/en/city-hall/get-know-your-city/open-data#open-data-licence-ve

## Columns

| column | kind | non-null | distinct | summary |
| --- | --- | --- | --- | --- |
| `OBJECTID` | num | 100% | 15 | 1.00 · p25 4.50 · p50 8.00 · p95 15.30 · max 16.00  ████████▁███████ |
| `LOT` | num | 100% | 15 | 3.00 · p25 7.00 · p50 11.00 · p95 25.10 · max 30.00  ██▄▄█▄▄▁▄▁▄█▁▁▁▄ |
| `ADDRESS` | cat | 100% | 15 | 210 Gloucester St. 7%, 70 Clarence St. 7%, 141 Clarence St. 7%, 110 Laurier Ave. 7%, 170 Second Ave. 7%, 234-250 Slater St. 7% |
| `SPACES` | num | 100% | 15 | 10.00 · p25 35.50 · p50 78.00 · p95 575 · max 845  █▂▂▃▁▃▁▁▂▁▁▁▁▁▁▂ |
| `TYPE` | cat | 100% | 2 | Surface 60%, Enclosed 40% |
| `HEIGHTRESTRICTION` | cat | 100% | 5 | NA 60%, 2.0 m max 13%, 2.2 m max 13%, 2.16 m max 7%, 2.4 m max 7% |
| `ADDRESS_FR` | cat | 100% | 15 | 210 rue Gloucester 7%, 70 rue Clarence 7%, 141 rue Clarence 7%, 110 avenue Laurier Ouest 7%, 170 avenue Second 7%, 234-250 rue Slater 7% |
| `PERMIT` | cat | 100% | 6 | Monthly parking 27%, Monthly parking - None a 27%, Monthly parking – not pr 20%, Seasonal Parking – May t 13%, Monthly parking  7%, Monthly parking – winter 7% |
| `PERMIT_FR` | cat | 100% | 7 | Stationnement mensuel -  27%, Stationnement mensuel  20%, Stationnement mensuel -  20%, Stationnement saisonnier 13%, Stationnement mensuel 
 7%, Stationnement mensuel 7% |
| `TYPE_FR` | cat | 100% | 2 | Parc de stationnement en 60%, Parc de stationnement co 40% |
| `GIS_UNIQUE_ID` | text | 0% | 0 | e.g.  |
| `GLOBALID` | cat | 100% | 15 | {829E7D0D-3F95-40F6-B9CF 7%, {EC467977-CACF-448B-9535 7%, {77A9E562-8F58-4280-9F52 7%, {B2878C66-8BFA-4822-82D7 7%, {C0AD1B81-D097-4A48-8B55 7%, {8C9F57AC-3375-40A8-ADE6 7% |
| `CREATED_DATE` | text | 0% | 0 | e.g.  |
| `LAST_EDITED_DATE` | date | 80% | 12 | 2018-02-14 → 2024-06-20, 4 gaps >30d |
| `geometry` | cat | 100% | 15 | {"type": "Point", "coord 7%, {"type": "Point", "coord 7%, {"type": "Point", "coord 7%, {"type": "Point", "coord 7%, {"type": "Point", "coord 7%, {"type": "Point", "coord 7% |
| `longitude` | num | 100% | 15 | -75.73 · p25 -75.70 · p50 -75.69 · p95 -75.61 · max -75.49  ▂▅█▁▃▁▁▁▁▁▁▁▁▁▁▂ |
| `latitude` | num | 100% | 15 | 45.37 · p25 45.41 · p50 45.42 · p95 45.46 · max 45.50  ▂▁▁▂▆█▂█▁▁▁▁▁▁▁▂ |

## Candidate questions

- (none templated)

_profiled 2026-09-09 · `python3 tools/profile.py open_city_parking_lots`_
