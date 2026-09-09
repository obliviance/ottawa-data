# Street Food Vendors 2020

`open_street_food_vendors_2020` · shape **arcgis-hub** · source `open-ottawa` · **spatial**

- origin: <https://open.ottawa.ca/datasets/ottawa::street-food-vendors-2020>
- fetched 2026-09-09 · **44 rows** · 13 columns
- geojson · licence: https://ottawa.ca/en/city-hall/get-know-your-city/open-data#open-data-licence-ve

## Columns

| column | kind | non-null | distinct | summary |
| --- | --- | --- | --- | --- |
| `FID` | num | 100% | 44 | 1.00 · p25 11.75 · p50 22.50 · p95 41.85 · max 44.00  ███▅██▅██▅██▅███ |
| `Trade_Name` | id/text | 100% | 40 | e.g. AD MARE MOBILE SEAFOOD, ALEXANDER'S HOT DOGS, ANGRY DRAGONZ |
| `Concept` | cat | 100% | 7 |   86%, Sustainable fish and sea 2%, Asian fusion with a twis 2%, Bibimbap - authentic Kor 2%, Churro (traditional Mexi 2%, fresh, local and seasona 2% |
| `LICENSE__T` | cat | 100% | 3 | Cart 39%, Truck 32%, Vehicle 30% |
| `Location` | id/text | 100% | 44 | e.g. South side of slater E, East Side of Elgin St , North Side of Gloucest |
| `X` | num | 100% | 43 | 45.35 · p25 45.40 · p50 45.42 · p95 45.43 · max 45.43  ▁▁▁▁▁▁▁▁▂▂▂▁▃▆█▂ |
| `Y_Coordina` | num | 100% | 43 | -75.79 · p25 -75.70 · p50 -75.70 · p95 -75.63 · max -75.62  ▁▁▁▁▁▁▁▂█▃▁▁▁▁▁▂ |
| `Website` | cat | 100% | 6 |   89%, http://admareseafood.com 2%, angrydragonz.ca 2%, hotdogottawa.com 2%, http://streatottawa.ca/ 2%, http://www.ricoperu.ca/ 2% |
| `Twitter` | cat | 100% | 10 |   80%, @Ad_Mare 2%, @angrydragonz 2%, @RaonKitchen 2%, @hotdigdogottawa 2%, @CatrinaChurros 2% |
| `Facebook` | cat | 100% | 5 |   91%, https://www.facebook.com 2%, https://www.facebook.com 2%, https://www.facebook.com 2%, https://www.facebook.com 2% |
| `geometry` | id/text | 100% | 43 | e.g. {"type": "Point", "coo, {"type": "Point", "coo, {"type": "Point", "coo |
| `longitude` | num | 100% | 43 | -75.79 · p25 -75.70 · p50 -75.70 · p95 -75.63 · max -75.62  ▁▁▁▁▁▁▁▂█▃▁▁▁▁▁▂ |
| `latitude` | num | 100% | 43 | 45.35 · p25 45.40 · p50 45.42 · p95 45.43 · max 45.43  ▁▁▁▁▁▁▁▁▂▂▂▁▃▆█▂ |

## Candidate questions

- (none templated)

_profiled 2026-09-09 · `python3 tools/profile.py open_street_food_vendors_2020`_
