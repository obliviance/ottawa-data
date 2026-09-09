# Railway Lines

`open_railway_lines` · shape **arcgis-hub** · source `open-ottawa`

- origin: <https://open.ottawa.ca/datasets/ottawa::railway-lines>
- fetched 2026-09-09 · **167 rows** · 13 columns
- csv · licence: https://ottawa.ca/en/city-hall/get-know-your-city/open-data#open-data-licence-ve

## Columns

| column | kind | non-null | distinct | summary |
| --- | --- | --- | --- | --- |
| `OBJECTID` | num | 100% | 167 | 1.00 · p25 42.50 · p50 84.00 · p95 159 · max 729  ██▇▄▁▁▁▁▁▁▁▁▁▁▁▂ |
| `STATUS` | cat | 100% | 2 | Active 93%, Non-Active 7% |
| `LEGAL_NAME` | cat | 53% | 19 | Walkley Line 46%, Trillium Line (O-Train) 12%, Trillium Rail Corridor 6%, Alexandria Subdivision " 4%, Beachburg Subdivision  " 3%, Alexandria Subdivision 3% |
| `COMMON_NAME` | cat | 100% | 15 | O-Train Confederation Li 47%, Walkley Rail Corridor 25%, Trillium Rail Corridor 10%, Beachburg Rail Corridor 4%, Alexandria Rail Corridor 4%, Montreal and Ottawa Rail 3% |
| `RAIL_TYPE` | cat | 92% | 2 | LRT 50%, Heavy 50% |
| `MISC` | cat | 53% | 13 | Walkley 46%, Trillium 13%, Beachburg 8%, Alexandria 8%, Prescott 6%, Montreal and Ottawa 6% |
| `COMMONNAME_FR` | cat | 100% | 14 | Ligne de la Confédératio 47%, corridor ferroviaire Wal 25%, corridor ferroviaire Tri 7%, corridor ferroviaire Bea 4%, corridor ferroviaire Ale 4%, corridor ferroviaire Pre 3% |
| `LABEL_BIL` | cat | 53% | 14 | corridor ferroviaire Wal 46%, corridor ferroviaire Tri 13%, corridor ferroviaire Bea 8%, corridor ferroviaire Ale 7%, corridor ferroviaire Pre 6%, corridor ferroviaire Mon 6% |
| `GIS_UNIQUE_ID` | text | 0% | 0 | e.g.  |
| `GLOBALID` | id/text | 100% | 167 | e.g. {481F7204-40B8-4AE7-A5, {D2C7AA2E-3AF5-42F2-8C, {089EFD33-34D7-4A46-AE |
| `CREATED_DATE` | date | 50% | 5 | 2022-07-04 → 2025-04-25, 1 gaps >30d |
| `LAST_EDITED_DATE` | date | 100% | 80 | 2017-04-13 → 2026-06-09, 4 gaps >30d |
| `Shape_Length` | num | 100% | 167 | 24.27 · p25 224 · p50 592 · p95 14,579 · max 54,796  █▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁ |

## Candidate questions

- (none templated)

_profiled 2026-09-09 · `python3 tools/profile.py open_railway_lines`_
