# Ottawa 311 service requests by ward

574,252 requests, 2025-01-01 to 2026-09-10. Source: Ottawa's two rolling 311 CSVs (OGL – City of Ottawa).

## Findings

- **Highest volume:** 12  Rideau-Vanier — 34,764 requests (6% of the city
  total). **Lowest:** 5  West Carleton-March — 11,120.
- **Slowest to close:** 5  West Carleton-March, median 13 days open.
  **Fastest:** 8  College, 2 days. *(See the
  correction below before reading anything into this.)*
- Raw volume tracks population and urban density, not need — normalise by ward
  population (2021 census ward data) before reading anything into it.

> ## ⚠ Correction (2026-09-19)
>
> **The time-to-close spread above is a request-mix artifact, not a service-speed
> signal.** An earlier version of this file called it "the more interesting
> signal". It is not.
>
> Ottawa's published close date is administrative rather than operational for
> most categories: garbage closes in a 2-day median and parking in 0, but roads
> takes 197 days, water 202, and dead-animal removal 210. Nobody leaves a
> carcass for seven months — those tickets stay open until a periodic
> reconciliation.
>
> The slow wards are simply the ones submitting proportionally more of those
> slow-to-administer categories: ward 5 is 13 days with 41% of such requests,
> ward 14 is 2 days with 21%. **Within garbage alone — a category that genuinely
> closes on completion — ward medians run 1 to 3 days.** Nearly flat.
>
> Full working: [`releases/311-service-equity`](../311-service-equity).

## Files

`by_ward.csv` — count, share, median days-to-close, % closed per ward.
`by_ward_type.csv` — ward × the 15 commonest request types.

Regenerate: `python3 explorations/requests_311_by_ward.py`
