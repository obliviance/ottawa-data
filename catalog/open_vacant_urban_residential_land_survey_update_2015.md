# Vacant Urban Residential Land Survey Update 2015

`open_vacant_urban_residential_land_survey_update_2015` · shape **arcgis-hub** · source `open-ottawa`

- origin: <https://open.ottawa.ca/datasets/ottawa::vacant-urban-residential-land-survey-update-2015>
- fetched 2026-09-09 · **718 rows** · 19 columns
- csv · licence: https://ottawa.ca/en/city-hall/get-know-your-city/open-data#open-data-licence-ve

## Columns

| column | kind | non-null | distinct | summary |
| --- | --- | --- | --- | --- |
| `SUB_AREA` | cat | 100% | 6 | KANATA-STITTSVILLE 36%, SOUTH NEPEAN 22%, ORLEANS 19%, RIVERSIDE SOUTH 15%, LEITRIM 9%, ORlEANS 0% |
| `PARCEL_12` | num | 100% | 260 | 100 · p25 248 · p50 342 · p95 778 · max 800  ▆▂▅█▅▆▄▃▄▆▁▃▃▁▁▃ |
| `UNIT` | num | 100% | 229 | 3.00 · p25 44.00 · p50 98.50 · p95 793 · max 2,295  █▃▁▁▁▁▁▁▁▁▁▁▁▁▁▁ |
| `AREA` | num | 100% | 256 | 0.11 · p25 1.42 · p50 3.03 · p95 20.46 · max 50.69  █▄▂▁▁▁▁▁▁▁▁▁▁▁▁▁ |
| `SINGLE_UNI` | num | 100% | 62 | 0.00 · p25 0.00 · p50 18.00 · p95 204 · max 646  █▃▁▁▁▁▁▁▁▁▁▁▁▁▁▁ |
| `SINGLE_ARE` | num | 100% | 75 | 0.00 · p25 0.00 · p50 0.91 · p95 8.78 · max 26.45  █▂▂▁▁▁▁▁▁▁▁▁▁▁▁▁ |
| `SEMI_UNIT` | num | 100% | 17 | 0.00 · p25 0.00 · p50 0.00 · p95 16.00 · max 282  █▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁ |
| `SEMI_AREA` | num | 100% | 22 | 0.00 · p25 0.00 · p50 0.00 · p95 0.68 · max 6.93  █▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁ |
| `TOWN_UNIT` | num | 100% | 64 | 0.00 · p25 0.00 · p50 8.00 · p95 113 · max 697  █▂▁▁▁▁▁▁▁▁▁▁▁▁▁▁ |
| `TOWN_AREA` | num | 100% | 76 | 0.00 · p25 0.00 · p50 0.13 · p95 3.02 · max 19.15  █▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁ |
| `STACK_UNIT` | num | 100% | 25 | 0.00 · p25 0.00 · p50 0.00 · p95 96.00 · max 588  █▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁ |
| `STACK_AREA` | num | 100% | 28 | 0.00 · p25 0.00 · p50 0.00 · p95 1.13 · max 7.12  █▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁ |
| `APT_UNIT` | num | 100% | 31 | 0.00 · p25 0.00 · p50 0.00 · p95 147 · max 938  █▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁ |
| `APT_ARAE` | num | 100% | 32 | 0.00 · p25 0.00 · p50 0.00 · p95 1.07 · max 7.06  █▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁ |
| `PLAN_1` | text | 100% | 66 | e.g. 4M-1248,  , 4M-1404 |
| `STATUS_1` | cat | 100% | 4 | REGISTERED 72%, NO PLAN 18%, DRAFT APPROVED 5%, PENDING 4% |
| `SUB_AREA_F` | cat | 100% | 5 | KANATA-STITTSVILLE 36%, NEPEAN-SUD 22%, ORLÉANS 19%, RIVERSIDE-SUD 15%, LEITRIM 9% |
| `STATUT` | cat | 100% | 4 | ENREGISTRÉ 72%, AUCUN PLAN 18%, PLAN APPROUVÉ 5%, EN COURS 4% |
| `ObjectId` | num | 100% | 718 | 1.00 · p25 180 · p50 360 · p95 682 · max 718  █████▇████▇█████ |

## Candidate questions

- (none templated)

_profiled 2026-09-09 · `python3 tools/profile.py open_vacant_urban_residential_land_survey_update_2015`_
