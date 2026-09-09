# Pay and Display Machines

`open_pay_and_display_machines` · shape **arcgis-hub** · source `open-ottawa`

- origin: <https://open.ottawa.ca/datasets/ottawa::pay-and-display-machines>
- fetched 2026-09-09 · **669 rows** · 31 columns
- csv · licence: https://ottawa.ca/en/city-hall/get-know-your-city/open-data#open-data-licence-ve

## Columns

| column | kind | non-null | distinct | summary |
| --- | --- | --- | --- | --- |
| `OBJECTID` | num | 100% | 669 | 11,260 · p25 11,467 · p50 11,687 · p95 12,069 · max 12,102  ▆▆▆▆▆▆▆▆▆▅▅▆▆▅██ |
| `VENDORLOT` | num | 100% | 669 | 1,092 · p25 2,062 · p50 2,907 · p95 4,774 · max 5,371  ▆▁▃▅▁▄█▃▄▃▁▁▇▂▂▁ |
| `PRECISE_ID` | num | 82% | 548 | 3.00 · p25 8,411 · p50 8,665 · p95 9,239 · max 9,944  ▁▁▁▁▁▁▁▁▁▁▁▁▃▇█▁ |
| `GROUP_ID` | text | 83% | 398 | e.g. FRIEL_E_RIDEA-DEADEND, CONST_E_CENTR-BASEL, GEORG_S_SUSSE-DALHO |
| `X` | num | 85% | 572 | -75.83 · p25 -75.70 · p50 -75.69 · p95 -75.67 · max 369,848  █▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁ |
| `Y` | num | 85% | 572 | 45.34 · p25 45.41 · p50 45.42 · p95 45.43 · max 5,032,884  █▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁ |
| `NEW_ID` | num | 85% | 568 | 75,371 · p25 83,984,376 · p50 86,581,167 · p95 92,387,454 · max 99,442,747  ▁▁▁▁▁▁▁▁▁▁▁▁▃▇█▁ |
| `WARD` | num | 84% | 7 | 7.00 · p25 14.00 · p50 14.00 · p95 17.00 · max 18.00  ▁▁▁▁▁▁▁▃▁▁█▁▁▁▂▁ |
| `STATUS` | cat | 100% | 4 | a 94%, b 3%, d 3%, c 0% |
| `NOTES` | text | 79% | 39 | e.g. Corrected, 8:30am - 7:30pm MON-FR, 8:30-7:30 MON-FRI; 10- |
| `RATE_DESC` | text | 100% | 62 | e.g. $0.25/15 min, Monday /, $0.25/5 min, Monday / , $0.25/3 min 45s, Monda |
| `LOCATE_DESC` | id/text | 83% | 496 | e.g. 240 Friel St. (N. Ride, 2-100 CONSTELLATION DR, 98 GEORGE |
| `DAYS` | num | 100% | 3 | 5.00 · p25 5.00 · p50 6.00 · p95 6.00 · max 7.00  ▇▁▁▁▁▁▁█▁▁▁▁▁▁▁▁ |
| `MON_FRI_HOURS` | cat | 100% | 16 | 830-530 57%, 830-730 20%, 9-330 8%, 8-530 3%, O 3%, 9-530 3% |
| `SAT_HOURS` | cat | 53% | 9 | 10-530 57%, 10-730 32%, O 3%, 7-7 2%, 830-530 2%, 830-730 1% |
| `MON_FRI_HR` | num | 100% | 7 | 1.00 · p25 3.00 · p50 3.00 · p95 4.00 · max 4.00  ▁▁▁▁▁▁▁▁▁▁█▁▁▄▁▅ |
| `SAT_HR` | num | 53% | 6 | 1.50 · p25 3.00 · p50 3.50 · p95 4.00 · max 4.00  ▁▁▁▁▁▁▁▁▁█▁▁▂▁▁▇ |
| `SUN_HR` | num | 3% | 6 | 1.50 · p25 3.00 · p50 3.00 · p95 3.53 · max 4.00  ▁▁▁▂▁▁▁▁▁█▁▁▅▁▁▁ |
| `MON_FRI_MR` | num | 100% | 7 | 5.00 · p25 5.00 · p50 15.00 · p95 418 · max 730  █▁▁▁▁▁▁▄▁▃▁▁▁▁▁▁ |
| `SAT_MR` | num | 53% | 10 | 5.00 · p25 5.00 · p50 345 · p95 418 · max 730  █▁▁▁▁▁▁▇▁▂▁▁▁▁▁▁ |
| `SUN_MR` | cat | 3% | 7 | 5 39%, n 26%, 730 9%,   9%, 15 9%, 10 4% |
| `HOLIDAY` | cat | 0% | 2 | $0.25/6 min 50%, $2.00 50% |
| `BIA` | text | 0% | 0 | e.g.  |
| `OPP_AREA` | text | 81% | 70 | e.g. 13-2, 1-1, 12-1 |
| `SUN_HOURS` | cat | 0% | 2 | O 83%, 830-530 17% |
| `GLOBALID` | id/text | 100% | 669 | e.g. {005739F3-652E-4488-80, {00992BAA-611B-4B90-99, {00B2D091-B948-4877-BE |
| `CREATED_DATE` | date | 100% | 33 | 2022-08-10 → 2026-04-17, 4 gaps >30d |
| `MODIFIED_DATE` | date | 100% | 85 | 2025-10-29 → 2026-04-28, 2 gaps >30d |
| `ZONES` | num | 99% | 25 | 1.00 · p25 12.00 · p50 14.00 · p95 24.00 · max 25.00  ▂▂▁▂▂▃▃▇█▇▅▄▂▃▂▅ |
| `BLOCKFACE` | text | 96% | 483 | e.g. FRIEL_E_RIDEA-DEADEND, CONST_E_CENTR-BASEL, GEORG_S_SUSSE-DALHO |
| `Details` | text | 58% | 39 | e.g. On-street # 102, On-street # 73, On-street # 76 |

## Candidate questions

- `VENDORLOT` by `WARD` — equity gradient? (join ONS income)
- Trend / seasonality of open_pay_and_display_machines over `CREATED_DATE`; structural breaks?

_profiled 2026-09-09 · `python3 tools/profile.py open_pay_and_display_machines`_
