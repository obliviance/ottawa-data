# Ontario Public Sector Salary Disclosure 2025

`ontario_sunshine_2025` · shape **html** · source `sunshine-list`

- origin: <https://www.ontario.ca/page/public-sector-salary-disclosure>
- fetched 2026-10-24 · **404,922 rows** · 13 columns
- English CSV of Compendium + Addendum from ontario.ca artefact manifest; all employers; salary_paid / taxable_benefits parsed numeric

## Columns

| column | kind | non-null | distinct | summary |
| --- | --- | --- | --- | --- |
| `Sector` | cat | 100% | 18 | School Boards 28%, Municipalities & Service 23%, Hospitals & Boards of Pu 18%, Government of Ontario –  9%, Universities 8%, Crown Agencies 5% |
| `Last Name` | text | 100% | 114,822 | e.g. Aarts, Aaslepp, Abalos |
| `First Name` | text | 100% | 59,738 | e.g. Cheri, Drew, L. Michelle |
| `Salary` | num | 100% | 328,466 | 100,000 · p25 113,217 · p50 122,262 · p95 202,689 · max 1,907,409  █▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁ |
| `Benefits` | num | 100% | 78,977 | 0.00 · p25 93.36 · p50 307 · p95 2,025 · max 134,304  █▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁ |
| `Employer` | text | 100% | 2,285 | e.g. Fanshawe College Of Ap, Humber College Institu, George Brown College O |
| `Job Title` | text | 100% | 61,636 | e.g. Professor, Manager, Awards, Schol, Director, Office of St |
| `Year` | num | 100% | 1 | 2,025 · p25 2,025 · p50 2,025 · p95 2,025 · max 2,025   |
| `kind` | cat | 100% | 1 | compendium 100% |
| `source_file` | cat | 100% | 1 | tbs-pssd-compendium-sala 100% |
| `salary_paid` | num | 100% | 328,466 | 100,000 · p25 113,217 · p50 122,262 · p95 202,689 · max 1,907,409  █▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁ |
| `taxable_benefits` | num | 100% | 78,977 | 0.00 · p25 93.36 · p50 307 · p95 2,025 · max 134,304  █▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁ |
| `disclosure_year` | num | 100% | 1 | 2,025 · p25 2,025 · p50 2,025 · p95 2,025 · max 2,025   |

## Candidate questions

- Trend / seasonality of ontario_sunshine_2025 over `Year`; structural breaks?
- Concentration in `Last Name` — which actors dominate? (join entity spine)

_profiled 2026-10-24 · `python3 tools/profile.py ontario_sunshine_2025`_
