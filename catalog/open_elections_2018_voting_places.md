# Elections 2018  Voting Places

`open_elections_2018_voting_places` · shape **arcgis-hub** · source `open-ottawa`

- origin: <https://open.ottawa.ca/datasets/ottawa::elections-2018-voting-places-1>
- fetched 2026-09-09 · **642 rows** · 15 columns
- csv · licence: https://ottawa.ca/en/city-hall/get-know-your-city/open-data#open-data-licence-ve

## Columns

| column | kind | non-null | distinct | summary |
| --- | --- | --- | --- | --- |
| `Ward___Quartier` | num | 100% | 24 | 1.00 · p25 8.00 · p50 13.00 · p95 23.00 · max 99.00  ▆▇█▃▁▁▁▁▁▁▁▁▁▁▁▁ |
| `Day` | cat | 100% | 6 | Voting Day 55%, Adv Day 1 42%, Special Adv 1 1%, Special Adv 2 1%, Special Adv 3 1%, Special Adv 4 1% |
| `Jour` | cat | 96% | 2 | Jour du scrutin 57%, Ant jr 1 43% |
| `Area___Section_de_vote` | num | 100% | 29 | 1.00 · p25 4.00 · p50 8.00 · p95 21.00 · max 29.00  █▇▆▆▃▅▄▄▂▂▂▁▁▁▁▁ |
| `Name` | id/text | 100% | 565 | e.g. Eastern Ontario Christ, Arlington Woods Free M, Sir Robert Borden High |
| `Nom` | id/text | 100% | 565 | e.g. Eastern Ontario Christ, Arlington Woods Free M, Sir Robert Borden High |
| `Address` | id/text | 100% | 564 | e.g. 224 Viewmount Dr, 225 McClellan Rd, 131 Greenbank Rd |
| `Adresse` | id/text | 100% | 564 | e.g. 224 Prom Viewmount, 225 Ch McClellan, 131 Ch Greenbank |
| `ClosestIntersection` | id/text | 100% | 535 | e.g. Overlake Dr - Viewmoun, McClellan Rd @ Camwood, Greenbank Rd @ Banner  |
| `Intersection` | id/text | 99% | 531 | e.g. prom. Overlake- prom. , ch.McClellan @ crois. , ch. Greenbank @ ch. Ba |
| `AccessibleEntrance` | text | 100% | 39 | e.g. Main Entrance, Parking Lot Entrance, Merivale Rd Entrance |
| `Entrée_accessible` | text | 100% | 37 | e.g. Entrée principale, Entrée du stationnemen, Entrée du ch Merivale |
| `Hours` | cat | 100% | 3 | 10 a.m. to 8 p.m. 86%, 10 a.m. to 2 p.m. 7%, 4 p.m. to 8 p.m. 7% |
| `Heures` | cat | 100% | 3 | De 10 h à 20 h 86%, De 10 h à 14 h 7%, De 16 h à 20 h 7% |
| `FID` | num | 100% | 642 | 1.00 · p25 161 · p50 322 · p95 610 · max 642  █▇▇▇▇▇▇▇▇▇▇▇▇▇▇█ |

## Candidate questions

- (none templated)

_profiled 2026-09-09 · `python3 tools/profile.py open_elections_2018_voting_places`_
