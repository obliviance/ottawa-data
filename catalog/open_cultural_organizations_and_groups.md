# Cultural Organizations and Groups

`open_cultural_organizations_and_groups` · shape **arcgis-hub** · source `open-ottawa` · **spatial**

- origin: <https://open.ottawa.ca/datasets/ottawa::cultural-organizations-and-groups>
- fetched 2026-09-09 · **932 rows** · 21 columns
- csv · licence: https://ottawa.ca/en/city-hall/open-transparent-and-accountable-government/open-

## Columns

| column | kind | non-null | distinct | summary |
| --- | --- | --- | --- | --- |
| `Unique_ID` | num | 100% | 932 | 1.00 · p25 234 · p50 466 · p95 885 · max 932  █▇▇▇▇█▇▇▇▇█▇▇▇▇█ |
| `Name` | id/text | 100% | 932 | e.g. 100th Regiment Histori, 613Flea, 2359 Productions |
| `Nom` | id/text | 100% | 931 | e.g. Société historique du , 613Flea, 2359 Productions |
| `Structure` | cat | 100% | 8 | Non-profit/Charity 49%, Business 28%, Student Group 15%, Community Group 6%, Crown Corporation 1%, Social Enterprise or Co- 0% |
| `Structure__Fr_` | cat | 99% | 7 | Organismes à but non luc 49%, Affaires 28%, Groupe d’étudiants 15%, Groupe communautaire 6%, Sociétés d’État 1%, Entreprise sociale ou co 1% |
| `Category` | text | 100% | 97 | e.g. Live Performance, Food and Beverage,Visu, Visual and Applied Art |
| `Categorie` | text | 100% | 93 | e.g. Spectacle, Alimentation et Restau, Spectacle,Arts Visuels |
| `Sub_Category` | text | 99% | 214 | e.g. Performing Arts, Crafts,Festivals and C, Performing Arts,Film a |
| `Sub_Categorie` | text | 99% | 216 | e.g. Arts de la Scène, Artisanat,Festivals et, Arts de la Scène,Films |
| `Associated_Tags` | text | 98% | 461 | e.g. Historical Reenactment, Textiles,Housewares,Fu, Music,Theatre (Includi |
| `Mots_Cles` | text | 98% | 461 | e.g. Reconstitution Histori, Textiles,Articles Ména, Musique,"Théâtre (Comé |
| `Languages` | text | 99% | 87 | e.g. English, English,French, English,Sign |
| `Langue` | text | 99% | 87 | e.g. Anglais, Anglais,français, Anglais,Sign |
| `Email___Contact_Page` | id/text | 95% | 864 | e.g. join@100thregiment.org, Hello@613flea.ca , bonjour@2359.productio |
| `Website___Main_SM_Profile` | id/text | 98% | 915 | e.g. https://100thregiment., https://www.613flea.ca, https://2359.productio |
| `Website___Main_SM_Profile_French` | id/text | 98% | 913 | e.g. https://100thregiment., https://www.613flea.ca, https://2359.productio |
| `Physical_Address` | text | 93% | 648 | e.g. 1015 Bank Street,Ottaw, 3-55 Spruce Street, Ot, City View United Churc |
| `Adresse_physique` | text | 92% | 640 | e.g. 1015, rue Bank, Ottawa, 3-55, rue Spruce, Otta, Église unie City View, |
| `Latitude` | num | 81% | 744 | 44.90 · p25 45.38 · p50 45.41 · p95 45.44 · max 46.40  ▁▁▁▁▂█▁▁▁▁▁▁▁▁▁▁ |
| `Longitude` | num | 81% | 738 | -76.15 · p25 -75.72 · p50 -75.69 · p95 -75.60 · max -75.42  ▁▁▁▁▁▁▁▁▂▆█▂▁▁▁▁ |
| `ObjectId` | num | 100% | 932 | 1.00 · p25 234 · p50 466 · p95 885 · max 932  █▇▇▇▇█▇▇▇▇█▇▇▇▇█ |

## Candidate questions

- Spatial clustering of open_cultural_organizations_and_groups; overlay wards + the decision timeline

_profiled 2026-09-09 · `python3 tools/profile.py open_cultural_organizations_and_groups`_
