#  Elected Officials 2022-2026

`open_elected_officials_2022_2026` · shape **arcgis-hub** · source `open-ottawa`

- origin: <https://open.ottawa.ca/datasets/ottawa::-elected-officials-2022-2026>
- fetched 2026-09-09 · **26 rows** · 17 columns
- csv · licence: https://ottawa.ca/en/city-hall/open-transparent-and-accountable-government/open-

## Columns

| column | kind | non-null | distinct | summary |
| --- | --- | --- | --- | --- |
| `Ward_name` | cat | 96% | 25 | Orléans East-Cumberland 4%, Orléans West-Innes 4%, Barrhaven West 4%, Kanata North 4%, West Carleton-March 4%, Stittsville 4% |
| `Ward_number` | num | 96% | 24 | 1.00 · p25 7.00 · p50 13.00 · p95 22.80 · max 24.00  ▅▃▅▃▅▃▅▃▃▅▃▅▃█▃▅ |
| `Primary_Role` | cat | 100% | 2 | Councillor 96%, Mayor 4% |
| `First_name` | cat | 100% | 25 | David 8%, Mark 4%, Matthew 4%, Laura 4%, Cathy  4%, Clarke 4% |
| `Last_name` | id/text | 100% | 26 | e.g. Sutcliffe, Luloff, Dudas |
| `Email` | id/text | 100% | 26 | e.g. Mark.Sutcliffe@ottawa., Matt.Luloff@ottawa.ca, Laura.Dudas@ottawa.ca |
| `Source_URL` | id/text | 100% | 26 | e.g. https://ottawa.ca/en/c, https://ottawa.ca/en/c, https://ottawa.ca/en/c |
| `Photo_URL` | id/text | 100% | 26 | e.g. https://ottawa.ca/site, https://ottawa.ca/site, https://ottawa.ca/site |
| `Website` | cat | 92% | 24 | https://marksutcliffe.ca 4%, https://matthewluloff.ca 4%, https://lauradudas.ca/ 4%, https://www.davidhillbar 4%, https://www.kanatanorth. 4%, https://www.clarkekelly. 4% |
| `Address_line_1` | cat | 100% | 2 | 110 Laurier Avenue West 96%, 111 Laurier Avenue West 4% |
| `Address_line_2` | text | 0% | 0 | e.g.  |
| `City` | cat | 100% | 1 | Ottawa 100% |
| `Postal_code` | cat | 100% | 2 | K1P 1J1 96%, K1P 1J2 4% |
| `Province` | cat | 100% | 1 | ON 100% |
| `Phone` | cat | 100% | 25 | 613-580-2490 8%, 613-580-2496 4%, 613-580-2471 4%, 613-580-2472 4%, 613-580-2473 4%, 613-580-2474 4% |
| `Fax` | cat | 92% | 24 | 613-580-2509 4%, 613-580-2511 4%, 613-580-2512 4%, 613-580-2513 4%, 613-580-2514 4%, 613-580-2515 4% |
| `ObjectId` | num | 100% | 26 | 1.00 · p25 7.25 · p50 13.50 · p95 24.75 · max 26.00  ██▄█▄█▄██▄█▄█▄██ |

## Candidate questions

- (none templated)

_profiled 2026-09-09 · `python3 tools/profile.py open_elected_officials_2022_2026`_
