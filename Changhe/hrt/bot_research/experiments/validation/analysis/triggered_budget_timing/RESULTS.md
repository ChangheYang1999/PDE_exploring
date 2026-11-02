# Earlier and later triggered strikes

Checked 2026-10-31T15:33:54.446398+00:00.

REFUTED: one of these eight fixed timing and budget settings beats both nominees. CONFIRMED: the round-six and round-seven variants beat P4TNUB, but neither beats P5TNUBM.

Each row represents two matching physical assignments. Outcomes and HP are from the target perspective. The handoff is the first actual HP-triggered switch, which can be later than its eligibility round.

| Target | Counter | Target outcome | HP target:counter | Final round | Handoff |
|---|---|---|---|---:|---:|
| P4TNUB | strike4_lead5_budget1of2 | W | 740:-107 | 12 | none |
| P4TNUB | strike4_lead5_budget1of1 | W | 740:-107 | 12 | none |
| P4TNUB | strike4_lead6_budget1of2 | W | 740:-107 | 12 | none |
| P4TNUB | strike4_lead6_budget1of1 | W | 740:-107 | 12 | none |
| P4TNUB | strike6_lead7_budget1of2 | L | 520:755 | 50 | 9 |
| P4TNUB | strike6_lead7_budget1of1 | L | 520:755 | 50 | 9 |
| P4TNUB | strike7_lead8_budget1of2 | L | 660:755 | 50 | 8 |
| P4TNUB | strike7_lead8_budget1of1 | L | 660:755 | 50 | 8 |
| P5TNUBM | strike4_lead5_budget1of2 | W | 740:-107 | 12 | none |
| P5TNUBM | strike4_lead5_budget1of1 | W | 740:-107 | 12 | none |
| P5TNUBM | strike4_lead6_budget1of2 | W | 740:-107 | 12 | none |
| P5TNUBM | strike4_lead6_budget1of1 | W | 740:-107 | 12 | none |
| P5TNUBM | strike6_lead7_budget1of2 | W | 800:-155 | 12 | none |
| P5TNUBM | strike6_lead7_budget1of1 | W | 800:-155 | 12 | none |
| P5TNUBM | strike7_lead8_budget1of2 | W | 800:-493 | 13 | none |
| P5TNUBM | strike7_lead8_budget1of1 | W | 800:-493 | 13 | none |

Both nominees beat the unguarded round-four strike. It lands for 60 damage, but the counter fails to preserve its own HP lead and never switches to its defensive policy. At the reached 291-gold decision, a tier4 costs 260 and the intended splash guard costs 60, so both cannot be purchased. This is a specific cash constraint, not a proof that every round-four strike must fail.

The round-six strike against P4TNUB does not trigger handoff at its earliest eligible round 7; the lead appears at round 9. The round-seven strike triggers at round 8. Both preserve a win to round 50. Neither later strike wins against P5TNUBM. The half- and full-budget versions agree on each listed outcome and final HP, but are retained as separate declared policies.

All 32 games pass strict accounting, full original-engine replay and source/data archive checks. All 16 assignment pairs have identical normalized histories. Fresh controllers reproduce all 692 decisions with unchanged observations, independently verified public triggers and legal actions. There are 288 locally filtered parent proposals, no submitted invalid actions and no bot errors. The prefix checks were completed before each full campaign. These are development results, not independent samples from a policy population. No pool C condition was used.

Reproduction uses the two triggered-timing manifests with run_data_development, followed by audit_development_strict, replay_audit, summarize_plain_campaign, audit_data_archives and check_triggered_budget_histories. Run from the project root with .venv/bin/python -B, bytecode disabled, temporary files under bot_research/tmp, low priority, one thread and assigned affinity.

Audit inputs:

- `bot_research/runs/validation/triggered-timing-a001-strict.json`.
- `bot_research/runs/validation/triggered-timing-a001-replay.json`.
- `bot_research/runs/validation/triggered-timing-a001-summary.json`.
- `bot_research/runs/validation/triggered-timing-a001-data.json`.
- `bot_research/runs/validation/triggered-timing-a001-histories.json`.
- `bot_research/runs/validation/triggered-timing-a001-opening.json`.
- `bot_research/experiments/validation/triggered-timing-a001.json`.
- `bot_research/runs/validation/triggered-timing-b001-strict.json`.
- `bot_research/runs/validation/triggered-timing-b001-replay.json`.
- `bot_research/runs/validation/triggered-timing-b001-summary.json`.
- `bot_research/runs/validation/triggered-timing-b001-data.json`.
- `bot_research/runs/validation/triggered-timing-b001-histories.json`.
- `bot_research/runs/validation/triggered-timing-b001-opening.json`.
- `bot_research/experiments/validation/triggered-timing-b001.json`.
