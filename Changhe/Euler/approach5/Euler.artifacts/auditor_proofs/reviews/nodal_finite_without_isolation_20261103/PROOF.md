# Finite nodal jets without an isolated-leading assumption

Status: independent audit of all five LIT211 sections and all eight LIT213 sections. This is a conditional local theorem and its global consequence. It does not assert existence of a supported local nodal center.

## 1. Exact hypotheses and conclusions

Fix 2/5<c<1/2 and finite real omega. Put Jx=(-x2,x1,0), A=cI-omega J, X=Ax, a=1-2c, b=2(1-c), q=b/a>6, p=(1-c)/c. Suppose U in C2(R3;R3), P in C1(R3), div U=0, and

    (1-c)U+DU(Ax+U)+omega JU+grad P=0,
    U.curl U=0,
    |U(y)|<=C(1+|y|)^(-p), |DU(y)|<=C(1+|y|)^(-p-1), C<infinity.

Let V,W=curl V,P2 be the actual tails, k=X.V and S=P2-|V|^2/2. At x0!=0 assume V=DV=0, V is smooth nearby with finite first nonzero order m>=2, and the local nodal condition holds: k=0 implies W=0 on a neighborhood. There is no support, pressure-value or leading-isolation assumption.

In oriented transverse coordinates (t,s,z3), e3=X0/|X0|, N=m+1, the conclusion is

    V_m=(-psi_s,psi_t,0), psi=r^N M cos(N(theta-theta0)), M!=0,
    k_N=(a/N)r^N g'(theta), g=M cos(N(theta-theta0)).

The full leading velocity is therefore nonzero off the transverse origin. On a fixed corresponding sphere patch O,

    integral_(O intersect {|k|<tau}) |W| dA <= C0 tau^(1+1/N).

With the global nodal condition and these smooth finite-order assumptions at every supported common flat pressure zero T0, the profile is zero. Constants and m may vary with the point.

## 2. Local identities and the general leading term

Poisson, -Delta P2=tr((DV)^2), makes P2 smooth wherever V is smooth: a localized smooth Newtonian potential leaves a harmonic difference. The established tail equations give divergence zero, V.W=0,

    DV X=-[(1-c)I+omega J]V, grad k=X cross W-aV,
    X.grad k=-ak, X.grad S=-bS,
    grad k cross grad S=0 on {W!=0}.

Consequently S=D_*|k|^q on any connected open region where k and W are nonzero. The leading homogeneity makes V_m independent of z3. Divergence supplies homogeneous polynomials psi of degree N and chi of degree m with

    V_m=(-psi_s,psi_t,chi), W_(m-1)=(chi_s,-chi_t,Delta psi).

The exact identity grad k cross V=kW restricts on z3=0 to

    C.grad f=f div C, C=(V2,-V1), f=k, div C=W3.       (2.1)

On every zero of f, the nodal condition gives W=0 and grad_(t,s) f=-a(V1,V2).

## 3. A single wedge excludes chi

If chi is nonzero, there is an angular interval with nonempty interior on which |chi| is bounded below on the unit circle. Its homogeneous radial derivative gives |grad chi|>=m|chi| there. Taylor expansion yields |k| comparable to r^m and W!=0 in a sufficiently small punctured wedge. Its product with a short X-flow interval is open and connected and retains both nonvanishing conditions by exact homogeneity. The constant D_* above is therefore one finite constant there, giving |S|<=C1 r^(mq) on the transverse wedge.

In particular S(x0)=0. If a first scalar Taylor term H_l had l<=2m, its homogeneity would give partial_3 H_l=0. Since mq>2m, the wedge bound makes this planar polynomial vanish on an open angular sector, which is impossible for a nonzero polynomial. Thus all S terms through2m vanish.

The leading pressure equation now says

    div V_m=0, -Delta(|V_m|^2/2)=tr((DV_m)^2).

Apply A1006 to the polynomial pair v=V_m, pi=|V_m|^2/2 on a full ball centered at0. It is smooth, v=curl v=0 at0, and s=pi-|v|^2/2 is identically zero. In the A1006 form with alpha=1/2, epsilon=1/8 is strictly below alpha/[2(1+alpha)]=1/6, and s-s(0)>=-epsilon|v|^2 holds on the entire ball. That confirmed local pressure theorem forces v=0 nearby, contradicting the nonzero leading term. Therefore chi=0 and psi!=0. This argument never needs all transverse directions to be vortical.

## 4. The scalar coefficient and a nodal characteristic

If g in psi=r^N g is a nonzero constant, Delta psi=N^2g r^(N-2) has no punctured transverse zero. The same holds for W on a small punctured disk and its connected flow tube. The nodal condition makes k nonzero there; one constant law extends by continuity across the central orbit to a full ball, with |S|<=C|V|^q. Since q>2 this implies the A1006 deficit with epsilon=1/8 after shrinking. It contradicts finite nonzero order. Thus g is nonconstant.

Write the first possible transverse scalar term as H_N=r^N h, possibly zero. Equation(2.1) at degree2N-2 gives g'h'=g''h. On an interval where g'!=0, h=Dg'. Both are trigonometric polynomials, so this equality holds on the full circle with one constant D.

Choose theta0 at a positive maximum of |g|, set g0=g(theta0)!=0 and sigma=g''/(Ng0)<=0. The polar C equation admits a radial curve theta=theta0+z(r), z=O(r): after division it is

    r z'=sigma z+z^2G(z)+rH(r,z).

On the normed space sup |z(r)|/r, use

    z(r)=r^sigma integral_0^r [s^(-sigma-1)z(s)^2G(z(s))
                                     +s^(-sigma)H(s,z(s))] ds.

The constant H term has norm at most ||H||/(1-sigma); the quadratic and difference terms have bounds C r0 on a fixed ball. A sufficiently large ball and small r0 give a contraction. The fixed point solves the equation for r>0.

On this curve f=O(r^(N+1)), but (2.1) gives r df/dr=(nu+O(r))f with nu=N+g''/(Ng0)<=N. A nonzero solution would have f=C2 r^nu exp(O(r)), C2!=0. Hence f=0 along the entire curve. The nodal condition and the leading W3 term imply g''(theta0)=-N^2g0.

## 5. Harmonicity, normalization and weighted flux

The exact interpolation formula proved in A1115/A1136 has weights at theta_j=pi j/N

    w0=-(2N^2+1)/6, wj=-(-1)^j/[2 sin^2(pi j/(2N))], j>0,
    T''(0)=sum wj T(theta_j), sum |wj|=N^2.

All weights are nonzero. After shifting theta0 and choosing g0>0, equality g''=-N^2g0 forces g(theta_j)=g0(-1)^j. Discrete Fourier interpolation leaves only an undetermined sin(Ntheta) term. Its addition would make the supremum exceed g0 unless its coefficient were zero. Thus psi is the claimed harmonic polynomial.

At the nodal characteristic, the exact gradient equation gives partial_theta f=-a N g0 r^N+O(r^(N+1)); the Taylor coefficient Dg' gives -D N^2g0 r^N+O(r^(N+1)). Therefore D=a/N. This coefficient has2N simple angular nodes. Uniform angular C1 Taylor estimates give exactly2N smooth nodal curves theta_j(r), and

    |f|>=d r^N |theta-theta_j(r)|,
    |W|<=C3 r^m |theta-theta_j(r)|

on fixed small arcs. The second estimate uses harmonic cancellation of the order m-1 curl, its angular derivative bound O(r^m), and W=0 on the exact nodes.

The inner disk r<=C4 tau^(1/N) contributes O(tau^((m+2)/N)). The outer contribution is at most

    C5 tau^2 integral_(C4 tau^(1/N))^r0 r^(m+1-2N) dr
        =O(tau^(1+1/N)).

Since (m+2)/N=1+1/N, both agree. The smooth X-section map to the sphere has bounded Jacobian and scales k and |W| by bounded positive factors, preserving this estimate. These arguments reproduce and recheck the parts of A1136-A1137 that did not require initial isolation.

## 6. The global nodal conclusion and LIT211

Under the global nodal condition, if U!=0 the confirmed actual joint-flux bound is J(tau)>=c0 tau, where J integrates |W| over |k|<c1tau, |S|<c2tau^q on the sphere. Section5 gives o(tau) on a fixed patch at each T0 point. The A1055-A1057 localization gives fixed o(tau) patches elsewhere, including regular scalar zeros and nonflat saddles. A finite sphere cover gives J=o(tau), a contradiction. There is no uniform-order requirement.

All five LIT211 sections were also checked. Its original isolated-leading assumption makes each boundary point of E0=supp(1_Z V) an isolated full angular V zero, forbidden by A1133. Thus E0 is empty or full. The empty case follows from the preceding flux proof (or A1138); full support gives global k=0 by continuity and invokes A1119. Its dependencies are now confirmed, so the older FO theorem is confirmed too. Its final degenerate-leading caveat describes the reach of that older argument and is superseded by A1151, which removes that premise.

## 7. Supported versus unsupported local centers

For actual supported T0 centers, A1150 now says every smooth finite-order point lies inside the interior of E0. Under the global nodal premise E0 is empty, so such a center cannot occur. This makes the conditional local flux implication compatible with the shorter global proof, rather than an existence result. LIT213 does not require support locally, and nothing here rules out all unsupported local irrotational zeros.

## 8. Verification and scope

All five LIT211 and eight LIT213 sections were read and compared with the full eleven-section A1133-A1138 proof. The new wedge step is justified on a three-dimensional open flow tube before applying its scalar constant. The polynomial pressure lemma is used on a full ball with its numerical threshold checked exactly. No numerical computation, formal build or new model client is used.

The existing configured model coordinator supplied a focused comparison for A1139-A1143, but the new wedge proof still awaits that same kind of focused response. Its runtime identity remains unattested. The unrestricted bare-decay/arbitrary-helicity conjecture remains open; local smoothness and finite order are extra premises.
