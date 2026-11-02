# An early heavy strike before defensive handoff

## Statement and hypotheses

Use the bundled balanced engine and standard initial state. The controller follows ForecastHandoff except at a fixed strike round before handoff, where it first attempts a bounded number of copies of a specified heavy tier, then filters the parent's proposals through the original action validator on a reconstruction of its own public state. Both its parent and its target model are private fresh instances driven once per reached observation from round 1.

Every submitted action is legal in sequence. The controller reads no opponent pending action. When its target model is the exact P5TNUBM source and parameterization, its predictions are exact on the standard start, under the terminating standard-transition hypotheses of ../retargeted_forecast/PROOF.md. None of these claims implies a win.

The empirical hypothesis is that one tier4 bought in round 5, followed by defensive handoff in round 6, 7, 8, or 9, beats P5TNUBM. Controls omit the early purchase. All other parameters are fixed and both physical assignments are tested. This is a development comparison, not reserved validation.

## Notation and argument

Let s be the player's observed pre-submission state and A the parent's proposed actions. Construct s' as a deep independent reconstruction. Attempt the strike purchases first, applying the original validator to s'; append only accepted actions. Next attempt every action in A in its original order, again appending only accepted actions. Induction on these attempted actions shows that applying the returned list to s produces the same state as the accepted transitions on s'. The engine's interleaving with the other player cannot change this legality because construction and purchase validation depend only on the owner's state. Every returned action is therefore legal.

The parent is evaluated once on the actual public observation, before filtering. Its target clone is thereby advanced once on each actual public history. Filtering the counter's own proposed list does not change this observed-history synchronization. The exact-model argument for P5TNUBM still applies. The strike decision uses only constructor parameters, the observed round, whether the parent has switched, and the player's legal action budget; hence it reveals or accesses no hidden current submission.

For the proposed opening mechanism, if the target's post-construction round-5 map contains only splashes with total route exposure S<560, a single active tier4 that has time to traverse that route arrives and deals 60. It starts at dense index 0 and tick 0. On a simple 12x12 route its length is at most 143, below the 250-tick horizon. If the counter has HP755, the target has HP800, and no counter damage occurs in that round, the resulting HPs are755 and740, respectively. The unchanged-engine component check must verify the map and HP hypotheses rather than assume them. A later defense may still fail, so the resulting 15-point lead is not a full-game guarantee.

## Dependencies and scope

The core arguments depend on the original actions.py, combat.py and engine.py; the single-copy criterion is a special case of ../splash_threshold/PROOF.md. Exact target predictions use ../retargeted_forecast/PROOF.md. Actual data and source hashes are recorded with the component and campaign receipts. Excess parent proposals rejected by the local filter are reported separately from rejected engine submissions. This is an informal argument, with original-engine tests as supplementary evidence.
