# Verified current-round witness

Recorded: 2026-10-31T11:13:57.437958+00:00.

The component receipt `bot_research/runs/validation/defense-step-budget-002.json`
checks the exact position and opponent actions stated in PROOF.md. Budgets 30
and 60 both return the same 22-turret construction, costing 3010 gold. Every
action is accepted, and original combat computes zero incoming damage. The
counter keeps all 790 HP through that round. The saved receipt includes the
complete action list and all input hashes. It discharges the conditional
existence statement for this position, not for other positions or later rounds.

The 15-step control reproduces the recorded construction exactly and incurs
1120 damage. The measured search times are about 6.08 seconds for 15 steps and
7.21 seconds for 30 steps in this component run. This demonstrates a search
limit failure despite sufficient gold; it does not prove a best global limit.
