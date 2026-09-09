# Urban Fences

`open_urban_fences` · shape **arcgis-hub** · source `open-ottawa`

- origin: <https://open.ottawa.ca/datasets/ottawa::urban-fences>
- fetched 2026-09-09 · **403,819 rows** · 6 columns
- csv · licence: https://ottawa.ca/en/city-hall/get-know-your-city/open-data#open-data-licence-ve

## Columns

| column | kind | non-null | distinct | summary |
| --- | --- | --- | --- | --- |
| `OBJECTID` | num | 100% | 403,819 | 336,947 · p25 437,902 · p50 538,856 · p95 720,574 · max 740,765  ██▇██▇██▇█▇██▇██ |
| `Shape` | text | 0% | 0 | e.g.  |
| `FEAT_NAME` | cat | 100% | 4 | wood 76%, wire 19%, unknown 3%, chainlink 2% |
| `YEAR` | num | 100% | 3 | 2,005 · p25 2,009 · p50 2,019 · p95 2,019 · max 2,019  ▃▁▁▁▁▁▁▁▁▁▁▁▁▁▁█ |
| `Shape_Length` | num | 100% | 403,467 | 0.00 · p25 5.64 · p50 14.69 · p95 93.87 · max 1,341  █▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁ |
| `GlobalID` | id/text | 100% | 403,819 | e.g. {0064E004-BE7E-45C6-A3, {00F7E7C5-2981-4FCE-94, {011CE630-CBAE-4FA6-B2 |

## Candidate questions

- Trend / seasonality of open_urban_fences over `YEAR`; structural breaks?

_profiled 2026-09-09 · `python3 tools/profile.py open_urban_fences`_
