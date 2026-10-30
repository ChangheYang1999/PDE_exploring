# Independent assembly of registered forcing norms

## Exact quantities and inputs

Let F be the full-plane residual of the exact potential C1-N1-007-d2w-j7-e2bal, at c = 4076476460239181/2251799813685248. The source and every numerical dependency are identified in source/MANIFEST.json. Put J^s = (1-Delta)^(s/2), omega = (1+4r^2)^(2/5), and

    G0 = ||F||2, G1 = ||grad F||2,
    P2 = ||omega D^2 F||2, Q3 = ||omega D^3 F||2,
    E_w(F)^2 = P2^2 + w1 G1^2 + w2 G0^2,
    X_(s,w)(F) = E_w(J^s F).

The tensor convention is the complete ordered Cartesian tensor, so |D^2 F|^2 = F_xx^2 + 2 F_xy^2 + F_yy^2, and the third tensor has multiplicities 1,3,3,1. All quantities are full-plane norms. F is smooth and has the exact far-field cancellations required by the no-negative-norm registry. The complete components G0, G1, P2 and Q3 have independent numerical confirmation in N4-139, N4-153, N4-166 and N4-170. Their containing balls, not their displayed midpoint digits, are the arithmetic inputs.

This audit applies the already audited comparison of theory_v03, section 2, NORM-T-XSW-v1. It does not prove a new operator estimate. For 0<s<1 with 1-(48/25)s>0, the comparison is

    (1-(48/25)s) E_w <= X_(s,w)(F)
        <= E_w^(1-s) (2 Q3^2 + C_w E_w^2)^(s/2)
           + (48/25)s E_w,

where C_w = 409657/25 when (w1,w2) = (2^14,2^18), and C_w = 819257/25 when (w1,w2) = (2^15,2^20). The registry attributes the proof to T2-R3, independently audited through T4-042. The lower bounds gamma_0 >= G0 and gamma_1 >= G1 follow from the Bessel multiplier and the registered graded comparisons.

The numerical instances are s = 1/7744, 1/5184, 1/5476, 1/6561, and 2^-17, with their exact weights and sufficient thresholds from the registry. A norm larger than a sufficient threshold excludes that sufficient smallness test. It does not by itself prove that the stated correction ball has no solution, or exclude an alternative inverse theorem. The independently audited weak distances are a separate result.

## Containing arithmetic and monotonicity

Suppose exact G0, G1, P2, Q3 lie in their positive input intervals. The square-root expression E_w is increasing in each component. Both the lower comparison expression and the upper comparison expression increase in E_w, and the latter increases in Q3: all factors have positive exponents, s<1, and positive coefficients. Substituting lower component endpoints in the lower expression and upper endpoints in the upper expression therefore gives a whole-plane norm enclosure. Arb evaluation encloses the exact expressions including endpoint rounding. Each input interval is formed as the union of its lower and upper containing balls.

For the relative contribution to E_w^2, calculate each nonnegative weighted component divided by the sum of all three. This is an interval division, retaining correlations only through inclusion; the resulting enclosing interval remains valid. It describes this quadratic energy, not the operator's difficult direction or the best optimization objective.

For comparison with N3, first check equal raw and canonical candidate semantics through the independently confirmed source records. Then evaluate the same monotone formulas from N3's frozen component intervals, without executing N3 code. The resulting enclosures need not have the same endpoints because the two weight approximants have different errors. The own narrower complete component interval must lie inside the peer component interval when strict containment is available, and otherwise must overlap. Every coarse published interval below is checked directly against the own containing expression; a numerical overlap alone never proves correctness of either derivation.

## Decimal output

Rounding an upper or lower binary endpoint to nearest decimal does not generally preserve its direction. Therefore the output retains containing balls and separate rational floors and ceilings. A binary64 number may propose a rational endpoint, but an exact Arb inequality must verify it. The verification repeats with a wider rational proposal if needed and stops if it cannot certify containment. For a strict lower bound L use a rational q satisfying the full-ball inequality q<L; for an upper bound U use p with U<p. Positive thresholds are exact rationals, and the same rule applies to their ratios.

The checker also tests the generic nearest-decimal endpoint failure on an exact rational fixture and checks the frozen N3 weighted Hardy-proxy square. A display-format issue has no automatic consequence for a wide bound on another mathematical quantity, and any affected scope is stated separately.

## Dependencies and verification

The local source manifest freezes the registered definitions, N3's component and assembled records and assembly code, and N4's four independently confirmed component records. N3 code is inspected, never executed. Verification uses independent scalar expressions at 512 bits, complete input hashes, exact rational thresholds, and strictly outward decimal endpoint checks. The computation is small and runs between the serialized field integrations. All new results are retained with actual timestamps. Numerical agreement confirms these derived comparisons and their limited sufficient-test conclusion. It does not certify missing background, inverse or nonlinear hypotheses.
