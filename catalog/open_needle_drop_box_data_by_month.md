# Needle Drop Box Data by Month

`open_needle_drop_box_data_by_month` · shape **arcgis-hub** · source `open-ottawa`

- origin: <https://open.ottawa.ca/datasets/ottawa::needle-drop-box-data-by-month>
- fetched 2026-09-09 · **60 rows** · 5 columns
- csv · licence: https://ottawa.ca/en/city-hall/open-transparent-and-accountable-government/open-

## Columns

| column | kind | non-null | distinct | summary |
| --- | --- | --- | --- | --- |
| `Source` | cat | 100% | 1 | Needle Drop Box 100% |
| `Year_Month` | date | 100% | 60 | 2021-01-01 → 2026-03-01, 35 gaps >30d |
| `Total_Weight__Kg_` | num | 100% | 60 | 125 · p25 265 · p50 329 · p95 445 · max 472  ▁▁▂▃▂▃▃▃▆▅▃█▃▅▂▂ |
| `Estimated_Needles_based_on_Weight` | num | 100% | 60 | 41,700 · p25 89,256 · p50 109,717 · p95 148,355 · max 157,236  ▁▁▂▃▂▃▄▃▆▅▃█▂▅▃▂ |
| `ObjectId` | num | 100% | 60 | 1.00 · p25 15.75 · p50 30.50 · p95 57.05 · max 60.00  ███▆██▆██▆██▆███ |

## Candidate questions

- (none templated)

_profiled 2026-09-09 · `python3 tools/profile.py open_needle_drop_box_data_by_month`_
