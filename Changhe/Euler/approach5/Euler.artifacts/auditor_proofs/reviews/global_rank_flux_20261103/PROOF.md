# Global rank, zero flux and bounded-ratio rigidity

## 1. Exact statements and dependencies

Let D=R3 minus{0}, 0<c<1/2 with c!=1/3, omega any finite real number, Jx=e3 cross x, A=cI-omega J, X=Ax and L=(1-c)I+omega J. Suppose smooth V:D->R3 and S:D->R satisfy

    div V=0, DV X=-LV, X.grad S=-bS, W.grad S=0,
    W=curl V, b=2-2c, k=X.V,
    grad k cross grad S=0 on {S!=0}.                  (1)

Suppose fixed constants0<r_-<=r_+<infinity obey

    r_-|S|<=E<=r_+|S| on S2, E=|V|^2.               (2)

Then V=S=0 throughout D. There is no separate k=0 premise and no pressure premise in this smooth theorem.

For2/5<c<1/2, the same conclusion, and P=0, holds instead with V locally C^(1,alpha), 2/c-4<alpha<1, P continuous, Delta P=-tr((DV)^2) in distributions, and S=P-E/2. Retain all of(1)-(2). Poisson regularity makes P locally C^(2,alpha) and S locally C^(1,alpha). Both versions permit the replacement of full rank on {S!=0} by rank on {W!=0,S!=0} and density of this latter set in {S!=0}.

The removal inputs are the complete independently confirmed proofs global_bounded_ratio_20261103, Sections2-3, and poisson_ratio_removal_20261103, Sections2-3. Their full arguments were reread. The smooth removal uses only smoothness and the upper comparison at that stage; the natural version uses Poisson and both comparisons. The Harnack input is the actual Serrin1964 theorem and full source audit recorded in the first proof, Sections4-5. These named dependencies are retained, including their regularity and coefficient hypotheses.

## 2. Closedness through arbitrary scalar zeros

Set a=1-2c, eta=a/b, rho=1/2-eta, gamma=2rho and m=1/c. The complete explicit linear flow F_t=exp(tA)=exp(ct)Q_t, Q_t=exp(-omega tJ), gives

    V(F_t x)=exp(-(1-c)t)Q_t V(x),
    S(F_t x)=exp(-bt)S(x).

Every orbit meets S2 once, so(2) holds globally. Its two zero sets coincide. Define beta=|S|^(-eta)V off S=0 and beta=0 there. The named removal theorem gives beta continuous and locally W^(1,t) for some t>1, with D beta=0 almost everywhere on S=0. In the natural version every1<=t<1/(1-rho) is available. Neither removal argument assumes k=0.

The product-curl identity and velocity homogeneity give

    grad k=X cross W-aV.

Taking grad S cross this identity, using X.grad S=-bS and W.grad S=0, gives

    grad S cross grad k+a grad S cross V=bS W.

Consequently full rank implies grad S cross V=(b/a)S W on S!=0. Substitution into

    curl beta=|S|^(-eta)W-eta |S|^(-eta)S^(-1)grad S cross V

gives zero there. The weak derivative vanishes almost everywhere on S=0, so beta has zero distributional curl on all D. No interface flux or deleted-set limit is omitted.

A continuous distributionally closed one-form has local C1 primitives by mollification on balls and uniform limits of normalized primitives. D is simply connected, so they patch to a single global C1 function psi with grad psi=beta. This topological step concerns all D, not each scalar component separately.

## 3. The potential may initially have additive drift

Since(1-c)-b eta=c,

    beta(F_t x)=exp(-ct)Q_t beta(x),
    F_t^*(beta.dx)=beta.dx.

It follows that psi(F_t x)-psi(x)=d(t), independent of x because D is connected. Evaluation at a point makes d continuous, and the flow group law gives d(s+t)=d(s)+d(t). Thus d(t)=Ct for a real constant C, and

    psi(F_t x)=psi(x)+Ct, X.grad psi=C.              (3)

No invariance has been presumed. This distinction is essential even for a globally exact form on simply connected punctured three-space.

## 4. Annular zero flux and a compact regular level force C=0

Let Phi(r) be the outward flux of V across |x|=r. The divergence theorem on annuli gives Phi(r)=Phi(1). Rotation covariance and the velocity scaling give

    Phi(exp(ct))=exp((3c-1)t)Phi(1).

Since c!=1/3, Phi(r)=0 for all r>0. This argument uses no extension of V or its divergence across the missing origin.

Suppose C!=0. Equation(3) makes grad psi nonzero everywhere, so S and V never vanish. For x=r theta put

    pi(x)=exp((omega/c)log(r)J)theta, u=psi restricted to S2.

Then pi is constant on each F_t orbit and

    psi(x)=(C/c)log r+u(pi(x)).                     (4)

The function u is bounded. For C>0, psi tends uniformly to minus infinity as r->0 and to plus infinity as r->infinity; for C<0 the signs reverse. The level Sigma={psi=0} is therefore compact and regular. Every orbit through n in S2 meets it once at F_(-u(n)/C)n. This gives a continuous bijective parametrization, with inverse pi; differentiating pi composed with the parametrization shows its differential is injective. Equivalently the regular level theorem and X.grad psi!=0 give a C1 embedded sphere. In the natural version the fields are smoother off S=0, but C1 suffices.

For C>0 use the side psi<0; for C<0 use psi>0. It is bounded, contains a sufficiently small punctured ball, and has Sigma as its only outer boundary. Removing a closed small centered ball gives a bounded domain avoiding0 to which the divergence theorem applies. The inner sphere flux is zero. On Sigma its outward normal is

    n=sign(C)grad psi/|grad psi|,
    V.n=sign(C)|S|^eta |grad psi|.

The latter is continuous, nonzero and has one strict sign on the compact surface. Its integral cannot be zero, contradicting the zero inner flux. Therefore C=0. Equation(3) and V=|S|^eta grad psi now give k=0 off S=0, and V=0 gives k=0 on S=0.

This proves the new step without characteristic-flow completeness for V or W, without regular nodal charts, and without derivatives of a scalar ratio coefficient.

## 5. Global maximum and the full weak equation

Since C=0, psi is invariant under F_t. Its maximum M on S2 is a global maximum on D, attained in D. On S!=0 put R=E/|S| and tau=(m-2)/2=eta/gamma. Algebra gives

    V=q|grad psi|^(m-2)grad psi, q=R^(-tau),
    0<r_+^(-tau)<=q<=r_-^(-tau)<infinity.            (5)

Assign q=r_+^(-tau) on S=0. Both vector sides vanish there. Thus q is bounded measurable with a positive lower bound on all D, and div V=0 gives the full weak equation

    div(q|grad psi|^(m-2)grad psi)=0.

The potential is C1 and locally W^(1,m). Dividing the flux by its positive ellipticity constant gives Serrin's coercive m-growth hypotheses with every lower-order coefficient zero. His1964 Theorems5,6,9 cover respectively m<3,m=3,m>3, as checked against the actual source in the preceding audit. Here m=3 is excluded but causes no extra dependency. The nonnegative solution M-psi obeys Harnack with zero additive term. Its zero set is nonempty, open by Harnack and closed by continuity. D is connected, so psi is constant. Equation(5) gives V=0; the lower comparison gives S=0; in the pressure version P=S+E/2=0.

Density in the alternative hypothesis extends rank by continuity precisely on S!=0 and completes that variant. Density is an additional assumption, not a consequence of bounded ratios.

## 6. The exact exceptional exponent

For c=1/3, every omega and K!=0 take

    V=Kx/|x|^3, P=-K^2/(2|x|^4), S=-K^2/|x|^4.

These fields are smooth on D, div V=curl V=0, and have the required twisted homogeneity. Also k=(K/3)|x|^(-1), so grad k cross grad S=0, and E/|S|=1. The eigenvalues of DV are -2K/r^3,K/r^3,K/r^3, giving tr((DV)^2)=6K^2/r^6. Since Delta(r^-4)=12r^-6, the pressure Poisson equation holds. Irrotationality and P=-E/2 also give stationary Euler momentum on D.

Here eta=1/4, beta=sign(K)sqrt(|K|)x/r^2 and psi=sign(K)sqrt(|K|)log r. Its additive drift is C=sign(K)sqrt(|K|)/3 and its flux is4pi K. Thus the exceptional exponent is essential even with Poisson and ratio1. The example is singular at0 and outside the target interval; it is not a campaign counterexample.

## 7. Verdict and actual-profile scope

LIT268's closedness, additive homogeneity, zero-flux drift exclusion, conditional global rigidity and exceptional countertest are CONFIRMED. All six submitted sections and all seven independent sections were read. The target natural regularity is supplied by A533/A538/A539 under the explicit full-profile natural U/DU bounds. Global zero helicity supplies W.grad S=0 and rank on vortical points, not full rank across arbitrary open irrotational holes. The specified full-rank or density premise and both global comparison bounds remain extra.

The conclusion here is tail vanishing. A faithful-tail argument with its own exact hypotheses is required before concluding original-profile vanishing. Neither the all-omega bare-decay conjecture nor local strong continuation from merely bounded ratios is resolved. No computation or formal build was needed. The source is pinned in the team records; the comparison is through existing configured-model file exchanges, with provider runtime independently unattested.
