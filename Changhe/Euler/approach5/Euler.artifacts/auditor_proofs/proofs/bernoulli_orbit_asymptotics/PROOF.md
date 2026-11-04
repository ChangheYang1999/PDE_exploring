# Almost-everywhere Bernoulli asymptotics along the carrier

## Statement and notation

Let 2/5 <= c < 1/2, omega be any finite real number, J(y1,y2,y3)=(-y2,y1,0), A=cI-omega J, and a=1-2c>0. Let U in C2(R3;R3), P in C1(R3) satisfy

    div U=0,
    (1-c)U + (Ay+U).grad U + omega JU + grad P=0,
    U(y) -> 0 uniformly as |y| -> infinity.

Write B=Ay+U, q=|U|^2/2, beta=5-2/c in [0,1). Let Phi_t be the complete B flow. Choose the single canonical pressure representative P0 established in A031/A277, and set H0=P0+q+Ay.U=P0-q+U.B.

For every bounded measurable Q there are finite constants C_Q, allowed to depend on U,c,omega,Q, such that:

(A) The future integral of |U.B|(Phi_t y) converges for almost every y, and

    H0(y)=a integral_0^infinity (U.B)(Phi_t y) dt,
    ||sup_(t>=T)|H0(Phi_t y)||_L2(Q) <= C_Q exp(-aT).

The shifted integral identity holds for all T>=0 on one full-measure set. In particular H0(Phi_t y) tends to zero through all real times for almost every y.

(B) There is a measurable K in L2_loc(R3), defined on a full-measure set G invariant under every Phi_s, s real, such that

    K(y)=lim_(t->infinity) exp(at) H0(Phi_t y),
    K(Phi_s y)=exp(-as) K(y),
    K(y)=H0(y)+a integral_0^infinity exp(at)(P0-q)(Phi_t y) dt.

The last integral is absolutely convergent on G. For all T>=0,

    ||sup_(t>=T)|exp(at)H0(Phi_t y)-K(y)||_L2(Q)
        <= C_Q exp(-cT).

For almost every y, |H0(Phi_t y)| <= C_y exp(-at) for all t>=0. For every 0<delta<c, on one common full-measure subset,

    H0(Phi_t y)=exp(-at)K(y)+O_(y,delta)(exp(-(a+delta)t)).

The coefficient is not asserted continuous or locally bounded. No point on a singular invariant support is automatically in G. These are necessary conditions, not a nonexistence theorem.

## Dependencies

A031 supplies canonical pressure and removal of harmonic ambiguity. A040 supplies E(R)=integral_B_R |U|^2 <= C R^beta for R>=1. A277, proved independently in the team records, supplies the SAME representative P0 with

    integral_B_R |P0|^2 <= C R^beta + C R^(2beta-3),
    integral_B_R H0^2 <= C R^(beta+2),
    ||H0 composed Phi_t||_L2(Q) <= C_Q exp(-at).

No derivative decay, Dini condition, finite total energy, symmetry, invariant measure, helicity or basin premise is present. Ordinary integral inequalities below are applied to measurable nonnegative functions; their finite-interval versions precede all infinite-time limits.

## Completeness, Jacobian and derivative estimates

U is bounded, say by M. Linear growth of B and local C1 regularity imply complete flow in both time directions. Because the skew matrix contributes no radial growth, for t>=0,

    |Phi_t y| <= exp(ct)(|y|+M/c).

The exact divergence div B=3c gives det D Phi_t=exp(3ct). For bounded Q choose R_Q>=1 with Phi_t Q contained in B_(R_Q exp(ct)). On this ball |B|<=C_Q exp(ct). Therefore

    integral_Q |(U.B)(Phi_t y)|^2 dy
      <= C_Q exp(-ct) E(R_Q exp(ct))
      <= C_Q exp(c(beta-1)t)
      = C_Q exp(-2at).

Also q^2<=M^2 |U|^2/4. Since 2beta-3<=beta, the canonical pressure estimate implies

    integral_B_R |P0-q|^2 <= C R^beta, R>=1.

Change variables under Phi_t again:

    ||(P0-q) composed Phi_t||_L2(Q)
       <= C_Q exp(c(beta-3)t/2)
       = C_Q exp(-(1-c)t).

Every exponent follows directly from beta=5-2/c; neither estimate restricts omega.

The exact reduced Lamb identity gives B H0=-a U.B. Since U.B=H0-(P0-q), also

    (B+a)H0=a(P0-q).

These classical scalar identities hold along every orbit with the stated regularity.

## Proof of (A)

Put g_t(y)=(U.B)(Phi_t y). Minkowski on [T,S] gives

    ||integral_T^S |g_t| dt||_L2(Q)
       <= integral_T^S ||g_t||_L2(Q) dt
       <= (C_Q/a) exp(-aT).

Let S increase to infinity. Monotone convergence of the squares proves the same bound for the infinite nonnegative integral. A countable ball covering gives absolute convergence from zero for almost every y in R3. At such points the identity

    H0(Phi_t y)=H0(y)-a integral_0^t g_s(y) ds

has a finite limit L(y) through all real t. The A277 norm estimate and Fatou along integer times give integral_Q |L|^2=0. Thus L=0 almost everywhere. Taking the limit proves the future integral, and subtracting any finite initial segment proves its shifted version simultaneously for every T. There is no exceptional set chosen separately for different real T.

For t>=T its absolute value is at most a integral_T^infinity |g_s| ds. Taking the supremum and the preceding L2 bound proves (A). The supremum is measurable since the orbit function is continuous and rational times suffice.

For completeness, (A) alone implies every pointwise rate delta<a: Chebyshev makes the measure of {sup_(t>=n)|H0(Phi_t)|>exp(-delta n)} at most C_Q exp(-2(a-delta)n). Borel-Cantelli, continuity over the finite initial interval and a countable ball covering prove the claim. Part (B) upgrades this to the endpoint a.

## Proof of (B), including the common invariant domain

Differentiate exactly:

    d/dt[exp(at)H0(Phi_t y)]
       = a exp(at)(P0-q)(Phi_t y).

Its local L2 norm is at most C_Q exp(-ct), since (1-c)-a=c. As before, finite-interval Minkowski followed by monotone convergence gives

    ||integral_T^infinity exp(at)|(P0-q)(Phi_t y)| dt||_L2(Q)
       <= (C_Q/c) exp(-cT).

Define G to be ALL points where this nonnegative integral from zero is finite. It is measurable and full measure. The integrated derivative identity defines K on G and proves the claimed limit and integral formula. The same bound at T=0 shows K-H0 in L2(Q), hence K in L2_loc. Set K=0 on the null complement if a representative on all R3 is desired.

The tail of the integral controls |exp(at)H0(Phi_t y)-K(y)| uniformly for t>=T and gives the stated supremum L2 estimate. Its measurability follows from rational times and continuity of the finite-time function.

For y in G and ANY real s, substitution r=t+s gives

    integral_0^infinity exp(at)|(P0-q)(Phi_t(Phi_s y))| dt
      = exp(-as) integral_s^infinity exp(ar)|(P0-q)(Phi_r y)| dr.

The added or removed finite orbit segment is integrable by continuity and completeness. The right side is finite. Thus Phi_s G is contained in G for every real s; applying -s gives equality. This is a pointwise argument for all s, not an intersection of uncountably many full-measure sets. Shifting the already existing limit yields K(Phi_s y)=exp(-as)K(y).

The supremum bound at T=0 implies exp(at)H0(Phi_t y) is bounded for almost every y, proving the endpoint a rate. For 0<delta<c, Chebyshev and Borel-Cantelli applied to the tail bound at integer n give

    sup_(t>=n)|exp(at)H0(Phi_t y)-K(y)| <= exp(-delta n)

for all sufficiently large n, almost everywhere locally. For real t choose n<=t<n+1; the extra factor is at most exp(delta). A countable ball covering and a countable sequence delta_j increasing to c produce a common full-measure subset for every delta<c. Multiplication by exp(-at) gives the displayed error rate. No endpoint error rate c is asserted.

If desired the covariance implies B K=-a K distributionally: for compact smooth phi, differentiate the identity after changing variables with Jacobian exp(3cs). Local L2 integrability justifies differentiation of the transported test. The result is integral K div(B phi)=a integral K phi. This is not classical differentiability of K.

## Why compact backward orbits do not force K=0

For the negative flow, the radial inequality gives

    |Phi_-t y| <= exp(-ct)|y| + M/c, t>=0.

Thus each negative orbit lies in a compact ball. If K(y) is nonzero and y in G, covariance gives |K(Phi_-t y)|=exp(at)|K(y)|. Local L2 does not bound values on this orbit. Its surrounding volume contracts at rate exp(-3ct), so this growth is not a contradiction to local integrability. Uniform convergence or local boundedness of K has not been proved. The full-measure domain can miss an entire singular SRB support. No transfer to such a support, no helicity sign and no nonexistence conclusion follows.

## Independent counterexample to a mean-only argument

This construction concerns a scalar, not an Euler profile. Fix the same c,beta and B0=Ay. Choose smooth 0<=chi<=1 supported in (-1,1), chi(0)=1, put r_n=4^n and w_n=r_n^beta/16, and define

    F(y)=sum_(n>=1) chi((|y|-r_n)/w_n).

The radial supports are disjoint, avoid zero, and are locally finite; F is bounded smooth on R3. Each shell has volume at most C r_n^2 w_n. A shell meeting B_R has r_n<=2R. A geometric sum gives integral_B_R F^2<=C R^(beta+2) for R>=1. Exact radial growth and Jacobian for B0 then give

    integral_Q |F(exp(At)y)|^2 <= C_Q exp(c(beta-1)t)
                              = C_Q exp(-2at).

For every y!=0, at t_n=c^-1 log(r_n/|y|), eventually positive, F(exp(At_n)y)=1. At the intervening radii 2r_n it equals zero. Thus no nonzero initial point has a forward scalar limit. The actual U=0 Euler profile has canonical H0=0, not F. The construction refutes only inference from the mean estimate alone; the derivative estimate in (A) excludes it.

## Audit scope

LIT61 and LIT62 are confirmed at the stated decaying C2 scope. The counterexample is confirmed as a scalar inference test. No numerical calculation, external solver, formalization or build is used. A focused configured-model challenge has been requested through shared files; no unreceived response is counted as evidence.
