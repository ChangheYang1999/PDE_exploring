# Selective early attack after visible route investment

Written 2026-10-31T16:24:04.960274+00:00, before the new selector is implemented or evaluated.

## Exact policy and hypotheses

Use the unchanged two branches of ProjectedLeadSelector: E buys the corner gun and a tier4 in round four, then uses the public-budget joint wall/turret planner; G grows through round six and delegates to the frozen fortress in round ten. Both branches agree through round three on the registered standard-start histories. Let Q be the previous no-new-enemy-action round-four projection, including package presence, positive surviving own HP and a positive own-minus-enemy HP margin. Let L be the edge length of the shortest legal route on the visible enemy map and D the Manhattan distance between configured spawn and base.

The new rule chooses E exactly when Q holds and L > D, and G otherwise. Forced E and G retain their original meanings. If first invoked after round four it uses G. It reads only its observation and its own state. This rule was devised after seeing all 144 projection games, not independently of those outcomes. The test is development evidence.

## Conditional branch identity

Assume the source bytes and configurations are fixed, the branches make the same first three submissions against a given target, and subsequent branch decisions are reproducible under the recorded execution environment. A match of the selector against that target has the same complete normalized action/event history as the forced branch it chooses, if both see the same prefix.

Proof. The identical first three submissions and deterministic engine give identical states after each of the three rounds by induction. At round four the rule evaluates only that public state. The chosen branch is at its corresponding internal state after the common prefix and submits the same round-four action list as its forced version. The engine and target therefore receive equal actions and observations. Repeating this argument gives equal later actions and events until termination. The three-second cutoff retained in G makes execution reproducibility a hypothesis to verify, not a proved consequence of this induction.

The route predicate is public: shortest_path uses the configured grid, spawn, base and visible building cells. No policy identifier, current hidden enemy action, live engine state or external file is needed for the predicate. The fixed branch data remain explicit JSON dependencies.

## Motivation and open empirical claim

In the disclosed 24-target set, failed positive projections against E25RM, E30, lead8, eco3_t1 and eco6_t5 occurred on enemy routes of the unobstructed length. The intended rationale is to reserve the early attack for an enemy already investing in a long defensive route. This is a heuristic, not a theorem about investment, ability to defend, future purchases or winning. A route-building aggressive opponent can invalidate it.

The falsifiable repair claim is that the route gate removes the previous selector's ten losses on those 48 assignments while retaining its wins against the nominee opening variants. We will run all 48 assignments, independently replay them, regenerate every counter action, and compare each full history with the previously recorded selected branch. No additional fixed-branch games are needed for that exact comparison. A later separate experiment must challenge the route feature with aggressive route-building opponents and retain any failures.

## Dependencies and scope

Dependencies: ../round4_public_projection/PROOF.md and RESULTS.md, the original engine/configuration/pathfinder, ProjectedLeadSelector and its frozen branch sources, exact JSON map/guard data, and the declared campaign manifest. The mathematical claim is conditional history equality. The repair claim, legality, source stability and full-game outcomes remain OPEN. No pool C outcome is used to construct this rule, and the installed final candidate is unchanged.
