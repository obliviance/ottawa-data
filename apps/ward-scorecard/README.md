# Your ward, 2026

Published: https://claude.ai/code/artifact/89a3d8d7-549b-4652-a636-a8a52710c6e2

Ward scorecard for the 26 October 2026 Ottawa municipal election. Data and
regeneration: [`releases/ward-scorecard`](../../releases/ward-scorecard).

    python3 spine/entities.py
    python3 explorations/ward_scorecard.py
    python3 apps/ward-scorecard/build.py

`template.html` is the page; `build.py` inlines `scorecard.json` into
`index.html`. The page carries its own data rather than fetching it — an
artifact is a single file, and a voter guide that breaks when a host goes away
is worse than useless.

House layout from [`apps/council-recorded-votes`](../council-recorded-votes),
with one structural difference: the other finding pages lead with a chart and an
argument, this leads with a ward finder and makes no argument at all. Nothing is
scored, and the wards are in number order — sorting them by "worst 311 response"
would be an editorial act, and the neutral version is the one that doesn't
otherwise exist.
