# Repeated audit of the dynamical foundations

Status: CONFIRMED for the individual statements below, with their stated external dependencies and hypotheses. This is not approval of the whole assembled report or a nonexistence theorem for unrestricted rotating profiles.

## 1. Scope, exact equations and completeness

Let 0<c<1/2, omega be any finite real number, Jx=(-x2,x1,0), A=cI-omega J, U in C2(R3;R3), and P in C1(R3). Assume

    div U=0,  (1-c)U+DU(Ax+U)+omega JU+grad P=0,
    U(x)=o(|x|) uniformly as |x| tends to infinity.

Put B=Ax+U, X=cx+U, Omega=curl U, a=1-2c, kappa=1+c. Let Phi_s be the forward B flow and Psi_t=Phi_-t. In this proof only, use

    H=P+|U|^2/2+(Ax).U-ca|x|^2/2.

The quadratic correction distinguishes H from the reduced Bernoulli function elsewhere in the report. Direct differentiation gives

    div B=3c,  grad H=-aX-Omega cross B,
    [B,Omega]=-kappa Omega,
    D Phi_s Omega=e^(kappa s) Omega composed Phi_s,
    L_B(U.dx)=-a U.dx+d(|U|^2/2-P).

Curling the last identity, or combining the bracket with div B, gives Phi_s^*sigma=e^(-as)sigma for sigma=i_Omega(dx1 dx2 dx3). These formulas use the full Euler equation; a freely chosen bracket partner is not automatically curl U.

Uniform sublinearity bounds |B| by C(1+|x|), hence both time directions exist globally by the ordinary differential equation continuation criterion. Choose R0 so |U(x)|<=c|x|/2 outside its ball D. Then B(x).x>=c|x|^2/2 there. Thus Psi traps D and every backward orbit eventually enters D. Its limit set is nonempty, compact, connected and invariant. The core Lambda=intersection_(t>=0) Psi_t(D) is null because |Psi_t(D)|=e^(-3ct)|D|. None of these estimates restricts omega: Jx.x=0.

## 2. Circulation and periodic orbits

The one-form identity integrated on any closed C1 curve transported for an existing time interval gives

    integral_(Phi_s C) U.dx=e^(-as) integral_C U.dx.

The same formula for X follows because X.dx-U.dx=d(c|x|^2/2). For a nonstationary periodic orbit of period T, B and a nonzero Omega are independent eigenvectors of D Phi_T with eigenvalues 1 and e^(kappa T). The determinant e^(3cT) gives the third eigenvalue e^(-aT). This proves the claimed forward and backward saddle dimensions.

For every periodic orbit, circulation is zero when a!=0. Parametrizing by B and writing U=B-cx+omega Jx gives

    integral_0^T |B|^2 ds=-2 omega A_xy,
    2A_xy=integral (x1 dx2-x2 dx1).

For a T-periodic planar curve z, Fourier expansion gives |integral Im(conj(z)z')|<=(T/(2pi)) integral |z'|^2. Equality requires precisely one first Fourier mode, apart from translation. Comparing planar speed with |B| gives T>=2pi/|omega| when omega!=0; equality forces constant height and a uniformly traversed planar circle. At omega=0 there is no nonstationary periodic orbit. The circulation derivation itself needs only the times on which a local flow exists, and a periodic orbit supplies its own complete trajectory.

The harmonic-gradient example U=(-cx1,-cx2,2cx3), with harmonic potential phi and P=-a phi-(Ax).grad phi-|grad phi|^2/2, is exact by differentiating this pressure. Its carrier is (-omega Jx_h,3cx3). It has circular backward limits when omega!=0 and singleton limits when omega=0. It violates sublinearity and decay. Likewise a nonzero constant U with its linear pressure has a singleton core and entropy zero; it cannot be included in a statement asserting positive core entropy for every nonzero sublinear profile.

## 3. Compact invariant measures and exact exponents

Let mu be a compactly supported probability invariant and ergodic for the entire B flow, with B and Omega nonzero mu-almost everywhere. No time-one ergodicity is assumed. The flow derivative of log|Omega| equals n.Sn-1, where n=Omega/|Omega| and S=sym DU, and is bounded on the compact support. The derivative of log|B| is also bounded. Birkhoff applied to either derivative gives a constant limiting increment per unit time. A nonzero constant would make the finite-valued logarithm tend to plus or minus infinity almost everywhere, contradicting the fact that its distribution is unchanged by the flow. Applying the same argument backward gives sublinear logarithmic increments in both directions.

The Cauchy law now gives the pure Oseledets line R Omega of exponent kappa. Self-transport of B gives the pure zero line R B. The two-sided calculation is necessary to identify pure lines. Their independence also follows from invariance of the parallel set: if Omega=fB there, then f(Phi_s x)=e^(-kappa s)f(x), inconsistent with recurrence of a finite nonzero f. The determinant supplies the last exponent -a. For Psi the spectrum is (a,0,-kappa).

On a compact initial subset of {Omega!=0}, all backward images lie in a common compact ball, so the Cauchy law gives uniform contraction along Omega. The exact quotient area law is the flux law Psi_t^*sigma=e^(at)sigma. Euclidean quotient area has the extra ratio |Omega(x)|/|Omega(Psi_t x)|. The statement does not assert uniform hyperbolicity near zeros of B or Omega.

## 4. Null basins and equilibrium limit sets

For x with Omega(x)!=0 and K=alpha(x), the maximum forward cocycle exponent on K is at least kappa. Here the named semiuniform cocycle theorem identifies the uniform top growth rate with the maximum over ergodic invariant probabilities on K. If it were less than kappa, a fixed-time derivative bound strictly below e^(kappa T) would hold in a neighborhood of K. The late backward orbit stays in that neighborhood. Applying this derivative bound successively in the forward direction, and using Cauchy transport backward, would force |Omega(Psi_(nT)x)| to grow without bound. Compact backward trapping contradicts this.

If K={p}, the largest real part of an eigenvalue of DB(p) is therefore at least kappa. Since tr DB=3c, some real part is at most (2c-1)/2<0. Thus -B has a genuinely unstable direction near the eligible equilibrium set. On a compact piece of that set choose a uniform strict threshold, for example (2c-1)/4 for the negative real part of DB. The local trapped set is contained in a Lipschitz graph of dimension at most two, by the local center-stable graph theorem, equivalently its weighted variation-of-constants construction. A finite spatial cover on each compact piece and integer entry times cover all convergent vortical orbits by countably many pullbacks of null graphs. This proves nullity without an uncountable union of stable manifolds.

Suppose instead that all of a nonpoint K consists of equilibria. Connectedness makes its points nonisolated zeros, so DB is singular there. The maximal-exponent equilibrium has spectrum lambda,0,3c-lambda with lambda>=kappa and opposite nonzero signs. Rank two and the implicit function theorem reduce nearby zeros to a curve, and connectedness of K supplies a nontrivial interior equilibrium arc. The cited local invariant-manifold theorem of Bonatti-Crovisier, applied to the time-T map of Psi and its inverse, supplies center-stable and center-unstable surfaces. Only invariance for this discrete map is needed.

After straightening these surfaces, write its coordinates as (w,s,u). Along an equilibrium arc,

    w'=w+F(w,s,u),  s'=A(w,s,u)s,  u'=D(w,s,u)u,
    |F|<=C(|s|+|u|),  |A|<=theta<1,  |D|>=theta^-1.

On a finite passage of n steps the total center displacement is at most C(1-theta)^-1(|s_entry|+|u_exit|). Every sufficiently late point lies close to K, so both normal endpoints are small. A late entrance near an interior arc point therefore cannot make a first exit through the smaller center box. It remains there, has u=0, and has summable s and center increments. The discrete orbit converges to an equilibrium; continuity for the intervening bounded time interval gives convergence of the whole flow. This contradicts the assumed nonpoint limit. The essential hypothesis is that the entire K consists of equilibria.

An independent proof for limits consisting of vortical equilibria uses the cited Alves-Pinheiro positive-volume unstable-disk theorem on a compact positive-volume survivor set. Its invariant core would contain an unstable disk of equilibria, impossible because the time map is the identity there. This secondary proof is not needed to enlarge the preceding conclusion.

## 5. Core entropy and its regularity boundary

For nonconstant smooth U, curl U cannot vanish identically: otherwise every component of U is entire harmonic and uniformly sublinear, hence constant by the harmonic gradient estimate. Choose a loop of nonzero circulation. Backward transport multiplies its circulation by e^(at); its images lie in a common compact ball where U is bounded. Their lengths are consequently bounded below by C e^(at).

Cut off U outside that ball and compactify the resulting linear-at-infinity field by inversion to a smooth field on S3. The affine part becomes the linear field -(cI+omega J)z in the inverted coordinate. Every invariant probability is supported on the core or the added point, so the compactified backward time-one map has the core's entropy. The named Yomdin volume-growth inequality at regularity r gives a<=h_top+R/r, where R is its derivative-growth rate. For a smooth field the same compactification permits r to tend to infinity, proving h_top(Psi_1|Lambda)>=a.

At fixed finite r the loss R/r remains. The separate C2 loss-free argument requires Omega nowhere zero on the entire core. Then finitely many vortex flow boxes represent the quotient flux area, and an n-step Bowen ball has uniformly bounded quotient image area. The exact growth e^(an) of a transverse disk's flux forces at least C e^(an) such balls. This supplies the entropy lower bound under that extra hypothesis. Neither argument establishes unconditional C2 entropy in the presence of vorticity zeros, and the smooth branch requires nonconstant U under sublinearity.

## 6. Vortex completeness and regular hyperbolicity

The frozen C1 vector field Omega is complete without a global bound on Omega. For a compact set E of starting points, all Phi_-s(E), s>=0, lie in one compact ball. There is a uniform local Omega-flow time delta on a slightly larger ball. If chi denotes that local flow, then

    z_s(tau)=Phi_s chi_(e^(-kappa s)tau) Phi_-s(x)

solves z_s'=Omega(z_s) for |tau|<=delta e^(kappa s). Uniqueness glues these solutions to all real tau. It also gives Psi_t chi_tau=chi_(e^(-kappa t)tau) Psi_t. A compact vortex segment therefore contracts at most C e^(-kappa t) in Euclidean length.

On a compact invariant regular set K, meaning |B cross Omega| is bounded below by a positive constant, the plane span(B,Omega) is continuous and invariant, with neutral and contracting directions for Psi. Transport of the covector alpha=(B cross Omega).dx gives expansion e^(at) on its transverse quotient, up to bounded changes of norm. The graph transform supplies a complementary unstable line; thus K is uniformly hyperbolic with rates -kappa,0,a. Its complete strong stable curves are the complete vortex lines, by the local stable-manifold theorem and the contraction just proved.

This statement does not extend uniform hyperbolicity through B=0, Omega=0 or B cross Omega=0. On a bounded full orbit where Omega=fB with neither zero, the exponential law for f forces accumulation at B=0 in one direction and Omega=0 in the other. It therefore yields the report's regular/degenerate alternatives, which need not be mutually exclusive.

## 7. Regular attracting sets, survivor disks and entropy

For a compact regular set saturated by full weak unstable leaves, a local unstable curve together with carrier and vortex shifts has three independent tangent vectors. The inverse function theorem gives an open tube, and vortex contraction makes it an attracting neighborhood. Minimal nonempty compact weak-unstable-saturated subsets exist by nested compact intersection. Their leaf closures fill the set; local product structure and the hyperbolic closing lemma then give local maximality, transitivity and dense periodic orbits. Distinct such attracting sets have disjoint open basins, so there are at most countably many.

For the coverage statement, the source first reduces positive-volume survivors with regular alpha limits to a compact positive-volume forward-Psi-invariant set C with uniform regularity bounds. Its nested core K is regular hyperbolic. Choose T large enough that domination and inverse unstable contraction are strict on K, extend the splitting to a neighborhood, and replace C by Psi_(mT)C inside that neighborhood. The neutral flow direction is retained in the center-stable plane. These are exactly the hypotheses of the cited Alves-Pinheiro theorem, which produces a local unstable interval I in K, not a whole unstable leaf.

Choose an interior point p of I and a forward accumulation q. Expansion makes the intrinsic distances of both endpoints of Psi_(nT)I from its center tend to infinity. For every fixed backward iterate of q, compactness and continuous local unstable manifolds therefore put its full local unstable interval inside K. Taking forward images and their union gives W^u(q) contained in K, and flow saturation gives its weak unstable leaf. Its closure contains one of the minimal attracting sets above. The corresponding open basin meets the original surviving orbit, contradicting removal of all such basins. Thus the countable basins cover the stated regular-alpha class almost everywhere, not automatically every vortical point.

For one resulting basic regular attractor A, let e^u be a unit unstable vector and g(x)=|alpha_x(e^u)|. It is continuous and bounded above and below by positive constants. Covector transport gives J_t^u=e^(at)g(x)/g(Psi_t x). Hence the integral of the geometric unstable potential is -a for every invariant probability. The Bowen-Ruelle zero-pressure theorem for a C2 basic attracting flow and the variational principle give h_top(Psi_1|A)=a. The whole-core entropy estimate alone would not prove this individual-attractor equality. Basins are open and invariant, hence have infinite volume under the constant negative divergence; the attractors themselves are null subsets of the core.

No compact regular invariant set can contain a B,Omega plaque. Stable thickening using local product structure would then give an open subset of the null core. Regular and singular kinematic models used as obstruction examples need not have their bracket field equal to curl U, so they do not construct actual Euler counterexamples.

## 8. Lorenz-type carrier zeros and finite networks

Let K=alpha(x) be an actual nonsingleton backward limit set, and suppose Omega is nowhere zero on K. At p in K with B(p)=0, the bracket identity gives DB(p)Omega(p)=kappa Omega(p); the other eigenvalues sum to -a. If both had negative real part, p would be hyperbolic for -B with one-dimensional stable manifold equal to its vortex line. That line meets K only at p: a nontrivial bounded full orbit on it has Omega parallel to B, and the exponential ratio law contradicts the positive lower bound for |Omega| on K.

The actual orbit defining a nonsingleton K has arbitrarily late entrances toward p and exits from a fixed neighborhood. Taking limits of entrance points whose residence times tend to infinity produces another point of K on the local stable manifold, a contradiction. Thus the remaining eigenvalues are real, lambda3<0<=lambda2, with lambda2+lambda3=-a. The argument needs the actual limit-orbit hypothesis. It gives neither lambda2<kappa nor the same assertion for an arbitrary disconnected invariant set.

The separate finite-vortical-network result retains its stated source hypotheses: if a backward limit is contained in such a network, it is a node. It does not exclude singleton node limits. Its local passage identity is |g'(r)|=e^(aT(r)); replacing this derivative by the displacement g(r) would be wrong. No fresh derivation of that entire separate network proof is claimed here.

## 9. Verification boundary and dependencies

All 679 lines of the current assembled Section2B were read in this pass, and all ten sections of the earlier detailed correction proof and all eight sections of the previous complete-proof audit were reread. The preserved report is pinned by sha256 in the team records. The present audit checks statements, proof uses, time directions, completeness, pressure convention, countability and every-omega scope.

Named external inputs are the ordinary invariant/center-stable manifold and graph-transform theorems, Oseledets and Birkhoff, the semiuniform cocycle maximum theorem, Bonatti-Crovisier's local invariant surfaces, Yomdin's volume-growth bound, Alves-Pinheiro's unstable-disk theorem, the hyperbolic closing and local product theorems, and Bowen-Ruelle's pressure theorem. Their relevant primary statements were checked in the earlier dependency audits cited by Section2B and the preserved correction proof; this pass did not retrieve every publication again. The assembled opening sentence that the text is self-contained must be read with its explicit preceding qualification about these external inputs and deferred network/model arguments.

The proof statements above are confirmed at their exact scopes. Whole-report approval, unconditional finite-regularity coverage, exclusion of arbitrary helicity-sign-changing basins, and unrestricted decaying rotating-profile nonexistence remain OPEN.
