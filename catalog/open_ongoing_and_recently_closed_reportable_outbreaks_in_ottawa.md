# Ongoing and recently closed reportable outbreaks in Ottawa

`open_ongoing_and_recently_closed_reportable_outbreaks_in_ottawa` · shape **arcgis-hub** · source `open-ottawa`

- origin: <https://open.ottawa.ca/datasets/ottawa::ongoing-and-recently-closed-reportable-outbreaks-in-ottawa>
- fetched 2026-09-09 · **62 rows** · 8 columns
- csv · licence: https://ottawa.ca/en/city-hall/open-transparent-and-accountable-government/open-

## Columns

| column | kind | non-null | distinct | summary |
| --- | --- | --- | --- | --- |
| `Type_of_Outbreak` | cat | 100% | 2 | Respiratory 53%, Enteric 47% |
| `Outbreak_Name` | id/text | 100% | 57 | e.g. ANDREW FLECK CHILDREN', BARRHAVEN MANOR, BORDEN FARM CHILD CARE |
| `Facility_Type` | cat | 100% | 7 | Long Term Care Home 35%, Retirement Home 27%, Hospital 18%, Childcare 13%, School - Public 3%, School - Elementary 2% |
| `Outbreak_Location_Details` | text | 100% | 35 | e.g. Single Cohort, Facility-Wide, Multiple Cohorts |
| `Start_Date` | date | 100% | 25 | 2026-01-08 → 2026-02-19 |
| `End_Date` | date | 56% | 15 | 2026-02-06 → 2026-02-20 |
| `Aetiologic_Agent` | cat | 100% | 10 | GASTROENTERITIS UNSPECIF 34%, RESPIRATORY INFECTION UN 18%, NOROVIRUS 11%, INFLUENZA A 11%, COVID-19 10%, SEASONAL CORONAVIRUS 8% |
| `ObjectId` | num | 100% | 62 | 1.00 · p25 16.25 · p50 31.50 · p95 58.95 · max 62.00  █████▆████▆█████ |

## Candidate questions

- (none templated)

_profiled 2026-09-09 · `python3 tools/profile.py open_ongoing_and_recently_closed_reportable_outbreaks_in_ottawa`_
