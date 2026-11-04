# Null basins of compact sets of vortical equilibria

## Statement

Let U in C2(R3;R3), P in C1(R3), div U=0, satisfy the rotating Euler profile equation. Assume U=o(|y|) uniformly, 0<c<1/2 and any finite omega. Put B=(cI-omega J)y+U, Omega=curl U, and let Phi_t be the complete B flow. Write N={B=0}, and alpha(x) for the backward limit set of x.

Then the set of x for which alpha(x) is contained in N and Omega is nonzero everywhere on alpha(x) has Lebesgue measure zero. In particular this confirms B15's conclusion for vortical x. No regular manifold structure of the whole equilibrium set is assumed.

This is a dynamical consequence of the bracket transport and constant divergence, once Omega is the given transported nonzero field. It does not by itself exclude backward limits that contain irrotational equilibria.

## 1. Compactness and linear structure

Uniform sublinearity gives completeness and a compact ball containing N and every backward limit set. Each alpha(x) is nonempty, compact and connected. At a vortical equilibrium p, the exact vorticity equation gives

    DB(p) Omega(p)=(1+c)Omega(p),    tr DB(p)=3c.

At a non-isolated equilibrium, DB(p) has a zero eigenvalue: an invertible derivative would isolate p by the inverse function theorem. Since Omega(p) is nonzero, the other eigenvalues are then exactly 0 and 2c-1. They and 1+c are distinct. Thus DB(p) has rank two and three simple real eigenlines.

For delta>0 let

    K_delta={p in N: p is non-isolated in N, |Omega(p)|>=delta}.

This set is compact. The derived set of N is closed, and the vorticity bound is closed. On K_delta the reversed vector field -B has a continuous invariant splitting into eigenlines with exponents

    -(1+c), 0, 1-2c.

Consequently, for a sufficiently large fixed time T and f=Phi_-T, the splitting E^cs plus E^u, of dimensions two and one, is dominated, and E^u is uniformly expanding. The bundles can be extended continuously to a neighborhood. In a metric adapted on the compact K_delta, inverse contraction on E^u and domination remain strict on a sufficiently small neighborhood. Invariance of the extensions away from K_delta is unnecessary.

## 2. An elementary application of the unstable-disk theorem

We use the following consequence of Alves-Pinheiro Theorem A. Let f be a C^(1+alpha) diffeomorphism, and K a compact set of fixed points admitting a dominated splitting E^cs plus E^u with dim E^u>0 and uniform expansion of E^u. Then

    {x: dist(f^n x,K) tends to zero}

has zero Lebesgue measure.

Here are all steps of the consequence. Suppose the basin has positive measure and restrict it to a bounded set of finite positive measure. By Egorov's theorem and inner regularity, choose a compact subset E of positive measure on which dist(f^n x,K) tends uniformly to zero. Extend the splitting to a neighborhood V of K in which the inverse expansion estimate stays strictly contracting. For N large, f^n(E) is contained in V for every n>=N. Define

    S=K union closure(union_{n>=N} f^n(E)).

Then S is compact, forward invariant and of positive measure. Uniform convergence implies

    intersection_{m>=0} f^m(S)=K.

Indeed f^m(S)=K union closure(union_{n>=N+m}f^n(E)), whose points have uniformly vanishing distance to K as m tends to infinity. The extended splitting on S is dominated over K. By choosing V small, every inverse derivative on its extended E^u line has norm at most some sigma<1. Hence the nonuniform-expansion condition of Alves-Pinheiro is satisfied uniformly on S.

Theorem A produces a positive-dimensional local unstable disk D contained in K. Any two points of D have backward iterates converging exponentially to each other. But f is the identity on K, so those distances are constant. A disk containing two distinct points is impossible. This proves the consequence.

For the present whole-space flow, cut off the vector field outside a compact neighborhood containing S and its finite-time orbit segments and compactify to S3. This gives the compact-manifold diffeomorphism required by the source without changing any dynamics used above.

The actual manuscript is in the team records, arXiv:math/0603148v1. Theorem A explicitly permits a forward-invariant S and requires bundle invariance only over its limiting invariant set. The neutral equilibrium direction belongs to E^cs. No uniformly hyperbolic map theorem, global center-stable graph, or normally hyperbolic manifold with boundary is being invoked.

## 3. Apply the consequence and cover the remaining points

The consequence makes the basin of each K_{1/k}, k a positive integer, null. If alpha(x) is not a point, its connectedness implies that none of its points is isolated in N: an isolated point would be both open and closed relative to alpha(x). If Omega never vanishes on alpha(x), compactness gives min_alpha(x)|Omega|>0. Thus alpha(x) is contained in some K_{1/k}, and dist(Phi_-t x,K_{1/k}) tends to zero. All such x lie in the countable union of these null basins.

It remains to treat alpha(x)={p} with p vortical. The eigenvalue 1+c is positive and the other two eigenvalues have real parts summing to 2c-1<0. Hence DB(p) has an eigenvalue with negative real part; the reversed flow has a nonzero unstable subspace. The local trapped set is contained in a Lipschitz center-stable graph of dimension at most two. One may use the explicit variation-of-constants graph estimate already proved in the team records, Section 4; that local estimate does not use omega=0 or Bernoulli monotonicity. A countable cover of these equilibrium neighborhoods, followed by countably many finite-time images, proves nullity of the entire point-convergent set.

The two cases prove the statement.

## Scope and repairs to the submitted sketch

The conclusion of B15 is confirmed by this replacement proof. Its asserted finite collection of global two-dimensional center-stable graphs over an arbitrary equilibrium subset was not established by the cited normally-hyperbolic-manifold theorem. A compact subset of an arc need not itself be a manifold; continuous bundle extension does not by itself supply the claimed global graphs. The unstable-disk argument avoids that gap entirely.

A nontrivial totally disconnected Cantor set cannot itself be alpha(x), since alpha(x) is connected. A larger zero set may have Cantor subsets, and the proof allows those without claiming that an individual nonpoint limit set is totally disconnected.

The argument is uniform in omega, but uses c<1/2 for the strict backward expanding exponent. It does not treat a limit set on which Omega vanishes at some point.

## B14: local zero geometry and arc scope

At any vortical zero with a zero eigenvalue, the spectrum above consists of three distinct real numbers, so rank DB=2. Choose two components of B with independent differentials. Their common zero set is a C2 curve by the implicit function theorem, and the full zero set N is a relatively closed subset of that curve. Its tangent at the equilibrium is ker DB. The negative eigenvalue 2c-1 supplies the same local null graph used for point limits.

On N, U=-cy+omega Jy, hence X=omega Jy and M=omega|y_h|^2. The momentum equation at a zero gives grad P=-(1-c)U-omega JU. Dotting with Jy yields

    partial_theta P=omega(2c-1)|y_h|^2.

Any compact arc or closed curve J of vortical equilibria has the fixed normal exponents -(1+c) and 1-2c for the backward flow. Its attracting set in the sense dist(Phi_-t x,J)->0 is null by the theorem proved above. This does not require treating an arc with endpoints as a boundaryless normally hyperbolic manifold. The stronger statement identifying the entire local distance-attracting set with one two-dimensional manifold needs a precise endpoint convention; the ordinary stable manifold formed from strong-stable fibers over J is a different definition. The nullity conclusion, all pointwise spectral facts, and the identities on N are confirmed.

## Independent source check of the repaired Bonatti-Crovisier route

The actual Bonatti-Crovisier manuscript, in the team records, arXiv:1401.2452v1, was retrieved and its Main Theorem, Corollaries 1.2-1.5 and Section 5.3.1 read. The Main Theorem allows the bundle called E^c to contain contracting directions. It states that a compact partially hyperbolic invariant set with splitting E^c+E^uu is contained in a locally invariant C1 submanifold tangent to E^c if and only if each strong unstable leaf meets the set in just its base point. The set is contained in the interior of that submanifold, which may have boundary.

For K_delta above, take f=Phi_-T and E^c=E^cs. Distinct fixed points cannot belong to one strong unstable leaf, since their backward f-iterates keep a fixed positive distance. Thus the theorem does supply the single C1 center-stable surface missing from the original sketch. This is stronger than a family of unrelated plaques, and unlike Fenichel's manifold theorem it does not assume that K_delta is itself a manifold.

The finite-distance expulsion step is valid after taking a sufficiently large iterate. On the surface near K_delta, use local transverse normal coordinates. Its local f-invariance makes the normal component zero at normal coordinate zero. The induced derivative on the normal quotient expands by exp((1-2c)T) at K_delta. In an adapted normal norm, after increasing T if necessary, that expansion is uniformly greater than one. Continuity and the mean-value formula preserve a strict expansion factor on a sufficiently small neighborhood. Finitely many normal-bundle charts give the same estimate for the unsigned normal norm, without requiring orientability. An orbit remaining in that neighborhood for all positive iterates must have normal coordinate zero. It lies in the C1 surface and hence in a null set. Countably many finite-time preimages cover the basin.

This validates the revised B15 source-based route as well as the independent unstable-disk proof above. The source's Corollary 1.2 alone concerns the maximal TWO-SIDED invariant set and would not by itself prove the forward trapped-set conclusion; the transverse expansion argument is required. No claim that an arbitrary locally invariant center surface is unique is used.
