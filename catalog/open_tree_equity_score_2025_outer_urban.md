# Tree Equity Score 2025 - Outer Urban

`open_tree_equity_score_2025_outer_urban` · shape **arcgis-hub** · source `open-ottawa` · **spatial**

- origin: <https://open.ottawa.ca/datasets/ottawa::tree-equity-score-2025-outer-urban>
- fetched 2026-09-09 · **69 rows** · 23 columns
- geojson · licence: Open Data | City of Ottawa

## Columns

| column | kind | non-null | distinct | summary |
| --- | --- | --- | --- | --- |
| `FID` | num | 100% | 69 | 1.00 · p25 18.00 · p50 35.00 · p95 65.60 · max 69.00  █▆▆█▆▆▆█▆▆▆█▆▆▆█ |
| `CTUID` | num | 100% | 69 | 5,050,001 · p25 5,050,007 · p50 5,050,062 · p95 5,050,137 · max 5,050,141  █▂▃▁▁▁▁▁▁▁▁▁▁▄▄▅ |
| `CTNUM` | num | 100% | 69 | 1.04 · p25 7.02 · p50 62.02 · p95 137 · max 141  █▂▃▁▁▁▁▁▁▁▁▁▁▄▄▅ |
| `CANCVR_R` | num | 100% | 25 | 11.00 · p25 19.00 · p50 22.00 · p95 34.80 · max 49.00  ▁▂▅▅▄█▂▂▂▁▁▁▁▁▁▁ |
| `CANGOAL` | num | 100% | 1 | 40.00 · p25 40.00 · p50 40.00 · p95 40.00 · max 40.00   |
| `CANGAP` | num | 100% | 24 | 0.00 · p25 16.00 · p50 18.00 · p95 25.00 · max 29.00  ▂▁▂▁▂▁▂▂▆▆▄█▅▄▁▂ |
| `GAPSCORE` | num | 100% | 24 | 0.00 · p25 0.55 · p50 0.62 · p95 0.86 · max 1.00  ▂▁▂▁▂▁▂▂▆▆▄█▅▄▁▂ |
| `E` | num | 100% | 69 | 0.25 · p25 0.36 · p50 0.44 · p95 0.56 · max 0.62  ▃▁▄▃▄▃▆▂▆█▃▂▄▁▁▂ |
| `TES_R` | num | 100% | 36 | 38.00 · p25 65.00 · p50 73.00 · p95 94.20 · max 100  ▁▁▂▁▁▃█▇▂▅▇▂▂▃▃▂ |
| `NOTE_EN` | cat | 100% | 1 |   100% |
| `NOTE_FR` | cat | 100% | 1 |   100% |
| `CREATED_DA` | text | 0% | 0 | e.g.  |
| `LAST_EDITE` | cat | 100% | 1 | 2025-09-09T00:00:00Z 100% |
| `CTNAME_EN` | id/text | 100% | 69 | e.g. Riverside Park, Clementine, Billings Bridge |
| `CTNAME_FR` | id/text | 100% | 69 | e.g. Riverside Park, Clementine, Billings Bridge |
| `TRNSCT_EN` | cat | 100% | 1 | Outer Urban 100% |
| `TRNSCT_FR` | cat | 100% | 1 | Urbain extérieur 100% |
| `PA_EN` | cat | 100% | 2 | No 96%, Yes 4% |
| `PA_FR` | cat | 100% | 2 | Non 96%, Oui 4% |
| `GLOBALID` | id/text | 100% | 69 | e.g. {B4798570-E125-4BA8-B7, {05CE19CC-F168-4B05-8A, {B2CA3D3C-EF1E-4762-84 |
| `Shape__Area` | num | 100% | 69 | 63,924 · p25 1,267,675 · p50 1,933,087 · p95 3,696,172 · max 5,256,648  ▂▄▄███▄▇█▄▁▃▁▁▁▁ |
| `Shape__Length` | num | 100% | 69 | 1,042 · p25 7,023 · p50 9,481 · p95 18,980 · max 30,155  ▂▂▅▇█▅▅▄▂▂▂▁▁▁▁▁ |
| `geometry` | id/text | 100% | 69 | e.g. {"type": "MultiPolygon, {"type": "Polygon", "c, {"type": "MultiPolygon |

## Candidate questions

- (none templated)

_profiled 2026-09-09 · `python3 tools/profile.py open_tree_equity_score_2025_outer_urban`_
