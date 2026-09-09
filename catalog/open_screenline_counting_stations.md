# Screenline Counting Stations

`open_screenline_counting_stations` · shape **arcgis-hub** · source `open-ottawa` · **spatial**

- origin: <https://open.ottawa.ca/datasets/ottawa::screenline-counting-stations>
- fetched 2026-09-09 · **324 rows** · 40 columns
- geojson · licence: https://ottawa.ca/en/city-hall/open-transparent-and-accountable-government/open-

## Columns

| column | kind | non-null | distinct | summary |
| --- | --- | --- | --- | --- |
| `OBJECTID` | num | 100% | 324 | 1.00 · p25 81.75 · p50 162 · p95 308 · max 324  █▇▇▇▇█▇▇▇▇█▇▇▇▇█ |
| `SL_NUM` | num | 100% | 39 | 2.00 · p25 24.00 · p50 35.00 · p95 53.00 · max 56.00  ▁▂▆▂▂▂▄▃▅▃█▁▆▆▃▄ |
| `STATION_ID` | num | 100% | 324 | 802 · p25 7,904 · p50 50,024 · p95 51,834 · max 99,506  ▄▃▁▁▁▁▁▃█▁▁▁▁▁▁▁ |
| `CORDON_EN` | cat | 100% | 11 | Central District 17%, Outside Greenbelt 1 - We 15%, Outside Greenbelt 1 - Ea 12%, Greenbelt 12%, Along Woodroffe 10%, Inner Area 10% |
| `CORDON_FR` | cat | 100% | 11 | District centre 17%, Extérieur de la Ceinture 15%, Extérieur de la Ceinture 12%, Ceinture de verdure 12%, Le long de Woodroffe 10%, Secteur intérieur 10% |
| `NAME_EN` | id/text | 100% | 324 | e.g. CUMMINGS BRIDGE, ST. PATRICK STREET BRI, ADÀWE CROSSING |
| `NAME_FR` | id/text | 100% | 324 | e.g. PONT CUMMINGS, PONT DE LA RUE ST-PATR, PASSERELLE ADÀWE |
| `NAME_TEXT1_EN` | text | 100% | 172 | e.g. CUMMINGS, ST PATRICK ST, BICYCLE |
| `NAME_TEXT1_FR` | text | 100% | 174 | e.g. CUMMINGS, RUE ST-PATRICK, VÉLOS |
| `NAME_TEXT2_EN` | text | 100% | 32 | e.g. BRIDGE, ST, PATH |
| `NAME_TEXT2_FR` | text | 100% | 30 | e.g. PONT, RUE, SENTIER |
| `SEASON_EN` | cat | 100% | 2 | Spring 66%, Fall 34% |
| `SEASON_FR` | cat | 100% | 2 | Printemps 66%, Automne 34% |
| `DURATION` | num | 100% | 3 | 0.00 · p25 13.00 · p50 13.00 · p95 13.00 · max 13.00  ▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁█ |
| `COUNTYEAR_EN` | cat | 100% | 3 | Both 51%, Even 30%, Odd 19% |
| `COUNTYEAR_FR` | cat | 100% | 3 | Les deux 51%, Paires 30%, Impaires 19% |
| `STATION_TYPE_EN` | cat | 100% | 7 | All Modes 67%, Path Major 14%, Path Minor 12%, LRT 4%, Future 2%, Decommissioned 1% |
| `STATION_TYPE_FR` | cat | 100% | 7 | Tous les modes 67%, Sentier majeur 14%, Sentier mineur 12%, TLR 4%, Futur 2%, Mis hors service 1% |
| `NEWYEAR_EN` | cat | 100% | 2 | Pre-2025 72%, 2025 28% |
| `NEWYEAR_FR` | cat | 100% | 2 | Avant 2025 72%, 2025 28% |
| `CHANGE_EN` | text | 100% | 137 | e.g.  , New station for Adawe , New station on bridge  |
| `CHANGE_FR` | id/text | 47% | 133 | e.g. Nouveau poste de compt, Nouveau poste de compt, Poste de comptage dépl |
| `FLOW_EN` | cat | 100% | 2 | False 98%, True 2% |
| `FLOW_FR` | cat | 100% | 2 | Faux 98%, Vrai 2% |
| `LOCAL_EN` | cat | 100% | 2 | False 96%, True 4% |
| `LOCAL_FR` | cat | 100% | 2 | Faux 96%, Vrai 4% |
| `DECOM_EN` | cat | 100% | 2 | False 99%, True 1% |
| `DECOM_FR` | cat | 100% | 2 | Faux 99%, Vrai 1% |
| `FUTURE_EN` | cat | 100% | 2 | False 99%, True 1% |
| `FUTURE_FR` | cat | 100% | 2 | Faux 99%, Vrai 1% |
| `YEAR` | num | 100% | 1 | 2,025 · p25 2,025 · p50 2,025 · p95 2,025 · max 2,025   |
| `STATUS_EN` | cat | 100% | 1 | Latest 100% |
| `STATUS_FR` | cat | 100% | 1 | Dernier en date 100% |
| `UNIQUE_ID` | num | 100% | 324 | 1.00 · p25 81.75 · p50 162 · p95 308 · max 324  █▇▇▇▇█▇▇▇▇█▇▇▇▇█ |
| `GLOBALID` | id/text | 100% | 324 | e.g. {8CB9D2DB-33B3-44F8-BE, {5D7F23C2-EA94-49D4-88, {7393D564-C723-4244-A3 |
| `CREATED_DATE` | date | 100% | 1 | 2026-06-23 → 2026-06-23 |
| `LAST_EDITED_DATE` | date | 100% | 1 | 2026-06-23 → 2026-06-23 |
| `geometry` | id/text | 100% | 324 | e.g. {"type": "Point", "coo, {"type": "Point", "coo, {"type": "Point", "coo |
| `longitude` | num | 100% | 324 | -75.94 · p25 -75.75 · p50 -75.69 · p95 -75.49 · max -75.44  ▁▂▂▂▁▃▂█▆▁▂▂▁▂▂▁ |
| `latitude` | num | 100% | 324 | 45.23 · p25 45.33 · p50 45.40 · p95 45.47 · max 45.51  ▁▂▃▂▂▃▃▂▂▄█▄▂▃▁▁ |

## Candidate questions

- Spatial clustering of open_screenline_counting_stations; overlay wards + the decision timeline

_profiled 2026-09-09 · `python3 tools/profile.py open_screenline_counting_stations`_
