# Screenlines

`open_screenlines` · shape **arcgis-hub** · source `open-ottawa`

- origin: <https://open.ottawa.ca/datasets/ottawa::screenlines>
- fetched 2026-09-09 · **39 rows** · 21 columns
- csv · licence: https://ottawa.ca/en/city-hall/open-transparent-and-accountable-government/open-

## Columns

| column | kind | non-null | distinct | summary |
| --- | --- | --- | --- | --- |
| `OBJECTID` | num | 100% | 39 | 1.00 · p25 10.50 · p50 20.00 · p95 37.10 · max 39.00  █▅█▅▅█▅█▅▅█▅▅█▅█ |
| `SL_NUM` | num | 100% | 39 | 2.00 · p25 13.50 · p50 30.00 · p95 54.10 · max 56.00  ▆▄█▄▂▄▄▆▆▄▆▂▄▆▄█ |
| `SL_TEXT` | id/text | 100% | 39 | e.g. SL16, SL55, SL20 |
| `CORDON_EN` | cat | 100% | 11 | Greenbelt 15%, Inner Area 15%, Outside Greenbelt 1 - We 13%, Central District 10%, Along Woodroffe 8%, Along CNR 8% |
| `CORDON_FR` | cat | 100% | 11 | Ceinture de verdure 15%, Secteur intérieur 15%, Extérieur de la Ceinture 13%, District centre 10%, Le long de Woodroffe 8%, Le long de la ligne du C 8% |
| `NAME_EN` | id/text | 100% | 39 | e.g. East Greenbelt (Innes , East of Hawthorne (Hwy, Rideau River (Hunt Clu |
| `NAME_FR` | id/text | 100% | 39 | e.g. Ceinture de verdure es, Est de Hawthorne (de l, Rivière Rideau (de Hun |
| `SEASON_EN` | cat | 100% | 2 | Spring 51%, Fall 49% |
| `SEASON_FR` | cat | 100% | 2 | Printemps 51%, Automne 49% |
| `COUNTYEAR_EN` | cat | 100% | 3 | Both 59%, Even 21%, Odd 21% |
| `COUNTYEAR_FR` | cat | 100% | 3 | Les deux 59%, Paires 21%, Impaires 21% |
| `CHANGE_EN` | text | 100% | 27 | e.g.  , Adjusted shape to avoi, Shorten east end of sc |
| `CHANGE_FR` | id/text | 66% | 26 | e.g. Forme modifiée pour év, Extrémité est de la li, Forme modifiée de la l |
| `YEAR` | num | 100% | 1 | 2,025 · p25 2,025 · p50 2,025 · p95 2,025 · max 2,025   |
| `STATUS_EN` | cat | 100% | 1 | Latest 100% |
| `STATUS_FR` | cat | 100% | 1 | Dernier en date 100% |
| `UNIQUE_ID` | num | 100% | 39 | 1.00 · p25 10.50 · p50 20.00 · p95 37.10 · max 39.00  █▅█▅▅█▅█▅▅█▅▅█▅█ |
| `GLOBALID` | id/text | 100% | 39 | e.g. {16FDC766-9CED-40EC-8B, {22049F6D-D4F8-4190-B6, {61B9C508-1E4E-43FE-95 |
| `CREATED_DATE` | date | 100% | 1 | 2026-06-23 → 2026-06-23 |
| `LAST_EDITED_DATE` | date | 100% | 1 | 2026-06-23 → 2026-06-23 |
| `SHAPE_Length` | num | 100% | 39 | 226 · p25 3,354 · p50 6,718 · p95 18,928 · max 21,737  ▅▆▄▆▄▂▂▂▄█▃▂▁▃▂▂ |

## Candidate questions

- (none templated)

_profiled 2026-09-09 · `python3 tools/profile.py open_screenlines`_
