---
name: modern-statistician
description: Analyse data the way a careful modern statistician would, with a clear estimand, a model that matches how the data arose, honest uncertainty, and reproducible code. Use this skill whenever a task involves analysing or interpreting data, comparing groups, A/B tests or experiments, regression or any other statistical model, significance, p-values, confidence or credible intervals, sample size or power, forecasting or predictive modelling, causal questions ("did X cause Y", "what is the effect of"), or reviewing someone else's analysis, even if the user never says "statistics".
---

# Modern Statistician

The aim is an analysis whose conclusions would survive a sceptical review: the question is precise, the method fits how the data were generated, the uncertainty is stated honestly, and someone else can rerun it.

Most bad analyses fail before any model is fitted: the question was vague, the data were not what they seemed, or many analyses were tried and one was reported. So spend effort early, and scale the rigour to the stakes. A quick exploratory look does not need the full workflow, but say that it is exploratory.

## Workflow

### 1. Pin down the question
Decide which of three kinds of question this is, because each needs different methods and supports different claims:

- **Description:** what does the data look like? (summaries, rates, trends)
- **Prediction:** what will happen for new cases? (judged by out-of-sample accuracy)
- **Causation:** what would happen if we intervened? (needs a design or explicit assumptions)

Then write down the estimand in one sentence: which quantity, in which population, over which time frame, compared with what. If the request is too vague to do this, ask or state the interpretation you chose.

### 2. Understand how the data came to be
Before computing anything, establish:

- The unit of observation, and whether rows are independent (repeated measures, clusters, time series and spatial data are not).
- How units were selected, and who is missing as a result (survivorship, opt-in, filtering upstream).
- How each variable was measured, and whether definitions changed over time.
- Whether treatment or exposure was randomised. If not, why some units got it.

### 3. Look before modelling
Plot the raw data: distributions, relationships, values over time, and missingness patterns. Check ranges, duplicates, impossible values and unit mismatches. Many "findings" are data errors, and a plot finds them faster than a model does.

### 4. Choose a model that matches the data
Pick the model from the structure of the outcome and the design, not from habit. See the method guide below. Prefer a simple model you can defend over a complex one you cannot check. If you have decisions to make (covariates, exclusions, transformations), make them before looking at the outcome results where possible, and record them.

### 5. Check the model
A fitted model is a claim that can be wrong. Check it:

- Simulate data from the fitted model and compare with the observed data (posterior or parametric predictive checks).
- Inspect residuals for structure the model missed.
- For Bayesian fits, verify convergence (R-hat, effective sample size, divergences) and run prior predictive checks.
- For anything non-trivial, fit the model to fake data with known parameters first, to confirm it can recover them.

### 6. Quantify uncertainty
Report an interval with every estimate. Make sure the interval reflects the real structure of the data: clustered or robust standard errors, multilevel models, or a bootstrap that resamples whole clusters. An interval that ignores dependence is too narrow and gives false confidence.

### 7. Stress-test
Ask what would change the conclusion, then try it: a different reasonable specification, excluding influential observations, a different handling of missing data, a negative control or placebo outcome. Report whether the result held, including when it did not.

### 8. Report
Use the reporting structure below. Translate results to the scale the reader cares about (percentage points, euros, days) instead of raw coefficients.

## Principles

**Estimate, don't just test.** Lead with the effect size and its interval. A p-value says little about how big or important an effect is, and "significant" versus "not significant" is not a meaningful boundary: p = 0.04 and p = 0.06 are nearly the same evidence. Never read a non-significant result as "no effect"; look at whether the interval rules out effects that matter.

**Respect the garden of forking paths.** When many outcomes, subgroups, models or exclusions are tried, some will look convincing by chance. Say how many analyses were run, separate pre-planned from exploratory results, and adjust for multiplicity or use partial pooling when making many comparisons.

**Use the structure in the data.** Grouped, repeated or nested data call for multilevel models. Partial pooling gives better estimates for small groups than either analysing each group alone or ignoring groups entirely.

**Simulate when in doubt.** Simulation answers questions that formulas answer badly: power and sample size for realistic designs, whether a method behaves well on data like yours, and what the model implies. Seed every simulation.

**Causal claims need a causal argument.** Without randomisation, state the assumptions, ideally as a diagram (DAG). Adjust for confounders. Do not adjust for mediators or colliders, or for anything affected by the treatment, since that introduces bias instead of removing it. Do not interpret the coefficients of adjustment variables as effects. Add a sensitivity analysis for unmeasured confounding. If the assumptions are not credible, describe the result as an association.

**Prediction needs honest validation.** Split or cross-validate in a way that mirrors deployment (by time for forecasting, by group when predicting for new groups). Keep all preprocessing inside the validation loop to prevent leakage. Always compare against a simple baseline. For probabilities, check calibration and use proper scoring rules (log loss, Brier), not accuracy alone.

**Treat missing data as a modelling problem.** Report how much is missing and for whom. Dropping incomplete rows is only safe when missingness is unrelated to the outcome; otherwise use multiple imputation or model the missingness, and never impute with a single mean.

**Make it reproducible.** The whole analysis runs from a script from raw data to results, with fixed seeds, recorded package versions, and no manual steps. Keep raw data immutable.

## Habits to avoid

| Habit | Why it misleads | Do this instead |
|---|---|---|
| Dichotomising continuous variables | Throws away information and invents thresholds | Keep them continuous; use splines for non-linearity |
| Stepwise or p-value-based variable selection | Biased estimates, intervals too narrow | Choose variables from subject knowledge, or use regularisation |
| Testing normality to pick a test | The pre-test has poor power and distorts the result | Choose the model from the outcome type; use robust or resampling methods |
| Deleting outliers because they are inconvenient | Changes the population being studied | Investigate them; use robust models; report with and without |
| Post-hoc ("observed") power | Just a restatement of the p-value | Report the interval; plan power before the study |
| Reporting only the model that "worked" | Hides the search that produced it | Report the specifications tried |
| Bar charts of means with no spread | Hides the data | Show the points or the distribution, with intervals |
| Trusting a subgroup effect alone | Subgroups are noisy and numerous | Test the interaction; shrink with a multilevel model |

## Method guide

Defaults, not rules. Deviate when the design calls for it and say why.

| Situation | Reasonable default |
|---|---|
| Two groups, continuous outcome | Difference in means with interval (Welch or bootstrap); regression with baseline covariates if available |
| A/B test on a rate | Difference in proportions with interval; pre-registered metric and stopping rule; sequential methods if peeking |
| Binary outcome | Logistic regression; report risk differences or average marginal effects, not only odds ratios |
| Counts | Poisson or negative binomial with an offset for exposure |
| Skewed positive outcome (costs, durations) | Gamma or log-normal GLM; avoid log-transforming then interpreting as means |
| Time to event, with censoring | Kaplan-Meier, Cox or parametric survival models; never drop censored cases |
| Repeated measures or clusters | Multilevel (mixed) model, or cluster-robust standard errors |
| Many groups to compare | Multilevel model with partial pooling |
| Time series | Check autocorrelation and seasonality; validate on a rolling origin; compare with a naive forecast |
| Observational causal question | DAG first; then regression adjustment, matching or weighting, difference-in-differences, regression discontinuity or instruments as the design allows |
| Small samples or awkward statistics | Bootstrap, permutation tests, or a Bayesian model with considered priors |

## Reporting structure

Use this structure for a full analysis; shorten it for a quick answer but keep the first three items.

1. **Answer:** the estimate on a meaningful scale, with its interval, in one or two sentences.
2. **Confidence and caveats:** how far the result can be trusted and the main threat to it.
3. **Data:** source, unit, sample size, exclusions, missingness.
4. **Method:** the model and why it fits the design, in plain language.
5. **Checks:** diagnostics and sensitivity analyses, and what they showed.
6. **What this does not show:** limits on generalisation and causal interpretation.

Match the language to the evidence: "is associated with" for observational results, "caused" only with a design that supports it. Round to the precision the data justify.

## Tooling

Use the language and libraries the repository already uses. Where there is a free choice:

- **R:** tidyverse for data work; lme4 or brms for multilevel models; marginaleffects or emmeans for interpretable effects; mice for imputation; survival; fixest for panel and causal designs; tidymodels and rsample for validation.
- **Python:** pandas or polars; statsmodels and scipy; PyMC or Bambi with ArviZ for Bayesian models; scikit-learn for prediction and validation; lifelines for survival; pyfixest or linearmodels for panel designs.

Write analysis code as functions or a pipeline, not one-off cells, so the checks and sensitivity analyses can rerun it with different choices.

## Reviewing someone else's analysis

Work through the same questions in order, and stop at the first serious problem, since later steps cannot fix an earlier one:

1. Is the question clear, and does the analysis answer that question?
2. Could selection, measurement or missingness explain the result?
3. Does the model match the data structure (dependence, outcome type)?
4. Is the uncertainty honest, and were multiple analyses accounted for?
5. Do the conclusions go beyond the evidence (causal language, generalisation, "no effect")?

Give feedback as specific, fixable points ranked by how much they threaten the conclusion.
