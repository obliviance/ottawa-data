# Public Health Inspection Data - Recreational Camps — businesses.csv

`open_public_health_inspection_data_recreational_camps__businesses` · shape **arcgis-hub** · source `ottawa-public-health` · **spatial**

- origin: <https://open.ottawa.ca/documents/ottawa::public-health-inspection-data-recreational-camps>
- fetched 2026-09-09 · **15 rows** · 9 columns
- from zip · licence: https://ottawa.ca/en/city-hall/get-know-your-city/open-data#open-data-licence-ve

## Columns

| column | kind | non-null | distinct | summary |
| --- | --- | --- | --- | --- |
| `business_id` | cat | 100% | 15 | 66500EDD-AA28-4828-99FC- 7%, 78FE5709-EA7E-4E4F-AAD3- 7%, 1637F599-74FF-45F5-8122- 7%, 544E3D4D-37DF-40F3-9778- 7%, B9C390EB-2F68-40AC-B97C- 7%, 586CCDDE-1C37-457B-BE3F- 7% |
| `name` | cat | 100% | 15 | RIDEAUVIEW COMMUNITY CEN 7%, CHILDRENS VILLAGE SUMMER 7%, CHILDREN'S VILLAGE SUMME 7%, RCMP CAMP LONG ISLAND 7%, KANATA RESEARCH PARK FAM 7%, MC SHEFFREY DAY CAMP 7% |
| `address` | cat | 100% | 15 | 4310 SHORELINE Rd 7%, 4 THORNCLIFF PLACE 7%, 25 GIBBARD Ave 7%, 415 NICOLLS ISLAND Rd 7%, 100 PENFIELD Dr 7%, 2540 POLLOCK Rd 7% |
| `city` | cat | 100% | 2 | OTTAWA 93%, KANATA 7% |
| `state` | cat | 100% | 1 | ON 100% |
| `postal_code` | cat | 100% | 15 | K1V 1N4 7%, K2H 6L2 7%, K2G 3T9 7%, K4M 1A2 7%, K2K 2V7 7%, K0A 2T0 7% |
| `latitude` | num | 100% | 15 | 45.14 · p25 45.28 · p50 45.33 · p95 45.46 · max 45.51  ▃▁▁▁▅▃▅▃█▃▁▃▅▁▁▃ |
| `longitude` | num | 100% | 15 | -76.15 · p25 -75.91 · p50 -75.76 · p95 -75.64 · max -75.55  ▃▁▁▁▁▅▅▁▃▁▅██▁▁▃ |
| `phone_number` | num | 26% | 4 | 16,135,911,995 · p25 16,135,970,709 · p50 16,136,633,675 · p95 16,138,164,609 · max 16,138,321,234  █▁▁▁▁▁▁▁▁▄▁▁▁▁▁▄ |

## Candidate questions

- (none templated)

_profiled 2026-09-09 · `python3 tools/profile.py open_public_health_inspection_data_recreational_camps__businesses`_
