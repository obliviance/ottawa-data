# questions/

`backlog.csv` — the running list of things worth investigating. One row per
question:

| field | meaning |
| --- | --- |
| `id` | `q0001`, … (auto) |
| `question` | the hypothesis / thing to look at |
| `datasets` | warehouse dataset_ids it needs (space-separated) |
| `join_type` | e.g. `ward`, `date`, `entity`, `spatial`, `none` |
| `value` / `feasibility` / `novelty` | 1–5, filled by a human |
| `status` | `new` → `picked` → `building` → `shipped` / `parked` |
| `added` | date |

`tools/profile.py` appends templated questions per dataset. Curate by hand:
delete noise, score the rest, sort by `value × novelty × feasibility`. Review weekly.
