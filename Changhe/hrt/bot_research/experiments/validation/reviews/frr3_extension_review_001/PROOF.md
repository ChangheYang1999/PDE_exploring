# The duplicate v46 row preserves the recorded frr1 optimal set

Written 2026-10-31T22:45:12.541168+00:00. This is a standalone finite matrix argument. Its empirical premises are separately audited retained W/D/L outcomes, not assertions of repeatability under every execution deadline.

## Exact statement and hypotheses

Let the ten old strategy labels be ordered as follows: best_v9e, best_v9f, af2g, P5TNUBM, v41, V29, g1, guard00, threat_defender, AS1C. Let M be exactly the real matrix below. All ten diagonal entries are imposed zeros. No old self-play outcome is inferred from a physical game.

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


Add one new label v46. Define the eleven-by-eleven matrix N by preserving M on the old labels, setting N[v46,j] = M[v41,j] for every old label j, setting N[j,v46] = -M[v41,j], and imposing N[v46,v46] = 0. In particular, N[v46,v41] = N[v41,v46] = 0. The retained frr3 games supply the stated new off-diagonal W/D/L entries in both physical assignments. The new self-play zero is a convention, not a measured result.

The row player maximizes x^T N y and the column player minimizes it, where each vector is a nonnegative real probability vector on the eleven labels.

Theorem: the value is zero. The complete set of row max-min mixtures consists of weight 1/3 on g1, weight 1/3 on guard00, and the remaining 1/3 distributed arbitrarily and nonnegatively over AS1C, best_v9f and P5TNUBM. All other weights, including v41 and v46, are zero. The column minimax set is the same set. Every equilibrium profile is a pair of such mixtures.

## Argument

First establish the old optimal set directly from the displayed M. Put probability 1/3 on each of AS1C, g1 and guard00, calling this vector z. Direct multiplication gives

z^T M = (1/3, 0, 1/3, 0, 1, 1/3, 0, 0, 1, 0),

and Mz is the negative transpose of that vector. Thus z gives a primal lower bound zero and a dual upper bound zero, proving value zero.

For any old optimal x, x^T Mz is both nonnegative and the sum

-(x[best_v9e] + x[af2g] + x[V29])/3 - x[v41] - x[threat_defender].

Consequently all five displayed weights vanish. Write a = x[g1], b = x[guard00], and t = x[AS1C] + x[best_v9f] + x[P5TNUBM]. The guard00, g1 and AS1C columns respectively give a >= t, t >= b, and b >= a. Since a+b+t = 1, all equal 1/3. Conversely, put weights c,d,p on AS1C,best_v9f,P5TNUBM with c+d+p = 1/3. The complete old column-score vector is

(c, 0, c, 0, 1-p, 1/3, 0, 0, 1, 0),

which is nonnegative and has minimum zero. This proves both necessity and sufficiency over the full face, including its boundary.

Now define a map F from eleven-label probability vectors to ten-label vectors by adding the v46 weight to the v41 weight and retaining every other coordinate. By the definition of N, the complete v46 and v41 rows are identical, as are their columns. Therefore, for every pair of eleven-label probability vectors x,y,

x^T N y = F(x)^T M F(y).

The map F is onto the old simplex. Hence the worst payoff of x in N equals the worst payoff of F(x) in M. Thus x is optimal in N exactly when F(x) is old-optimal. Old optimality requires F(x)[v41] = x[v41] + x[v46] = 0. Nonnegativity forces both summands to vanish; all other old restrictions transfer unchanged. This proves the complete new optimal set, not merely feasibility of selected mixtures.

Skew symmetry gives the same column optimal set and the stated equilibrium profiles. An old-optimal mixture scores 1-p against the added v46 column, so its score there lies in [2/3,1]. This also directly verifies the report's lower bound 2/3.

## Dependencies, evidence and limits

The displayed M agrees with the prior standalone proof at bot_research/experiments/validation/analysis/frr1_equilibrium/PROOF.md, SHA256 e6656f1850ba2cf85deea5170edfcd5a73ab7a53db3830bcb34a7dbcdefd035d. Its retained result and all 90 original log hashes were rechecked in frr1_identity_supplement.json. The new ten opponent pairs and both physical assignments were parsed from all 20 retained frr3 logs; audit.json retains the exact specification identities and input hashes. The exact Fraction calculations independently check all three vertices of the old face in N. The preceding argument establishes necessity for the full continuum of mixtures.

Formal sources: none. This is an informal proof over an explicitly displayed finite matrix. It does not claim identity of HP margins or game trajectories between v41 and v46; their threat_defender margins differ. It does not infer the unmeasured v46 self-play result, prove load independence, authenticate historical runtime JSON beyond the retained provenance, or establish a strategy of the unrestricted tower-defense game. A randomized policy implementing this mixture would additionally require the selected execution payoffs to reproduce these entries.
