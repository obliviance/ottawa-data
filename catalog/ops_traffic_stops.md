# Ottawa Police — Traffic Stops (Race Data Collection Program)

`ops_traffic_stops` · shape **arcgis-hub** · source `ops-data-portal` · **spatial**

- origin: <https://services7.arcgis.com/2vhcNzw0NfUwAD3d/arcgis/rest/services/TSRDCP_TrafficStops_v1/FeatureServer/0>
- fetched 2026-10-24 · **455,717 rows** · 20 columns
- Hub CSV export via arcgis_layers.py; 455,717 rows

## Columns

| column | kind | non-null | distinct | summary |
| --- | --- | --- | --- | --- |
| `OBJECTID` | num | 100% | 455,717 | 1.00 · p25 113,930 · p50 227,859 · p95 432,931 · max 455,717  █▇▇█▇▇▇█▇▇▇█▇▇▇█ |
| `Occurred Date` | date | 100% | 4,018 | 2014-01-01 → 2024-12-31 |
| `Occurred Year` | num | 100% | 11 | 2,014 · p25 2,016 · p50 2,018 · p95 2,024 · max 2,024  █▇▁▆▇▁▆▇▁▇▁▆▄▁▄▄ |
| `Occurrence Number` | num | 100% | 260,081 | 1.00 · p25 70,642 · p50 151,151 · p95 316,493 · max 400,040  ▇▇█▇▆▅▅▆▆▅▆▆▅▂▁▁ |
| `Location` | text | 100% | 86,817 | e.g. BRADLEY AVE / MONTREAL, 36 PENNARD WAY, HIGHWAY 417 / HWY417 I |
| `Neighbourhood` | text | 99% | 111 | e.g. Vanier South, Greenboro East, Glebe - Dows Lake |
| `Division` | cat | 99% | 3 | East 38%, West 33%, Central 29% |
| `How Cleared` | cat | 100% | 4 | Charged 43%, Warning (T-Stop) 32%, Final 24%, Data Quality 0% |
| `Day of Week` | cat | 100% | 7 | Tue 16%, Wed 15%, Fri 15%, Thu 15%, Mon 14%, Sat 14% |
| `Occurred Hour` | num | 98% | 24 | 0.00 · p25 800 · p50 1,200 · p95 2,300 · max 2,300  ▅▂▂▁▃▄▇▄▅█▃▅▂▃▃▇ |
| `Driver Age` | cat | 83% | 4 | 25-54 62%, 16-24 20%, 55+ 17%, -15 0% |
| `Driver Gender` | cat | 83% | 3 | M 71%, F 29%, D 0% |
| `Driver Race` | cat | 100% | 10 | White 49%, UNKNOWN 20%, Middle Eastern 12%, Black 10%, East or Southeast Asian 3%, South Asian 3% |
| `Driver City` | text | 83% | 3,576 | e.g. OTTAWA, GLOUCESTER, DUNROBIN |
| `Driver Province` | text | 83% | 60 | e.g. ON, QC, NB |
| `x_coordinate` | num | 100% | 26,963 | 317,279 · p25 364,174 · p50 368,294 · p95 383,991 · max 411,611  ▁▁▁▁▁▁▁▃█▄▂▁▁▁▁▁ |
| `y_coordinate` | num | 100% | 24,567 | 4,981,006 · p25 5,021,566 · p50 5,026,720 · p95 5,036,226 · max 5,048,026  ▁▁▁▁▁▁▁▂▄▄▇▆█▂▁▁ |
| `Time of Day` | cat | 98% | 4 | Afternoon 32%, Morning 30%, Evening 23%, Night 15% |
| `longitude` | num | 100% | 53,276 | -76.34 · p25 -75.74 · p50 -75.69 · p95 -75.49 · max -75.13  ▁▁▁▁▁▁▁▃█▄▂▁▁▁▁▁ |
| `latitude` | num | 100% | 53,279 | 44.97 · p25 45.33 · p50 45.38 · p95 45.46 · max 45.57  ▁▁▁▁▁▁▁▁▃▄▇▆█▂▁▁ |

## Candidate questions

- `Occurrence Number` by `Neighbourhood` — equity gradient? (join ONS income)
- Trend / seasonality of ops_traffic_stops over `Occurred Date`; structural breaks?
- Spatial clustering of ops_traffic_stops; overlay wards + the decision timeline

_profiled 2026-10-24 · `python3 tools/profile.py ops_traffic_stops`_
