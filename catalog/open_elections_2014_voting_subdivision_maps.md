# Elections 2014 Voting Subdivision Maps

`open_elections_2014_voting_subdivision_maps` · shape **arcgis-hub** · source `open-ottawa` · **spatial**

- origin: <https://open.ottawa.ca/datasets/ottawa::elections-2014-voting-subdivision-maps>
- fetched 2026-09-09 · **1,093 rows** · 11 columns
- geojson · licence: https://ottawa.ca/en/city-hall/get-know-your-city/open-data#open-data-licence-ve

## Columns

| column | kind | non-null | distinct | summary |
| --- | --- | --- | --- | --- |
| `FID` | num | 100% | 1,093 | 1.00 · p25 274 · p50 547 · p95 1,038 · max 1,093  █▇▇█▇▇▇█▇▇▇█▇▇▇█ |
| `OBJECTID` | num | 100% | 1,093 | 91,809 · p25 92,082 · p50 92,355 · p95 92,846 · max 92,901  █▇▇█▇▇▇█▇▇▇█▇▇▇█ |
| `VOT_SUBD` | id/text | 100% | 1,092 | e.g. 23-009.2, 23-006.5, 23-001.2 |
| `WARD` | num | 100% | 23 | 1.00 · p25 6.00 · p50 12.00 · p95 23.00 · max 23.00  ▇▄▅▂▃█▄▆▃▃▆▃▄▅▃▇ |
| `WARD_EN` | cat | 100% | 23 | COLLEGE 6%, ORLÉANS 6%, KANATA SOUTH 5%, BARRHAVEN 5%, ALTA VISTA 5%, RIVER 5% |
| `WARD_FR` | cat | 100% | 23 | COLLÈGE 6%, ORLÉANS 6%, KANATA-SUD 5%, BARRHAVEN 5%, ALTA VISTA 5%, RIVIÈRE 5% |
| `SHAPE_AREA` | num | 100% | 1,093 | 8.10 · p25 157,178 · p50 253,658 · p95 20,186,970 · max 119,470,345  █▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁ |
| `SHAPE_LEN` | num | 100% | 1,093 | 105 · p25 1,939 · p50 2,552 · p95 21,926 · max 46,479  █▃▁▁▁▁▁▁▁▁▁▁▁▁▁▁ |
| `Shape__Area` | num | 100% | 1,093 | 16.21 · p25 318,552 · p50 513,264 · p95 40,910,283 · max 239,268,135  █▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁ |
| `Shape__Length` | num | 100% | 1,093 | 149 · p25 2,759 · p50 3,628 · p95 31,195 · max 65,774  █▃▁▁▁▁▁▁▁▁▁▁▁▁▁▁ |
| `geometry` | id/text | 100% | 1,093 | e.g. {"type": "Polygon", "c, {"type": "Polygon", "c, {"type": "Polygon", "c |

## Candidate questions

- `WARD` by `WARD` — equity gradient? (join ONS income)
- Spatial clustering of open_elections_2014_voting_subdivision_maps; overlay wards + the decision timeline

_profiled 2026-09-09 · `python3 tools/profile.py open_elections_2014_voting_subdivision_maps`_
