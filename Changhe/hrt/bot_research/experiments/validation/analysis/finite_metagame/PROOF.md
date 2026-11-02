# A certificate for a finite empirical policy game

## Statement, hypotheses and notation

Fix a finite list of n policies and one explicitly specified initial-state
condition. Let A be a rational n by n matrix with A_ij equal to the row
policy's payoff against the column policy, averaging the two player
assignments. A win pays 1, a draw 0 and a loss -1. Suppose each off-diagonal
entry is supported by the two recorded games, their outcomes and conditions
are checked, and A_ji = -A_ij. Put A_ii = 0, the symmetric self-play payoff.
This defines an empirical finite game. It does not assert that the entries
are exact expectations for nondeterministic policies or future machine loads.

Suppose rational numbers p_1,...,p_n satisfy p_i >= 0, sum_i p_i = 1, and
sum_i p_i A_ij >= 0 for every j. Then p is a maximin strategy with value zero
in this finite game. Against every probability distribution q over the
listed column policies, its expected payoff is nonnegative.

The random realization drawn from p must remain unknown while the opponent
selects its policy. The opponent may know p. It may also adapt during the
game exactly as its listed policy does; that behavior is already included
in A. No assertion is made about an opponent outside the list, a new initial
condition, or an opponent that can select a different policy after seeing
the random realization.

## Proof

For any probability vector q, linearity gives
p^T A q = sum_j q_j (sum_i p_i A_ij) >= 0.
Thus p guarantees at least zero in the stated finite game.

Antisymmetry gives x^T A x = 0 for every real vector x, since this scalar is
its own transpose and its transpose is -x^T A x. For any proposed row
probability vector x, the opponent can choose the same vector, obtaining
payoff zero for the row player. No row strategy therefore guarantees more
than zero. The feasible vector p attains that upper bound. This proves the
claim without relying on numerical optimization tolerances.

## Dependence on data and implementation

The certificate consists only of exact nonnegativity, normalization and
matrix-product checks. A floating-point optimizer may propose p; its output
has no force until the rational checks pass. The matrix and rational
certificate are stored as JSON. The independent checker uses Fraction
arithmetic and does not trust the optimizer's success flag.

The initial application uses the lead's c2rr1 development round robin. An
independent original-engine replay audit must establish its recorded actions
and outcomes before it supplies the matrix. Replaying actions does not prove
that the named policy generated them. Source attestations, consistent version
identities and the earlier match execution provide separate evidence for
that association. A successful certificate applies only to this finite,
empirical table, not to the full tower-defense game.

Verification artifacts are listed in verification/evidence.json. This is an
informal argument, not a theorem-prover formalization.
