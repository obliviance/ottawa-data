# Greenfield Residential Land Survey

`open_greenfield_residential_land_survey` · shape **arcgis-hub** · source `open-ottawa`

- origin: <https://open.ottawa.ca/datasets/ottawa::greenfield-residential-land-survey-2024>
- fetched 2026-09-09 · **180 rows** · 19 columns
- csv · licence: https://ottawa.ca/en/city-hall/get-know-your-city/open-data#open-data-licence-ve

## Columns

| column | kind | non-null | distinct | summary |
| --- | --- | --- | --- | --- |
| `FID` | num | 100% | 180 | 1.00 · p25 45.75 · p50 90.50 · p95 171 · max 180  █▇▇▇▇█▇▇▇▇█▇▇▇▇█ |
| `PARCEL_1` | num | 100% | 180 | 100 · p25 293 · p50 473 · p95 764 · max 900  ▃▃▃▅▅▂▂█▄▁▅▃▃▁▂▁ |
| `TOT_UNIT_1` | num | 100% | 150 | 1.00 · p25 56.50 · p50 162 · p95 1,159 · max 8,016  █▂▁▁▁▁▁▁▁▁▁▁▁▁▁▁ |
| `PARC_HA_1` | num | 100% | 167 | 0.06 · p25 1.23 · p50 3.46 · p95 28.98 · max 223  █▂▁▁▁▁▁▁▁▁▁▁▁▁▁▁ |
| `SIN_UNIT_1` | num | 100% | 68 | 0.00 · p25 0.00 · p50 0.00 · p95 264 · max 346  █▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁ |
| `SIN_HA_1` | num | 100% | 78 | 0.00 · p25 0.00 · p50 0.00 · p95 11.11 · max 19.22  █▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁ |
| `SEM_UNIT_1` | num | 100% | 10 | 0.00 · p25 0.00 · p50 0.00 · p95 2.10 · max 136  █▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁ |
| `SEM_HA_1` | num | 100% | 13 | 0.00 · p25 0.00 · p50 0.00 · p95 0.11 · max 3.57  █▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁ |
| `TOW_UNIT_1` | num | 100% | 81 | 0.00 · p25 0.00 · p50 5.00 · p95 429 · max 752  █▂▁▁▁▁▁▁▁▁▁▁▁▁▁▁ |
| `TOW_HA_1` | num | 100% | 89 | 0.00 · p25 0.00 · p50 0.11 · p95 8.35 · max 19.15  █▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁ |
| `STA_UNIT_1` | num | 100% | 25 | 0.00 · p25 0.00 · p50 0.00 · p95 170 · max 930  █▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁ |
| `STA_HA_1` | num | 100% | 26 | 0.00 · p25 0.00 · p50 0.00 · p95 2.03 · max 15.98  █▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁ |
| `APA_UNIT_1` | num | 100% | 28 | 0.00 · p25 0.00 · p50 0.00 · p95 299 · max 1,857  █▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁ |
| `APA_HA_1` | num | 100% | 27 | 0.00 · p25 0.00 · p50 0.00 · p95 1.90 · max 10.76  █▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁ |
| `MIX_UNIT_1` | num | 100% | 50 | 0.00 · p25 0.00 · p50 0.00 · p95 787 · max 8,016  █▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁ |
| `MIX_HA_1` | num | 100% | 55 | 0.00 · p25 0.00 · p50 0.00 · p95 21.76 · max 223  █▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁ |
| `STATUS_1` | cat | 100% | 6 | REGISTERED 37%, CDP 26%, DRAFT APPROVED 20%, PENDING 13%, NO PLAN 2%, SP PROCESS INITIATED 2% |
| `Shape__Area` | num | 100% | 180 | 1,248 · p25 39,327 · p50 142,184 · p95 1,267,359 · max 17,044,501  █▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁ |
| `Shape__Length` | num | 100% | 180 | 156 · p25 1,144 · p50 2,193 · p95 6,959 · max 22,837  █▅▄▂▂▁▁▁▁▁▁▁▁▁▁▁ |

## Candidate questions

- (none templated)

_profiled 2026-09-09 · `python3 tools/profile.py open_greenfield_residential_land_survey`_
