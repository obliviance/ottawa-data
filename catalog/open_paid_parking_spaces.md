# Paid Parking Spaces

`open_paid_parking_spaces` · shape **arcgis-hub** · source `open-ottawa` · **spatial**

- origin: <https://open.ottawa.ca/datasets/ottawa::paid-parking-spaces>
- fetched 2026-09-09 · **1,095 rows** · 35 columns
- geojson · licence: https://ottawa.ca/en/city-hall/get-know-your-city/open-data#open-data-licence-ve

## Columns

| column | kind | non-null | distinct | summary |
| --- | --- | --- | --- | --- |
| `OBJECTID` | num | 100% | 1,095 | 940 · p25 3,840 · p50 4,161 · p95 9,128 · max 9,184  ▁▁▁▁▁█▆▁▁▁▁▁▁▁▁▄ |
| `ANGLED` | cat | 99% | 2 | N 95%, Y 5% |
| `IN_USE` | cat | 100% | 2 | a 96%, b 4% |
| `GLOBALID` | id/text | 100% | 1,095 | e.g. {114A8231-BB75-4F32-B2, {7ED595ED-6680-441C-BD, {E3C7B100-81D7-4917-8E |
| `SHAPE_Length` | num | 100% | 1,095 | 4.98 · p25 15.27 · p50 25.52 · p95 81.66 · max 221  █▅▄▂▂▁▁▁▁▁▁▁▁▁▁▁ |
| `ROAD` | text | 100% | 120 | e.g. SOMERSET, CUMBERLAND, DANIEL MCCANN |
| `SIDE` | cat | 100% | 6 | N 36%, S 31%, E 16%, W 15%, OFF 1%, MED 1% |
| `TYPE_OF_SPACE` | cat | 100% | 1 | PAID 100% |
| `ZONE` | num | 100% | 25 | 1.00 · p25 13.00 · p50 14.00 · p95 24.00 · max 25.00  ▂▂▁▂▂▄▁▆█▆▄▃▁▂▁▄ |
| `PARKING_SUPPLY` | num | 100% | 21 | 1.00 · p25 2.00 · p50 3.00 · p95 10.00 · max 26.00  █▅▂▂▁▁▁▁▁▁▁▁▁▁▁▁ |
| `OUT_OF_SERVICE` | num | 99% | 14 | 0.00 · p25 0.00 · p50 0.00 · p95 1.00 · max 15.00  █▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁ |
| `AVAILABLE_SPACES` | num | 100% | 23 | 0.00 · p25 1.00 · p50 3.00 · p95 9.30 · max 26.00  ▆█▃▃▂▁▁▁▁▁▁▁▁▁▁▁ |
| `BLOCKFACE_SUPPLY` | num | 100% | 35 | 1.00 · p25 6.00 · p50 10.00 · p95 29.00 · max 61.00  ▆▇█▅▃▁▁▁▁▁▁▁▁▁▁▁ |
| `RATE_STRUCTURE` | num | 100% | 44 | 7.00 · p25 69.00 · p50 81.00 · p95 99.80 · max 108  ▁▁▁▁▁▁▁▁▁█▃▄▂▄▄▂ |
| `DAYS_IN_EFFECT` | num | 100% | 3 | 5.00 · p25 5.00 · p50 5.00 · p95 6.00 · max 7.00  █▁▁▁▁▁▁▇▁▁▁▁▁▁▁▁ |
| `MAX_STAY` | num | 100% | 3 | 1.00 · p25 2.00 · p50 2.00 · p95 2.30 · max 3.00  ▁▁▁▁▁▁▁█▁▁▁▁▁▁▁▁ |
| `RATE` | num | 100% | 6 | 5.00 · p25 5.00 · p50 15.00 · p95 418 · max 418  █▁▁▁▁▁▁▁▁▁▁▁▁▄▁▃ |
| `HOURLY_RATE` | num | 100% | 6 | 1.00 · p25 3.00 · p50 3.00 · p95 4.00 · max 4.50  ▁▁▁▁▁▁▁▁▁█▁▄▁▅▁▁ |
| `MODIFIED_DATE` | date | 100% | 43 | 2026-03-04 → 2026-05-26 |
| `CREATED_DATE` | date | 100% | 125 | 2024-11-28 → 2026-03-27, 4 gaps >30d |
| `CREATED_BY` | cat | 100% | 1 | PALMERCOD 100% |
| `MODIFIED_BY` | cat | 100% | 1 | PALMERCOD 100% |
| `IN_USE_FR` | cat | 100% | 2 | a 96%, b 4% |
| `ANGLED_FR` | cat | 100% | 2 | N 95%, O 5% |
| `TYPE_OF_SPACE_FR` | cat | 100% | 1 | PAYANT 100% |
| `ZONE_FR` | num | 100% | 25 | 1.00 · p25 13.00 · p50 14.00 · p95 24.00 · max 25.00  ▂▂▁▂▂▄▁▆█▆▄▃▁▂▁▄ |
| `SIDE_FR` | cat | 100% | 6 | N 36%, S 31%, E 16%, O 15%, Côté 1%, MÉD 1% |
| `RATE_STRUCTURE_FR` | num | 100% | 44 | 7.00 · p25 69.00 · p50 81.00 · p95 99.80 · max 108  ▁▁▁▁▁▁▁▁▁█▃▄▂▄▄▂ |
| `DAYS_IN_EFFECT_FR` | num | 100% | 3 | 5.00 · p25 5.00 · p50 5.00 · p95 6.00 · max 7.00  █▁▁▁▁▁▁▇▁▁▁▁▁▁▁▁ |
| `MAX_STAY_FR` | num | 100% | 3 | 1.00 · p25 2.00 · p50 2.00 · p95 2.30 · max 3.00  ▁▁▁▁▁▁▁█▁▁▁▁▁▁▁▁ |
| `RATE_FR` | num | 100% | 6 | 5.00 · p25 5.00 · p50 15.00 · p95 418 · max 418  █▁▁▁▁▁▁▁▁▁▁▁▁▄▁▃ |
| `HOURLY_RATE_FR` | num | 100% | 6 | 1.00 · p25 3.00 · p50 3.00 · p95 4.00 · max 4.50  ▁▁▁▁▁▁▁▁▁█▁▄▁▅▁▁ |
| `FROM1` | text | 95% | 178 | e.g. EMPRESS, UPPER LORNE, BOOTH |
| `TO1` | text | 95% | 190 | e.g. UPPER LORNE, BOOTH, LEBRETON |
| `geometry` | id/text | 100% | 1,095 | e.g. {"type": "LineString",, {"type": "LineString",, {"type": "LineString", |

## Candidate questions

- Trend / seasonality of open_paid_parking_spaces over `MODIFIED_DATE`; structural breaks?
- Spatial clustering of open_paid_parking_spaces; overlay wards + the decision timeline

_profiled 2026-09-09 · `python3 tools/profile.py open_paid_parking_spaces`_
