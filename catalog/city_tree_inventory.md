# City of Ottawa — tree inventory (Forestry MapServer layer 0)

`city_tree_inventory` · shape **arcgis-hub** · source `trees-parks` · **spatial**

- origin: <https://maps.ottawa.ca/arcgis/rest/services/Forestry/MapServer/0>
- fetched 2026-10-24 · **304,208 rows** · 52 columns
- paged by OBJECTID via arcgis_layers.py; 304,208 rows

## Columns

| column | kind | non-null | distinct | summary |
| --- | --- | --- | --- | --- |
| `OBJECTID` | num | 100% | 304,208 | 63,893 · p25 166,971 · p50 288,790 · p95 551,099 · max 569,687  ▆▆▆▆▆▄▅▃▂▄▂▂▅▇█▇ |
| `TREEID` | id/text | 100% | 304,208 | e.g. 3A7D3E54-48D8-5A10-227, 007007D3-7823-F6A9-17C, 40BBA7B7-565F-AFC7-3BD |
| `DISRDCEN` | num | 38% | 2,029 | 0.00 · p25 0.00 · p50 0.00 · p95 0.00 · max 13.80  █▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁ |
| `WARD` | num | 99% | 24 | 1.00 · p25 6.00 · p50 13.00 · p95 24.00 · max 24.00  ▅▄▇▃▆▃▅▂▃▄▃▆▄▇▃█ |
| `ADDNUM` | num | 99% | 7,261 | 0.00 · p25 100 · p50 512 · p95 6,018 · max 8,359,202  █▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁ |
| `ADDSTR` | text | 99% | 7,050 | e.g. CHAPEL ST, ST. ANDREW ST, BOLTON ST |
| `LTLOCATION` | cat | 73% | 7 | Front 71%, Side 16%, Rear 6%, N/A 4%, Oppos 3%, Boul 0% |
| `RDLOCATION` | cat | 58% | 5 | N/A 65%, Boulevard 34%, CenterMed 1%, Median 0%, 0 0% |
| `OWNERSHIP` | cat | 100% | 2 | City 97%, Joint 3% |
| `PARK` | num | 100% | 2 | -1.00 · p25 -1.00 · p50 0.00 · p95 0.00 · max 0.00  ▃▁▁▁▁▁▁▁▁▁▁▁▁▁▁█ |
| `FACILITY` | num | 69% | 2 | -1.00 · p25 0.00 · p50 0.00 · p95 0.00 · max 0.00  ▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁█ |
| `MUNATAREA` | num | 68% | 2 | -1.00 · p25 0.00 · p50 0.00 · p95 0.00 · max 0.00  ▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁█ |
| `EDGETREE` | num | 69% | 2 | -1.00 · p25 0.00 · p50 0.00 · p95 0.00 · max 0.00  ▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁█ |
| `PATHTRAIL` | num | 69% | 2 | -1.00 · p25 0.00 · p50 0.00 · p95 0.00 · max 0.00  ▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁█ |
| `SPECIES` | text | 100% | 169 | e.g. Elm Siberian, Lilac Japanese, Maple Norway |
| `DBH` | num | 99% | 170 | 1.00 · p25 6.00 · p50 15.00 · p95 57.00 · max 200  █▄▃▂▁▁▁▁▁▁▁▁▁▁▁▁ |
| `PLNTDATE` | date | 15% | 45,452 | 1970-01-01 → 1970-01-01 |
| `REPLANT` | cat | 18% | 6 | N/A 67%, Replacement 25%, No 4%, 0 2%, Underplanting 1%, Interplanting 1% |
| `UTILITIES` | cat | 92% | 6 | N/A 93%, Hydro 6%, Bell/Cable 1%, Cable 0%, Bell 0%, TGHydro 0% |
| `HSURFACE` | num | 73% | 2 | -1.00 · p25 0.00 · p50 0.00 · p95 0.00 · max 0.00  ▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁█ |
| `SSUPPORT` | num | 70% | 2 | -1.00 · p25 0.00 · p50 0.00 · p95 0.00 · max 0.00  ▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁█ |
| `TRGUARD` | num | 74% | 2 | -1.00 · p25 0.00 · p50 0.00 · p95 0.00 · max 0.00  ▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁█ |
| `GRATE` | num | 73% | 2 | -1.00 · p25 0.00 · p50 0.00 · p95 0.00 · max 0.00  ▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁█ |
| `PLANTER` | num | 73% | 17 | -1.00 · p25 0.00 · p50 0.00 · p95 0.00 · max 4,074  █▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁ |
| `STAKED` | num | 74% | 2 | -1.00 · p25 0.00 · p50 0.00 · p95 0.00 · max 0.00  ▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁█ |
| `WTUBES` | num | 75% | 2 | -1.00 · p25 0.00 · p50 0.00 · p95 0.00 · max 0.00  ▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁█ |
| `FOUNDCLAIMFILE` | num | 63% | 2 | -1.00 · p25 0.00 · p50 0.00 · p95 0.00 · max 0.00  ▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁█ |
| `TNOTES` | text | 46% | 17,586 | e.g. 20-50cm, Updated species and si, Dead End Bolton St |
| `CREATEDATE` | date | 94% | 144,596 | 1970-01-01 → 1970-01-01 |
| `MODIFYDATE` | date | 99% | 73,854 | 1970-01-01 → 1970-01-01 |
| `PROBENTRY` | num | 53% | 2 | -1.00 · p25 0.00 · p50 0.00 · p95 0.00 · max 0.00  ▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁█ |
| `X_COORD` | num | 100% | 302,480 | 0.00 · p25 360,030 · p50 366,739 · p95 385,876 · max 460,324  ▁▁▁▁▁▁▁▁▁▁▁▁█▂▁▁ |
| `Y_COORD` | num | 99% | 302,272 | 0.00 · p25 5,016,038 · p50 5,024,296 · p95 5,037,173 · max 5,043,080  ▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁█ |
| `COMTREE` | num | 46% | 2 | -1.00 · p25 0.00 · p50 0.00 · p95 0.00 · max 0.00  ▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁█ |
| `LEGACYID` | cat | 26% | 3 |   98%, 0 2%, Null 0% |
| `TRUNCSTRCT` | cat | 99% | 4 | S 90%, M 9%, H 1%, T 0% |
| `STATUS` | cat | 100% | 1 | Active 100% |
| `TREESEQID` | num | 26% | 5,026 | 0.00 · p25 139 · p50 388 · p95 3,455 · max 5,043  █▃▂▁▁▁▁▁▁▁▁▁▁▁▁▁ |
| `TREATMENT` | cat | 0% | 6 | EAB 76%, DED2 11%, LDD 10%, DED1 2%,   0%, 0 0% |
| `NEAR_FID` | num | 30% | 1,057 | -1.00 · p25 0.00 · p50 0.00 · p95 37,146,614 · max 37,156,288  █▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁ |
| `NEAR_DIST` | num | 30% | 8,536 | -1.00 · p25 0.00 · p50 0.00 · p95 2.88 · max 18.44  █▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁ |
| `STREET` | text | 57% | 8,946 | e.g. CHAPEL ST, ST. ANDREW ST, BOLTON ST |
| `TREATMENT_YEAR` | date | 0% | 249 | 1970-01-01 → 1970-01-01 |
| `EABTAGNUMBER` | num | 26% | 1,686 | 0.00 · p25 0.00 · p50 0.00 · p95 0.00 · max 9,999  █▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁ |
| `DEDTAGNUMBER` | num | 26% | 141 | 0.00 · p25 0.00 · p50 0.00 · p95 0.00 · max 3,999  █▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁ |
| `NOWUPLOAD` | num | 30% | 5 | -5.00 · p25 0.00 · p50 0.00 · p95 0.00 · max 0.00  ▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁█ |
| `SAP_ID` | num | 98% | 299,488 | 827,832 · p25 8,225,545 · p50 8,378,044 · p95 8,577,643 · max 820,002,285  █▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁ |
| `GLOBALID` | id/text | 100% | 304,208 | e.g. {D949A631-386E-43FD-8E, {507342CB-4505-4904-B8, {0B9C4B48-1178-4CFB-92 |
| `FLAG` | cat | 0% | 5 |   36%, R 35%, NoTree 16%, 0 8%, DR 4% |
| `PROGRAM` | cat | 40% | 10 | None 79%, TNT 11%, Parks 6%, Streetscape 2%, Commemorative 1%, ROW Replacement 0% |
| `longitude` | num | 100% | 303,897 | -76.34 · p25 -75.80 · p50 -75.71 · p95 -75.47 · max -75.26  ▁▁▁▁▁▁▄▂▅█▅▂▃▁▁▁ |
| `latitude` | num | 100% | 303,845 | 44.97 · p25 45.28 · p50 45.36 · p95 45.47 · max 45.52  ▁▁▁▁▁▁▁▂▇▅▅█▆▆▄▁ |

## Candidate questions

- `WARD` by `WARD` — equity gradient? (join ONS income)
- Trend / seasonality of city_tree_inventory over `PLNTDATE`; structural breaks?
- Spatial clustering of city_tree_inventory; overlay wards + the decision timeline

_profiled 2026-10-24 · `python3 tools/profile.py city_tree_inventory`_
