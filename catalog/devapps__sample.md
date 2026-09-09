# Development Applications — API sample

`devapps__sample` · shape **json-api** · source `devapps`

- origin: <https://devapps-restapi.ottawa.ca/devapps/feature/all>
- fetched 2026-09-09 · **10 rows** · 21 columns
- first 10 of 813 dev-app features; authKey is client-embedded

## Columns

| column | kind | non-null | distinct | summary |
| --- | --- | --- | --- | --- |
| `id` | text | 0% | 0 | e.g.  |
| `properties.devAppId` | cat | 100% | 7 | __01Q03N 20%, __06TITQ 20%, __0R1RYS 20%, __01OAMK 10%, __0FJHE4 10%, __0FUCIK 10% |
| `properties.applicationNumber` | cat | 100% | 7 | D07-12-16-0002 20%, D07-12-16-0052 20%, D07-12-15-0117 20%, D07-16-15-0015 10%, D01-01-16-0022 10%, D02-02-16-0114 10% |
| `properties.applicationStatus.en` | cat | 100% | 2 | File Pending 90%, Active 10% |
| `properties.applicationStatus.fr` | cat | 100% | 2 | Dossier en cours 90%, Actif 10% |
| `properties.devAppAddress.addressReferenceId` | cat | 100% | 10 | __01OAP1 10%, __01Q09K 10%, __01Q08B 10%, __A1MJP2 10%, __06TIYR 10%, __0FJINM 10% |
| `properties.devAppAddress.addressNumber` | num | 100% | 9 | 137 · p25 377 · p50 507 · p95 1,243 · max 1,626  ▃▃▃▅█▁▃▁▁▁▁▁▁▁▁▃ |
| `properties.devAppAddress.addressQualifier` | cat | 100% | 1 |  100% |
| `properties.devAppAddress.legalUnit` | cat | 100% | 1 |  100% |
| `properties.devAppAddress.roadName` | cat | 100% | 8 | RIDEAU 20%, TERRY FOX 20%, OLD PRESCOTT 10%, BRONSON 10%, CAMBRIDGE 10%, GOULBOURN FORCED 10% |
| `properties.devAppAddress.cardinalDirection` | cat | 100% | 2 |  90%, SOUTH 10% |
| `properties.devAppAddress.roadType` | cat | 100% | 4 | Street 50%, Road 20%, Drive 20%, Avenue 10% |
| `properties.devAppAddress.municipality` | cat | 100% | 3 | Old Ottawa 60%, Kanata 30%, Osgoode 10% |
| `properties.devAppAddress.addressType` | cat | 100% | 2 | MAIN 90%, SUBORD 10% |
| `properties.devAppAddress.addressLatitude` | num | 100% | 8 | 45.25 · p25 45.33 · p50 45.40 · p95 45.43 · max 45.43  ▄▁▁▁▁▁█▄▁▁▁▁▁███ |
| `properties.devAppAddress.addressLongitude` | num | 100% | 8 | -75.95 · p25 -75.87 · p50 -75.70 · p95 -75.62 · max -75.57  ▆▁▁▁▁▁▁▁▁▁█▄▁▁▁▂ |
| `properties.devAppAddress.addressNumberRoadName` | cat | 100% | 9 | 457 TERRY FOX 20%, 1626 OLD PRESCOTT 10%, 774 BRONSON 10%, 557 CAMBRIDGE 10%, 590 RIDEAU 10%, 594 RIDEAU 10% |
| `properties.devAppAddress.parcelPinNumber` | num | 100% | 8 | 41,030,125 · p25 41,140,002 · p50 42,070,667 · p95 45,241,941 · max 45,241,941  █▁▁▄▁▁▁▁▂▁▁▁▁▁▁▆ |
| `properties.applicationType.en` | cat | 100% | 4 | Site Plan Control 60%, Plan of Subdivision 20%, Official Plan Amendment 10%, Zoning By-law Amendment 10% |
| `properties.applicationType.fr` | cat | 100% | 4 | Réglementation du plan d 60%, Plan de lotissement 20%, Modification au Plan off 10%, Modification au Règlemen 10% |
| `geometry.coordinates` | cat | 100% | 8 | [-75.675689  45.432672] 20%, [-75.946851  45.326257] 20%, [-75.57001   45.247909] 10%, [-75.69976   45.400366] 10%, [-75.700261  45.400152] 10%, [-75.926119  45.331481] 10% |

## Candidate questions

- (none templated)

_profiled 2026-09-09 · `python3 tools/profile.py devapps__sample`_
