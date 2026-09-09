# Wards 2003  (Historical)

`open_wards_2003_historical` · shape **arcgis-hub** · source `open-ottawa` · **spatial**

- origin: <https://open.ottawa.ca/datasets/ottawa::wards-2003-historical>
- fetched 2026-09-09 · **21 rows** · 9 columns
- geojson · licence: https://ottawa.ca/en/city-hall/get-know-your-city/open-data#open-data-licence-ve

## Columns

| column | kind | non-null | distinct | summary |
| --- | --- | --- | --- | --- |
| `FID` | num | 100% | 21 | 1.00 · p25 6.00 · p50 11.00 · p95 20.00 · max 21.00  █▄▄█▄▄▄█▄▄▄█▄▄▄█ |
| `WARDNAME` | cat | 100% | 21 | Innes 5%, Beacon Hill-Cyrville 5%, Alta Vista 5%, Orléans 5%, Kanata 5%, Baseline 5% |
| `WARDNUMBER` | num | 100% | 21 | 1.00 · p25 6.00 · p50 11.00 · p95 20.00 · max 21.00  █▄▄█▄▄▄█▄▄▄█▄▄▄█ |
| `COUNCILLOR` | cat | 100% | 21 | Rainer Bloess 5%, Michel Bellemare 5%, Peter Hume 5%, Herb Kreling 5%, Peggy Feltmate 5%, Rick Chiarelli 5% |
| `SHAPE_Leng` | num | 100% | 21 | 14,727 · p25 21,469 · p50 37,024 · p95 106,482 · max 169,995  █▅▂▃▁▅▁▂▂▂▁▁▁▁▁▂ |
| `SHAPE_Area` | num | 100% | 21 | 5,961,155 · p25 14,383,121 · p50 27,039,195 · p95 415,218,073 · max 633,275,184  █▁▁▁▁▁▂▁▁▁▁▁▁▁▁▁ |
| `Shape__Area` | num | 100% | 21 | 12,097,121 · p25 29,112,569 · p50 54,772,294 · p95 833,362,832 · max 1,283,211,481  █▁▁▁▁▁▂▁▁▁▁▁▁▁▁▁ |
| `Shape__Length` | num | 100% | 21 | 20,981 · p25 30,573 · p50 52,752 · p95 150,865 · max 242,093  █▅▂▃▁▅▂▁▂▂▁▁▁▁▁▂ |
| `geometry` | cat | 100% | 21 | {"type": "Polygon", "coo 5%, {"type": "MultiPolygon", 5%, {"type": "Polygon", "coo 5%, {"type": "MultiPolygon", 5%, {"type": "Polygon", "coo 5%, {"type": "Polygon", "coo 5% |

## Candidate questions

- (none templated)

_profiled 2026-09-09 · `python3 tools/profile.py open_wards_2003_historical`_
