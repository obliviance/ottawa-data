# Ditches

`open_ditches` · shape **arcgis-hub** · source `open-ottawa`

- origin: <https://open.ottawa.ca/datasets/ottawa::ditches>
- fetched 2026-09-09 · **61,755 rows** · 4 columns
- csv · licence: https://ottawa.ca/en/city-hall/get-know-your-city/open-data#open-data-licence-ve

## Columns

| column | kind | non-null | distinct | summary |
| --- | --- | --- | --- | --- |
| `OBJECTID` | num | 100% | 61,755 | 112,410 · p25 127,848 · p50 143,287 · p95 171,076 · max 174,164  ██▇██▇██▇█▇██▇██ |
| `YEAR` | num | 100% | 4 | 2,005 · p25 2,019 · p50 2,019 · p95 2,021 · max 2,021  ▂▁▁▁▁▁▁▁▁▁▁▁▁█▁▂ |
| `Shape_Length` | num | 100% | 61,552 | 0.00 · p25 18.09 · p50 43.42 · p95 292 · max 1,317  █▂▁▁▁▁▁▁▁▁▁▁▁▁▁▁ |
| `GlobalID` | id/text | 100% | 61,755 | e.g. {00562144-7974-4890-AC, {01249234-AE6B-4B4E-A9, {0148A6C1-7BEA-4115-9C |

## Candidate questions

- Trend / seasonality of open_ditches over `YEAR`; structural breaks?

_profiled 2026-09-09 · `python3 tools/profile.py open_ditches`_
