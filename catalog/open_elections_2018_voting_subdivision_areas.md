# Elections 2018 Voting Subdivision Areas

`open_elections_2018_voting_subdivision_areas` · shape **arcgis-hub** · source `open-ottawa` · **spatial**

- origin: <https://open.ottawa.ca/datasets/ottawa::elections-2018-voting-subdivision-areas>
- fetched 2026-09-09 · **1,134 rows** · 8 columns
- geojson · licence: https://ottawa.ca/en/city-hall/get-know-your-city/open-data#open-data-licence-ve

## Columns

| column | kind | non-null | distinct | summary |
| --- | --- | --- | --- | --- |
| `FID` | num | 100% | 1,134 | 1.00 · p25 284 · p50 568 · p95 1,077 · max 1,134  █████▇████▇█████ |
| `VOT_SUBD` | id/text | 100% | 1,134 | e.g. 11-013.1, 08-022.2, 08-013.1 |
| `WARD` | num | 100% | 23 | 1.00 · p25 6.00 · p50 12.00 · p95 23.00 · max 23.00  █▄▅▃▃▇▄▆▃▃▆▃▄▆▃▇ |
| `WARD_EN` | cat | 100% | 23 | COLLEGE 6%, BARRHAVEN 6%, ORLÉANS 6%, KANATA SOUTH 5%, INNES 5%, CUMBERLAND 5% |
| `WARD_FR` | cat | 100% | 23 | COLLÈGE 6%, BARRHAVEN 6%, ORLÉANS 6%, KANATA-SUD 5%, INNES 5%, CUMBERLAND 5% |
| `Shape__Area` | num | 100% | 1,134 | 646 · p25 153,135 · p50 249,351 · p95 17,690,206 · max 119,470,345  █▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁ |
| `Shape__Length` | num | 100% | 1,134 | 105 · p25 1,948 · p50 2,620 · p95 22,000 · max 46,479  █▃▁▁▁▁▁▁▁▁▁▁▁▁▁▁ |
| `geometry` | id/text | 100% | 1,134 | e.g. {"type": "Polygon", "c, {"type": "Polygon", "c, {"type": "Polygon", "c |

## Candidate questions

- `WARD` by `WARD` — equity gradient? (join ONS income)
- Spatial clustering of open_elections_2018_voting_subdivision_areas; overlay wards + the decision timeline

_profiled 2026-09-09 · `python3 tools/profile.py open_elections_2018_voting_subdivision_areas`_
