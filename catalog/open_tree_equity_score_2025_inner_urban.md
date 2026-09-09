# Tree Equity Score 2025 - Inner Urban

`open_tree_equity_score_2025_inner_urban` · shape **arcgis-hub** · source `open-ottawa` · **spatial**

- origin: <https://open.ottawa.ca/datasets/ottawa::tree-equity-score-2025-inner-urban>
- fetched 2026-09-09 · **47 rows** · 23 columns
- geojson · licence: Open Data | City of Ottawa

## Columns

| column | kind | non-null | distinct | summary |
| --- | --- | --- | --- | --- |
| `FID` | num | 100% | 47 | 1.00 · p25 12.50 · p50 24.00 · p95 44.70 · max 47.00  ████████▅███████ |
| `CTUID` | num | 100% | 47 | 5,050,004 · p25 5,050,021 · p50 5,050,033 · p95 5,050,118 · max 5,050,138  ▄▆▅█▄▁▅▁▁▁▁▄▁▁▂▁ |
| `CTNUM` | num | 100% | 47 | 4.00 · p25 20.51 · p50 33.02 · p95 118 · max 138  ▄▆▅█▄▁▅▁▁▁▁▄▁▁▂▁ |
| `CANCVR_R` | num | 100% | 23 | 7.00 · p25 19.00 · p50 22.00 · p95 32.40 · max 47.00  ▁▁▁▅▃█▄▆▃▂▂▁▁▁▁▁ |
| `CANGOAL` | num | 100% | 1 | 40.00 · p25 40.00 · p50 40.00 · p95 40.00 · max 40.00   |
| `CANGAP` | num | 100% | 23 | 0.00 · p25 14.00 · p50 18.00 · p95 26.40 · max 33.00  ▁▁▁▁▂▄▅▅▆█▄▆▁▁▁▁ |
| `GAPSCORE` | num | 100% | 23 | 0.00 · p25 0.42 · p50 0.55 · p95 0.80 · max 1.00  ▁▁▁▁▂▄▅▅▆█▄▆▁▁▁▁ |
| `E` | num | 100% | 47 | 0.24 · p25 0.35 · p50 0.41 · p95 0.56 · max 0.62  ▂▂▅▅▄▆█▃██▃▃▃▂▂▂ |
| `TES_R` | num | 100% | 24 | 59.00 · p25 70.00 · p50 77.00 · p95 91.70 · max 100  ▂▁▁█▄▃▅▅▄▂▇▁▄▁▁▁ |
| `NOTE_EN` | cat | 100% | 2 |   98%, Majority of this neighbo 2% |
| `NOTE_FR` | cat | 100% | 2 |   98%, La majeure partie du sec 2% |
| `CREATED_DA` | text | 0% | 0 | e.g.  |
| `LAST_EDITE` | cat | 100% | 1 | 2025-09-09T00:00:00Z 100% |
| `CTNAME_EN` | id/text | 100% | 47 | e.g. Laurentian View-Highla, Westboro-Dovercourt, Westboro-Hampton Park |
| `CTNAME_FR` | id/text | 100% | 47 | e.g. Laurentian View-Highla, Westboro-Dovercourt, Westboro-Hampton Park |
| `TRNSCT_EN` | cat | 100% | 1 | Inner Urban 100% |
| `TRNSCT_FR` | cat | 100% | 1 | Urbain intérieur 100% |
| `PA_EN` | cat | 100% | 3 | No 87%, Yes 9%,   4% |
| `PA_FR` | cat | 100% | 3 | Non 87%, Oui 9%,   4% |
| `GLOBALID` | id/text | 100% | 47 | e.g. {7721E693-ADB7-469E-B7, {88AE2D5E-3302-4ECA-8D, {671A5A2E-EAEF-4151-BA |
| `Shape__Area` | num | 100% | 47 | 32,695 · p25 731,927 · p50 1,260,379 · p95 2,886,836 · max 3,782,809  ▄▄▄▄▆█▅▃▁▄▁▁▁▁▁▁ |
| `Shape__Length` | num | 100% | 47 | 1,072 · p25 5,372 · p50 7,531 · p95 12,470 · max 14,968  ▃▃▃▅▃▄▇█▄▃▇▃▄▂▁▃ |
| `geometry` | id/text | 100% | 47 | e.g. {"type": "MultiPolygon, {"type": "Polygon", "c, {"type": "MultiPolygon |

## Candidate questions

- (none templated)

_profiled 2026-09-09 · `python3 tools/profile.py open_tree_equity_score_2025_inner_urban`_
