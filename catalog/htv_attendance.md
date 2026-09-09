# howtheyvoted — attendance

`htv_attendance` · shape **json-api** · source `howtheyvoted`

- origin: <https://howtheyvoted.ca/>
- fetched 2026-09-09 · **6,132 rows** · 3 columns

## Columns

| column | kind | non-null | distinct | summary |
| --- | --- | --- | --- | --- |
| `meeting_id` | text | 100% | 569 | e.g. 8bb828f4-1807-4a03-982, 52bf58a6-97a9-4392-8af, d5a96450-49d1-4b4e-a4d |
| `councillor_name` | text | 100% | 222 | e.g. Allan Hubley, Cathy Curry, Chair: Mayor Jim Watso |
| `status` | cat | 100% | 2 | present 92%, absent 8% |

## Candidate questions

- (none templated)

_profiled 2026-09-09 · `python3 tools/profile.py htv_attendance`_
