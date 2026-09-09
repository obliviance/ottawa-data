# Ottawa Neighbourhood Equity Index (NEI) 2024

`open_ottawa_neighbourhood_equity_index_nei_2024` · shape **arcgis-hub** · source `open-ottawa`

- origin: <https://open.ottawa.ca/datasets/ottawa::ottawa-neighbourhood-equity-index-nei-2024>
- fetched 2026-09-09 · **218 rows** · 23 columns
- csv · licence: https://ottawa.ca/en/city-hall/open-transparent-and-accountable-government/open-

## Columns

| column | kind | non-null | distinct | summary |
| --- | --- | --- | --- | --- |
| `OBJECTID` | num | 100% | 218 | 1.00 · p25 55.25 · p50 110 · p95 207 · max 218  ██▇█▇█▇██▇█▇█▇██ |
| `CTID` | num | 100% | 218 | 5,050,001 · p25 5,050,037 · p50 5,050,125 · p95 5,050,174 · max 5,050,302  ▆▄▄▁▁▁▆█▅▂▂▁▁▁▁▁ |
| `ISURBAN` | cat | 100% | 2 | Urban 93%, Rural 7% |
| `URB_RURAL` | cat | 100% | 6 | Urban 55%, Suburban 36%, Rural 7%, Rural-Greenbelt 1%, Greenbelt-Rural 0%, Greenbelt 0% |
| `URB_RUR_FR` | cat | 100% | 5 | Urbain 55%, Suburbain 36%, Secteur rural 7%, Rural-Greenbelt 1%, Ceinture de verdure 0% |
| `CTNAME_EN` | id/text | 100% | 218 | e.g. Riverside Park, Clementine, Billings Bridge |
| `CTNAME_FR` | id/text | 100% | 218 | e.g. Riverside Park, Clementine, Billings Bridge |
| `SZDNEI` | num | 100% | 218 | 0.00 · p25 0.23 · p50 0.28 · p95 0.48 · max 0.62  ▁▁▁▂▂▅█▆▅▃▂▂▁▁▁▁ |
| `SCORENEI` | num | 100% | 218 | 0.00 · p25 65.52 · p50 72.23 · p95 83.68 · max 88.16  ▁▁▁▁▁▁▁▁▁▁▂▃▅█▄▂ |
| `R_NEI` | num | 100% | 18 | 0.00 · p25 3.00 · p50 4.00 · p95 14.00 · max 18.00  ▅▆█▆▅▄▄▅▃▂▁▁▂▁▁▁ |
| `Y_NEI` | num | 100% | 15 | 0.00 · p25 4.25 · p50 6.50 · p95 11.00 · max 14.00  ▁▂▂▆▅▇▇▅▁█▅▅▃▂▁▁ |
| `LG_NEI` | num | 100% | 16 | 0.00 · p25 6.00 · p50 8.00 · p95 14.00 · max 15.00  ▁▁▂▂▂▆▆▆█▄▅▄▃▂▃▁ |
| `G_NEI` | num | 100% | 17 | 0.00 · p25 4.00 · p50 6.00 · p95 14.00 · max 16.00  ▄▄▆█▄▇▄▃▄▃▄▁▂▃▁▁ |
| `RED_GREEN` | cat | 100% | 9 | Urb_Yellow 23%, Urb_Red 23%, Urb_Green 23%, Urb_Light_Green 23%, Rur_Red 2%, Rur_Yellow 2% |
| `LEGEND_EN` | cat | 100% | 9 | Urb_Possible equity conc 23%, Urb_No equity concern 23%, Urb_Strong equity concer 23%, Urb_Nominal equity conce 22%, Rur_Strong equity concer 2%, Rur_Possible equity conc 2% |
| `LEGEND_FR` | cat | 100% | 9 | Urb_Préoccupation possib 23%, Urb_Grande préoccupation 23%, Urb_Aucune préoccupation 23%, Urb_Préoccupation minime 23%, Rur_Grande préoccupation 2%, Rur_Préoccupation possib 2% |
| `NAME_EN` | cat | 100% | 1 | Ottawa Neighbourhood Equ 100% |
| `NAME_FR` | cat | 100% | 1 | Indice de l’équité des q 100% |
| `GLOBALID` | id/text | 100% | 218 | e.g. {83B4AE6F-3B76-493D-A9, {A04EFACE-D7E7-41F8-92, {EC48A0AC-CE8F-4CBE-9C |
| `CREATED_DATE` | text | 0% | 0 | e.g.  |
| `LAST_EDITED_DATE` | text | 0% | 0 | e.g.  |
| `SHAPE_Length` | num | 100% | 218 | 2,732 · p25 6,697 · p50 8,795 · p95 72,316 · max 119,170  █▃▁▁▁▁▁▁▁▁▁▁▁▁▁▁ |
| `SHAPE_Area` | num | 100% | 218 | 400,547 · p25 2,163,138 · p50 3,435,430 · p95 227,722,659 · max 551,899,412  █▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁ |

## Candidate questions

- (none templated)

_profiled 2026-09-09 · `python3 tools/profile.py open_ottawa_neighbourhood_equity_index_nei_2024`_
