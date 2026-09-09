# Ottawa Paramedic Service daily response volume

`open_ottawa_paramedic_service_daily_response_volume` · shape **arcgis-hub** · source `open-ottawa`

- origin: <https://open.ottawa.ca/datasets/ottawa::ottawa-paramedic-service-daily-response-volume>
- fetched 2026-09-09 · **1,095 rows** · 3 columns
- csv · licence: https://ottawa.ca/en/city-hall/get-know-your-city/open-data#open-data-licence-ve

## Columns

| column | kind | non-null | distinct | summary |
| --- | --- | --- | --- | --- |
| `Date` | date | 100% | 1,095 | 2021-01-01 → 2023-12-31 |
| `Responses` | num | 100% | 329 | 262 · p25 424 · p50 479 · p95 620 · max 763  ▁▁▂▃▅▇▇█▇▅▃▂▁▁▁▁ |
| `ObjectId` | num | 100% | 1,095 | 1.00 · p25 274 · p50 548 · p95 1,040 · max 1,095  █▇█▇▇█▇█▇▇█▇▇█▇█ |

## Candidate questions

- Trend / seasonality of open_ottawa_paramedic_service_daily_response_volume over `Date`; structural breaks?

_profiled 2026-09-09 · `python3 tools/profile.py open_ottawa_paramedic_service_daily_response_volume`_
