# Closed Confirmed Reportable Outbreaks Excluding COVID19

`open_closed_confirmed_reportable_outbreaks_excluding_covid19` · shape **arcgis-hub** · source `open-ottawa`

- origin: <https://open.ottawa.ca/datasets/ottawa::closed-confirmed-reportable-outbreaks-excluding-covid19>
- fetched 2026-09-09 · **843 rows** · 14 columns
- csv · licence: https://ottawa.ca/en/city-hall/open-transparent-and-accountable-government/open-

## Columns

| column | kind | non-null | distinct | summary |
| --- | --- | --- | --- | --- |
| `Outbreak_Identification_Number` | id/text | 100% | 843 | e.g. 2251-2022-00253, 2251-2023-00189, 2251-2023-00219 |
| `Facility_Type` | cat | 100% | 3 | Retirement Home 45%, Long Term Care Home 43%, Hospital 12% |
| `Location_Name` | text | 100% | 211 | e.g. ALTA VISTA RETIREMENT , AMICA THE GLEBE, AMICA WESTBORO PARK |
| `Outbreak_Type` | cat | 100% | 3 | Respiratory 74%, Enteric 25%, Other 1% |
| `Aetiologic_Agent` | cat | 100% | 20 | INFLUENZA A 19%, GASTROENTERITIS UNSPECIF 18%, RHINOVIRUS 14%, RESPIRATORY INFECTION UN 11%, SEASONAL CORONAVIRUS 9%, PARAINFLUENZA VIRUS 8% |
| `Start_Date` | date | 100% | 536 | 2021-09-19 → 2025-11-25 |
| `End_Date` | date | 100% | 572 | 2021-09-28 → 2025-12-08 |
| `Resident__Patient_Cases` | num | 100% | 60 | 0.00 · p25 4.00 · p50 7.00 · p95 35.00 · max 88.00  █▆▃▂▁▁▁▁▁▁▁▁▁▁▁▁ |
| `Resident__Patient_Deaths` | num | 100% | 5 | 0.00 · p25 0.00 · p50 0.00 · p95 1.00 · max 4.00  █▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁ |
| `Staff_Cases` | num | 100% | 26 | 0.00 · p25 0.00 · p50 0.00 · p95 8.00 · max 31.00  █▂▁▁▁▁▁▁▁▁▁▁▁▁▁▁ |
| `Staff_Deaths` | num | 100% | 1 | 0.00 · p25 0.00 · p50 0.00 · p95 0.00 · max 0.00   |
| `Total_Cases` | num | 100% | 64 | 0.00 · p25 4.00 · p50 8.00 · p95 41.00 · max 114  █▄▂▁▁▁▁▁▁▁▁▁▁▁▁▁ |
| `Total_Deaths` | num | 100% | 5 | 0.00 · p25 0.00 · p50 0.00 · p95 1.00 · max 4.00  █▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁ |
| `ObjectId` | num | 100% | 843 | 1.00 · p25 212 · p50 422 · p95 801 · max 843  ██▇██▇██▇█▇██▇██ |

## Candidate questions

- Trend / seasonality of open_closed_confirmed_reportable_outbreaks_excluding_covid19 over `Start_Date`; structural breaks?

_profiled 2026-09-09 · `python3 tools/profile.py open_closed_confirmed_reportable_outbreaks_excluding_covid19`_
