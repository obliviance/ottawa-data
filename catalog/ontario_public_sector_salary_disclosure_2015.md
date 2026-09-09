# Public sector salary disclosure 2015

`ontario_public_sector_salary_disclosure_2015` · shape **ckan** · source `sunshine-list`

- origin: <https://data.ontario.ca/dataset/public-sector-salary-disclosure-2015>
- fetched 2026-09-09 · **115,920 rows** · 8 columns
- csv · licence: Public Sector Salary Disclosure Act

## Columns

| column | kind | non-null | distinct | summary |
| --- | --- | --- | --- | --- |
| `Sector` | cat | 100% | 18 | Municipalities & Service 30%, Universities 15%, School Boards 13%, Hospitals & Boards of Pu 11%, Government of Ontario -  11%, Ontario Power Generation 7% |
| `Last Name` | text | 100% | 44,759 | e.g. Aniol, Bennett, Bliss |
| `First Name` | text | 100% | 20,504 | e.g. Richard, Phyllis, Rose |
| `Salary Paid` | num | 100% | 98,539 | 100,000 · p25 105,520 · p50 115,332 · p95 193,262 · max 1,528,933  █▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁ |
| `Taxable Benefits` | text | 100% | 36,262 | e.g. $177.35, $187.86, $177.79 |
| `Employer` | text | 100% | 1,670 | e.g. Aboriginal Affairs, Agriculture, Food & Ru, Attorney General |
| `Job Title` | text | 100% | 26,401 | e.g. Senior Negotiator / Né, Manager, Issues Manage, Manager, Performance M |
| `Calendar Year` | num | 100% | 1 | 2,015 · p25 2,015 · p50 2,015 · p95 2,015 · max 2,015   |

## Candidate questions

- Trend / seasonality of ontario_public_sector_salary_disclosure_2015 over `Calendar Year`; structural breaks?
- Concentration in `Last Name` — which actors dominate? (join entity spine)

_profiled 2026-09-09 · `python3 tools/profile.py ontario_public_sector_salary_disclosure_2015`_
