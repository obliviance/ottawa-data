# Public sector salary disclosure 2013

`ontario_public_sector_salary_disclosure_2013` · shape **ckan** · source `sunshine-list`

- origin: <https://data.ontario.ca/dataset/public-sector-salary-disclosure-2013>
- fetched 2026-09-09 · **97,916 rows** · 8 columns
- csv · licence: Public Sector Salary Disclosure Act

## Columns

| column | kind | non-null | distinct | summary |
| --- | --- | --- | --- | --- |
| `Sector` | cat | 100% | 17 | Municipalities and Servi 26%, Universities 16%, School Boards 13%, Hydro One and Ontario Po 12%, Government of Ontario -  11%, Hospitals and Boards of  9% |
| `Last Name` | text | 100% | 39,306 | e.g. ABBAS, AGATE, AL-AZZAWI |
| `First Name` | text | 99% | 17,857 | e.g. SADIQ, JEFFERY MICHAEL, ABDUL |
| `Salary Paid` | num | 100% | 83,464 | 100,000 · p25 105,802 · p50 115,414 · p95 193,125 · max 1,714,000  █▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁ |
| `Taxable Benefits` | num | 100% | 32,183 | 0.00 · p25 207 · p50 487 · p95 2,462 · max 103,081  █▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁ |
| `Employer` | text | 100% | 1,498 | e.g. Algonquin College, Cambrian College, Canadore College |
| `Job Title` | text | 100% | 23,180 | e.g. Professor, Manager, Counselling a, Manager, Client Suppor |
| `Calendar Year` | num | 100% | 1 | 2,013 · p25 2,013 · p50 2,013 · p95 2,013 · max 2,013   |

## Candidate questions

- Trend / seasonality of ontario_public_sector_salary_disclosure_2013 over `Calendar Year`; structural breaks?
- Concentration in `Last Name` — which actors dominate? (join entity spine)

_profiled 2026-09-09 · `python3 tools/profile.py ontario_public_sector_salary_disclosure_2013`_
