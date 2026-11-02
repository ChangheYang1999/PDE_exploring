# The AF5 row changes the optimal support of the recorded finite game

Prepared 2026-10-31T23:40:11.361486+00:00. The informal argument was written before its new exact-arithmetic verification. This is a conditional finite matrix-game theorem. Empirical row authentication is a separate obligation, recorded in `verification/`.

## Exact object and hypotheses

Use the coordinate order

`best_v9e, best_v9f, af2g, P5TNUBM, v41, V29, g1, guard00, threat_defender, AS1C, AF5`.

Let A be the following eleven-by-eleven real matrix. Its upper-left ten-by-ten block M is defined by this table, and its last row against the first ten columns is r = (1,1,1,-1,1,1,1,1,1,-1). Set the last column to minus that row, transposed, and the last diagonal entry to zero.

| Row / column | best_v9e | best_v9f | af2g | P5TNUBM | v41 | V29 | g1 | guard00 | threat_defender | AS1C |
| --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| best_v9e | 0 | 0 | 0 | 0 | 1 | 1 | 1 | -1 | 1 | -1 |
| best_v9f | 0 | 0 | 0 | 0 | 1 | 1 | 1 | -1 | 1 | 0 |
| af2g | 0 | 0 | 0 | 0 | 1 | 1 | 1 | -1 | 1 | -1 |
| P5TNUBM | 0 | 0 | 0 | 0 | 0 | 1 | 1 | -1 | 1 | 0 |
| v41 | -1 | -1 | -1 | 0 | 0 | 1 | -1 | -1 | 1 | -1 |
| V29 | -1 | -1 | -1 | -1 | -1 | 0 | 1 | -1 | 1 | -1 |
| g1 | -1 | -1 | -1 | -1 | 1 | -1 | 0 | 1 | 1 | -1 |
| guard00 | 1 | 1 | 1 | 1 | 1 | 1 | -1 | 0 | 1 | 1 |
| threat_defender | -1 | -1 | -1 | -1 | -1 | -1 | -1 | -1 | 0 | -1 |
| AS1C | 1 | 0 | 1 | 0 | 1 | 1 | 1 | -1 | 1 | 0 |

The empirical interpretation assigns payoff +1 to a win, 0 to a draw and -1 to a loss on the standard start. It requires the retained frr1 games to supply M and the twenty retained afrr result rows to supply r, with both physical seats agreeing on each strategy's outcome. All diagonal entries are imposed zero conventions. Neither campaign measures self-play. A is skew-symmetric, meaning A^T = -A; it is not a symmetric numerical matrix.

For the simplex Delta of probability vectors, the row payoff is x^T A y. The row max-min value is max over x in Delta of min over columns j of (x^T A)[j]. These definitions specify a finite strategic-form game. They do not assume that new executions reproduce its measured entries.

## Theorem and value certificate

**Theorem 1.** The value is zero. The complete row and column optimal sets are

S_new = {(0,0,0,p,0,0,0,1/3,0,c,1/3): p,c >= 0, p+c = 1/3}.

Thus AF5 and guard00 each receive exactly one third; the remaining third is split arbitrarily between AS1C and P5TNUBM. Every other coordinate, including g1 and best_v9f, has zero weight in every optimum. All equilibrium profiles are S_new x S_new.

Take z uniform on guard00, AS1C and AF5. Direct multiplication gives

A z = (-1,-2/3,-1,0,-1,-1,-1/3,0,-1,0,0)^T.

Every entry is nonpositive. Skew symmetry gives z^T A = -(A z)^T, whose entries are all nonnegative. Therefore z guarantees at least zero as a row strategy and at most zero as a column strategy. The value is exactly zero.

This certificate reflects the three recorded edges guard00 beats AS1C, AS1C beats AF5, and AF5 beats guard00. The rest of the calculation checks that no other row can exploit their uniform mixture.

## Necessity of the stated weights

For an optimal row strategy x, all coordinates of x^T A are nonnegative, hence x^T A z >= 0. Each coordinate of A z is nonpositive. Its strict entries force x to vanish outside P5TNUBM, guard00, AS1C and AF5. This is a strict dual certificate, not an inference from weak dominance.

Write a = x[AF5], b = x[guard00] and t = x[P5TNUBM] + x[AS1C]. Then a+b+t = 1. The payoffs against guard00, AF5 and AS1C, respectively, are a-t, t-b and b-a. Each is nonnegative. Consequently a >= t >= b >= a, so a=b=t=1/3. This proves every necessary restriction in the theorem.

## Sufficiency, including either endpoint of the split

Let x have the form stated in Theorem 1. The complete payoff vector is

x^T A = (2/3+c, 2/3, 2/3+c, 0, 2/3+c, 1, 1/3, 0, 1, 0, 0).

All coordinates are nonnegative for 0 <= c <= 1/3, and some are zero. Thus every such x guarantees exactly zero. This includes p=0 and c=0 and proves sufficiency for the entire line segment, not only its endpoints. Skew symmetry identifies the column optimal set with the row optimal set. A zero-sum equilibrium consists exactly of a pair of optimal strategies, proving the last assertion.

## Every earlier optimum is exploited by the AF5 row

The prior frr1 proof gives

S_old = {(0,d,0,p,0,0,1/3,1/3,0,c): c,d,p >= 0, c+d+p = 1/3}.

For every x in S_old, AF5's payoff r x is

1/3 + 1/3 + d - p - c = 1/3 + 2d.

It lies in [1/3,1] and is strictly positive, including d=0. Equivalently, the old mixture's payoff against the added AF5 column is negative. None of the old optima, padded with zero AF5 weight, remains optimal in A. This changes the empirical finite game's support; it does not invalidate the earlier theorem about its original ten-by-ten matrix.

## Fortress additions, including unmeasured edges

**Theorem 2.** Adjoin any finite number of rows F_i whose payoffs against the original ten strategies equal the v41 row

s = (-1,-1,-1,0,0,1,-1,-1,1,-1).

Let A_extended[AF5,F_i] = alpha_i be any real in [-1,1]. Reverse signs on transposed entries and impose zero diagonals. The mutual entries between distinct added F_i may be arbitrary real numbers, with their transposes negated. Then the value is zero and the complete row and column optimal sets are S_new padded with zero weights on every F_i.

To prove this, extend z by zeros. Its dual entry for F_i is

(-1-1-alpha_i)/3 <= -1/3 < 0.

Thus the old value certificate still works, and the strict dual entry forces every optimal strategy to put zero weight on each F_i, independently of all mutual entries. Any such optimum restricted to A must lie in S_new. Conversely, for x in S_new, its payoff against F_i is

(1+alpha_i)/3 + c >= 0.

So every padded x remains optimal against all added columns. Skew symmetry proves the column assertion as before.

This covers v46 and v48 conditionally on the recorded frr3 and frr5 rows s. In particular, AF5-v46 and v46-v48 need not be supplied as fabricated draws. Their unmeasured entries remain explicit variables. Any later measured frr8 AF5-v48 W/D/L entry is in [-1,1] and can specialize alpha_v48, provided its physical-seat convention is consistent with the matrix interpretation. The theorem itself requires no prediction of that game.

## Evidence dependencies and limits

The base definition and prior optimal set come from `bot_research/experiments/validation/analysis/frr1_equilibrium/PROOF.md` and its `verification/independent_audit_001.json`. The AF5 premise comes from `bot_research/runs/economy/afrr/results.jsonl` and the independent source/result inspection `bot_research/experiments/validation/reviews/economy_final_gate_001/afrr-20261031T233750162131Z/inspection.json`. The latter receipt reports twenty complete conditions and sixteen wins, zero draws and four losses; its exact bytes and input archive edges must be authenticated separately. Optional fortress premises use frr3 and frr5, with the sealed review `bot_research/experiments/validation/reviews/frr5_frr6_final_fortress_001/`.

The exact JSON matrix and verification receipt beside this proof supply the machine-readable finite object and input hashes. They check arithmetic and recorded-row joins; they are not a proof of the engine or of future policy behavior. The informal necessity arguments above are essential because checking two extreme mixtures alone would not characterize every optimum.

AF5 was chosen during research before afrr; some afrr opponents repeat earlier observations. Its twenty conditions are not twenty independent strategy samples. afrr retained loss logs only, so its win rows do not have complete action histories in that campaign. Source hashes and row summaries cannot repair that missing evidence. The earlier frr1 audit also does not establish historical runtime JSON identities, absence of erased attempts, or continuous historical source integrity. No part of this proof supplies those missing guarantees.

All statements concern the defined W/D/L matrices. They do not concern an HP-margin payoff, scripted starts, untested opponents or the optimum of the full tower-defense game. Some policy dependencies inspect clocks. A controller that randomly selects one of these strategies would inherit the displayed payoffs only if the selected, correctly initialized executions reproduce them under its actual observations and timing. No such controller was implemented or evaluated here, and this proof does not change the deployed entry point.
