# City Council Meeting Attendance 2022-2026

`open_city_council_meeting_attendance_2022_2026` · shape **arcgis-hub** · source `open-ottawa`

- origin: <https://open.ottawa.ca/datasets/ottawa::city-council-meeting-attendance-2022-2026>
- fetched 2026-09-09 · **936 rows** · 8 columns
- csv · licence: https://ottawa.ca/en/city-hall/open-transparent-and-accountable-government/open-

## Columns

| column | kind | non-null | distinct | summary |
| --- | --- | --- | --- | --- |
| `OBJECTID` | num | 100% | 936 | 1.00 · p25 235 · p50 468 · p95 889 · max 936  █▇█▇█▇█▇▇█▇█▇█▇█ |
| `council_term` | cat | 100% | 1 | 2022-2026 100% |
| `meeting_type` | cat | 100% | 1 | City Council 100% |
| `meeting_date` | date | 100% | 39 | 2024-10-02 → 2026-06-10, 3 gaps >30d |
| `meeting_time` | date | 100% | 4 | 2026-09-09 → 2026-09-09 |
| `meeting_datetime` | date | 100% | 39 | 2024-10-02 → 2026-06-10, 3 gaps >30d |
| `attendees_present` | text | 100% | 26 | e.g. Mayor Mark Sutcliffe, Councillor Matt Luloff, Councillor Laura Dudas |
| `uuid` | text | 100% | 39 | e.g. 534308ac-8f54-4e99-a7e, a2eae498-343f-4085-b82, 3efcc478-d9c4-4d92-a0f |

## Candidate questions

- Trend / seasonality of open_city_council_meeting_attendance_2022_2026 over `meeting_date`; structural breaks?

_profiled 2026-09-09 · `python3 tools/profile.py open_city_council_meeting_attendance_2022_2026`_
