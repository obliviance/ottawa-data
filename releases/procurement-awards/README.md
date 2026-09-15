# Ottawa contract awards — concentration and sole-sourcing

5,648 award actions across 4,714 contracts and
1,620 vendors, worth **$5.97B**, 2022 H2 to 2025 H2.
Source: Open Ottawa's half-year contract-award releases (OGL – City of Ottawa),
normalised by [`tools/ingest/procurement.py`](../../tools/ingest/procurement.py).

## Findings

- **Concentration.** The top 10 vendors take **40.5%** of the
  $5.97B; the top 50 take **67.0%**; the top 100 take
  77.1%. The single largest vendor, **Miller Waste Systems Inc**,
  is 8.2% on its own — $492M
  across 1 contract(s).
- **One clause does most of the sole-sourcing.** 1,081 awards
  (19.1%) were non-competitive, worth $911M
  (15.3% of value). Of that, **clause D alone accounts
  for $633M — 70% of all
  non-competitive value** across 536 awards and
  268 vendors.
- **Contracts grow after they are awarded.** 664 contracts
  (14%) were amended or extended at least once.
  Amendments and extensions total **$1,477M**, or
  25% of all value committed — money added to work already
  under way rather than competed.
- **The sole-sourced share moves a lot between half-years**, from
  8% to
  24% of value. Six months is a short
  window and a single large award moves it, so read the series, not a point.

## Files

`by_vendor.csv` — per vendor: distinct contracts, award actions, total value,
share and cumulative share of all value, and how much of it was sole-sourced.
`by_contract.csv` — per contract number followed across periods: initial award,
amount added later, total, and `growth_multiple` (total ÷ initial, null where
the initial award predates this series).
`by_clause.csv` — each Procurement By-law s.22(1) clause cited: awards, value,
vendors, median award, share of non-competitive value.
`by_department.csv` — per department, including its sole-sourcing rate.
`by_period.csv` — the half-year series.

## Caveats

- **An award action is not a contract.** A contract amended twice appears three
  times. `by_vendor.csv` counts actions; `by_contract.csv` deduplicates.
- **Clause letters are reproduced as the city cites them.** The text of
  Procurement By-law s.22(1) is on
  [ottawa.ca](https://ottawa.ca/en/business/procurement/procurement-law), which
  did not render for automated retrieval, so no clause is described here — only
  counted. Naming them is the obvious next step and needs a human to read the
  by-law.
- **Coverage is uneven at the edges.** 2022 is Transit Commission only; the
  all-departments series starts 2023 H1. Two reporting streams run in parallel
  (all-departments and Transit Commission) and are near-disjoint — 14 duplicate
  rows across the whole set, dropped.
- Vendor names are used as published. No entity resolution has been done, so a
  firm appearing under two spellings is counted twice. That understates
  concentration rather than overstating it.

Regenerate: `python3 tools/ingest/procurement.py && python3 explorations/procurement_concentration.py`
