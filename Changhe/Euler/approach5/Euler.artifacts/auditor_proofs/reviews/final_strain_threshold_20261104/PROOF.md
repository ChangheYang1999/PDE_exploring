# Final check of the one-sided strain criterion

This is a final-phase recheck of A506. Its derivative-growth premise remains additional to bounded or decaying velocity. The complete existing C comparison agrees after independent checking of all five derivations and the report scope. A3252 confirms this exact recheck; the old A506 theorem is unchanged.

## 1. Statement and dependencies

Let J(y1,y2,y3)=(-y2,y1,0), 0<c<1 and omega be any fixed finite real number. Let U in C2(R3;R3), P in C1(R3) satisfy

    ((1-c)I+omega J)U+DU((cI-omega J)y+U)+grad P=0,
    div U=0, M=sup|U|<infinity.

Write B=(cI-omega J)y+U, G=DU, S=(G+G^T)/2, W=curl U and lambda=lambda_max(S). Matrix norms are operator norms unless marked F. Constants may depend on c, omega, the whole profile and the stated exterior bounds.

If lambda<=L outside a ball, where L>=0 is finite, then

    |W(y)|<=C(1+|y|)^((L-1)/c),
    ||G(y)||<=C(1+|y|)^max(0,(L-1)/c).                 (1)

More generally, if lambda<=1+gamma+epsilon(|y|) outside a ball, gamma>=-1, epsilon is bounded, nonnegative and measurable, and integral_R0^infinity epsilon(r)dr/r<infinity, then (1) holds with L-1 replaced by gamma.

Consequently each of the following gives G tending uniformly to zero, its Dini condition, and |G|+|W|=O((1+r)^-1):

- bounded U and limsup_(|y|->infinity)lambda(y)<1+c/2;
- uniform U->0 and lambda<=1+c/2+epsilon(|y|) outside a ball for one epsilon of the stated Dini class.

With vanishing distributional blow-down and1/3<c<1, also |G|=O((1+r)^(-1/c)). The tail limsup of lambda for any bounded profile therefore lies in {0} union [1+c/2,infinity]. For a decaying profile without derivative decay, for every allowed epsilon the set where lambda>1+c/2+epsilon(|y|) is unbounded. The critical bound is sufficient for decaying U and is not asserted for merely bounded U.

The analytic inputs after (1) are the two growth-to-decay conclusions of A498 and the downstream derivative conclusions of A3249. The fresh A498 reconstruction is here; its pending recheck does not change the existing A498 theorem. The entire105-line A506 source was freshly read and is captured.

## 2. Exterior time and vorticity growth

The C1 carrier B has at most linear growth. Gronwall bounds every finite-time trajectory inside a compact ball, and local existence and uniqueness continue it in both directions. On an exterior segment, r=|y| satisfies cr-M<=r'<=cr+M. Choose R1>max(1,R0,2M/c). Every point outside that sphere reaches it in a finite backward time: otherwise r(-t)<=r(0)exp(-ct/2) would contradict r(-t)>=R1. Strict radial increase makes the crossing unique.

For elapsed time s from the sphere to y, integrate r'/r=c+O(M/r). Since r'>=cr/2,

    |cs-log(r/R1)|<=integral_0^s M/r(t)dt
                       <=(2M/c)integral_R1^infinity dr/r^2<1.   (2)

The skew rotation vanishes in this calculation. All initial vorticity values on the crossing sphere have one finite bound.

The momentum equation makes grad P in C1, so curling it is justified. It gives W'=GW-W-omega JW along B. A nonzero W remains nonzero on each finite orbit segment by uniqueness of this linear ODE; identically zero segments satisfy every upper bound. Taking the scalar product with W yields

    d log|W|/ds=(W.SW)/|W|^2-1<=lambda-1.              (3)

Under the constant bound, integrate (3) and use (2). This gives

    |W(y)|<=sup_(|z|=R1)|W(z)| exp(|L-1|/c)(r/R1)^((L-1)/c).

The error factor is valid for either sign of L-1. For the Dini envelope the additional exponent is bounded by

    integral_0^s epsilon(r(t))dt<=(2/c)integral_R1^infinity epsilon(r)dr/r.

The same argument with exp(gamma s) gives the second growth claim. Measurability suffices for this integral comparison; no derivative or monotonicity of epsilon is used.

Since tr S=0, lambda>=0; if lambda<=L then every eigenvalue lies in [-2L,L], so ||S||<=2L. In the envelope case use the finite nonnegative bound L=1+gamma+sup epsilon. The skew part satisfies ((G-G^T)/2)v=(W cross v)/2, hence its norm is |W|/2. Therefore ||G||<=2L+|W|/2 proves (1), extended through the interior by compact continuity.

## 3. Exact composition and contrapositive

For the strict-limsup premise choose a finite L between that limsup and1+c/2. Equation(1) has exponent delta=max(0,(L-1)/c)<1/2. Thus G=o(sqrt r), and bounded U supplies precisely A498 case1. For the critical Dini-envelope premise set gamma=c/2. Equation(1) gives G=O(sqrt r); the separately assumed uniform U decay supplies precisely A498 case2. Neither application requires smallness of its finite growth constant.

Both give G->0. Apply A3249 with any c<kappa<1 to obtain |W|<=C r^(-kappa/c) and |G|<=C(r^(-kappa/c)log r+r^-1). This is O(r^-1) and is Dini after division by r and integration. The additional blow-down and c>1/3 supply A3249's natural gradient rate. No circular use of those conclusions occurs in (1).

If limsup lambda<1+c/2 the first argument gives lambda->0, proving the gap. If a decaying profile without derivative decay admitted any allowed epsilon with lambda<=1+c/2+epsilon(r) outside some ball, the second argument would contradict its assumed failure. Negating that exterior bound gives the stated unbounded exceptional set. This is a contrapositive about derivative decay, not nonexistence of a nonzero profile.

## 4. Scalar criterion and scope

The same momentum divergence identity gives -Delta P=tr(G^2). Orthogonality of symmetric and skew matrices gives

    ||S||_F^2=|W|^2/2-Delta P.

For eigenvalues lambda>=lambda2>=lambda3 with zero sum, lambda2^2+lambda3^2>=lambda^2/2, so lambda^2<=(2/3)||S||_F^2. Thus

    limsup_(|y|->infinity)(|W|^2/2-Delta P)<(3/2)(1+c/2)^2

implies the strict strain premise and derivative decay. This is a sufficient criterion. Neither its scalar constant nor1+c/2 is claimed to be sharp for Euler profiles. The equality endpoint with a Dini envelope retains uniform velocity decay. No global vorticity-flow completeness, pressure normalization, finite energy, helicity sign or bound uniform in omega has entered.

No new theorem direction, numerical diagnostic or formal verification is used. The physical singular-set conclusions adjacent to this theorem in the report are not part of this proof.
