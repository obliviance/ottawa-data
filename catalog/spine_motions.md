# spine — council/committee motions (2022→)

`spine_motions` · shape **spine**

- origin: <https://howtheyvoted.ca/>
- fetched 2026-09-09 · **7,621 rows** · 13 columns
- from howtheyvoted; site terms, not open data

## Columns

| column | kind | non-null | distinct | summary |
| --- | --- | --- | --- | --- |
| `date` | date | 100% | 508 | 2022-11-01 → 2026-09-03 |
| `meeting_name` | text | 100% | 37 | e.g. Finance and Economic D, Agriculture and Rural , Board of Health |
| `agenda_item_number` | num | 100% | 563 | 1.00 · p25 5.10 · p50 8.11 · p95 24.00 · max 46.00  ▃█▅▃▂▂▂▂▁▁▁▁▁▁▁▁ |
| `agenda_item_title` | text | 100% | 3,829 | e.g. Motion – Waive the Dis, FEDC Minutes 41 – June, Quarterly Stage 2 LRT  |
| `motion_id` | id/text | 100% | 7,621 | e.g. 6caaae44a1a53b8ef71842, bd72a5adc1feb623cec20b, 42bd6250f865fb8c5b02b8 |
| `motion_text` | text | 100% | 4,600 | e.g. That the Finance and E, During the consent por,  |
| `motion_moved_by` | text | 100% | 68 | e.g. , G. Gower, J. Cloutier |
| `motion_seconded_by` | text | 100% | 31 | e.g. , K. Egli, C. Curry |
| `result` | text | 89% | 149 | e.g. Carried as amended, Carried, Received |
| `for_count` | num | 100% | 26 | 0.00 · p25 0.00 · p50 0.00 · p95 0.00 · max 25.00  █▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁ |
| `against_count` | num | 100% | 24 | 0.00 · p25 0.00 · p50 0.00 · p95 0.00 · max 23.00  █▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁ |
| `vote_kind` | cat | 100% | 3 | none 96%, recorded 4%, dissent 0% |
| `summary` | id/text | 100% | 6,786 | e.g. Council is being asked, Council is waiving its,  |

## Candidate questions

- Trend / seasonality of spine_motions over `date`; structural breaks?

_profiled 2026-09-09 · `python3 tools/profile.py spine_motions`_
