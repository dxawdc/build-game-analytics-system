# UA and marketing analytics

Read this when the request involves paid acquisition (买量/投放), channel evaluation, creative performance,
attribution, budget allocation, payback, or ad fraud. Product-side analysis lives in the other references;
this file covers the money-out side and the boundary where channel data meets game data.

## 1. Three data layers — never mix them in one table

| Layer | Owner of truth | Typical fields | Reliability caveat |
|---|---|---|---|
| Ad platform / network | channel | spend, impressions, clicks, CTR, CVR, eCPM, bid, campaign state | self-reported, self-attributing, deduped by the seller |
| Landing / store | store or landing host | store page views, download starts, second-hop rate, load and dwell time | often partially observable; store-side is aggregated only |
| In-game behavior | you | install, first launch, register, role creation, retention, purchases, LTV | authoritative for value, but attribution is inherited |

Reconcile top-down (spend → impressions → clicks → installs) and bottom-up (cohort size → activation → value)
before any conclusion. Persistent gaps are normal; unexplained gaps that move week to week are a data incident.

## 2. Delivery identities

```text
spend        = impressions × eCPM / 1000
installs     = impressions × CTR × CVR
CPI          = eCPM / (1000 × CTR × CVR)
CAC(target)  = spend / entities reaching the target action
ROAS_Dn      = attributable net revenue through day n / attributable spend
```

These identities are the diagnostic backbone: any CPI move must decompose into eCPM, CTR, or CVR.
Report volume alongside every rate — a great CTR on 2,000 impressions decides nothing.

## 3. Campaign diagnosis decision tree

**Cost rose / quality fell suddenly**
1. Check for a change event first: bid, budget, creative swap, audience edit, tracking/SDK change, store page change, app version, price change.
2. Decompose CPI into eCPM, CTR, CVR. Each points elsewhere: eCPM → auction competition or bid; CTR → creative or placement; CVR → store page, package size, device/OS mix, or landing failure.
3. Check platform/region/device mix shift — the same campaign can drift into cheaper, worse inventory.
4. Verify the measurement path before believing the drop (SDK version, attribution outage, consent changes).
5. If a change was made, test recovery by reverting one variable at a time; throttling volume (控量) then restoring is a common probe.

**Campaign cannot spend / lost volume (缩量)**
- Falling eCPM with stable CTR/CVR → bid or budget uncompetitive, or auction competition rose.
- Falling CTR → creative fatigue; check impression-weighted creative age and frequency.
- Falling CVR → store or funnel regression, not creative.
- Frequent bid edits reset the platform's learning; count edits per campaign as a diagnostic dimension.

**Quality mismatch: cheap installs, bad cohorts**
- Compare cohort D1/D3/D7 retention and first-value rate by campaign, creative, placement, and geo.
- Check fraud signals (§6) before concluding "bad audience".
- Check incentivized or rewarded-install inventory separately.

## 4. Creative analysis

Track creative as a first-class entity with a stable ID and a tag taxonomy (theme, hook type, first-3s content,
format, aspect, language, actor, gameplay-vs-CG, call to action). Then measure:

- creative lifecycle: first-impression date, impression-weighted age, spend share, decay curve;
- fatigue: CTR/CVR by cumulative impressions and by frequency band;
- duplication: near-identical creatives competing in the same audience;
- downstream value: cohort retention and ROAS by creative, not just CTR;
- deduplicated learning: creative-level results are confounded by the platform's own delivery optimization —
  a creative that "won" may simply have been given better inventory.

Creative-level attribution is directional evidence. To claim a creative caused better value, use a controlled
split (separate campaigns with matched budgets/audiences, or platform experiment tools), and predefine the horizon.

## 5. Attribution

- Use one MMP/attribution source of record (AppsFlyer, Adjust, SolarEngine, platform-native) and version its config.
- Document: attribution windows (click and view-through), lookback, reattribution/reinstall rules, dedup order,
  self-attributing network precedence, deep-link handling, and organic classification.
- On privacy-restricted platforms (SKAdNetwork/AdAttributionKit, consent-gated Android, China store variants),
  expect aggregated, delayed, coarse, and postback-window-truncated data. Never join it to user-level tables as if exact.
- Keep **attribution** (accounting split of credit) separate from **incrementality** (would this have happened anyway).
  For incrementality use geo holdouts, PSA/ghost-bid tests, staggered rollout, or platform lift tests.
- Organic contamination: paid campaigns lift organic installs; comparing paid ROAS against total revenue double-counts.

## 6. Fraud and invalid traffic

Look for signature patterns rather than single metrics:

- CTIT (click-to-install-time) distribution: spikes at implausibly short or long delays;
- click flooding: huge click volume, tiny CVR, broad device spread;
- click injection: install-time clicks arriving just before first open;
- device farms/emulators: narrow device/OS/resolution clusters, reset advertising IDs, datacenter IPs;
- SDK spoofing: installs with no plausible in-game event sequence;
- retention cliffs: normal D0 then near-zero D1, or unnaturally flat retention;
- incentivized traffic mislabeled as UA: high install, near-zero first-value.

Hold suspected traffic in a separate class rather than deleting it; keep the exclusion rule versioned so historical
metrics remain reproducible. Coordinate any enforcement or refund claim with the channel contract terms.

## 7. Payback, budget, and scaling

```text
payback day  = min{ n : cumulative net contribution per acquired entity ≥ fully loaded CAC }
```

- State the revenue basis: gross bookings, post-platform-fee, post-channel-share, or contribution margin.
  A payback computed on gross bookings can be off by the entire share chain.
- Include all cost in CAC when the decision is investment-level: media spend, agency/ad-serving fees,
  creative production, incentives, and (where relevant) variable server and payment costs.
- Cash timing matters separately from profitability: a 12-month-payback title can be unfundable.
- Scale decisions need **marginal** ROAS, not average. Rising spend usually raises CPI and shifts audience quality;
  model the spend-response curve per geo/channel and re-estimate as you scale.
- Test-and-learn cadence: agree in advance on a minimum learning window and volume per campaign before judging it,
  and hold the rule constant across campaigns so results are comparable. Common practice quotes a few days for
  "is it viable" and about a week for "what is the cost baseline" — calibrate those windows against your own
  cohort maturity curves rather than adopting them as given.
- For early decisions use a backtested early-horizon predictor (see [growth-accounting-and-forecasting.md](growth-accounting-and-forecasting.md))
  and report its error band, not a point estimate.

## 8. Global and multi-region UA

- Segment by geo tier, platform, language, and payment infrastructure; blended global CPI/ROAS hides everything.
- Currency: state FX policy for both spend and revenue; report a stable reporting currency plus local currency.
- Payment culture differences change payer conversion and price-point mix, not just volume.
- Store and platform differences (iOS vs Android vs domestic Android channels vs mini-game platforms) change
  attribution availability, share chain, and even the meaning of "install".
- Run region-segmented readouts on every experiment and campaign test; a globally flat result often hides
  opposing regional effects.

## 9. Reporting checklist

Every UA readout should state: date range and cohort maturity, attribution source and windows, spend scope,
revenue basis, currency and FX policy, exclusion rules, volume alongside every rate, and whether the claim is
attributed, correlational, or experimentally identified.
