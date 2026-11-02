# Defensive handoff without an opponent policy model

## Statement and hypotheses

Use the unchanged balanced engine. Before a specified handoff round H, a controller follows the declared ScreenedGuardMaze opening. In one specified earlier round it attempts a bounded heavy purchase before the opening's proposals. From H onward it buys no minions. It constructs a finite list of hypothetical opposing rosters from the current public active roster R: R itself, and R followed by min(k, floor(B/c_t)) copies of each tier t, where B=floor(nG/d), G is the opponent's observed gold, c_t is its current cost, 0<=n<=d, d>0, and k is a declared finite cap. It asks the frozen free_plan routine for at most s turret additions within its own observed gold, applies only legal proposals, and then buys affordable factories before round48 up to a declared per-round cap.

Every returned action is legal in sequence, and the policy uses only the observation and its declared state. It uses no opponent policy clone or private action. There is no asserted bound on damage against all affordable mixed purchases, and no asserted full-game win.

The empirical question is whether this budget-based forecast preserves the round5 tier4 counter's 755:740 win against P5TNUBM. The first development matrix tests H=6 or7 and n/d in {1/4,1/2,1}, both physical assignments. A failure is a negative result for that complete policy, not a proof that opponent models are necessary.

## Notation and argument

At each decision reconstruct the owner's state from the public snapshot. Attempt each selected action on this independent reconstruction using the original apply_action, appending it if and only if accepted. Induction over the ordered proposals proves that the returned subsequence makes exactly the accepted state transitions. Original action validation depends only on the owner's state, so the other player's interleaved actions do not invalidate this subsequence. The same reasoning covers the early heavy purchase followed by opening actions and the subsequent factory purchases. A factory is added only after its affordability is checked on the already updated state.

The active roster is obtained from the observed entries and the engine's active-round predicate, preserving entry order. Each appended pure-tier count is an integer expression in constructor parameters, observed gold, and public costs. Every other input to the bounded turret planner is the owner's public state or the public rules. Thus no current opposing submission is accessed. Removing an opponent clone avoids any assumption about the identity or synchronization of that clone.

The hypothetical set is deliberately finite and incomplete. A mixture can have different dense indices, modulo spawn phases, gun interactions, and arrival counts from any pure-tier extension. Even if the original combat engine confirms zero damage for every enumerated roster, this does not certify every affordable roster. The count cap may also omit affordable pure-tier rosters. Moreover, greedy planning may fail to find a defense that exists or may spend more than necessary, reducing later income. These observations prevent any logical inference from the hypothetical set alone to a guaranteed win. Complete original-engine matches and separate fresh-policy reproduction are required to answer the empirical question.

## Dependencies and scope

Legality uses td_game/actions.py and the ownership-local transition property of engine.py. Active-roster semantics use state.py. The planner is the already frozen economy/v17/freeplan.py, with its documented greedy stopping rule and frozen local simulator; full-game outcomes use the unchanged original engine. The mixed-roster limitation is demonstrated separately in ../pure_tier_threat/PROOF.md. The earlier exact-model comparison is in ../early_heavy_handoff/PROOF.md and RESULTS.md. This is a standalone informal argument, with no proof-assistant claim. Parameters and all data dependencies must be pinned before the matrix starts.
