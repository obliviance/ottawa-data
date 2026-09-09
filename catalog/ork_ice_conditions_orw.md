# Ice Conditions ORW

`ork_ice_conditions_orw` · shape **arcgis-hub** · source `riverkeeper`

- origin: <https://ottawa-riverkeeper-open-data-ork-so.hub.arcgis.com/datasets/ork-so::ice-conditions-orw>
- fetched 2026-09-09 · **6 rows** · 8 columns
- csv · licence: 

## Columns

| column | kind | non-null | distinct | summary |
| --- | --- | --- | --- | --- |
| `X` | num | 100% | 6 | -8,508,695 · p25 -8,454,104 · p50 -8,442,418 · p95 -8,377,245 · max -8,361,507  █▁▁▁▁███▁█▁▁▁▁▁█ |
| `Y` | num | 100% | 6 | 5,680,695 · p25 5,687,271 · p50 5,695,969 · p95 5,708,789 · max 5,712,030  █▁█▁▁▁█▁██▁▁▁▁▁█ |
| `Location` | cat | 100% | 6 | Ottawa River @ Deschenes 17%, Ottawa River @ Sand Poin 17%, Ottawa River @ Breckenri 17%, Ottawa River @ Alexandri 17%, Ottawa River @ Wendover 17%, Ottawa River @ River Hou 17% |
| `Lat` | num | 100% | 6 | 45.37 · p25 45.42 · p50 45.47 · p95 45.55 · max 45.57  █▁█▁▁▁█▁██▁▁▁▁▁█ |
| `Lon` | num | 100% | 6 | -76.43 · p25 -75.94 · p50 -75.84 · p95 -75.25 · max -75.11  █▁▁▁▁███▁█▁▁▁▁▁█ |
| `Ice_Conditions` | cat | 100% | 2 | Full ice ON 67%, Ice forming 33% |
| `Date` | date | 100% | 6 | 2021-12-22 → 2024-01-20, 1 gaps >30d |
| `FID` | num | 100% | 6 | 1.00 · p25 2.25 · p50 3.50 · p95 5.75 · max 6.00  █▁▁█▁▁█▁▁█▁▁█▁▁█ |

## Candidate questions

- (none templated)

_profiled 2026-09-09 · `python3 tools/profile.py ork_ice_conditions_orw`_
