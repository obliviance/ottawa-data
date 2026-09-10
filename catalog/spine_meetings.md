# spine — meetings (eScribe calendar)

`spine_meetings` · shape **spine**

- origin: <https://pub-ottawa.escribemeetings.com/>
- fetched 2026-09-09 · **2,071 rows** · 7 columns
- eScribe calendar; in_howtheyvoted flags meetings with a parsed agenda

## Columns

| column | kind | non-null | distinct | summary |
| --- | --- | --- | --- | --- |
| `meeting_id` | id/text | 100% | 2,071 | e.g. bc6f7f8a-957b-151a-396, 38c3cb4a-42e4-2561-325, 65235af4-5e30-252a-3a3 |
| `meeting_name` | text | 100% | 68 | e.g. City Council, Committee of Adjustmen, Committee of Adjustmen |
| `start` | date | 100% | 1,965 | 2019-01-07 → 2026-09-29 |
| `location` | cat | 100% | 21 | Electronic Participation 43%, Champlain Room, 110 Laur 20%, Ben Franklin Place, The  12%, Champlain Room, 110 Laur 9%, Andrew S. Haydon Hall, 1 8%, The Chamber, 101 Centrep 4% |
| `url` | text | 0% | 0 | e.g.  |
| `date` | date | 100% | 1,161 | 2019-01-07 → 2026-09-29 |
| `in_howtheyvoted` | cat | 100% | 2 | False 71%, True 29% |

## Candidate questions

- Trend / seasonality of spine_meetings over `date`; structural breaks?

_profiled 2026-09-09 · `python3 tools/profile.py spine_meetings`_
