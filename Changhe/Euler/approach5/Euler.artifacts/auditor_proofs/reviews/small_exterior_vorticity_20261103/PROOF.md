# Small exterior vorticity forces gradient decay

Independent mathematical audit of C49, in the team records. This proof distinguishes the pressure-free growth estimate from its exact-Euler decay consequences. No computation, formalization, helicity condition or bounded-gradient premise is used in the growth estimate.

## 1. Exact statement and notation

Let 0<c<1 and omega be any finite real number. Let J(x1,x2,x3)=(-x2,x1,0), A=cI-omega J, B(y)=Ay+U(y). Suppose U belongs to C2(R3;R3), P belongs to C1(R3), div U=0, and

    (1-c)U + DU B + omega JU + grad P = 0.                 (1)

Put Omega=curl U and M=sup_R3 |U|<infinity. Norms of matrices are Euclidean operator norms. For 0<alpha<1, brackets denote the ordinary Holder seminorm with exponent alpha.

If W0>0 and |Omega(y)|<=W0 for |y|>=R1, then, for every 0<alpha<1 and

    gamma > (1+alpha)W0/alpha,                              (2)

there are finite K,R such that, for |y|>=R,

    ||DU(y)||<=K |y|^(gamma/c),
    [Omega]_(alpha,B(y,|y|/4))<=exp(K |y|^(gamma/c)).         (3)

The constants can depend on c,M,W0,R1,alpha,gamma and the C2 norm of U on a fixed compact annulus. They need not be controlled by M alone. Every gamma>2W0 is allowed by choosing alpha sufficiently close to 1. Neither gamma=2W0 nor alpha=1 is asserted.

Write omega_inf=limsup_(|y|->infinity)|Omega(y)|, with values in [0,+infinity]. If |U|=O(|y|^-kappa) for some kappa>=0, set

    delta_star=min(5/4,1/c,(1+kappa)/2).

Then

    omega_inf < c delta_star/2
       implies DU->0 and |Omega|+||DU||<=C/(1+|y|).        (4)

Consequently omega_inf is zero or at least c delta_star/2, including the possibility +infinity. For bounded U alone the threshold is c/4. For kappa>=1 it is at least c/2. For the natural velocity tail kappa=1/c-1 and 2/5<c<1/2 it is exactly 1/4.

In particular, bounded U and Omega->0 force DU->0 for every 0<c<1 and finite omega. This does not prove Omega->0 from U->0.

## 2. Dependencies and separation of hypotheses

The proof of (3) uses only incompressibility, exact vorticity transport, bounded velocity, the physical change of variables, and localized Newtonian-potential estimates proved below. It makes no pressure estimate.

For (4), the following previously confirmed exact-Euler results are separate dependencies.

1. A498(A): bounded U and DU=o(|y|^(1/2)) imply DU->0, for 0<c<1 and all finite omega. Its proof includes pressure control and is in in the team records.
2. A757: if 1/2<=delta<=5/4, c delta<1, DU=O(|y|^delta), and U=o(|y|^(1-2delta)), then DU->0. The exact hypotheses, pressure normalization, local Holder bound and envelope iteration are in in the team records. Sections 4-8 were reread for this composition. In particular, the pressure envelope is bounded only after the fixed source estimate and prior polynomial barrier have been established.
3. A492 and A476: bounded U and bounded DU imply Omega=O(1/|y|), then a Dini gradient bound, and finally DU=O(1/|y|). These results apply only after (4) has supplied DU->0. A477/A686 give the natural velocity and derivative rates if U->0 and c>1/3.

No premise in this list is supplied merely by a sampled numerical residual. All are exact-profile statements. The proof below does not use any of its decay consequences in obtaining (3).

## 3. Physical variables and complete characteristics

Let tau=T-t, s=-log tau, Q=exp(omega sJ), and y=exp(sA)x. Define

    u(x,t)=tau^(c-1) Q U(y),
    xi(x,t)=tau^-1 Q Omega(y),
    Du(x,t)=tau^-1 Q DU(y) Q^T.                            (5)

Direct substitution and curl of (1) give div u=0 and

    xi_t+(u.grad)xi=(Du)xi.                                (6)

These are pointwise identities at the stated regularity. The zero field is immediate, so assume M>0. Choose tau0=T-t0<=1 such that

    (2M/c)tau0^c<=1/8,  tau0^-c/16>=R1.

Then M tau0<=c/16<1/16. For t0<=t<T,

    |u(x,t)|<=M tau^(c-1) everywhere,
    |xi(x,t)|<=w(t):=W0/tau for |x|>=1/16.                (7)

On each compact time interval below T, u is locally Lipschitz in space and has an integrable spatially uniform speed bound. Thus a characteristic cannot reach spatial infinity in finite time on that interval. Its unique backward continuation exists all the way to t0. No global gradient bound is needed for this conclusion.

Let xstar be any unit vector and define

    r(t)=1/4+(2M/c)tau^c,
    B_t=B(xstar,r(t)),
    d(sigma,t)=(M/c)(tau_sigma^c-tau_t^c),
    E_(sigma,t)=B(xstar,r(t)+d(sigma,t)).

For sigma<t one has

    M(t-sigma)<=d(sigma,t)<=1/16,
    E_(sigma,t)+d(sigma,t)=B_sigma,
    1/4<r(t)<=3/8.                                        (8)

A characteristic ending in B_t stays in E_(sigma,t) at time sigma by integrating the speed bound. Both paths and their joining line segment remain inside this convex ball, and all balls are inside 5/8<|x|<11/8.

## 4. Exact strain coefficient and localized estimates

Use BS f=curl(N*f), N(z)=1/(4 pi |z|). For compactly supported C-alpha vector data,

    D BS f(x)=p.v. integral K(x-z)f(z) dz + C_f(x)/3,
    K(z)f=[C_f-3(f cross theta) tensor theta]/(4 pi |z|^3),
    C_f v=f cross v, theta=z/|z|.                          (9)

The kernel has zero spherical mean. Its full operator norm is at most 2|f|/(4 pi |z|^3). However, for each unit e,

    e.K(z)f e=-3(e.theta) f.(theta cross e)/(4 pi |z|^3).

The local term has zero quadratic form. The relevant spherical average is exactly

    (1/(4 pi)) integral_S2 3|e.theta|sqrt(1-(e.theta)^2)
       =3 integral_0^1 z sqrt(1-z^2) dz=1.                (10)

One must take the quadratic form and integrate before taking the supremum over e. For bounded f, (10) gives an annular strain bound ||f||_infinity log(b/a). The direction of f can vary with position; the scalar bound was pointwise before integration. Thus the leading logarithmic coefficient is 1, not the full-gradient coefficient 2.

Subtracting f(x) inside a radius epsilon and integrating the Holder difference gives

    ||sym D BS f(x)||
       <=epsilon^alpha [f]_alpha/alpha
         +||f||_infinity log(1/epsilon)+C||f||_1,
    0<epsilon<=1.                                        (11)

The zero-mean kernel also gives [D BS f]_alpha<=C_alpha[f]_alpha. For a difference at separation h, split at 2h, subtract local values in the near part, and use the kernel derivative in the far part. The radial integrals are constants times h^alpha from the powers r^(alpha-1) and h r^(alpha-2). This is why 0<alpha<1 is needed.

Choose a fixed cutoff chi0 supported in 1/16<|x|<16 and equal to one in 1/8<|x|<8. The vector field

    v_h=u-BS(chi0 xi)

is harmonic on the latter annulus: -Delta u=curl xi and -Delta BS f=curl f. It need not be curl free. Its supremum there is bounded by M tau^(c-1)+Cw, so its first two derivatives on 1/4<=|x|<=4 are bounded by the same expression. No core vorticity bound is being assumed.

For any ball E with margin 0<d<=1/16 inside 1/2<=|x|<=3/2, insert a cutoff chi equal to one on E+d/2 and supported in E+d. Its source satisfies

    [chi xi]_alpha<=[xi]_(alpha,E+d)+C_alpha w d^-alpha.

The remaining cutoff source vanishes on E+d/2. Its strain has bound w log(1/d)+Cw by (10); the second derivative of its Biot-Savart field is O(w/d), and interpolation gives a Holder bound Cw d^-alpha(1+log(1/d)). Therefore, with S=sym Du and Z=M tau^(c-1)+w,

    [Du]_(alpha,E)<=C[ xi ]_(alpha,E+d)
       +Cw d^-alpha(1+log(1/d))+CZ,                       (12)

    sup_E ||S||<=epsilon^alpha([xi]_(alpha,E+d)
       +Cw d^-alpha)/alpha+w log(1/epsilon)
       +w log(1/d)+Cw+CZ.                                 (13)

The cutoff product estimate includes pairs straddling the support: the distance to the cutoff boundary supplies the same d^-alpha term.

## 5. Transport inequality with a nonlinear logarithm

Set Theta(t)=[xi(t)]_(alpha,B_t), Y(t)=log(e+Theta(t)), and

    Lambda(sigma,t)=sup_(E_(sigma,t))||S(sigma)||.

In (13), take epsilon=min(d,exp(-Y(sigma)/alpha)). Since epsilon^alpha Theta<=1 and epsilon<=d, (8) yields

    Lambda(sigma,t)<=w(sigma)Y(sigma)/alpha+b(sigma,t),    (14)
    b(sigma,t)=2w(sigma)ell(t-sigma)+Cw(sigma)
       +C(1+tau_sigma^(c-1)),
    ell(h)=log(1/(Mh))>0.

All coefficients can be enlarged to be nonnegative. Put

    Phi(rho,t)=alpha integral_rho^t Lambda(sigma,t) d sigma.

For a pair of characteristics, the derivative of the logarithm of their separation is the average of e.S e along their joining segment. Thus their earlier separation to power alpha is at most exp(Phi) times the terminal separation to that power.

The antisymmetric part of Du is v -> xi cross v/2. Hence (Du)xi=S xi exactly. Apply the product estimate to S xi and then (12). Integrating (6) along the two paths gives

    Theta(t)<=exp(Phi(t0,t))Theta0
       +integral_t0^t exp(Phi(rho,t))
         [(Lambda(rho,t)+Cw(rho))Theta(rho)+H(rho,t)] d rho, (15)

    H(rho,t)=Cw(rho)^2 m(t-rho)+Cw(rho)Z(rho),
    m(h)=(Mh)^-alpha(1+ell(h)).

Here Theta0 can be chosen uniformly in xstar using the C1 norm of xi(t0) on 1/2<=|x|<=3/2. The kernel m is integrable because alpha<1. The singular endpoint rho=t is never used in (12); it is harmless in (15). The right side is increasing in all nonnegative Theta and Y values after using (14).

## 6. Uniform nonlinear barrier, including the diagonal

Fix gamma as in (2) and let

    F(t)=K tau^-gamma,  theta=W0/(alpha gamma),
    Lambda_F(rho,t)=theta F'(rho)+b(rho,t),
    D(rho,t)=F(t)-F(rho),
    q(rho,t)=integral_rho^t b(sigma,t)d sigma.

The identity wF/alpha=theta F' is exact. We first show

    q(rho,t)<=beta_K D(rho,t)+r_K,
    beta_K->0, r_K->0, uniformly in t0<=rho<t<T.          (16)

Write a=T-t and v=T-sigma. Split the logarithm exactly as

    log(1/(M(v-a)))=log(1/(Mv))+log(v/(v-a)).

The contribution 2W0 log(1/(Mv))/v, together with Cw+C(1+v^(c-1)), is bounded by C v^(-gamma-1). Its integral is at most C D/K. For the second logarithm choose N=sqrt K. Its constant part contributes at most

    2W0 tau0^gamma D/(gamma sqrt K).

For the remainder, z=a/v gives

    integral_a^(T-rho) [log(v/(v-a))-N]_+ dv/v
       <=integral_0^1 [-log(1-z)-N]_+ dz/z
       <=e^-N/(1-e^-N).

The last inequality uses h=1-z and integral_0^(e^-N)(-log h-N)dh=e^-N. Thus (16) holds with

    beta_K=C/K+2W0 tau0^gamma/(gamma sqrt K),
    r_K=2W0 exp(-sqrt K)/(1-exp(-sqrt K)).

This estimate is uniform even when t-rho is arbitrarily small. It resolves the nonseparable time dependence of Lambda and does not invoke ordinary linear Gronwall on (15).

Let kappa_K=1-alpha(theta+beta_K), positive for large K. If Phi_F is defined using Lambda_F, then

    exp(Phi_F(rho,t)+F(rho)-F(t))
       <=exp(alpha r_K)exp(-kappa_K D(rho,t)).             (17)

Let R_F denote the right side of (15) with Lambda=Lambda_F and Theta(rho)=exp(F(rho)). The initial term, normalized by exp(F(t)), is at most exp(alpha r_K)Theta0 exp(-F(t0)). The theta F' term is at most exp(alpha r_K)theta/kappa_K.

For the b term let Q(D)=q(rho,t). Then Q(0)=0 and Q(D)<=beta_K D+r_K. Integration by parts, including the upper boundary, gives

    integral exp(-kappa_K D)b(rho,t)d rho
       <=beta_K/kappa_K+r_K.                             (18)

Indeed the integral is integral_0^D0 exp(-kappa_K z)dQ(z); substituting the bound in its boundary term and the integral term gives beta_K(1-exp(-kappa_K D0))/kappa_K+r_K. The additional Cw term is at most C/(K kappa_K), since w/F'<=W0 tau0^gamma/(gamma K).

Finally integral_t0^t H(rho,t)d rho<=C tau_t^-2, by integrability of m, w<=W0/tau_t and Z<=C/tau_t. The normalized forcing is therefore bounded by

    C exp(alpha r_K) tau_t^-2
       exp(-kappa_K K tau_t^-gamma),

whose supremum tends to zero as K grows. We obtain

    limsup_(K->infinity) sup_(t0<=t<T) R_F(t)/exp(F(t))
       <=theta/(1-alpha theta)<1.                        (19)

The strict last inequality is precisely gamma>(1+alpha)W0/alpha. All constants in the terms tending to zero were fixed before K was increased.

The submitted Lemma B uses another valid estimate for the same logarithm: it absorbs 2w ell by eta F' except on an exponentially short interval, with an L1 remainder O(K^-1/gamma). Its fixed positive kappa and limiting ratio theta_source/(alpha kappa), theta_source=W0/gamma, are consistent with (19). Its source bound and continuation argument also pass independently. These are two proofs of the same comparison, not independent assumptions.

## 7. Continuity and the comparison principle

Theta is continuous on compact time intervals below T. To see this, parameterize the closed moving ball by xstar+r(t)z, |z|<=1. The Holder difference quotient on the product of two closed unit balls extends by zero across the diagonal, uniformly in time, because xi has a bounded local gradient and alpha<1. It is then continuous on a compact parameter set, and its maximum is continuous in t. The maximum equals the seminorm over the open ball by density.

Choose eta<1 larger than the last ratio in (19), and increase K until, uniformly in t,

    R_F(t)<=eta exp(F(t)),
    (1-eta)exp(F(t0))>e,
    log(e+Theta0)<F(t0).

At a first contact Y(t)=F(t), earlier values satisfy Y<=F and Theta<=exp(F). Equations (14)-(15) and monotonicity imply

    Theta(t)<=R_F(t)<exp(F(t))-e,

which contradicts that contact. Thus Y<F on all of [t0,T). A global gradient bound has not been assumed; only compact preterminal regularity was used to justify continuity and characteristics.

## 8. Return to the profile and uniform constants

Apply (13) with E=B(xstar,1/8), d=1/16 and epsilon=min(1/16,exp(-Y(t)/alpha)). Since E+d is contained in B_t and ||Du||<=||S||+|xi|/2,

    ||Du(xstar,t)||<=(W0 K/alpha) tau^(-1-gamma)+C tau^-1.

For |y|=r large choose tau=r^-1/c and xstar=exp(-sA)y. Then |xstar|=1. Multiplication by tau in (5) proves the first estimate (3).

The physical ball B(xstar,1/4) maps onto B(y,r/4). Its exact seminorm scaling is

    [Omega]_(alpha,B(y,r/4))
       =tau^(1+c alpha)[xi]_(alpha,B(xstar,1/4))
       <=exp(K r^(gamma/c)),

after tau<=1. The compact-annulus initial bound was uniform over all unit xstar, so K and R are uniform in direction. Rotation contributes only orthogonal conjugations and does not impose an upper bound or resonance exclusion on omega.

## 9. The gradient and vorticity gaps

Suppose omega_inf<c delta_star/2. Choose

    omega_inf<W0<c delta_star/2,
    2W0<gamma<c delta_star,

using any sufficiently small positive W0 if omega_inf=0. Choose alpha<1 close enough to 1 that (2) holds. Let delta=gamma/c. Equation (3) gives a global polynomial gradient bound with exponent delta after enlarging its constant on a compact ball.

If delta<1/2, this is o(|y|^(1/2)), so A498(A) gives DU->0 even for bounded U without decay. Otherwise 1/2<=delta<delta_star, and

    delta<5/4, c delta<1,
    delta<(1+kappa)/2,
    U=O(|y|^-kappa)=o(|y|^(1-2delta)).

A757 gives DU->0. Only now apply A492 and A476 to obtain (4). In particular omega_inf=0. This proves the asserted gap, including Omega->0 as a sufficient condition for gradient decay.

For the natural tail in the target range, 1/c-1>1 and

    min(5/4,1/c,(1+(1/c-1))/2)=1/(2c),

so the threshold is 1/4 for every such c and omega. The threshold is strict. A757 at delta>=1/(2c) would require a velocity little-o premise already sufficient for the energy exclusion A053; this does not yield an endpoint improvement from a natural big-O bound.

If U->0 and c>1/3, the existing A477/A686 bootstrap additionally gives U=O(r^(1-1/c)) and DU=O(r^-1/c). Those rates are not asserted by this composition for c<=1/3.

## 10. Physical exterior statement

For any rho>0, the change of variables (5) gives the exact identity

    tau ||xi(t)||_(Linf(|x|>=rho))
       =sup_(|y|>=rho tau^-c)|Omega(y)|.

The right side decreases to omega_inf as tau->0, in the extended real sense. Thus a limit exists, not just a limsup. If omega_inf<c/4, (4) and C/(1+r)<=C/r give

    ||Du(t)||_(Linf(|x|>=rho))
       <=C rho^-1 tau^(c-1), 0<tau<=1.

This time bound is integrable because c>0. It is an exterior estimate; it is not a global Euler continuation theorem and does not control a shrinking physical core.

## 11. Exact residuals and the remaining derivative problem

For any C2 divergence-free candidate, let R be the left side of (1). A direct curl calculation gives

    curl R=(B.grad)Omega-DU Omega+Omega+omega J Omega.    (20)

If a bounded candidate with Omega->0 satisfied this exact vorticity equation, the nonpressure part of momentum would be a C1 curl-free field on simply connected R3. It would be the gradient of a C2 scalar, so a pressure could be chosen making it an exact profile. Equation (4) would then force DU->0. Therefore a bounded candidate with Omega->0 but persistent gradient cannot satisfy (20) with zero right side everywhere. Changing pressure cannot remove a nonzero curl residual. Small momentum residual in value alone gives no such identity.

For an exact profile with U->0 and DU not tending to zero, the contrapositive of (4) gives omega_inf>=c/4, or the stronger weighted threshold when the stated velocity tail is available. This is a lower bound along suitable sequences of profile points. In physical variables it supplies vorticity at least of order tau^-1 along corresponding point-time sequences whose profile radii diverge.

The wording in source Remark R4, 'type-I vorticity with a lower bound on its constant', is too strong if understood to assert a type-I upper bound. No finite upper bound on omega_inf has been proved, and +infinity is allowed. Replace it by 'a type-I-scale lower bound along sequences'. The lower-bound conclusion itself is valid. No fixed physical ray, uniform lower bound in the exterior, or tau^-1 upper bound follows from this argument.

## 12. Verdict, scope and provenance

CONFIRMED: the exact logarithmic strain coefficient, complete finite-time characteristics, localized transport, uniform nonlinear comparison, growth theorem (3), conditional decay theorem (4), physical exterior consequence and exact-curl residual obstruction. These statements hold for every finite omega with parameter-dependent constants.

OPEN: endpoint equality in (2) or (4), optimality of the constants, any exclusion of profiles above the threshold, a proof of Omega->0 from U->0, removal of the derivative premise in full, and the main arbitrary-helicity bare-decay nonexistence conjecture. The work neither imposes nor proves zero helicity.

All 419 lines of the submitted C49 source and all nine sections of its 322-line referee proof were read. The referee answer was also read; it identifies the first-contact and uniform-remainder issues and supplies the strain improvement. The author's repaired proof resolves both. Symbolic and sampled checks in the source are not used as proof here.

This is continuing file-based collaboration with Theory Agent A, configured as the primary model. Provider runtime is not independently attested. The nested the external referee (a second model) reports that its own attempted model consultation failed at credential acquisition before any model invocation. That failed attempt is not counted as a second model review. No new model client or remote computation was launched by this audit.
