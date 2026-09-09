# sample — Engage Ottawa

- source id `engage-ottawa` · catalogue access `['api', 'html']` · operator *City of Ottawa*
- url <https://engage.ottawa.ca/projects>
- captured: 
- headless render: 24,247 chars, 10 data XHR
- backing endpoints seen: `https://engage.ottawa.ca/api/v2/home_page_revisions?filters%5Bsort%5D%5Bid%5D=desc&filters`; `https://engage.ottawa.ca/api/v2/theme/`; `https://engage.ottawa.ca/api/v2/navigation_links?filters%5Bsearch%5D=header&filters%5Bsort`

**Sample status:** landing page only — data is one navigation step deeper

**A full parser needs:**

EngagementHQ /api/v2/* works in-browser but 404s on direct fetch (needs browser-context headers); drive via the CDP browser.
