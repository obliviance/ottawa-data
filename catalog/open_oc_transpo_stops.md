# OC Transpo Stops

`open_oc_transpo_stops` · shape **arcgis-hub** · source `open-ottawa` · **spatial**

- origin: <https://open.ottawa.ca/datasets/ottawa::oc-transpo-stops>
- fetched 2026-09-09 · **5,785 rows** · 9 columns
- csv · licence: https://ottawa.ca/en/city-hall/open-transparent-and-accountable-government/open-

## Columns

| column | kind | non-null | distinct | summary |
| --- | --- | --- | --- | --- |
| `X` | num | 100% | 5,785 | -8,465,044 · p25 -8,434,186 · p50 -8,425,911 · p95 -8,401,520 · max -8,387,110  ▁▁▃▃▂▃▅█▇▆▂▃▄▂▁▁ |
| `Y` | num | 100% | 5,785 | 5,642,033 · p25 5,672,516 · p50 5,680,226 · p95 5,696,705 · max 5,703,712  ▁▁▁▁▂▄▅▄▇█▆▆▇▅▃▁ |
| `FID` | num | 100% | 5,785 | 1.00 · p25 1,447 · p50 2,893 · p95 5,496 · max 5,785  ██▇█▇█▇█▇█▇█▇█▇█ |
| `F560` | num | 100% | 5,585 | 0.00 · p25 2,174 · p50 4,405 · p95 8,630 · max 9,999  ▃▆▆▅█▃▄▄▃▄▅▅▅▅▂▁ |
| `Location` | text | 100% | 4,004 | e.g. SUSSEX / RIDEAU FALLS, SUSSEX / ALEXANDER, ALEXANDER / THOMAS |
| `Latitude` | num | 100% | 5,725 | 45.13 · p25 45.32 · p50 45.37 · p95 45.48 · max 45.52  ▁▁▁▁▂▄▅▄▇█▆▆▇▅▃▁ |
| `Longitude` | num | 100% | 5,749 | -76.04 · p25 -75.77 · p50 -75.69 · p95 -75.47 · max -75.34  ▁▁▃▃▂▃▅█▇▆▂▃▄▂▁▁ |
| `Shelter` | cat | 100% | 2 |   77%, Y 23% |
| `Bench` | cat | 100% | 2 |   86%, Y 14% |

## Candidate questions

- Spatial clustering of open_oc_transpo_stops; overlay wards + the decision timeline

_profiled 2026-09-09 · `python3 tools/profile.py open_oc_transpo_stops`_
