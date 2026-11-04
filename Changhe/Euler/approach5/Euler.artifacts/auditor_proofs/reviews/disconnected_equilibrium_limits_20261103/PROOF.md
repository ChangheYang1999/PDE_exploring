# Totally disconnected equilibrium subsets of bounded vortex limits

Status: CONFIRMED as A640 after a complete independent proof and postread.

## 1. Exact statement

Let X be a C1 vector field on a C2 surface Sigma. Let y:[0,infinity) to Sigma be a nonstationary forward-complete orbit with compact omega-limit set K. Put E=K intersect {X=0}. Assume that at every q in E the linearization DX(q) has a positive real eigenvalue. Assume also that every regular C1 equilibrium arc contained in E has a positive transverse eigenvalue. Then E is totally disconnected. In the application below the trace of DX on E is the same positive constant, so the second assumption follows from the first eigenvalue being zero along an arc.

No assertion of isolation, finiteness, absence of a Cantor subset, or convergence of y follows from this statement alone.

The Euler application uses precisely Section1 of in the team records: 2/5<c<1/2, all real omega, C2/C1 helicity-free local profile, a bounded nonstationary vortical half-line in a regular H level, its compact limit K, and constant rho<=-a, a=1-2c. The induced C1 surface field X agrees with B on K and on the late orbit. At every equilibrium its level eigenvalues are lambda<=0<eta and its trace is d=3c-rho>0. No far-field derivative or symmetry assumption enters.

## 2. Exclusion of equilibrium arcs

For completeness, write a regular C1 equilibrium arc in a surface chart as y=f(s). Let the original C1 field be (P,Q). With r=y-f(s), the fundamental theorem of calculus in the original y variable gives

    s'=r A(s,r),  r'=r C(s,r),
    A=integral_0^1 P_y(s,f(s)+u r) du,
    C=integral_0^1 [Q_y-f'(s)P_y](s,f(s)+u r) du.

Both coefficients are continuous. C(s,0) is the transverse eigenvalue. On a small closed rectangle around an interior point of the arc choose C>=b>0 and |A|<=M. While a negative-time orbit stays inside,

    |r(-t)|<=|r(0)|exp(-bt),
    |s(-t)-s(0)|<=M|r(0)|/b.

A sufficiently narrow inner rectangle therefore has its entire negative orbit trapped in the larger rectangle. Compact containment and uniqueness for the ORIGINAL C1 field supply continuation for all negative times. This does not require the graph-transformed field to be C1.

If the given nonstationary orbit accumulates at the middle point, fix an earlier orbit point and choose the larger rectangle to omit it. That point is not an equilibrium by uniqueness. A sufficiently late visit to the inner rectangle traps its whole earlier orbit in the larger rectangle, a contradiction. Thus E contains no regular C1 arc. A nonconstant C1 curve contains a regular subarc, since at least one component derivative is nonzero at some point.

## 3. Local clopen neighborhoods

Fix q in E. Since DX(q) has a positive eigenvalue, it is nonzero. In any local trivialization of the tangent bundle some scalar component of X has nonzero differential at q. The implicit function theorem makes its zero set a regular C1 graph on a small chart containing q. Every zero of X in that chart, hence E in the chart, lies on that graph.

Straighten this graph to r=0 and choose an outer rectangle with compact closure in the chart. The projection onto s of E on a shorter closed subrectangle is compact. It contains no interval: such an interval would be a regular equilibrium arc in E, contrary to Section2. Consequently its complement is dense in the s interval.

Choose s_-<s(q)<s_+ arbitrarily close to s(q), both outside this projection, and choose arbitrarily small positive upper and lower r heights while keeping the closed rectangle in the shorter chart. Its horizontal boundary misses E because r is nonzero; its vertical boundary misses E by the choice of s_-,s_+. Thus its intersection with E is both relatively open and relatively closed in E. These sets form an arbitrarily small clopen neighborhood basis at q.

Given distinct q_1,q_2 in E, choose such a neighborhood of q_1 excluding q_2. Its relative complement separates any subset containing both points. Therefore no connected subset of E contains two distinct points. E is totally disconnected.

In the Euler application an equilibrium arc has a zero tangent eigenvalue. Its other eigenvalue is the trace d>0. The assumptions of Sections1-3 follow, including at flat equilibria and at rho=-kappa, kappa=1+c.

## 4. What can and cannot be combined with surface collapse

A629 proves: if all equilibria of K are isolated zeros of the SURFACE field X and are hyperbolic saddles or have eigenvalues 0,eta>0, then the external orbit converges to one equilibrium. Compactness of E makes it finite if each point is isolated in the surface zero set: an infinite E would have an accumulation point in E, contradicting its isolation.

Total disconnectedness alone supplies none of this isolation. Failure of the collapse criterion requires a nonisolated surface zero in E, which can occur either through an infinite E or through surface zeros outside K accumulating on a point of a finite E. In particular, saying that the residual case necessarily has infinitely many equilibria IN K is unsupported.

At a nonisolated surface zero, DX is singular by the inverse function theorem, so lambda=0. At rho!=-kappa, the established nonflat equilibrium classification forces nonflat points to be hyperbolic. Thus any nonisolated zero at these rates is flat. At rho=-kappa, a nonflat equilibrium can have level eigenvalues 0,d. A631 excludes it as the actual singleton limit of the given vortex half-line. It does not exclude it from a nonsingleton K.

For an actual hyperbolic endpoint, A630 proves lambda>=-kappa and the power law along the stable curve. For a semihyperbolic endpoint lambda=0 the inequality is automatic, but the expression 1-kappa/lambda is undefined. The smooth integer order is the order along the stable curve, not necessarily the first ambient vorticity jet. No result here excludes the surviving global heteroclinic connection or constructs a global Euler profile.

## 5. Dependencies and verification

The arc proof and all endpoint inputs were independently reconstructed in A628-A633. The new argument is the elementary implicit-function and clopen-neighborhood proof in Section3. The complete saved second review in the team records was read and compared. It agrees with the independent reconstruction and identifies the same exceptional-rate and surface-isolation limitations. Its attempted inner model call failed before a response and is not counted as a model consultation. Existing configured model team agents remain the collaboration channel.

No computation or formal build was needed. Formal sources are absent; in the team records records that fact. Verification evidence contains relative source paths and hashes.
