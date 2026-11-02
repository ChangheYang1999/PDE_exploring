# A finite policy comparison after the early-heavy counter

## Statement and hypotheses

Fix four exact policy specifications and standard initial conditions under the bundled engine: A=P4TNUB, B=P5TNUBM, C=the early-heavy handoff6 controller with its P5TNUBM public model, and D=the HP-lead8 handoff controller from the nominee-handoff declaration. Use their declared parameters without retuning. An edge X to Y means both original-engine games, with X assigned to each physical seat in turn, end in an engine-declared win for X. A draw or divergent pair supplies no such edge.

If a directed cycle is present, no policy on that cycle beats every other policy on the cycle. If the complete finite payoff matrix admits a verified rational mixed-strategy certificate, that certificate applies only to these policies and this initial-state condition.

The new empirical questions are A against B, A against C, and C against D. The other three unordered pairs already have checked games in early-heavy-handoff and nominee-handoff. Reusing them adds no independent samples. In particular, C's public clone remains B when its actual opponent is A or D; it is not retargeted. The controller remains a valid observation-based policy, but its forecast may be wrong.

## Argument

In a directed cycle X1 to X2 to ... to Xk to X1, each Xi is beaten by its predecessor in both assignments. Thus Xi cannot beat every other cycle member. This is a finite counterexample to universal dominance within the listed set, without any conclusion about an unlisted policy. Every edge requires exact source and parameter identity and checked outcomes; matching informal policy names is insufficient.

For a finite payoff table, assign 1 to an engine-declared win, 0 to a draw and -1 to a loss, and average the two assignments. Swapping row and column reverses the sign by definition. The resulting skew-symmetric matrix, together with a rational probability vector whose payoff against every column is nonnegative, satisfies the theorem in ../finite_metagame/PROOF.md. That argument is algebraic. It does not convert repeated deterministic games into population evidence or certify the game-theoretic value of the full tower-defense game.

No result is assumed for the three new pairs. If there is no cycle, the complete table must say so. Source files, results, replay hashes and any rational certificate belong alongside this argument. Full replay proves the recorded transitions and outcomes; separate policy-generation checks support association of these actions with the named controllers.

## Dependencies and scope

The existing pair evidence is in ../nominee_handoff/RESULTS.md and ../early_heavy_handoff/RESULTS.md. Legality and public-information scope for C are in ../early_heavy_handoff/PROOF.md. D's public state trigger is covered by ../hp_handoff/PROOF.md. The finite matrix theorem is in ../finite_metagame/PROOF.md. This is an informal conditional argument and a preregistered empirical comparison, not a claim of global optimality.
