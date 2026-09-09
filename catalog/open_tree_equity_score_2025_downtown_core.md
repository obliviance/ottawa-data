# Tree Equity Score 2025 - Downtown Core

`open_tree_equity_score_2025_downtown_core` · shape **arcgis-hub** · source `open-ottawa` · **spatial**

- origin: <https://open.ottawa.ca/datasets/ottawa::tree-equity-score-2025-downtown-core>
- fetched 2026-09-09 · **20 rows** · 23 columns
- geojson · licence: Open Data | City of Ottawa

## Columns

| column | kind | non-null | distinct | summary |
| --- | --- | --- | --- | --- |
| `FID` | num | 100% | 20 | 1.00 · p25 5.75 · p50 10.50 · p95 19.05 · max 20.00  █▄▄▄▄█▄▄▄▄█▄▄▄▄█ |
| `CTUID` | num | 100% | 20 | 5,050,014 · p25 5,050,038 · p50 5,050,044 · p95 5,050,055 · max 5,050,056  ▅▁▁▁▁▁▁▃▅█▅▁▅▅██ |
| `CTNUM` | num | 100% | 20 | 14.00 · p25 37.76 · p50 44.50 · p95 55.05 · max 56.00  ▅▁▁▁▁▁▁▃▅█▅▁▅▅██ |
| `CANCVR_R` | num | 100% | 12 | 5.00 · p25 12.00 · p50 17.00 · p95 21.25 · max 26.00  ▄▁▁▁▄▄▂▄▂▄▂█▄▁▁▂ |
| `CANGOAL` | num | 100% | 1 | 30.00 · p25 30.00 · p50 30.00 · p95 30.00 · max 30.00   |
| `CANGAP` | num | 100% | 12 | 4.00 · p25 10.00 · p50 13.00 · p95 24.05 · max 25.00  ▂▁▁▄█▂▄▂▄▂▄▄▁▁▁▄ |
| `GAPSCORE` | num | 100% | 12 | 0.16 · p25 0.40 · p50 0.52 · p95 0.96 · max 1.00  ▂▁▁▄█▂▄▂▄▂▄▄▁▁▁▄ |
| `E` | num | 100% | 20 | 0.21 · p25 0.34 · p50 0.37 · p95 0.50 · max 0.55  ▂▁▁▁▂▅█▁▃▂▃▃▂▂▁▂ |
| `TES_R` | num | 100% | 14 | 63.00 · p25 71.00 · p50 81.00 · p95 92.10 · max 94.00  ▅▅▃▁▃▃▅▁▃█▅▅▃▁▃▃ |
| `NOTE_EN` | cat | 100% | 3 |   90%, Tree planting action to  5%, Tree planting action to  5% |
| `NOTE_FR` | cat | 100% | 3 |   90%, Les mesures de plantatio 5%, Les mesures de plantatio 5% |
| `CREATED_DA` | text | 0% | 0 | e.g.  |
| `LAST_EDITE` | cat | 100% | 1 | 2025-09-09T00:00:00Z 100% |
| `CTNAME_EN` | cat | 100% | 20 | Lowertown-Rideau St 5%, Centretown-Lyon St-Macla 5%, Centretown-Elgin-Cooper 5%, Centretown-Bank St 5%, LeBreton Flats 5%, Sandy Hill-King Edward A 5% |
| `CTNAME_FR` | cat | 100% | 20 | Basse-Ville-rue Rideau 5%, Centre-ville-rue Lyon-ru 5%, Centre-ville-Elgin-Coope 5%, Centreville-rue Bank 5%, Plaines LeBreton 5%, Côte-de-Sable-avenue Kin 5% |
| `TRNSCT_EN` | cat | 100% | 1 | Downtown Core 100% |
| `TRNSCT_FR` | cat | 100% | 1 | Centre-ville 100% |
| `PA_EN` | cat | 100% | 2 | No 90%, Yes 10% |
| `PA_FR` | cat | 100% | 2 | Non 90%, Oui 10% |
| `GLOBALID` | cat | 100% | 20 | {F3FD0C42-168E-471C-9E7F 5%, {56F95B43-4401-4B2C-B597 5%, {980D3802-C116-4433-8B06 5%, {DF44C852-F958-46D7-9842 5%, {0C365D8C-099C-4DB2-ADFD 5%, {970D686F-4675-4683-9E9F 5% |
| `Shape__Area` | num | 100% | 20 | 51,353 · p25 474,968 · p50 729,284 · p95 1,133,921 · max 1,207,988  ▄▁▁▁▄▄▂▁▄█▄▂▄▁▂▂ |
| `Shape__Length` | num | 100% | 20 | 1,500 · p25 3,875 · p50 4,542 · p95 7,951 · max 8,142  ▄▁▁▁▂█▂▆▂▄▄▁▁▂▂▄ |
| `geometry` | cat | 100% | 20 | {"type": "Polygon", "coo 5%, {"type": "Polygon", "coo 5%, {"type": "Polygon", "coo 5%, {"type": "Polygon", "coo 5%, {"type": "MultiPolygon", 5%, {"type": "MultiPolygon", 5% |

## Candidate questions

- (none templated)

_profiled 2026-09-09 · `python3 tools/profile.py open_tree_equity_score_2025_downtown_core`_
