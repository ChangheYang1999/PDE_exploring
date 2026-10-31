# A modal gauge with fixed binary64 constants and stored stencil inputs

Status: proved finite-dimensional identities under explicit nonsingularity and positivity hypotheses. Decimal evaluations below are numerical checks, not certified enclosures.

## Statement

Let Q be a finite nonempty index set. Let n >= 3. A free leading coefficient array has n-2 real entries for each q in Q. Partition Q into blocks of one or two indices. For each block b with k_b indices, fix a real matrix C_b with 2k_b rows and nk_b columns. Order columns by the block index, then radial index 0,...,n-1. Let M_b be the square matrix formed by the last two radial columns for each index. Assume det(M_b) is nonzero.

For each channel A and C and each block, retain the prescribed free entries and determine the last two entries by C_b a_b=0. The two channels may use different matrices satisfying the same hypotheses. This defines unique linear expansion maps E_A and E_C.

Fix nonnegative real modal weights wT_q,wS_q and real scale factors pT_q,pS_q. For expanded arrays a and c set

N(a,c) = sum_q [wT_q (pT_q sum_k a_kq)^2 + wS_q (pS_q sum_k c_kq)^2].

No spherical-harmonic interpretation is required for this identity. In the intended application these weights and powers are the stated, already-rounded production constants, treated as exact real numbers. They are not silently replaced by recomputed real powers.

Let b_A,b_C be free base arrays and d_A,d_C free direction arrays. Expand both the base and direction by E_A,E_C. Define T_q=pT_q sum_k (E_A b_A)_kq, S_q=pS_q sum_k (E_C b_C)_kq, U_q=pT_q sum_k (E_A d_A)_kq and V_q=pS_q sum_k (E_C d_C)_kq. Then along the free line b+x d,

N(x)=A+2Bx+Cx^2,

A=sum_q(wT_q T_q^2+wS_q S_q^2),
B=sum_q(wT_q T_q U_q+wS_q S_q V_q),
C=sum_q(wT_q U_q^2+wS_q V_q^2).

If N(x)>10^-300 on an open interval about zero, the unclamped gauge g(x)=100(sqrt(N(x))-1) is differentiable there and g'(0)=100B/sqrt(A).

Let h>0. Let x_+,x_-,x_++,x_-- be four arbitrary stored real offsets, with N at all four points greater than 10^-300. They need not equal h,-h,2h,-2h. Put

D = [N(x_+)-N(x_-)]/[sqrt(N(x_+))+sqrt(N(x_-))],
D' = [N(x_++)-N(x_--)]/[sqrt(N(x_++))+sqrt(N(x_--))].

The finite differences of the gauge on those actual inputs, divided by their nominal step, are exactly

D2(h)=100D/(2h),
D4(h)=100(8D-D')/(12h).

These are identities for the stated four input points. Calling D2 or D4 a second- or fourth-order approximation additionally requires an appropriate statement about the offsets. In particular, no exact symmetry or asymptotic order is inferred merely from labels containing plus or minus h.

## Proof

Write the constraint equations for a block as M_b y + R_b f=0, where f consists of its free entries and y consists of its last two entries per index. Since M_b is nonsingular, y=-M_b^-1 R_b f is uniquely defined and linear in f. Joining the blocks proves that each expansion map is linear. Consequently its value on b+x d equals its value on b plus x times its value on d.

Each scaled radial sum is therefore T_q+x U_q or S_q+x V_q. Expanding the squares in the finite sum gives the coefficients A,B,C exactly. Differentiating the positive square root gives g'(0)=100(2B)/(2sqrt(A)). Positivity above the clamp threshold ensures this is also the derivative of the clamped implementation's real formula on the specified interval.

For any positive u,v, sqrt(u)-sqrt(v)=(u-v)/(sqrt(u)+sqrt(v)), because multiplication by the denominator gives u-v. Apply this identity to the two pairs of norm values. The constant minus one in g cancels in each difference. Substitution into the definitions of the two finite differences proves the stated formulas without any assumption of symmetric input offsets.

If all supplied matrix entries, free entries, modal weights and powers are finite binary64 values, they are dyadic rationals. Exact rational elimination computes the expansion and A,B,C as rational numbers when the matrices are nonsingular. The actual offsets obtained by subtracting two stored binary64 inputs as real numbers are also exact dyadic rationals. Thus all norm values and norm differences in these formulas can be computed exactly. Only the displayed square roots and divisions by expressions involving them require a further numerical approximation or certified enclosure.

## Dependencies and scope

Dependencies: finite-dimensional linear algebra, finite polynomial identities and the real chain rule. The modal norm interpretation for the Euler representation is proved separately in ../gauge_coefficient_derivative/PROOF.md. Invertibility of the intended real tail equations is discussed in ../tail_coordinates/PROOF.md; it does not automatically imply invertibility of an arbitrary rounded matrix. The rational implementation checks each supplied matrix by exact elimination.

An implementation must bind the supplied constraint rows, free base, directions, powers, weights and mode order to the production case. This theorem alone does not establish that correspondence. Importing a production JVP as a direction would not independently check the coordinate map. Nor does an arbitrary-precision decimal square root alone constitute a proved arithmetic error bound. Parameter directions are excluded: their matrices and constants vary and must also be differentiated.
