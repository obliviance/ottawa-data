# Solid Waste Collection Calendar - Collection Days

`open_solid_waste_collection_calendar_collection_days` · shape **arcgis-hub** · source `open-ottawa`

- origin: <https://open.ottawa.ca/datasets/ottawa::solid-waste-collection-calendar-collection-days>
- fetched 2026-09-09 · **2,853 rows** · 7 columns
- csv · licence: https://ottawa.ca/en/city-hall/get-know-your-city/open-data#open-data-licence-ve

## Columns

| column | kind | non-null | distinct | summary |
| --- | --- | --- | --- | --- |
| `GCD` | cat | 100% | 5 | MONDAY 29%, THURSDAY 21%, FRIDAY 17%, TUESDAY 17%, WEDNESDAY 17% |
| `C_ZONE` | cat | 100% | 3 | Central 66%, West 20%, East 14% |
| `SCHEDULE` | cat | 100% | 13 | A-Apt (Gar) 44%, B-Apt (Gar) 43%, A-Apt (Gar-GMP-Fbr) 4%, B-Apt (Gar-GMP-Fbr) 3%, A 2%, B 2% |
| `CONTRACTOR` | cat | 100% | 2 | City 66%, Miller 34% |
| `OBJECTID` | num | 100% | 2,853 | 1.00 · p25 714 · p50 1,427 · p95 2,710 · max 2,853  █▇▇█▇▇▇█▇▇▇█▇▇▇█ |
| `Shape_Length` | num | 100% | 2,684 | 2.03 · p25 148 · p50 261 · p95 1,592 · max 222,290  █▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁ |
| `Shape_Area` | num | 100% | 2,682 | 0.01 · p25 613 · p50 1,752 · p95 44,497 · max 737,661,743  █▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁ |

## Candidate questions

- Concentration in `CONTRACTOR` — which actors dominate? (join entity spine)

_profiled 2026-09-09 · `python3 tools/profile.py open_solid_waste_collection_calendar_collection_days`_
