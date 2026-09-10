# sample — Development Applications Search

- source id `devapps` · catalogue access `['api', 'html']` · operator *City of Ottawa*
- url <https://devapps.ottawa.ca/>
- captured: `api_feature_all_sample.json`
- headless render: 1,917 chars, 3 data XHR
- backing endpoints seen: `https://devapps-restapi.ottawa.ca/devapps/feature/all?authKey=<redacted>`; `https://devapps-restapi.ottawa.ca/devapps/apptype/all?authKey=<redacted>`; `https://devapps-restapi.ottawa.ca/devapps/ward/all?authKey=<redacted>`

**Sample status:** real data sample saved

**A full parser needs:**

devapps-restapi.ottawa.ca/devapps/{feature,apptype,ward}/all — client-embedded authKey (re-extract from the page). feature/all = all 813 applications. Sampled + in warehouse.
