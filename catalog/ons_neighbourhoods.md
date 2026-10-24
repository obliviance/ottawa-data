# Ottawa Neighbourhood Study — neighbourhoods (Gen 3)

`ons_neighbourhoods` · shape **json-api** · source `ons` · **spatial**

- origin: <https://ons-sqo.ca/wp-json/ons/v1/get-data/neighbourhoods>
- fetched 2026-10-24 · **116 rows** · 5 columns
- geometry = JSON {position, bounds, latLngs}; ONS_ID joins ons_indicator_values

## Columns

| column | kind | non-null | distinct | summary |
| --- | --- | --- | --- | --- |
| `name` | id/text | 100% | 116 | e.g. Airport, Alta Vista, Bayshore |
| `description` | cat | 100% | 1 |  100% |
| `geometry` | id/text | 100% | 116 | e.g. {"position": {"lat": 4, {"position": {"lat": 4, {"position": {"lat": 4 |
| `ONS_ID` | num | 100% | 116 | 3,001 · p25 3,030 · p50 3,058 · p95 3,111 · max 3,117  █▇▇█▇▇▇█▇▇▇█▇▆▇█ |
| `name_fr` | id/text | 100% | 116 | e.g. Aéroport, Alta Vista, Bayshore  |

## Candidate questions

- (none templated)

_profiled 2026-10-24 · `python3 tools/profile.py ons_neighbourhoods`_
