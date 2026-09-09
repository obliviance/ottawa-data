# Budget 2020 Capital Status Report Q1

`open_budget_2020_capital_status_report_q1` · shape **arcgis-hub** · source `open-ottawa`

- origin: <https://open.ottawa.ca/datasets/ottawa::budget-2020-capital-status-report-q1>
- fetched 2026-09-09 · **800 rows** · 21 columns
- csv · licence: https://ottawa.ca/en/city-hall/get-know-your-city/open-data#open-data-licence-ve

## Columns

| column | kind | non-null | distinct | summary |
| --- | --- | --- | --- | --- |
| `Order` | num | 100% | 800 | 900,300 · p25 907,784 · p50 908,570 · p95 909,594 · max 909,937  ▁▁▁▁▁▁▁▁▁▁▂▂▄▇█▅ |
| `Project` | num | 100% | 800 | 900,300 · p25 907,784 · p50 908,570 · p95 909,594 · max 909,937  ▁▁▁▁▁▁▁▁▁▁▂▂▄▇█▅ |
| `Project_Description` | id/text | 100% | 780 | e.g. 909250 Alexander Park , 909252 Nepean Sportspl, 908475 2017 Parks - Pa |
| `Order_Description` | id/text | 100% | 797 | e.g. Alexander Park - Impro, Nepean Sportsplex Foot, 2017 Parks - Parks & R |
| `Committee_Description` | cat | 100% | 11 | Stding Com. EP WW Mgm, R 29%, Transportation 28%, Community & Protective S 19%, Transit Commission 8%, Finance & Economic Devel 3%, Planning 3% |
| `IO_Department_Description` | cat | 100% | 12 | Planning, Infr, & Econom 34%, Transportation Services  24%, PW & Enviromental Servic 18%, Rec, Cultural and Facili 13%, Community & Social Servi 3%, Ottawa Police Services 3% |
| `IO_Service_Description` | text | 100% | 33 | e.g. Parks & Facilities Pla, Infrastructure Service, Parks, Forestry & Stor |
| `Service_Area_Description` | text | 100% | 31 | e.g. Parks, Recreation & Cu, Transit Services, Transportation Service |
| `IO_Branch_Description` | text | 100% | 73 | e.g. Recreation, D&C Buildings-Faciliti, Parks, Buildings & Gro |
| `Capital_Project_Category_Description` | cat | 100% | 4 | Renewal of City Assets 60%, Growth 18%, Service Enhancement 18%, Regulatory 4% |
| `Ward_Code` | text | 100% | 52 | e.g. CW, 22, 08 |
| `Ward_Description` | cat | 100% | 25 | City-Wide 59%, Multiple 5%, Ward 11 - Beacon Hill-Cy 3%, Ward 21 - Rideau-Goulbou 3%, Ward 3 - Barrhaven 2%, Ward 19 - Cumberland 2% |
| `First_Year_of_Approved_Budget` | num | 100% | 20 | 1,999 · p25 2,015 · p50 2,017 · p95 2,019 · max 2,020  ▁▁▁▁▁▁▁▁▁▂▂▂█▅▆▆ |
| `Estimated_Year_of_Completion` | num | 100% | 12 | 2,012 · p25 2,019 · p50 2,020 · p95 2,023 · max 2,028  ▁▁▁▁▁▁▇█▆▂▁▁▁▁▁▁ |
| `Budget_Amount` | num | 100% | 574 | 0.00 · p25 375 · p50 1,120 · p95 16,505 · max 2,095,600  █▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁ |
| `Actual_Amount` | num | 100% | 784 | -133 · p25 91.72 · p50 416 · p95 10,635 · max 2,084,315  █▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁ |
| `Unspent_Cash_Balance_March_31_2020` | num | 100% | 784 | -31,157 · p25 54.03 · p50 295 · p95 6,747 · max 236,147  ▁█▁▁▁▁▁▁▁▁▁▁▁▁▁▁ |
| `Contractual_Obligations` | num | 100% | 493 | 0.00 · p25 0.00 · p50 18.85 · p95 1,197 · max 138,522  █▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁ |
| `Unspent_Balance_including_Contractual_Obligations` | num | 100% | 782 | -34,923 · p25 22.81 · p50 179 · p95 5,829 · max 188,831  ▁▁█▁▁▁▁▁▁▁▁▁▁▁▁▁ |
| `Explanation__Deficit_of____100K_Suitable_for_Council` | cat | 1% | 4 | BA to be processed durin 50%, There are recoveries/rev 25%, Expenditures will be off 12%, There are recoveries/rev 12% |
| `FID` | num | 100% | 800 | 1.00 · p25 201 · p50 400 · p95 760 · max 800  ████████████████ |

## Candidate questions

- Trend / seasonality of open_budget_2020_capital_status_report_q1 over `First_Year_of_Approved_Budget`; structural breaks?

_profiled 2026-09-09 · `python3 tools/profile.py open_budget_2020_capital_status_report_q1`_
