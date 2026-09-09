# howtheyvoted — votes

`htv_votes` · shape **json-api** · source `howtheyvoted`

- origin: <https://howtheyvoted.ca/>
- fetched 2026-09-09 · **6,374 rows** · 5 columns

## Columns

| column | kind | non-null | distinct | summary |
| --- | --- | --- | --- | --- |
| `motion_id` | text | 100% | 338 | e.g. 41a66bc3f93fb4f9b3e056, 2d084a8bbcd9fc5061bea4, b8a962b925b6b6ed2aff6c |
| `meeting_id` | text | 100% | 145 | e.g. c84c9326-a0ec-4936-b0f, 41eba6be-95f2-4a0b-a94, b9ee9522-a44c-4c63-8d3 |
| `meeting_date` | date | 100% | 145 | 2022-11-09 → 2026-09-02, 9 gaps >30d |
| `councillor_name` | text | 100% | 87 | e.g. A. Hubley, C. Curry, C. Kitts |
| `vote` | cat | 100% | 2 | for 63%, against 37% |

## Candidate questions

- Trend / seasonality of htv_votes over `meeting_date`; structural breaks?

_profiled 2026-09-09 · `python3 tools/profile.py htv_votes`_
