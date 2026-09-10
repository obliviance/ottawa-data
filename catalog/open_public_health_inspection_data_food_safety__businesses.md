# Public Health Inspection Data - Food Safety — businesses.csv

`open_public_health_inspection_data_food_safety__businesses` · shape **arcgis-hub** · source `ottawa-public-health` · **spatial**

- origin: <https://open.ottawa.ca/documents/ottawa::public-health-inspection-data-food-safety-1>
- fetched 2026-09-09 · **12,932 rows** · 9 columns
- from zip · licence: https://ottawa.ca/en/city-hall/get-know-your-city/open-data#open-data-licence-ve

## Columns

| column | kind | non-null | distinct | summary |
| --- | --- | --- | --- | --- |
| `business_id` | id/text | 100% | 12,932 | e.g. 95E50BB8-7019-4533-988, D0A8CB6F-0AD0-4B48-80F, 56E53B20-197F-4933-AA0 |
| `name` | text | 100% | 9,740 | e.g. BABAR WINE + EATS, MOJO FRESH, PURE APOTHECARY |
| `address` | text | 100% | 7,908 | e.g. 826 Somerset St W, 1261 STITTSVILLE MAIN , 989 Wellington St. W |
| `city` | text | 98% | 91 | e.g. Ottawa, OTTAWA, OTTAWA ONT |
| `state` | cat | 100% | 1 | ON 100% |
| `postal_code` | text | 96% | 3,582 | e.g. K1R 6R5, K2S 2E4, K1Y 2Y1 |
| `latitude` | num | 99% | 7,336 | 0.00 · p25 45.35 · p50 45.40 · p95 45.46 · max 161  ▁▁▁▁█▁▁▁▁▁▁▁▁▁▁▁ |
| `longitude` | num | 99% | 7,355 | -551 · p25 -75.74 · p50 -75.69 · p95 -75.50 · max 75.42  ▁▁▁▁▁▁▁▁▁▁▁▁█▁▁▁ |
| `phone_number` | num | 81% | 8,586 | 1.00 · p25 16,132,880,223 · p50 16,136,956,333 · p95 16,138,981,714 · max 161,388,276,496,131,227,648  █▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁ |

## Candidate questions

- Spatial clustering of open_public_health_inspection_data_food_safety__businesses; overlay wards + the decision timeline

_profiled 2026-09-09 · `python3 tools/profile.py open_public_health_inspection_data_food_safety__businesses`_
