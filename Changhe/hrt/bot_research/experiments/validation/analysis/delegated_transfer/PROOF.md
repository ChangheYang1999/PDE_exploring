# Transfer of the two frozen defensive continuations

Written 2026-10-31T16:58:08.002093+00:00, before the transfer manifests and games.

## Exact empirical question

Test both already implemented continuations of DelegatedRouteSelector, econ20 and fortress38, on every one of the 45 target specifications in emergency-transfer-a001, b001 and c001. Use both physical assignments: 90 new games per continuation, 180 total. Compare each new game with its corresponding completed emergency-template game. The targets and these two continuations are fixed before seeing this transfer matrix. The focused six-target matrix is still finishing; neither continuation is omitted according to its result.

The success claim for a continuation is that it retains every old win or draw and repairs all six old losses. A weaker result must be described as such. Also report exact complete-history agreement, every W/D/L transition, final HP, ending round, rejected actions, errors and decision times. This is development transfer on disclosed opponents, not reserved validation or population inference.

## Policy argument and hypotheses

The implementation and the prefix argument are those of the preceding delegated_defense/PROOF.md. The only new operation here is evaluation. Each new policy uses the same first four calls as the old emergency selector. Both old and new runners display each original target ID and the common counter ID route_adaptive, so those names do not distinguish the paired policies. In each actual pairing, equality of the first four complete recorded rounds is checked directly after removing only the run identifier.

The growth branch is unchanged and the frozen delegate is unused there. Therefore, if every policy involved is deterministic on these histories, a selected growth branch has the same complete trajectory as its old control. Exact observed agreement is checked, rather than inferred from determinism. Search cutoffs in teammate code can make wall-clock timing relevant, so no arbitrary-load guarantee is claimed.

For the adaptive early branch the first defensive handoff is determined entirely by public observations. Before round five it cannot start. From round five it starts at the first positive own HP lead or positive original-combat damage from the visible current opposing roster, whichever first applies on the actual history. The earlier controller has no possible trigger before round five. Once started the handoff persists. This yields an independent reconstruction of every delegation trace without importing the controller or its trigger helper. It establishes information and activation properties only, not winning strength.

## Verification

Write ten manifests with nine targets apiece, five for each continuation. Each uses source-pinned unchanged code, the original engine and the standard start. Complete strict accounting, original-engine replay, data/source checks and fresh counter regeneration for each manifest. Then separately reconstruct all handoff decisions from original public states and original combat. Compare all 180 pairs against the 90 old controls. Keep every condition, failure, loss and draw, and distinguish aborted computation from an outcome. No change to installed best_v9e or its final pool C follows.
