# Controlled nodal surfaces and curves for a degenerate tail

Status: CONFIRMED as A547-A548 after complete source comparison and independent postread. The exact weighted Harnack statement is an imported primary theorem, not a new proof. The curve-threshold countertest is kinematic and explicitly fails Poisson.

## 1. Exact hypotheses

Let 2/5<c<1/2, omega be any finite real number, p=(1-c)/c in(1,3/2), a=1-2c, beta=a/[2(1-c)]=(p-1)/(2p) in(0,1/6). Set J(x1,x2,x3)=(-x2,x1,0), A=cI-omega J, Q_t=exp(omega tJ), D=R3 minus{0}. Suppose V in C1(D;R3), S in C1(D;R), and W=curl V satisfy

    div V=0, Ax cross W=aV, W.grad S=0,
    V(exp(tA)x)=exp(-(1-c)t)Q_t^T V(x),
    S(exp(tA)x)=exp(-2(1-c)t)S(x), for every real t.   (1)

For every x0 with S(x0)=0, suppose a C1 diffeomorphism x=Phi(z) maps a product neighborhood of0 onto a neighborhood of x0, with DPhi and its inverse bounded on a smaller product, and

    C0^-1 rho^m <= |S(Phi(z))| <= C0 rho^m,
    rho=|z_normal|, k=dim z_normal in{1,2},
    m>=1, eta=m beta<k.                              (2)

The constants and k,m may vary with the chart. Thus each zero has a neighborhood on which the zero set is exactly one C1 surface or one C1 curve. No intersections, singular strata, infinitely flat zeros or arbitrary critical sets are allowed. An empty zero set is allowed.

Then V=0. Every surface order m<=6 and every curve order m<=12 satisfies the strict inequalities for the stated open c interval. If V is nonzero under (1), some zero on every centered sphere must fail (2).

No pressure equation is needed for this theorem. Application to a full Euler profile needs the separately proved natural-tail regularity and compatibility, S=P2-|V|²/2, and E=-aV+Ax cross W=0 on ALL of D. A proper open cone of E=0 does not supply this hypothesis.

## 2. The integrating factor extends as a closed field

Taking dot product with Ax in (1) gives Ax.V=0. Differentiating scalar homogeneity gives Ax.grad S=-2(1-c)S. The vector triple product, with W.grad S=0, therefore gives

    grad S cross V=(S/beta)W.                        (3)

For epsilon>0, elementary product differentiation yields

    curl[(S²+epsilon²)^(-beta/2)V]
      =epsilon²(S²+epsilon²)^(-beta/2-1)W.            (4)

The zero set is null, by its local manifold charts and a countable subcover. On a chart the normal volume element is comparable to rho^(k-1)drho times angular and tangential measure. Since eta<k,

    |S|^-beta (|V|+|W|)<=C rho^-eta

is integrable on compact subsets. In fact G=|S|^-beta V belongs locally to Lq for every 1<q<k/eta on that chart. A finite chart cover gives one q>1 on each given compact set, with no common exponent claimed on all D.

The right side of (4) is bounded almost everywhere by |S|^-beta |W| and tends to0 off the null zero set. The regularized fields tend to G in local L1 by the same domination. Testing (4) and passing to the limit proves

    curl G=0 in distributions on D.                 (5)

This explicitly excludes any curl measure on the nodal set. Merely checking curl G=0 off that set would be insufficient.

On a ball compactly contained in D, mollify G on a larger ball, integrate each smooth closed field and fix its potential's mean. The Poincare inequality gives convergence in W1q on the smaller ball. Local potentials differ by constants on connected overlaps. The domain D is simply connected: a homotopy of any loop to a point can be subdivided into finitely many such balls, and their additive constants cancel around the small loops. Thus these potentials glue to a single weak potential psi on D with

    grad psi=G, psi in W1q locally.                   (6)

Here q>1 may depend on the compact subset. The field G is continuous off S=0, so psi has a C1 representative there. There is no assumption that the complement of the zero set is simply connected.

In a smaller chart write u=psi composed with Phi. The weak chain rule gives

    |Du|<=C rho^-eta almost everywhere,              (7)

and the bound is classical off rho=0. Put b=|S|^beta. From b grad psi=V and div V=0,

    div(b grad psi)=0 in distributions.              (8)

The exact energy completion required by weighted Harnack is verified next.

## 3. Surface charts: trace and approximation

For k=1, eta<1. Integrating (7) on positive and negative normal segments gives traces u_+(z') and u_-(z'), with uniform error C|s|^(1-eta) on smaller horizontal cubes. To compare two trace values a distance d apart, lift to height d, use the horizontal derivative bound C d^-eta and add the two vertical errors. Each trace is continuous, with modulus at most C d^(1-eta).

The W1q function u is absolutely continuous on almost every normal line across the whole chart. Its derivative is bounded by the integrable majorant C|s|^-eta, so its two traces agree almost everywhere. Continuity makes them agree everywhere. This supplies a continuous and locally bounded representative across the surface.

For a concrete approximation leave u unchanged outside |s|<epsilon and interpolate linearly between its values at s=-epsilon and s=epsilon inside. Call the result u_epsilon. Its normal and tangential derivatives in the band are bounded by C epsilon^-eta, and it is Lipschitz on a smaller cube for each fixed epsilon. Its uniform error is C epsilon^(1-eta), and

    integral |s|^eta |Du_epsilon-Du|²
      <=C integral_0^epsilon s^eta
                         (epsilon^-2eta+s^-2eta)ds
      <=C epsilon^(1-eta) ->0.                       (9)

The weighted function norm also converges. Thus u is in the completion of Lipschitz functions for the local norm integral |s|^eta(|u|²+|Du|²), with its actual weak gradient.

## 4. Curve charts: completion before continuity

For k=2, 0<eta<2, no ordinary Sobolev continuity is asserted yet. Fix a positive normal radius rho0 inside a larger chart. Values of u on that cylinder, over a smaller compact tangential interval, are bounded because the cylinder is compact and avoids the zero set. Integrate (7) radially from rho0, uniformly in normal angle and tangential position. After absorbing the chart size into the constant,

    |u|<=C F_eta(rho),
    F_eta(rho)=1                    for eta<1,
              1+|log rho|          for eta=1,
              1+rho^(1-eta)        for eta>1.         (10)

Normal polar integration proves

    integral rho^eta |Du|² <= C integral_0^rho0 rho^(1-eta)drho <infinity,
    integral rho^eta |u|² <= C integral_0^rho0 rho^(1+eta)F_eta(rho)²drho <infinity.   (11)

Let chi be a smooth radial cutoff with chi=0 on[0,1], chi=1 on[2,infinity), and bounded derivative. Set u_epsilon=chi(rho/epsilon)u. This is Lipschitz on each smaller chart: it vanishes near the curve, and u,Du are bounded on compact sets a positive distance from the curve. The weighted function error tends to zero by (10)-(11). The part of the gradient error involving Du is O(epsilon^(2-eta)). The cutoff derivative costs at most

    C epsilon^-2 integral_epsilon^(2epsilon)
                         rho^(1+eta)F_eta(rho)²drho
      <=C epsilon^eta F_eta(epsilon)² ->0.            (12)

For eta<1 the last bound is C epsilon^eta; for eta=1 it is C epsilon(1+|log epsilon|)²; for 1<eta<2 it is C epsilon^(2-eta). All tend to zero. This gives the required weighted completion even when (10) by itself permits unbounded values. The weak potential was already constructed across the curve in Section2. No separate arbitrary values or a jump are inserted on the curve.

## 5. The weighted regularity input

Changing variables in (8) gives the symmetric measurable coefficient matrix

    C(z)=b(Phi(z)) |det DPhi(z)| DPhi(z)^-1 DPhi(z)^-T.   (13)

It is comparable above and below to w(z)I with w=rho^eta. The weight is A2 for |eta|<k. To check this, a ball whose distance from the normal zero plane exceeds twice its radius has w and its reciprocal comparable to their central values. For any other ball of radius R, normal polar integration bounds their averages by C R^eta and C R^-eta. The two integrals converge because -k<eta<k. Their product is uniformly bounded. A bounded measurable elliptic factor can be set equal to the identity outside the smaller chart, preserving the global comparison to wI while leaving the local equation unchanged.

Sections3-4 prove membership in the weighted H1,2 completion of Lipschitz functions. For compactly supported Lipschitz tests, ordinary mollification after extension gives weighted convergence: the gradients remain bounded, converge almost everywhere along a subsequence, and w is locally integrable. The equation initially valid for smooth tests therefore extends to Lipschitz tests and then, by Cauchy-Schwarz, to the compactly supported weighted completion. These are the weak-solution hypotheses of the imported theorem.

The precise source is Fabes, Jerison and Kenig, The Wiener test for degenerate elliptic equations, Annales de l'Institut Fourier32(3)(1982),151-182, DOI10.5802/aif.883. The retained actual PDF was read at printed151-156: measurable symmetric coefficients comparable to an A2 weight on152; weighted Lipschitz completion and Definition1.3 on154-155; local Holder continuity on155 and Harnack(1.9) on156. The underlying proof attributed to Fabes, Kenig and Serapioni, Comm. PDE7(1)(1982),77-116, Section2.3.8, is imported and has not been independently reconstructed here. The companion source audit is in the team records relative to the agent root.

The imported local regularity theorem now gives a continuous representative for psi through the curve charts as well as the surface charts. Representatives on overlaps agree almost everywhere and hence everywhere. At a zero-free point the coefficient is locally bounded above and below, so the same result uses reference weight1.

## 6. A global maximum forces V=0

Equations (1) and (6) give Ax.grad psi=0 almost everywhere. Differentiate the pullback by the smooth linear flow in distributions, using local W1q approximation on the compact flow cylinder. For each fixed t,

    psi(exp(tA)x)=psi(x) almost everywhere.

Continuity upgrades this to every x for that t; t was arbitrary. The radius of exp(tA)x is exp(ct)|x|, so every point moves to the unit sphere. The continuous function psi attains a finite global maximum M on that compact sphere and thus on D.

The function M-psi is a nonnegative continuous weak solution of (8). At a maximum point use a small doubled ball, in nodal coordinates if needed. Harnack gives its inner supremum at most a constant times its inner infimum, which is zero. Therefore the maximum set is open. It is also nonempty and closed in connected D. Hence psi is constant, and V=b grad psi=0 almost everywhere and then everywhere by continuity.

Exact homogeneity transports any chart satisfying (2) along exp(tA), with the same exponent and only a changed multiplicative constant. It transports failure as well by the inverse map. A nonzero field must therefore have a failed zero on every centered sphere. This is not a conclusion about which geometry an Euler tail actually has.

## 7. Exact countertest at the curve threshold

The strict bound eta<2 for a curve cannot be replaced by eta<=2 in this standalone kinematic theorem. Take omega=0, p=(1-c)/c, nu=1/beta=2p/(p-1)>6, r=|x|, rho=(x1²+x2²)^(1/2), w=rho²/r², and K>0. Define

    V=r^(-p-1)Jx, S=-K r^(-2p)w^nu.                 (14)

The field V is smooth on D. The scalar S is C1 there, and is smooth if nu is an integer; c=3/7 gives p=4/3 and nu=8. Its zero set in D is exactly the x3 axis. Near each point of that axis |S| is comparable to rho^(2nu), so m=2nu and eta=2 at every zero.

The field V is divergence-free, tangent to centered spheres and homogeneous of degree-p. Differentiating x.V=0 gives x cross curl V=(p-1)V, and c(p-1)=a. Thus the degenerate identity holds. With z=cos theta, F(z)=1-z² and s=sin theta,

    V=r^-p s e_phi,
    W=r^(-p-1)[-F'(z)e_r+(p-1)F(z)e_theta/s].

Substitution of S=-K r^-2p F^nu gives W.grad S proportional to [2p-(p-1)nu]F'F^nu=0. All identities (1) hold, including on the axis by continuity. Yet V is nonzero.

Off the axis the integrating factor is exactly

    G=|S|^-beta V=K^-beta e_phi/rho.                 (15)

It is locally Lq for every q<2, but

    curl G=2pi K^-beta delta_(x1=x2=0) e3             (16)

in distributions on D. Indeed remove a cylinder rho<epsilon when testing against a compact smooth vector field. Classical curl is zero outside. The inner normal is -e_rho; integration by parts gives boundary integrand K^-beta phi3/epsilon. Multiplying by epsilon dtheta dx3 and letting epsilon tend to zero gives (16). The support avoids the deleted origin. The same coefficient is the circulation around any positive small circle linking the axis.

Even the weighted field energy is locally finite: b|G|²=K^-beta r^(-p-1) is bounded on compact subsets of D. Thus local Lq integrability and finite weighted energy do not justify a global potential. At eta=2 the domination in (4) and the A2 condition fail, and the line curl survives.

## 8. The countertest fails the pressure equation explicitly

To prevent conflation with an actual Euler tail, prescribe K so its assigned pressure Pstar=S+|V|²/2 fails Poisson. Put

    T0=integral_(S2)|V|²=8pi/3,
    I_nu=2pi integral_-1^1(1-z²)^nu dz>0,
    K=1+(p+1)T0/(2p I_nu).                           (17)

If a homogeneous pressure of degree-2p satisfied -Delta Pstar=partial_i partial_j(V_i V_j), testing against a smooth radial chi supported in an annulus would give, for P0=integral_(S2)Pstar,

    -P0 integral r^(2-2p)(chi''+2chi'/r)dr
       =T0 integral r^(1-2p)chi'dr.

Integrating twice by parts gives P0=-T0/(2p), since p>1. Consequently

    integral_(S2)S=-(p+1)T0/(2p).                   (18)

But (14),(17) give the left side equal to the right side minus I_nu. Poisson therefore fails. The field is also singular at the origin. This example is neither a full smooth Euler profile nor a counterexample to the rotating conjecture.

More generally for a twisted homogeneous tail satisfying Poisson, with R0=integral V_r² and T0=integral|V_T|², the same annular test yields

    integral_(S2)S=[(2-3p)R0-(p+1)T0]/(2p).          (19)

This is strictly negative for a nonzero tail. It supplies a negative point, while the zero-free special case of Sections2-6 independently supplies a zero. It does not supply a positive point, sign change or a nodal chart.

## 9. Verification and limits

All estimates and exact countertest identities were checked analytically; no computation is needed. The theoretical question tested by (14)-(18) is whether the non-strict curve threshold can replace the strict one without Poisson. The nonzero example answers no, and the explicit spherical mean identifies the missing full-Euler condition.

The complete LIT142 source and the surface reconstruction were read. The source and exact primary weighted-Harnack audit are retained by hash. Existing configured-model coordinator and theory agents have the focused nodal-completion comparison request; no successful focused model reply has yet been received. Established natural-tail premises have actual model reviews, but they are not a substitute for the explicit nodal estimates above. No new client or delegated computation was used.
