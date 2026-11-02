# Terminal selection with one exact retained model

## Statement, hypotheses, and notation

Consider the final configured round of the unchanged bundled game. Adopt the fixed-construction and exact-combat hypotheses of `../catalogue_attack_selection/PROOF.md`. In addition, assume that exactly one catalogue model remains and that it is the actual opponent policy, with its private state synchronized. A singleton produced by eliminating other models does not by itself establish this last hypothesis.

Let P be the finite, nonempty set of affordable ordered minion-purchase sequences actually evaluated by `AdaptiveCatalogue`. Its already chosen construction is fixed. Let H and K be the two bases' HP before combat, r the exactly predicted incoming damage, and d(p) the exactly predicted outgoing damage for p in P. Appending offensive minions does not change the counter's defensive map or the opponent's attacking roster. Thus r is independent of p. Factories purchased with the remainder affect neither base's HP in this round.

Order terminal results as loss < draw < win. Under these hypotheses, the purchase selected by the implemented final-round ranking attains the best terminal result among P. This is conditional optimality within the evaluated purchase set, with construction held fixed. It is not optimality among all legal actions, a guarantee that the remaining model is true, or a statement about earlier rounds.

## Proof

Put u = H - r and v(p) = K - d(p). The original engine first settles both combat directions, then resolves destruction, then applies the final-round HP comparison if both bases remain positive.

For fixed u, the terminal result is a nondecreasing function of d(p). To check every case:

1. If u <= 0, the result is a loss while v(p) > 0 and a draw while v(p) <= 0. Increasing d can only decrease v, so it can change a loss to a draw but cannot worsen the result.
2. If u > 0 and v(p) <= 0, the result is a win.
3. If u > 0 and v(p) > 0, the result is the comparison of u with v(p): loss if u < v(p), draw if equal, and win if u > v(p). Decreasing v cannot worsen that comparison. Crossing v = 0 also leaves a win.

Now examine the ranking. Its first entry marks a forecast safe-lethal sequence: u > 0 and d(p) >= K. Every such sequence wins. If any such sequence exists, the selected sequence has that first entry and therefore attains the largest possible terminal result.

Otherwise every sequence has the same false first entry. With one model, the final-round utility is

    g(p) = d(p) - d(empty).

The subtracted baseline is constant. Maximizing g is therefore the same as maximizing d. The next ranking entry is again g; subsequent cost and length tie breakers only choose between sequences with the same outgoing damage. By the monotonicity just proved, the selected sequence attains the best terminal result among P.

These alternatives exhaust the ranking, proving the claim. If the immunity shortcut reduces P to the empty sequence, optimality within that singleton is immediate; it does not enlarge P or imply an untested search claim.

## Dependencies, limitations, and status

The proof uses the original engine's simultaneous-destruction and final-round HP rules, action isolation between the two player maps, and the exact-forecast assumptions of `../stateful_catalogue/PROOF.md`. Source references are recorded under `source/`; review evidence is under `verification/`.

The multi-model counterexample in `../catalogue_terminal_score/PROOF.md` has different outgoing baselines across retained models and therefore does not contradict this result. Outside-catalogue fallback does not satisfy the true-model premise. Approximate combat values or a wall-time-dependent target that diverges from its clone also invalidate the exact-forecast premise.

This is a standalone informal proof checked by the displayed case analysis and source inspection. No proof-assistant formalization, exhaustive reachable-state search, or full-game strength result is claimed. The mathematical argument was written without changing the policy or any active experiment.
