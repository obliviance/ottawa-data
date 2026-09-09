# Automated Speed Enforcement Camera Removal – Monitoring Speed Data

`open_automated_speed_enforcement_camera_removal_monitoring_speed_data` · shape **arcgis-hub** · source `open-ottawa`

- origin: <https://open.ottawa.ca/datasets/ottawa::automated-speed-enforcement-camera-removal-monitoring-speed-data>
- fetched 2026-09-09 · **598 rows** · 9 columns
- csv · licence: https://ottawa.ca/en/city-hall/open-transparent-and-accountable-government/open-

## Columns

| column | kind | non-null | distinct | summary |
| --- | --- | --- | --- | --- |
| `Data_Type` | cat | 100% | 3 | ASE Active  85%, ASE Removed 13%, Pre ASE Installation 1% |
| `Location` | cat | 100% | 8 | E002 - Innes Rd. between 13%, E003 - Bayshore Dr. betw 13%, E007 - Smyth Rd. between 13%, E008 - Meadowlands Dr. W 13%, E004 - Katimavik Rd. bet 13%, E006 - Ogilvie Rd. betwe 13% |
| `Camera_Install_Year` | num | 100% | 1 | 2,020 · p25 2,020 · p50 2,020 · p95 2,020 · max 2,020   |
| `Date_of_Data_Collection` | date | 99% | 78 | 1-01-21 → 1-12-25 |
| `AvgSpeed` | num | 97% | 34 | 33.00 · p25 37.00 · p50 40.00 · p95 58.00 · max 66.00  ▃█▄▃▂▃▃▂▁▁▂▁▁▁▁▁ |
| `Pct85th` | num | 100% | 35 | 0.00 · p25 42.00 · p50 47.00 · p95 64.15 · max 74.00  ▁▁▁▁▁▁▁▁▇█▄▆▃▂▁▁ |
| `PctCompliance` | num | 100% | 81 | 0.00 · p25 63.00 · p50 75.00 · p95 90.00 · max 95.00  ▁▁▁▁▁▁▁▁▁▂▃▄▆▆█▃ |
| `PctHighEndSpeeders` | num | 100% | 88 | 0.00 · p25 0.30 · p50 1.00 · p95 6.61 · max 22.00  █▃▁▁▁▁▁▁▁▁▁▁▁▁▁▁ |
| `ObjectId` | num | 100% | 598 | 1.00 · p25 150 · p50 300 · p95 568 · max 598  █▇▇█▇▇█▇▇█▇▇█▇▇█ |

## Candidate questions

- Trend / seasonality of open_automated_speed_enforcement_camera_removal_monitoring_speed_data over `Camera_Install_Year`; structural breaks?

_profiled 2026-09-09 · `python3 tools/profile.py open_automated_speed_enforcement_camera_removal_monitoring_speed_data`_
