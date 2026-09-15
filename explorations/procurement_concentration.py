#!/usr/bin/env python3
"""q0002 — who wins Ottawa's contracts, how concentrated is it, and what is sole-sourced.

The city publishes contract awards twice a year and never as a series, so the
question "which firms win the most, and how much never goes to tender?" has to
be reassembled from nine separate releases. `tools/ingest/procurement.py` does
that; this reads the result.

One row in `procurement_awards` is an award *action* -- an initial award, an
amendment, or an extension -- so a contract amended twice appears three times.
Both framings matter and both are published here: `by_vendor.csv` counts
actions (what the city committed in a period), `by_contract.csv` follows each
contract number across periods (what a contract ended up costing).

Produces:
  releases/procurement-awards/
    by_vendor.csv       per vendor: contracts, actions, value, share, sole-sourced share
    by_contract.csv     per contract: initial vs amendment vs extension, growth multiple
    by_clause.csv       s.22(1) non-competitive clauses: how often, how much, by whom
    by_department.csv   per department, with its sole-sourcing rate
    by_period.csv       the half-year series
    datapackage.json + README.md

Run: python3 explorations/procurement_concentration.py
     (needs d_procurement_awards -- build it with tools/ingest/procurement.py)
"""
from __future__ import annotations

import json
import pathlib
import sys

sys.path.insert(0, str(pathlib.Path(__file__).parent.parent / "tools"))
import warehouse  # noqa: E402

OUT = pathlib.Path(__file__).parent.parent / "releases" / "procurement-awards"

# Awards whose approval type says the money was added to an existing contract
# rather than committed at the start.
GROWTH_TYPES = ("Amendment", "Extension")


def main() -> None:
    import numpy as np
    import pandas as pd

    c = warehouse.con()
    a = c.execute("""
        SELECT contract_no, vendor, department, description, approval_type,
               amount, is_noncompetitive, clause, period, period_year,
               period_half, stream
        FROM d_procurement_awards
        WHERE amount IS NOT NULL AND vendor <> ''
    """).df()
    c.close()

    total = a.amount.sum()
    a["is_growth"] = a.approval_type.str.contains("|".join(GROWTH_TYPES), na=False)

    # ---- vendors -----------------------------------------------------------
    by_vendor = (a.groupby("vendor")
                 .agg(contracts=("contract_no", "nunique"),
                      actions=("amount", "size"),
                      total_amount=("amount", "sum"),
                      noncompetitive_amount=("amount",
                                             lambda s: a.loc[s.index][a.loc[s.index].is_noncompetitive].amount.sum()))
                 .sort_values("total_amount", ascending=False))
    by_vendor["share_of_total"] = (by_vendor.total_amount / total).round(5)
    by_vendor["cumulative_share"] = by_vendor.share_of_total.cumsum().round(5)
    by_vendor["noncompetitive_share"] = (
        by_vendor.noncompetitive_amount / by_vendor.total_amount).round(4)
    by_vendor = by_vendor.round({"total_amount": 2, "noncompetitive_amount": 2}).reset_index()

    # ---- contracts, followed across periods --------------------------------
    def part(frame, kinds):
        m = frame.approval_type.str.contains("|".join(kinds), na=False)
        return frame.loc[m, "amount"].sum()

    by_contract = (a.groupby("contract_no")
                   .apply(lambda g: pd.Series({
                       "vendor": g.vendor.mode().iat[0] if not g.vendor.mode().empty else "",
                       "department": g.department.mode().iat[0] if not g.department.mode().empty else "",
                       "description": g.description.iloc[0][:160],
                       "actions": len(g),
                       "initial_amount": part(g, ["Initial", "Follow-On"]),
                       "added_amount": part(g, GROWTH_TYPES),
                       "total_amount": g.amount.sum(),
                       "first_period": g.period.min(),
                       "last_period": g.period.max(),
                       "noncompetitive": bool(g.is_noncompetitive.any()),
                   }), include_groups=False)
                   .reset_index())
    # Growth is only meaningful where an initial award is on the record; many
    # amendments belong to contracts first awarded before this series starts.
    by_contract["growth_multiple"] = np.where(
        by_contract.initial_amount > 0,
        (by_contract.total_amount / by_contract.initial_amount).round(3),
        np.nan)
    by_contract = by_contract.sort_values("total_amount", ascending=False).round(2)

    # ---- non-competitive clauses -------------------------------------------
    nc = a[a.is_noncompetitive]
    by_clause = (nc.groupby(nc.clause.fillna("(unlettered)"))
                 .agg(awards=("amount", "size"),
                      amount=("amount", "sum"),
                      vendors=("vendor", "nunique"),
                      median_award=("amount", "median"),
                      top_department=("department",
                                      lambda s: s.mode().iat[0] if not s.mode().empty else ""))
                 .sort_values("amount", ascending=False))
    by_clause["share_of_noncompetitive"] = (by_clause.amount / nc.amount.sum()).round(4)
    by_clause = by_clause.round(2).reset_index().rename(columns={"clause": "clause"})

    # ---- departments --------------------------------------------------------
    by_department = (a.groupby("department")
                     .agg(awards=("amount", "size"),
                          contracts=("contract_no", "nunique"),
                          total_amount=("amount", "sum"),
                          noncompetitive_awards=("is_noncompetitive", "sum"),
                          noncompetitive_amount=("amount",
                                                 lambda s: a.loc[s.index][a.loc[s.index].is_noncompetitive].amount.sum()))
                     .sort_values("total_amount", ascending=False))
    by_department["noncompetitive_share"] = (
        by_department.noncompetitive_amount / by_department.total_amount).round(4)
    by_department = by_department.round(2).reset_index()

    # ---- the half-year series ----------------------------------------------
    by_period = (a.groupby("period")
                 .agg(awards=("amount", "size"),
                      contracts=("contract_no", "nunique"),
                      total_amount=("amount", "sum"),
                      noncompetitive_amount=("amount",
                                             lambda s: a.loc[s.index][a.loc[s.index].is_noncompetitive].amount.sum()),
                      added_amount=("amount",
                                    lambda s: a.loc[s.index][a.loc[s.index].is_growth].amount.sum()))
                 .sort_index())
    by_period["noncompetitive_share"] = (
        by_period.noncompetitive_amount / by_period.total_amount).round(4)
    by_period = by_period.round(2).reset_index()

    OUT.mkdir(parents=True, exist_ok=True)
    for name, frame in (("by_vendor", by_vendor), ("by_contract", by_contract),
                        ("by_clause", by_clause), ("by_department", by_department),
                        ("by_period", by_period)):
        frame.to_csv(OUT / f"{name}.csv", index=False)

    # ---- the numbers worth stating -----------------------------------------
    span = f"{by_period.period.iloc[0]} to {by_period.period.iloc[-1]}"
    top = {n: by_vendor.total_amount.head(n).sum() / total for n in (1, 5, 10, 25, 50, 100)}
    nc_value, nc_n = nc.amount.sum(), len(nc)
    grew = by_contract[by_contract.actions > 1]
    added = a.loc[a.is_growth, "amount"].sum()
    d = by_clause[by_clause.clause == "D"].iloc[0] if (by_clause.clause == "D").any() else None

    (OUT / "datapackage.json").write_text(json.dumps({
        "name": "procurement-awards",
        "title": "Ottawa contract awards — concentration and sole-sourcing",
        "description": (f"{len(a):,} contract award actions worth ${total/1e9:.2f}B, "
                        f"{span}, normalised from nine half-year releases and "
                        "aggregated by vendor, contract, department, "
                        "non-competitive clause and period."),
        "licenses": [{"name": "OGL-Ottawa",
                      "title": "Open Government Licence – City of Ottawa"}],
        "sources": [{"title": "Open Ottawa — contracts awarded (half-year releases)",
                     "path": "https://open.ottawa.ca/search?q=contracts%20awarded"}],
        "resources": [{"path": f"{n}.csv", "format": "csv"} for n in
                      ("by_vendor", "by_contract", "by_clause",
                       "by_department", "by_period")],
    }, indent=2) + "\n")

    (OUT / "README.md").write_text(f"""# Ottawa contract awards — concentration and sole-sourcing

{len(a):,} award actions across {a.contract_no.nunique():,} contracts and
{a.vendor.nunique():,} vendors, worth **${total/1e9:.2f}B**, {span}.
Source: Open Ottawa's half-year contract-award releases (OGL – City of Ottawa),
normalised by [`tools/ingest/procurement.py`](../../tools/ingest/procurement.py).

## Findings

- **Concentration.** The top 10 vendors take **{top[10]:.1%}** of the
  ${total/1e9:.2f}B; the top 50 take **{top[50]:.1%}**; the top 100 take
  {top[100]:.1%}. The single largest vendor, **{by_vendor.vendor.iloc[0].title()}**,
  is {top[1]:.1%} on its own — ${by_vendor.total_amount.iloc[0]/1e6:,.0f}M
  across {int(by_vendor.contracts.iloc[0])} contract(s).
- **One clause does most of the sole-sourcing.** {nc_n:,} awards
  ({nc_n/len(a):.1%}) were non-competitive, worth ${nc_value/1e6:,.0f}M
  ({nc_value/total:.1%} of value). Of that, **clause {d.clause} alone accounts
  for ${d.amount/1e6:,.0f}M — {d.share_of_noncompetitive:.0%} of all
  non-competitive value** across {int(d.awards)} awards and
  {int(d.vendors)} vendors.{'' if d is not None else ''}
- **Contracts grow after they are awarded.** {len(grew):,} contracts
  ({len(grew)/len(by_contract):.0%}) were amended or extended at least once.
  Amendments and extensions total **${added/1e6:,.0f}M**, or
  {added/total:.0%} of all value committed — money added to work already
  under way rather than competed.
- **The sole-sourced share moves a lot between half-years**, from
  {by_period.noncompetitive_share.min():.0%} to
  {by_period.noncompetitive_share.max():.0%} of value. Six months is a short
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
""")

    print(f"releases/procurement-awards/ — {len(a):,} actions, "
          f"{a.contract_no.nunique():,} contracts, ${total/1e9:.2f}B, {span}")
    print(f"\nconcentration: " + "  ".join(f"top{n}={s:.1%}" for n, s in top.items()))
    print(f"non-competitive: {nc_n:,} awards, ${nc_value/1e6:,.0f}M ({nc_value/total:.1%} of value)")
    if d is not None:
        print(f"  clause {d.clause}: {int(d.awards)} awards, ${d.amount/1e6:,.0f}M "
              f"= {d.share_of_noncompetitive:.0%} of non-competitive value")
    print(f"growth: {len(grew):,} contracts amended/extended, ${added/1e6:,.0f}M added "
          f"({added/total:.0%} of all value)")
    print("\ntop 10 vendors:")
    print(by_vendor.head(10)[["vendor", "contracts", "actions", "total_amount",
                              "share_of_total", "noncompetitive_share"]].to_string(index=False))
    print("\nclauses:")
    print(by_clause.to_string(index=False))


if __name__ == "__main__":
    main()
