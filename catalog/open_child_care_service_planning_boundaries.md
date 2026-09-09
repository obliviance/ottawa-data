# Child Care Service Planning Boundaries

`open_child_care_service_planning_boundaries` · shape **arcgis-hub** · source `open-ottawa` · **spatial**

- origin: <https://open.ottawa.ca/datasets/ottawa::child-care-service-planning-boundaries>
- fetched 2026-09-09 · **51 rows** · 17 columns
- geojson · licence: https://ottawa.ca/en/city-hall/get-know-your-city/open-data#open-data-licence-ve

## Columns

| column | kind | non-null | distinct | summary |
| --- | --- | --- | --- | --- |
| `FID` | num | 100% | 51 | 1.00 · p25 13.50 · p50 26.00 · p95 48.50 · max 51.00  █▆▆▆▆▆▆█▆▆▆▆▆▆▆█ |
| `Name` | id/text | 100% | 51 | e.g. Alta Vista, Beaconhill, Beaverbrook/Marchwood |
| `ID` | num | 100% | 51 | 1.00 · p25 13.50 · p50 26.00 · p95 48.50 · max 51.00  █▆▆▆▆▆▆█▆▆▆▆▆▆▆█ |
| `Nom_FR` | id/text | 100% | 51 | e.g. Alta Vista, Beaconhill, Beaverbrook/Marchwood |
| `NumVul1m4_` | num | 100% | 29 | 0.00 · p25 0.00 · p50 21.00 · p95 92.00 · max 111  █▁▂▂▁▂▂▂▁▁▁▁▁▁▁▁ |
| `PercVul1m4` | num | 100% | 32 | 0.00 · p25 0.00 · p50 0.21 · p95 0.44 · max 0.46  █▁▁▁▁▁▂▂▂▂▂▂▁▂▁▂ |
| `Pop0to6_C2` | num | 100% | 48 | 440 · p25 718 · p50 1,115 · p95 2,632 · max 3,075  ▂█▃▂▅▁▂▂▃▁▃▂▂▂▁▁ |
| `PercPop0to` | num | 100% | 30 | 0.00 · p25 0.00 · p50 0.01 · p95 0.03 · max 0.04  █▁▁▂▂▂▂▁▁▁▂▁▂▁▁▁ |
| `NumOtherON` | num | 100% | 24 | 0.00 · p25 0.00 · p50 30.00 · p95 418 · max 555  █▂▁▁▁▁▂▁▁▁▁▁▁▁▁▁ |
| `PercOtherO` | num | 100% | 28 | 0.00 · p25 0.00 · p50 0.04 · p95 0.27 · max 0.39  █▁▁▂▁▂▁▁▁▁▁▁▁▁▁▁ |
| `PercOthe_1` | num | 100% | 24 | 0.00 · p25 0.00 · p50 0.00 · p95 0.05 · max 0.07  █▂▁▁▁▁▂▁▁▁▁▁▁▁▁▁ |
| `NumFRHome0` | num | 100% | 22 | 0.00 · p25 0.00 · p50 40.00 · p95 285 · max 695  █▂▂▁▁▁▁▁▁▁▁▁▁▁▁▁ |
| `PercFRHome` | num | 100% | 22 | 0.00 · p25 0.00 · p50 0.01 · p95 0.04 · max 0.09  █▂▂▁▁▁▁▁▁▁▁▁▁▁▁▁ |
| `SRIindex_2` | num | 100% | 10 | 0.00 · p25 0.00 · p50 1.00 · p95 10.00 · max 10.00  █▁▁▁▁▁▁▁▁▁▁▁▁▁▁▃ |
| `Shape__Area` | num | 100% | 51 | 4,207,625 · p25 10,159,822 · p50 24,500,905 · p95 686,921,675 · max 1,079,497,003  █▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁ |
| `Shape__Length` | num | 100% | 51 | 8,685 · p25 14,511 · p50 24,269 · p95 117,228 · max 145,735  █▄▄▂▁▁▁▁▁▁▁▁▁▁▁▁ |
| `geometry` | id/text | 100% | 51 | e.g. {"type": "Polygon", "c, {"type": "Polygon", "c, {"type": "Polygon", "c |

## Candidate questions

- (none templated)

_profiled 2026-09-09 · `python3 tools/profile.py open_child_care_service_planning_boundaries`_
