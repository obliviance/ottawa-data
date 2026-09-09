# Building Footprints

`open_building_footprints` · shape **arcgis-hub** · source `open-ottawa`

- origin: <https://open.ottawa.ca/datasets/ottawa::building-footprints>
- fetched 2026-09-09 · **392,278 rows** · 4 columns
- csv · licence: https://ottawa.ca/en/city-hall/get-know-your-city/open-data#open-data-licence-ve

## Columns

| column | kind | non-null | distinct | summary |
| --- | --- | --- | --- | --- |
| `OBJECTID` | num | 100% | 392,278 | 2,296,666 · p25 2,394,735 · p50 2,492,804 · p95 2,669,329 · max 2,688,943  █▇▇█▇▇█▇▇█▇▇█▇▇█ |
| `Shape_Length` | num | 100% | 392,236 | 0.09 · p25 23.38 · p50 66.98 · p95 118 · max 6,072  █▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁ |
| `Shape_Area` | num | 100% | 392,236 | -0.00 · p25 31.90 · p50 211 · p95 619 · max 156,855  █▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁ |
| `GlobalID` | id/text | 100% | 392,278 | e.g. {00F95843-C30D-46BA-B3, {011EF3BD-ADD2-4B54-A6, {01884622-DE5C-4D21-A7 |

## Candidate questions

- (none templated)

_profiled 2026-09-09 · `python3 tools/profile.py open_building_footprints`_
