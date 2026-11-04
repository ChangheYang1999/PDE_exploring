# Conditional Lorenz return maps: exact constraints and scope

Audited 2026-11-02T20:56:24Z. This is an audit of Theory Agent B B22, not a classification of all mixed backward limits.

## Assumptions and notation

Let U be C2 and P be C1 on a neighborhood of a compact invariant set of a rotating Euler profile. Put B=(cI-omega J)y+U, Omega=curl U, k=1-2c>0, b=1+c, and let Psi_t be the flow of -B. Suppose Omega is nonzero on this neighborhood and that a section saturated by short Omega segments has a two-branch quotient return map f. This section and its Lorenz geometry are ADDITIONAL assumptions. They have not been established for every remaining mixed limit set.

Write w2=i_Omega vol and alpha=i_(-B)w2. On the section choose the scalar flux coordinate r with alpha=dr. Choose consistent orientations. Suppose the quotient domain is (-1,0) union (0,1), each branch is increasing, f(0+)=-1 and f(1)=q<=1, with odd reflection for the negative branch. Return times are finite, positive and continuous off zero and are denoted T(r). When the endpoint 1 is included its return time is positive. A Lorenz singular roof is assumed nonconstant and tends to infinity at zero.

For the local singular model, suppose DB(p) has eigenvalues b,s,-e, where s>0, e=s+k, and put nu=s/e in (0,1). Calling Omega the strongest stable direction of the backward flow additionally requires s<b; none of the scalar branch calculations below proves that inequality.

## 1. Exact derivative and branch constraints

The identities d alpha=k w2 and L_(-B)alpha=k alpha give, for a variable-time return R,

    R*alpha=exp(k T)alpha.

The derivative of T contributes a multiple of -B and is killed by alpha. The bracket implies preservation of the Omega foliation, so T is constant on its local fibers and R induces f. Therefore

    f'(r)=exp(k T(r)),
    f(r)=-1+integral_0^r exp(k T(u)) du,                 (1)
    integral_0^1 exp(k T(r)) dr=1+q<=2.                 (2)

In particular q>0. Since the roof is nonconstant,

    exp(k inf T)<1+q<=2,
    inf T<log(2)/k.                                   (3)

Jensen's inequality gives

    integral_0^1 T(r) dr <= log(1+q)/k.                 (4)

The integrals in (2) and (4) use Lebesgue measure in the normalized flux coordinate, not an invariant density. Integrability of T follows already from T>0 and integrability of exp(kT). Without a nonconstant-roof hypothesis the first inequality in (3) is non-strict. These conclusions depend only on the bracket and divergence package, not on the actual-curl coupling.

For f(r)=-1+L r^nu with 0<L<=2, (1) uniquely fixes

    T(r)=log(L nu)/k + log(1/r)/e.

Positive return time at r=1 requires L nu>1. Thus the full-branch power ansatz L=2 requires nu>1/2. At nu=1/2 its endpoint time is zero, incompatible with a genuine transverse return through that endpoint. This is a restriction of that ansatz.

## 2. Positive full-branch model roofs for every exponent

Choose a smooth function chi valued in [0,1], equal to one on [0,1/2] and zero on [1,infinity), flat at the transition endpoint. For small delta>0 put

    theta_delta(r)=chi(r/delta) log(delta/r),  0<r<delta,
    theta_delta(r)=0,                         r>=delta,
    I_delta=integral_0^1 exp((1-nu)theta_delta(r)) dr.

Direct comparison with (delta/r)^(1-nu) on (0,delta) gives

    1<I_delta<=1+delta(1/nu-1).

Choose delta so that I_delta<2, set tau=log(2/I_delta)/k>0, and define

    T_delta(r)=tau+theta_delta(r)/e,
    f_delta(r)=-1+integral_0^r exp(k T_delta(u)) du.

Then f_delta(1)=1, f_delta'>1, and all off-singularity data are smooth. Near zero,

    T_delta=tau+log(delta/r)/e,
    f_delta(r)+1=exp(k tau) delta^(1-nu) r^nu/nu.

The planar linear saddle u'=eu, v'=-sv has divergence k. On an incoming section v=v0 and an outgoing section u=u0, its flux coordinates can be taken as r_in=s v0 u and r_out=e u0 v. With delta=s v0 u0, its passage has time log(delta/r_in)/e and output delta^(1-nu)r_in^nu/nu. A regular affine transition of time tau supplies the factor exp(k tau). Thus the constructed data have compatible local singular and regular pieces. This does not construct a global embedded three-dimensional bracket field, still less an Euler profile.

## 3. A bounded roof remainder does not give a limiting power coefficient

If only

    T(r)=log(1/r)/e+O(1)

is known, (1) proves f(r)+1 is bounded above and below by positive multiples of r^nu. It does not prove f(r)+1 divided by r^nu has a limit.

For an explicit scalar counterexample, take epsilon>0, a real constant tau, and, for sufficiently small r>0,

    T(r)=log(1/r)/e+tau+epsilon sin(log(log(1/r))).

This is smooth off zero, positive for small r, has the specified O(1) remainder, and defines a finite branch by (1). Put L(r)=exp(k epsilon sin(log(log(1/r)))). Then

    [f(r)+1]/r^nu = exp(k tau) integral_0^1 t^(nu-1)L(rt) dt.

For each fixed t in (0,1], L(rt)/L(r) tends to one as r tends to zero. The ratio is uniformly bounded above and below. Dominated convergence against t^(nu-1) gives

    [f(r)+1]/r^nu = exp(k tau)L(r)/nu + o(1).

L has distinct subsequential limits, so no constant leading coefficient exists. This refutes the displayed scalar inference. It does not show that this oscillatory roof arises from a C2 Euler saddle. A proof using stronger local saddle regularity could recover a limiting coefficient; such a proof is separate from the stated O(1) estimate. If instead the remainder tends to tau0, the same dominated-convergence argument yields f(r)+1 asymptotic to exp(k tau0)r^nu/nu.

## 4. Actual Euler action and periodic-orbit test

Here the actual-curl and momentum coupling matters. Use V=cy+U, reserving -B for the backward vector field. The rotating Bernoulli quantity H satisfies

    B.grad H=-k V.B.

Consequently on the FULL section,

    integral_0^T V.B(Psi_t z) dt = [H(Rz)-H(z)]/k.       (5)

The sign is positive because time is backward. H need not be constant on a vortex fiber: Omega.grad H=-k V.Omega. Thus (5) cannot simply be assigned to the scalar quotient without a choice of representatives and a correction.

If a quotient periodic point lifts to a genuine nonstationary periodic orbit of the full return map, with total backward period S, (1) gives

    log (f^n)' = k S.                                  (6)

For an actual Euler periodic orbit gamma, U=-gamma_dot-c gamma+omega J gamma in backward time. Its zero U-circulation implies

    integral_0^S |gamma_dot|^2 dt=2 omega A_gamma,
    A_gamma=(1/2) integral_0^S (gamma_1 gamma_dot_2-gamma_2 gamma_dot_1) dt.

The c gamma term is an exact derivative and integrates to zero. Subtract the horizontal mean of gamma, apply Cauchy-Schwarz and the periodic Wirtinger inequality to obtain

    2|A_gamma| <= S/(2 pi) integral_0^S |gamma_dot|^2 dt.

For omega nonzero this proves

    S>=2 pi/|omega|,
    log (f^n)' >= 2 pi k/|omega|.                       (7)

For omega=0 there is no nonstationary periodic orbit. Endpoint symbolic points count in (7) only when they represent actual return orbits. These are not bounds on each individual flight time.

Equation (6) is kinematic. The energy-area identity, (5), and (7) use the Euler relation between B-Ay, pressure, and the primitive of i_Omega vol. An independent bracket field W has no reason to make that primitive equal to U.flat.

## 5. Conditional entropy statement

Here is a sufficient precise version of the entropy assertion. Assume inf T>0, f is C1 on its two monotone branches, eta has an invariant density rho with respect to dr, and integral T d eta is finite. Then

    h_eta(f)=integral log f' d eta=k integral T d eta<=log 2.   (8)

To see the equality without a hidden density-integrability assumption, the two-branch partition is generating: a length-n cylinder has diameter at most 2 exp(-k n inf T). Conditional probabilities of its two inverse branches at x are

    q_i(x)=rho(g_i x)/(rho(x) f'(g_i x)),

where only existing branches are used and their sum is one almost everywhere. The entropy formula for a finite generating partition gives h_eta(f)=integral log J_eta f d eta, with

    J_eta f(y)=rho(fy)f'(y)/rho(y)=1/q_i(fy).

This integral lies in [0,log 2]. Also log f'=kT is integrable. Therefore log rho composed with f minus log rho is an integrable measurable coboundary. Such a coboundary has zero integral even if log rho is not integrable: its Birkhoff averages telescope and tend to zero in probability because log rho is finite eta-almost everywhere and eta is invariant; the integrable ergodic theorem then makes their almost-sure limit zero. This proves (8).

If the full return dynamics is the invertible natural extension of f with contracting vortex fibers, and the flow is its suspension with roof T, Abramov's suspension formula gives entropy per unit physical backward time equal to k. In a usual compact Lorenz return construction the contraction follows from the exact fiber multiplier exp(-bT), and its bounded full fibers encode the inverse itinerary. Calling this measure a physical SRB measure additionally uses that full contracting-fiber construction or an independently verified physical-measure theorem. An abstract density on an unspecified scalar map alone does not supply an embedded physical flow measure.

## 6. Refuted universal interpretation

The claim that any roof satisfying (1) also realizes all Euler constraints is false. For example choose c=9/20, so k=1/10, choose nu=3/4, and use the full-branch power model. It has positive roof with endpoint period S=10 log(3/2). For omega=1, an actual endpoint fixed orbit would require S>=2 pi. But log(3/2)<1/2 and pi>3 give S<5<2 pi. Thus the scalar roof satisfies the exact derivative law and violates the Euler periodic test if that endpoint is used as a genuine orbit.

No inference that every future obstruction must come from one pressure-Hessian moment or from the far field is proved. The branch calculations are necessary consistency conditions and local constructions. They leave the existence and classification of the mixed attractor OPEN.

## Dependencies

The exact transverse form and local section construction are A155/A161. The Euler Bernoulli and circulation identities and Wirtinger bound are A030 and the foundation audit. The entropy paragraph states its extra return-map assumptions explicitly and uses only the finite-generator entropy formula, the integrable ergodic theorem and Abramov's formula for the stated suspension. No numerical computation, global Lorenz classification, or global profile construction is used.
