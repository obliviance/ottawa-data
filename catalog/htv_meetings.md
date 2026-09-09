# howtheyvoted — meetings

`htv_meetings` · shape **json-api** · source `howtheyvoted`

- origin: <https://howtheyvoted.ca/>
- fetched 2026-09-09 · **612 rows** · 7 columns

## Columns

| column | kind | non-null | distinct | summary |
| --- | --- | --- | --- | --- |
| `meeting_id` | id/text | 100% | 612 | e.g. 8bb828f4-1807-4a03-982, 52bf58a6-97a9-4392-8af, d5a96450-49d1-4b4e-a4d |
| `meeting_name` | text | 100% | 37 | e.g. Finance and Economic D, Agriculture and Rural , Board of Health |
| `meeting_number` | num | 100% | 123 | 0.00 · p25 7.00 · p50 18.00 · p95 111 · max 132  █▅▄▃▂▁▁▁▁▁▁▁▁▁▁▁ |
| `meeting_date` | date | 100% | 508 | 2022-11-01 → 2026-09-03 |
| `start_time` | date | 100% | 23 | 2026-09-09 → 2026-09-09 |
| `location` | cat | 100% | 9 | Champlain Room, 110 Laur 46%, Andrew S. Haydon Hall, 1 24%, Electronic Participation 21%, Ben Franklin Place, The  6%, Andrew S. Haydon Hall, 1 1%, Colonel By Room, 110 Lau 1% |
| `source_url` | id/text | 100% | 612 | e.g. https://pub-ottawa.esc, https://pub-ottawa.esc, https://pub-ottawa.esc |

## Candidate questions

- Trend / seasonality of htv_meetings over `meeting_date`; structural breaks?

_profiled 2026-09-09 · `python3 tools/profile.py htv_meetings`_
