# Elections 2014 Voting Places

`open_elections_2014_voting_places` · shape **arcgis-hub** · source `open-ottawa`

- origin: <https://open.ottawa.ca/datasets/ottawa::elections-2014-voting-places>
- fetched 2026-09-09 · **565 rows** · 6 columns
- csv · licence: https://ottawa.ca/en/city-hall/get-know-your-city/open-data#open-data-licence-ve

## Columns

| column | kind | non-null | distinct | summary |
| --- | --- | --- | --- | --- |
| `FID` | num | 100% | 565 | 1.00 · p25 142 · p50 283 · p95 537 · max 565  █▇▇█▇▇▇█▇▇▇█▇▇▇█ |
| `OBJECTID` | num | 100% | 565 | 5,201 · p25 5,342 · p50 5,483 · p95 5,737 · max 5,765  █▇▇█▇▇▇█▇▇▇█▇▇▇█ |
| `LOCATION_N` | id/text | 100% | 511 | e.g. Hunt Club/Riverside Pa, Suites of Landmark, The Denbury |
| `ADDRESS_EN` | id/text | 100% | 513 | e.g. 3320 Paul Anka Dr, 136 Darlington Pvt, 2951 Riverside Dr |
| `ADDRESS_FR` | id/text | 100% | 512 | e.g. 3320, prom Paul Anka, 136, priv Darlington, 2951, prom Riverside |
| `WARD_POLL_` | id/text | 100% | 564 | e.g. 916000, 316009, 316005 |

## Candidate questions

- (none templated)

_profiled 2026-09-09 · `python3 tools/profile.py open_elections_2014_voting_places`_
