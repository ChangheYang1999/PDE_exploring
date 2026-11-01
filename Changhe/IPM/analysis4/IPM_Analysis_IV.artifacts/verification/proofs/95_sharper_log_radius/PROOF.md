# A sharper exterior radius for geometrically bounded log coefficients

Status: PROVED after the theory part's independent review at2026-10-31T07:27Z and verifier closure V173. The all-order hypotheses for the computed rational sequence remain open.

## Statement

Let delta=a/b be reduced in(0,1), q_0=2b/gcd(a,2), and kappa=1/q_0. Use the canonical stationary log recursion from nonzero finite real S1 leading data. Suppose its plain density and stream coefficient sums satisfy

    M_n,N_n <= C A^n, n>=1,

for some C,A>0. For every R>=e such that

    q_R=A R^(-delta)(log R)^kappa<1,                (1)

the density, stream and a common potential converge absolutely and uniformly in their leading weights on r>=R. Every fixed appropriately weighted Cartesian derivative also converges there, and the sums are real analytic and solve the stationary IPM equation on r>R.

Thus the exponent2/q_0 in the sufficient radius condition of topic41 can be replaced by1/q_0. The former condition remains valid; it was a convenient overestimate rather than a necessary loss.

In particular, if delta=2/3, f_1=sin(theta), and the all-order plain inequality N_n<=M_n/4 holds, then topic88 supplies a common geometric base A=6. Under precisely that unproved all-order hypothesis, the conclusion holds on r>=27. This improves the earlier conditional radius64. It does not establish the hypothesis for the actual sequence.

## Proof of the radius improvement

The degree and common-potential reconstruction bounds in topics17 and41 give, for all sufficiently large n,

    deg_t F_n, deg_t G_n, deg_t C_n <= kappa n,
    ||F_n||_*, ||G_n||_*, ||C_n||_* <= C' A^n.

The Fourier frequencies are O(n). Potential reconstruction may add exceptional logarithms at finitely many early orders; those orders are treated individually below. Since t=log r>=1, the absolute angular norm of any of these polynomials is at most C' A^n t^(kappa n). After factoring its leading radial growth, the order-n term is bounded by

    C' A^n exp(-delta(n-1)t)t^(kappa n).           (2)

For n>=2 this scalar expression is nonincreasing in t>=1. Indeed its logarithmic derivative is

    -delta(n-1)+kappa n/t
       <=-delta(n-1)+kappa n<=0,

because delta/kappa=delta q_0 is an even positive integer and is therefore at least2, while n<=2(n-1). Consequently the supremum of(2) over r>=R occurs at r=R. It is

    C' A (log R)^kappa q_R^(n-1).                 (3)

Condition(1) sums this geometric majorant. For every N above the finite exceptional orders, its tail is at most

    C' A (log R)^kappa q_R^N/(1-q_R).

Each fixed weighted Cartesian derivative multiplies the coefficient norm by at most a fixed polynomial in n and does not increase log degree. The same argument therefore gives a summable polynomial times q_R^(n-1). Every exceptional early term with n>=2 is a fixed log polynomial times r^(-delta(n-1)), whose weighted supremum on r>=R is finite. At n=1 the leading homogeneous potential, stream and density have no log terms: their positive radial degrees and the exact first-order potential construction avoid the relevant resonances. Thus no exceptional leading logarithm spoils the chosen weights.

The potential identities and stationary equation now pass to the limit by the already verified argument of topic41. A strict margin in(1), together with the O(n) Fourier cutoff, also gives convergence in small complex neighborhoods of each real point in the exterior, proving real analyticity. No global interior extension is asserted.

## Exact conditional radius27

At delta2/3, q_0=3 and A=6, the cube of q_27 is

    q_27^3=216 log(27)/27^2=(8/9)log3.

The elementary exponential series gives

    exp(9/8) > sum_(j=0)^4 (9/8)^j/j!
               =300993/98304 > 3.

Hence log3<9/8, so q_27<1. Topic88 gives M_n<=6^(n-1)/n and N_n<=M_n/4 under its all-order hypothesis, which meet the required common-base bound. This proves the conditional assertion with no rounded constants.

## Dependencies and limitations

The only new step is retaining t^(n/q_0) and maximizing each complete radial term, instead of replacing n by2(n-1) before summation. The log degree estimates, coefficient reconstruction, PDE identities and derivative calculus are inherited from topics17,41,88. The argument does not turn a finite numerical prefix into an all-order estimate.

## The conditional unit-ratio radius

At delta=2/3 with f_1=sin(theta), the all-order assumption N_n<=M_n gives A=24 in topic88. Radius300 is sufficient. Indeed exp(3)>sum_(j=0)^5 3^j/j!=92/5, so exp(6)>(92/5)^2=8464/25>300 and log300<6. Therefore q_300^3=24^3 log300/300^2<24^3*6/300^2=576/625<1. This is a rational certificate for the radius, conditional on the unproved all-order unit-ratio hypothesis.
