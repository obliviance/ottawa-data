# howtheyvoted — councillors

`htv_councillors` · shape **json-api** · source `howtheyvoted`

- origin: <https://howtheyvoted.ca/>
- fetched 2026-09-09 · **25 rows** · 9 columns

## Columns

| column | kind | non-null | distinct | summary |
| --- | --- | --- | --- | --- |
| `slug` | cat | 100% | 25 | mark-sutcliffe 4%, matthew-luloff 4%, laura-dudas 4%, david-hill 4%, cathy-curry 4%, clarke-kelly 4% |
| `full_name` | cat | 100% | 25 | Mark Sutcliffe 4%, Matthew Luloff 4%, Laura Dudas 4%, David Hill 4%, Cathy Curry 4%, Clarke Kelly 4% |
| `first_name_initial` | cat | 100% | 25 | M. Sutcliffe 4%, M. Luloff 4%, L. Dudas 4%, D. Hill 4%, C. Curry 4%, C. Kelly 4% |
| `title` | cat | 100% | 3 | Councillor 92%, Mayor 4%, Councillor and Deputy Ma 4% |
| `ward_number` | num | 100% | 25 | 1.00 · p25 6.75 · p50 12.50 · p95 22.85 · max 24.00  █▄█▄█▄█▄▄█▄█▄█▄█ |
| `ward_name` | cat | 100% | 25 |  4%, Orléans East-Cumberland 4%, Orléans West-Innes 4%, Barrhaven West 4%, Kanata North 4%, West Carleton-March 4% |
| `email` | cat | 100% | 25 | mark.sutcliffe@ottawa.ca 4%, matt.luloff@ottawa.ca 4%, laura.dudas@ottawa.ca 4%, david.hill@ottawa.ca 4%, cathy.curry@ottawa.ca 4%, clarke.kelly@ottawa.ca 4% |
| `telephone` | cat | 100% | 25 | 613-580-2496 4%, 613-580-2471 4%, 613-580-2472 4%, 613-580-2473 4%, 613-580-2474 4%, 613-580-2475 4% |
| `active` | cat | 100% | 1 | True 100% |

## Candidate questions

- (none templated)

_profiled 2026-09-09 · `python3 tools/profile.py htv_councillors`_
