# Sufficient derivative premises for the conditional profile theorems

Status: CONFIRMED as A601 after full source, dependency and independent-proof postreads of Theory Agent A Note A25 item5. This combines already confirmed estimates; it does not derive a derivative bound from velocity decay.

## 1. Exact statement

Fix 0<c<1 and any finite real omega. Let U in C2(R3;R3), P in C1(R3) solve div U=0 and

    ((1-c)I+omega J)U+DU((cI-omega J)y+U)+grad P=0,
    J(y1,y2,y3)=(-y2,y1,0).

Assume U tends uniformly to0 at infinity. Each of the following sufficient premises gives DU->0 uniformly and |DU|+|curl U|<=C/(1+|y|):

1. DU is bounded.
2. |DU(y)|<=C0(1+|y|)^(1/2) for a finite constant C0.
3. Outside a ball, lambda_max((DU+DU^T)/2)<=1+c/2+epsilon(|y|), where epsilon is bounded, nonnegative and measurable and integral_R0^infinity epsilon(r)dr/r is finite.

The premises are alternatives sufficient for the same conclusion, not asserted pairwise equivalent as arbitrary function conditions. The constants in the conclusion may depend on the profile, c and omega. If also c>1/3, the stronger natural estimates |DU|<=C(1+r)^(-1/c) and |U|<=C(1+r)^(-(1-c)/c) hold.

## 2. Proof and dependency check

Premise1 gives bounded U and DU. A492 proves DU->0 and |curl U|=O(1/r), independently of any Dini or C36 assumption. A476 then gives DU=O(1/r). Premise2 is exactly A498(B), with no smallness requirement for C0. Once its derivative decay holds, compact continuity gives a global bound and A492,A476 apply.

For premise3, put B=(cI-omega J)y+U, G=DU, W=curl U and M=sup|U|. The complete carrier flow has radial derivative cr+O(M). Every sufficiently large point is reached by a unique outward trajectory from a fixed sphere. Its elapsed time s obeys cs=log(r/R1)+O(1), with constants uniform over that sphere. Along that trajectory the exact vorticity equation gives

    d log|W|/ds<=lambda_max(sym G)-1<=c/2+epsilon(r(s))

where W!=0; zero W is preserved and satisfies the resulting estimate too. Since dr/ds>=cr/2 outside R1,

    integral epsilon(r(s))ds<=(2/c)integral_R1^infinity epsilon(r)dr/r.

Hence |W|<=C r^(1/2). Trace(sym G)=0 and its eigenvalues are bounded above by the finite number 1+c/2+sup epsilon, so its operator norm is bounded. The skew part has norm |W|/2. Thus |G|<=C(1+r)^(1/2), reducing to premise2. This is the complete short argument of A506, whose independent proof has been reread.

When c>1/3, U->0 implies U(R dot)->0 distributionally, and the now bounded gradient lets A477 give G=O(r^(-1/c)). Since 1/c>1, integrate the radial derivative along a ray from r to infinity using U(infinity)=0. It gives |U|<=C r^(1-1/c). Compact continuity handles small r. These are precisely the natural velocity and derivative exponents.

## 3. Consequences and limits

In the target interval2/5<c<1/2, every occurrence of the half-power derivative premise in the full conditional axisymmetric-tail theorem A570, the actual-tail package called HF+, or the A2/exterior-density theorem A598 can therefore be replaced by premise1 or3. All other hypotheses remain: in particular global zero helicity, actual-tail symmetry for A570, and original exterior density or exterior analyticity plus the scalar A2 alternative for A598. The general witness theorem A571 does not itself need this extra derivative premise.

Premise3 asks only for the upper largest-strain bound. Trace freedom supplies the remaining strain eigenvalue bounds inside the proof. No derivative, strain, density, A2 or symmetry hypothesis follows here from bare U->0. The displayed quantitative threshold is sufficient, not a sharpness assertion for Euler profiles. No computation is needed.
