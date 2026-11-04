# Regular nodal periods and critical angular zeros

Status: A844-A850 CONFIRMED; unrestricted nodal exclusions OPEN, A851. This is the independent audit of the complete revised Theory Agent C C43 manuscript, including its signs and its C1 collar argument.

## 1. Setting and exact inputs

Assume U in C2(R3), P in C1(R3), 2/5<c<1/2, omega real, and

    div U=0, (1-c)U+DU(Ax+U)+omega JU+grad P=0,
    U.curl U=0,
    |U|<=C(1+|x|)^(-p), |DU|<=C(1+|x|)^(-p-1),

where Jx=(-x2,x1,0), A=cI-omega J, p=(1-c)/c, a=1-2c and lambda=p-1=a/c. Let D=R3 minus{0}; V and W=curl V are the actual tails. Write k=(Ax).V, E=grad k and K=k restricted to S2. A538 and A568 give V in C^(1,alpha) for each alpha<1 and

    V(exp(sA)x)=exp(-s)exp(sA)V(x),
    W(exp(sA)x)=exp(-(1+c)s)exp(sA)W(x),
    k(exp(sA)x)=exp(-as)k(x),
    E(exp(sA)x)=exp(-s)exp(sA)E(x),
    (Ax).E=-ak, E=-aV+Ax cross W,
    E cross V=kW, W.E=0, curl(V/k)=0 on {k!=0}.      (1)

Only these identities, div V=0 and the actual exclusion A701 of nonconstant periodic W curves are needed. No pressure-tail identity or nodal vorticity-vanishing premise is used. The latter exclusion requires an actual profile, and cannot be asserted for an abstract homogeneous V.

Let pi:D->S2 be the twisted projection x=exp(sA)pi(x), exp(cs)=|x|. Each component C of {k!=0} is homeomorphic to U_C times R, where U_C=C intersect S2 is a component of {K!=0}. Its boundary relative to D is the cone over boundary U_C. At a zero of K, E!=0 if and only if grad_T K!=0: a radial E perpendicular to Ax must vanish since (Ax).x=c|x|^2.

## 2. Signed band flux

For any component U of {K!=0} and 0<t1<t2,

    integral_{U intersect {t1<|K|<t2}} G_r dA=0,
    G_r(w)=w.W(w).                                 (2)

Indeed, alpha=V.dx restricted to S2 is C1, and theta=alpha/K is C1 and closed on {K!=0}. Thus d alpha=dK wedge theta=G_r dA there. If phi is continuous with compact support in (0,infinity), put Psi(s)=integral_0^|s| phi(t)dt. The form Psi(K)theta has compact support in U, because Psi vanishes near0 and the sphere is compact. Stokes gives

    0=integral_U d(Psi(K)theta)
     =sign(K) integral_U phi(|K|)G_r dA.

Approximate interval indicators by bounded continuous functions and use dominated convergence. This proves(2); letting t1 decrease to0 also proves zero flux over 0<|K|<t2. No regularity of these sublevel boundaries is assumed.

## 3. A constant normal multiplier on every regular arc

Let Gam be any connected open arc or closed component of the regular zero set {K=0,grad_T K!=0}. Then there is one real constant sigma with

    V=sigma E on the entire twisted cone over Gam,
    (1+a sigma)E=Ax cross W.                        (3)

This includes arcs meeting W=0. To prove spatial constancy without differentiating E, choose C1 coordinates (u,v) on S2 with K=u. Write the pullback of alpha as f du+g dv and of G_r dA as H du wedge dv, all with continuous coefficients. At u=0, (1) gives V=sigma(v)E, hence f(0,v)=sigma(v), g(0,v)=0. On u>0 the form (f/u)du+(g/u)dv is closed.

Stokes on [epsilon,b0] times[v1,v2] gives

    integral_epsilon^b0 (f(u,v2)-f(u,v1))du/u
     =integral_v1^v2 [g(b0,v)/b0-g(epsilon,v)/epsilon]dv. (4)

Stokes for alpha on [0,epsilon] times[v1,v2] makes integral g(epsilon,v)dv=O(epsilon), since f,H are bounded. Thus the right side of(4) is bounded as epsilon decreases to0. The left side equals

    (sigma(v2)-sigma(v1))log(b0/epsilon)+o(log(1/epsilon)).

It follows that sigma(v2)=sigma(v1). Connectivity and the common homogeneity of V,E give(3) on the whole cone. Stokes is valid in these C1 coordinates: approximate the charts in C1 by smooth charts, or mollify their continuous pulled-back forms and continuous distributional exterior derivatives on smaller rectangles. No C2 coordinate change is required.

If sigma=-1/a, W is parallel to Ax. Otherwise, with a continuous unit tangent e to Gam, write on S2

    W=alpha0 Aw+beta0 e,
    G_r=c alpha0,
    N:=|grad_T K|=c|beta0|/|1+a sigma|.              (5)

Here beta0 never vanishes. Indeed Aw and e span E perpendicular, and Aw cross W=(1+a sigma)E!=0. The tangential part of Aw cross e is c w cross e, since Jw and e are tangent to S2. This proves(5).

## 4. Collar periods and vortex displacement

Suppose gam is a closed connected regular zero component. It has a C1 collar chi(u,v), K=u, v in R/LZ, obtained by flowing a smooth vector field transverse to grad_T K. Orient v by e, let n=grad_T K/N and delta=w.(n cross e) in {1,-1}. On either side of the collar, the period P of theta around the loop u=t is independent of t and satisfies

    P=delta integral_gam G_r/N dl.                 (6)

The orientation e is kept fixed on both sides, so P is the same on both sides. To check the sign, use u=epsilon K with epsilon=+1 or -1, and write chi*alpha=epsilon(f du+g dv), chi*(G_r dA)=epsilon H du wedge dv. Stokes on the full annulus gives

    tP=integral_0^t integral_0^L H(u,v)dv du.

At u=0, chi_v=e and chi_u=(epsilon/N)n+b e. Thus H(0,v)=delta G_r/N, and continuity yields(6).

When sigma!=-1/a, formula(5) also gives

    beta0=-delta(1+a sigma)N/c,
    integral_gam alpha0/beta0 dl=-P/(1+a sigma).    (7)

If P=0, define s(l)=integral_0^l alpha0/beta0. It is C1 and L-periodic. The curve z(l)=exp(s(l)A)gam(l) is a nonconstant closed C1 curve, and by(1)

    z'(l)=exp((1+c)s(l))/beta0(l) W(z(l)).

Its scalar factor is continuous, never zero and has one sign. Reparametrizing by its integral gives a nonconstant periodic W curve, forbidden by A701. Therefore every actual closed regular component with sigma!=-1/a has P!=0. In the general nonzero-period case, (7) is the exact change in dilation time per angular turn.

## 5. Exact potentials cannot diverge positively at every boundary point

For completeness the A665 flux input is rechecked here. Under just the kinematic identities and divergence in Section1 with p<2, no component C of {k!=0} admits a potential Gamma with

    grad Gamma=cV/k,
    Gamma(x)->+infinity as x->x0 within C
    for every x0 in the boundary of C relative to D. (8)

Homogeneity gives Gamma(exp(sA)x)=Gamma(x)+cs, so Gamma(x)=Gamma(pi(x))+log|x|. The assumed boundary divergence and angular compactness give a finite attained minimum m of Gamma on U_C. Fix gamma0>m and a radial cutoff chi_epsilon, zero for r<=epsilon and one for r>=2epsilon. The function (gamma0-Gamma)_+ chi_epsilon, extended by0 outside C, is Lipschitz and compactly supported away from the relative boundary: (8) excludes finite boundary limit points and Gamma>=m+log r bounds r above on its support.

Integrate div V against this test to get

    integral_{C intersect {Gamma<gamma0}} chi_epsilon c|V|^2/k
      =integral (gamma0-Gamma)_+ V.grad chi_epsilon.

The right side has magnitude O(epsilon^(2-p)log(1/epsilon)), tending to0 because p<2. The left side has constant sign and contains a fixed strictly positive integral of c|V|^2/|k| on some interior ball. This contradiction proves(8). No unproved vanishing of a flux at a nodal boundary is used.

Near any point x0 of the cone over a regular arc, a potential as above satisfies

    Gamma(x)=c sigma log|k(x)|+o(log(1/|k(x)|)).     (9)

In the chart of Section3, integrate dGamma=c((f/u)du+(g/u)dv) in u from a fixed u0>0. The relation f(u,v)=sigma+o(1) is uniform near the chosen v0. The integral gives(9), and bounded radial factors handle arbitrary x approaching x0 in D. In particular sigma<0 forces positive divergence there.

## 6. The nodal-component theorem and critical zeros

There is no component C of {k!=0} such that all boundary points of U_C are regular zeros of K and every period of V.dx/k in C vanishes.

Indeed, zero periods provide the potential Gamma. The boundary of U_C is compact and relatively open and closed in the regular zero set: a regular level chart has a connected half-neighborhood belonging to U_C, and its whole intervening nodal arc is therefore boundary. A compact regular one-manifold has finitely many components, so this boundary is a finite union of closed regular curves, possibly empty. Each has collar period0. Section4 forces sigma=-1/a on each curve; Section5 then forces Gamma to tend to positive infinity at every relative boundary point. This contradicts(8). If the boundary is empty, U_C=S2, and the same flux proof applies with a vacuous boundary condition.

Consequently K has a critical zero on S2. More precisely, each side of every closed regular zero curve contains a critical zero. To prove the second assertion, its two complementary components are open disks. Suppose a chosen disk D1 has only regular zeros. Since the boundary curve has a regular collar containing no other zero component, the zeros inside D1 form a compact regular one-manifold, hence finitely many disjoint circles. If there are none, D1 itself is a zero-free disk component. Otherwise choose an innermost of those finitely many circles. Its disk interior contains no zeros and is a component of {K!=0}. In both cases it is simply connected and its boundary is regular. Its periods vanish, contradicting the theorem.

If K had no zero, the whole sphere would give the same contradiction. If all its zeros were regular, compactness would give a closed regular component, to which the preceding paragraph applies. Thus some zero is critical. The trivial tail K=0 is included.

Under the additional nodal hypothesis {k=0} subset {W=0}, equation(1) gives E=-aV at a zero. Therefore critical angular zeros are exactly velocity zeros there. One lies on S2, and one lies on each side of every closed regular nodal curve. This recovers the zero-free exclusion without using the stopped-flow mass argument.

## 7. A kinematic check and the actual-profile limitation

At omega=0 define, on D,

    V=(2-p)r^(-p)e3+p x3 r^(-p-2)x.

Direct differentiation gives div V=0,

    W=p(3-p)r^(-p-2)e3 cross x, V.W=0,
    k=2c x3 r^(-p).

The regular zero set is the equator, sigma=(2-p)/(2c)>0, G_r=0 and P=0. On each half-space a potential of cV/k is

    Gamma=((2-p)/2)log|x3|+(p/2)log r.

It tends to minus infinity at the equatorial boundary. The equatorial W curves are circles. Thus the kinematic potential-flux input alone cannot eliminate positive sigma; the actual periodic-curve exclusion is essential. This field is not claimed to solve the pressure-tail identities or arise from an actual profile.

## 8. Dependencies and open scope

The complete revised in the team records and the complete proof of its A665 flux input were read and checked. The source supplies an existing configured model agent derivation plus an the external referee (a second model); runtime remains unattested. The independent argument above checks the collar sign, low regularity, finite boundary-component count and innermost-disk step. No computation is needed. Source versions and hashes are retained in verification.

Regular arcs ending at critical nodes, and closed regular curves with nonzero periods, are not excluded by this theorem. The pressure-based A837 result and actual-sheet A810-A818 are additional inputs, not implicit premises of this proof. No unconditional conclusion about arbitrary smooth decaying profiles follows, and no general sign restriction on sigma is obtained.
