# Ottawa Neighbourhood Study (ONS) - Neighbourhood Boundaries Gen 2 (Historical)

`open_ottawa_neighbourhood_study_ons_neighbourhood_boundaries_gen_2_hist` · shape **arcgis-hub** · source `open-ottawa` · **spatial**

- origin: <https://open.ottawa.ca/datasets/ottawa::ottawa-neighbourhood-study-ons-neighbourhood-boundaries-gen-2-historical>
- fetched 2026-09-09 · **111 rows** · 9 columns
- geojson · licence: https://ottawa.ca/en/city-hall/get-know-your-city/open-data#open-data-licence-ve

## Columns

| column | kind | non-null | distinct | summary |
| --- | --- | --- | --- | --- |
| `FID` | num | 100% | 111 | 1.00 · p25 28.50 · p50 56.00 · p95 106 · max 111  ████████▇███████ |
| `flag` | num | 100% | 3 | 0.00 · p25 0.00 · p50 0.00 · p95 1.00 · max 3.00  █▁▁▁▁▆▁▁▁▁▁▁▁▁▁▁ |
| `ONS_ID` | num | 100% | 111 | 3.00 · p25 54.50 · p50 903 · p95 952 · max 958  ▄▃▁▁▁▁▁▁▁▁▁▁▁▁▁█ |
| `Name` | id/text | 100% | 111 | e.g. Old Barrhaven West, Beacon Hill South - Ca, Beaverbrook |
| `POPEST` | num | 100% | 111 | 17.00 · p25 4,372 · p50 6,727 · p95 18,148 · max 26,674  ▃▄▆█▅▅▅▂▂▁▁▁▁▁▁▁ |
| `Name_FR` | text | 100% | 52 | e.g. Old Barrhaven Ouest, Beacon Hill Sud - Card,   |
| `Shape__Area` | num | 100% | 111 | 416,360 · p25 4,235,271 · p50 6,935,196 · p95 287,164,570 · max 491,356,930  █▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁ |
| `Shape__Length` | num | 100% | 111 | 3,527 · p25 10,064 · p50 13,184 · p95 103,246 · max 248,572  █▂▁▁▁▁▁▁▁▁▁▁▁▁▁▁ |
| `geometry` | id/text | 100% | 111 | e.g. {"type": "Polygon", "c, {"type": "Polygon", "c, {"type": "Polygon", "c |

## Candidate questions

- (none templated)

_profiled 2026-09-09 · `python3 tools/profile.py open_ottawa_neighbourhood_study_ons_neighbourhood_boundaries_gen_2_hist`_
