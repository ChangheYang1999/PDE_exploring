# Completeness, slow escape and recurrence of the frozen vorticity flow

## Statement

Assume U in C^2(R^3), P in C^1(R^3) solve the full divergence-free rotating
profile equation, with c>0, omega real, and U=o(|y|) uniformly. Set
B=cy-omega Jy+U, Omega=curl U and b=1+c. Then the autonomous Omega flow
psi_t is complete. For every compact K and epsilon>0,

    sup_(x in K)|psi_t x| <= C_(K,epsilon)(1+|t|)^((c+epsilon)/b).

For bounded U, epsilon=0 is allowed. The exact global conjugacy is

    Phi_s psi_t = psi_(exp(bs)t) Phi_s.

If additionally c<1/2, psi_t is conservative with respect to Lebesgue
measure: for each fixed tau>0 and bounded measurable A, almost every point
of A returns to A at infinitely many positive and negative integer multiples
of tau. Almost every point is topologically recurrent in both directions.

## Global continuation before using global conjugacy

Uniform sublinearity makes B globally at most linear, so its C^1 flow Phi
is complete. The radial equation has no rotation contribution. For all s>=0,

    |Phi_s z| <= exp((c+epsilon)s)(|z|+C_epsilon/(c+epsilon)).

For bounded U, use epsilon=0 and C_epsilon=sup|U|. An outward-pointing large
sphere traps all negative-time B orbits from a compact K in one compact ball
D. On a slightly larger ball Omega and DOmega are bounded, so there is a
common delta>0 such that the local Omega flow from all points of D exists
for |t|<=delta and stays inside that larger ball. This uses only ordinary
local existence and a speed bound, not global completeness of Omega.

For s>=0 define, whenever |t|<=delta exp(bs),

    z_s(t)=Phi_s(psi_(exp(-bs)t)(Phi_-s x)).

The inner flow is the short local flow just constructed. The Cauchy identity
D Phi_s Omega=exp(bs) Omega composed with Phi_s gives z_s'(t)=Omega(z_s(t))
and z_s(0)=x. Uniqueness makes these solutions consistent as s varies. Their
time intervals exhaust the real line, proving completeness. The conjugacy
then follows for all s,t by uniqueness.

Choose s=b^-1 log(1+|t|/delta). The inner point stays in a fixed ball, so the
radial bound above gives precisely the stated polynomial growth. All constants
are uniform for x in K. Neither the norm of DOmega at infinity nor a complete
B-orbit bound is required.

## Conservativity by volume packing

Choose epsilon>0 with d=(c+epsilon)/b<1/3, possible exactly when c<1/2.
Since div Omega=0, the complete flow preserves Lebesgue measure. Fix tau>0
and bounded measurable A. Let W be the subset of points in A having no
strictly future return to A under psi_tau. The sets psi_(n tau)W, n>=0, are
pairwise disjoint. They all lie, for n<=N, inside a ball of radius
C(1+N tau)^d. Consequently

    (N+1)|W| <= C'(1+N tau)^(3d).

Division by N+1 gives |W|=0. Any point of A with only finitely many future
returns has a last return in W. Such points lie in a countable union of
inverse images of W and form a null set. The same proof for the inverse
flow gives infinitely many past returns. For topological recurrence use
tau=1 and a countable basis of rational balls, discard the union of all
exceptional null sets, then take successively smaller balls around each
remaining point and strictly increasing return integers.

## Scope

These are LIT12 and LIT13. No finite total invariant volume or boundedness
of individual Omega orbits is inferred. The exceptional null set may depend
on a specified tau. Recurrence is for the frozen Omega flow, not for B.
The proof does not imply that the compact set of bounded B-orbits is
Omega-invariant. Its conjugacy has a positive exponent under positive B time.
No pressure normalization, integrability or symmetry is used.

Audit recorded: 2026-11-02T18:46:07Z
