# 3D Buildings LOD1

`open_3d_buildings_lod1` · shape **arcgis-hub** · source `open-ottawa`

- origin: <https://open.ottawa.ca/datasets/ottawa::3d-buildings-lod1>
- fetched 2026-09-09 · **116 rows** · 11 columns
- csv · licence: https://ottawa.ca/en/city-hall/get-know-your-city/open-data#open-data-licence-ve

## Columns

| column | kind | non-null | distinct | summary |
| --- | --- | --- | --- | --- |
| `FID` | num | 100% | 116 | 1.00 · p25 29.75 · p50 58.50 · p95 110 · max 116  █▇▇▇▇█▇▇▇▇█▇▇▇▇█ |
| `join_field` | num | 100% | 116 | 9,046 · p25 9,075 · p50 9,104 · p95 9,156 · max 9,162  █▇▇█▇▇▇█▇▇▆█▇▇▇█ |
| `SHAPE_Leng` | num | 100% | 116 | 4,668 · p25 9,791 · p50 12,858 · p95 90,397 · max 112,536  █▆▂▁▁▁▁▁▁▁▁▁▁▁▁▁ |
| `SHAPE_Area` | num | 100% | 116 | 1,004,756 · p25 4,253,188 · p50 7,542,453 · p95 305,340,028 · max 522,850,673  █▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁ |
| `ONS_ID` | num | 100% | 116 | 3,001 · p25 3,030 · p50 3,058 · p95 3,111 · max 3,117  █▇▇█▇▇▇█▇▇▇█▇▆▇█ |
| `ONS_Name` | id/text | 100% | 116 | e.g. TREND-ARLINGTON, NAVAN - SARSFIELD, MUNSTER - ASHTON |
| `ONS_Region` | cat | 100% | 1 | OTTAWA 100% |
| `Shape__Area` | num | 100% | 116 | 1,004,756 · p25 4,253,188 · p50 7,542,453 · p95 305,340,037 · max 522,850,673  █▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁ |
| `Shape__Length` | num | 100% | 116 | 4,668 · p25 9,423 · p50 12,858 · p95 88,908 · max 109,679  █▇▂▂▁▁▁▁▁▁▁▂▁▁▁▁ |
| `DXF` | id/text | 100% | 114 | e.g. https://arcg.is/rWrLO, https://arcg.is/0qXLa, https://arcg.is/1mSqy1 |
| `GDB` | id/text | 100% | 114 | e.g. https://arcg.is/191uWm, https://arcg.is/0zWenX, https://arcg.is/0LvzL0 |

## Candidate questions

- (none templated)

_profiled 2026-09-09 · `python3 tools/profile.py open_3d_buildings_lod1`_
