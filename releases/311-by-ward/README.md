# Ottawa 311 service requests by ward

574,252 requests, 2025-01-01 to 2026-09-10. Source: Ottawa's two rolling 311 CSVs (OGL – City of Ottawa).

## Findings

- **Highest volume:** 12  Rideau-Vanier — 34,764 requests (6% of the city
  total). **Lowest:** 5  West Carleton-March — 11,120.
- **Slowest to close:** 5  West Carleton-March, median 13 days open.
  **Fastest:** 8  College, 2 days.
- Raw volume tracks population and urban density, not need — normalise by ward
  population (2021 census ward data) before reading anything into it. The
  time-to-close spread is the more interesting signal.

## Files

`by_ward.csv` — count, share, median days-to-close, % closed per ward.
`by_ward_type.csv` — ward × the 15 commonest request types.

Regenerate: `python3 explorations/requests_311_by_ward.py`
