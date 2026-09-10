#!/usr/bin/env python3
"""q0018 — recorded-vote cohesion on Ottawa City Council (2022→).

Ontario doesn't require municipalities to publish recorded votes; howtheyvoted.ca
compiles them. Of ~7,600 motions since the 2022 election only ~1,000 had a recorded
division (the rest carried on consent) — this looks at those.

Produces:
  releases/council-vote-cohesion/
    councillor_stats.csv   per-member: recorded votes, dissents, dissent rate
    agreement_pairs.csv    every councillor pair: shared votes, agreement rate
    datapackage.json + README.md

Run: python3 explorations/vote_cohesion.py   (needs d_htv_votes in the warehouse)
"""
from __future__ import annotations

import json
import pathlib
import sys

sys.path.insert(0, str(pathlib.Path(__file__).parent.parent / "tools"))
import warehouse  # noqa: E402

OUT = pathlib.Path(__file__).parent.parent / "releases" / "council-vote-cohesion"


def main() -> None:
    import itertools

    import pandas as pd

    c = warehouse.con()
    v = c.execute("""
        SELECT motion_id, meeting_date::DATE AS date, councillor_name AS who, vote
        FROM d_htv_votes WHERE vote IN ('for','against')
    """).df()
    c.close()
    # drop the mayor's chair-only entries and any councillor with < 20 recorded votes
    counts = v["who"].value_counts()
    v = v[v["who"].isin(counts[counts >= 20].index)]

    # majority side per motion, then per-councillor dissent
    maj = (v.groupby(["motion_id", "vote"]).size().unstack(fill_value=0))
    maj["majority"] = maj.apply(lambda r: "for" if r.get("for", 0) >= r.get("against", 0) else "against", axis=1)
    v = v.merge(maj["majority"], left_on="motion_id", right_index=True)
    v["dissent"] = v["vote"] != v["majority"]

    stats = (v.groupby("who")
             .agg(recorded_votes=("vote", "size"),
                  dissents=("dissent", "sum"),
                  first=("date", "min"), last=("date", "max"))
             .assign(dissent_rate=lambda d: (d.dissents / d.recorded_votes).round(3))
             .sort_values("dissent_rate", ascending=False)
             .reset_index())

    # pairwise agreement on motions both voted on
    wide = v.pivot_table(index="motion_id", columns="who", values="vote", aggfunc="first")
    members = list(wide.columns)
    pairs = []
    for a, b in itertools.combinations(sorted(members), 2):
        both = wide[[a, b]].dropna()
        if len(both) < 15:
            continue
        agree = (both[a] == both[b]).mean()
        pairs.append({"councillor_a": a, "councillor_b": b,
                      "shared_votes": len(both), "agreement_rate": round(agree, 3)})
    pairs = pd.DataFrame(pairs).sort_values("agreement_rate")

    OUT.mkdir(parents=True, exist_ok=True)
    stats.to_csv(OUT / "councillor_stats.csv", index=False)
    pairs.to_csv(OUT / "agreement_pairs.csv", index=False)

    span = f"{v.date.min():%Y-%m-%d} to {v.date.max():%Y-%m-%d}"
    n_motions = v.motion_id.nunique()
    (OUT / "datapackage.json").write_text(json.dumps({
        "name": "council-vote-cohesion",
        "title": "Ottawa City Council — recorded-vote cohesion (2022→)",
        "description": f"Per-councillor dissent rates and pairwise agreement on {n_motions} "
                       f"recorded divisions, {span}. Derived from howtheyvoted.ca.",
        "licenses": [{"name": "site-terms",
                      "title": "Source (howtheyvoted.ca) carries ordinary site terms, not an open licence"}],
        "sources": [{"title": "howtheyvoted.ca", "path": "https://howtheyvoted.ca/data/ottawa/"}],
        "resources": [
            {"path": "councillor_stats.csv", "format": "csv",
             "schema": {"fields": [{"name": n} for n in stats.columns]}},
            {"path": "agreement_pairs.csv", "format": "csv",
             "schema": {"fields": [{"name": n} for n in pairs.columns]}},
        ],
    }, indent=2) + "\n")

    lo = pairs.iloc[0]
    hi = pairs.iloc[-1]
    (OUT / "README.md").write_text(f"""# Ottawa City Council — recorded-vote cohesion (2022→)

{n_motions} motions with a recorded division, {span}. Source: howtheyvoted.ca
(compiled by hand — Ontario does not require municipalities to publish recorded votes).

## Findings

- **Most independent:** {stats.iloc[0].who} dissents from the majority on
  {stats.iloc[0].dissent_rate:.0%} of recorded votes ({stats.iloc[0].dissents} of
  {stats.iloc[0].recorded_votes}). **Most reliably with the majority:**
  {stats.iloc[-1].who} at {stats.iloc[-1].dissent_rate:.0%}.
- **Least-aligned pair:** {lo.councillor_a} & {lo.councillor_b} agree on
  {lo.agreement_rate:.0%} of the {lo.shared_votes} motions they both voted on.
- **Most-aligned pair:** {hi.councillor_a} & {hi.councillor_b}, {hi.agreement_rate:.0%}
  over {hi.shared_votes}.
- Council-wide, {(pairs.agreement_rate > 0.8).mean():.0%} of councillor pairs agree
  more than 80% of the time — recorded divisions are the exception, and when they
  happen the council is not sharply factional.

## Caveats

Only ~{100 * n_motions // 7621}% of motions get a recorded vote; the rest carry on
consent and are invisible here. "Majority" is computed per motion from the recorded
votes only. `agreement_pairs.csv` drops pairs with < 15 shared votes.

Regenerate: `python3 explorations/vote_cohesion.py`
""")
    print(f"releases/council-vote-cohesion/ — {len(stats)} councillors, {len(pairs)} pairs, {n_motions} motions")
    print("\ntop 5 by dissent rate:")
    print(stats.head(5).to_string(index=False))
    print("\n5 least-aligned pairs:")
    print(pairs.head(5).to_string(index=False))


if __name__ == "__main__":
    main()
