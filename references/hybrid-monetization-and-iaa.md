# IAA and hybrid monetization analytics

Read this for ad-monetized products (IAA), mini-game/instant-platform titles, and hybrid IAP+IAA products.
Ad revenue is not "IAP with a different SKU": its supply chain, latency, identity constraints, and player-experience
trade-offs are different, and it fails in ways IAP does not.

## 1. Revenue identity

```text
ad revenue
= DAU
× ad-exposed rate            (exposed actives / DAU)
× impressions per exposed    (ad load)
× eCPM / 1000

ad ARPDAU = ad revenue / DAU = ad-exposed rate × impressions per exposed × eCPM / 1000
```

Every ad-revenue movement decomposes into these four factors. Diagnose in that order before touching design:
a drop caused by eCPM (market/mediation) demands a different action than one caused by exposure or ad load.

For hybrid products:

```text
total ARPDAU = IAP ARPDAU + ad ARPDAU
cohort LTV   = IAP LTV + ad LTV        (state whether ad LTV is net of network/platform fees)
```

## 2. Delivery funnel and metric set

Instrument the full ad lifecycle server-authoritatively where possible:

```text
opportunity → request → fill → render (impression) → view/complete → reward grant → revenue postback
```

| Metric | Formula | Notes |
|---|---|---|
| Ad opportunity rate | opportunities shown to eligible actives / eligible actives | design-side, not network-side |
| Fill rate | filled responses / requests | low fill can be floor price, geo, or mediation config |
| Show rate | rendered impressions / filled responses | gap here is usually client-side timing or user exit |
| Ad penetration | actives with ≥1 impression / DAU | the "ad-exposed rate" in the identity |
| Ad load | rendered impressions / ad-exposed active | report distribution, not just mean |
| Rewarded start rate | rewarded starts / rewarded entry-point views | measures offer attractiveness |
| Rewarded completion | completed views / started views | drops signal creative length, network, or connectivity |
| Reward grant success | rewards granted / completions | failures are a trust and support incident |
| eCPM | ad revenue / impressions × 1000 | slice by format, network, geo, placement, day |
| Ad ARPDAU | net ad revenue / DAU | the summary metric; always paired with retention |
| Time to first ad | first impression time − first launch | early aggressive exposure trades retention for revenue |
| Misclick indicators | immediate back-out / bounce after impression | quality guardrail for banner/native placements |

Revenue arrives from networks with **delay and revision**. Define a revenue-restatement policy: which day's number
is provisional, when it finalizes, and how dashboards show revised history.

## 3. eCPM: what actually moves it

eCPM is largely exogenous. Before attributing an eCPM change to your own work, check calendar and market effects.

Levers you control:
- **format mix** — rewarded video, interstitial, banner, native, and app-open have systematically different eCPM
  and different experience costs. The ordering is stable enough to plan with; the levels are not. Public figures
  for format eCPM ranges are undated, geo-blended, and vendor-sourced — measure your own by geo and week.
- **mediation setup** — number of demand sources, waterfall vs in-app bidding, floor prices, per-geo waterfalls,
  timeout settings. Floors trade fill rate against eCPM; measure the product of the two (ad revenue), not either alone.
- **placement design** — natural break points (level fail, resource shortage, run end) versus interruptions in the
  core loop; explicit reward framing ("+50 gold") versus vague framing.
- **inventory quality** — geo/device mix, session length, viewability, and whether requests are cached and timely.
- **frequency and pacing** — caps per session and per day; over-serving depresses both eCPM and retention.

Exogenous factors: seasonal advertiser budgets, quarter boundaries, holiday spikes, geo mix drift, network policy
changes, and platform privacy changes. Always compare against the same weekday and geo composition.

## 4. Hybrid monetization: the cannibalization question

The core question is whether an ad impression displaces a purchase, or converts value that would never be paid.

- Segment by monetization state (non-payer, low, mid, whale) and measure ad exposure, ad revenue, and IAP revenue
  per segment. Whales usually should see less advertising; verify rather than assume.
- Measure "remove ads" or ad-free bundle purchase as a monetization path with its own funnel.
- Rewarded ads that grant soft currency are an **economy source** — route them into the economy ledger with a
  reason code, and monitor inflation and sink pressure. See the economy section of [metric-library.md](metric-library.md).
- The only defensible cannibalization estimate comes from an experiment: randomize ad load, placement, or eligibility
  and read total ARPDAU (IAP + ad), retention, playtime, and complaint guardrails together.
- Long-run effects exceed the experiment window in many titles. Prefer a longer holdout on a small population over
  a short test on a large one, and pre-register the guardrails.

## 5. Guardrails specific to IAA

Never optimize ad revenue without simultaneous readouts on:

- D1/D7 retention and session length for the exposed population;
- ad load distribution tail (the P95 player, not the mean);
- crash/ANR, load time, and memory during ad rendering (SDKs are a common stability regressor);
- misclick and immediate-exit rate per placement;
- reward-grant failure and related support tickets;
- opt-out/consent rates and regional privacy constraints;
- child-directed and age-gating requirements where applicable;
- store policy compliance for ad formats and frequency.

Verify current platform and regional policy requirements separately; they change and are not encoded here.

## 6. Mini-game and instant-platform specifics

Mini-game platforms (including WeChat mini-games and similar instant-play channels) change the analytics substrate:

- **Identity**: platform-scoped user IDs, no device advertising ID, limited cross-app joining. Attribution is
  platform-mediated, so build the acquisition analysis around platform-provided channels and self-served links.
- **Install has no meaning**; the funnel starts at first launch or first frame. Retention anchors must be re-chosen.
- **Session pattern** skews to short, high-frequency, low-commitment play — retention and ad-load norms from
  installed apps do not transfer.
- **Revenue share and settlement** differ from app stores; pin the share chain before computing ROAS or payback.
- **Traffic mix** blends paid, platform recommendation/organic, and social sharing loops; separate them explicitly,
  because sharing-driven growth responds to different levers than paid.
- Platform-native analytics dashboards use their own definitions; treat them as a partner source to reconcile
  against, not as your dictionary.

## 7. Diagnosis playbook: ad revenue dropped

1. Confirm the number is final, not a pending/restated network figure.
2. Decompose: DAU × exposed rate × ad load × eCPM. Identify which factor moved and by how much.
3. If eCPM: slice by network, geo, format, placement, and day-of-week; check mediation/floor changes and market seasonality.
4. If fill or show rate: check SDK/mediation version, timeouts, network outages, and client release notes.
5. If exposed rate or ad load: check app version, placement changes, frequency caps, and player-mix shift
   (new-user share changes ad exposure because entry-point exposure is front-loaded).
6. If DAU: this is a retention/UA problem, not a monetization problem — hand off to the relevant playbook.
7. Only then consider design changes, and validate them experimentally with the §5 guardrails attached.
