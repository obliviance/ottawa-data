# Ottawa City Council — recorded-vote cohesion (2022→)

334 motions with a recorded division, 2022-11-09 to 2026-09-02. Source: howtheyvoted.ca
(compiled by hand — Ontario does not require municipalities to publish recorded votes).

## Findings

- **Most independent:** S. Menard dissents from the majority on
  53% of recorded votes (131 of
  247). **Most reliably with the majority:**
  M. Sutcliffe at 10%.
- **Least-aligned pair:** G. Darouze & S. Menard agree on
  23% of the 124 motions they both voted on.
- **Most-aligned pair:** D. Brown & I. Skalski, 95%
  over 77.
- Council-wide, 30% of councillor pairs agree
  more than 80% of the time — recorded divisions are the exception, and when they
  happen the council is not sharply factional.

## Caveats

Only ~4% of motions get a recorded vote; the rest carry on
consent and are invisible here. "Majority" is computed per motion from the recorded
votes only. `agreement_pairs.csv` drops pairs with < 15 shared votes.

Regenerate: `python3 explorations/vote_cohesion.py`
