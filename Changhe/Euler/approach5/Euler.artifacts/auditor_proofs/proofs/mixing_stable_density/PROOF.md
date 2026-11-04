# Mixing gives strong stable density and conditional Bernoulli rigidity

## Abstract statement

Let phi be the flow of a C2 vector field X on a smooth Riemannian manifold. Let Lambda be compact, invariant, nonsingular, locally maximal and uniformly hyperbolic. If phi restricted to Lambda is topologically mixing, then for every x in Lambda the set Wss(x) intersect Lambda is dense in Lambda. The analogous unstable assertion holds.

Topological mixing means that for any two nonempty relatively open subsets V,Q of Lambda, phi_t(V) meets Q for every sufficiently large real t. The proof does not require Lambda to be an attractor.

## Proof

The local-product theorem supplies the following uniform fact. For any sufficiently small plaque size e and phase bound eta>0 there is delta>0 such that whenever p,q in Lambda are within delta, there are y' in Lambda and |tau|<eta satisfying

    y' in Wuu_local(p) intersect Wss(phi_tau q),
    d(phi_(-t)y',phi_(-t)p)<=C exp(-lambda t)e, t>=0.

The usual phase-on-first-coordinate formulation gives this by applying the opposite phase to the intersection. Adjusting e absorbs the uniformly bounded derivative of short flow times. This is the only local-product input.

Fix x,z in Lambda and epsilon>0. Put M=sup_Lambda|X| and choose eta so that M eta<epsilon/3. Choose the corresponding product data. Set V=Lambda intersect B(z,epsilon/3), and cover Lambda by finitely many balls B(q_j,delta/3). Mixing supplies one common threshold T0 for the intersections of phi_T(V) with every one of these balls. Choose T>=T0 also making C exp(-lambda T)e<epsilon/3. Some q_j lies within delta/3 of phi_T x, and some v in V has phi_T v within delta/3 of that q_j. The two late points are within delta.

Apply local product to p=phi_T v and q=phi_T x. Then w=phi_(-T)y' lies in Lambda and Wss(phi_tau x), and d(w,v)<epsilon/3. Set y=phi_(-tau)w. Then y lies in Wss(x) intersect Lambda, and d(y,w)<=M|tau|<epsilon/3. Thus d(y,z)<epsilon. The finite cover is essential: it makes the mixing threshold uniform while phi_T x moves. Time reversal proves the unstable assertion.

## Conditional Euler theorem

Let 0<c<1/2, omega be any finite real number, U in C2(R3;R3), and P in C1(R3) solve

    div U=0,
    (1-c)U+((cI-omega J)y+U).grad U+omega JU+grad P=0.

Assume U is uniformly sublinear. Put B=(cI-omega J)y+U, Omega=curl U, O={Omega!=0}, a=1-2c, kappa=1+c, and H=P+|U|^2/2+((cI-omega J)y).U. Suppose there is a family of compact nonsingular locally maximal uniformly hyperbolic attractors A_j for Psi, the reversed B flow, such that:

1. A_j lies in O and Psi restricted to A_j is mixing.
2. Their open attraction basins V_j cover almost every point of O.
3. U.Omega=0 at every point of every V_j.

Then U is spatially constant, and decay at infinity forces U=0. None of these three additional premises follows here from decay.

## Completeness and basin geometry

Sublinearity makes B at most linear, so its flow is complete. Outside a large ball, y.B>0; every Psi semiorbit therefore stays in a compact ball. The exact bracket is [B,Omega]=-kappa Omega. For completeness of the Omega flow Gamma, fix x and a compact neighbourhood of its entire Psi semiorbit, with one uniform local Omega existence interval [-s0,s0]. For arbitrary finite s choose T so that |s|exp(-kappa T)<s0 and define

    Gamma_s x=Phi_T Gamma_(s exp(-kappa T)) Phi_(-T)x.

Local bracket conjugacy and uniqueness make this consistent as T increases. It extends every finite Omega time and gives the global identity

    Psi_t Gamma_s=Gamma_(s exp(-kappa t)) Psi_t.

On compact A_j, Omega is nonzero and its transported direction contracts exactly at rate -kappa, up to bounded endpoint norms. It is independent of B. The determinant of D Psi_t is exp(-3ct), so the remaining transverse direction has rate kappa-3c=a>0. Hence the strong stable dimension is one and is spanned by Omega.

Every finite Gamma segment through a point x in A_j contracts to the orbit of x by the conjugacy, hence lies on Wss(x). Locally it is a nondegenerate curve on that one-dimensional stable manifold, so it contains a neighbourhood of x in the manifold. Uniformity over compact A_j and the late-image characterization of global stable manifolds show that the entire Wss(x) is the complete Gamma orbit. The in-phase theorem for a locally maximal hyperbolic set gives V_j as the union of these Wss(x), x in A_j. Precompactness of Psi orbits verifies its limit-set condition. Any phase is absorbed in the invariant set A_j.

## Bernoulli constancy

The Lamb identity is aU+grad H=B cross Omega, hence Omega.grad H=-a U.Omega. Hypothesis3 makes H constant on each complete vortex line in V_j. The abstract mixing lemma makes the trace of each such strong stable leaf dense in A_j. Therefore H is constant on A_j, then on all of V_j. Since these open basins cover almost every point of O, continuity gives grad H=0 on O: a nonzero gradient at one point would persist on a positive-volume ball disjoint from the covering sets.

For clarity, the analytic closure is included. Let D=int{Omega=0}. If O is nonempty, its boundary lies in {Omega=0}, and continuity and the Lamb identity give U=0 there, in particular on the boundary of D. Extend U|D by zero outside D. On each compact ball this extension is Lipschitz: for a segment crossing the boundary, compare to the first exit point and use the local bound on DU. Its weak derivative is 1_D DU. On the zero set this follows from the fact that a Lipschitz function has derivative zero almost everywhere on its zero set. Thus the extension has distributional divergence and curl zero, is entire harmonic, and vanishes on the nonempty open set O. It is zero everywhere. Consequently U=0 on {Omega=0}, and the Lamb identity gives grad H=0 globally.

For global constant H, dotting with B gives U.B=0. Subtracting a pressure constant gives P=q=|U|^2/2. The exact identities are

    partial_i partial_j(U_i U_j)+Delta q=0,
    div(qB+qU)=(5c-2)q.

Writing E(R)=integral_(B_R)|U|^2 and M_R=sup_(|y|=R)|U|, the second identity gives

    (cR-2M_R)E'(R)<=(5c-2)E(R).

For c<2/5 its large-radius sign forces E=0; for c=2/5 it makes E bounded. For 2/5<c<1/2 choose epsilon<min(c/2,1-2c). Sublinearity gives M_R<=epsilon R for large R, hence E(R)<=C R^p with p=(5c-2)/(c-2epsilon)<1. In the last two cases annular energy is o(R).

Test the pressure identity with chi_R sqrt(1+|y|^2), where chi_R is a smooth radial cutoff equal to one on B_R and zero outside B_(2R). The errors are at most C/R times the annular energy, hence vanish. The remaining integrand is

    U^T D2 sqrt(1+|y|^2) U+q Delta sqrt(1+|y|^2),

nonnegative and strictly positive wherever U!=0. Its integral on each fixed ball is zero, so U=0. If O was empty from the start, U is entire harmonic and sublinearity makes DU=0 by the interior gradient estimate on arbitrarily large balls. Thus U is constant in every case.

## Source verification and scope

The actual manuscript Fisher, Petty and Tikhomirov, arXiv:1510.05933v1, printed page5, Definition2.2 and Lemma2.3, was read for the local-product statement. The actual Bakker, Fisher and Hasselblatt manuscript, arXiv:1903.10948v1, Theorem2.6, printed page5, was read for the in-phase statement. Their files are retained by the literature agent. The manuscript filename using “petrosyan” in that agent is only a filename; the author on the actual manuscript is Petty.

This confirms LIT58 and the mixing implication needed for CO21. It does not replace mixing by transitivity, exclude constant-roof attractors, or supply basin coverage at C2 regularity.
