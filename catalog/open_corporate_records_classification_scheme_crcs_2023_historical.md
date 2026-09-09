# Corporate Records Classification Scheme (CRCS) 2023 (Historical)

`open_corporate_records_classification_scheme_crcs_2023_historical` · shape **arcgis-hub** · source `open-ottawa`

- origin: <https://open.ottawa.ca/datasets/ottawa::corporate-records-classification-scheme-crcs-2023-historical>
- fetched 2026-09-09 · **1,819 rows** · 10 columns
- csv · licence: https://ottawa.ca/en/city-hall/get-know-your-city/open-data#open-data-licence-ve

## Columns

| column | kind | non-null | distinct | summary |
| --- | --- | --- | --- | --- |
| `CRCS_Code` | id/text | 100% | 1,819 | e.g. D09-03, D09-99, D10 |
| `Records_Classification` | text | 100% | 1,415 | e.g. Heritage Confirmation , Special Projects, Park Planning
Includes |
| `Active_Retention` | cat | 87% | 16 | T 49%, 2 21%, 3 19%, 1 5%, 10 3%, 5 1% |
| `Inactive_Transfer_Trigger` | text | 43% | 145 | e.g. Project completed, Superseded, File dormant |
| `Inactive_Retention` | num | 87% | 35 | 1.00 · p25 3.00 · p50 6.00 · p95 30.00 · max 100  █▂▁▁▂▁▁▁▁▁▁▁▁▁▁▁ |
| `Final_Disposition` | cat | 87% | 5 | Destroy 68%, Permanent: Sent to City  25%, Archival Value: To Be De 4%, Permanent: Remains Inact 2%, Archival Value:  To Be D 0% |
| `Restricted` | cat | 8% | 1 | Restricted 100% |
| `Archives_Transfer_Trigger` | cat | 26% | 4 | After Inactive Retention 84%, TBD 15%, After
Inactive
Retention 0%, After Inactive  Retentio 0% |
| `column8` | text | 0% | 0 | e.g.  |
| `FID` | num | 100% | 1,819 | 1.00 · p25 456 · p50 910 · p95 1,728 · max 1,819  ██▇██▇██▇█▇██▇██ |

## Candidate questions

- Trend / seasonality of open_corporate_records_classification_scheme_crcs_2023_historical over `Final_Disposition`; structural breaks?

_profiled 2026-09-09 · `python3 tools/profile.py open_corporate_records_classification_scheme_crcs_2023_historical`_
