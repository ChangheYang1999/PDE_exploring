# Round-four selection by a public one-round projection

## Exact policy and hypotheses

The two branches are the fixed screened growth-6, handoff-10 counter and the guarded round-four tier4 counter with the frozen-v7 joint wall/turret defensive continuation. On a standard empty-board start, both branches make the same decisions in rounds 1 through 3. The selector calls both branches on separate copies of each of those observations, checks equality of their actions, and returns the common action list.

At round 4, it obtains the early branch's proposed actions and legally applies them to a private reconstruction of its public state. Keeping the opponent's observed buildings and roster unchanged, it uses the original combat simulator in both directions. Let d_in be the damage to the reconstructed own map from the visible enemy roster, and d_out the damage to the observed enemy map from the reconstructed own roster. Define projected lead L = own HP - d_in - (enemy HP - d_out). Select the early branch only if its accepted proposal contains the prescribed corner gun and tier4 purchase, its projected own HP is positive, and L is strictly positive. Otherwise select the growth branch. Commit to that choice for the rest of the game. The forced-branch variants use exactly the same branch objects and common prefix. A first call after round 4 defaults to the growth branch; no continuation-strength claim is made.

## Public-input and prefix argument

The branch wrappers differ only in actions at or after round 4 and their later defensive handoff. With the fixed empty layout, growth period and no bait, both use the same screened opening in rounds 1 through 3. Their retained state has received the same observation history. The equality check enforces this invariant in the implementation. No branch action list is applied to the live engine by the selector; construction and combat checks use newly reconstructed private states. Both damage computations therefore depend only on the observation, proposed own actions and current bundled rules. No current enemy action, opponent code, name or future state is read.

The simulator's prediction is exact under the explicit hypothesis that the enemy submits no actions this round and the early actions are applied as proposed. It is not a forecast guarantee against the actual opponent, which can make simultaneous hidden purchases or construction. The positive projected lead is a heuristic selection rule. Its strength is an empirical question.

## Evaluation and scope

Before any new full games, check both branches and the projection on the already disclosed twenty-target development set and four P5TNUBM opening-purchase variants. Preserve forced-branch controls and compare exact complete histories where the selected branch is already recorded. Neither the target set nor its outcome is held out. Fresh games, original-engine replay, source and data pinning, and fresh policy regeneration must be reported separately from this component argument. Pool C is excluded.
