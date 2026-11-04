# Critical pressure flatness, tensor transport and the conditional annular flux argument

Status: CONFIRMED A976-A979 for the exact results; the uniform strengthening A980 remains OPEN. Complete independent audit of Theory Agent C C45. The proof below does not use A963. That later stronger result excludes the entire actual noninterior-node configuration, so C45's remaining-plane status is historical rather than the current frontier.

## 1. Exact setting and inputs

Let 2/5<c<1/2, omega be finite, A=cI-omega J, Jx=(-x2,x1,0), a=1-2c, kappa=1+c, lambda=2(1-c), q=lambda/a>6 and p=(1-c)/c. Suppose U in C2(R3;R3), P in C1(R3) solve the rotating Euler profile equation, div U=0 and U.curl U=0 everywhere, with

    |U(x)|<=C(1+|x|)^(-p), |DU(x)|<=C(1+|x|)^(-p-1).

Let B=Ax+U, Omega=curl U, Phi and Gamma their complete flows, E the forward escaping set, O its vortex saturation, and L the actual transported C1 scalar on O. Normalize pressure at its actual limit Pinf and set

    H=P-Pinf+|U|^2/2+(Ax).U,
    Q=P-Pinf-|U|^2/2, g=H-Q=U.B, S_U=sym DU.

Assume y0 in O is a vortical noninterior zero of L. Let N be its full joint B,Omega orbit and Cbar its ambient closure. The earlier confirmed C44/A936-A939 supplies Cbar subset O, invariance, and throughout Cbar

    H=Q=g=L=0, dH=dQ=dL=0,
    B cross Omega=aU!=0, U.B=U.Omega=0,
    D Phi_t^T U(Phi_t y)=exp(-at)U(y).

All its points are of the same noninterior type. On {Omega!=0,dL!=0} in O, dH and dQ are multiples of dL. For each fixed z in E,

    exp(at)H(Phi_t z)->L(z),
    exp(lambda t)Q(Phi_t z)->S(Xi z).

The other used identities are BH=-ag, BL=-aL, Gamma invariance of H,Q,L, the bracket [B,Omega]=-kappa Omega, and Gamma invariance of the velocity one-form U.dx. The last follows by Cartan's formula from curl U=Omega and U.Omega=0. The quantities H,Q are C2, by momentum. No second derivative of the tails or of Gamma is assumed.

## 2. One-sided scalar comparison and full pressure Hessian

First work at a noninterior point y in E. Choose a transverse vector nu so that B(y),Omega(y),nu are independent. The C1 map

    (s,t,v)->Gamma_s Phi_t(y+v nu)

is a diffeomorphism from a small box onto a neighborhood contained in E intersect {Omega!=0}. Put l(v)=L(y+v nu). The scalar in this chart is exp(-at)l(v), so interior and boundary points of {L=0} on the transversal correspond exactly to those of the closed set Z={l=0}.

Let v1 be an endpoint of a complementary interval of Z, and take a fixed va in that interval on one side, with z=y+va nu. For v between v1 and va, consider

    gamma_v(w)=Phi_(tau(w))(y+w nu),
    tau(w)=a^(-1)log(l(w)/l(v)).

The ratio is positive on that interval. The curve is C1, its L value is the nonzero constant l(v), and dL(B)=-aL!=0. It stays in O with Omega nonzero. The rank identities imply H and Q are constant along this whole finite path, even if the path leaves the small chart. Therefore, with T(v)=a^(-1)log(l(va)/l(v)),

    H(y+v nu)=H(Phi_T z), Q(y+v nu)=Q(Phi_T z).

As v tends to v1 from this interval, T tends to positive infinity. The limits at the one fixed point z give

    H(y+v nu)=l(v)(1+o(1)),
    |Q(y+v nu)|<=C_z |l(v)|^q.                         (2)

The constants may depend on the chosen complementary interval and va. At y1=y+v1 nu the noninterior type gives H=dH=Q=dQ=0. Since H is C2, (2) implies |l(v)|<=C|v-v1|^2, and then |Q(y+v nu)|<=C|v-v1|^(2q). The one-sided quadratic Taylor expansion of Q thus gives D2Q(y1)[nu,nu]=0.

Every boundary point of Z is a limit of such complementary-interval endpoints: for wn outside Z tending to v1, the endpoint between wn and v1 lies in Z and tends to v1. Continuity of D2Q therefore gives the same normal quadratic coefficient at every boundary point, in particular at the initial v=0. Along the two joint-orbit curves dQ vanishes, so D2Q annihilates B and Omega. Its symmetry and the transverse coefficient then imply D2Q=0.

For a point y in O outside E, choose a finite vortex time with y'=Gamma_s y in E. Use Q composed with Gamma_s=Q and Q=dQ=0 at both points. The Taylor expansion under a C1 diffeomorphism gives

    D2Q(y)=D Gamma_s(y)^T D2Q(y')D Gamma_s(y).

This requires no D2 Gamma_s. Thus D2Q=0 on N, and continuity extends it to all of Cbar. The source's one-sided-germ statement also holds for any straight segment satisfying its explicit nonzero-L and endpoint-in-E hypotheses; that argument does not need a full transverse chart.

A precision limit is needed for the source Remark(ii): (2) controls each specified one-sided complementary interval. It does not give a uniform H/L limit on a transversal crossing infinitely many complementary intervals whose constants vary. No such uniform assertion is used to prove D2Q=0, because the endpoint-density argument uses only continuity of that Hessian.

## 3. Exact normal-Hessian transport and the common backward limit set

Since dH vanishes on the invariant critical set, its Hessian annihilates B and Omega. Write

    D2H=h U tensor U

there, with h continuous. Differentiate the integrated identity

    H composed with Phi_t-H=-a integral_0^t g composed with Phi_r dr

twice in the initial variable. All functions inside are C2 and the integration interval is finite. Their first differentials vanish at the points used; the Kelvin law and D2g=D2H-D2Q=D2H give, for f(t)=exp(-2at)h(Phi_t y),

    f(t)-f(0)=-a integral_0^t f(r)dr.

Therefore h(Phi_t y)=exp(at)h(y). Gamma invariance of H and of U.dx gives h(Gamma_s y)=h(y), using the same C1 Taylor composition as above. On any compact full Phi-invariant subset h is bounded along every full orbit, so its positive exponential law forces h=0 throughout that subset.

The backward carrier half-orbits are bounded. Let Lambda be the nonempty compact alpha-limit set of y0. Every point y=Gamma_s Phi_r y0 of N has this same alpha-limit set, since

    Phi_t y=Gamma_(exp(kappa t)s)Phi_(t+r)y0

and bounded Omega gives distance to Phi_(t+r)y0 at most sup|Omega| |s| exp(kappa t), tending to zero as t tends to negative infinity. Hence Lambda is a compact full Phi-invariant subset of Cbar, lies in the carrier core, and has D2H=D2Q=0. All points remain in O with U,B,Omega nonzero.

## 4. Poisson, invariant averages and the strain lower bound

The pointwise identities used by C45 follow directly from momentum, vorticity transport and divergence:

    Delta Q=U.curl Omega-2|S_U|^2,
    B(|U|^2/2)=-(1-c)|U|^2-U.grad Q-U.S_U U,
    B(|Omega|^2/2)=Omega.S_U Omega-|Omega|^2,
    B(|B|^2/2)=c|B|^2+B.S_U B.                       (3)

For the first identity, Delta P=-tr((DU)^2), Delta U=-curl Omega and Delta(|U|^2/2)=|DU|^2-U.curl Omega. The sum |DU|^2+tr((DU)^2) is 2|S_U|^2. The other identities follow by scalar multiplication, and the skew J terms cancel.

On Cbar, Delta Q=0, so U.curl Omega=2|S_U|^2 and curl Omega has nonnegative component along U/|U|. Let mu be any Phi-invariant probability on Lambda. The functions log|U|^2, log|Omega|^2, log|B|^2 are C1 near this compact set, bounded there, and have bounded flow derivatives. Invariance makes the integrals of those derivatives zero. With u=U/|U|, w=Omega/|Omega| and b=B/|B|, (3) yields

    integral u.S_U u dmu=-(1-c),
    integral w.S_U w dmu=1,
    integral b.S_U b dmu=-c.

Since u and w are orthogonal, complete them by e=u cross w. The trace-free property gives integral e.S_U e=-c as well. The pointwise matrix-norm inequality in this orthonormal frame and Jensen's inequality prove

    integral |S_U|^2 dmu >= (1-c)^2+1+c^2.

This does not treat b,w as orthogonal; their orthogonality is neither asserted nor needed.

## 5. Pulled-back Stokes and the two-ended annular exclusion

For j(theta,zeta)=Gamma_zeta Phi_theta y*, the derivatives are j_theta=B-kappa zeta Omega and j_zeta=Omega. Thus their cross product is aU. For the C1 form alpha=Omega.dx, (3) gives

    j^*d alpha=2a|S_U(j)|^2 dtheta wedge dzeta.

Stokes holds on any compact parameter domain with piecewise C1 boundary. One may justify it by smooth approximation of j in C1 and of alpha in C1. The boundary pullback of alpha and the interior pullback of d alpha then converge uniformly, so the smooth Stokes identities pass to the limit. No second derivative of j or first derivative of the pulled-back one-form is needed. No properness of a noncompact immersed leaf is needed for this compact-domain identity.

Suppose an annular joint leaf has j periodic in theta with period T0 and both open halves zeta>0 and zeta<0 lie in E. Write Circ(Z) for the integral of alpha over theta->j(theta,Z) in the direction of increasing theta. The counterclockwise boundary of [0,T0] times[Z1,Z2] gives

    Circ(Z1)-Circ(Z2)=integral 2a|S_U(j)|^2 dtheta dzeta>=0.

Thus Circ is nonincreasing. For any fixed nonzero Z, the closed curve c_Z is a compact subset of E, and Phi_t maps it to c_(exp(kappa t)Z), preserving its orientation. Actual C1 scattering on that compact curve gives length(Phi_t c_Z)<=C exp(ct), and its distance from0 is at least m exp(ct). The natural vorticity bound then gives

    |Circ(exp(kappa t)Z)|<=C exp(ct)exp(-(p+1)ct)
                              =C exp(-(1-c)t)->0.

Both signs of Z give zero limits at both ends of the real Z axis. Monotonicity implies Circ identically zero, hence S_U=0 on the annular leaf by the nonnegative integrand and continuity. Equation(3) now gives |Omega(Phi_t y)|=exp(-t)|Omega(y)|. This diverges backward, contrary to bounded backward orbits and continuous Omega. The annular configuration with both halves in E is excluded.

No claim that a half avoids the core is inferred from almost-everywhere volume information. No uncontrolled boundary term at infinity is dropped. The plane-strip identity in the source is also the same pullback calculation in coordinates Phi_theta Gamma_m y*: it needs separate control of the two integrals of Omega.B before integration over an unbounded strip.

## 6. Scope and source comparison

The entire 230-line C45 source was read before this independent reconstruction. Its Theorem54 and Corollaries55-56 are valid with the one-sided interpretation of the asymptotic remark noted in Section2. The source's C44 inputs are now independently confirmed, so their old SUBMITTED labels are historical. The calculations do not require running its symbolic algebra script.

C45 was written before A963/A970, which excludes all of its actual noninterior critical configurations at C2 for every finite omega. It nevertheless supplies a valid independent derivation of full-closure pressure flatness and the two-ended annular contradiction without using that exclusion. Its remarks listing critical planes or annuli meeting the core as the active open frontier must be updated to the stronger result. Open scalar-zero interiors and their supported flat boundaries remain outside C45.

This is a received substantive source from the existing configured model Theory Agent C agent, independently checked here. It is not a focused reply to the requested A963 stable-contraction audit, which remains pending; provider runtime is not independently attested. No new client or agent, computation or formal build was used.
