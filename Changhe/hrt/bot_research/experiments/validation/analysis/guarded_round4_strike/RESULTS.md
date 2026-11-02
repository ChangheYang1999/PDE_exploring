# One cheap gun makes the early strike win against both nominees

Checked 2026-10-31T15:35:26.177450+00:00.

CONFIRMED: the 30-gold round-four corner gun converts the fixed early-heavy policy from a loss into a 755:740 win against both P4TNUB and P5TNUBM, for both tested public-budget fractions and both assignments.

Each row represents both physical assignments. Outcome and HP are from the target perspective.

| Target | Counter | Target outcome | HP target:counter | Final round |
|---|---|---|---|---:|
| P4TNUB | earlygun0_budget1of2 | W | 740:-107 | 12 |
| P4TNUB | earlygun0_budget1of1 | W | 740:-107 | 12 |
| P4TNUB | earlygun1_budget1of2 | L | 740:755 | 50 |
| P4TNUB | earlygun1_budget1of1 | L | 740:755 | 50 |
| P5TNUBM | earlygun0_budget1of2 | W | 740:-107 | 12 |
| P5TNUBM | earlygun0_budget1of1 | W | 740:-107 | 12 |
| P5TNUBM | earlygun1_budget1of2 | L | 740:755 | 50 |
| P5TNUBM | earlygun1_budget1of1 | L | 740:755 | 50 |

The common opening reaches round 4 with 291 gold. The tier4 costs 260. A 60-gold splash cannot accompany it, but gun1 at (10,1) costs 30 and stops the three incoming tier1 copies on the unchanged empty route. The counter retains 755 HP while its tier4 reduces either nominee to 740. At round 5 the public-HP trigger sees that lead and switches to the budget defender. Both a half-budget and a full-budget forecast preserve the lead through round 50. No target policy clone or opponent-name lookup is used.

This is a complete-policy intervention. Prepending the gun also filters now-unaffordable later proposals and changes future income; the result is not attributed to a hypothetical gun with no opportunity cost. All eight disabled-gun controls match the earlier unguarded complete histories exactly, including their round-12 loss. Prefix and full-game checks use the original engine. The analytical gun claim is separately stated with its exact empty-route and three-tier1 hypotheses in PROOF.md.

The two nominees have identical gameplay through round 4 under equal labels. This counter therefore does not need to distinguish them before their policies diverge. The result illustrates why an identical-observation theorem alone cannot establish that one common strategy must lose against one of the targets.

All 16 games pass strict accounting, original-engine replay and source/data archive checks. All eight assignment pairs match exactly. Fresh instances reproduce all 496 decisions with unchanged observations and independently verified first-switch rounds. There are 184 locally rejected parent proposals, all omitted before submission; there are no invalid submitted actions or bot errors. These are disclosed development conditions, not independent statistical samples. Pool C remains unused.

The exact two winning specs and full source closure are in guarded-round4-001.json. Reproduce it with run_data_development, then audit_development_strict, replay_audit, summarize_plain_campaign, audit_data_archives and check_guarded_round4_histories. The prefix and disabled-control checks are check_guarded_round4_opening and compare_recorded_controls. Use the project root, .venv/bin/python -B, bytecode disabled, bot_research/tmp, one thread, low priority and assigned affinity.

Audit inputs:

- `bot_research/runs/validation/guarded-round4-001-strict.json`.
- `bot_research/runs/validation/guarded-round4-001-replay.json`.
- `bot_research/runs/validation/guarded-round4-001-summary.json`.
- `bot_research/runs/validation/guarded-round4-001-data.json`.
- `bot_research/runs/validation/guarded-round4-001-histories.json`.
- `bot_research/runs/validation/guarded-round4-001-opening.json`.
- `bot_research/runs/validation/guarded-round4-controls-001.json`.
- `bot_research/experiments/validation/guarded-round4-control-pairs-001.json`.
- `bot_research/experiments/validation/guarded-round4-001.json`.
- `bot_research/experiments/validation/analysis/triggered_budget_timing/verification/full_games.json`.
