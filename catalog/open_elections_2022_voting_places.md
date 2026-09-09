# Elections 2022 – Voting Places

`open_elections_2022_voting_places` · shape **arcgis-hub** · source `open-ottawa`

- origin: <https://open.ottawa.ca/datasets/ottawa::elections-2022-voting-places>
- fetched 2026-09-09 · **680 rows** · 17 columns
- csv · licence: https://ottawa.ca/en/city-hall/get-know-your-city/open-data#open-data-licence-ve

## Columns

| column | kind | non-null | distinct | summary |
| --- | --- | --- | --- | --- |
| `Ward_Quartier` | num | 100% | 25 | 1.00 · p25 7.00 · p50 13.00 · p95 99.00 · max 99.00  ▇█▇▄▁▁▁▁▁▁▁▁▁▁▁▂ |
| `Day` | cat | 100% | 8 | Voting Day 53%, Adv Day 2 21%, Adv Day 1 21%, Special Adv 1 1%, Special Adv 2 1%, Special Adv 3 1% |
| `Jour` | cat | 99% | 7 | Jour du scrutin 53%, Ant jr 2 21%, Ant jr 1 21%, ant spc jr 1 1%, ant spc jr 2 1%, ant spc jr 3 1% |
| `Area_Section_de_vote` | num | 100% | 34 | 1.00 · p25 3.00 · p50 7.00 · p95 22.05 · max 34.00  █▄▄▃▃▃▂▁▁▁▁▁▁▁▁▁ |
| `Name` | id/text | 100% | 582 | e.g. Cobalt, The Orion, C.C.C. #8 |
| `Nom` | id/text | 100% | 582 | e.g. Cobalt, The Orion, C.C.C. #8 |
| `ADDRESS` | id/text | 100% | 583 | e.g. 90 Woodridge Cres, 25 Woodridge Cres, 3100 Carling Ave |
| `Adresse` | id/text | 100% | 582 | e.g. 90 Crois. Woodridge, 25 Crois. Woodridge, 3100 Av. Carling |
| `Intersection` | text | 100% | 526 | e.g. Woodridge Cres @ Baysh, Carling Ave @ Bayshore, Richmond Rd @ High St |
| `Intersection_FR` | text | 100% | 527 | e.g. crois. Woodridge @ pro, av. Carling @ prom. Ba, ch. Richmond @ rue Hig |
| `Accessible_Entrance` | text | 100% | 56 | e.g. Back Entrance, Main Entrance, Back Accessible Entran |
| `Entrée_accessible` | text | 100% | 56 | e.g. Entrée arrière, Entrée principale, Entrée accessible situ |
| `Hours` | cat | 100% | 8 | 10 am to 8 pm 88%, 10 am to 2 pm 6%, 4 pm to 8 pm 6%, Entrée principale 0%,  boul. St-Laurent" 0%,  prom. Brittany" 0% |
| `Heures` | cat | 100% | 6 | de 10 h à 20 h 88%, de 10 h à 14 h 6%, de 16 h à 20 h 6%, 10 am to 8 pm 0%, Entrée principale 0%,  Porte ""D""" 0% |
| `X` | num | 98% | 569 | -76.21 · p25 -75.77 · p50 -75.69 · p95 -75.47 · max -75.34  ▁▁▁▁▁▃▁▄▅█▆▂▂▂▁▁ |
| `Y` | num | 99% | 572 | -75.65 · p25 45.34 · p50 45.38 · p95 45.47 · max 45.52  ▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁█ |
| `ObjectId` | num | 100% | 680 | 1.00 · p25 171 · p50 340 · p95 646 · max 680  █▇█▇█▇█▇▇█▇█▇█▇█ |

## Candidate questions

- (none templated)

_profiled 2026-09-09 · `python3 tools/profile.py open_elections_2022_voting_places`_
