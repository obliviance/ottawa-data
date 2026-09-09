# Ottawa Neighbourhood Study (ONS) - Neighbourhood Boundaries Gen 3

`open_ottawa_neighbourhood_study_ons_neighbourhood_boundaries_gen_3` · shape **arcgis-hub** · source `open-ottawa` · **spatial**

- origin: <https://open.ottawa.ca/datasets/ottawa::ottawa-neighbourhood-study-ons-neighbourhood-boundaries-gen-3>
- fetched 2026-09-09 · **116 rows** · 9 columns
- geojson · licence: https://ottawa.ca/en/city-hall/get-know-your-city/open-data#open-data-licence-ve

## Columns

| column | kind | non-null | distinct | summary |
| --- | --- | --- | --- | --- |
| `FID` | num | 100% | 116 | 1.00 · p25 29.75 · p50 58.50 · p95 110 · max 116  █▇▇▇▇█▇▇▇▇█▇▇▇▇█ |
| `ONS_ID` | num | 100% | 116 | 3,001 · p25 3,030 · p50 3,058 · p95 3,111 · max 3,117  █▇▇█▇▇▇█▇▇▇█▇▆▇█ |
| `ONS_Name` | id/text | 100% | 116 | e.g. TREND-ARLINGTON, NAVAN - SARSFIELD, MUNSTER - ASHTON |
| `ONS_Region` | cat | 100% | 1 | OTTAWA 100% |
| `Shape_Leng` | num | 100% | 114 | 4,668 · p25 9,353 · p50 12,716 · p95 85,928 · max 109,339  █▆▂▂▁▁▁▁▁▁▁▁▁▁▁▁ |
| `Shape_Area` | num | 100% | 114 | 1,004,756 · p25 4,342,615 · p50 7,424,005 · p95 300,992,572 · max 522,814,451  █▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁ |
| `Shape__Area` | num | 100% | 116 | 1,004,756 · p25 4,348,817 · p50 8,198,220 · p95 300,859,675 · max 522,349,321  █▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁ |
| `Shape__Length` | num | 100% | 116 | 4,668 · p25 9,803 · p50 13,173 · p95 85,982 · max 115,241  █▆▂▁▁▁▁▁▁▁▁▁▁▁▁▁ |
| `geometry` | id/text | 100% | 116 | e.g. {"type": "Polygon", "c, {"type": "Polygon", "c, {"type": "Polygon", "c |

## Candidate questions

- (none templated)

_profiled 2026-09-09 · `python3 tools/profile.py open_ottawa_neighbourhood_study_ons_neighbourhood_boundaries_gen_3`_
