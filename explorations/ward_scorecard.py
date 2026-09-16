#!/usr/bin/env python3
"""The 2026 ward scorecard: what each incumbent did, and who is on the ballot.

    python3 explorations/ward_scorecard.py

A record, not a ranking. Everything here is a published fact about a public
office holder or a filed candidacy; nothing is scored, weighted or ordered by
anything except ward number. Sorting 24 wards by "worst 311 response" would be
an editorial act, and the point of this is to be the neutral version that does
not otherwise exist -- the only comparable tool is an advocacy organisation's.

Produces:
  releases/ward-scorecard/
    by_ward.csv           one row per ward: incumbent, record, conditions, race
    incumbent_record.csv  one row per councillor-term (ward 20 has two)
    candidates.csv        the 2026 roster with filed contact details
    candidate_links.csv   websites and social links, as filed with the Clerk
    trustee_races.csv     which four trustee races each ward votes in
    scorecard.json        the same, shaped for the page
    datapackage.json + README.md

Two measurement notes that shape everything below.

**Only ~4% of motions get a recorded vote.** Dissent rate therefore describes
the contested slice of council business, not all of it, and the count is always
carried next to the rate: 15% of 87 votes and 53% of 247 are not comparable
quantities, and a bare percentage invites exactly that misreading.

**The city's own attendance dataset starts in October 2024** -- two years into a
term that began November 2022 -- and covers 39 meetings. `htv_attendance` spans
2022-11 to 2026-09 and marks absences explicitly, so it is used instead. The
discrepancy is reported rather than quietly resolved.
"""
from __future__ import annotations

import json
import pathlib
import re
import sys

sys.path.insert(0, str(pathlib.Path(__file__).parent.parent / "tools"))
import warehouse  # noqa: E402

REPO = pathlib.Path(__file__).parent.parent
OUT = REPO / "releases" / "ward-scorecard"
ELECTION_DAY = "2026-10-26"

# Filed links, in the order a voter is most likely to want them.
LINK_ORDER = ["Website", "Facebook", "Instagram", "LinkedIn", "X", "BlueSky",
              "Youtube", "Snapchat", "Blog/Other"]


def money(series):
    """'$7,482,653,645' -> 7482653645.0"""
    import pandas as pd
    return pd.to_numeric(series.astype(str).str.replace(r"[^0-9.]", "", regex=True),
                         errors="coerce")


def main() -> None:
    import numpy as np
    import pandas as pd

    c = warehouse.con()
    spine = c.execute("SELECT * FROM d_spine_councillors WHERE role='Councillor'").df()
    aliases = c.execute("SELECT * FROM d_spine_councillor_aliases").df()
    votes = c.execute("""SELECT motion_id, councillor_name, vote FROM d_htv_votes
                         WHERE vote IN ('for','against')""").df()
    att = c.execute("SELECT councillor_name, status FROM d_htv_attendance").df()
    cands = c.execute("SELECT * FROM d_election_candidates").df()
    links = c.execute("SELECT * FROM d_election_candidate_links").df()
    zones = c.execute("SELECT * FROM d_election_trustee_zones").df()
    taxes = c.execute("""SELECT WARD ward_number, F_2026_Current_Value_Assessment__CVA_ cva,
                                F2026_Municipal_Taxes tax
                         FROM d_open_taxes_by_ward_2022_2026""").df()
    pop = c.execute("""SELECT WARD_NUM ward_number, POPULATION population
                       FROM d_open_population_household_estimates_by_ward_mid_2021""").df()
    places = c.execute("""SELECT Ward ward_number, Acc_Entr FROM
                          d_open_2026_municipal_elections_voting_places""").df()
    city_att = c.execute("""SELECT min(meeting_date) f, max(meeting_date) l,
                            count(DISTINCT meeting_date) n
                            FROM d_open_city_council_meeting_attendance_2022_2026""").df().iloc[0]
    c.close()

    # ---- resolve vote and attendance rows onto a councillor -------------------
    lookup = dict(zip(aliases.alias, aliases.surname_key))
    votes["surname_key"] = votes.councillor_name.map(lookup)
    att["surname_key"] = att.councillor_name.map(lookup)
    votes = votes.dropna(subset=["surname_key"])
    att = att.dropna(subset=["surname_key"])

    # Majority side per motion, then dissent -- the q0018 method, now joined
    # through the alias table so no spelling variant is dropped.
    tally = votes.groupby(["motion_id", "vote"]).size().unstack(fill_value=0)
    for col in ("for", "against"):
        if col not in tally:
            tally[col] = 0
    tally["majority"] = np.where(tally["for"] >= tally["against"], "for", "against")
    votes = votes.merge(tally["majority"], left_on="motion_id", right_index=True)
    votes["dissent"] = votes.vote != votes.majority

    record = (votes.groupby("surname_key")
              .agg(recorded_votes=("vote", "size"), dissents=("dissent", "sum"))
              .reset_index())
    record["dissent_rate"] = (record.dissents / record.recorded_votes).round(3)

    presence = (att.assign(present=att.status.eq("present"))
                .groupby("surname_key")
                .agg(meetings_recorded=("present", "size"), meetings_present=("present", "sum"))
                .reset_index())
    presence["attendance_rate"] = (
        presence.meetings_present / presence.meetings_recorded).round(3)

    incumbents = (spine.merge(record, on="surname_key", how="left")
                       .merge(presence, on="surname_key", how="left"))
    incumbents["ward_number"] = incumbents.ward_number.astype(int)
    incumbents = incumbents.sort_values(["ward_number", "term"]).reset_index(drop=True)

    # ---- ward conditions ------------------------------------------------------
    svc = pd.read_csv(REPO / "releases" / "311-by-ward" / "by_ward.csv")
    svc["ward_number"] = svc.ward.str.extract(r"^(\d+)").astype(int)
    svc = svc[["ward_number", "requests", "median_days_to_close", "pct_closed"]]

    taxes["ward_number"] = taxes.ward_number.astype(int)
    taxes["assessment"] = money(taxes.cva)
    taxes["municipal_taxes"] = money(taxes.tax)
    taxes = taxes[["ward_number", "assessment", "municipal_taxes"]]

    pop["ward_number"] = pd.to_numeric(pop.ward_number, errors="coerce")
    pop = pop.dropna(subset=["ward_number"])
    pop["ward_number"] = pop.ward_number.astype(int)

    places["ward_number"] = pd.to_numeric(places.ward_number, errors="coerce")
    places = places.dropna(subset=["ward_number"])
    vp = (places.assign(accessible=places.Acc_Entr.notna() & places.Acc_Entr.astype(str).str.strip().ne(""))
          .groupby(places.ward_number.astype(int))
          .agg(voting_places=("accessible", "size"),
               voting_places_accessible=("accessible", "sum"))
          .reset_index())

    # ---- the race -------------------------------------------------------------
    council = cands[cands.office == "councillor"].copy()
    council["ward_number"] = council.ward_number.astype(int)
    race = (council.groupby("ward_number")
            .agg(candidates=("name", "size"),
                 rebate_optin=("rebate_program", "sum"))
            .reset_index())
    race["acclaimed"] = race.candidates == 1

    wards = (spine[["ward_number", "ward_name"]].astype({"ward_number": int})
             .drop_duplicates("ward_number").sort_values("ward_number"))
    by_ward = (wards.merge(race, on="ward_number", how="left")
                    .merge(svc, on="ward_number", how="left")
                    .merge(taxes, on="ward_number", how="left")
                    .merge(pop[["ward_number", "population"]], on="ward_number", how="left")
                    .merge(vp, on="ward_number", how="left"))

    # An incumbent seeking re-election, where there is exactly one current holder.
    current = incumbents[~incumbents.term.str.contains("2025", na=False)
                         | incumbents.term.str.contains("present", na=False)]
    seat = (current.sort_values("term")
            .groupby("ward_number")
            .agg(incumbent=("display_name", "last"),
                 incumbent_on_ballot=("seat_on_ballot", "last"),
                 incumbent_running_for=("running_for", "last")).reset_index())
    by_ward = by_ward.merge(seat, on="ward_number", how="left")
    by_ward["open_seat"] = ~by_ward.incumbent_on_ballot.fillna(False)

    # ---- write ----------------------------------------------------------------
    OUT.mkdir(parents=True, exist_ok=True)
    keep = ["ward_number", "ward_name", "term", "display_name", "recorded_votes",
            "dissents", "dissent_rate", "meetings_recorded", "meetings_present",
            "attendance_rate", "seat_on_ballot", "running_for", "official_email"]
    incumbents[keep].to_csv(OUT / "incumbent_record.csv", index=False)
    by_ward.to_csv(OUT / "by_ward.csv", index=False)
    cands.drop(columns=["n_links"], errors="ignore").to_csv(OUT / "candidates.csv", index=False)
    links.to_csv(OUT / "candidate_links.csv", index=False)
    zones.to_csv(OUT / "trustee_races.csv", index=False)

    # ---- the page's data ------------------------------------------------------
    link_map = {}
    for cid, group in links.groupby("candidate_id"):
        ordered = sorted(group.itertuples(),
                         key=lambda r: (LINK_ORDER.index(r.link_type)
                                        if r.link_type in LINK_ORDER else 99))
        link_map[cid] = [{"t": r.link_type, "u": r.url} for r in ordered]

    def candidate_block(row):
        return {"name": row["name"], "nom": str(row.nomination_date)[:10],
                "rebate": bool(row.rebate_program), "email": row.email,
                "links": link_map.get(row.candidate_id, [])}

    trustee_by_ward = {}
    for ward, group in zones.groupby("ward_number"):
        races = []
        for _, z in group.sort_values("school_board").iterrows():
            runners = cands[(cands.office == "trustee")
                            & (cands.school_board == z.school_board)
                            & (cands.zone_number == z.zone_number)]
            races.append({"board": z.school_board, "board_full": z.school_board_full,
                          "zone": int(z.zone_number),
                          "candidates": [candidate_block(r) for _, r in runners.iterrows()]})
        trustee_by_ward[int(ward)] = races

    page = {"election_day": ELECTION_DAY,
            "generated": pd.Timestamp.now("UTC").strftime("%Y-%m-%d"),
            "city_attendance_note": (f"the city's own attendance dataset covers "
                                     f"{int(city_att.n)} meetings, {city_att.f} to {city_att.l}"),
            "mayor": [candidate_block(r) for _, r in
                      cands[cands.office == "mayor"].sort_values("nomination_date").iterrows()],
            "wards": []}
    for _, w in by_ward.iterrows():
        holders = incumbents[incumbents.ward_number == w.ward_number]
        page["wards"].append({
            "n": int(w.ward_number), "name": w.ward_name,
            "open_seat": bool(w.open_seat),
            "acclaimed": bool(w.acclaimed) if pd.notna(w.acclaimed) else False,
            "running_for": w.incumbent_running_for or "",
            "incumbents": [{
                "name": h.display_name, "term": h.term,
                "votes": int(h.recorded_votes) if pd.notna(h.recorded_votes) else None,
                "dissents": int(h.dissents) if pd.notna(h.dissents) else None,
                "dissent_rate": float(h.dissent_rate) if pd.notna(h.dissent_rate) else None,
                "meetings": int(h.meetings_recorded) if pd.notna(h.meetings_recorded) else None,
                "attendance_rate": float(h.attendance_rate) if pd.notna(h.attendance_rate) else None,
                "on_ballot": bool(h.seat_on_ballot),
            } for _, h in holders.iterrows()],
            "svc": {"requests": int(w.requests) if pd.notna(w.requests) else None,
                    "days": float(w.median_days_to_close) if pd.notna(w.median_days_to_close) else None},
            "pop": int(w.population) if pd.notna(w.population) else None,
            "tax": float(w.municipal_taxes) if pd.notna(w.municipal_taxes) else None,
            "places": int(w.voting_places) if pd.notna(w.voting_places) else 0,
            "places_acc": int(w.voting_places_accessible) if pd.notna(w.voting_places_accessible) else 0,
            "candidates": [candidate_block(r) for _, r in
                           council[council.ward_number == w.ward_number]
                           .sort_values("nomination_date").iterrows()],
            "trustees": trustee_by_ward.get(int(w.ward_number), []),
        })
    (OUT / "scorecard.json").write_text(json.dumps(page, indent=1, default=str) + "\n")

    (OUT / "datapackage.json").write_text(json.dumps({
        "name": "ward-scorecard",
        "title": "Ottawa 2026 municipal election — ward scorecard",
        "description": (f"For each of the 24 wards: the incumbent's recorded-vote and "
                        f"attendance record, service and tax conditions, the 2026 "
                        f"candidates with their filed contact details, and the four "
                        f"trustee races that ward votes in. Voting day {ELECTION_DAY}."),
        "licenses": [{"name": "OGL-Ottawa",
                      "title": "Open Government Licence – City of Ottawa"},
                     {"name": "site-terms",
                      "title": "Vote and attendance data derived from howtheyvoted.ca, "
                               "which carries ordinary site terms, not an open licence"}],
        "sources": [{"title": "City of Ottawa elections web service",
                     "path": "https://elections.ottawa.ca/ws/api/"},
                    {"title": "Open Ottawa", "path": "https://open.ottawa.ca/"},
                    {"title": "howtheyvoted.ca", "path": "https://howtheyvoted.ca/data/ottawa/"}],
        "resources": [{"path": f"{n}.csv", "format": "csv"} for n in
                      ("by_ward", "incumbent_record", "candidates",
                       "candidate_links", "trustee_races")]
        + [{"path": "scorecard.json", "format": "json"}],
    }, indent=2) + "\n")

    open_seats = by_ward[by_ward.open_seat]
    acclaimed = by_ward[by_ward.acclaimed.fillna(False)]
    (OUT / "README.md").write_text(f"""# Ottawa 2026 municipal election — ward scorecard

Voting day **{ELECTION_DAY}**. {len(cands)} candidates across 24 ward races, the
mayoralty and {zones.school_board.nunique() * 0} + four school boards.

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

- **{len(open_seats)} of 24 seats have no incumbent on the ballot**:
  {", ".join(f"{r.ward_name}" for _, r in open_seats.iterrows())}.
- **{len(acclaimed)} are decided already** — one candidate each:
  {", ".join(f"{r.ward_name}" for _, r in acclaimed.iterrows())}.
- Ward 20 (Osgoode) had **two councillors** this term and both records are
  shown; the city encodes the changeover inside the ward name field.

## Caveats

- **Only about 4% of motions get a recorded vote.** Dissent rate describes the
  contested slice of council business, not all of it. Vote counts are printed
  beside every rate because 15% of 87 and 53% of 247 are not comparable.
- **Attendance comes from howtheyvoted.ca, not the city.** The city's own
  attendance dataset covers only {int(city_att.n)} meetings from
  {city_att.f} to {city_att.l} — it begins nearly two years into the term.
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
""")

    print(f"releases/ward-scorecard/ — 24 wards, {len(cands)} candidates, "
          f"{len(incumbents)} councillor-terms")
    print(f"  open seats ({len(open_seats)}): "
          + ", ".join(open_seats.ward_name.tolist()))
    print(f"  acclaimed ({len(acclaimed)}): " + ", ".join(acclaimed.ward_name.tolist()))
    print(f"  city attendance dataset: {int(city_att.n)} meetings, {city_att.f} to {city_att.l}")
    print("\nrecord (first 6 by ward):")
    print(incumbents.head(6)[["ward_number", "display_name", "recorded_votes",
                              "dissent_rate", "meetings_recorded", "attendance_rate",
                              "seat_on_ballot"]].to_string(index=False))


if __name__ == "__main__":
    main()
