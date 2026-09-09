# Recovered Needles and Glass Pipes

`open_recovered_needles_and_glass_pipes` · shape **arcgis-hub** · source `open-ottawa`

- origin: <https://open.ottawa.ca/datasets/ottawa::recovered-needles-and-glass-pipes>
- fetched 2026-09-09 · **11,090 rows** · 12 columns
- csv · licence: https://open.ottawa.ca/pages/open-data-licence

## Columns

| column | kind | non-null | distinct | summary |
| --- | --- | --- | --- | --- |
| `Source` | cat | 100% | 3 | Needle Hunters 59%, City Staff 36%, Residents/Businesses 4% |
| `Year_Month` | date | 100% | 63 | 2021-01-01 → 2026-03-01, 36 gaps >30d |
| `Total_Needles` | num | 84% | 310 | 0.00 · p25 2.00 · p50 4.00 · p95 85.00 · max 888  █▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁ |
| `Total_Glass_Pipes` | num | 69% | 233 | 0.00 · p25 1.00 · p50 3.00 · p95 60.00 · max 982  █▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁ |
| `Intersection` | text | 99% | 1,170 | e.g. BOOTH ST, ECCLES ST, BOOTH ST, ECCLES ST S, BY WARD MARKET SQ, YOR |
| `X_Coordinate_of_Closest_Intersection` | num | 100% | 799 | -76.17 · p25 -75.70 · p50 -75.69 · p95 -75.66 · max 0.00  █▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁ |
| `Y_Coordinate_of_Closest_Intersection` | num | 100% | 635 | 0.00 · p25 45.41 · p50 45.43 · p95 45.44 · max 45.51  ▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁█ |
| `Ward_ID` | num | 99% | 24 | 1.00 · p25 12.00 · p50 12.00 · p95 15.00 · max 24.00  ▁▁▁▁▁▁▁█▁▆▁▁▁▁▁▁ |
| `Ward_Name` | cat | 99% | 25 | RIDEAU-VANIER 54%, SOMERSET 33%, KITCHISSIPPI 6%, CAPITAL 2%, RIVER 2%, RIDEAU-ROCKCLIFFE 1% |
| `ONS_Neighbourhood_ID` | num | 99% | 94 | 0.00 · p25 3,055 · p50 3,068 · p95 3,115 · max 3,117  ▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁█ |
| `ONS_Neighbourhood_Name` | text | 99% | 93 | e.g. WEST CENTRETOWN, LOWERTOWN WEST, SANDY HILL |
| `ObjectId` | num | 100% | 11,090 | 1.00 · p25 2,773 · p50 5,546 · p95 10,536 · max 11,090  █▇▇▇▇▇▇▇▇▇▇▇▇▇▇█ |

## Candidate questions

- Trend / seasonality of open_recovered_needles_and_glass_pipes over `Year_Month`; structural breaks?

_profiled 2026-09-09 · `python3 tools/profile.py open_recovered_needles_and_glass_pipes`_
