# One-signed tail pressure deficits and component end flux

Status: exact results CONFIRMED as A723-A727 and A729, with the three unsupported strengthenings OPEN as A728. The complete submitted source, dependency proof and independent reconstruction have been read.

## 1. Exact setting

Let D=R3 minus{0}, 2/5<c<1/2, omega be finite and real, J(x1,x2,x3)=(-x2,x1,0), A=cI-omega J, p=(1-c)/c, lambda=p-1, mu=2-p, a=c lambda, t=omega/c and q=2p/lambda. Let V in C^(1,alpha)_loc(D) for every0<alpha<1 and P2 in C1(D) satisfy

    div V=0, W=curl V, V.W=0,
    V(exp(sA)x)=exp(-(1-c)s)exp(-omega sJ)V(x),
    P2(exp(sA)x)=exp(-2(1-c)s)P2(x),
    -Delta P2=partial_i partial_j(V_i V_j),
    W.grad S=0, S=P2-|V|^2/2,
    grad k cross grad S=0 on{W!=0}, k=(Ax).V,
    {k=0} subset{W=0}.

The last nodal premise is additional and explicit. These are abstract tail hypotheses; the actual finite-time core-return theorem is not used here.

Use the twisted polar coordinates rho=log r, z=cos theta and chi=phi+t rho. The coordinate-invariant decomposition is

    V.dx=r^(-lambda)(K d rho+gamma),
    R=K+tF, F=gamma(Z), Z=partial_chi,
    M=the inverse sphere metric+t^2 Z tensor Z,
    Bq=M gamma+tKZ, div Bq=-mu R.

On S2, k=cK. Let K=-m<=0, N={m=0}, and suppose V is not identically zero. On a component O of{m>0} define

    beta=gamma/K, b=beta(Z), A_beta=M beta+tZ.

All coordinate expressions are interpreted as smooth tensor expressions on the sphere, including the axis. The confirmed identities A677-A681 give

    V=DV=0 on the zero cone,
    P2=S=0 on the rays over boundary(N),
    d beta=0 on O,
    div(m A_beta)=-mu m(1+tb),
    m A_beta=-M gamma+t mZ.                         (1)

The complete independent proof of those conclusions was reread, including the Holder stable-manifold step, the Hopf barrier, and the exact critical-zero flux. In particular the first two equations are not assumed merely from a pointwise zero of helicity.

## 2. Independent local pressure lemma by a virial identity

Let v be C^(1,alpha), divergence free on a ball B_R about0, let P be C1 there, and assume in distributions

    partial_i partial_j(v_i v_j+P delta_ij)=0,
    v(0)=Dv(0)=0, P(0)=0,
    P>=kappa |v|^2/2, kappa>1/(1+alpha).

Then v=P=0 on the ball. No boundary condition is assumed at radiusR.

Put F(r)=integral_(B_r)P and E(r)=integral_(B_r)|v|^2/2. For n on S2 define

    A0(r)=integral_S2(P+(v.n)^2)(rn)dA,
    B0(r)=integral_S2(3P+|v|^2)(rn)dA.

A smooth radial test supported inside the ball has Hessian phi'' n tensor n+(phi'/r)(I-n tensor n). The double-divergence equation gives

    integral[r^2 A0 phi''+r(B0-A0)phi']dr=0.

After one integration the bracket -(r^2 A0)'+r(B0-A0) is constant. Its limit at0 is0 by C1 regularity. Hence(r^2 A0)'=r(B0-A0), equivalently(r^3 A0)'=r^2 B0. Integrating from0 yields

    r F'(r)+r integral_(boundary B_r)(v.n)^2=3F(r)+2E(r).        (2)

Since P>=kappa|v|^2/2, F>=kappa E>=0. Equation(2) implies rF'<=gamma F with gamma=3+2/kappa.

The weak Poisson equation is Delta P=-tr((Dv)^2). Because Dv=O(r^alpha), its right side is O(r^(2alpha)). The radial mean equation(r^2 average(P)')'=r^2 average(Delta P), with the regular integration constant0 and average(P)(0)=0, gives average(P)=O(r^(2+2alpha)). Thus F=O(r^(5+2alpha)). This mean equation follows directly by radial testing and only uses the displayed distributional Poisson equation and C1 regularity; it does not require an unproved pointwise second derivative of P.

By the strict condition on kappa, gamma<5+2alpha. The function F/r^gamma is nonincreasing, nonnegative and tends to0 as r decreases to0. It is therefore identically zero. Continuity and P>=kappa|v|^2/2 force P=v=0 throughout the ball.

The threshold is strict. At alpha=1, the exact stationary Euler pair v=varrho Jx, P=varrho^4/4, with varrho=(x1^2+x2^2)^(1/2), is C^(1,1), has v=Dv=0 on the axis, and P=|v|^2/4. Indeed (v.grad)v=-varrho^2(x1,x2,0)=-grad P and div v=0. This nonzero pair satisfies equality kappa=1/2. It is a local pressure-lemma test, not a negative-degree tail.

## 3. Pressure deficits and the correct strict accumulation statement

Let x0 lie over boundary(N). By(1), V=DV=P2=0 at x0. Every neighborhood contains a point of{m>0}, where V!=0. If, for a fixed epsilon<1/4, one whole neighborhood satisfied

    S>=-epsilon|V|^2,

then P2>=(1-2epsilon)|V|^2/2. Choose alpha<1 sufficiently close to1 that1-2epsilon>1/(1+alpha). Section2 would force V=0 in a smaller ball, a contradiction. Therefore every neighborhood contains a point with

    S<-epsilon|V|^2                                 (3)

for every fixed epsilon<1/4. For a quantitative deficit take0<epsilon<1/4. The endpoint epsilon=1/4 is not proved by this argument.

Normalize approaching points to the sphere using twisted homogeneity; inequality(3) is preserved since both sides have degree-2p. At a vortical point m>0, the rank contraction h dK=(1/q)K dh gives h=C_j m^q on its connected vortical component. The constant C_j may have either sign or be zero. Since m<=C_A|V| on the sphere, at a vortical deficit point

    C_j< -epsilon |V|^2/m^q
        <=-epsilon C_A^(-q)|V|^(2-q).

As such points approach x0, V tends to0 and q>2, so their constants tend to negative infinity. A fixed finite collection of component constants cannot supply this sequence.

If approaching deficit neighborhoods do not meet the vortical set, there are open irrotational deficit neighborhoods. If rank holds on one of their connected m>0 components, the same contraction gives h=C_j m^q there and the same conclusion applies to any deficit sequence in such components. Otherwise the argument retains rank-failing irrotational regions or zero-velocity negative-pressure regions. The exact alternative uses(3) with any fixed epsilon<1/4. A claim of S<-|V|^2/4 in those regions is not supplied by this proof. No classification of all irrotational component boundaries is needed for the stated alternative.

A useful full-neighborhood exclusion is nevertheless exact: no boundary point of N has a neighborhood with S>=-C|k|^q for any finite C>=0. Near x0, |k|<=C_x|V| and V tends to0. Since q>2, that bound implies S>=-epsilon|V|^2 on a smaller neighborhood for any chosen epsilon>0, contradicting(3). This premise is a bound on a full neighborhood, not only on its vortical part.

## 4. All positive integrating-factor parameters in the exact window

Suppose beta=d phi on O. For s>0 define J_s=m exp(-s phi) A_beta. Product differentiation in(1) gives

    div J_s=-m exp(-s phi) Q_s,
    Q_s=mu+(mu+s)t b+s M(beta,beta).                 (4)

Since |Z|<=1 on the unit sphere, |beta|^2>=b^2 and M(beta,beta)>= (1+t^2)b^2. Completing the square yields

    Q_s>=[4 mu s-t^2(mu-s)^2]/[4s(1+t^2)].           (5)

For t!=0 the lower bound is strictly positive exactly when

    mu (sqrt(1+t^2)-1)/(sqrt(1+t^2)+1)
       <s<mu (sqrt(1+t^2)+1)/(sqrt(1+t^2)-1).

For t=0 it is positive for every s>0. In particular s=mu always belongs to the window, and

    Q_mu=mu[(1+tb)^2+|beta|^2]>=mu/(1+t^2)>0.

These inequalities hold for every finite t. They introduce no smallness assumption on rotation.

## 5. Boundary cutoffs and the exact potential-growth conclusion

Assume boundary(O) is nonempty and write d for spherical distance to that boundary. Suppose for one s in the strict window

    exp(-s phi)<=C d^(-sigma), sigma<1.              (6)

Near the boundary, (1) and a fixed global C^(1,alpha) bound give m+|gamma|<=C_alpha d^(1+alpha). Choose0<alpha<1 with alpha>=sigma. The smooth bounded tensor coefficients and(6) give |J_s|<=C d. A finite constant covers the compact interior of O as well.

Let chi_epsilon be a Lipschitz cutoff equal0 for d<=epsilon and1 for d>=2epsilon, with derivative bounded by C/epsilon. It has compact support in O. Testing(4), by ordinary approximation of this Lipschitz test on its compact support, gives

    integral chi_epsilon m exp(-s phi)Q_s
       =integral J_s.grad chi_epsilon.

The absolute value of the right side is at most C area{epsilon<d<2epsilon}, which tends to0. These collars lie inside O and decrease into the empty set in the enclosing sets{0<d<2epsilon}; the boundary need not have zero area or be smooth. Fatou's lemma and the positive lower bound(5) make the left side positive on any fixed compact ball in nonempty O. This is a contradiction. If O=S2, direct integration of(4) gives the contradiction without a distance function.

Therefore a nonempty exact component satisfies, for each s in the window and each sigma<1,

    sup_O exp(-s phi)d^sigma=infinity.              (7)

Its potential is unbounded below near its boundary. Equivalently there is no uniform lower bound phi>=(sigma/s)log d-C for sigma<1. Since phi is bounded on compact subsets of O, (7) also implies

    limsup_(d->0) (-s phi)/log(1/d)>=1.              (8)

This is a component-level statement about some approaching sequence. It does not locate a flux at every individual boundary point and does not assert a strict inequality in(8). The scalar test phi=(1/s)log d has exactly critical growth and fails every bound(6); it refutes the inference of strictly faster-than-critical growth merely from failure of all the subcritical bounds. This test is not an Euler-tail construction.

## 6. Connected zero sets, exact periods and the component mean

If N is a nonempty connected closed subset of S2, every component O of S2 minus N is simply connected. Here is a direct proof sufficient for the closed one-form beta. Choose a point in N as the stereographic pole. A closed curve in O has compact image and can be deformed in O to a polygonal curve in general position. Split its finite intersections to express its integral as a sum over simple polygonal loops. For each such loop, connected N is disjoint from it and contains the point at infinity, so the bounded Jordan disk contains no point of N. That disk and the loop lie in one component of the complement, namely O. Stokes' theorem gives zero integral of beta on the loop. Thus all its periods vanish and path integration defines phi with beta=d phi. The same filling argument gives simple connectivity. If N is empty, the whole sphere has the same zero-period property.

On any loop contained in{m>0} and in an open irrotational region, the curl identity gives dK+lambda gamma=0, hence

    beta=-(1/lambda)d log m.

Its period is zero regardless of topology outside that region. A loop crossing m=0 is not in the domain of beta and is not covered.

For every component O of{m>0}, even if beta is not exact, the last identity of(1) and the same boundary Taylor bound give |m A_beta|<=C d^(1+alpha). Test its divergence with chi_epsilon as in Section5. The cutoff flux tends to0. The scalar m(1+tb)=m-tF is bounded and integrable, so dominated convergence yields

    integral_O m(1+tb)dA=0.                         (9)

If t!=0, the m-weighted mean of b is -1/t. The numerator is integrable because mb=-F extends continuously; b itself need not be bounded at the boundary. If t=0, (9) excludes every nonempty component and hence every nonzero one-signed tail. Equation(9) does not determine any period.

## 7. Sign-changing K and the retained weighted nodal defect

For this section allow K to change sign, retaining all the other hypotheses of Section1. The exact A679 measure on regular nodal points is

    dnu=M(dK,dK)/(lambda|dK|) dH1,

with finite mass and no extra critical-zero part. For any C1 real weight psi,

    integral_(K>0)(mu psi R-dpsi(Bq))=-integral psi dnu.          (10)

Take psi=|h|^r0, r0>1. At regular zeros in the vortical closure the rank contraction implies h=0. The same conclusion holds wherever rank holds at a regular zero. Thus the weighted defect is concentrated on regular zeros in open irrotational regions where rank fails. It need not vanish by any identity confirmed so far. The zero right side printed in CO42 Section2(d) requires an extra zero-weighted-defect premise; (10) is the unconditional formula. The derivative term is r0|h|^(r0-1)sgn(h)dh(Bq), with no known sign. Even when the defect vanishes, this is a moment balance, not a positive integral contradiction, and weights vanishing at h=0 do not detect mass there.

The unweighted formula is

    integral|K|+(2/mu)nu(S2)=-t integral sgn(K)F.      (11)

Under the additional pointwise or integrated domination -t sgn(K)F<=theta|K| with theta<1, (11) forces K=0 and then V=0 by the nodal premise. No such domination is derived here. At t=0, (11) gives that conclusion directly for all tails in this nodal class, including the sign-changing case. A strictly positive regular-zero measure strengthens this contradiction. None of these formulas removes the nodal premise for an arbitrary abstract tail.

## 8. Other algebra in the source and final scope

The pressure uniqueness multiplier recalled in CO42 is also exact. For a twisted homogeneous harmonic scalar of degree-2p, its spherical harmonic coefficient of indices(l,n) has multiplier

    2p(2p-1)-l(l+1)-t^2 n^2+i t(1-4p)n.

If tn!=0 its imaginary part is nonzero. If tn=0, 2p(2p-1) lies strictly between2 and6, while the spherical eigenvalues l(l+1) are0,2,6,12,... . The multiplier never vanishes. A harmonic difference is smooth on D and admits the usual sphere expansion, so it is zero. No finite angular truncation is used. The recalled exponent equality(3-2c)/(1-2c)=(3p+1)/lambda follows by substituting c=1/(p+1); it yields no additional interface constraint here.

The exact results are the strict local deficit, the full-neighborhood scalar bound exclusion, the parameter window, the cutoff criterion, the component topology and mean, and formulas(10)-(11). The endpoint deficit, omission of the remaining sign-changing defect, and strictly faster growth at every end are not supplied by the source proof. No actual nonzero profile or abstract-tail example satisfying all these requirements is constructed or excluded in the general rotating case.

The full submitted source is pinned in verification. It identifies the coordinator's configured model check of an answer of the external referee (a second model); its nested model request failed and is not counted. The three qualifications were sent back through working files for a focused response. No new model client, numerical computation, symbolic computation or formal build is used. The local endpoint test is checked exactly above; the source's numerical virial check is not needed as evidence.
