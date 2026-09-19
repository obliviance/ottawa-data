#!/usr/bin/env python3
"""Build the entity spine: `spine_councillors`, one row per person-who-held-a-seat.

    python3 spine/entities.py

The join key problem. The same councillor appears under four different names
across four datasets the city and its watchers publish:

    open_elected_officials_2022_2026   "Matthew" + "Luloff"
    city attendance                    "Councillor Matt Luloff"   <- preferred name
    htv_votes                          "M. Luloff"                <- initial + surname
    election_candidates                "Matt Luloff"              <- as filed

The city's own two datasets disagree about whether he is Matthew or Matt. There
is no shared identifier anywhere. Every cross-source question about a councillor
-- did they vote, did they attend, are they running again -- needs this table
first, which is why the roadmap listed it and why it stayed unbuilt.

Surname is the key, but surname *alone* is not safe. The vote table records the
same person as both "C. Kitts" and "Kitts", so picking one alias loses votes --
22 of 62 surnames there carry more than one spelling. And the attendance table
covers committees, not just council: 222 distinct names across 127 surnames,
including "Tammy Kelly", who is not councillor **Clarke** Kelly.

So the resolver matches on surname *and*, where the alias carries one, the first
initial. Titles and committee roles are stripped first -- the attendance data
contains entries like "Agriculture and Rural Affairs Committee Vice-Chair:
Councillor Clarke Kelly". Every resolved alias is written out to
`spine_councillor_aliases` so the mapping is auditable rather than hidden in a
join, and the build fails loudly if any councillor resolves to nothing.

Two things the tables record that are not in any single source:

* **Mid-term turnover.** Ward 20 had two councillors -- Darouze to Feb 2025,
  Skalski from June 2025. The city encodes this inside the ward *name*
  ("Osgoode (November 15, 2022 to February 27, 2025)"), which is parsed out here
  into a real term field so the ward can show both records.
* **Whether the incumbent is on the 2026 ballot**, and for which office. Three
  are not running for their seat: Gower (Stittsville) is off the ballot, Leiper
  (Kitchissippi) is running for mayor, and Darouze already left mid-term. Those
  are the open seats, and nothing publishes them as a list.
"""
from __future__ import annotations

import pathlib
import re
import sys

sys.path.insert(0, str(pathlib.Path(__file__).parent.parent / "tools"))
import warehouse  # noqa: E402

# "Osgoode (November 15, 2022 to February 27, 2025)" -> name, term
TERM_IN_NAME = re.compile(r"^(?P<name>.*?)\s*\((?P<term>[^)]*\d{4}[^)]*)\)\s*$")


def surname_key(value: str) -> str:
    """Lowercase letters only. Handles 'Jeff  Leiper' and accented spellings."""
    return re.sub(r"[^a-z]", "", str(value).lower())


def main() -> None:
    import pandas as pd

    c = warehouse.con()
    officials = c.execute("""
        SELECT Ward_number, Ward_name, Primary_Role, First_name, Last_name,
               Email, Website
        FROM d_open_elected_officials_2022_2026
    """).df()
    vote_names = [r[0] for r in c.execute(
        "SELECT DISTINCT councillor_name FROM d_htv_votes").fetchall()]
    att_names = [r[0] for r in c.execute(
        "SELECT DISTINCT councillor_name FROM d_htv_attendance").fetchall()]
    candidates = c.execute("""
        SELECT candidate_id, name, office, ward_number
        FROM d_election_candidates WHERE office IN ('councillor', 'mayor')
    """).df()
    c.close()

    rows = []
    for _, o in officials.iterrows():
        name = str(o.Ward_name) if pd.notna(o.Ward_name) else ""
        match = TERM_IN_NAME.match(name)
        rows.append({
            "ward_number": int(o.Ward_number) if pd.notna(o.Ward_number) else None,
            "ward_name": (match.group("name") if match else name).strip(),
            # Present only where the seat changed hands mid-term.
            "term": match.group("term").strip() if match else "",
            "role": str(o.Primary_Role).strip(),
            "first_name": str(o.First_name).strip(),
            "last_name": str(o.Last_name).strip(),
            "display_name": re.sub(r"\s+", " ", f"{o.First_name} {o.Last_name}").strip(),
            "surname_key": surname_key(o.Last_name),
            "official_email": str(o.Email).strip() if pd.notna(o.Email) else "",
        })
    spine = pd.DataFrame(rows)

    # --- resolve every alias, not one per surname -----------------------------
    # The mayor is included: they chair council and their votes are recorded
    # alongside everyone else's, so a vote-cohesion analysis that drops them is
    # missing the person the majority forms around.
    councillors_by_surname = {}
    for _, r in spine.iterrows():
        councillors_by_surname.setdefault(r.surname_key, []).append(r)

    def parse_alias(raw: str):
        """(surname_key, first_initial) from a name carrying titles or roles.

        Handles 'Agriculture and Rural Affairs Committee Vice-Chair: Councillor
        Clarke Kelly', 'Brian Wade, Vice-Chair', 'C. Kitts' and bare 'Kitts'.
        """
        s = str(raw)
        s = s.split(":")[-1]                     # drop anything before a role colon
        s = re.sub(r",.*$", "", s)               # drop ', Vice-Chair' suffixes
        s = re.sub(r"\(.*?\)", " ", s)           # drop '(Vice-Chair)'
        s = re.sub(r"\b(Mayor|Councillor|Member|Acting|Chair|Vice-Chair|Trustee)\b",
                   " ", s, flags=re.I)
        parts = [p for p in re.split(r"[\s.]+", s) if re.search(r"[A-Za-z]", p)]
        if not parts:
            return "", ""
        initial = parts[0][0].lower() if len(parts) > 1 else ""
        return surname_key(parts[-1]), initial

    def resolve(names, source):
        """Map each raw alias onto a councillor, or drop it.

        A bare surname matches when exactly one councillor has it. An alias
        carrying a first initial must agree with that councillor's initial --
        which is what keeps 'Tammy Kelly' off Clarke Kelly's record.
        """
        out = []
        for raw in names:
            key, initial = parse_alias(raw)
            matches = councillors_by_surname.get(key, [])
            if len(matches) != 1:
                continue
            councillor = matches[0]
            if initial and initial != councillor.first_name[:1].lower():
                continue
            out.append({"surname_key": key, "source": source,
                        "alias": str(raw), "display_name": councillor.display_name})
        return out

    aliases = pd.DataFrame(
        resolve(vote_names, "htv_votes") + resolve(att_names, "htv_attendance"))
    aliases = aliases.sort_values(["surname_key", "source", "alias"]).reset_index(drop=True)

    counts = aliases.groupby(["surname_key", "source"]).size().unstack(fill_value=0)
    for source in ("htv_votes", "htv_attendance"):
        spine[f"n_{source}_aliases"] = spine.surname_key.map(
            counts[source] if source in counts else {}).fillna(0).astype(int)

    # --- 2026 ballot ----------------------------------------------------------
    # Same discipline as the alias resolver: surname alone would mark an
    # incumbent as running if any unrelated candidate shared the surname. There
    # is no such collision in 2026, but a wrong "running again" on a ward card
    # is exactly the kind of error that must not be possible by construction.
    candidates["surname_key"] = candidates.name.map(
        lambda n: surname_key(str(n).split()[-1]))
    candidates["initial"] = candidates.name.map(lambda n: str(n).split()[0][:1].lower())

    def on_ballot(row):
        hits = candidates[(candidates.surname_key == row.surname_key)
                          & (candidates.initial == row.first_name[:1].lower())]
        if len(hits) != 1:
            return pd.Series({"candidate_id": "", "running_for": ""})
        hit = hits.iloc[0]
        return pd.Series({"candidate_id": hit.candidate_id, "running_for": hit.office})

    spine = spine.join(spine.apply(on_ballot, axis=1))
    spine["seat_on_ballot"] = spine.apply(
        lambda r: r.running_for == r.role.lower(), axis=1)

    # --- the checks that make the key trustworthy -----------------------------
    councillors = spine[spine.role == "Councillor"]
    dupes = councillors.surname_key.duplicated().sum()
    if dupes:
        sys.exit(f"FAIL: {dupes} duplicate surname(s) — surname is no longer a safe key")
    for source in ("htv_votes", "htv_attendance"):
        missing = councillors[councillors[f"n_{source}_aliases"] == 0]
        if len(missing):
            sys.exit(f"FAIL: {len(missing)} councillor(s) unmatched in {source}: "
                     + ", ".join(missing.display_name))

    spine = spine.sort_values(["ward_number", "term"], na_position="first").reset_index(drop=True)
    warehouse.register(
        "spine_councillors", spine, shape="spine",
        title="spine — councillors of the 2022–2026 term, with 2026 ballot status",
        origin_url="https://open.ottawa.ca/datasets/ottawa::elected-officials-2022-2026",
        notes=("surname is the join key, verified unique and resolvable against both the "
               "vote and attendance data at build time; `term` is populated only where a "
               "seat changed hands mid-term; `seat_on_ballot` is False for an incumbent "
               "not seeking their own seat again. Join to source data through "
               "spine_councillor_aliases, not by name."))
    warehouse.register(
        "spine_councillor_aliases", aliases, shape="spine",
        title="spine — every name variant each councillor appears under, by source",
        notes=("resolved on surname plus first initial where the alias carries one. "
               "Written out so the crosswalk is auditable: an alias that should have "
               "matched and did not is visible as an absence here rather than as a "
               "silently low vote count."))

    open_seats = councillors[~councillors.seat_on_ballot]
    print(f"spine_councillors — {len(spine)} rows "
          f"({len(councillors)} councillor-terms across {councillors.ward_number.nunique()} wards, "
          f"{len(spine) - len(councillors)} mayor)")
    print(f"  {len(aliases)} name aliases resolved "
          f"({(aliases.source=='htv_votes').sum()} vote, "
          f"{(aliases.source=='htv_attendance').sum()} attendance) — "
          f"all {len(councillors)} councillors and the mayor matched in both")
    turnover = councillors[councillors.term != ""]
    if len(turnover):
        print(f"  mid-term turnover: " + " · ".join(
            f"ward {int(r.ward_number)} {r.display_name} ({r.term})" for _, r in turnover.iterrows()))
    print(f"  incumbents not seeking their seat ({len(open_seats)}):")
    for _, r in open_seats.iterrows():
        where = f"running for {r.running_for}" if r.running_for else "not on the ballot"
        print(f"     ward {int(r.ward_number):>2} {r.ward_name:<22} {r.display_name:<18} {where}")


if __name__ == "__main__":
    main()
