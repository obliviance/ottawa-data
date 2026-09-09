# Outdoor Pools

`open_outdoor_pools` · shape **arcgis-hub** · source `open-ottawa`

- origin: <https://open.ottawa.ca/datasets/ottawa::outdoor-pools>
- fetched 2026-09-09 · **11 rows** · 23 columns
- csv · licence: https://ottawa.ca/en/city-hall/get-know-your-city/open-data#open-data-licence-ve

## Columns

| column | kind | non-null | distinct | summary |
| --- | --- | --- | --- | --- |
| `X` | num | 100% | 11 | -8,449,293 · p25 -8,444,247 · p50 -8,431,113 · p95 -8,417,581 · max -8,411,698  █▁▁▅▁▁▁▃▃▁█▁▁▁▁▃ |
| `Y` | num | 100% | 11 | 5,657,945 · p25 5,669,327 · p50 5,673,439 · p95 5,690,784 · max 5,691,404  █▁▁▁▄▁▄██▄▁▁▁▁▁█ |
| `OBJECTID` | num | 100% | 11 | 1.00 · p25 3.50 · p50 6.00 · p95 10.50 · max 11.00  ██▁██▁██▁█▁██▁██ |
| `PARK_ID` | num | 100% | 10 | 234 · p25 322 · p50 514 · p95 1,366 · max 1,700  █▅▁▃▁▃▁▁█▁▁▁▁▁▁▃ |
| `FACILITYID` | num | 100% | 11 | 7,054 · p25 7,240 · p50 26,069 · p95 31,212 · max 36,164  ▅▁▁▁▁▁▁▁▁▁█▁▁▁▁▂ |
| `NAME` | cat | 100% | 10 | Long Island Aquatic Club 18%, Entrance Outdoor Pool 9%, Katimavik Outdoor Pool 9%, Beaverbrook Outdoor Pool 9%, Crestview Outdoor Pool 9%, Glen Cairn Outdoor Pool 9% |
| `NAME_FR` | cat | 100% | 10 | Club aquatique de Long I 18%, Piscine extérieure Entra 9%, Piscine extérieure Katim 9%, Piscine extérieure Beave 9%, Piscine extérieure Crest 9%, Piscine extérieure Glen  9% |
| `POOL_TYPE` | cat | 100% | 1 | full pool 100% |
| `POOL_TYPE_FR` | cat | 100% | 1 | piscine extérieure 100% |
| `ACCESSIBLE` | cat | 100% | 1 | no/non 100% |
| `OPEN` | cat | 100% | 1 | no/non 100% |
| `MODIFIED_DATE` | date | 100% | 11 | 2022-08-26 → 2022-09-06 |
| `CREATED_DATE` | text | 0% | 0 | e.g.  |
| `LINK` | cat | 100% | 3 | http://ottawa.ca/en/resi 73%, http://longislandaquatic 18%, http://ottawa.ca/en/resi 9% |
| `LINK_FR` | cat | 100% | 3 | http://ottawa.ca/fr/resi 73%, http://longislandaquatic 18%, http://ottawa.ca/fr/resi 9% |
| `LINK_LABEL` | cat | 100% | 1 | Outdoor Pools 100% |
| `LINK_LABEL_FR` | cat | 100% | 1 | Piscines extérieures 100% |
| `LINK_DESCRIPTION` | text | 0% | 0 | e.g.  |
| `LINK_DESCRIPTION_FR` | text | 0% | 0 | e.g.  |
| `PARKNAME` | cat | 100% | 10 | Long Island Aquatic Club 18%, Entrance Park 9%, Cattail Creek Park 9%, Beaverbrook Pool Park 9%, Bob Mitchell Park 9%, Beaton Park 9% |
| `PARKNAME_FR` | cat | 100% | 10 | Club Aquatique Long Isla 18%, Parc Entrance 9%, Parc Cattail Creek 9%, Parc Beaverbrook Pool 9%, Parc Bob-Mitchell 9%, Parc Beaton 9% |
| `PARKADDRESS` | cat | 100% | 10 | 5495 South River Drive,  18%, 2 Eaton Street, Nepean 9%, 38 Chimo Drive, Kanata 9%, 1002 Beaverbrook Road, K 9%, 58 Fieldrow Street, Nepe 9%, 70 Castlefrank Road, Kan 9% |
| `PARKADDRESS_FR` | cat | 100% | 10 | 5495, promenade South Ri 18%, 2, rue Eaton, Nepean 9%, 38, promenade Chimo, Kan 9%, 1002, chemin Beaverbrook 9%, 58, rue Fieldrow, Nepean 9%, 70, chemin Castlefrank,  9% |

## Candidate questions

- (none templated)

_profiled 2026-09-09 · `python3 tools/profile.py open_outdoor_pools`_
