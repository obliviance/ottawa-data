# 2022 Elections Voting Subdivision Map

`open_2022_elections_voting_subdivision_map` · shape **arcgis-hub** · source `open-ottawa` · **spatial**

- origin: <https://open.ottawa.ca/datasets/ottawa::2022-elections-voting-subdivision-map>
- fetched 2026-09-09 · **1,179 rows** · 10 columns
- geojson · licence: https://ottawa.ca/en/city-hall/get-know-your-city/open-data#open-data-licence-ve

## Columns

| column | kind | non-null | distinct | summary |
| --- | --- | --- | --- | --- |
| `FID` | num | 100% | 1,179 | 1.00 · p25 296 · p50 590 · p95 1,120 · max 1,179  ██▇██▇██▇█▇██▇██ |
| `VOT_SUBD` | id/text | 100% | 1,179 | e.g. 03-004.6, 02-011.4, 08-015.2 |
| `WARD_NUM` | num | 100% | 24 | 1.00 · p25 6.00 · p50 12.00 · p95 23.00 · max 24.00  █▃▅▃▇▃▆▃▃▅▃▆▃▅▂▇ |
| `WARD` | cat | 100% | 24 | Orléans West-Innes 6%, College 6%, Orléans East-Cumberland 5%, Kanata South 5%, Gloucester-Southgate 5%, Barrhaven East 5% |
| `QUARTIER` | cat | 100% | 24 | Orléans-Ouest-Innes 6%, Collège 6%, Orléans-Est-Cumberland 5%, Kanata-Sud 5%, Gloucester-Southgate 5%, Barrhaven-Est 5% |
| `SHAPE_AREA` | num | 100% | 1,179 | 646 · p25 164,888 · p50 252,098 · p95 16,089,585 · max 119,492,766  █▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁ |
| `SHAPE_LEN` | num | 100% | 1,179 | 105 · p25 2,067 · p50 2,687 · p95 21,496 · max 46,515  █▃▁▁▁▁▁▁▁▁▁▁▁▁▁▁ |
| `Shape__Area` | num | 100% | 1,179 | 1,312 · p25 334,743 · p50 511,280 · p95 32,442,638 · max 239,312,973  █▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁ |
| `Shape__Length` | num | 100% | 1,179 | 149 · p25 2,941 · p50 3,825 · p95 30,503 · max 65,825  █▃▁▁▁▁▁▁▁▁▁▁▁▁▁▁ |
| `geometry` | id/text | 100% | 1,179 | e.g. {"type": "Polygon", "c, {"type": "Polygon", "c, {"type": "Polygon", "c |

## Candidate questions

- `WARD_NUM` by `WARD` — equity gradient? (join ONS income)
- Spatial clustering of open_2022_elections_voting_subdivision_map; overlay wards + the decision timeline

_profiled 2026-09-09 · `python3 tools/profile.py open_2022_elections_voting_subdivision_map`_
