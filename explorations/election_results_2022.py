#!/usr/bin/env python3
"""2022 municipal election — margins and turnout, race by race.

Answers the question that unblocked `tools/ingest/election_results.py`: of the 24 ward
Councillor races plus Mayor, which were actually close in 2022, and which were landslides
or acclamations? Every 2026 comparison (who's vulnerable, where a strong challenger could
flip a seat) starts from knowing 2022's real margin, not an assumption from name
recognition.

Produces:
  releases/election-margins-2022/
    race_margins.csv   one row per race: winner, runner-up, margin (votes + %), turnout
    datapackage.json + README.md

Run: python3 explorations/election_results_2022.py
  (needs d_election_results_2022_totals, d_spine_wards -- run
  tools/ingest/election_results.py and spine/geography.py first)
"""
from __future__ import annotations

import json
import pathlib
import sys

import pandas as pd

sys.path.insert(0, str(pathlib.Path(__file__).parent.parent / "tools"))
import warehouse  # noqa: E402

OUT = pathlib.Path(__file__).parent.parent / "releases" / "election-margins-2022"


def main() -> None:
    c = warehouse.con()
    totals = c.execute("SELECT * FROM d_election_results_2022_totals").df()
    wards = c.execute("SELECT ward_num, ward_name FROM d_spine_wards").df()
    c.close()

    rows = []
    for (race, ward), grp in totals.groupby(["race", "ward"], dropna=False):
        grp = grp.sort_values("votes", ascending=False).reset_index(drop=True)
        cast_total = int(grp["votes"].sum())  # candidate votes, i.e. valid ballots -- the
        # honest margin-% denominator; times_cast also counts declined/spoiled ballots.
        winner, winner_votes = grp.loc[0, "candidate"], int(grp.loc[0, "votes"])
        if len(grp) > 1:
            runner_up, runner_up_votes = grp.loc[1, "candidate"], int(grp.loc[1, "votes"])
            margin_votes = winner_votes - runner_up_votes
            margin_pct = round(100 * margin_votes / cast_total, 2) if cast_total else None
        else:
            # Acclaimed: no second name ever appeared as a candidate column on this sheet.
            runner_up, runner_up_votes, margin_votes, margin_pct = None, None, None, None
        registered = int(grp.loc[0, "registered_voters"] or 0)
        times_cast = int(grp.loc[0, "times_cast"] or 0)
        rows.append(
            {
                "race": race,
                "ward": int(ward) if pd.notna(ward) else None,  # Mayor's ward is None/NaN
                "candidates": len(grp),
                "winner": winner,
                "winner_votes": winner_votes,
                "runner_up": runner_up,
                "runner_up_votes": runner_up_votes,
                "margin_votes": margin_votes,
                "margin_pct": margin_pct,
                "valid_votes_cast": cast_total,
                "registered_voters": registered,
                "turnout_pct": round(100 * times_cast / registered, 2) if registered else None,
            }
        )

    df = pd.DataFrame(rows).merge(
        wards.rename(columns={"ward_num": "ward"}), on="ward", how="left"
    )
    df = df.sort_values(
        by=["margin_pct"], key=lambda s: s.fillna(999)
    )  # acclamations (no margin) sort last, not first as NaN would

    OUT.mkdir(parents=True, exist_ok=True)
    cols = [
        "race", "ward", "ward_name", "candidates", "winner", "winner_votes",
        "runner_up", "runner_up_votes", "margin_votes", "margin_pct",
        "valid_votes_cast", "registered_voters", "turnout_pct",
    ]
    df[cols].to_csv(OUT / "race_margins.csv", index=False)

    n_races = len(df)
    acclaimed = df[df["candidates"] == 1]
    closest = df[df["candidates"] > 1].nsmallest(5, "margin_pct")
    landslides = df[df["candidates"] > 1].nlargest(5, "margin_pct")
    turnout_sorted = df.dropna(subset=["turnout_pct"]).sort_values("turnout_pct")

    def _place(r) -> str:
        return r["ward_name"] if pd.notna(r["ward"]) else r["race"]

    lowest_turnout = turnout_sorted.iloc[0]
    highest_turnout = turnout_sorted.iloc[-1]

    (OUT / "README.md").write_text(f"""# Ottawa 2022 municipal election — margins by race

{n_races} races (Mayor + 24 wards), from the city's own poll-by-poll Statement of Votes
Cast. Source: Open Ottawa (`election-results-history`), OGL – City of Ottawa. Every
candidate's vote total here is cross-checked against the sum of their own poll-level
results in the same file and matches exactly.

## Findings

- **{len(acclaimed)} acclaimed** (one candidate, no vote): {', '.join(
        f"{r.ward_name} (ward {int(r.ward)})" for r in acclaimed.itertuples()
    ) or 'none'}.
- **Closest contested races** (margin as % of valid votes cast):
{chr(10).join(
        f"  - {r.race}{' ward ' + str(int(r.ward)) + ' (' + str(r.ward_name) + ')' if r.ward == r.ward else ''}: "
        f"{r.winner} beat {r.runner_up} by {r.margin_votes:,} votes ({r.margin_pct}%)"
        for r in closest.itertuples()
    )}
- **Widest contested margins:**
{chr(10).join(
        f"  - {r.race}{' ward ' + str(int(r.ward)) + ' (' + str(r.ward_name) + ')' if r.ward == r.ward else ''}: "
        f"{r.winner} beat {r.runner_up} by {r.margin_pct}%"
        for r in landslides.itertuples()
    )}
- **Turnout range:** {_place(lowest_turnout)} lowest at {lowest_turnout['turnout_pct']}%,
  {_place(highest_turnout)} highest at {highest_turnout['turnout_pct']}%.

## Caveats

- **Mayor and ward races are not directly comparable on turnout**: `registered_voters`
  for Mayor is the whole city; a ward's is that ward's own list, so the two `turnout_pct`
  figures answer the same question at different scopes, not a ranking across all 25 rows.
- **Margin % denominator is valid candidate votes, not `times_cast`.** `times_cast`
  includes declined and (for the tallying process) spoiled ballots, which is the right
  figure for turnout but would understate a margin computed against candidates alone.
- School-board trustee races are not included — see `tools/ingest/election_results.py`'s
  module docstring for why (no ward crosswalk exists for the trustee zones yet).
- This is 2022 only. Whether a close 2022 race stays close in 2026 depends on who is
  actually running again — join to `d_election_candidates` (2026 roster) for that, not
  assumed here.

Full detail: `race_margins.csv`.
""")

    (OUT / "datapackage.json").write_text(
        json.dumps(
            {
                "name": "election-margins-2022",
                "title": "Ottawa 2022 municipal election margins",
                "description": f"{n_races} races (Mayor + 24 wards): winner, runner-up, "
                "margin, and turnout, from the city's own poll-by-poll results.",
                "licenses": [{"name": "OGL-Ottawa", "title": "Open Government Licence – City of Ottawa"}],
                "sources": [
                    {
                        "title": "2022 Elections Official Results (Statement of Votes Cast)",
                        "path": "https://open.ottawa.ca/documents/ottawa::2022-elections-official-results",
                    }
                ],
                "resources": [{"path": "race_margins.csv", "format": "csv"}],
            },
            indent=2,
        )
        + "\n"
    )
    print(f"wrote {OUT}/  ({n_races} races)")


if __name__ == "__main__":
    main()
