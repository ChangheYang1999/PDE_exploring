# Public-label and player-index invariance on recorded histories

## Exact finite assertion

Fix the installed best_v9e source with SHA256 70ef8eab00ceca625b0f7459b8a12282d3391ce72cc2b812b6a8e6cf63a2fd87 and its declared dependencies. Fix all 72 retained histories in runs/validation/reserved-C-best-v9e-001. These consist of twelve opponent settings, the standard start and two prescribed continuations, in both player assignments. Pool C was already used for selection. No held-out claim attaches to this check.

For each history initialize two fresh default factory instances. At every round where the candidate was actually invoked, apply the following transformations to the original pre-round public observation and call the corresponding instance:

1. Replace both player names by the same neutral string `anonymous`.
2. Replace both names by `anonymous`, reverse the two player snapshots and replace the observer index p by 1-p.

The assertion to check is that both output action lists equal the candidate's recorded action list at every such round. Each instance must receive its entire transformed history in order. Prescribed prefix rounds are not calls and do not update either policy instance. The original engine must independently reproduce every retained round. Transformations must not alter rules, the observer's own state or the other player's state except for names and position in the two-player list. Neither policy may mutate the observation it receives, and every generated action must be legal on the transformed own state.

## Argument and verification method

The transformations preserve the observer-relative physical state by construction: after a swap, the state originally at index p lies at index 1-p, which is also the new observer index. The other state likewise remains the opposing state. Names are public metadata. Reversal applied twice restores the unnamed observation. This is checked directly for every observation used.

Fresh instances preserve any dependence on earlier decisions. Induction over rounds establishes the finite history assertion if each checked action list is equal. For a prefix round neither instance is called and the prescribed submissions advance the original engine. At an actual call, equality verifies the assertion for that history prefix. The original engine then advances on the two retained submissions and its full round records must equal the stored records. Thus the next observation is exactly the next retained state. This continues through the recorded terminal round.

The declaration pins the candidate, its source closure, the checker, all job/result/replay inputs and the parent campaign metadata before any transformed candidate call. Every case runs in a fresh interpreter, and every failed attempt or timeout is retained. The summary reports all 72 cases and actual call counts. A discrepancy refutes the finite assertion and must be retained, not discarded or repaired by changing the candidate.

## Dependencies and scope

The unchanged bundled Engine, balanced rules, original retained actions, frozen candidate sources and this checker's transformation logic are dependencies. No opponent policy is called. There are no new matches, no new random samples and no new W/D/L outcomes. Passing verifies two particular metadata transformations on these finite histories only. It does not prove that the candidate ignores every possible name in every reachable state, that arbitrary opponents ignore names, or that the game hides opponent identity. The engine exposes both configured names and the observer index. Full-game adaptation can still use visible gameplay history.
