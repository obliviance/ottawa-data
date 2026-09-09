# Beaches

`open_beaches` · shape **arcgis-hub** · source `open-ottawa`

- origin: <https://open.ottawa.ca/datasets/ottawa::beaches>
- fetched 2026-09-09 · **4 rows** · 25 columns
- csv · licence: https://ottawa.ca/en/city-hall/get-know-your-city/open-data#open-data-licence-ve

## Columns

| column | kind | non-null | distinct | summary |
| --- | --- | --- | --- | --- |
| `X` | num | 100% | 4 | -8,438,186 · p25 -8,434,826 · p50 -8,429,888 · p95 -8,406,692 · max -8,403,272  █▁█▁▁█▁▁▁▁▁▁▁▁▁█ |
| `Y` | num | 100% | 4 | 5,679,179 · p25 5,679,389 · p50 5,681,722 · p95 5,698,947 · max 5,701,587  █▁▁▄▁▁▁▁▁▁▁▁▁▁▁▄ |
| `OBJECTID` | num | 100% | 4 | 1.00 · p25 1.75 · p50 2.50 · p95 3.85 · max 4.00  █▁▁▁▁█▁▁▁▁█▁▁▁▁█ |
| `FACILITYID` | num | 100% | 4 | 36,110 · p25 36,111 · p50 36,112 · p95 36,113 · max 36,113  █▁▁▁▁█▁▁▁▁█▁▁▁▁█ |
| `NAME` | cat | 100% | 4 | Westboro Beach 25%, Britannia Beach 25%, Petrie Island East Bay B 25%, Mooney's Bay Beach 25% |
| `NAME_FR` | cat | 100% | 4 | Plage Westboro 25%, Plage Britannia 25%, Petrie Baie de l'est 25%, Plage de Mooney’s Bay 25% |
| `ADDRESS` | cat | 100% | 4 | 234 Atlantis Avenue 25%, 102 Greenview Road 25%, 777 Tweddle Road 25%, 2960 Riverside Drive 25% |
| `ADDRESS_FR` | cat | 100% | 4 | 234, avenue Atlantis 25%, 102, chemin Greenview 25%, 777, chemin Tweddle 25%, 2960, promenade Riversid 25% |
| `BEACH_TYPE` | cat | 100% | 1 | Beach 100% |
| `BEACH_TYPE_FR` | cat | 100% | 1 | Plage 100% |
| `ACCESSIBLE` | text | 0% | 0 | e.g.  |
| `OPEN` | cat | 100% | 1 | no/non 100% |
| `MODIFIED_DATE` | date | 100% | 4 | 2022-06-17 → 2022-08-29, 1 gaps >30d |
| `CREATED_DATE` | text | 0% | 0 | e.g.  |
| `LINK` | cat | 100% | 1 | http://ottawa.ca/en/beac 100% |
| `LINK_FR` | cat | 100% | 1 | http://ottawa.ca/fr/plag 100% |
| `LINK_LABEL` | cat | 100% | 1 | Beaches 100% |
| `LINK_LABEL_FR` | cat | 100% | 1 | Plages 100% |
| `LINK_DESCRIPTION` | text | 0% | 0 | e.g.  |
| `LINK_DESCRIPTION_FR` | text | 0% | 0 | e.g.  |
| `PARK_ID` | num | 100% | 4 | 182 · p25 750 · p50 1,273 · p95 1,682 · max 1,696  ▄▁▁▁▁▁▁▁▄▁▁▁▁▁▁█ |
| `PARKNAME` | cat | 100% | 4 | Westboro Beach 25%, Britannia Park 25%, Stuemer Park 25%, Mooney's Bay Park 25% |
| `PARKNAME_FR` | cat | 100% | 4 | Plage Westboro 25%, Parc Britannia 25%, Parc Stuemer 25%, Parc Mooney's Bay 25% |
| `PARKADDRESS` | cat | 100% | 4 | 745 Sir John A. MacDonal 25%, 2805 Carling Avenue 25%, 777 Tweddle Road, Cumber 25%, 2960 Riverside Drive, Ot 25% |
| `PARKADDRESS_FR` | cat | 100% | 4 | 745, promenade de Sir-Jo 25%, 2805 avenue Carling 25%, 777, chemin Tweddle, Cum 25%, 2960, promenade Riversid 25% |

## Candidate questions

- (none templated)

_profiled 2026-09-09 · `python3 tools/profile.py open_beaches`_
