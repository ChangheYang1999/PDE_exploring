# Aggressive route builders as a challenge to the route gate

Written 2026-10-31T16:30:18.481250+00:00, before these new matches.

## Statement, notation and scope

Use the unchanged RouteGatedSelector with its public round-four predicate Q and L > D, as defined in ../route_gated_selection/PROOF.md. The empirical hypothesis is that this predicate can still select a losing early branch against an aggressive route-building opponent while the unchanged growth branch draws or wins. A qualifying witness must occur in both physical assignments, pass every strict and replay check, and have the adaptive complete trajectory equal to its selected forced-branch trajectory.

The declared finite challenge consists of four existing MazeGrower layouts (empty, lead_opening, cash_rank_1, cash_rank_10), two last growth rounds (3 and 6), and two repeated attack tiers (tier1 and tier5). There is no bait; factory and purchase caps retain the existing defaults. Each of these16 complete opponents is compared with adaptive, forced early and forced growth, in both seats:96 new games. All are standard starts. Layouts and policy implementation are already known; these tests are an adversarial development expansion, not a held-out estimate of population strength. No pool-C outcome is used to choose this matrix.

## Why the predicate has no guarantee

On these standard prefixes, both branches spend rounds1-3 on the same actions. The opponent's visible route is determined by its round-one wall layout. Route length depends only on the blocked cells, and can exceed D even if the opponent intends to spend future income on attacks. Likewise Q forecasts the next combat only under no new enemy action. Nothing in either predicate restricts a current hidden purchase or later offense. Therefore the predicate does not imply the absence of a losing continuation. This logical observation does not itself establish a full-game counterexample; the complete games must supply one.

For each new target, the conditional branch-identity induction from ../route_gated_selection/PROOF.md applies. The audit will regenerate the decisions, verify the public predicate and compare every adaptive history with the selected forced mode. Any clock-dependent disagreement is a failed control, retained in the evidence rather than counted as a strategic result.

## Dependencies and reproducibility

Dependencies: the existing unmodified maze_grower.py, route_projection_selector.py and both branch source closures; exact maze, guard and template JSON inputs; the unchanged original engine and configuration; and the two48-game manifests. Proof and source hashes are declared before execution. Every valid or failed attempt is retained. The report must show all sixteen rows and all three modes, including controls that do not challenge the predicate.
