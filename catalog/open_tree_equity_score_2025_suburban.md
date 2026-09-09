# Tree Equity Score 2025 - Suburban

`open_tree_equity_score_2025_suburban` · shape **arcgis-hub** · source `open-ottawa` · **spatial**

- origin: <https://open.ottawa.ca/datasets/ottawa::tree-equity-score-2025-suburban>
- fetched 2026-09-09 · **80 rows** · 23 columns
- geojson · licence: Open Data | City of Ottawa

## Columns

| column | kind | non-null | distinct | summary |
| --- | --- | --- | --- | --- |
| `FID` | num | 100% | 80 | 1.00 · p25 20.75 · p50 40.50 · p95 76.05 · max 80.00  ████████████████ |
| `CTUID` | num | 100% | 80 | 5,050,124 · p25 5,050,140 · p50 5,050,151 · p95 5,050,171 · max 5,050,300  ▆█▃▆▇▁▁▁▁▁▁▁▁▁▁▁ |
| `CTNUM` | num | 100% | 80 | 124 · p25 140 · p50 151 · p95 171 · max 300  ▆█▃▆▇▁▁▁▁▁▁▁▁▁▁▁ |
| `CANCVR_R` | num | 100% | 26 | 1.00 · p25 8.00 · p50 15.00 · p95 25.00 · max 29.00  ▂▄▅▃▃▂▅▄▃▄█▃▂▃▂▁ |
| `CANGOAL` | num | 100% | 1 | 40.00 · p25 40.00 · p50 40.00 · p95 40.00 · max 40.00   |
| `CANGAP` | num | 100% | 26 | 11.00 · p25 21.00 · p50 25.00 · p95 37.00 · max 39.00  ▁▂▃▂▃█▄▅▂▅▂▄▂▅▄▂ |
| `GAPSCORE` | num | 100% | 26 | 0.28 · p25 0.54 · p50 0.64 · p95 0.95 · max 1.00  ▁▂▃▂▃█▄▅▂▅▂▄▂▅▄▂ |
| `E` | num | 100% | 80 | 0.20 · p25 0.36 · p50 0.39 · p95 0.52 · max 0.61  ▁▁▁▁▃▃█▅▆▄▄▂▂▁▁▁ |
| `TES_R` | num | 100% | 31 | 48.00 · p25 67.50 · p50 75.00 · p95 86.10 · max 90.00  ▁▁▁▃▂▁▂▁▅▃▃▄█▃▁▂ |
| `NOTE_EN` | cat | 100% | 2 |   78%, This census tract contai 22% |
| `NOTE_FR` | cat | 100% | 2 |   78%, Ce secteur de recensemen 22% |
| `CREATED_DA` | text | 0% | 0 | e.g.  |
| `LAST_EDITE` | cat | 100% | 1 | 2025-09-09T00:00:00Z 100% |
| `CTNAME_EN` | id/text | 100% | 80 | e.g. Stittsville-Iber Rd-St, Nottinggate South-Prov, Orleans Village-Chatea |
| `CTNAME_FR` | id/text | 100% | 80 | e.g. Stittsville-chemin Ibe, Notting Gate-Sud-Prove, Village d’Orléans–Chât |
| `TRNSCT_EN` | cat | 100% | 1 | Suburban 100% |
| `TRNSCT_FR` | cat | 100% | 1 | Suburbain 100% |
| `PA_EN` | cat | 100% | 3 |   98%, Yes 1%, No 1% |
| `PA_FR` | cat | 100% | 3 |   98%, Oui 1%, Non 1% |
| `GLOBALID` | id/text | 100% | 80 | e.g. {5E5B844E-543A-464B-BB, {A35239BB-99E0-4E14-92, {469AB2CD-F4E7-40C1-9B |
| `Shape__Area` | num | 100% | 80 | 423,639 · p25 1,832,645 · p50 2,268,920 · p95 4,431,890 · max 6,310,162  ▁▁▃▅▆█▃▃▁▁▁▁▁▁▁▁ |
| `Shape__Length` | num | 100% | 80 | 4,448 · p25 9,547 · p50 12,232 · p95 24,327 · max 40,437  ▂▄█▆▃▂▃▁▂▁▁▁▁▁▁▁ |
| `geometry` | id/text | 100% | 80 | e.g. {"type": "MultiPolygon, {"type": "Polygon", "c, {"type": "Polygon", "c |

## Candidate questions

- (none templated)

_profiled 2026-09-09 · `python3 tools/profile.py open_tree_equity_score_2025_suburban`_
