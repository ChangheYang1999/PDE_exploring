# Public HP switching produces complementary counters

Checked 2026-10-31T15:28:58.794987+00:00.

CONFIRMED: the no-strike HP-triggered budget defender beats P4TNUB and best_v9e, while its one-tier4 variant beats P5TNUBM. REFUTED: one of these four fixed counter settings beats all six targets, or adding the HP trigger repairs transfer of the previous one-strike fixed-handoff counter to any of the five transfer targets.

Each row represents both physical assignments. Outcome and HP are from the target's perspective. The handoff column gives the first observed switch to pure defense, or none if the trigger never fires.

| Target | Counter | Target outcome | HP target:counter | Final round | Handoff |
|---|---|---|---|---:|---:|
| P4TNUB | trigger_strike0_budget1of2 | L | 660:755 | 50 | 8 |
| P4TNUB | trigger_strike0_budget1of1 | L | 660:755 | 50 | 8 |
| P4TNUB | trigger_strike1_budget1of2 | W | 800:-337 | 13 | none |
| P4TNUB | trigger_strike1_budget1of1 | W | 800:-337 | 13 | none |
| P5TNUBM | trigger_strike0_budget1of2 | W | 800:-493 | 13 | none |
| P5TNUBM | trigger_strike0_budget1of1 | W | 800:-493 | 13 | none |
| P5TNUBM | trigger_strike1_budget1of2 | L | 740:755 | 50 | 6 |
| P5TNUBM | trigger_strike1_budget1of1 | L | 740:755 | 50 | 6 |
| F36 | trigger_strike0_budget1of2 | W | 520:-75 | 13 | 8 |
| F36 | trigger_strike0_budget1of1 | W | 520:-3155 | 36 | 8 |
| F36 | trigger_strike1_budget1of2 | W | 660:-153 | 12 | none |
| F36 | trigger_strike1_budget1of1 | W | 660:-153 | 12 | none |
| F37 | trigger_strike0_budget1of2 | W | 520:-101 | 13 | 9 |
| F37 | trigger_strike0_budget1of1 | W | 520:-521 | 35 | 9 |
| F37 | trigger_strike1_budget1of2 | W | 660:-153 | 12 | none |
| F37 | trigger_strike1_budget1of1 | W | 660:-153 | 12 | none |
| best_v9e | trigger_strike0_budget1of2 | L | 660:755 | 50 | 8 |
| best_v9e | trigger_strike0_budget1of1 | L | 660:755 | 50 | 8 |
| best_v9e | trigger_strike1_budget1of2 | W | 800:755 | 50 | none |
| best_v9e | trigger_strike1_budget1of1 | W | 800:755 | 50 | none |
| lead8 | trigger_strike0_budget1of2 | D | -40:-40 | 8 | none |
| lead8 | trigger_strike0_budget1of1 | D | -40:-40 | 8 | none |
| lead8 | trigger_strike1_budget1of2 | W | 560:520 | 50 | 6 |
| lead8 | trigger_strike1_budget1of1 | W | 560:380 | 50 | 6 |

All counters use the same screened opening and the same finite public-budget defense after switching. The eligibility round is 6, the HP margin is zero, and the forecast uses half or all public opponent gold. The strike flag changes only whether one tier4 is attempted in round 5. No counter receives a target identity or creates an opponent policy clone.

Without that extra strike, the counter reaches a 755:660 lead against P4TNUB and best_v9e and switches at round 8. Both budget fractions preserve that lead to round 50. Against P5TNUBM the same no-strike opening never leads and dies in round 13. Adding the tier4 reverses this comparison: P5TNUBM loses 740:755 after the counter switches in round 6, while P4TNUB and best_v9e win. These are complementary complete policies, not an identified universal adaptation rule.

Both fortress targets defeat every setting. In the no-strike games a lead exists at the switch, but the budget defender later leaks and loses. This is a concrete failure of treating an observed HP lead as a guarantee of future safety. Against lead8, both no-strike settings draw by simultaneous destruction in round 8; both HP totals are -40. The engine's declared result, not HP sign, determines the draw. The one-strike settings lose to lead8 despite switching while ahead in round 6.

Comparing only the one-strike variants to the previously published fixed-handoff transfer matrix, the HP trigger repairs no transfer loss. The new wins against P4TNUB and best_v9e also remove the round-five strike, so they do not isolate the effect of changing the handoff rule. A matched no-strike fixed-deadline control is needed for that causal comparison. The half- and full-budget settings agree in outcome throughout this matrix but sometimes differ greatly in final HP and survival time.

All 48 games pass strict accounting, complete original-engine replay and source/data archive checks. All 24 assignment pairs have identical normalized histories. Fresh instances reproduce all 1,426 counter decisions, with unchanged observations, legal submitted actions and independently verified first-switch rounds. There are 312 locally filtered parent factory proposals and no rejected submitted actions or bot errors. No minion is bought after an actual handoff. Prefix checks cover all 48 settings before the full-game runs. The original fortress planners retain their wall-clock limits; observed agreement is not a proof of load independence.

These are disclosed development conditions. Player swaps are controls, not independent samples. Pool C remains unused. Reproduce each triggered-budget manifest with `run_data_development` into a fresh directory, then run the strict, replay, data and `check_triggered_budget_histories` audits. Use the project root, `.venv/bin/python -B`, bytecode disabled, temporary files under `bot_research/tmp`, one thread, low priority and assigned CPU affinity.

Audit inputs:

- `bot_research/runs/validation/triggered-budget-a001-strict.json`.
- `bot_research/runs/validation/triggered-budget-a001-replay.json`.
- `bot_research/runs/validation/triggered-budget-a001-summary.json`.
- `bot_research/runs/validation/triggered-budget-a001-data.json`.
- `bot_research/runs/validation/triggered-budget-a001-histories.json`.
- `bot_research/experiments/validation/triggered-budget-a001.json`.
- `bot_research/runs/validation/triggered-budget-b001-strict.json`.
- `bot_research/runs/validation/triggered-budget-b001-replay.json`.
- `bot_research/runs/validation/triggered-budget-b001-summary.json`.
- `bot_research/runs/validation/triggered-budget-b001-data.json`.
- `bot_research/runs/validation/triggered-budget-b001-histories.json`.
- `bot_research/experiments/validation/triggered-budget-b001.json`.
- `bot_research/runs/validation/triggered-budget-c001-strict.json`.
- `bot_research/runs/validation/triggered-budget-c001-replay.json`.
- `bot_research/runs/validation/triggered-budget-c001-summary.json`.
- `bot_research/runs/validation/triggered-budget-c001-data.json`.
- `bot_research/runs/validation/triggered-budget-c001-histories.json`.
- `bot_research/experiments/validation/triggered-budget-c001.json`.
- `bot_research/runs/validation/triggered-budget-opening-001.json`.
