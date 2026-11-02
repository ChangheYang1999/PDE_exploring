# A common public prefix with opposite continuation preferences

Written 2026-10-31T16:37:44.084428+00:00, before implementation and the declared matches.

## Statement and hypotheses

Use the current balanced configuration, unchanged original engine, and standard initial state. Give the target policy the public name anonymous_target and the selector the public name anonymous_selector, regardless of their implementations. The two target policies both execute the same P5TNUBM policy with r1_poke=0 through round3. Target B continues that policy thereafter. Target F instead spends on tier1 purchases from round4, using the existing MazeGrower with growth_rounds=3, tier=tier1 and no bait. The target's branch parameter is not supplied to the opposing policy. Neither target examines pending actions or other hidden state.

The tested selector shares the existing early E and growth G branches and their common first-three-round actions. It commits to one branch at round4. We will compare adaptive, forced E and forced G against both B and F, in both physical assignments, for12 games. The falsifiable empirical hypothesis is that E wins and G loses against B, while E loses and G wins against F. Exact outcomes, legal actions and public-prefix equality must be checked; until then the hypothesis is OPEN.

## Common-prefix argument

Fix a physical assignment. Initially the original-engine states and both public names agree across the two target branches. Through round3, the targets run identical policy code with identical parameters and observations; their internal states therefore agree and their submitted actions agree. The two selector branches submit identical actions in these rounds, as asserted by the existing selector and independently regenerated in the checker. The unchanged engine is deterministic on these actions, so induction through the three round transitions gives identical complete public observations at the start of rounds1,2,3 and4. This includes names, action histories if present, map cells, roster indices, HP, gold, factory counts, round number and rules. Comparison must use the entire original observation object, not a small feature summary or name-normalized digest. The different target continuation code is not public information.

Consequently any deterministic round-four selector whose input consists only of this public history and its own identically initialized, legitimately updated state chooses the same E/G branch in the two games. If the empirical outcome matrix above is confirmed, such a selector cannot win both games. This conclusion is about a one-time choice of these two continuations after this common prefix. It does not exclude a third continuation, delaying the choice, later adaptive switching, or another opening.

## Randomized restricted game

Conditional on the confirmed matrix, assign utilities +1 for a win and -1 for a loss. Let q be the probability of choosing E, with randomness independent of the hidden target branch and the same distribution in both games. Expected utility against B is 2q-1, and against F is 1-2q. Their minimum is at most0 because their sum is0. At q=1/2 both are0. Thus the two-by-two restricted game has maximin value0; each deterministic choice has worst-case utility -1. This is exact rational algebra on the verified finite matrix, not a claim about the value of the full game or population win rates.

## Verification and dependencies

A new anonymous-name experiment wrapper uses the existing unmodified isolated_match and evaluator. Only public display names differ from the usual development wrapper. All12 games require strict accounting, original-engine replay, frozen source/data closure, fresh regeneration of both policies on every observation, input immutability and action legality. The checker compares the full public observation histories across all three selector modes and both target branches at each physical assignment. Original names remain in the compared observations. It also verifies that the adaptive complete history equals its selected forced branch.

Dependencies: route_projection_selector and its E/G closures; lead v30 with the exact fixed parameters above; MazeGrower and pinned JSON; original engine/configuration; the declared anonymous-name wrapper and checker. The growth planner's existing three-second cutoff remains: observed regeneration must agree, and no load-independent determinism claim is made. This is adversarial development evidence. Final best_v9e and its already-completed pool-C validation are unchanged.
