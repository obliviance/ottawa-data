# Homicide

`open_homicide` · shape **arcgis-hub** · source `open-ottawa`

- origin: <https://open.ottawa.ca/datasets/ottawa::homicide>
- fetched 2026-09-09 · **131 rows** · 13 columns
- csv · licence: https://data.ottawapolice.ca/pages/open-data-licence

## Columns

| column | kind | non-null | distinct | summary |
| --- | --- | --- | --- | --- |
| `OBJECTID` | num | 100% | 131 | 1.00 · p25 33.50 · p50 66.00 · p95 124 · max 131  █▇▇▇▇▇▇█▇▇▇▇▇▇▇█ |
| `Year` | num | 100% | 8 | 2,018 · p25 2,020 · p50 2,022 · p95 2,025 · max 2,025  ▅▁▄▁▃▁▅▁▁▅▁▅▁█▁▆ |
| `Reported Date` | date | 100% | 120 | 2018-01-09 → 2025-11-17, 31 gaps >30d |
| `Occurred Date` | date | 100% | 120 | 2018-01-09 → 2025-11-17, 31 gaps >30d |
| `Weekday` | cat | 100% | 7 | Wednesday 20%, Thursday 15%, Friday 15%, Tuesday 14%, Monday 14%, Saturday 11% |
| `Offence Category` | cat | 100% | 3 | Murder 1st Dgree 59%, Murder 2nd Dgree 36%, Manslaughter 5% |
| `Sector` | num | 100% | 19 | 11.00 · p25 17.00 · p50 24.00 · p95 35.00 · max 37.00  ▁▃▄▆▁▁▄█▅▁▁▁▇▄█▁ |
| `Division` | cat | 100% | 3 | East 39%, Central 34%, West 27% |
| `Neighbourhood` | text | 100% | 46 | e.g. Hunt Club East - Weste, Bells Corners West, Centretown |
| `Ward` | cat | 100% | 20 | Ward 12 - Rideau-Vanier 17%, Ward 10 - Gloucester-Sou 10%, Ward 18 - Alta Vista 9%, Ward 14 - Somerset 8%, Ward 8 - College 7%, Ward 13 - Rideau-Rockcli 6% |
| `Councillor` | cat | 100% | 20 | Stéphanie Plante 17%, Jessica Bradley 10%, Marty Carr 9%, Ariel Troster 8%, Laine Johnson 7%, Rawlson King 6% |
| `x` | num | 100% | 109 | 343,754 · p25 365,055 · p50 368,825 · p95 383,037 · max 384,598  ▁▁▁▁▁▁▂▄▄▇█▅▁▁▁▃ |
| `y` | num | 100% | 109 | 5,003,930 · p25 5,023,943 · p50 5,029,100 · p95 5,034,757 · max 5,039,619  ▁▁▁▁▁▃▁▁▅▄▂▅█▄▁▁ |

## Candidate questions

- `Sector` by `Neighbourhood` — equity gradient? (join ONS income)

_profiled 2026-09-09 · `python3 tools/profile.py open_homicide`_
