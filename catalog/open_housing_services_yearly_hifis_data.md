#  Housing Services yearly HIFIS data

`open_housing_services_yearly_hifis_data` · shape **arcgis-hub** · source `open-ottawa`

- origin: <https://open.ottawa.ca/datasets/ottawa::-housing-services-yearly-hifis-data>
- fetched 2026-09-09 · **212 rows** · 5 columns
- csv · licence: https://ottawa.ca/en/city-hall/open-transparent-and-accountable-government/open-

## Columns

| column | kind | non-null | distinct | summary |
| --- | --- | --- | --- | --- |
| `Date` | num | 100% | 12 | 2,014 · p25 2,017 · p50 2,021 · p95 2,025 · max 2,025  ▅▅▅▁▅▅▁▅▇▁▇▇▁▇██ |
| `Count_` | num | 100% | 200 | 60.00 · p25 398 · p50 1,170 · p95 6,844 · max 9,495  █▆▂▁▂▃▂▁▁▁▁▁▁▁▁▁ |
| `TotalLengthOfStay` | num | 100% | 180 | 5,232 · p25 30,746 · p50 172,122 · p95 724,690 · max 1,299,199  █▁▃▂▁▂▁▁▁▁▁▁▁▁▁▁ |
| `Category` | cat | 100% | 24 | All Clients 6%, All Singles 6%, Family Household Members 6%, Family Households 6%, Family Member 6%, Family Units 6% |
| `ObjectId` | num | 100% | 212 | 1.00 · p25 53.75 · p50 106 · p95 201 · max 212  █▇▇▇▇█▇▇▇▇█▇▇▇▇█ |

## Candidate questions

- (none templated)

_profiled 2026-09-09 · `python3 tools/profile.py open_housing_services_yearly_hifis_data`_
