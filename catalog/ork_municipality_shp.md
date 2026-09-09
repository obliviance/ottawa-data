# Municipality shp

`ork_municipality_shp` · shape **arcgis-hub** · source `riverkeeper`

- origin: <https://ottawa-riverkeeper-open-data-ork-so.hub.arcgis.com/datasets/ork-so::municipality-shp-1>
- fetched 2026-09-09 · **276 rows** · 12 columns
- csv · licence: 

## Columns

| column | kind | non-null | distinct | summary |
| --- | --- | --- | --- | --- |
| `FID` | num | 100% | 276 | 1.00 · p25 69.75 · p50 138 · p95 262 · max 276  █▇▇▇▇█▇▇▇▇█▇▇▇▇█ |
| `MUS_NM_MUN` | id/text | 100% | 276 | e.g. Alleyn-et-Cawood, Amherst, Amos |
| `Shape_Leng` | num | 100% | 276 | 0.03 · p25 0.43 · p50 0.72 · p95 1.76 · max 6.69  ▆█▄▂▁▁▁▁▁▁▁▁▁▁▁▁ |
| `Shape_Area` | num | 100% | 276 | 0.00 · p25 0.01 · p50 0.02 · p95 0.10 · max 0.66  █▂▁▁▁▁▁▁▁▁▁▁▁▁▁▁ |
| `Municipali` | id/text | 100% | 276 | e.g. Alleyn-et-Cawood, Amherst, Amos |
| `Website` | id/text | 100% | 268 | e.g. www.alleyn-cawood.ca, www.municipalite.amher, www.amos.quebec |
| `Phone` | id/text | 100% | 270 | e.g. 819-467-2941, 819-681-3372, 819-732-3254 |
| `Regional` | cat | 100% | 21 |   26%, MRC Papineau 9%, MRC Les Laurentides 7%, MRC Pontiac 7%, MRC Témiscamingue 7%, MRC La Vallée-de-la-Gati 6% |
| `Ministry` | cat | 100% | 2 | https://www.quebec.ca/en 64%, https://www.ontario.ca/p 36% |
| `Province` | cat | 100% | 2 | QC 64%, ON 36% |
| `Shape__Area` | num | 100% | 276 | 530,916 · p25 117,385,393 · p50 311,744,642 · p95 1,744,042,466 · max 12,338,106,589  █▂▁▁▁▁▁▁▁▁▁▁▁▁▁▁ |
| `Shape__Length` | num | 100% | 276 | 4,470 · p25 57,292 · p50 94,526 · p95 228,880 · max 889,010  ▆█▄▃▁▁▁▁▁▁▁▁▁▁▁▁ |

## Candidate questions

- (none templated)

_profiled 2026-09-09 · `python3 tools/profile.py ork_municipality_shp`_
