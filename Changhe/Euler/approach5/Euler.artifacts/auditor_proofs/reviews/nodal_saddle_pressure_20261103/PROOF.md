# Nodal saddle mass, pressure transversality and local countertests

Status: A832-A842 CONFIRMED at the scopes below; the global exclusions in Section10 remain OPEN, A843. This is the independent audit of coordinator CO45. No computation or formal proof build is used.

## 1. Statements, hypotheses and normalization

Fix 2/5<c<1/2 and any real omega. Set Jx=(-x2,x1,0), A=cI-omega J, X(x)=Ax, L=(1-c)I+omega J, p=(1-c)/c in (1,3/2), a=1-2c, lambda=p-1=a/c, q=2p/lambda>6 and eta=1/q. A local tail is a vector field V in C^(1,alpha), 0<alpha<1, and P2 in C1 on a twisted cone away from0, satisfying

    V(exp(sA)x)=exp(-sL)V(x),
    P2(exp(sA)x)=exp(-2(1-c)s)P2(x),
    div V=0, V.curl V=0,
    -Delta P2=partial_i partial_j(V_i V_j),
    W.grad S=0, grad k cross grad S=0 on {W!=0},       (1)

where W=curl V, k=X.V and S=P2-|V|^2/2. The pressure equation is distributional. The optional nodal hypothesis is

    {k=0} subset {W=0}.                              (N)

On S2 put K=k, h=S and G=W. With rho=log r and x=exp(rho A/c)w, the correct angular decomposition is

    V.dx=r^(-lambda)((K/c) d rho+gamma).              (2)

Some earlier quotient notes use K for k/c on S2. CO45 combines that older decomposition with the newer K=k convention. Formula(2) keeps the factor c explicit. This changes none of the sublevel exponents or zero sets below. In particular, at a nodal point with W=0 one has dK=-a gamma, rather than -lambda gamma in this normalization.

The actual-profile class additionally consists of U in C2(R3), P in C1(R3) satisfying

    div U=0,
    (1-c)U+DU(Ax+U)+omega JU+grad P=0,
    U.curl U=0 everywhere,
    |U|<=C(1+|x|)^(-p), |DU|<=C(1+|x|)^(-p-1).       (3)

V and P2 must then be its actual limits, with canonical pressure. The weaker premise U->0 and |DU|=O(sqrt(|x|)) supplies the two natural bounds through the already confirmed A601 in this c interval. No conclusion here removes global zero helicity or a premise supplying the gradient estimate.

Define M(O,tau)=integral_{O intersect {|K|<tau}} |G| dA. Let Sigma be the set of angular points with no neighborhood O for which M(O,tau)=o(tau). Under(3), A730-A733 and A705-A708 give a positive lower bound C_* tau for the full-sphere mass if U!=0. They also give the joint lower bound with |K|<tau and |h|<tau^q. These are actual-flow theorems, not consequences of(1) alone.

## 2. A uniform hyperbolic passage estimate

Assume(N), and let x0 on S2 satisfy V(x0)=0 and DV(x0)!=0. Then there are C1 local coordinates (u,v), constants 0<b0<=B0 and an angular neighborhood O such that

    b0|uv|<=|K(u,v)|<=B0|uv|,
    M(O,tau)=O(tau^(1+alpha/2)).                    (4)

No differentiability of dK at x0 is assumed.

Here is the complete argument. Differentiating homogeneity gives DV X=-LV and

    grad k=X cross W-aV, grad k cross V=kW.          (5)

At the zero, N gives W=0, so M=DV(x0) is symmetric, trace free and annihilates X(x0). Since M!=0, its two other eigenvalues are opposite and nonzero. The tangent plane of S2 is transverse to X(x0), because X(x0).x0=c. Thus the restriction of its quadratic form to that tangent plane is nonsingular and indefinite. If gamma is the angular one-form in(2), D gamma(x0) is symmetric and has negative determinant. Define the angular C^(1,alpha) field C by i_C dA=gamma. It has a hyperbolic saddle at x0 with eigenvalues nu,-nu, nu>0. Helicity applied to(2) gives

    dK wedge gamma=K d gamma, hence C K=K div C.     (6)

In smooth coordinates diagonalizing DC(x0), write C=(nu x,-nu y)+R with R=O(|z|^(1+alpha)) and DR=O(|z|^alpha). The local C1 stable and unstable manifolds are graphs x=f(y), y=g(x). Their derivatives satisfy f'=O(|y|^alpha), g'=O(|x|^alpha). For completeness, variation of constants on a stable orbit bounds its unstable component by C|y|^(1+alpha); the graph invariance equation then gives f'(y)=O(|y|^alpha). Reverse time for g.

Set u=x-f(y), v=y-g(x). This is a C1 local diffeomorphism. Invariance of the two graphs and the mean value theorem in x, respectively y, give

    u'=u(nu+e1), v'=v(-nu+e2),
    |e1|+|e2|<=C(|u|+|v|)^alpha.                   (7)

This argument does not assume that this C1 coordinate change gives a differentiable linearization of the vector field. Choose a fixed small box |u|,|v|<R0 with |e_i|<=nu/2. The magnitudes |u| and |v| increase and decrease respectively along any passage. Integrating their alpha powers yields

    integral_passage (|u|+|v|)^alpha dt<=C R0^alpha, (8)

uniformly in the duration. Therefore |uv| changes by a bounded multiplicative factor during the passage, since its logarithmic derivative is e1+e2. Also div C=O(|z|^alpha), so by(6) the same holds for any nonzero K.

K vanishes on both stable branches: their points approach x0 exponentially, the integral of |div C| is finite, and(6) would otherwise give a nonzero limiting K. Reverse time on the unstable branches. On these four branches away from x0, C!=0 and N imply W=0 and dK=-a gamma!=0. On each fixed incoming transversal v=R0 or v=-R0, therefore, |K(u_in,v)| is comparable to |u_in| near the stable branch. Every off-axis point in a sufficiently small inner box reaches the appropriate incoming transversal backward. Equation(8) gives R0|u_in| comparable to |uv| and(6) gives K comparable to its incoming value. This proves the two-sided bound in(4). It also excludes any additional nodal curve in the inner box.

The continuous vorticity G is C^alpha and vanishes on both axes by N. Hence

    |G(u,v)|<=C min(|u|,|v|)^alpha.

The coordinate Jacobian is bounded. With h0=tau/b0, split each quadrant along u=v and then at v=sqrt(h0). The resulting bound is

    M(O,tau)<=C integral_0^eps integral_0^min(v,h0/v) u^alpha du dv
              <=C_alpha h0^(1+alpha/2).

This proves(4). It uses only homogeneity, divergence, helicity, N and C^(1,alpha) regularity. Pressure and the scalar S do not enter. The conclusion for alpha=1 is not asserted from the available tail regularity.

## 3. What remains under the nodal hypothesis

For an actual profile(3) satisfying N,

    Sigma subset {V=0,DV=0} intersect supp G.        (9)

Indeed, a point outside supp G contributes no mass. At K!=0 there is no sufficiently small sublevel. At K=0,V!=0, equation(5) gives grad k=-aV!=0; its angular gradient cannot vanish, since grad k.X=0 but a nonzero radial vector cannot be perpendicular to X. In regular level coordinates, N and Holder continuity give |G|<=C|K|^alpha and local mass O(tau^(1+alpha)). The remaining nonflat velocity zeros are handled by Section2. This proves(9).

Consequently, N plus the absence of flat velocity zeros in supp G implies U=0: cover S2 by finitely many neighborhoods with mass o(tau), contradict the full-sphere lower bound if U!=0.

There is a further necessary local alternative at every point of Sigma. Either every sufficiently small neighborhood meets an open irrotational region, or, on every neighborhood in which {W!=0} is dense, the constants D in

    S=D|k|^q                                       (10)

are unbounded among its nodal components. To check this formulation, on {W!=0,k!=0} contraction of the rank relation with X gives grad(S/|k|^q)=0. If vorticity is dense throughout a neighborhood, continuity of this gradient extends the identity to its whole intersection with {k!=0}. Thus S/|k|^q is constant on each connected local nodal component. Finitely many such components give bounded constants. Bounded constants imply |S|<=C|V|^q throughout a smaller ball, including its zeros by continuity; N and vorticity density ensure that the nonzero-k set is dense.

At a flat zero x0, V=O(|x-x0|^(1+alpha)). The estimate with q>2 makes P2>=theta|V|^2 near x0 for any fixed theta<1/2 sufficiently close to1/2. The radial stress lemma proves that V vanishes on a neighborhood, which contradicts x0 in supp G. Here are its needed details. Center spheres at x0, set E(r)=integral |V|^2, E_r(r)=integral |V.e|^2, and A(r)=integral(P2+|V.e|^2). The distributional double divergence of V tensor V+P2 I is zero, so radial testing gives rA'=E-3E_r. The integration constant at0 is zero by the stated regularity and vanishing. Since A>=theta E>=0,

    (r^(-1/theta) A)'<=0.

The estimate P2=|V|^2/2+O(|V|^q) gives A=O(r^(2+2alpha)). Choose theta in (1/(2+2alpha),1/2). Then r^(-1/theta)A tends to0 at0; monotonicity and nonnegativity imply A=E=0. This proves the alternative. It does not exclude unbounded constants on infinitely many accumulating nodal components, or uncontrolled irrotational regions.

## 4. Pressure transversality at a vortical regular node

Under the local hypotheses(1), at any zero x0 of V the function S has a second-order Peano expansion whose Hessian trace is

    tr Hess_Peano S(x0)=-2|sym DV(x0)|^2.            (11)

Indeed divergence gives -Delta P2=tr((DV)^2), whose right side is C^alpha. Interior elliptic regularity gives P2 in C^(2,alpha). With M=DV(x0), |V(x0+h0)|^2/2=|M h0|^2/2+o(|h0|^2), so the Peano Hessian of S is D2P2-M^T M. Its trace is -tr M^2-|M|^2=-2|sym M|^2.

If also S(x)=o(|x-x0|^2), this Peano Hessian is zero. Thus M is skew. Homogeneity gives MX(x0)=0, and

    grad k(x0)=A^T V(x0)+M^T X(x0)=0.              (12)

Now suppose k(x0)=0,W(x0)!=0 and grad k(x0)!=0. Shrink to a regular level chart with W!=0. On each of its two connected nonzero-k sides the rank identity gives(10), with two finite constants. Continuity gives S=0 at the intervening nodal surface and S=O(|k|^q). Since q>2 and k is C1, S=o(|x-x0|^2). If V(x0) vanished, (12) would contradict regularity. Therefore V(x0)!=0, and grad k cross V=kW shows that V is a nonzero normal multiple of grad k at the node. This is local and needs no N or actual-profile return theorem.

## 5. Joint sufficient conditions

For actual profiles let F=max(|K|,|h|^eta). Each of the following gives the stated conditional conclusion.

First, suppose

    {K=h=0,G!=0} subset {V=0}.                      (J)

Then the concentration set for integral_{F<tau}|G| is contained in {V=0}. To prove this at a joint zero with V!=0, J first gives G=0. Equation(5) makes K regular there. Shrink so V remains nonzero and K regular. At any nearby zero of K with G!=0, the local rank equation forces h=0; otherwise grad k=eta k grad S/S implies k vanishes on an open neighborhood, inconsistent with regularity. Condition J then contradicts V!=0. Thus G vanishes on the entire local nodal curve, giving the O(tau^(1+alpha)) estimate. Off the joint zero set there is no sufficiently small joint sublevel. This proves the localization.

If V has no angular zero, compactness and the actual joint lower bound give U=0. By Section4, J is equivalent to excluding all vortical regular nodes and requiring V=0 at every vortical critical joint zero. Open regions k=0,S!=0 are allowed by J and invisible to the sufficiently small joint sublevel locally. J by itself does not exclude velocity zeros.

Second, if

    integral_S2 |G|/max(|K|,|h|^eta) dA < infinity,  (13)

then U=0. Define 0/0=0 and positive/0=+infinity. Thus (13) includes G=0 almost everywhere on {F=0}. Dominated convergence gives

    integral_{F<tau}|G|<=tau integral_{0<F<tau}|G|/F=o(tau),

contradicting the lower bound for a nonzero profile. Merely requiring G=0 at area-almost every joint zero is insufficient for this argument: a regular zero curve has zero area and can carry a positive tubular coefficient of order tau. No assertion that it is a full-profile counterexample is intended.

## 6. Local open nodal regions for every rotation

At omega=0, cylindrical coordinates (R,phi,z) away from the axis give the exact local profile

    V=R^(-p)e_phi, W=-(p-1)R^(-p-1)e_z,
    P2=-R^(-2p)/(2p), k=0,
    S=-(p+1)R^(-2p)/(2p).

Its divergence and helicity vanish. The linear profile terms cancel because cp=1-c, while DV V=-R^(-2p-1)e_R and grad P2=R^(-2p-1)e_R. Thus all equations(1) hold. The axis singularity excludes a global smooth profile.

For every fixed omega, there is an analytic local solution of all tail equations(1) with k identically0 and with S=1,V=e1,W=-lambda e2 at one point. This does not assert a solution of the full profile momentum equation. The construction and its noncharacteristic check follow.

On z=x3>0 define u+iv=(x1+i x2) z^(-1+i omega/c). Direct differentiation gives X.u=X.v=0. Seek analytic functions psi(u,v), h(u,v) near (0,0) and set

    S=z^(-2p)h(u,v)>0, f=S^eta,
    V=f grad psi, P2=S+|V|^2/2.                     (14)

The homogeneities hold because f has X-degree -a and grad psi transforms with exp(-sA^T). Their product transforms with exp(-sL). Also k=f X.psi=0, W=grad f cross grad psi, V.W=0 and W.grad S=0 identically. The rank equation is automatic because grad k=0. It remains to solve

    div(f grad psi)=0,
    Delta(S+|V|^2/2)+tr((DV)^2)=0.                 (15)

These reduce to an analytic second-order system in u,v. To verify this rather than assume away third derivatives, write g0=grad psi. Differentiating f Delta psi+grad f.g0=0 gives

    f grad Delta psi=-grad f Delta psi-D2f g0-D2psi grad f.

Substitution into Delta V yields exactly

    V.Delta V=f(|g0|^2 Delta f-D2f(g0,g0)
                 +D2psi(g0,grad f))+(grad f.g0)^2. (16)

Thus the pressure equation contains at most second derivatives of h and psi. Its principal coefficient on the physical Hessian of S is

    I+(eta f^2/S)(|g0|^2 I-g0 tensor g0),            (17)

which is positive definite. The other terms contain only first derivatives of f and first or second derivatives of psi.

Prescribe analytic Cauchy data at v=0:

    h=1, h_v=0, psi=u, psi_v=0.

At x=(0,0,1), grad u=e1, grad v=e2, f=S=1 and g0=e1. The divergence equation has coefficient1 on psi_vv and has no h_vv. Solve it first. After that substitution the pressure equation has coefficient1+eta on h_vv by(17). Both remain nonzero in a small neighborhood of these data. The analytic Cauchy theorem for a solved second-order system therefore supplies h and psi, with h>0 after shrinking. In reconstructing(16), one only differentiated the first equation; any solution of the solved system satisfies both equations(15).

Finally grad S=-2p e3 at the base point, so grad f=-lambda e3. Hence V=e1 and W=-lambda e2!=0. This verifies all claimed point data and proves local consistency for arbitrary omega. It does not provide a globally smooth tail, the canonical global pressure, or an actual-profile realization.

## 7. The flux law on a regular nodal cone

Let an angular connected regular zero curve have arclength l, and consider its twisted cone. Write k=r^(-lambda)K and kappa(l)=|grad_T K|>0. The vector W is tangent to that cone because W.grad k=0. In coordinates (rho,l), with rho=log r, its homogeneity gives

    W=e^(-(p+2)rho)(g(l) partial_rho+u(l) partial_l).

The area density induced from volume and dk is

    e^((p+2)rho) d rho dl/kappa(l).                 (18)

To justify this at a specified zero level, use a full local coordinate chart (k,rho,l). Since div W=0 and W.k=0 throughout the chart, its weak divergence equation becomes the tangential divergence equation on almost every k slice. The coefficients are continuous in k, so testing in rho,l and then taking k->0 gives the identity on the zero slice as well. This is stronger than making an unjustified almost-everywhere flow assertion at k=0. Applying it to(18) gives

    u(l)/kappa(l)=j, a constant on the component.   (19)

If j=0 and W!=0, each curve has fixed angle and e^((p+2)rho) is affine in vortex time. It has one origin end. If j!=0, orient l so j>0. Then

    rho(l)=rho0+integral g/(j kappa) dl,
    dt=e^((p+2)rho)/(j kappa) dl.                  (20)

These formulas define the curves without requiring a C1 vector field W. On a closed angular component, the increment Delta=integral g/(j kappa) over one turn is constant. If Delta=0, the lifted curve is periodic with a positive finite vortex period; actual tails exclude it by A701. If Delta!=0, the repeated turns give one finite-time origin end and one infinite-time spatial-infinity end. Compactness of the angular circle bounds kappa away from0 and makes this time conclusion immediate from the geometric series in(20).

Thus a curve returning to the origin at both ends must project onto a noncompact angular component. Every angular accumulation point at either end is a critical zero of K. Otherwise the implicit level chart continues that component regularly, precluding an angular end there; a zero of W cannot stop it at a regular point because u=j kappa!=0. At a critical accumulation point kappa->0, so the tangential part u of W tends to0. Therefore W is parallel to X there. Since k=0 and grad_T K=0 imply grad k=0, equation(5) gives V=0 at every such accumulation point.

For actual C1 tail flows the same calculation holds with the actual vortex time. It does not show that their curves on this prescribed cone return at both ends. Ambient three-dimensional almost-everywhere return cannot be restricted to this null surface.

## 8. A reduced returning-cone model

The reduced equations(18)-(20) alone allow two finite origin ends. On 0<l<pi, put j=1, kappa=u=sin l and g=cos l. Then

    rho(l)=rho0+log(sin l),
    dt=e^((p+2)rho0) sin(l)^(p+1) dl.

The latter integral is finite at both endpoints and rho tends to minus infinity at both. This is an exact example for the reduced cone flux equations only. No angular K, global V, pressure or all-five-equation realization is claimed by this example.

## 9. Dependencies and verification

The source is coordinator CO45 in the team records, with the complete nested answers actual_vortical_node and tail_saddle_flux read independently. The Cauchy coefficients left unchecked by the coordinator were recomputed in Section6. The fixed-transversal argument was checked through the full uniform passage estimate, not just the hyperbolic eigenvalues. The distinction between K=k and the older K=k/c is recorded in Section1.

Prior audited inputs are A796-A802 for local algebra and rank classification, A696-A697 for radial stress rigidity, A730-A733 for actual concentration and regular-node bounds, A705-A708 for the actual partial flow and critical mass lower bound, and A701 for exclusion of actual periodic W curves. Their hypotheses are explicit here. Source hashes and a clean coordinator snapshot are in verification. The nested failed model credential requests are not successful reviews; the existing configured model coordinator agent supplies the ongoing source comparison, with provider runtime unattested.

## 10. Scope

The saddle bound and pressure transversality are proved locally. The sufficient nonexistence criteria in Sections3 and5 are proved only for(3), or its confirmed alternative derivative premise. The local open-nodal constructions disprove an attempted exclusion by these local equations alone; they are not global counterexamples. Flat zeros with unbounded nodal constants or accumulating irrotational regions remain. Excluding all vortical regular or critical nodes remains open. No surfacewise return follows from ambient almost-everywhere return. Nothing here proves the unrestricted smooth decaying nonexistence conjecture for arbitrary nonzero omega.
