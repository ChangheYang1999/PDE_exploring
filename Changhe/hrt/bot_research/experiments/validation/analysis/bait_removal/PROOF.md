# Removing the round-two bait from fixed schedules

## Exact empirical question

Keep both fixed A/B schedules from bots/defense/counter_astra41.py, except remove their three round-two tier1 purchases. Keep the two round-two factories and every other requested action in its original round and order. Do not spend the saved gold. Compare these two interventions against the original A/B controls on the six defenders used in bait_guard_transfer: frozen Fortress41, best_v9e, V33C, P5TNUBM, and the adaptive and forced-early Fortress38 delegated policies. Use both assignments: 24 new full games and 24 existing audited controls.

H1: removing the bait changes at least one previously losing defender condition to a draw or win. H2: at least one defender that previously lost all four A/B conditions avoids all four losses after bait removal. Report every W/D/L transition, HP difference and ending round even if both claims fail. The former is a finite existence claim, the latter a per-defender conjunction. They are decided by the complete paired table, not the average margin.

## Interpretation and causal scope

The sole intervention in the attacker's requested schedule is deletion of those three purchases. The resulting difference includes their damage, hit bounties, roster lifetime, defender responses to them, and all later consequences. It does not isolate the psychological idea of bait from direct damage. In particular, a changed result alone cannot prove that speculative defensive spending is the mechanism. Retain per-round defender purchases, factory counts, gold and incoming damage so that proposed explanations can be checked.

Affordability may depend on hit income. If a retained action becomes illegal after removing bait, preserve that failure and do not silently filter or replace it. Such a condition does not establish a legal whole-policy outcome for the requested intervention. The audit claim remains open until the complete accounting states the limitation.

## Verification and dependencies

Before complete games, check that the two intervention policies return exactly the original list in every round except round two, where only the three specified tier1 actions disappear. The check does not call defender policies. Full games use the original balanced Engine, complete source and JSON registration, all-result accounting, independent original-engine replay and fresh reconstruction of both actual policies from their public histories. Existing controls are reused only after their published receipt and source archive are verified. Canonical repeated assignment histories are reproducibility checks, not independent random samples.

This is development ablation, not reserved validation or a change to best.py. Dependencies are the unchanged A/B source, six frozen defender specifications, the original engine, and bait_guard_transfer/PROOF.md plus its complete 24-game receipt. All output is relative to the project and no protected file is modified.
