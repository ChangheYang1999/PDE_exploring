# Adding both final fortress rows to the recorded finite game

Prepared 2026-10-31T23:23:12.172221+00:00. This is a conditional algebraic theorem. The source and retained-record checks supplying its empirical premises are separate from the argument.

## Statement and dependencies

Let M be exactly the ten-by-ten skew-symmetric W/D/L matrix in `bot_research/experiments/validation/analysis/frr1_equilibrium/PROOF.md`, ordered as best_v9e, best_v9f, af2g, P5TNUBM, v41, V29, g1, guard00, threat_defender, AS1C. Wins, draws and losses have payoffs 1, 0 and -1. Its diagonal is imposed as zero, not measured. The earlier proof establishes value zero and the complete optimal set

S = {(0,d,0,p,0,0,1/3,1/3,0,c): c,d,p >= 0 and c+d+p = 1/3}.

Adjoin one or both strategies a = v46 and b = v48. Assume each added row against the ten original columns is

r = (-1,-1,-1,0,0,1,-1,-1,1,-1),

which is the original v41 row. Impose zero added diagonals and reverse signs on the transposed entries. If both strategies are added, let their unmeasured mutual entry E[a,b] = q be any real number and E[b,a] = -q. No assumption that q is zero is made.

**Theorem.** The extended matrix E has value zero. Its complete row and column optimal sets are S with zero weights on the added coordinates. In particular, both v46 and v48 have weight zero in every optimum, irrespective of q.

## Proof

Let z give weight 1/3 to AS1C, g1 and guard00 and zero to every other strategy, including any added strategy. The earlier matrix multiplication gives Mz <= 0 coordinatewise and z^T M >= 0. Each new row gives r z = (-1-1-1)/3 = -1. By skew symmetry, z's payoff against each new column is +1. Thus the same z, extended by zeros, is both a row guarantee of at least zero and a column guarantee of at most zero for E. Its zero weights on a and b make q irrelevant to both calculations. The value is therefore zero.

Let x be any optimal row strategy for E. Its payoff against z must be nonnegative. Every coordinate of E z is nonpositive, and the coordinates for a and b are strictly negative, equal to -1. Since x has nonnegative coordinates, x^T E z can be nonnegative only if x assigns zero weight to each added strategy. Its restriction to the original coordinates is then a probability vector that guarantees at least zero against every original column. It belongs to S by the earlier theorem.

Conversely, take any x in S and pad it by zeros. The earlier proof shows that it guarantees at least zero against all original columns. Its payoff against each added column is -x^T r = 1-p. Since 0 <= p <= 1/3, this is at least 2/3. Thus it also guarantees at least zero against every added column and is optimal for E. This proves necessity and sufficiency for the row set. Skew symmetry gives the identical column optimal set. The equilibrium profiles are all pairs of these optimal strategies.

## Empirical premise and limits

The independent archived-record aggregation in `../record_audit_initial.json` joins the full opponent specification, start condition and physical candidate seat. All twenty standard-start frr3 conditions and all twenty frr5 conditions give the stated row in both seats. Every matched condition also agrees in terminal HP and round count. This strengthens the observed equality but is unnecessary for the algebraic theorem.

This is a theorem about each such finite matrix completion, including the joint extension. It is not a measured v46 versus v48 result, a theorem about the full tower-defense game, or a reason to deploy a randomized controller. Self-play entries remain imposed zeros. Reproduction of these payoffs by later executions, under changed opponents, starts, source bytes or clock behavior, is an additional premise. The prior frr1 audit's limitations on historical runtime JSON and erased attempts remain in force. No game, policy, engine replay or project checker was executed for this argument.
