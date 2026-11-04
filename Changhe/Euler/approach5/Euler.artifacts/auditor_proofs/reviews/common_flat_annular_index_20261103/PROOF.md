# Exact orders and annular indices around a common flat orbit

Status: LIT301 confirmed at the local scopes of A2426-A2428 and A2430; the flatness-only inference is refuted A2429; full-system and global extensions remain open A2431. The planar counterexample concerns an inference from flatness and zero indices. It is not a solution of the carrier or Euler equations.

## 1. Exact hypotheses and conclusions

Fix 0<c<1/2 and omega in R. Define Jx=e3 cross x, A=cI-omega J, L=(1-c)I+omega J, X(x)=Ax, a=1-2c, b=2(1-c) and eta=a/b. Let Phi:D times I -> G be a smooth X-flowbox, where D is an open disc in R2 centered at zero and I is an interval containing zero. Thus partial_t Phi=X composed with Phi. Put Gamma=Phi({0} times I), and let x0 be a point of Gamma. Smooth V,S on G satisfy the complete conditional system F:

    div V=0, X.V=0, DV X=-LV,
    X.grad S=-bS, X cross W=aV, W.grad S=0,
    W=curl V, P=S+|V|^2/2, -Delta P=tr((DV)^2).

Assume S=0 on Gamma, S<0 off Gamma, and every derivative of V and S vanishes at x0. No global profile or decay is assumed. Define Pi=pr_D composed with Phi^{-1} and

    v(y)=dPi_(Phi(y,0)) V(Phi(y,0)).

Its zeros away from zero are locally isolated. Each such zero q has an integer N(q)>=1, equal to the exact vanishing order of both V and W at the corresponding point. In a smaller product flowbox around its orbit, each of |V| and |W| is bounded above and below by positive constants times |y-q|^N(q). Its transverse index is -N(q). N is constant along each connected zero orbit segment. Neither N nor the constants are claimed uniform near Gamma.

Call r admissible if the closed radius-r disc lies in D and v is nonzero on its boundary. Write d(r)=deg(v/|v|,|y|=r). For admissible 0<r<R,

    d(r)-d(R)=sum_(r<|q|<R, v(q)=0) N(q).             (1)

The sum is finite. Either some punctured neighborhood of zero contains no other zero, in which case d is constant for all small radii, or zeros accumulate at zero and d(r) tends to positive infinity through admissible radii. A uniform upper bound on any cofinal sequence of admissible radii excludes this accumulation. It does not exclude the central flat orbit itself.

For every fixed integer M>=1, the planar field represented by

    f_M(z)=exp(-1/|z|^2) conjugate(sin(1/z)^M), z!=0,
    f_M(0)=0,                                        (2)

is smooth and flat exactly at zero. Its other zeros q_k=1/(k pi), k a nonzero integer, have order M and index -M, while

    deg(f_M/|f_M|,|z|=r)=M(2 floor(1/(pi r))+1)       (3)

whenever 1/(pi r) is not an integer. This gives unbounded inner degree, even with zero first derivatives at every other zero when M>=2. It is not divergence-free and fails any estimate |div f_M|<=C|f_M| on a neighborhood of zero with finite C.

## 2. Exact common order and local index

Apply the already confirmed LIT288 theorem, A2134-A2140, on G minus Gamma. This connected open set has S nonzero, with either sign permitted by that theorem. All its local carrier, divergence and scalar hypotheses occur in F. The alternative V identically zero there is impossible: continuity would give V=0 throughout G, whence P=S and Delta S=0. The harmonic maximum principle applied to S<=0 with its interior zero x0 would force S=0, contradicting the strict sign off Gamma.

For completeness, the local scalar reduction off Gamma is

    W=eta grad(log|S|) cross V,
    V=|S|^eta grad phi,
    X.grad phi=0,
    Delta phi+eta grad(log|S|).grad phi=0.             (4)

The drift is smooth and bounded on a sufficiently small closed neighborhood of any p off Gamma. The explicit Carleman estimate in the audited LIT288 proof rules out a flat nontrivial zero. At a remaining zero the first nonzero scalar term has degree N+1, N>=1. Since X.grad phi=0, it is independent of the direction X(p). At its lowest degree the Euclidean Laplacian vanishes, so on an orthonormal transverse plane it is

    Q(u1,u2)=Re(C(u1+i u2)^(N+1)), C!=0.

Its gradient has norm (N+1)|C||u|^N and winding number -N. Taylor's remainder in the velocity is O(|u|^(N+1)). The smooth positive factor |S|^eta gives the asserted exact velocity order and two-sided bounds on a smaller disc.

The first equation in (4) gives |W|<=C|V| locally, while aV=X cross W gives |V|<=C'|W|, since a>0 and X is bounded locally. Thus W has the same exact order and two-sided bounds. In particular the zeros coincide. Alternatively, grad S.X=-bS!=0 makes cross product with grad S injective on X-perp, so it cannot annihilate the leading velocity tensor.

The transport law is

    V(exp(tA)x)=exp(-tL)V(x).

For each finite time whose orbit segment remains in G, differentiation in x gives invertible linear transformations of every derivative tensor. Therefore the first nonzero derivative order is constant along the zero orbit. The same formula gives a uniform bound over a smaller compact time interval. It propagates flatness from x0 to Gamma. W=curl V and aV=X cross W then give equality of the flat sets. This also recovers the relevant C66 conclusions without extending the bounded drift through Gamma.

## 3. Quotient coordinates and annular degree

The kernel of dPi is span{X}. Since X.V=0, dPi is injective on the plane containing V, and v=0 precisely where V=0 on the section. Its restriction to X-perp has bounded norm and bounded inverse on any compact smaller section. It preserves exact local order and the two-sided estimates.

The index computed on an orthonormal section in Section 2 is the index on the quotient used in (1). Indeed A+L=I gives

    exp(-tL)=exp(-t) exp(tA).

Thus transport of V is a positive scalar times the differential of the X-flow. Changing a section along an orbit preserves the direction of the quotient vector field. A smooth coordinate change on that quotient acts on both the domain and the vector components by its differential. Its two orientation signs cancel. Near a zero the varying differential can be deformed to its invertible value at the zero. These observations prove that the quotient index is -N. Only finite local flow times are used.

The zero set is closed relative to D minus {0}, and each zero there is isolated by Section 2. There can therefore be only finitely many zeros in a compact admissible annulus: an infinite sequence would have a zero accumulation point inside that annulus. Remove mutually disjoint small discs around these zeros. On the remaining region v is nonzero. Pulling back the closed angular form (u1 du2-u2 du1)/(u1^2+u2^2) and applying Stokes' theorem gives

    d(R)-d(r)=sum index_q(v)=-sum N(q),

with the inner boundaries carrying the negative orientation. This proves (1).

Every compact interval of positive radii contains only finitely many zero radii. Admissible radii are consequently cofinal at zero. Fix one admissible R. If only finitely many zeros lie inside it, all sufficiently small discs avoid them away from zero. Otherwise their distances tend to zero. Since every term N(q) is a positive integer, the sum in (1) grows without bound as r decreases to zero. This proves the stated dichotomy and the implication of an upper bound along any cofinal admissible sequence. No bound on N or d has been inserted.

## 4. The exact smooth counterexample

Fix M>=1. Every finite derivative of sin(1/z)^M on |z|=r is bounded by C r^(-K) exp(M/r), by repeated chain and product rules and the elementary exponential bounds for sine and cosine. Derivatives of exp(-1/r^2) multiply that exponential by functions bounded by powers of r^{-1}. Hence each derivative of f_M is bounded by

    C r^(-K) exp(-1/r^2+M/r).

For sufficiently small r this is at most C r^(-K) exp(-1/(2r^2)), which is O(r^j) for every fixed j. Extend every derivative by zero at the origin. Inductively, the vanishing difference quotients show that these extensions are the derivatives of the extended function. Thus f_M is smooth and flat at zero.

The positive exponential creates no new zeros. The only zeros of sin w are k pi, each simple. Inversion misses w=0 at finite z. At q_k=1/(k pi),

    (sin(1/z))' = -(k pi)^2 (-1)^k !=0.

Therefore f_M has exact order M and local index -M at q_k. These are all off-center zeros; none is flat. Nonzero values cannot be flat either. If M>=2, all first derivatives vanish at each q_k.

For a positive radius-r circle, inversion w=1/z parametrizes |w|=1/r clockwise. There are exactly 1+2 floor(1/(pi r)) simple zeros of sin w in that disc when the boundary avoids them. The argument principle therefore gives degree -M(1+2 floor(1/(pi r))) for sin(1/z)^M on the original positive circle. Conjugation reverses the sign; the positive multiplier does not change it. This proves (3). In the source's sentence calling M times the count "that number", the intended quantity is the degree with multiplicity, as its correct displayed formula states.

Finally, the complex field h=conjugate(sin(1/z)^M) has zero real divergence by the Cauchy-Riemann equations. For F(r)=exp(-1/r^2),

    div(Fh)=grad F.h.

At positive real r with sin(1/r)=1, h=(1,0), so

    div f_M(r)=2 exp(-1/r^2)/r^3,
    |div f_M(r)|/|f_M(r)|=2/r^3.

Such radii occur arbitrarily near zero. This proves both the failure of divergence freedom and the failure of a bounded first-order divergence estimate. The earlier independent draft here used M=1 and exp(-1/r^4), which has the same degree and a stronger flat multiplier; the submitted LIT301 family (2) includes arbitrary finite order M and makes the limitation more explicit.

## 5. Scope of the result and the refuted inference

The exact F consequence is the local order, index and annular dichotomy of Sections 1-3. A bound on d would exclude accumulating off-orbit zeros, not the possibility that Gamma is the only zero orbit near itself. Smooth flatness, negative finite indices off the center, and even vanishing first derivatives at those zeros do not alone yield such a bound, as (2) proves.

The counterexample supplies no divergence-free carrier, scalar S, pressure P, or Euler profile. It does not even satisfy the bounded divergence relation identified in Section 4. Thus no inference retaining that differential information is refuted. Whether those additional equations bound the degrees remains open. Existence or exclusion of F, its positive-trace endpoint, a global tail realization and the unrestricted decaying rotating-profile conjecture all remain open.

The quantifiers are local, for every fixed 0<c<1/2 and every real omega. Local constants may depend on these parameters and on the zero under consideration. No pressure normalization, boundary at infinity, complete flow, extra decay or unproved uniformity has entered the argument.

## 6. Dependencies and verification

The exact source LIT301 is retained as in the team records with its hash in the team records. All five source sections were read. The entire seven-section literature comparison, the four-section C66 source, and the already reconstructed LIT288 and C66 audit proofs supply the stated dependencies. The local Carleman theorem is inherited from its confirmed proof; it is not claimed as a newly executed calculation.

No numerical computation or formal build is needed for the new argument. The pass criteria are the exact local zero order and orientation, finite-annulus identity (1), derivative bounds, degree formula (3), and explicit divergence failure. All are established above analytically. The source correctly requires no numerical computation.

Existing configured model coordinator and theory agents were notified through this agent's notes, and their already confirmed C66 input is used at its exact scope. Their provider execution is not independently attested. No new model client, remote computation, or agent was used. The final postread evidence and individual ledger entries record the exact confirmed and open scopes. No global theorem is implied.
