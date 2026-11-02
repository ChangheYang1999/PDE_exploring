# Completing the screened-roster counter with a five-wall guard

## Statement, hypotheses and notation

Use frozen best_v9e, the unchanged balanced Engine, standard starts and both player assignments. For c in {original, fortress38, economy20}, let Q(c) be the screened-order policy of screened_roster_continuation: C02 through round5, buy (tier2,tier2,tier3) in round6, then continuation c. Let G(c) submit the same actions except that in round6 it also buys the five walls selected by the preceding declared geometric component experiment: (0,4),(1,4),(2,4),(3,3),(3,2). Their order and provenance are retained in exact JSON. The total round6 purchase cost is185, below the190gold available on this common prefix.

The five-wall selection is informed by the component result, before any G(c) full-game calls. It is a minimum only among the five declared packages tested there. This is targeted development against the fixed selected candidate, not held-out evidence. Use the six retained Q(c) games as explicit controls; run six new G(c) games. No result is duplicated as a new sample.

H1: at least one G(c) wins against best_v9e in both assignments. H2: for each continuation and seat, G(c)'s final own-minus-enemy HP margin is at least that of Q(c). Both are OPEN before new calls. Engine winner determines W/D/L. Retain every failed, invalid or differing attempt and label incomplete evidence as OPEN.

## Shared prefix and one-round guard

The implementations coincide through round5 and use the same target model and initial state. Under deterministic decisions, induction over the engine transition gives the same public histories through that round. The target cannot observe round6 pending walls, so its round6 action is also unchanged. These finite equalities are checked against the retained controls and original component witness, with fresh full-policy calls rather than scripted target actions.

The exact component witness establishes that adding the five legal walls to this state changes the counter's incoming damage from26 to0 while retaining26damage to the target. The route exposure is190 nominal splash damage per copy. This is evidence for the reached fixed-action state only. After round6 the extra walls, gold, HP and path income change observations and may alter both policies. Hence H1 and H2 require full games; neither follows from the local guard proposition.

## Verification and scope

Freeze the guard JSON, Python sources, control results and replays, and all runner/checker dependencies before execution. Each new game uses a fresh process. Run strict accounting, complete original-engine replay, source/archive checks and fresh instances of both factory policies on every recorded observation. Compare common prefixes, actual round6 target actions, guard purchases and HP changes with every matched control. The original Fortress38 wall-clock cutoff remains a reproducibility limitation beyond these checked executions. Six paired conditions comprise three new and three reused behavioral matchups; they are not independent population samples. No candidate selection or modification of installed best.py follows from these tests. Pool D stays separate.

Dependencies: analysis/screened_roster_continuation/{PROOF.md,RESULTS.md}; analysis/screened_roster_wall_guard/{PROOF.md,RESULTS.md}; exact declared source and data hashes; the unchanged engine. No proof-assistant result or unrestricted strategic guarantee is claimed.
