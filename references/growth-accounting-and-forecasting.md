# Growth accounting and forecasting

Read this for DAU decomposition, retention-curve fitting, LTV extrapolation, payback, capacity/KPI feasibility,
and any "how many users do we need" or "will we hit the target" question.

## 1. DAU identity

```text
DAU_t = retained_t + resurrected_t + new_t
```

where the three populations are **mutually exclusive** on day t:

- `new_t` — first qualifying activity on day t (per the product's identity unit);
- `retained_t` — active on day t and active within the retention lookback window before t;
- `resurrected_t` — active on day t after meeting the product's inactivity threshold.

Also track `churned_t` (active previously, now past the inactivity threshold) for the net-change view:

```text
DAU_t − DAU_{t−1} = new_t + resurrected_t − churned_t (+ definitional residual)
```

Report the residual explicitly. A residual that is not near zero means the population definitions overlap or the
lookback windows are inconsistent — fix that before interpreting anything.

Quick ratio (`(new + resurrected) / churned`) is a useful single summary but hides mix: a title can hold DAU flat
by buying new users while its retained base erodes. Always show the composition trend, not only the total.

## 2. Steady-state DAU

If daily new users are approximately constant at `N` and the retention curve `r(k)` is stable:

```text
steady-state DAU ≈ N × ( 1 + Σ_{k=1..K} r(k) )
```

`Σ r(k)` over the practical horizon K is the "retention area" — the number of active days an average acquired user
contributes. This is the single most useful planning constant a product has.

Consequences worth stating to stakeholders:

- **DAU target → required daily new users**: `N_required ≈ DAU_target / (1 + Σ r(k))`.
- **Budget feasibility**: `budget/day ≈ N_required × CPI`, then compare with the actual plan. This is often how an
  unrealistic DAU KPI is disproven before money is spent.
- Ramp time to steady state is roughly the horizon over which retention still contributes materially; a title with
  a long tail takes months to converge, so do not read early DAU as the equilibrium.

Assumptions to state every time: stable acquisition mix, stable retention curve, no major content/version shocks,
no resurrection surge, and a fixed identity unit. When any fails, the estimate is an upper or lower bound — say which.

## 3. Retention-curve fitting

Common functional forms, in order of increasing capability:

```text
power law    r(t) = a · t^(−b)                 log r = log a − b · log t   (linear regression in log-log)
exponential  r(t) = a · e^(−λt)                 log r = log a − λt
double exp   r(t) = p·e^(−λ1 t) + (1−p)·e^(−λ2 t)   heterogeneous cohorts (fast churners + loyal core)
sBG / BG-NBD                                    survival with individual heterogeneity; better long-tail behavior
```

Practical rules:

- Fit on **weighted cohort retention**, not on averaged daily percentages.
- Exclude day 0, and consider excluding D1, which is usually off-curve relative to the tail.
- Fit per cohort family (channel, geo, platform, version) — blended fits inherit mix, not behavior.
- Never fit and extrapolate on immature cohorts without marking censoring: a D30 estimate from 10-day-old cohorts
  is a model output, not a measurement.
- Power-law fits typically **overestimate** the long tail because the heavy-churn early segment dominates the fit;
  double-exponential or heterogeneity models usually behave better beyond the observed window.
- Always backtest: fit on cohorts old enough to have realized values, compare predicted vs actual at the target
  horizon, and report error by segment. Publish the error band with every forecast.
- Re-fit on a schedule and after any onboarding, difficulty, or acquisition-mix change. Treat the coefficients as
  perishable product facts with an owner and a refresh date.

## 4. LTV projection

Two equivalent construction paths — choose one and label it:

```text
A. daily build:   LTV_n = Σ_{t=0..n} r(t) × ARPDAU(t)
B. curve fit:     fit cumulative ARPU per cohort against t, then extrapolate to n
```

Requirements:

- State the contribution basis: gross bookings, post-fee net revenue, or contribution margin. Payback conclusions
  swing by the entire share chain otherwise.
- Separate IAP and ad components for hybrid products, since their curves have different shapes.
- `ARPDAU(t)` is not constant: monetization per active day usually rises with tenure as payers concentrate.
  A flat-ARPDAU projection systematically misstates long-horizon LTV; model the tenure profile or say you didn't.
- For predicted LTV, report: model date, training cohorts, horizon, features, censoring treatment, uncertainty,
  and backtest error. Label the number as predicted everywhere it appears, including dashboards.
- Early-horizon predictors (e.g. D0–D7 signals → D30/D180) must be re-validated whenever acquisition mix, price
  points, or onboarding change. A stale predictor is worse than no predictor because it is trusted.

## 5. Payback and cash

```text
cumulative ROAS_n = cumulative attributable net revenue per cohort / cohort acquisition cost
payback day       = min{ n : cumulative net contribution per acquired entity ≥ fully loaded CAC }
```

- Distinguish accounting payback (does it recover cost) from cash payback (when the cash actually arrives, after
  store settlement lag and channel terms).
- Discount long horizons when comparing investment options; a nominal 1.0× at D365 is not the same asset as 1.0× at D60.
- Use marginal, not average, returns for scaling decisions — see [ua-and-marketing-analytics.md](ua-and-marketing-analytics.md).

## 6. Forecasting practice

- Start with transparent baselines: seasonal naive, moving average, or the DAU identity driven by a planned
  acquisition schedule. A structural DAU model that a stakeholder can audit usually beats an opaque one they can't.
- Add known future events explicitly: releases, seasons, holidays, campaign flights, price changes, server merges.
- Use rolling-origin backtests. Report intervals, and report which horizon the interval is valid for.
- Separate the **plan** (what we intend, with levers) from the **forecast** (what we expect, given no new action).
  Conflating them produces targets that are neither.
- Recheck after every incident and every content shock; do not silently carry a broken model forward.

## 7. Common failure modes

| Symptom | Likely cause |
|---|---|
| DAU identity doesn't close | overlapping new/retained/resurrected definitions, or inconsistent lookback windows |
| Forecast good in-sample, bad live | fitted on blended mix; mix shifted |
| LTV keeps getting revised up | power-law tail extrapolation, or immature cohorts treated as realized |
| Payback looks great, cash is tight | gross-bookings basis, ignored share chain and settlement lag |
| Target "achieved" but revenue flat | DAU inflated by low-value or artificial accounts; check composition and value per active |
| Retention improved but DAU didn't | acquisition volume fell; decompose before celebrating |
