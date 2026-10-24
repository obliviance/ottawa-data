# Ottawa Neighbourhood Study — indicator values by neighbourhood

`ons_indicator_values` · shape **json-api** · source `ons`

- origin: <https://ons-sqo.ca/wp-json/ons/v1/get-data/data>
- fetched 2026-10-24 · **97,929 rows** · 4 columns
- ons_id 0 = city total; 'NA' in raw = suppressed/unavailable (value is null)

## Columns

| column | kind | non-null | distinct | summary |
| --- | --- | --- | --- | --- |
| `indicator_id` | text | 100% | 837 | e.g. pop2021_total, dwellings_priv_count, household_count |
| `ons_id` | num | 100% | 117 | 0.00 · p25 3,029 · p50 3,058 · p95 3,112 · max 3,117  ▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁█ |
| `raw` | num | 99% | 20,718 | -3,895,640 · p25 0.04 · p50 7.62 · p95 6,000 · max 962,000,000  █▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁ |
| `value` | num | 92% | 20,673 | -3,895,640 · p25 0.04 · p50 7.62 · p95 6,000 · max 962,000,000  █▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁ |

## Candidate questions

- (none templated)

_profiled 2026-10-24 · `python3 tools/profile.py ons_indicator_values`_
