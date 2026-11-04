# Pressure means and forcing signs at a common flat orbit

Status: CONFIRMED A2127-A2132 at the exact stated scope; extensions OPEN A2133. This is a local conditional theorem, not an exclusion of all common flat zeros.

## 1. Exact hypotheses and conclusions

Let 0<c<1/2, omega in R, Jx=e3 cross x, A=cI-omega J, X=Ax, L=(1-c)I+omega J, a=1-2c, b=2(1-c), eta=a/b and m=1/c. Let x0!=0. Let G be an X-flowbox whose central orbit segment is Gamma, containing x0, and whose transverse section is a disk. Let V and S be smooth on G, with W=curl V, E=|V|^2 and P=S+E/2. Assume

    div V=0, X.V=0, X.grad V=-LV, X.grad S=-bS,
    X cross W=aV, W.grad S=0,
    -Delta P=T, T=tr((DV)^2),
    S<0 on G minus Gamma, S=0 on Gamma,
    every derivative of V and S vanishes at x0.

Choose r0>0 with the closed ball B_r0(x0) contained in G. For 0<r<r0 let M(r) be the mean of P on the Euclidean sphere centered at x0. On G minus Gamma write H=-S>0 and R=E/H.

The conclusions are:

1. If T>=0 on B_r0, then M(r)<0 for every 0<r<r0, and every such sphere has an off-Gamma point with R<2. If T<=0, all these inequalities reverse.
2. If M(r_j)>=0 along some sequence r_j tending to zero, T<0 at points arbitrarily close to x0. If M(r_j)<=0, T>0 at such points. The same conclusions follow from P>=0 or P<=0, respectively, near x0.
3. Exactly one of these alternatives occurs: M is strictly positive on an initial interval; M is strictly negative on an initial interval; or M has zeros tending to zero. They imply, respectively, negative T values approaching x0, positive T values approaching x0, or both signs approaching x0. In particular T cannot vanish on a neighborhood.
4. If omega=0, 2/5<c<1/2, and the period of H^(-eta)V.dx about Gamma is zero, T>0 at points approaching x0. Under the sequence condition M(r_j)>=0, both signs approach. A sufficient period condition is a bound R(|x0|n)<=C rho_j^(-N) on every full geodesic circle of radius rho_j tending to zero about n0=x0/|x0|, with fixed finite C,N.

The statements concern the displayed local equations. No assertion derives a sign condition, a period condition, or a smooth common-flat germ from a global Euler profile.

## 2. Why pressure cannot vanish on a neighborhood

The pressure P is flat at x0 because S and V are. The flow identity V(exp(tA)x0)=exp(-tL)V(x0) gives V=0 on Gamma. Thus P=0 there. Off Gamma, P=H(R/2-1).

Suppose P vanished on a ball about x0. Since X(x0)!=0, choose a smaller central flowbox G' inside that ball. There S=-E/2, so H=E/2>0 off its central orbit, and R=2. The triple-product identity gives

    grad H cross V=(b/a)H W,
    curl(H^(-eta)V)=0.

Consequently the normalized form alpha=E^(-eta)V.dx is closed off the central orbit, being the constant multiple 2^(-eta)H^(-eta)V.dx. Define alpha=0 on the orbit. Its magnitude is |V|^(1-2eta), and 1-2eta>0. Flatness and the smooth flow identity make this magnitude vanish to every transverse order, uniformly on compact orbit segments. Integration by parts outside a tube of radius epsilon has boundary error at most C epsilon sup|alpha|, which tends to zero. Hence alpha is continuous and distributionally closed on all of G'.

Here is the exact previously confirmed analytic dependency, A1467-A1468: under the smooth homogeneity, divergence and X.V=0 identities, a continuous distributionally closed alpha of this form and a flat V at x0 imply V=0 on a smaller flowbox. Its proof first constructs a C1 potential psi with grad psi=alpha and X.psi=0. The identity (1-2eta)(m-1)=1 yields

    V=|grad psi|^(m-2)grad psi.

In flow coordinates, divergence becomes a planar m-Laplace equation with a smooth positive metric and smooth first-order drift. Smooth isothermal coordinates reduce it to the precise planar strong unique-continuation theorem of Guo and Kar, with locally Lipschitz drift. The potential and its gradient are flat, so the theorem makes psi constant. The primary theorem and the first-order proof were previously checked in A1437-A1440; the full flow-coordinate derivation is reread and pinned here in flat_ratio_equation_20261103, Sections7-9. The coefficient is the smooth background geometric weight, not an uncontrolled function of H.

Applying that dependency gives V=0 on a smaller flowbox. Then S=-E/2=0 there, contradicting the strict sign of S off Gamma. Thus P cannot vanish on any neighborhood of x0. No pressure mean assumption enters this exclusion, and no global period for H^(-eta)V is needed: when R=2 the continuous normalized form itself extends closed across the orbit.

## 3. Strict spherical means and the sequence consequences

Differentiation of the spherical average and the divergence theorem give

    M'(r)=-(4*pi*r^2)^(-1) integral_(B_r(x0)) T dx,
    lim_(r->0) M(r)=P(x0)=0.

If T>=0, M is nonincreasing and M<=0. If M(r1)=0, monotonicity and the limit imply M=0 on (0,r1]. The displayed derivative then implies that every smaller ball has zero integral of the continuous nonnegative T. Hence T=0 on B_r1. The Poisson equation makes P harmonic there. Harmonic functions are analytic, and every derivative of P at x0 is zero, so P=0 on that connected ball. Section2 gives a contradiction. Therefore M<0. Reversing every sign gives M>0 when T<=0.

A continuous function with a strictly negative or positive mean on a compact sphere takes that strict sign somewhere on it. Such a point is off Gamma because P=0 on Gamma; the identity P=H(R/2-1) proves the ratio conclusions.

If M(r_j)>=0 and some neighborhood contained no negative T, a smaller ball in it would have T>=0. The strict mean conclusion would fail at all sufficiently small r_j. This proves the first sequence conclusion; the other is identical with reversed signs. Pointwise signs of P imply the corresponding signs of all sufficiently small means.

Continuity of M gives the three alternatives exactly: if its zeros do not approach zero, M is nonzero and has one fixed strict sign on a connected initial interval. Otherwise a sequence of zeros approaches. In the third case both sequence tests apply to the same sequence. If T were zero on a neighborhood, either strict-sign theorem would contradict the other. If T<=0 on a ball, the positive-mean alternative is forced. Nothing decides whether that alternative occurs in a general rotating germ.

## 4. The zero-rotation corollary and its period condition

For omega=0 put p=(1-c)/c, so 1<p<3/2, and rho0=|x0|. Homogeneity and X.V=0 give, on a small cone segment about n0,

    V(rn)=r^(-p)w(n), H(rn)=r^(-2p)h(n),
    P(rn)=r^(-2p)u(n), u=|w|^2/2-h,
    div_gamma w=0.

Here w,h are smooth and flat at n0, h>0 off n0, and w is tangent to the unit sphere. Since 2p eta=p-1, the one-form H^(-eta)V.dx is exactly the pullback of h^(-eta)w^flat. Its period is therefore the same punctured-disk period. In an orthonormal tangent/radial frame the matrix r^(p+1)DV has blocks

    [nabla_gamma w, -p w; -w^T, 0].

Thus T(rn)=r^(-2p-2)F(n), where F=tr((nabla_gamma w)^2)+2p|w|^2, and Poisson becomes

    -(Delta_gamma+2p(2p-1))u=F.

These are exactly the hypotheses of confirmed A1911. For clarity, its sign argument is as follows. A smooth stream function psi on the full disk satisfies w=J grad psi. If F<=0, its Hessian B obeys det B>=p|grad psi|^2 and |B|<=eta|grad log h||grad psi|. Gronwall on each compact punctured path makes grad psi either identically zero or nowhere zero. The zero case gives a positive h with an interior zero solving Delta h=-2p(2p-1)h, contrary to the minimum principle. In the nonzero case B is definite with constant sign. A small regular level curve of either psi or -psi surrounds n0, and its orientation along w gives a strictly positive integral of h^(-eta)w^flat. The zero-period hypothesis makes the same integral zero. This contradiction proves F>0 arbitrarily near n0 and hence the desired positive T values. Section3 supplies negative values under the additional mean sequence condition.

For the sufficient condition, closedness makes the period I independent of a small geodesic radius rho. On its full circle,

    |I|<=2*pi*sin(rho) sup(|w|^(1-2eta)R^eta).

Flatness gives sup|w|<=C_k rho^k for every k. Along the stated sequence the right side is at most C'_k rho_j^[1+k(1-2eta)-N eta]. Choose k so that this exponent is positive. The period is zero. A bound only along one radial path would not suffice.

## 5. Support and propagation along the orbit

If W vanished on a ball about x0, X cross W=aV would give V=0 there. Then P=S and Delta S=0, while S<=0 and S(x0)=0. The maximum principle makes S=0 on that ball, again contradicting its strict sign off Gamma. Thus x0 lies in the relative support of W, and V is nontrivial on every neighborhood. In particular x0 belongs to the finite-jet zero set {V=DV=0,S=0} intersect supp W.

The explicit smooth linear flow identities for V and S carry all their zero derivatives at x0 to each point of the central orbit segment. The same argument and all conclusions may therefore be centered at any such point, on a suitably smaller ball. This uses only finite local flow segments; completeness of a characteristic flow is not needed.

## 6. Verification and open scope

All four source sections and this six-section proof are fully read before the final verdict, together with all ten sections of the exact functional-ratio dependency and all six sections of the angular sign dependency. The Guo-Kar input is a previously verified primary-source theorem, not a new numerical observation. No computation is needed or run.

The mean inequalities and trichotomy hold for every stated c and omega without a period premise. The extra positive-sign conclusion without a mean premise retains omega=0, the target c interval, and the zero period or its stated sufficient condition. Neither result excludes a common flat point. In particular, a rotating germ with T<=0 near x0 remains unexcluded and would have positive pressure means. Bare-decay global nonexistence, global realization of these local hypotheses, and the general common-flat problem remain open.
