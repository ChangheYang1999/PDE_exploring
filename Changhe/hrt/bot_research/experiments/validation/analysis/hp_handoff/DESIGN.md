# Declared development design

Ten target policies face six handoff variants in both seats, 120 conditions.
Targets: v28 P5TNUB, v27 always-current and fail-limit3, F34, F35, E25RM,
best_v9e, budget_timing tier3 round3 with half-gold defense envelope, rush_t1,
and eco5_t3. Parameters are in hp-handoff-001.json.

The six opponents are fixed handoff8,9,10; lead-from8 with deadline12;
panic-HP600 with deadline12; and both triggers with deadline12. Lead means
strictly more HP than the target, observed at the start of a round. A switch
uses the defender immediately in that round. The old H10 records provide
matched controls for the six unchanged strong targets. P5TNUB and the three
simple policies have no such old H10 controls in that campaign.

The primary questions are whether an early lead trigger preserves H10's
wins against strong targets and whether the panic trigger repairs rush
losses. No aggregate is treated as a population win-rate estimate. A
fixed deadline can dominate these choices on this finite pool without
being universally stronger. Half the conditions run on each of two cores;
assignment equality is checked from the resulting complete histories.
