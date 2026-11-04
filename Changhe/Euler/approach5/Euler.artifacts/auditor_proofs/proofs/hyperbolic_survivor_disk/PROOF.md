# An unstable manifold in a positive-volume hyperbolic survivor set

## Statement

Assume U in C2 is a uniformly sublinear rotating Euler profile with 0<c<1/2. Let C be a compact subset of a backward-trapping ball on which |Omega|>=delta and |B cross Omega|>=delta, for some delta>0. Put Psi_t=Phi_-t and

S={x in C: Psi_t x is in C for every t>=0},
K={x in C: Psi_t x is in C for every real t}.

If the set of points whose Psi-orbits eventually stay in C has positive Lebesgue measure, then K contains the entire strong unstable manifold of at least one point for Psi. It therefore also contains the two-dimensional weak unstable manifold obtained by flow saturation.

No local maximality or transitivity of K is assumed here. The additional assertion in CO5-prime that local maximality forces a contained basic attractor is not part of this statement.

## Reduction to a forward-invariant positive-volume set

The eventual-survivor set is the countable union of Psi_-n(S), n>=0. A finite-time C2 flow diffeomorphism preserves null sets, so |S|>0. S is compact and forward invariant for Psi. For every fixed T>0,

K=intersection_{n>=0} Psi_{nT}(S).

Indeed, belonging to the right side means the whole orbit through arbitrarily early discrete times stays in C, which is equivalent to staying in C at every real time. Nested compactness implies that Psi_{nT}(S) approaches K uniformly in distance.

A056 gives a uniform hyperbolic splitting on K for Psi: a one-dimensional unstable line with exponent a=1-2c>0, the flow line, and a one-dimensional stable line with exponent -(1+c). In particular E^cu=E^u and E^cs=E^s plus E^0 are dominated for a sufficiently large time-T map f=Psi_T. Choose T so large that, in a fixed metric, both the domination product and ||Df^-1|E^u|| are strictly less than one.

The splitting extends continuously to a neighborhood of K. By continuity, after shrinking the neighborhood, inverse contraction on the extended E^u and the unstable cone properties still hold uniformly. Replacing S by f^m(S) for large m puts it in that neighborhood and preserves its positive volume. This replacement leaves K unchanged. A cutoff outside the compact region makes f the time-T map of a C2 flow on S3 without changing this argument.

## Disk theorem and exact hypotheses

Apply Alves and Pinheiro, Theorem A (equivalently their Theorem 5.1 after choosing a transverse disk by Fubini): a forward-invariant compact positive-volume set S for a C^(1+alpha) compact diffeomorphism, with a continuous splitting on S dominated over intersection f^n(S), and nonuniform expansion along E^cu on a positive-volume subset, has a local unstable disk in that intersection.

Here nonuniform expansion is actually uniform. Continuity of the extended line and inverse contraction give a sigma<1 with

||Df^-1|E^cu(fx)||<=sigma

for every x in the replaced S. Thus every average in their NUE condition is at most log sigma<0. All regularity and splitting hypotheses hold, and the disk dimension is one. We obtain a local strong unstable interval D contained in K.

For clarity, the part of the source argument needed in this uniform setting is as follows. Fubini supplies a smooth curve transverse to E^cs whose intersection with S has positive length. At a length-density point, inverse images of a fixed-size unstable cone interval contract uniformly. Bounded distortion follows from C^(1+alpha) regularity and dominated control of the tangent direction: the logarithms of the Jacobian ratios are bounded by a convergent sum of Holder powers of backward distances. In dimension one the preintervals have uniformly comparable left and right lengths. The density-point property therefore makes the images' relative length outside f^n(S) tend to zero. A C1 convergent subsequence of fixed-size cone intervals has a limit contained in every f^m(S), by closedness and this relative-length estimate. Backward contraction identifies that limit as a local unstable interval in K. This is the mechanism of their Section 5; no entropy or physical-measure premise is used.

## From a local interval to a full unstable manifold

Let p be an interior point of D. Pass to a subsequence f^{n_j}p->q in K. For each fixed integer m>=0,

f^{n_j-m}p -> f^-m q.

Uniform expansion on unstable lines implies that the distance from f^{n_j-m}p to both endpoints of f^{n_j-m}D, measured intrinsically on that unstable curve, tends to infinity. Therefore the entire fixed-size local unstable interval around f^{n_j-m}p lies in K for all large j. Continuous dependence of local unstable manifolds over a compact hyperbolic set, and closedness of K, imply

W^u_loc(f^-m q) is contained in K.

Since K is invariant, f^m W^u_loc(f^-m q) is contained in K for every m. Their increasing union is W^u(q), proving full strong unstable saturation at q. Flow invariance then gives union_{t in R} Psi_t W^u(q) contained in K, which is the weak unstable manifold of the orbit of q.

## Actual source and remaining scope

J. F. Alves and V. Pinheiro, Topological structure of (partially) hyperbolic sets with positive volume, arXiv:math/0603148v1. The actual manuscript is retained at in the team records, with extracted text and SHA256 retrieval metadata. The hypotheses on pages 3-4 and Section 5 on pages 11-15 were read. The uniform-expansion application above does not depend on the printed choices of constants in their nonuniform Pliss step.

Their map Theorem E assumes a uniformly contracting E^cs and cannot be applied to the flow time map here, since E^cs contains the neutral flow direction. Their Theorems F-G concern uniformly hyperbolic maps, also not directly the time-one map of a nonsingular flow. These statements have not been used to infer a basic attractor. Thus this settles the first implication in CO5-prime and leaves its locally-maximal-to-attractor implication for a separate flow argument.

## Stronger conclusion: a contained hyperbolic attracting set

Under the same hypotheses, K contains a nonempty compact hyperbolic attracting set L for the backward flow. Here attracting set means that there is a compact neighborhood N and a time T>0 such that Psi_T(N) is contained in the interior of N and

    L = intersection_{n>=0} Psi_{nT}(N).

The set L is invariant under the entire flow. Transitivity and density of periodic orbits are not included in this assertion. Consequently this statement alone does not authorize direct application of the basic-set theorem of Bowen and Ruelle.

Let q be the point obtained above, and define

    M = union_{t in R} Psi_t W^u(q),
    L = closure(M).

All closures here are in the ambient manifold. Since M is contained in the compact invariant K, L is compact, flow invariant and hyperbolic, with no flow zeros. We first show that L contains the entire strong unstable manifold of each of its points. If x_j in M tends to x in L, then W^u_loc(x_j) is contained in M. The local unstable manifolds vary continuously in C1 over K. Their limit W^u_loc(x) is therefore contained in L. Applying this argument at Psi_-t(x) and using invariance gives W^u(x) contained in L. In particular L contains a fixed-size local weak unstable disk at each point.

Choose a sufficiently small uniform local stable radius epsilon, measured by intrinsic length in the one-dimensional stable leaf. Write W^s_epsilon(x) for the open stable arc and define

    V = union_{x in L} W^s_epsilon(x),
    N = union_{x in L} closure(W^s_epsilon(x)).

The continuity of local stable arcs over the compact set L gives compactness of N and N=closure(V). We check that V is open. At any x in L, choose a sufficiently small local weak unstable disk D through x. This whole disk belongs to L. Its local stable arcs depend continuously on their base points. After shrinking the disk and stable length, distinct such arcs are disjoint, by uniqueness of local stable versus weak unstable intersection. Thus their evaluation map from an open three-dimensional product disk into the ambient three-manifold is continuous and injective. Invariance of domain makes its image open. The same argument with a small interval around any interior point of a stable arc shows that every point of V is interior. This uses only standard local stable-manifold geometry on the nonsingular hyperbolic K. It does not assume that K was locally maximal, and it does not use differentiability of stable holonomy.

Uniform stable contraction gives constants C>=1 and lambda>0 such that, for z in closure(W^s_epsilon(x)), the intrinsic stable distance between Psi_t(z) and Psi_t(x) is at most C epsilon exp(-lambda t), t>=0. Take T sufficiently large that C exp(-lambda T)<1/2. Then

    Psi_T(N) is contained in union_{x in L} W^s_{epsilon/2}(x),

which is contained in V and hence in the interior of N. The compact sets Psi_{nT}(N) are nested. Each contains L. Conversely, every point of Psi_{nT}(N) is within C epsilon exp(-lambda nT) of L, so their intersection is exactly L. This proves the assertion.

If a definition requires a neighborhood appropriate to the full flow, use the finite saturation union_{0<=t<=T} Psi_t(N). It is compact, contains an open neighborhood of L, still maps strictly into its interior after time T, and its forward intersection is L. Every point of V converges in distance to L for continuous forward Psi-time.

This closure-and-stable-saturation argument parallels the map argument in Alves-Pinheiro Section 7.2. The extra neutral direction has been included explicitly in the weak unstable disk. Bowen-Ruelle Proposition 5.5 contains the corresponding stable-neighborhood geometry in its basic-set setting. Neither source's uniformly hyperbolic map theorem is applied to a time-one flow map.

Remaining distinction: proving that L contains a BASIC hyperbolic attractor requires a flow spectral-decomposition or equivalent argument. That additional reduction is not claimed here. The new result repairs the existence of a hyperbolic attracting set in CO5-prime without the extra local-maximality assumption, while retaining this distinction.
