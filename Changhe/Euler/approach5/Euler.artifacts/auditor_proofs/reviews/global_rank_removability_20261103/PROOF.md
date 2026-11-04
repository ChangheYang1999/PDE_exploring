# Weighted removability of a globally ranked twisted tail

Status: CONFIRMED at the exact conditional or countertest scopes in A593, A594. Full independent proof postread completed. The unrestricted campaign conjecture is not proved.

## 1. Statement, notation and dependencies

Let 1/3<c<1/2, omega be any finite real number, p=(1-c)/c in(1,2), a=1-2c, beta=(p-1)/(2p), Jx=(-x2,x1,0), A=cI-omega J, Q_t=exp(omega tJ), T_t=exp(tA)=exp(ct)Q_t^T, and D=R3 minus{0}. Suppose S is real C1 on D. Require its exact homogeneity S(T_t x)=exp(-2(1-c)t)S(x) for every real t. At each zero require one of the following charts, with constants and exponents allowed to vary:

- A C1 diffeomorphism x=Phi(z) from a product box, with bounded DPhi and inverse on smaller boxes, such that C^-1 rho^m<=|S(Phi(z))|<=C rho^m, rho=|(z1,...,zj)|, j in{1,2}, m>=1 and eta=m beta<j. The zero set is exactly the central surface or curve.
- A chart of the same regularity such that C^-1 product_(i=1)^j |z_i|^m_i<=|S(Phi(z))|<=C product_(i=1)^j |z_i|^m_i, j in{1,2,3}, m_i>0 and eta_i=m_i beta<1 for every i. The zero set is exactly the union of the coordinate planes.

An empty zero set is allowed. The scalar S identically zero is excluded from these chart hypotheses. Arbitrary flat, tangent or accumulating zero sets do not qualify. On any compact set a finite number of charts suffices.

Weighted theorem. Let Y be locally Lipschitz on D, with continuous actual distributional curl Z, div Y=0 distributionally, and

    Y(T_t x)=exp(-(1-c)t)Q_t^T Y(x),
    grad S cross Y=(S/beta)Z.

Then Y=0.

Global-rank corollary. Let V be C1, divergence free, with the same velocity homogeneity; write W=curl V, k=(Ax).V and E=grad k. If W.grad S=0 and E cross grad S=0 throughout D, then V=0. No pressure equation, axisymmetry, global E=0 or extra helicity premise is needed in this standalone statement.

For the normal-crossing charts, rank only on {W!=0}, together with W.grad S=0 everywhere, implies the weaker conclusions: each vortical point has k!=0 and S!=0, and E=0 at any point implies V=0 there. This is a localization theorem, not global V=0. The analogous radial curve localization with additional exponents is recorded separately in A567-A568; it is not inferred from the larger radial chart scope above.

Dependencies: elementary weak product/chain rules and Poincare inequality; the elementary potential gluing argument below; completed weighted-energy signed-solution regularity in Fabes, Jerison and Kenig, The Wiener test for degenerate elliptic equations, Ann. Inst. Fourier32(3)(1982),151-182, Definition1.3 and(1.7)-(1.8), printed154-156. The exact source and its imported FKS dependency are recorded in the team records and the literature agent's source-scope file. The full FKS regularity proof is imported, not independently reproved.

## 2. The actual closed field and its potential

Put b=|S|^beta, disregarding values on the null nodal set. The charts show local integrability of b and b^-1. They also give b^-q locally integrable for some q>1 on each compact set: choose q eta<j in a radial chart and q eta_i<1 in a crossing chart. Thus G=b^-1Y belongs to local Lq. The regularized product rule, including the actual curl of Y, is

    curl[(S^2+epsilon^2)^(-beta/2)Y]
      =epsilon^2(S^2+epsilon^2)^(-beta/2-1)Z.

The right side tends to zero almost everywhere and is bounded by b^-1|Z|; the regularized field is bounded by b^-1|Y| and converges locally in L1 to G. Dominated convergence proves curl G=0 throughout D in distributions. This explicitly excludes nodal surface, curve or intersection curl. Closedness off the nodes alone would not prove it.

On a ball whose closure lies in D, mollify G using a slightly larger ball. Integrate the smooth closed fields and fix the potential mean on the smaller ball. Poincare and gradient convergence give a W1q potential. On overlaps these potentials differ by constants. The domain D is simply connected: any loop contracts, and a subdivision of its compact contracting homotopy into such balls makes the overlap constants telescope. The potentials glue to a single real weak potential psi with

    grad psi=G, div(b grad psi)=div Y=0.

The last equality is initially distributional. To apply the primary regularity theorem, completion by Lipschitz functions in the weighted norm is still needed.

## 3. Completion on a surface or a radial curve

Write u=psi composed with Phi. The weak chain rule gives |Du|<=C rho^-eta. Off the nodes G is continuous, so u has a C1 representative there. All constructions below use smaller boxes and harmless outer cutoffs.

For a surface, eta<1. Integrating in the normal variable gives one-sided traces with error at most C rho^(1-eta). Lift any two nearby tangential points to normal height comparable to their distance, use the derivative bound there, then return to the traces. This proves a common Holder modulus of exponent1-eta on each trace. Ordinary W1q absolute continuity on almost every normal line forces the two traces to coincide almost everywhere, hence everywhere by that continuity. The representative is therefore continuous through the surface.

Interpolate u linearly between the faces at normal heights plus/minus epsilon, leaving it unchanged outside. The face tangential derivatives are bounded by C epsilon^-eta; the two face values differ by at most C epsilon^(1-eta). Thus the entire interpolated derivative in the band is bounded by C epsilon^-eta. The weighted derivative error is at most

    C integral_0^epsilon s^eta
                       [epsilon^(-2eta)+s^(-2eta)]ds
      <=C epsilon^(1-eta).

The function error tends to zero as well. Each approximant is locally Lipschitz, proving the required completion.

For a curve, eta<2. Integrate in the normal radial variable from a fixed positive radius; compactness of its circle and of the tangential base supplies a uniform starting bound. Thus |u|<=C F_eta(rho), where F_eta is1 for eta<1, 1+|log rho| for eta=1, and1+rho^(1-eta) for eta>1. The weighted derivative integral is bounded by C integral rho^(1-eta)drho, and the function integral is finite. A radial cutoff vanishing below epsilon and equal to1 above2epsilon gives derivative error O(epsilon^(2-eta)) from Du. Its cutoff-derivative error is bounded by C epsilon^eta F_eta(epsilon)^2. This tends to zero: respectively like epsilon^eta, epsilon(1+|log epsilon|)^2, or epsilon^(2-eta). The function error also tends to zero. The cut-off functions are locally Lipschitz. No unproved boundedness at a curve is used.

## 4. Completion at transverse intersections

For a crossing chart write w(z)=product |z_i|^eta_i, so b composed with Phi is comparable to w and |Du|<=C/w. Choose a base slice in each orthant with all normal coordinates at a fixed small nonzero magnitude. Values on these finitely many compact slices are bounded. Move the normal coordinates to the desired point successively. Since each integral integral_0^rho0 s^-eta_i ds is finite, this gives

    |u(z)|<=C [1+sum_(i=1)^j product_(l<i)|z_l|^-eta_l].

Consequently integral w|Du|^2 and integral w|u|^2 are finite on a smaller box. The derivative integrand is bounded by C/w. In a squared term of the function bound, each prefix exponent after multiplying by w is -eta_l and each remaining exponent is +eta_l, all integrable. No continuous representative at an intersection has yet been assumed.

Here is a direct completion proof. Take a nonnegative smooth approximate identity rho_epsilon supported in a cube of side2epsilon and bounded by C epsilon^-3. Extend the product weight to R3. Then

    w(x) (rho_epsilon*w^-1)(x)<=C0

uniformly in epsilon and almost every x. For each factor, if |x_i|>2epsilon the coordinate is comparable throughout the interval. Otherwise integral_(x_i-epsilon)^(x_i+epsilon)|y_i|^-eta_i dy_i<=C epsilon^(1-eta_i), and |x_i|^eta_i<=C epsilon^eta_i. Multiplication gives the displayed bound; coordinates absent from w contribute1.

Cauchy-Schwarz and Tonelli now give

    |rho_epsilon*f(x)|^2
       <=[rho_epsilon*(|f|^2w)](x)[rho_epsilon*w^-1](x),
    ||rho_epsilon*f||_L2(w)<=sqrt(C0)||f||_L2(w).

Continuous compactly supported functions are dense in L2(w), since w dx is a locally finite regular Borel measure. Their mollifications converge uniformly on a fixed compact set. The uniform operator bound therefore gives mollifier convergence for every f in L2(w).

For a smooth cutoff chi interior to the chart, chi u and all its weak derivatives are in L2(w), and Cauchy-Schwarz with w^-1 locally integrable puts them in ordinary L1. Extending chi u by zero gives W1,1 with compact support. Its mollifications and their derivatives converge in L2(w) by the preceding argument. Thus smooth approximation holds for the entire function and derivative norm, which proves completion.

## 5. Local A2, regularity and additive homogeneity

The transformed coefficient for div(b grad psi)=0 is

    b(Phi(z)) |det DPhi(z)| DPhi(z)^-1 DPhi(z)^-T.

It is real symmetric measurable and bounded above and below by fixed positive multiples of rho^eta I or w I on a smaller chart. Function and gradient norms transform equivalently. Pulling back smooth approximants gives C1, locally Lipschitz approximants in the original coordinates.

For the radial normal weight rho^eta, the A2 averages are bounded for |eta|<j: balls far from the central subspace have comparable weight throughout; for nearby balls, integrate in the j normal variables to get averages at most C R^eta and C R^-eta. For the product weight the averages over cubes factor into one-dimensional power-weight averages, bounded for |eta_i|<1. Enclose each ball in a cube with comparable volume. Multiplication by uniformly bounded positive factors preserves the bound. A bi-Lipschitz chart preserves the local A2 estimate by the Jacobian bounds and containment in balls of comparable radius. Therefore b is locally A2 on D.

The distributional equation also holds for completed weighted-energy tests. To justify this passage independently of psi's approximations, mollify any compactly supported Lipschitz test: its gradients converge almost everywhere with a common bound, and local integrability of b gives weighted convergence. Then use the definition of the completion and Cauchy-Schwarz. The primary Definition1.3 and signed estimates(1.7)-(1.8) apply. They give a continuous representative of psi across every node. Nonnegativity is needed for the separate Harnack estimate(1.9), not for the continuity used here.

The exact degrees give b(T_t x)=exp(-at)b(x) and

    G(T_t x)=exp(-ct)Q_t^T G(x)=T_t^(-T)G(x).

For fixed t the weak chain rule makes psi composed with T_t minus psi have zero weak gradient on connected D. It is constant, and continuity makes the identity pointwise. Its constants form a continuous additive function of t. Hence

    psi(T_t x)=psi(x)+gamma t

for a real gamma. Moving x to the unit sphere yields |psi(x)|<=C(1+|log|x||). The proof does not prematurely set gamma=0.

## 6. A2 and energy at the missing origin

Put d=p-1 in(0,1). The weight has ordinary radial degree -d up to an angular rotation: b(r theta)=r^-d b(R_r theta). Integrate on a fixed annulus using Tonelli and invariance of spherical measure. Its already established b and b^-1 integrability implies

    B_plus=integral_S2 b(theta)dtheta in(0,infinity),
    B_minus=integral_S2 b(theta)^-1 dtheta in(0,infinity).

This uses no separate angular trace theorem. Exact radial integration gives

    integral_(|x|<R)b=B_plus R^(3-d)/(3-d),
    integral_(|x|<R)b^-1=B_minus R^(3+d)/(3+d).

If |x0|<=2R, enclose B(x0,R) in B(0,3R); its two averages are bounded by C R^-d and C R^d. If |x0|>2R, use T_t to put the center on the unit sphere. Its radius becomes less than1/2; the product of averages is unchanged. On a slightly larger compact annulus, a finite cover gives uniform local A2 bounds for all sufficiently small balls. Larger balls have volume bounded below and weight integrals bounded by fixed annular integrals. Thus b, with arbitrary null-set assignments, is globally A2 on R3. The constants may depend on omega; the conclusion holds separately for every finite omega.

The velocity homogeneity bounds |Y|<=C r^-p. Its square divided by b has degree -(p+1), with finite spherical integral since Y is bounded on the sphere and B_minus is finite. Therefore

    integral_(r<epsilon)b|grad psi|^2
       =integral_(r<epsilon)|Y|^2/b<=C epsilon^(2-p).

The weighted function integral is finite by the logarithmic bound and the b-volume formula. Also integral_(r<epsilon)|G|<=C epsilon^2, since G has degree-1 and integrable angular norm.

Extend psi across0 as a locally integrable function. In its weak derivative identity an inner radial cutoff introduces a term bounded by C epsilon^2(1+|log epsilon|), which vanishes. The remaining G term converges in L1. Thus grad psi=G globally. The analogous divergence cutoff gives

    epsilon^-1 integral_(epsilon<r<2epsilon)|Y|
       <=C epsilon^(2-p)->0.

Hence div(b grad psi)=0 on all R3, with no hidden point source.

Let chi_epsilon vanish below epsilon and equal1 above2epsilon. The gradient norm of chi_epsilon psi minus psi is at most

    C epsilon^(2-p)(1+|log epsilon|)^2,

using the small-ball gradient estimate and epsilon^-2 times the b-volume of the annulus. It tends to zero because p<2. The function error tends to zero too. For fixed epsilon, Sections3-4 and a finite partition of unity approximate the cut-off potential by Lipschitz functions on a fixed ball. A diagonal choice proves completion across0. Weighted tests extend as in Section5. The primary signed-solution theorem now gives continuity at0.

As t tends to minus infinity, T_t x tends to0. The identity psi(T_t x)=psi(x)+gamma t and continuity first force gamma=0, then force psi(x)=psi(0). Thus G=0 almost everywhere, Y=bG=0 almost everywhere, and continuity of Y gives Y=0 everywhere. This proves the weighted theorem.

## 7. Global rank and crossing localization

The homogeneity of C1 V gives DV Ax=-[(1-c)I+omega J]V. The elementary derivative identity for k yields

    Ax cross W=E-A^T V-DV Ax=aV+E,
    Ax.grad S=-2(1-c)S.

Cross the first identity on the left with grad S. The hypotheses W.grad S=0 and grad S cross E=0 remove the other terms, leaving a grad S cross V=2(1-c)S W. This is the weighted theorem's equation and proves the global-rank corollary.

For normal-crossing localization assume rank only on the vortical set. On any small connected region where W and S are nonzero, grad S is nonzero by its homogeneity. Rank and contraction with Ax give

    grad k=(beta k/S)grad S,
    k/|S|^beta is spatially constant.

At a zero of S with W!=0, choose its entire crossing chart inside that set. Each orthant has one constant C_sigma. Continuity first gives k=0 on all its nodal faces. Hold the other normal coordinates fixed and nonzero while approaching one face z_i=0. Since k is C1, |k|<=C|z_i|, while |S|^beta>=C'|z_i|^eta_i. Thus |C_sigma|<=C''|z_i|^(1-eta_i)->0. All constants vanish, including across intersections. So k=0 on the whole chart.

On a connected vortical component C, a zero of k propagates by an open-and-closed argument, using the constant law away from S0 and the preceding charts at S0. It gives k=E=0 throughout C. The same conclusion starts from any S0 point in C. At its boundary, W=0 and E=0 by continuity; the vector identity forces V=0 there. Extend Y=V on C and Y=0 elsewhere in D. This is locally Lipschitz: for points on opposite sides use the first exit of the joining segment, where V=0, and a bound for DV. Its derivative equals DV on C and0 almost everywhere on the complement; on the boundary a Lipschitz function has zero derivative almost everywhere on its zero set. Consequently div Y=0 and its actual curl is Z=W on C and0 outside. The curl is continuous because W=0 on the boundary.

The spiral preserves C, since it preserves W!=0 and each time path is connected. The extension has exact velocity homogeneity. Globally Ax cross Z=aY, Z.grad S=0, so grad S cross Y=(S/beta)Z. The weighted theorem applies and gives Y=0, contradicting the nonzero curl on C. No vortical point can have k0 or S0. If E=0 and W!=0, the homogeneity Ax.E=-ak would give the already excluded k0. If E=0 and W=0, the vector identity gives V0 directly.

## 8. Scope

This confirms an entire-space conclusion only under global rank. Rank merely on the actual vortical set supports localization, not an automatic extension through an open irrotational region. Original exterior-vorticity density can supply global tail rank by the separate proof in the team records. All-zero nodal geometry remains an additional hypothesis.

For target2/5<c<1/2 one has beta<1/6. Hence transverse normal crossings with every surface order at most6 satisfy the strict exponent conditions. This does not cover arbitrary analytic zero sets, tangencies, flat nodes or arbitrary curves. The radial curve theorem allows eta<2, whereas the crossing theorem requires every face eta_i<1. At equality nodal curl may survive; A548 supplies a nonprofile axial countertest. At p=2 the origin energy argument fails. Neither endpoint failure is claimed to prove existence of an Euler counterexample.

No symbolic, numerical, formal or remote computation is used. The source proof and all new estimates have been independently reconstructed. Verification and model-comparison records are in the team records.
