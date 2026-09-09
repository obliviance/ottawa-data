# Adult School Crossing Guard Locations 2019

`open_adult_school_crossing_guard_locations_2019` · shape **arcgis-hub** · source `open-ottawa` · **spatial**

- origin: <https://open.ottawa.ca/datasets/ottawa::adult-school-crossing-guard-locations-2019>
- fetched 2026-09-09 · **222 rows** · 11 columns
- geojson · licence: https://ottawa.ca/en/city-hall/get-know-your-city/open-data#open-data-licence-ve

## Columns

| column | kind | non-null | distinct | summary |
| --- | --- | --- | --- | --- |
| `Guard` | id/text | 100% | 222 | e.g. Shirley’s Brook / Marc, Portobello / Scala, Maitland / Glenmount / |
| `Brigadier_Placement` | id/text | 100% | 222 | e.g. Shirley’s Brook / Marc, Portobello / Scala, Maitland / Glenmount / |
| `Control_Type` | cat | 100% | 7 | All-way stop 54%, Midblock 23%, Traffic Signal 17%, Pedestrian Crossover 5%, Intersection Pedestrian  0%, Side street 0% |
| `Type_de_Contrôle_de_la_Circulation` | cat | 100% | 8 | Arrêt Toutes Directions 54%, Bloc Médian 23%, Feux de Circulations 14%, Passage pour Piétons 5%, Feux de Circulation 2%, Feux pour Piétons 0% |
| `Num__Guards___Brigadier_` | num | 100% | 3 | 1.00 · p25 1.00 · p50 1.00 · p95 2.00 · max 3.00  █▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁ |
| `X` | num | 100% | 221 | -76.03 · p25 -75.78 · p50 -75.71 · p95 -75.47 · max -75.46  ▁▁▄▄▃▂▁▄█▅▄▄▂▂▂▅ |
| `Y` | num | 100% | 221 | 45.23 · p25 45.29 · p50 45.37 · p95 45.47 · max 45.49  ▁▃▅▇▂▃▂▅▅▄█▁▂▄▅▄ |
| `FID` | num | 100% | 222 | 1.00 · p25 56.25 · p50 112 · p95 211 · max 222  █████▇████▇█████ |
| `geometry` | id/text | 100% | 221 | e.g. {"type": "Point", "coo, {"type": "Point", "coo, {"type": "Point", "coo |
| `longitude` | num | 100% | 221 | -76.03 · p25 -75.78 · p50 -75.71 · p95 -75.47 · max -75.46  ▁▁▄▄▃▂▁▄█▅▄▄▂▂▂▅ |
| `latitude` | num | 100% | 221 | 45.23 · p25 45.29 · p50 45.37 · p95 45.47 · max 45.49  ▁▃▅▇▂▃▂▅▅▄█▁▂▄▅▄ |

## Candidate questions

- Spatial clustering of open_adult_school_crossing_guard_locations_2019; overlay wards + the decision timeline

_profiled 2026-09-09 · `python3 tools/profile.py open_adult_school_crossing_guard_locations_2019`_
