# Finite transverse polynomial velocities cannot form a smooth outgoing endpoint

Status: CONFIRMED by the complete independent proof,197 exact manufactured controls and two written actual Opus5.5 reviews. This is a local ansatz exclusion, not a full beta2 nonexistence theorem.

## 1. Abstract local statement

Use oriented orthonormal Cartesian coordinates (u,v) centered at p, with u increasing along the outward tangent to an equilibrium arc. Let W=(W_u,W_v) be C-infinity on a full rectangle about0, with constant divergence D>0. Assume:

1. W(0)=0, partial_v W_v(0)=D, and the normal nullcline v=k(u) is smooth. It contains an equilibrium half-arc for -epsilon<u<=0, so W_u(u,k(u))=0 there. On0<u<epsilon the reduced component W_u(u,k(u)) is strictly positive. Thus0 is an immediate outgoing endpoint, rather than a point with additional zeros accumulating beyond it.
2. For every sufficiently small u>0 there is a nonempty open interval of v values on which curl W(u,v)=0.
3. On the full rectangle the two components are polynomials of uniformly finite degree in the physical Cartesian normal coordinate v:

       W_i(u,v)=sum_(j=0)^N a_ij(u) v^j,   a_ij in C-infinity.

These three conditions are incompatible. No global inverse, parity or far-field condition is needed for this lemma.

The polynomial condition concerns the actual vector field in an orthonormal physical chart. It is not a condition after an arbitrary smooth straightening of the dynamics. It does not describe a general finite angular spectral representation, and it is not an objection to polynomial approximation at finitely many points.

## 2. From a transverse interval to a harmonic polynomial

For each fixed u>0, curl W=partial_u W_v-partial_v W_u is a polynomial in v. Hypothesis2 gives an open interval on which it vanishes. The polynomial identity theorem therefore gives curl W(u,v)=0 for every v in the rectangle. Hence W has constant divergence and zero curl on the positive half-rectangle. The exact planar identities

    Delta W_u=partial_u divW-partial_v curlW,
    Delta W_v=partial_v divW+partial_u curlW

show that both components are harmonic there.

Comparing powers of v gives the finite triangular system

    a_ij''(u)+(j+2)(j+1)a_i,j+2(u)=0,
    a_i,N+1=a_i,N+2=0.                              (1)

The top two coefficients have second derivative0 and are affine in u. Descending in j, the right side of(1) is a polynomial already determined at higher indices, so twice integrating shows that a_ij is a polynomial in u. More precisely deg a_ij<=N-j+1: this is immediate for j=N,N-1 and the induction adds two degrees from j+2 to j. All constants of integration are finite because the coefficients are smooth up to u=0. Thus W on u>0 equals a single vector polynomial P(u,v), of total degree at most N+1, which extends to a neighborhood on both sides of0.

This extension is a polynomial of the positive-half field only. It is not assumed equal to W for u<0. Since W and P agree on u>0 and W is smooth on the full rectangle, all their derivatives at0 agree. In particular P(0)=0 and partial_v P_v(0)=D.

## 3. Analytic continuation of the reduced zero equation

By the analytic implicit-function theorem, P_v=0 has a unique real analytic graph v=k_P(u) near0. The ordinary smooth implicit-function theorem gives the original normal graph k(u). On u>0 both normal equations coincide and uniqueness gives k=k_P. Consequently

    f(u)=W_u(u,k(u))

is smooth across0, is zero for u<=0, and equals the real analytic function

    f_P(u)=P_u(u,k_P(u))

on u>0. Every derivative of f at0 is zero, so every derivative of f_P at0 is zero. Real analyticity forces f_P=0 on a whole interval about0. This contradicts f(u)>0 for u>0. The abstract lemma follows.

The argument also works with strict negativity of the reduced component if hypothesis2 is separately supplied; only nonvanishing is used in the final contradiction. The B2 application below obtains hypothesis2 specifically from outgoing dynamics.

## 4. Application to smooth beta2 B2 profiles

Suppose a smooth B2 profile has an outgoing endpoint p of its equilibrium arc, in the sense of45,53 and162. The physical field W satisfies divW=4 and Omega=-curlW. Its derivative at p is4 n tensor n in an orthonormal tangent-normal chart, and its normal nullcline has the required equilibrium half-arc and outgoing reduced field.

The local normal form and explicit backward-containment estimates in162 section2 give a nonempty outgoing side of the local strong unstable curve on which every sufficiently small backward orbit stays near p and converges to p. For clarity, after simultaneously straightening the center and strong unstable curves the equations are U'=g(U)+UVc, V'=Vd, where d>2, g=0 inward and g>0 outward. Backward |V(t)|<=|V(0)|exp(2t), and the integrating factor for U bounds |U(t)| by |U(0)|exp(C|V(0)|/2); sufficiently small starting points remain local. For U>0 the resulting scalar monotonicity implies U(t)->0. This uses only the local outgoing geometry and the standard finite-C4 invariant-curve existence input recorded in53, not a global assumption that the zero set is one arc.

The coordinate change only changes spatial coordinates: it pushes forward W with the original time parameter. There is no time rescaling. Choose U positive outward; the local diffeomorphism then takes U=0 to the physical strong unstable graph and U>0 to u>h(v). The coefficients have at least the C1 regularity and boundedness used above.

The exact thermal transport and continuity give Theta=Theta(p) on this open local outgoing side. Its physical Cartesian derivative Theta_x is zero there. Along any of these backward orbits the vorticity equation is therefore W.gradOmega+Omega=0. Boundedness near the backward limit gives Omega=0 on the same local outgoing side.

The strong unstable curve is tangent to the physical normal direction and is locally a graph u=h(v) with h(0)=0. Its outgoing side is u>h(v). Every sufficiently small physical u>0 therefore has a nonempty v interval, containing v=0 after shrinking the neighborhood, in that outgoing region. This supplies hypothesis2. Thus no smooth B2 profile can have both an outgoing endpoint and a velocity polynomial of any fixed finite degree in this physical transverse coordinate on a full neighborhood of that endpoint.

This strictly enlarges the local Cartesian affine-in-y ansatz obstruction73 in polynomial degree. It does not enlarge the broad endpoint theorem: a general smooth velocity may have infinitely many transverse orders, and a nonlinear flow chart changes the Euclidean metric and does not preserve this polynomial hypothesis. In particular it neither excludes the incoming/accumulating alternatives nor the general smooth outgoing endpoint with nonconstant flat terminal temperature. No NO endpoint follows.

## 5. Dependencies and verification scope

The abstract lemma uses only polynomial identities, the Cartesian div-curl identities, integration of a finite triangular system and smooth/analytic implicit functions. The B2 corollary uses the local endpoint geometry and the explicitly proved backward bounds of162, with its finite-C4 invariant-curve dependency stated and source-checked in53. No PDE solution is obtained from the controls. Manufactured harmonic polynomials test(1) and its reconstruction, and flat-detachment test fields illustrate why their vorticity cannot vanish on the required transverse intervals. Finite tests do not prove an endpoint theorem.

Written UTC 2026-10-21T12:13:45.205547+00:00, before control implementation and review.

Review clarification UTC 2026-10-21T12:18:56.022364+00:00: actual Opus260 confirmed the abstract lemma and Opus261 confirmed the B2 backward-orbit argument after a sign correction to the review. Our convention throughout is Omega=-curlW. The reviews require the original flow time and the outgoing chart orientation; both are now explicit. Neither review is treated as a substitute for the proof.
