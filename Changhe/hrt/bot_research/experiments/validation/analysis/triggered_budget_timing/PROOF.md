# Timing a public-budget handoff strike

## Exact statement and hypotheses

Fix the unchanged balanced engine, standard initial state, the exact P4TNUB and P5TNUBM specifications, and the already implemented TriggeredBudgetHandoff policy. Keep the screened opening, one tier4 strike, margin zero, and all search bounds fixed. Vary only the strike round R, earliest handoff L, and forecast budget fraction f. The new settings are (R,L)=(4,5),(4,6),(6,7),(7,8), each with f=1/2 or f=1, and both physical assignments against each target. This gives 32 new conditions. Previously measured round-five settings are references, not additional games or fresh validation.

The empirical hypothesis is that an earlier or later heavy strike can beat both nominees under one fixed specification. It is OPEN before the complete games and audits. In particular, the round-four move can arrive before the nominees' round-five insurance divergence, but sacrifices opening investment and possibly the first splash guard. An earlier hit alone gives no winning guarantee.

## Public-input and legality argument

These settings change only constructor parameters of the policy proved in ../triggered_budget_handoff/PROOF.md. They satisfy 1<=R<L<=50 and the nonnegative-margin requirement. Before the first public observation at or after L with own HP greater than enemy HP, the controller uses its screened opening and attempts one tier4 at R. Thereafter it uses the budget defender and buys no new minions. The action-subsequence argument in ../budget_handoff/PROOF.md applies unchanged: each proposed action is checked against the same updated owner-local state that the original engine will use. Rejected local proposals are omitted, not submitted.

The tier4 costs 260 and a splash costs 60 in the authoritative balanced configuration. On any round-four observation with own gold exactly 291, buying the tier4 leaves 31. Thus the same action list cannot also buy a splash, regardless of ordering, because 260+60>291. This is a conditional cash statement, not an assertion about every reachable opening. The component checker must record the actual starting gold, accepted strike and guard actions. The original engine supplies any HP consequences.

The timing comparison changes whole subsequent trajectories. If it succeeds, it does not establish that an isolated round-four attack has positive value against arbitrary defense. If it fails, it does not rule out other counts, growth schedules, guard placements or adaptive rules. All results are development evidence. No reserved scenario or pool C condition is used.

## Dependencies and verification

Dependencies are the original configuration, actions, engine, state and combat; TriggeredBudgetHandoff and its unchanged imports; the exact JSON guard layouts; and both pinned target sources and their imported planners. First verify all declared prefixes through round eight, using fresh policies and original-engine transitions, checking the public trigger independently and every submitted action. Then run all complete games, audit every declared completion and source/data archive, replay each trajectory, and regenerate the counter decisions from recorded observations. Report losses, failed attempts and any policy disagreement explicitly.
