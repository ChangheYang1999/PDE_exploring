# Closure of the vortical zero-contraction region

Independent audit of Theory Agent C C58. The complete source and dependencies are pinned in the team records. The proof below distinguishes the local system from two additional consequences of a global Euler profile.

## 1. Exact hypotheses

Fix 2/5<c<1/2 and omega in R. Put Jx=e3 x x, A=cI-omega J, X(x)=Ax, L=(1-c)I+omega J, a=1-2c>0, b=2(1-c), q=b/a and eta=1/q. Let G be an open subset of R^3 not containing the origin, and V,P smooth on G. Set W=curl V, k=X.V, E=|V|^2 and S=P-E/2. Assume the following local system:

    div V=0, V.W=0, DV X=-LV, -Laplacian P=tr((DV)^2),
    grad k=X x W-aV, X.grad S=-bS, W.grad S=0,
    k grad S=qS grad k on supp W.                         (1)

All supports, closures, interiors and boundaries are relative to G. Define the open set Y={W!=0} intersect int{k=0}. A T-flat point has V=DV=0, and T0={V=DV=0,S=0} intersect supp W. For a vector z and a matrix M, z x M acts columnwise; u tensor v denotes u v^T.

The extra profile consequences, stated separately, are:

(P1) At any point of supp W with V=W=0, S>=0; moreover S=0 if DW!=0.

(P2) At any point with V=W=0 and DW!=0, DV=0 and DW=X tensor ell for a nonzero covector ell with ell(X)=0.

The source obtains these from A1319-A1323 and A1186. Their actual-profile class consists of full C^2 velocity and C^1 pressure profiles, U.curl U=0, and finite natural bounds |U(x)|<=C(1+|x|)^(-p), |DU(x)|<=C(1+|x|)^(-p-1), p=(1-c)/c. The local pair must be the actual tail pair, with the smooth local regularity required in (1). The numerical value and sign of S use that tail's pressure normalization. Statements below can instead assume precisely (P1) and (P2), without claiming that (1) implies them.

On int(supp W) intersect {S!=0}, (1) directly gives

    grad(k|S|^(-1/q))
      =|S|^(-1/q)(grad k-k grad S/(qS))=0.                 (2)

Thus this function is constant on every connected component there, including neighborhoods of its zero points.

## 2. The closure identities and two alternatives

Every derivative of k vanishes on Y, because k vanishes on an open neighborhood of every point of Y. Smoothness extends each of these equalities separately to cl(Y). On Y, grad k=0 gives aV=X x W. The vector triple product, together with (1), gives

    a grad S x V=grad S x (X x W)=bS W.

Differentiating the first identity inside Y and then taking limits proves on cl(Y)

    aV=X x W,
    a grad S x V=bS W,
    a DV e_j=(A e_j) x W+X x (DW e_j).                    (3)

Any y in cl(Y)\Y belongs to supp W. If W(y)!=0 and S(y)!=0, choose a connected ball about y with W,S nowhere zero. By (2), k|S|^(-1/q) is constant there. The ball meets Y, so the constant is zero and the whole ball is in Y, a contradiction. Hence W(y)!=0 implies S(y)=0 and grad S(y) x V(y)=0.

If W(y)=0, equations (3) give V(y)=0, P(y)=S(y), and a DV(y)=X(y) x DW(y). Also DV(y) is symmetric because curl V(y)=0, trace-free because div V=0, and annihilates X(y) because DV(y)X(y)=-LV(y)=0. These alternatives are mutually exclusive and exhaustive. No profile consequence is used in this section.

## 3. Negative components and positive components

Assume first just the sign part of (P1). The set Y intersect {S<0} is open in {S<0}. If a point of its relative closure were outside Y, Section 2 would either force S=0 or give a supported common zero V=W=0 with S<0. The first contradicts membership in {S<0}; the second contradicts (P1). Therefore this set is also closed in {S<0}.

A connected component C of {S<0} is consequently either contained in Y or disjoint from Y. In the first case k=0, W!=0, and V!=0, since the middle identity in (3) would force S=0 at any V zero. In the second case k!=0 on C intersect int(supp W): otherwise (2) gives a ball within this open set where k=0, and that ball must contain a point of {W!=0}, hence a point of C intersect Y. On each connected component C' of C intersect int(supp W), (2) now gives a nonzero constant K and

    S=-|K|^(-q)|k|^q.                                    (4)

On C intersect int{k=0}, W=0 because C is disjoint from Y. There grad k=0 and (1) give V=0 as well. Every relative boundary point of C has S=0: continuity gives S<=0; if S<0 there, a connected ball in {S<0} meeting C would be contained in C and would make that boundary point interior.

Now assume also the equality part of (P1). If y in cl(Y)\Y has S(y)>0, Section 2 gives V=W=0. The equality part of (P1) forces DW=0, and then (3) forces DV=0. Thus these points are supported T-flat points with both W and DW zero. Define their set

    Fplus=(cl(Y) intersect {S>0})\Y.

It is closed relative to {S>0}, because cl(Y) is closed and Y is open. Let O={S>0}\Fplus, an open set. Y intersect O is both open and closed in O by the definition of Fplus. Every connected component C of O is therefore contained in Y or disjoint from Y. In the first case k=0 and V,W are nonzero. In the second case the same argument as above gives k!=0 on C intersect int(supp W), and on each of its connected components

    S=|K|^(-q)|k|^q,

with V=W=0 on C intersect int{k=0}.

Finally, assume (P2) as well. For y in cl(Y)\Y with W(y)=0 and S(y)=0, Section 2 gives V=0. If DW=0, (3) gives DV=0; if DW!=0, (P2) gives DV=0. Thus every point of cl(Y)\Y lies in exactly one of the disjoint sets

    {W!=0,S=0},  T0,  Fplus,

where the assertion is membership in their union, not that all points of these larger sets belong to cl(Y)\Y. This distinction avoids a converse not present in the source.

## 4. Analytic local examples with either pressure sign

For either sigma=1 or sigma=-1 there is a real-analytic solution of (1) on a ball about x*=(1,0,0), with k=0, sigma S>0, and V(x*)=W(x*)=0, S(x*)=P(x*)=sigma. Here is the complete local construction, including the noncharacteristic step.

Define

    pi(x)=exp((omega/c)log|x| J)x/|x|,
    u=pi_2(x), v=pi_3(x),
    phi(x)=f(u,v), H(x)=|x|^(-b/c)h(u,v),
    V=H^eta grad phi, S=sigma H, P=sigma H+|V|^2/2.        (5)

Near x*, (u,v) are real-analytic coordinates on the spherical transversal, and X.grad u=X.grad v=0. For real-analytic f,h with h>0, X.grad phi=0 and X.grad H=-bH. Formula (5) gives

    W=eta H^(eta-1) grad H x grad phi,
    k=0, V.W=W.grad S=0, X.grad S=-bS.

The derivative of X.grad phi=0 gives X.grad grad phi=-A^T grad phi. Hence X.grad V=-(aI+A^T)V=-LV. The identity X x curl V=(DV)^T X-DV X then proves grad k=X x W-aV. The rank identity in (1) is zero on both sides. Only div V=0 and the Poisson equation remain.

Let H2=H^(2eta), F=Laplacian phi+eta grad(log H).grad phi, E1=H^eta F and E2=Laplacian P+tr((DV)^2). An exact product expansion gives

    E2=E2s+H2 grad phi.grad F,
    E2s=sigma Laplacian H+(|grad phi|^2/2)Laplacian H2
        +2 grad H2.(D^2 phi grad phi)+H2|D^2 phi|^2
        -eta H2 grad phi.grad(grad(log H).grad phi)
        +tr((DV)^2).                                    (6)

All derivatives in E2s have order at most two. E1 is affine in second derivatives of f and has no second derivative of h. E2s is affine in second derivatives of h. Under the similarity flow exp(tA), E1 has weight 1 and E2s weight 2. Thus vanishing on the spherical transversal implies vanishing on a full neighborhood of x*.

Prescribe analytic Cauchy data along v=0:

    f(u,0)=u^2/2, f_v(u,0)=0, h(u,0)=1, h_v(u,0)=0.

The coefficient of f_vv in E1 is H^eta|grad v|^2, which is positive. Solve E1=0 for f_vv analytically. Substitution into E2s leaves an equation affine in h_vv; at the base point its coefficient is sigma|grad v(x*)|^2=sigma, since grad phi(x*)=0. All other possible second-h terms in that coefficient have factors of grad phi. The coefficient stays nonzero in a neighborhood of the base data. Therefore both equations solve for f_vv,h_vv as analytic functions of the remaining jets of order at most two, with fewer than two v derivatives. The classical Cauchy-Kovalevskaya theorem gives an analytic local solution. Shrinking the neighborhood keeps h>0. The homogeneity just proved gives E1=E2s=0 throughout the corresponding three-dimensional neighborhood, so F=0 there and (6) gives E2=0. All of (1) hold.

The argument works for every finite real omega; no rotational symmetry or angular truncation is used. The source's negative-sign construction and the positive-sign extension differ only in the nonzero coefficient sigma. They are genuine analytic germs of (1), not formal Taylor series.

## 5. Exact first jets and what they refute

Put g=(omega/c,1,0), X0=(c,-omega,0). At x*, grad u=g, grad v=e3, H=1 and grad H=-(b/c)e1. The Cauchy data give grad phi=0, f_uu=1, f_uv=0. Equation E1=0 there gives f_vv=-|g|^2. Consequently

    DV(x*)=g tensor g-|g|^2 e3 tensor e3,
    DW(x*)=-(a/c)(e3 tensor g+|g|^2 e2 tensor e3).          (7)

The second equality follows by differentiating W in (5): the terms multiplying grad phi vanish, and eta b=a. It does not depend on sigma.

The first matrix has rank two. For M=e3 tensor g+|g|^2 e2 tensor e3, direct multiplication gives

    M^2=|g|^2(e3 tensor e3+e2 tensor g),
    tr M=0, tr M^2=2|g|^2, det M=0.

Its characteristic polynomial is z^3-|g|^2 z. Thus DW has three simple eigenvalues 0 and plus or minus (a/c)|g|, is not nilpotent, and has range span{e2,e3}. This range is not the line R X0, since X0 has first component c!=0. Also X0 x DW=a DV, as required by (3). In particular DW!=0, so x* belongs to supp W and is a point of cl(Y)\Y.

After shrinking the ball, every zero of V has DV of rank two. Indeed grad u,grad v stay linearly independent, so a zero of grad phi forces f_u=f_v=0. At such a point, D^2 phi=N^T Hess(f)N, where N has rows grad u and grad v and rank two. Hess(f) is invertible at the base point, with diagonal entries 1,-|g|^2, and stays invertible nearby. Since N maps onto R^2 and N^T is injective, this product has rank two. Then DV=H^eta D^2 phi has rank two as well.

For sigma=-1 the whole ball has S<0. It meets Y and contains x* outside Y, so the negative-component dichotomy of Section 3 fails without the sign input. For sigma=1 the sign part of (P1) holds, since S>0 everywhere, but x* has DW!=0 and S>0 and DV!=0. Thus the equality part of (P1), the flatness conclusion in the positive-component statement, (P2), and nilpotence of DW cannot follow from (1). There are no T-flat V zeros anywhere in this small ball, so removing T-flat boundary points cannot restore the positive-component dichotomy in this example.

These examples are consistent with, and illuminate the need for, the global hypotheses of A1106-A1107 and A1186. They refute their derivation from the reduced local system, not those theorems about actual tails.

## 6. Dependencies and limits

The complete four-section C58 source was read, together with C56's inverse-rank statement and proof mechanism and C57's complete five-step analytic construction. C49's actual-profile hypotheses and A1186/A1106/A1107 were checked again at the exact points where used. The source's numerical jet script was not executed and supplies no part of this proof.

There is no global extension of either analytic germ here, no exclusion of Fplus or of T0, and no continuation theorem through a common infinitely flat point. For an actual tail, the sign and first-vorticity-jet inputs remain consequences of a full global profile with helicity zero and the natural bounds, not consequences of velocity decay alone. No assertion about arbitrary helicity or the unrestricted conjecture follows.
