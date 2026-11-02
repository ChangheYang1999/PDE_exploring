# Fixed counters transferred to the af2g candidate

Declared 2026-10-31T19:18:38.832516+00:00, before any af2g game in this lane.

## Statement and exact conditions

The new policy is `bot_research.experiments.lead.frozen.best_v9f:@make?passive_until=null`, frozen best_v9f with the passive rule disabled. The control is frozen best_v9e, SHA256 70ef8eab00ceca625b0f7459b8a12282d3391ce72cc2b812b6a8e6cf63a2fd87. Test standard starts under the unchanged balanced engine, both player assignments, against the exact D,G,H,I policies from the six-policy table and the earlier half-budget guarded round-four tier4 striker. Copy their full specifications into the manifest without tuning. Ten new games and ten prior best_v9e controls are used.

H1: af2g has no worse win/draw/loss outcome than best_v9e on any of the ten corresponding conditions. H2: at least one earlier best_v9e loss becomes a draw or win. Both remain OPEN until all audits complete. These hypotheses are independent: failure of H2 does not imply a regression. The engine winner, not the sign of an HP difference, defines the outcome.

The five opponents were selected after observing the old table. D,G,H and the guarded striker previously beat best_v9e; I is a negative control that best_v9e beat. This screen was designed after the lead proposed af2g and reported its GROWERS result. No statement of unseen validation or an unbiased average is intended. It does not replace the lead's much larger R13 conditionwise gate.

## Argument, dependencies and scope

The counter policies are unchanged, so their prior observation-only legality arguments remain applicable. The respective standalone proofs are delegated_defense, early_wall_guard, hp_handoff, hp_handoff_forecaster and guarded_round4_strike in this index. We do not infer any af2g outcome from the earlier results. Each new claim is a finite conjunction or disjunction over original-engine outcomes, checked only after every declared condition completes.

Require strict condition accounting, input hashes and archived source/data verification, original-engine replay, and fresh regeneration of both policies on every recorded public history. Check sequential action legality and observation immutability. Recheck the ten old records and their archives, and replay their actions on the current unchanged engine. Restored compressed replays must match their original trajectory SHA256. Report source drift, errors, rejections, timings, full HP, final rounds and normalized seat-pair agreement. Old records are reused, not new samples. A matching opponent swap is not independent evidence. Pool D remains unexecuted and this campaign does not read installed best.py.
