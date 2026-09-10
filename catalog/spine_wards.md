# spine — Ottawa wards (24, current)

`spine_wards` · shape **spine**

- origin: <https://open.ottawa.ca/datasets/ottawa::2022-elections-voting-subdivision-map>
- fetched 2026-09-09 · **24 rows** · 5 columns
- dissolved from the 2022 election voting-subdivision map; geometry as WKT

## Columns

| column | kind | non-null | distinct | summary |
| --- | --- | --- | --- | --- |
| `ward_num` | num | 100% | 24 | 1.00 · p25 6.75 · p50 12.50 · p95 22.85 · max 24.00  █▄█▄█▄█▄▄█▄█▄█▄█ |
| `ward_name` | cat | 100% | 24 | Orléans East-Cumberland 4%, Orléans West-Innes 4%, Barrhaven West 4%, Kanata North 4%, West Carleton-March 4%, Stittsville 4% |
| `ward_name_fr` | cat | 100% | 24 | Orléans-Est-Cumberland 4%, Orléans-Ouest-Innes 4%, Barrhaven-Quest 4%, Kanata-Nord 4%, West Carleton-March 4%, Stittsville 4% |
| `voting_subdivisions` | num | 100% | 20 | 31.00 · p25 43.75 · p50 48.50 · p95 67.25 · max 69.00  ▂▂▂▂▂▃▅█▃▃▂▁▂▂▁▃ |
| `geometry_wkt` | cat | 100% | 24 | POLYGON ((-75.4923091671 4%, POLYGON ((-75.5690971210 4%, POLYGON ((-75.7463906642 4%, POLYGON ((-75.9385103861 4%, POLYGON ((-76.0161211849 4%, POLYGON ((-75.9296227930 4% |

## Candidate questions

- (none templated)

_profiled 2026-09-09 · `python3 tools/profile.py spine_wards`_
