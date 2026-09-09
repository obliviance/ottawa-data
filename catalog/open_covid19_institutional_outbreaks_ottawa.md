# COVID19 Institutional Outbreaks Ottawa

`open_covid19_institutional_outbreaks_ottawa` · shape **arcgis-hub** · source `open-ottawa`

- origin: <https://open.ottawa.ca/datasets/ottawa::covid19-institutional-outbreaks-ottawa>
- fetched 2026-09-09 · **2,688 rows** · 11 columns
- csv · licence: https://ottawa.ca/en/city-hall/open-transparent-and-accountable-government/open-

## Columns

| column | kind | non-null | distinct | summary |
| --- | --- | --- | --- | --- |
| `Location_Name` | id/text | 100% | 2,573 | e.g. MAISON MERE SOEURS DE , AMICA THE GLEBE, CENTRE D'ACCUEIL CHAMP |
| `Facility_Type` | cat | 100% | 14 | Retirement Home 28%, Hospital 20%, Long Term Care Home 16%, Group Home 11%, School 11%, Licensed Child Care Faci 6% |
| `Start_Date` | date | 100% | 1,161 | 2020-03-20 → 2026-06-01, 1 gaps >30d |
| `End_Date` | date | 100% | 1,191 | 2020-04-09 → 2026-06-08, 2 gaps >30d |
| `Resident__Patient__Child__Student_Cases` | num | 100% | 77 | 0.00 · p25 2.00 · p50 4.00 · p95 30.00 · max 170  █▂▁▁▁▁▁▁▁▁▁▁▁▁▁▁ |
| `Resident__Patient__Child__Student_Deaths` | num | 100% | 20 | 0.00 · p25 0.00 · p50 0.00 · p95 1.00 · max 60.00  █▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁ |
| `Staff_Cases` | num | 100% | 52 | 0.00 · p25 0.00 · p50 1.00 · p95 11.00 · max 94.00  █▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁ |
| `Staff_Deaths` | num | 100% | 3 | 0.00 · p25 0.00 · p50 0.00 · p95 0.00 · max 2.00  █▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁ |
| `Total_Cases` | num | 100% | 98 | 0.00 · p25 3.00 · p50 6.00 · p95 39.65 · max 264  █▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁ |
| `Total_Deaths` | num | 100% | 20 | 0.00 · p25 0.00 · p50 0.00 · p95 1.00 · max 60.00  █▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁ |
| `ObjectId` | num | 100% | 2,688 | 1.00 · p25 673 · p50 1,344 · p95 2,554 · max 2,688  ████████████████ |

## Candidate questions

- Trend / seasonality of open_covid19_institutional_outbreaks_ottawa over `Start_Date`; structural breaks?

_profiled 2026-09-09 · `python3 tools/profile.py open_covid19_institutional_outbreaks_ottawa`_
