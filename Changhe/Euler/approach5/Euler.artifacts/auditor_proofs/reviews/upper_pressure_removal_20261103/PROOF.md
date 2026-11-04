# Upper scalar comparison and pressure regularity

Status: CONFIRMED A2020-A2026 after independent the literature agent and configured model coordinator reviews, followed by a complete mathematical recheck. This strengthens LIT267, CO67 and LIT278 at the exact hypotheses below. A2027 records the unresolved derivation of those hypotheses from bare decay.

## 1. Local removal theorem

Fix 2/5<c<1/2 and set

    eta=(1-2c)/(2-2c), rho=c/[2(1-c)], gamma=2rho,
    alpha0=2/c-4.

Thus rho=1/2-eta lies in (1/3,1/2), gamma=1-2eta lies in (2/3,1), and alpha0 lies in (0,1). Let alpha0<alpha<1. Suppose G is open in R3, V belongs to C_loc^(1,alpha)(G;R3), P is continuous on G, and

    Delta P=-tr((DV)^2) in distributions,
    E=|V|^2, S=P-E/2,
    E<=K|S|.                                            (1.1)

The last bound is local: on each relatively compact neighborhood there is a finite constant K>0 for which it holds. No lower comparison is assumed. Define beta=|S|^(-eta)V where S!=0 and beta=0 where S=0. Then beta is continuous and belongs locally to W^(1,t) for every 1<=t<1/(1-rho). Its weak derivative vanishes almost everywhere on {S=0}. In particular, classical zero curl on {S!=0} implies distributional zero curl throughout G.

Interior Poisson regularity gives P in C_loc^(2,alpha). To justify this with the stated hypotheses, localize the Holder continuous source -tr((DV)^2), form its Newtonian potential, and subtract it from P. The difference is distributionally harmonic, hence smooth on a smaller ball. Therefore S is C_loc^(1,alpha) and

    DS=DP-(DV)^T V,
    |P|<=|S|+E/2<=(1+K/2)|S|.                           (1.2)

The second inequality is the useful pressure bound. It uses only the upper comparison.

The scalar-root input is Ghisi and Gobbino, arXiv:1107.2694v2, Theorem 2.3. For 0<sigma<1, a real function f of local class C^(k,delta), with k>=1, 0<delta<=1 and k+delta=1/sigma, has a continuous signed sigma power with gradient locally in weak L^(1/(1-sigma)). Its gradient is consequently in every strictly smaller local L^t space. Off {f=0} the chain rule identifies its absolute value with sigma |f|^(sigma-1)|Df|. The Sobolev level-set property makes the gradient zero almost everywhere on {f=0}. The exact statement, Theorem 2.2 on which it rests, and the full higher-dimensional slicing proof were read in the retained primary manuscript. The final exponent typo in the slicing display does not affect the theorem or its preceding distribution-function estimate.

Apply this input to P with sigma=rho and (k,delta)=(2,alpha0). Apply it to each V_i with sigma=gamma and (k,delta)=(1,alpha0/2). The assumed alpha exceeds both required Holder exponents. On a fixed smaller neighborhood put

    H_P=|P|^(rho-1)|DP| on {P!=0}, and zero on {P=0},
    H_i=|V_i|^(gamma-1)|DV_i| on {V_i!=0}, and zero elsewhere.

They are in L^t for every t<1/(1-rho). The H_i in fact have the larger range t<1/(1-gamma). These estimates are applied to pressure and velocity components; no fractional-power estimate for S is needed.

For epsilon>0 let beta_e=(S^2+epsilon^2)^(-eta/2)V. On {S!=0}, with h=|S|, its classical derivative satisfies

    |D beta_e|
      <=h^(-eta)|DV|+eta h^(-eta-1)|V||DS|
      <=(1+eta K)h^(-eta)|DV|
          +eta sqrt(K)h^(rho-1)|DP|.                    (1.3)

For the second line insert DS from (1.2), use E<=Kh in the quadratic term, and use |V|<=sqrt(Kh) in the pressure term. The estimate is uniform in epsilon.

The first term on the last line of (1.3) is at most

    K^eta sum_i |V_i|^(-2eta)|DV_i|=K^eta sum_i H_i     (1.4)

almost everywhere: for a nonzero component, |V_i|^2<=Kh and the exponent is negative. On a zero set of a C1 component its derivative vanishes almost everywhere, so that component contributes zero. In particular, this argument does not assume that V vanishes only when S vanishes.

For the pressure term, (1.2) and rho-1<0 give on {P!=0}

    h^(rho-1)|DP|
      <=(1+K/2)^(1-rho)|P|^(rho-1)|DP|.                 (1.5)

On {P=0,S!=0}, DP=0 almost everywhere, so the same bound holds with H_P=0. On {S=0}, (1.1) gives V=0 and DV=0 almost everywhere. In the exact formula for D beta_e its other term contains SV and is zero there. Thus on the full neighborhood

    |D beta_e|<=C(c,K)(sum_i H_i+H_P)                    (1.6)

almost everywhere, independently of epsilon. All negative powers in (1.4)-(1.5) are used only off their zero sets; those sets have already been treated by the level-set derivative property.

The estimate |beta|<=sqrt(K)|S|^rho proves continuity across S=0. The same bound and a split into h<=epsilon and h>epsilon give uniform local convergence beta_e->beta, with error at most C epsilon^rho. On the second region use 1-(1+epsilon^2/h^2)^(-eta/2)<=C epsilon^2/h^2. For 1<t<1/(1-rho), weak compactness in W^(1,t), (1.6), and uniform convergence identify beta as a W_loc^(1,t) field. Finite measure on smaller neighborhoods gives t=1. Since beta vanishes on {S=0}, its weak derivative vanishes almost everywhere there. Elsewhere it is the classical derivative. This proves the local theorem and the claimed removal of curl across arbitrary scalar zeros.

## 2. Global theorem at finite regularity

Keep the range, exponents and regularity of Section 1, now on D=R3 minus{0}. Let omega be any finite real number, Jx=e3 cross x, A=cI-omega J, X(x)=Ax, a=1-2c and b=2(1-c). Put W=curl V and k=X.V. Suppose

    div V=0, DV X=-((1-c)I+omega J)V,
    X.grad S=-bS, W.grad S=0,                            (2.1)

and E<=K|S| on the unit sphere for one finite K>0. Impose either

    (I) k=0 on D; or
    (II) grad k cross grad S=0 on {S!=0}.                (2.2)

The pressure equation and definition S=P-E/2 from (1.1) remain part of the hypotheses. Then there is a global C1 function phi with

    grad phi=beta, X.grad phi=0.                         (2.3)

In particular, (II) implies k=0 without a lower comparison. If V is not identically zero, let M and L be the maximum and minimum of phi on the unit sphere. Then M>L. Both sets E_+={phi=M} and E_-={phi=L} have nonempty boundaries relative to D. Every z on either boundary satisfies

    V(z)=S(z)=0,
    {V!=0} accumulates at z,
    integral_(B_r(z) intersect {V!=0})
          (|V|^2/|S|)^(-tau) dx=infinity,
    tau=(1/c-2)/2,                                      (2.4)

for every ball B_r(z) contained in D. Consequently the lower limit of |V|^2/|S| along {V!=0} at z is zero.

It follows that V=S=P=0 if, in addition, there are a neighborhood O in D of the entire common zero set {V=S=0} and a constant kappa>0 such that

    kappa |S|<=|V|^2 on O.                              (2.5)

More generally, it is enough that the integrand in (2.4) be locally integrable near every point of either extremal boundary. No lower comparison away from the common zeros is used. The global upper comparison, scalar transport and one of (2.2) are explicit additional assumptions.

## 3. Exactness and removal of the additive drift

The complete linear flow F_t(x)=exp(tA)x satisfies |F_t(x)|=exp(ct)|x| and

    V(F_t x)=exp(-(1-c)t)exp(-omega tJ)V(x),
    S(F_t x)=exp(-bt)S(x).                              (3.1)

Every orbit crosses the unit sphere exactly once. Since E and |S| have the same scaling, the upper comparison holds on all of D. Section 1 applies on every compact subset.

Differentiate k=X.V and use (2.1). With the convention (DV)ij=partial_j V_i, the exact Lamb identity is

    grad k=-aV+X cross W.                               (3.2)

Cross (3.2) with grad S on the left. The vector triple-product identity, W.grad S=0 and X.grad S=-bS give

    grad S cross grad k+a grad S cross V=bSW.            (3.3)

Under either (I) or (II) the first term vanishes on {S!=0}, so grad S cross V=(b/a)SW there. Since eta=a/b, differentiating beta gives curl beta=0 on {S!=0}. Section 1 extends this equality to D in distributions.

Local mollification and normalized primitives on balls show that a continuous distributionally closed form has local C1 primitives. Simple connectivity of punctured R3 then gives a single-valued global C1 primitive phi. No componentwise period hypothesis is added. In case (I), X.grad phi=0 follows immediately from beta=|S|^(-eta)V off S=0 and continuity.

For case (II), (3.1) implies beta(F_t x)=exp(-ct)exp(-omega tJ)beta(x), including on S=0. Hence F_t pulls the one-form beta.dx back to itself. Differentiation in x shows that phi(F_t x)-phi(x) is independent of x. The group law and continuity therefore give a real constant C with

    phi(F_t x)=phi(x)+Ct, X.grad phi=C.                 (3.4)

Suppose C!=0. Then beta, V and S are nowhere zero. Let u be phi restricted to the unit sphere and put pi(x)=exp((omega/c)log|x| J)x/|x|. Equation (3.4) gives

    phi(x)=(C/c)log|x|+u(pi(x)).                        (3.5)

The function u is bounded. The zero level Sigma={phi=0} is therefore compact and separates a neighborhood of the origin from infinity. It is a regular C1 sphere, parametrized by n -> F_(-u(n)/C)n with inverse pi. The transversal derivative is C. For C>0 its bounded inside is {phi<0}; for C<0 it is {phi>0}. In either case the inside contains a sufficiently small punctured ball.

Let Flux(r) be the outward flux of V through the radius-r sphere. Applying div V=0 on annuli makes it independent of r, while (3.1) gives

    Flux(exp(ct))=exp((3c-1)t)Flux(1).

Here c>2/5, so 3c-1!=0 and every sphere flux is zero. Integrate div V over the region between a sufficiently small sphere and Sigma. Its origin is omitted and its inner flux is zero. Thus its flux across Sigma is zero. On the other hand, the outward normal to Sigma is sign(C)grad phi/|grad phi|, and

    V.normal=sign(C)|S|^eta |grad phi|

has a strict constant sign on this compact surface. Its integral cannot be zero. This contradiction gives C=0. Equation (3.4) now implies k=0 off S=0; on S=0, V=0 already. This proves (2.3) in both cases. All flows used here are the explicit complete linear flow, not the possibly incomplete V or W flows.

## 4. Harnack with an integrable upper weight

The following elementary version of the CO67 lemma is sufficient. Let p>2, let u be a nonnegative C1 solution on B_(3r) in R3 of

    div(q|Du|^(p-2)Du)=0,

where q is measurable, q>=q0>0 almost everywhere and q is integrable on that ball. Then

    sup_(B_r)u <= exp(C_p [mean_(B_3r)q/q0]^(1/p))
                      inf_(B_r)u.                      (4.1)

Take a cutoff chi supported in B_(3r), equal to one on B_(2r), with |Dchi|<=C/r. Tests with chi^p(u+epsilon)^(1-p) are admissible: the flux is locally integrable, and C1 compactly supported tests are limits of smooth tests with uniformly convergent first derivatives. Holder's inequality gives, for v=log(u+epsilon),

    integral q chi^p |Dv|^p
      <=[p/(p-1)]^p integral q |Dchi|^p.

Consequently ||Dv||_(L^p(B_2r))<=C_p q0^(-1/p)r^(-1)(integral q)^(1/p). Coarea selects sigma in (r,2r) such that the sphere integral of |Dv|^p is at most r^(-1) times the ball integral. The Morrey inequality on the two-dimensional sphere, valid since p>2, gives

    osc_(boundary B_sigma)v
      <=C_p r^(1-3/p)||Dv||_(L^p(B_2r))
      <=C_p[mean_(B_3r)q/q0]^(1/p).                   (4.2)

The weak maximum and minimum principles carry this oscillation bound into B_sigma. For example choose K slightly above the boundary maximum of u and test with (u-K)_+. It has compact support in the ball. Approximation of the truncation by smooth functions is justified by domination by q, since u and Du are bounded on that compact set. The resulting integral of q|D(u-K)_+|^p is zero. Positivity of q makes the truncation constant, and its boundary value makes it zero. The lower test is identical. Let K approach the boundary maximum or minimum, then exponentiate (4.2) and let epsilon decrease to zero. This proves (4.1). In particular, a zero at an interior point of B_r forces u=0 throughout B_r.

For our phi put m=1/c>2, N={V!=0} and R=E/|S| on N. Define q=R^(-tau) on N and q=K^(-tau) outside N, where tau=(m-2)/2. Direct exponent calculation gives

    q>=K^(-tau)>0,
    V=q|grad phi|^(m-2)grad phi.                       (4.3)

The equality holds on N because rho(m-2)=eta, and both sides vanish outside N. Its flux is the C1 vector field V even if q is not locally integrable. Divergence freedom therefore gives the full-domain weak equation associated with (4.3). Whenever q is locally integrable, (4.1) applies with p=m. No derivative of q is required.

## 5. Extremal zeros and the local lower comparison

Equation (2.3) makes phi constant on each orbit meeting the sphere, so its sphere maximum M and minimum L are global and attained in D. If V is nonzero, grad phi is nonzero somewhere and M>L. The two extremal sets are proper, nonempty and closed. Connectedness of D gives nonempty relative boundaries.

Let z belong to the boundary of E_+. Differentiability of phi and attainment of its maximum give grad phi(z)=0, hence V(z)=0. If S(z)!=0, near z the function phi solves the uniformly elliptic equation div(|S|^eta grad phi)=0 with a positive C1 coefficient. It is C2 there. The classical strong maximum principle implies that phi is locally constant, making z interior to E_+, a contradiction. Thus S(z)=0. If N missed a ball about z, grad phi would vanish there and z would again be interior. Hence N accumulates at z.

If the integral in (2.4) were finite for some ball, the extended q in (4.3) would be integrable on that ball. Apply (4.1) to M-phi on a smaller concentric ball and its triple. The zero at z would make phi=M on a neighborhood of z, contradicting boundary membership. This proves the infinite-integral assertion. A positive lower bound for R along N near z would make that integral finite, so its lower limit must be zero. Apply the same reasoning to phi-L for E_-.

Under (2.5), q is bounded near every common zero, since R>=kappa on N there and q has a fixed finite value outside N. This contradicts (2.4) if V is nonzero. Therefore V=0. The Poisson equation now makes S=P harmonic on D, and its twisted homogeneity gives

    |S(x)|<=C|x|^(-d0), d0=b/c in (2,3).

Its Kelvin transform H(y)=|y|^(-1)S(y/|y|^2) is harmonic away from zero and bounded by C|y|^(d0-1). Boundedness near zero makes that singularity removable. The resulting entire harmonic function has growth strictly below quadratic. Interior second-derivative estimates on arbitrarily large balls give D2H=0, so H is affine. Its vanishing at zero of order greater than one eliminates its affine coefficients. Hence S=P=0.

## 6. Scope, actual tails and verification

This argument weakens the regularity requirements of CO67 and LIT278 in the target interval by adding the stated Poisson structure and using the upper comparison alone in the removal estimate. It does not prove that any target profile has that comparison, k=0, full rank on all of {S!=0}, or W.grad S=0. In case (II) all four structural premises in (2.1) remain. Vortical rank plus density on {S!=0} is a sufficient way to supply full rank, but density alone without independently supplied vortical rank is insufficient.

For an actual whole-space C2 velocity/C1 pressure profile with the explicit natural bounds |U(x)|<=C(1+|x|)^(-p) and |DU(x)|<=C(1+|x|)^(-p-1), p=(1-c)/c, the already confirmed A533/A538/A539 give V in C_loc^(1,alpha) for every alpha<1 and the stated Poisson tail pressure P2. One can therefore choose alpha>alpha0 without a new tail smoothness premise. Here P means that actual P2, after the original pressure limit has been subtracted. Original zero helicity supplies W.grad S=0 by A531; absent that hypothesis the displayed scalar transport must be supplied separately. The present theorem then gives zero tail if its remaining upper, local lower and contraction or rank hypotheses hold. The separate faithful-tail implication to U=0 is LIT269 Section 4, independently confirmed A1877: its proof integrates the forced linear-flow equation using the canonical pressure estimate, obtains U=O(|x|^(-2p-1)), and checks all energy boundary errors before concluding U=0. No finite-energy premise is silently inserted here.

The complete Section 1 theorem is local removal, not local continuation from one zero. The global conclusion uses a maximum on the compact sphere and may concern arbitrary sign changes and arbitrary common zero sets. It holds for every finite omega, without a smallness condition, but no numerical constants uniform as |omega| tends to infinity are claimed.

All three source proofs LIT267, CO67 and LIT278 and the earlier independent proofs were read before this argument was written. Source snapshots, hashes, the primary root statement and its slicing proof are in the team records. No numerical computation, formal source or formal build was used. Independent comparison was completed through the existing configured model coordinator and literature agent files; both full reviews are retained in the team records. The coordinator checked ten items and relied on the prior root-theorem audit; the literature agent and this audit reread the actual primary statements and slicing proof. Runtime model identity is not independently attested. The bare-decay arbitrary-helicity conjecture remains OPEN.
