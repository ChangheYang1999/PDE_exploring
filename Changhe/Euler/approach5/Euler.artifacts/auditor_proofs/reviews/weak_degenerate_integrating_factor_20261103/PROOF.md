# The degenerate-tail integrating factor at locally Lipschitz regularity

Status: CONFIRMED A712 after complete source and independent-proof postreads. Date: 2026-11-03T10:24:55.152381+00:00.

## 1. Exact theorem

Let 2/5<c<1/2, omega be any finite real number, p=(1-c)/c, a=1-2c, beta=a/[2(1-c)], Jx=(-x2,x1,0), A=cI-omega J and D=R3 minus{0}. Suppose V is locally Lipschitz on D, W is continuous there and P2 is C1 there, with

    div V=0, curl V=W,
    V(exp(tA)x)=exp(-(1-c)t)exp(-omega tJ)V(x),
    P2(exp(tA)x)=exp(-2(1-c)t)P2(x),
    -Delta P2=partial_i partial_j(V_i V_j),
    Ax cross W=aV.

Weak derivatives are meant wherever needed. Let S=P2-|V|^2/2, which is locally Lipschitz, and assume W.grad S=0 almost everywhere. Then |S|^(-beta)V is locally Lipschitz and curl-free on {S!=0}. On every small ball there it is grad psi for a C1 function with locally Lipschitz gradient, satisfying

    Ax.grad psi=0, div(|S|^beta grad psi)=0.

A global potential on a nonzero-S component is asserted only if that component is simply connected. If V!=0, every centered sphere contains both a zero of S and a point where S<0. No positive value, sign change or extension through arbitrary zeros is asserted. The exact spherical mean is

    integral_S2 S=-[(3p-2)R0+(p+1)T0]/(2p),
    R0=integral_S2 |V.n|^2,
    T0=integral_S2 (|V|^2-|V.n|^2).

This confirms the previously unconfirmed locally Lipschitz portion of LIT135. It is a standalone leading-tail theorem; an actual application retains global degeneracy Ax cross W=aV, and the usual actual-tail hypotheses.

## 2. Weak identities and local potentials

Scalar homogeneity gives Ax.grad S=-2(1-c)S almost everywhere. Dotting the degeneracy identity with Ax and W gives Ax.V=V.W=0 pointwise. Hence the vector triple product, valid at almost every differentiability point of S, gives

    grad S cross V
      =[Ax(W.grad S)-W(Ax.grad S)]/a
      =(S/beta)W.

On compact subsets of {S!=0}, mu=|S|^(-beta) is Lipschitz and bounded. The weak chain and product rules yield

    grad mu=-beta mu grad S/S,
    curl(mu V)=mu W+grad mu cross V=0

as distributions. Mollify this continuous closed field on a ball slightly larger than the desired ball. The smooth closed mollifications have potentials, normalized at a fixed point, whose gradients converge uniformly; straight-line integration gives uniform convergence of the potentials. The limit is C1 with gradient mu V, and that gradient is locally Lipschitz. Gluing on a simply connected component by ordinary path independence is legitimate. On an arbitrary component only local potentials are supplied.

For such a potential, Ax.grad psi=mu Ax.V=0 pointwise. Also |S|^beta grad psi=V, so its divergence vanishes in distributions. Integrating the derivative of psi along a linear spiral segment lying in its domain makes psi constant on that segment. No W-flow argument or W differentiability is needed.

## 3. The zero-free case

If S never vanishes on D, the preceding closed field has one global C1 potential because D is simply connected. The ordinary identity Ax.grad psi=0 implies psi(exp(tA)x)=psi(x) for every t. Each point can be moved to the unit sphere by choosing t=-log|x|/c. Thus continuity and compactness of the sphere give an attained finite global maximum of psi on D.

On every ball compactly contained in D, b=|S|^beta is Lipschitz, positive and bounded above and below. The weak equation div(b grad psi)=0 is uniformly elliptic there. The local strong maximum principle, equivalently the local Harnack inequality applied to max(psi)-psi, makes the maximum set open. It is closed, nonempty and D is connected, so psi is constant and V=0.

The imported elliptic fact is the usual local Harnack principle for bounded measurable uniformly elliptic divergence-form coefficients. It is also the reference-weight1 case of the precise weighted result already read and retained in the A547-A548 audit. The function here is C1 with Lipschitz gradient and thus meets its weak energy hypotheses directly. No elliptic statement across a zero of b or at the deleted origin is used.

If V is nonzero, S therefore has a zero somewhere. Exact homogeneity moves this zero to every centered sphere. This conclusion survives at locally Lipschitz V regularity without any nodal regularity assumption.

## 4. Annular Poisson testing supplies a negative point

For a radial smooth test phi supported in an annulus, set P0=integral_S2 P2 and use the radial Hessian together with homogeneity. Logarithmic rotations disappear after angular integration, giving

    -P0 integral r^(2-2p)(phi''+2phi'/r)dr
      =R0 integral r^(2-2p)phi''dr
        +T0 integral r^(1-2p)phi'dr.

Compact-support integration by parts gives

    2p P0+(2p-2)R0+T0=0.

For example the coefficient is extracted using any nonzero nonnegative test after one further integration by parts, since p>1. Subtracting half of R0+T0 yields the stated mean. A nonzero continuous homogeneous V has R0+T0>0, so that mean is strictly negative. Continuity gives a negative point and homogeneity moves one to every centered sphere. No canonical global normalization beyond the stated P2 homogeneity and Poisson equation is required for this deduction.

## 5. Verification and scope

The full five-section LIT135 source is read. Weak chain and curl products, potential topology, attained maximum, elliptic regularity hypotheses and every radial coefficient were checked directly. No computation or formalization is needed. The proof adds only the locally Lipschitz scope to the previously confirmed C1 result. It does not continue the integrating factor through zeros. Actual natural tails already have stronger confirmed C1 regularity, so this lower-regularity extension is not an additional resolution of the campaign. Existing configured-model comparison is requested through working files, with no new client or agent and no unverified claim of a completed response.
