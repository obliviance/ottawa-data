# 2026 Municipal Elections – Voting Places

`open_2026_municipal_elections_voting_places` · shape **arcgis-hub** · source `open-ottawa`

- origin: <https://open.ottawa.ca/datasets/ottawa::2026-municipal-elections-voting-places>
- fetched 2026-09-09 · **639 rows** · 13 columns
- csv · licence: https://ottawa.ca/en/city-hall/open-transparent-and-accountable-government/open-

## Columns

| column | kind | non-null | distinct | summary |
| --- | --- | --- | --- | --- |
| `FID` | num | 100% | 639 | 1.00 · p25 160 · p50 320 · p95 607 · max 639  ████████▇███████ |
| `Ward` | num | 100% | 25 | 1.00 · p25 7.00 · p50 13.00 · p95 99.00 · max 99.00  ▇█▇▄▁▁▁▁▁▁▁▁▁▁▁▂ |
| `Day` | cat | 100% | 6 | Voting Day 58%, Adv Day 36%, Special Adv 1 2%, Special Adv 2 2%, Special Adv 3 2%, Special Adv 4 2% |
| `Area` | num | 100% | 29 | 1.00 · p25 4.00 · p50 7.00 · p95 19.00 · max 29.00  █▇▆▆▃▅▄▃▁▂▁▁▁▁▁▁ |
| `Name` | id/text | 100% | 550 | e.g. Sarsfield Community Ha, École élémentaire publ, Collège catholique Mer |
| `Address` | id/text | 100% | 549 | e.g. 3585 Sarsfield Rd, 6025 Longleaf Dr, 6401 Renaud Rd |
| `City` | cat | 100% | 1 | Ottawa 100% |
| `Intersect_` | id/text | 100% | 516 | e.g. ch. Colonial & ch. Sar, prom. Longleaf & boul., ch. Renaud & rue Fern  |
| `Acc_Entr` | text | 100% | 80 | e.g. Main Entrance, Side Entrance, Side door |
| `Hours` | cat | 100% | 3 | 10 am to 8 pm 88%, 10 am to 2 pm 6%, 4 pm to 8 pm 6% |
| `Postal` | text | 100% | 511 | e.g. K0A3E0, K1W1J2, K1W0H8 |
| `X` | num | 100% | 530 | 0.00 · p25 361,826 · p50 367,943 · p95 385,287 · max 395,360  ▁▁▁▁▁▁▁▁▁▁▁▁▁▁█▄ |
| `Y` | num | 100% | 530 | 0.00 · p25 5,020,712 · p50 5,026,443 · p95 5,037,251 · max 5,042,314  ▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁█ |

## Candidate questions

- `Ward` by `Ward` — equity gradient? (join ONS income)

_profiled 2026-09-09 · `python3 tools/profile.py open_2026_municipal_elections_voting_places`_
