# Ottawa Neighbourhood Equity Index (NEI) 2019

`open_ottawa_neighbourhood_equity_index_nei_2019` · shape **arcgis-hub** · source `open-ottawa`

- origin: <https://open.ottawa.ca/datasets/ottawa::ottawa-neighbourhood-equity-index-nei-2019>
- fetched 2026-09-09 · **196 rows** · 27 columns
- csv · licence: https://ottawa.ca/en/city-hall/get-know-your-city/open-data#open-data-licence-ve

## Columns

| column | kind | non-null | distinct | summary |
| --- | --- | --- | --- | --- |
| `FID` | num | 100% | 196 | 1.00 · p25 49.75 · p50 98.50 · p95 186 · max 196  █▇▇▇▇█▇▇▇▇█▇▇▇▇█ |
| `OBJECTID` | num | 100% | 196 | 1.00 · p25 49.75 · p50 98.50 · p95 186 · max 196  █▇▇▇▇█▇▇▇▇█▇▇▇▇█ |
| `CTID` | num | 100% | 196 | 5,050,001 · p25 5,050,033 · p50 5,050,124 · p95 5,050,176 · max 5,050,302  ▇▅▄▂▁▂▇█▅▂▂▁▁▁▁▁ |
| `URB_RURAL` | cat | 100% | 6 | Urban 58%, Suburban 32%, Rural 8%, Rural-Greenbelt 1%, Greenbelt 1%, Greenbelt-Rural 1% |
| `URB_RURAL_` | cat | 100% | 6 | Urbain 58%, Suburbain 32%, Secteur rural 8%, Secteur rural – Ceinture 1%, Ceinture de verdure 1%, Ceinture de verdure – Se 1% |
| `CTNAME` | id/text | 100% | 196 | e.g. Britannia Woods - Mich, Britannia Village - Ev, Lincoln Heights - McEw |
| `CTNAME_FR` | id/text | 100% | 196 | e.g. Britannia Woods - Mich, Britannia Village - Ev, Lincoln Heights - McEw |
| `SZDNEI` | num | 100% | 138 | 0.00 · p25 0.27 · p50 0.30 · p95 0.48 · max 0.63  ▁▁▁▁▁▂▆█▆▄▂▂▁▁▁▁ |
| `SCORENEI` | num | 100% | 138 | 0.00 · p25 64.38 · p50 69.50 · p95 78.45 · max 85.90  ▁▁▁▁▁▁▁▁▁▁▂▃▆█▂▁ |
| `R_NEI` | num | 100% | 19 | 0.00 · p25 3.00 · p50 5.00 · p95 14.25 · max 18.00  ▃▆▇▇▇▃▄█▂▃▁▂▂▁▁▂ |
| `Y_NEI` | num | 100% | 16 | 0.00 · p25 5.00 · p50 7.00 · p95 13.00 · max 16.00  ▃▄▃▅▆▇█▇▆▆▂▂▂▁▁▁ |
| `LG_NEI` | num | 100% | 14 | 0.00 · p25 5.00 · p50 7.00 · p95 11.00 · max 14.00  ▁▁▂▄▄▅▆▇▁█▄▃▂▁▁▁ |
| `G_NEI` | num | 100% | 18 | 0.00 · p25 5.00 · p50 8.00 · p95 14.00 · max 18.00  ▁▁▃▅▄▃▇█▄▄▂▃▂▁▁▁ |
| `RED_GREEN` | cat | 100% | 5 | Red 25%, Yellow 25%, Light Green 25%, Green 24%, No data 1% |
| `GLOBALID` | id/text | 100% | 196 | e.g. {4F001D54-3F52-44AF-8F, {5661A542-C71B-4800-87, {430986DA-93E6-41A2-87 |
| `CREATED_DA` | cat | 100% | 1 |   100% |
| `LAST_EDITE` | cat | 100% | 1 | 2021/02/03 00:00:00+00 100% |
| `LEGEND_EN` | cat | 100% | 5 | Strong equity concern 25%, Possible equity concern 25%, Nominal equity concern 25%, No equity concern 24%, No data 1% |
| `LEGEND_FR` | cat | 100% | 5 | Grande préoccupation en  25%, Préoccupation possible e 25%, Préoccupation minime en  25%, Aucune préoccupation en  24%, Aucune donnée 1% |
| `NAME_EN` | cat | 100% | 1 | Neighbourhood Equity Ind 100% |
| `NAME_FR` | cat | 100% | 1 | Indice de l’équité des q 100% |
| `DESCRIPTIO` | cat | 100% | 1 |   100% |
| `DESCRIPT_1` | cat | 100% | 1 |   100% |
| `SHAPE_Leng` | num | 100% | 196 | 3,425 · p25 6,736 · p50 8,610 · p95 77,902 · max 154,238  █▂▁▁▁▁▁▁▁▁▁▁▁▁▁▁ |
| `SHAPE_Area` | num | 100% | 196 | 634,394 · p25 2,113,892 · p50 3,322,053 · p95 224,922,662 · max 528,432,748  █▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁ |
| `Shape__Area` | num | 100% | 196 | 634,394 · p25 2,113,892 · p50 3,322,053 · p95 224,922,662 · max 528,432,748  █▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁ |
| `Shape__Length` | num | 100% | 196 | 3,425 · p25 6,736 · p50 8,610 · p95 77,902 · max 154,238  █▂▁▁▁▁▁▁▁▁▁▁▁▁▁▁ |

## Candidate questions

- (none templated)

_profiled 2026-09-09 · `python3 tools/profile.py open_ottawa_neighbourhood_equity_index_nei_2019`_
