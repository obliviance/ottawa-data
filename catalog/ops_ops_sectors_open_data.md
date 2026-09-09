# OPS Sectors Open Data

`ops_ops_sectors_open_data` · shape **arcgis-hub** · source `ops-data-portal`

- origin: <https://data.ottawapolice.ca/datasets/3b34d8b0a0b346e8847f1700f1abc30a_0>
- fetched 2026-09-09 · **19 rows** · 8 columns
- csv · licence: https://data.ottawapolice.ca/pages/about#termsofuse

## Columns

| column | kind | non-null | distinct | summary |
| --- | --- | --- | --- | --- |
| `FID` | num | 100% | 19 | 1.00 · p25 5.50 · p50 10.00 · p95 18.10 · max 19.00  █▄▄▄▄▄▄█▄▄▄▄▄▄▄█ |
| `SectorID` | num | 100% | 19 | 11.00 · p25 15.50 · p50 23.00 · p95 36.10 · max 37.00  ██▄█▁▁██▄▁▁▁█▄██ |
| `Division` | num | 100% | 3 | 1.00 · p25 1.00 · p50 2.00 · p95 3.00 · max 3.00  █▁▁▁▁▁▁▆▁▁▁▁▁▁▁█ |
| `SectorID2` | cat | 100% | 19 | Sector 11 5%, Sector 12 5%, Sector 36 5%, Sector 37 5%, Sector 13 5%, Sector 15 5% |
| `SectorID3` | cat | 100% | 19 | Secteur 11 5%, Secteur 12 5%, Secteur 36 5%, Secteur 37 5%, Secteur 13 5%, Secteur 15 5% |
| `Urban_Rura` | cat | 100% | 19 | Rural 1 5%, Rural 2 5%, Rural 3 5%, Rural 4 5%, Urban 1 5%, Urban 2 5% |
| `SHAPE__Area` | num | 100% | 19 | 7,288,370 · p25 34,875,583 · p50 98,227,891 · p95 1,432,727,752 · max 1,552,244,460  █▃▂▁▁▁▁▁▁▁▁▁▁▁▁▁ |
| `SHAPE__Length` | num | 100% | 19 | 11,441 · p25 32,764 · p50 55,873 · p95 176,751 · max 188,274  ▄▆▆▂█▁▁▄▁▁▂▁▁▁▄▂ |

## Candidate questions

- (none templated)

_profiled 2026-09-09 · `python3 tools/profile.py ops_ops_sectors_open_data`_
