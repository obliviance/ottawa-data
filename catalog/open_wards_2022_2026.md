# Wards 2022-2026

`open_wards_2022_2026` · shape **arcgis-hub** · source `open-ottawa` · **spatial**

- origin: <https://open.ottawa.ca/datasets/ottawa::wards-2022-2026>
- fetched 2026-09-09 · **24 rows** · 15 columns
- geojson · licence: https://ottawa.ca/en/city-hall/get-know-your-city/open-data#open-data-licence-ve

## Columns

| column | kind | non-null | distinct | summary |
| --- | --- | --- | --- | --- |
| `FID` | num | 100% | 24 | 1.00 · p25 6.75 · p50 12.50 · p95 22.85 · max 24.00  █▄█▄█▄█▄▄█▄█▄█▄█ |
| `NAME` | cat | 100% | 24 | Somerset 4%, Kanata South 4%, Kanata North 4%, Capital 4%, Kitchissippi 4%, Rideau-Rockcliffe 4% |
| `NAME_FR` | cat | 100% | 24 | Somerset 4%, Kanata-Sud 4%, Kanata-Nord 4%, Capitale 4%, Kitchissippi 4%, Rideau-Rockcliffe 4% |
| `WARD` | num | 100% | 24 | 1.00 · p25 6.75 · p50 12.50 · p95 22.85 · max 24.00  █▄█▄█▄█▄▄█▄█▄█▄█ |
| `SECTOR_EN` | cat | 100% | 3 | Urban 50%, Suburban 38%, Rural 12% |
| `SECTOR_FR` | cat | 100% | 3 | Urbain 50%, Suburbain 38%, Rural 12% |
| `OBJECTID` | num | 100% | 24 | 25.00 · p25 30.75 · p50 36.50 · p95 46.85 · max 48.00  █▄█▄█▄█▄▄█▄█▄█▄█ |
| `GLOBALID` | cat | 100% | 24 | {03C7C83F-DB65-49CC-BB4A 4%, {086F1700-E394-4394-8EC8 4%, {20002E33-7AE6-4D89-B234 4%, {3E049BC7-E873-4B10-8577 4%, {3FFF07C4-3187-42F7-A410 4%, {4E4EC93D-29C2-4C65-8B86 4% |
| `CREATED_DA` | date | 100% | 1 | 2021-10-14 → 2021-10-14 |
| `LAST_EDITE` | cat | 100% | 3 | 2021-10-14T00:00:00Z 83%, 2022-09-29T00:00:00Z 8%, 2022-02-17T00:00:00Z 8% |
| `SHAPE_Leng` | num | 100% | 24 | 16,123 · p25 28,531 · p50 41,080 · p95 179,347 · max 197,555  ▅█▄▄▄▁▁▂▁▁▁▁▁▂▂▂ |
| `SHAPE_Area` | num | 100% | 24 | 13,126,980 · p25 36,921,383 · p50 54,557,117 · p95 1,428,830,011 · max 1,550,245,091  █▂▁▁▁▁▁▁▁▁▁▁▁▁▁▁ |
| `Shape__Area` | num | 100% | 24 | 13,126,980 · p25 36,921,383 · p50 54,557,117 · p95 1,428,830,011 · max 1,550,245,091  █▂▁▁▁▁▁▁▁▁▁▁▁▁▁▁ |
| `Shape__Length` | num | 100% | 24 | 16,123 · p25 28,531 · p50 41,080 · p95 179,347 · max 197,555  ▅█▄▄▄▁▁▂▁▁▁▁▁▂▂▂ |
| `geometry` | cat | 100% | 24 | {"type": "Polygon", "coo 4%, {"type": "Polygon", "coo 4%, {"type": "Polygon", "coo 4%, {"type": "Polygon", "coo 4%, {"type": "Polygon", "coo 4%, {"type": "Polygon", "coo 4% |

## Candidate questions

- (none templated)

_profiled 2026-09-09 · `python3 tools/profile.py open_wards_2022_2026`_
