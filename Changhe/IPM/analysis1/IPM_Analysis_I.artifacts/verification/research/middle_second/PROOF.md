# Independent middle-cell reconstruction by density moment ODEs

2026-10-20. Written before implementation. This is an enclosure theorem, not a completed numerical certificate. The application is OPEN.

## Statement and scope

Let the exact normalized modal trial be the one in ../middle_residual/PROOF.md and ../inner_majorant/PROOF.md. In a middle spline span [a,b] in t=log(r), write

rho(r,theta)=r^3 sum_(j=0)^260 H_j(t) sin((2j+1)theta),

where each H_j is a polynomial of degree at most seven on the span. Set H_261=0. An accepted archive supplies outward dyadic intervals for every coefficient about c=(a+b)/2 and for the canonical density moments i_n(a), j_n(b), n=1,...,261. The archive must have a complete independent input audit, source hashes and exact span endpoints. Treating these intervals as point estimates is forbidden.

For a closed child cell [l,u] contained in [a,b], put t_c=(l+u)/2 and h=(u-l)/2. The construction below gives a rigorous upper bound for the angular sine coefficient sum W of

epsilon=(c_l X+U[rho]) dot grad rho-rho,

on every point of the child cell and all angles. Here c_l=1/k, and U is the canonical full-plane inverse of the same exact density. The constants k,L and the scalar normalization theorem are pinned dependencies. Neither the child cell nor the middle region includes the missing inner or exterior disk. This theorem concerns a zeroth residual bound only.

## Center moments by a finite density integral

Let m=2n. The canonical moments obey

i_n'=-(m+4)i_n+H_(n-1),
j_n'=(m-4)j_n-H_n.

These identities and the physical Green identities are independently derived by integration by parts in ../inner_cells/PROOF.md. They apply to every middle span, with the actual canonical continuation on both sides.

Writing d=t_c-c, h_l=t_c-a and h_r=b-t_c gives

i_n(t_c)=exp(-(m+4)h_l)i_n(a)
 +integral_0^h_l exp(-(m+4)v)H_(n-1)(t_c-v)dv,

j_n(t_c)=exp((4-m)h_r)j_n(b)
 +integral_0^h_r exp((4-m)v)H_n(t_c+v)dv.

For the first identity, split the lower defining integral at a and substitute s=t_c-v in its remaining part. For the second, split the upper defining integral at b and substitute s=t_c+v. Both formulas are stable finite-interval integrals. The rate 4-m can vanish at n=2, which requires an explicit zero-rate case.

Expand each shifted H(t_c+sigma v) by the binomial theorem using exact rational shifts and outward interval coefficient arithmetic. For a resulting polynomial P(v)=sum_(j=0)^d p_j v^j, d<=7, and exact lambda, define

I(P,H,lambda)=integral_0^H exp(lambda v)P(v)dv.

If lambda=0, I=sum_j p_j H^(j+1)/(j+1). If lambda is nonzero, the polynomial

Q_l=sum_(j=l)^d (-1)^(j-l) j! p_j/[l! lambda^(j-l+1)]

satisfies Q'+lambda Q=P, by cancellation of adjacent terms. Hence

I=exp(lambda H)Q(H)-Q(0).

A second, optional evaluation formula integrates the exponential Taylor polynomial through degreeK term by term. The production implementation uses the complete antiderivative formula at every nonzero rate, at160decimal digits, and records center-moment interval widths. The Taylor formula below is used only as an independent contract oracle, not as a production branch. For each monomial p_j v^j, the omitted series is bounded by

|p_j| H^(j+1) |lambda H|^(K+1)
 /[(K+1)!(K+j+2)(1-|lambda H|/(K+2))],

provided |lambda H|/(K+2)<1. The ratio of successive absolute terms after the first omitted term is at most |lambda H|/(K+2). Summing over j proves the remainder bound. This method differs from the primary moment evaluator's integrated Phi recurrence. Every branch must use interval arithmetic for exp and for the remainder, with outward conversion of rational inputs.

## Taylor models from density ODEs

Shift the polynomial coefficients to t_c exactly in rational arithmetic with outward interval coefficient operations. On v=(t-t_c)/h in [-1,1], the resulting degree-seven H models have zero analytic remainder. Let Q>=7 be the chosen Taylor degree, and pad polynomial models with zero coefficients to degree Q.

For y'=lambda y+sigma G, where G=sum_(j=0)^Q g_j v^j+e_G and |e_G|<=r_G, set ell=lambda h. A closed formula for the Taylor coefficients is

p_q=y_0 ell^q/q! + sigma h sum_(j=0)^(q-1) g_j j! ell^(q-1-j)/q!.

The sum is zero when q=0. Substitution verifies p_(q+1)=(ell p_q+sigma h g_q)/(q+1). With |sigma|<=1, the complete remainder is bounded by

exp(|ell|)(|ell p_Q+sigma h g_Q|/(Q+1)+h r_G).

Indeed the polynomial error solves a scalar ODE with zero center error and forcing (ell p_Q+sigma h g_Q)v^Q+sigma h e_G. Variation of constants bounds its integral on either side of zero. Interval center and coefficient uncertainties are choices among the enclosed exact coefficients, not omitted errors. The same proof therefore holds for interval coefficients. For density moments the largest |lambda| is 526.

Build i_n and j_n by this closed formula, independently of the primary recurrence for the physical moments A_n and B_n. Put H_avg=(H_(n-1)+H_n)/2. The exact Green formulas give

A_n/r^2=r^2(H_avg-m i_n),
B_n/r^2=r^2(m j_n-H_avg),

p_n=-(A_n+B_n)/(2r^2),
s_n=(B_n-A_n)/(2r^2).

The coefficients p_n and s_n are those of U_r/r and U_theta/r. Model r^2=exp(2t) by its Taylor polynomial and complete exponential remainder before performing either product. Retain all intermediate product truncation errors. This is a different intermediate representation from the primary physical Green ODEs, whose largest rate is 522.

Similarly construct the exponential-polynomial models

rho_j=exp(3t)H_j,
D_j=exp(3t)(3H_j+H_j'),
Theta_j=(2j+1)rho_j,
Lin_j=c_l D_j-rho_j.

The finite product theorem and exponential remainder theorem in ../outer_cells/PROOF.md apply for either sign of t_c. No exact cubic subtraction is needed because the middle region is bounded away from r=0.

## Angular products and bounds

The exact residual is

sum_j Lin_j sin((2j+1)theta)
 +(sum_n p_n cos(2n theta))(sum_j D_j sin((2j+1)theta))
 +(sum_n s_n sin(2n theta))(sum_j Theta_j cos((2j+1)theta)).

The complete product has all odd frequencies from 1 through 1043. Reconstruct it using compressed angular indices and exact integer interval convolution as proved in ../outer_cells/PROOF.md. An outward dyadic quantization of every interval coefficient to denominator 2^P gives integer midpoints and nonnegative radii. For products, the exact radius formula is |m_1|r_2+r_1|m_2|+r_1r_2, summed by integer convolution. This includes quantization errors and cannot underflow. Keep degrees through 2Q; bound every degree above Q by its absolute coefficient sum.

Transform each retained degree-Q polynomial on [-1,1] to Bernstein coefficients on [0,1] using the exact rational matrix. Its largest absolute Bernstein coefficient bounds the polynomial at every point. Summing this bound over all 522 sine modes, then adding the discarded-degree and nonpolynomial product remainders, bounds W. The absolute coefficient sum in each elementary sine-cosine product formula is one, which proves the angular model remainder estimate used here.

The primary cell evaluator can return17retained coefficients per mode forQ=16, but the full driver disables this output. A complete coefficient comparison must regenerate the primary cell from the same pinned archive, verify the previously saved scalar fields, and then compare all522*17=8874coefficient intervals. This comparison is a consistency check on the retained polynomial, not a proof of the new implementation. The degree-17 through degree-32 bounds and all remainders must be justified by their own exact construction even if not cross-compared. Different valid W majorants need not overlap. Publish the maximum of both independently valid upper bounds.

With u=r/L and m_w=u^3(1+u^2)^((k-3)/2), m_w increases because its logarithmic derivative is (3+k u^2)/(1+u^2)>0. Therefore divide a cell's W bound by m_w at its left endpoint. For delta>=0, multiply by (1+u_right)^delta for the weighted supremum. Orthogonality of the sine modes and integration in r give the cell bound

||epsilon/m_w||_(L2(dX/(1+u^2)))^2
 <=pi M^2 L^2[log(1+u_right^2)-log(1+u_left^2)]/2,

where M bounds W/m_w on the cell. This is an upper bound on the full angular integral because sum_j epsilon_j^2<=W^2. Every weight and integral is recomputed by interval arithmetic. Exact adjacent cells have disjoint interiors, so their squared bounds may be summed. A global middle conclusion requires the entire exact partition and all source/output audits, not selected cells.

## Remaining application obligations

No code or numerical result for this construction is accepted yet. Required steps are source review with actual Opus 5.5, exact polynomial/integral contract tests, independent center-moment comparisons, selected whole-cell coefficient comparisons, source-pinned complete execution, and a separate output audit. The previously accepted canonical archive is a shared dependency and must be identified as such. The full existing Arb middle pass remains independently useful and must not be invalidated or modified by this additional work.

## Source checks in progress,2026-10-20

The shared canonical archive is a common dependency. Agreement between the two cell methods cannot validate it; its independent source and interval audit remains required. Production arithmetic uses mpmath1.3.0 withiv.dps160, python-flint0.9.0 for exact integer polynomial products, and dyadic quantizationPint512. Primary regeneration uses Arb384 and the unchanged pinned physical Green implementation.

The independently certified point data in ../residual_samples/PROOF.md reconstruct all canonical moments from the original density using complete exponential-series integration, with a direct sine-product calculation and a separately checked Laurent product plus65directivpolar substitutions. The second-cell run must compare these point enclosures with its middle-cell bounds at all13specified cells. This supplements cell-model coefficient comparisons; it does not replace full-interval remainders or exhaustive covering.
