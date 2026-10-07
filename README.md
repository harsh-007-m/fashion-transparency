# Fashion Trend Analysis: What factors affect Sustainable Fashion?
--- 

An analysis to understand the relationship between the parameters:
- Thrift Store
- Sustainable Fashion
- Cruelty Free
- Fast Fashion


**Status:** Work in progress (Day 1 of 7: data collected and inspected)

---

**About the Data**
| Item | Details |
|---|---|
| Source | Google Trends (trends.google.com), "Interest over time" |
| Search type / category | Web Search / All categories |
| Terms | [term 1], [term 2], [term 3], [term 4] (queried together so they share one scale) |
| Regions | India, Worldwide |
| Date range | [January 2016] to [last full month], [monthly] resolution |
| Date downloaded | [YYYY-MM-DD] |
| Raw files | `data/raw/trends_india_[date].csv`, `data/raw/trends_world_[date].csv` |
 
---

**URLS**

- India: `https://trends.google.com/trends/explore?date=2016-01-01%202026-10-08&geo=IN&q=Thrift%20Stores,fast%20fashion,sustainable%20fashion,cruelty%20free&hl=en&legacy`

- World: `https://trends.google.com/trends/explore?date=2016-01-01%202026-10-08&q=Thrift%20Stores,fast%20fashion,sustainable%20fashion,cruelty%20free&hl=en&legacy`

 
## Project structure
 
```
data/raw/        untouched downloads (never edited)
data/clean/      cleaned tables produced by scripts
src/             scripts, run in numbered order
notebooks/       analysis notebooks
README.md
requirements.txt
```

## Roadmap
 
- [x] Day 1: set up, collect raw data, inspect
- [ ] Day 2: clean data, first charts (India vs world)
- [ ] Day 3: release-date table, spike detection
- [ ] Day 4: label spikes, lift and permutation test
- [ ] Day 5: notebook and README with findings
- [ ] Day 6: polish and publish
- [ ] Optional: brand newsroom counts, React dashboard
 
