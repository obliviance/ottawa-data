# Ottawa 2026 municipal election — ward scorecard

Voting day **2026-10-26**. 181 candidates across 24 ward races, the
mayoralty and 0 + four school boards.

A **record, not a ranking.** Nothing here is scored or weighted, and the wards
are ordered by number only. Every figure is a published fact about a public
office holder or a filed candidacy.

## What is in it

- **The incumbent's record** — recorded votes cast, dissents from the majority,
  and meeting attendance, resolved through `spine_councillor_aliases` so no
  spelling variant is dropped.
- **Ward conditions** — 311 volume and median days-to-close, 2026 assessment and
  municipal taxes, population.
- **The race** — every candidate, their nomination date, whether they opted into
  the contribution rebate programme, and the websites and social links **they
  filed with the City Clerk**. Nothing was gathered from anywhere else.
- **Trustees** — the four school board races each ward actually votes in,
  via the zone-to-ward crosswalk in `election_trustee_zones`.

## What is not in it, and why

**No platforms, policies or political affiliation.** Ontario municipal elections
are non-partisan by law, the nomination form is not a CV, and no public body
collects candidate platforms — `hierarchy.md` lists them under *never produced*.
For incumbents the voting record is the substitute, and it is a better one:
promises are cheap, votes are behaviour. For newcomers there is genuinely
nothing, and the scorecard says so rather than implying a comparison it cannot
support. Each candidate's own filed website is linked instead.

**No campaign finance.** 2026 filings are not due until roughly March 2027.

## Findings

- **2 of 24 seats have no incumbent on the ballot**:
  Stittsville, Kitchissippi.
- **2 are decided already** — one candidate each:
  River, Rideau-Jock.
- Ward 20 (Osgoode) had **two councillors** this term and both records are
  shown; the city encodes the changeover inside the ward name field.

## Caveats

- **Only about 4% of motions get a recorded vote.** Dissent rate describes the
  contested slice of council business, not all of it. Vote counts are printed
  beside every rate because 15% of 87 and 53% of 247 are not comparable.
- **Attendance comes from howtheyvoted.ca, not the city.** The city's own
  attendance dataset covers only 39 meetings from
  2024/10/02 to 2026/06/10 — it begins nearly two years into the term.
- Vote and attendance data is compiled by hand upstream and carries ordinary
  site terms, not an open licence.
- **These vote counts differ slightly from `releases/council-vote-cohesion`
  (q0018), and these are the correct ones.** That release matched councillors by
  a single name string, which silently dropped votes recorded under a second
  spelling — `htv_votes` writes the same person as both "C. Kitts" and "Kitts".
  Joining through `spine_councillor_aliases` recovers **35 votes across 18
  councillors**, and moves some rates materially: Catherine Kitts 12.5% → 15.1%,
  Isabelle Skalski 14.9% → 18.9%, Tim Tierney 13.4% → 15.4%. q0018 should be
  regenerated against the alias table.

Regenerate: `python3 spine/entities.py && python3 explorations/ward_scorecard.py`
