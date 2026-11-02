# Forecast dependence of an early heavy strike

## Exact statement and hypotheses

Use the unmodified balanced engine, standard start, and P5TNUBM with the exact parameter dictionary in early-heavy-knowledge-001.json. Compare EarlyHeavyHandoff with one tier4 attempted in round 5 and a switch to defense in round 6 or 7. Hold every other parameter fixed. The reference uses the exact public P5TNUBM model and forecast=true. The first intervention uses forecast=false with the same model; the second uses forecast=true with the earlier P5TNUB model and its parameter dictionary. Both assignments are evaluated.

This comparison is well defined from public observations and private legitimate state; all returned actions are legal. Exact prediction is claimed only for the reference model on its proved standard branch. It is an open empirical question whether either intervention retains the reference counter's win. No optimality or population-level claim is made.

## Argument

The constructor parameters fix the policy before play. In forecast=false mode the defense planner receives only the currently visible active roster; the model is still advanced on the public history, but its predicted additions do not enter that defense threat list. In the mismatched-model mode the threat list is formed from a private instance of the specified earlier public policy. That instance has no access to any live opponent state beyond the supplied public observation. Changing either input is therefore a permitted policy intervention. It may change all later states, so a resulting outcome difference is a full-policy effect, not the isolated value of a single prediction.

For legality, reconstruct the player's own observed state and apply the original action validator to every proposed purchase or building in sequence. Only accepted actions are returned. The argument in ../early_heavy_handoff/PROOF.md applies unchanged, because neither the forecast flag nor the chosen public model changes the final action-filter step. Opponent action interleaving cannot affect that induction, since it does not change the player's gold, buildings or roster during action validation.

The exact-model synchronization proof is ../retargeted_forecast/PROOF.md. It does not apply to the earlier model, and all disagreements there must be reported. Complete original-engine replays check outcomes separately from fresh counter-policy reproduction. A model disagreement is not itself an illegal action or a counter-policy reproduction failure.

## Dependencies and scope

Dependencies are the unchanged actions, combat and engine modules, ForecastHandoff, EarlyHeavyHandoff, the specified public target/model source closures, and the two linked informal proofs. Source and data hashes are frozen in the declaration. The comparison uses disclosed development conditions and does not use reserved pool C. These arguments establish validity of the experiment, not which policy wins.
