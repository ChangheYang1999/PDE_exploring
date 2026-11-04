# Exact source-positive extrema in the degree-one homogeneous family

## 1. Statement and scope

Fix 0<beta<1 and L>0, and put t=(beta-3)/2, k=t+2=(beta+1)/2, tau=t^2, D=k^2+2, H=tau(k^2+4)/D and gamma=4beta/D. For constant real vectors a,b, consider only the family

    U(rn)=r^t[k a-t(a.n)n+b cross n],
    (8pi/3)(D|a|^2+|b|^2)=beta L, r>0, n in S2.

The sphere has measure4pi. Set q=tr((DU)^2), M=integral_S2|DU(n)|_F^2/(beta L), A_inf^2=max_S2|DU(n)|_F^2 and rho=D|a|^2/(D|a|^2+|b|^2). If q(n)>=0 everywhere, then a,b are nonzero and

    rho_minus=D/(D+3tau)<=rho<=rho_plus=D/[2(k+1)].

Both endpoints lie strictly in(0,1), and rho_minus<rho_plus. Equality at either endpoint forces parallel axes. The interval is sufficient for parallel axes; no sufficiency is asserted for arbitrary axes.

Within this entire six-coefficient family under q>=0, the exact extrema are

    min M=H+2beta k(2-k)/[D(k+1)],
    min A_inf^2=(beta L/(4pi))*18tau/(D+3tau).

The first is attained precisely at parallel axes and rho_plus, the second precisely at parallel axes and rho_minus, up to rotation and choices of signs. No field attains both minima. Requiring q>0 everywhere gives the same two separate infima, with neither attained. A direction-independent |DU(n)|_F is incompatible with q>=0 in this nonzero family.

The parallel-axis extrema and approximations have smooth divergence-free completions on R3, equal to the tail for r>=2, satisfying E_0(R)=L R^beta for R>=2, E_z(R)=L R^beta+O_z(R^(beta-2)) at every fixed center, and D^jU=O(r^(t-j)) for each integer j>=0. They have smooth Poisson pressures but fail the full rotating profile equation for every real c,omega and any C1 pressure. These are kinematic family extrema, not extrema over all angular modes or actual Euler profiles.

This proof independently reconstructs source730957d0, all seven sections and40analytical obligations retained in `verification`. No LIT384-LIT386 theorem is used as a premise.

## 2. Complete family and pointwise matrix identities

Write P_a=k a-t(a.n)n and T_b=b cross n. Their radial components are2a.n and0. For a homogeneous field r^t(fn+w), div U=r^(t-1)[k f+div_S w]. Here the poloidal tangent part is k grad_S(a.n), and Delta_S(a.n)=-2a.n, so the divergence vanishes. The three real degree-one radial coefficients determine a, and the divergence relation determines their poloidal tangent part; the three toroidal coefficients determine b. Thus no degree-one coefficient is omitted.

Let C_b v=b cross v, s=(a cross b).n, and use tensor product u tensor v for the matrix u v^T. At r=1, direct differentiation gives

    D_P=t[k a tensor n-(a.n)I-n tensor a
                            -(t-2)(a.n)n tensor n],
    D_T=C_b+(t-1)(b cross n) tensor n.

In particular D_P n=tP_a and D_T n=tT_b. For a=|a|e3 in the meridional frame, with mu=e3.n and sigma=sqrt(1-mu^2),

    D_P=|a|t [[2mu,-sigma,0],[k sigma,-mu,0],[0,0,-mu]].

Squaring entries and taking trace squares, and using C_b^2=b tensor b-|b|^2I, gives

    |D_P|_F^2=tau[(1+k^2)|a|^2+(5-k^2)(a.n)^2],
    |D_T|_F^2=(1+tau)|b|^2+(1-tau)(b.n)^2,
    tr(D_P^2)=2tau[(k+3)(a.n)^2-k|a|^2],
    tr(D_T^2)=2[-t|b|^2+(t-1)(b.n)^2].

The cross pairings are different:

    D_P:C_b=t(k+1)s,
    D_P:((b cross n) tensor n)=tk s,
    tr(D_P C_b)=-t(k+1)s,
    tr(D_P((b cross n) tensor n))=-t s.

Consequently

    D_P:D_T=t(1+kt)s=t(k-1)^2s,
    tr(D_P D_T)=-t(k+t)s.

The full squares contain twice these pairings. A direct sign check takes n=e3,a=e1,b=e2: D_P has entries(1,3)=tk,(3,1)=-t, and D_T has entries(1,3)=t,(3,1)=-1, giving the displayed signs. This is an algebraic check, not a numerical sample.

Also P_a.T_b=k s. The velocity cross term and both derivative cross terms are odd in n, hence integrate to zero but need not vanish pointwise. Since integral_S2(n.v)^2=(4pi/3)|v|^2,

    integral_S2|P_a+T_b|^2=(8pi/3)(D|a|^2+|b|^2),
    integral_S2|D_P+D_T|_F^2
       =(8pi/3)[tau(k^2+4)|a|^2+(tau+2)|b|^2].

Thus M=rho H+(1-rho)(tau+2)=H+gamma(1-rho).

## 3. Necessary source constraints and their equality cases

Pointwise, the complete source is

    q(n)/2=tau[(k+3)(a.n)^2-k|a|^2]
            -t|b|^2+(t-1)(b.n)^2-t(k+t)(a cross b).n.

If a=0, evaluation along b gives negative source. If b=0, evaluation perpendicular to a gives negative source. Normalization excludes both zero, so a,b are nonzero.

Along n=b/|b|, the cross term is zero and

    0<=q(n)/2=tau[(k+3)(a.n)^2-k|a|^2]-|b|^2
                  <=3tau|a|^2-|b|^2.

This gives |b|^2<=3tau|a|^2, or rho>=rho_minus. Equality in that ratio forces |a.n|=|a|, hence parallel axes.

If a cross b is nonzero, evaluate at its two opposite unit directions. Both scalar products with a,b vanish, so positivity at both points gives

    -tau k|a|^2-t|b|^2>=|t(k+t)| |a cross b|.

Divide by the positive number -t to obtain

    |b|^2+tk|a|^2>=|k+t| |a cross b|.

For parallel axes, evaluation at any perpendicular direction gives the same bound with zero right side. Hence |b|^2>=-tk|a|^2, or rho<=D/(D-kt)=rho_plus. Since |k+t|=1-beta>0, equality forces a cross b=0. The interval has positive length because3tau+kt=t(4k-6)>0. The endpoint denominators exceed D and all terms are positive.

For a=Ae,b=Be with |e|=1, q/2 is affine in mu^2=(e.n)^2. Its values at mu=0 and mu^2=1 are -tau kA^2-tB^2 and3tau A^2-B^2. Nonnegativity of both is necessary and sufficient; strict positivity of both gives exactly the open rho interval. For arbitrary axes strict positivity likewise makes both necessary endpoint inequalities strict.

## 4. The two exact minimizers

Since gamma>0, M=H+gamma(1-rho) is strictly decreasing in rho. The largest admissible rho is rho_plus, forcing parallel axes. Conversely its parallel field is admissible. Substituting1-rho_plus=k(2-k)/[2(k+1)] gives the stated integrated minimum.

For the peak evaluate instead along n=a/|a|. The mixed Frobenius term vanishes and tau>1 gives

    |DU(n)|_F^2=6tau|a|^2+(1+tau)|b|^2
                          +(1-tau)(b.n)^2
                 >=6tau|a|^2+2|b|^2.

The normalization therefore implies

    A_inf^2>=(beta L/(4pi))[9tau rho/D+3(1-rho)].

The bracket strictly increases with rho, because3tau-D=2(k-1)(k-5)>0. Its smallest admissible value occurs at rho_minus and equals18tau/(D+3tau). Equality requires that endpoint, already forcing parallel axes.

Conversely, for the parallel endpoint |b|^2=3tau|a|^2, the coefficient of mu^2 in the gradient square is

    tau|a|^2[8-k^2-3tau]
       =-4tau|a|^2(k^2-3k+1)>0.

Indeed k^2-3k+1 equals -1/4 at k=1/2 and decreases on(1/2,1). The maximum is at the poles, where the lower bound is attained. This proves the complete equality classification. Since the two endpoint ratios differ, there is no simultaneous minimizer. Parallel fields approaching either endpoint from the open interval prove the separate strict-source infimum statements.

## 5. Constant sphere norm is incompatible with source positivity

The only odd part of |DU(n)|_F^2 is2t(k-1)^2(a cross b).n. Direction independence forces a cross b=0, since t and k-1 are nonzero. Pure poloidal and pure toroidal nonzero fields have nonzero quadratic coefficients, of opposite signs, so both vectors must be nonzero and parallel. Their remaining quadratic coefficient vanishes precisely at

    |b|^2/|a|^2=tau(5-k^2)/(tau-1),
    rho_d=(tau-1)D/(7tau-D).

The denominator is positive since it equals(tau-1)D+tau(5-k^2). Section4 gives5-k^2>3(tau-1), so this ratio is strictly greater than3tau. Thus rho_d<rho_minus and the source at a pole is2(3tau|a|^2-|b|^2)<0. No assertion about a larger angular family follows.

## 6. Exact-energy completion and all centers

For the required parallel fields choose a=Ae,b=Be with A,B>0; signs do not affect the attainable values. Put mu=e.n and define the solenoidal field

    V_g=2g(r)mu n+[rg'(r)+2g(r)]grad_S mu.

Its divergence is zero by direct differentiation. It equals the required poloidal tail for g=r^t, and equals2g e near0 when g is constant. Interpolate smoothly from2^t on r<=2-epsilon to r^t on r>=2. Also interpolate w from2^(t-1) to r^(t-1) on that same annulus. A cutoff with derivative O(1/epsilon) multiplies endpoint differences O(epsilon), so g,g',w stay bounded there. The transition energy tends to zero.

The base field A V_g+B w(e cross y) is smooth and divergence-free, with pointwise orthogonal parts. As epsilon decreases its energy within radius2 tends to

    (8pi/3)2^beta[2A^2+B^2/5].

The desired value is(8pi/(3beta))2^beta[DA^2+B^2]. Their difference is positive because D-2beta=tau>0 and beta<5. Choose epsilon with positive deficit Delta. For a smooth nonnegative radial psi supported in r<1/2 and equal to1 near0, add lambda psi(e cross y). The change in energy is

    lambda^2 I+2lambda B0,
    I=integral psi^2|e cross y|^2>0,
    B0=B2^(t-1) integral psi|e cross y|^2>0.

It is continuous and strictly increasing from0 to infinity for lambda>=0, so exactly one positive lambda fills Delta. The poloidal cross term vanishes; the toroidal cross term is retained. Exterior sphere energy is beta L r^(beta-1), hence E_0(R)=LR^beta for R>=2. Smoothness and D^jU=O(r^(t-j)) follow from the fixed core and homogeneous tail.

The poloidal part is even, the toroidal part odd, and their pointwise product zero. Therefore |U|^2 is even. The first center derivative of E_z(R) at z=0 is the boundary integral of |U|^2 n and vanishes. Its second center derivatives, uniformly for z in a fixed bounded set, are boundary integrals of derivatives of |U|^2, bounded by O(R^2 R^(2t-1))=O(R^(beta-2)). Taylor's theorem proves the all-center remainder. The corresponding logarithmic gradient functional has G_0(R)=beta LM log R+O(1). A fixed translation changes the exterior gradient-square density by O(r^(2t-3)); multiplying by r^(4-beta) gives O(r^-2), integrable. Thus G_z-G_0=O_z(1), and the full spatial peak amplitude is also unchanged by a fixed translation.

## 7. Pressure, arbitrary rotation axis and review status

The completed source is smooth and q=O(r^(beta-5)). Its Newton potential

    P(y)=integral_R3 q(x)/(4pi|y-x|) dx

is absolutely convergent: the local kernel singularity is integrable, and at infinity the radial integrand is O(r^(beta-4)). Distributionally -Delta P=q, and local elliptic regularity gives a smooth pressure. This proves only the Poisson relation.

Let the prescribed rotation be Jv=e3 cross v. Near0 the completed field is U=d+C_zeta y with

    d=2A2^t e,
    zeta=[B2^(t-1)+lambda]e!=0,
    C_zeta v=zeta cross v.

For the pressure-free momentum residual

    F=(1-c)U+[((cI-omega J)y+U).grad]U+omega JU,

the linear coefficient is C_zeta+C_zeta^2+omega(J C_zeta-C_zeta J); all omitted terms are constant. The c terms cancel, C_zeta^2 is symmetric, and the commutator is C_(e3 cross zeta). Consequently

    curl F=2[zeta+omega(e3 cross zeta)].

Its scalar product with zeta is2|zeta|^2>0 for every real omega. The curl of a C1 pressure gradient is zero distributionally, so no such pressure repairs momentum, for any real c or omega. The core source is -2|zeta|^2<0; this does not conflict with positive exterior source.

All source sections and40obligations were read. The existing configured model A comparison is reconciled in Section8; actual provider execution is independently unattested. No mathematical computation, numerical optimization, formal build or fresh source retrieval was used. Full-mode optimality, automatic source positivity and the arbitrary-rotation Euler conjecture remain OPEN.


## 8. Existing comparison and verified refinements

The complete eleven analytical points and four remarks of the existing A comparison in the team records, SHA256 recorded in the team records, were read against Sections1-7. They agree. Its symbolic scripts, sampled signs, claimed run count and execution history are not independently certified here. The source remains the seven-section version730957d0. The gradient grad_S in Section6 is the unit-sphere gradient, grad_S mu=e-mu n, at every radius.

The necessary rho interval is not sufficient for nonparallel axes. Choose nonzero perpendicular a,b with the normalized ratio rho=rho_plus. Then |b|^2+tk|a|^2=0, while (1-beta)|a cross b|>0. At one of the two normal directions, the source inequality in Section3 fails strictly. By continuity it still fails for perpendicular a,b with rho strictly inside the interval and sufficiently close to rho_plus. Normalization can be maintained continuously by rescaling their two lengths. This is an exact obstruction, independent of any sampled offset.

The amplitude constants have the strict order

    H < M_d < 18tau/(D+3tau) < 9tau/D,
    M_d=H+gamma(1-rho_d).

Indeed 0<rho_d<rho_minus<1. For a parallel field the squared pole value, divided by beta L/(4pi), is phi(rho)=9tau rho/D+3(1-rho). This is strictly increasing. At rho_d the gradient norm is constant, so its pole value equals its spherical mean: phi(rho_d)=M_d. At rho_minus, phi(rho_minus)=18tau/(D+3tau). Finally 18tau/(D+3tau)<9tau/D is equivalent to D<3tau, already proved in Section4. Thus the source-positive family minimum lies strictly above the constant-norm aligned-family value and strictly below the pure-poloidal peak. The endpoint-gradient theorem is not contradicted, since M(rho_minus)>H.

The exact minima in this review belong only to the complete homogeneous degree-one family with pointwise nonnegative exterior source. The smooth completions show attainability in that family and give upper bounds for infima over any larger kinematic class containing them. They do not establish such larger-class infima, do not make source positivity automatic, and are not Euler counterexamples. The main arbitrary-rotation conjecture remains OPEN.
