# Cycling Network

`open_cycling_network` · shape **arcgis-hub** · source `open-ottawa`

- origin: <https://open.ottawa.ca/datasets/ottawa::cycling-network>
- fetched 2026-09-09 · **15,783 rows** · 4 columns
- csv · licence: https://ottawa.ca/en/city-hall/get-know-your-city/open-data#open-data-licence-ve

## Columns

| column | kind | non-null | distinct | summary |
| --- | --- | --- | --- | --- |
| `OBJECTID` | num | 100% | 15,783 | 54,442 · p25 58,782 · p50 62,884 · p95 81,348 · max 88,751  ▇▇▇▇█▆▂▃▂▂▂▁▂▁▁▁ |
| `EXISTING_CYCLING_NETWORK` | cat | 78% | 9 | Path 45%, Suggested Route 24%, Network Link 12%, Bike Lane 11%, Paved Shoulder 5%, Cycle Track 2% |
| `Shape_Length` | num | 100% | 15,772 | 0.01 · p25 50.49 · p50 120 · p95 1,105 · max 29,703  █▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁ |
| `GlobalID` | id/text | 100% | 15,783 | e.g. {E3B72A48-54ED-4E81-B0, {590A036B-84F7-4E88-83, {98F24252-7E21-4F92-92 |

## Candidate questions

- (none templated)

_profiled 2026-09-09 · `python3 tools/profile.py open_cycling_network`_
