# Transportation Midblock Volume 2025

`open_transportation_midblock_volume_2025` · shape **arcgis-hub** · source `open-ottawa` · **spatial**

- origin: <https://open.ottawa.ca/datasets/ottawa::transportation-midblock-volume-2025>
- fetched 2026-09-09 · **742 rows** · 11 columns
- csv · licence: https://ottawa.ca/en/city-hall/get-know-your-city/open-data#open-data-licence-ve

## Columns

| column | kind | non-null | distinct | summary |
| --- | --- | --- | --- | --- |
| `X` | num | 100% | 731 | -8,488,206 · p25 -8,434,055 · p50 -8,426,300 · p95 -8,401,986 · max -8,382,682  ▁▁▁▁▁▂▂▂▆█▄▁▂▂▁▁ |
| `Y` | num | 100% | 740 | 5,617,867 · p25 5,667,714 · p50 5,679,675 · p95 5,696,125 · max 5,703,482  ▁▁▁▁▁▁▁▂▆▃▅▇█▇▅▁ |
| `Geo_ID` | id/text | 100% | 742 | e.g. e___2JRR, __3Z00AN, __3Z06YU |
| `Midblock` | id/text | 100% | 742 | e.g. CELESTIAL GROVE btwn P, BEVERLY ST btwn DELAME, SHORELINE DR btwn COVE |
| `AADT_Year` | num | 100% | 1 | 2,025 · p25 2,025 · p50 2,025 · p95 2,025 · max 2,025   |
| `AADT_Volume` | num | 100% | 659 | 35.00 · p25 383 · p50 1,004 · p95 14,144 · max 33,078  █▂▁▁▁▁▁▁▁▁▁▁▁▁▁▁ |
| `Latitude` | num | 100% | 727 | 44.98 · p25 45.29 · p50 45.37 · p95 45.47 · max 45.52  ▁▁▁▁▁▁▁▂▆▄▅▇█▆▅▁ |
| `Longitude` | num | 100% | 725 | -76.25 · p25 -75.76 · p50 -75.69 · p95 -75.48 · max -75.30  ▁▁▁▁▁▂▂▂▆█▄▁▂▂▁▁ |
| `POINT_X` | num | 100% | 741 | 324,298 · p25 362,475 · p50 367,863 · p95 384,856 · max 398,403  ▁▁▁▁▁▂▂▂▆█▄▁▂▂▁▁ |
| `POINT_Y` | num | 100% | 731 | 4,982,095 · p25 5,017,176 · p50 5,025,652 · p95 5,037,391 · max 5,042,632  ▁▁▁▁▁▁▁▂▆▃▅▇█▇▄▁ |
| `FID` | num | 100% | 742 | 1.00 · p25 186 · p50 372 · p95 705 · max 742  █▇▇█▇▇█▇▇█▇▇█▇▇█ |

## Candidate questions

- Trend / seasonality of open_transportation_midblock_volume_2025 over `AADT_Year`; structural breaks?
- Spatial clustering of open_transportation_midblock_volume_2025; overlay wards + the decision timeline

_profiled 2026-09-09 · `python3 tools/profile.py open_transportation_midblock_volume_2025`_
