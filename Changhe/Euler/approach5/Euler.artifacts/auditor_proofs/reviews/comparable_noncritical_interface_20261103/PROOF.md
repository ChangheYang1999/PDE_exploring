# Noncritical contacts of comparable natural Euler tails

## 1. Exact statement and dependencies

Fix 2/5<c<1/2 and a finite real omega. On R3 write Jx=e3 cross x, A=cI-omega J, X(x)=Ax, L=(1-c)I+omega J, a=1-2c, b=2-2c and p=(1-c)/c. Let U in C2(R3;R3), P in C1(R3) satisfy

    div U=0, LU+DU(X+U)+grad P=0, U.curl U=0,
    |U(x)|<=C(1+|x|)^(-p), |DU(x)|<=C(1+|x|)^(-p-1)

for a finite C. Let V,P2 be the actual natural tails on D=R3 minus {0}, W=curl V, E=|V|^2, S=P2-E/2 and k=X.V. Assume fixed constants 0<r_-<=r_+<infinity with r_-|S|<=E<=r_+|S| on S2.

If U is nonzero, there is a connected component O of int{W=0}, invariant under F_t=exp(tA), meeting the open set {S!=0, grad k cross grad S!=0}. There is a point z of its relative boundary in D with |z|=1 such that

    z in supp W, W(z)=0, V(z)!=0, k(z)!=0, S(z)!=0,
    grad k(z)=-aV(z),
    grad S(z)=-bS(z)V(z)/k(z).

In particular both displayed gradients are nonzero and

    grad(log|S|-(b/a)log|k|)(z)=0.

The logarithms are defined on a neighborhood of z. Consequently either additional requirement k=0 on S2 intersect boundary(int{W=0}), or S=0 on that set, forces U=0.

The actual-tail package supplies V in C1,alpha_loc and P2 in C2,alpha_loc for every alpha<1, divergence and twisted homogeneity, the Poisson equation, W.grad S=0 and the actual rank identity on {W!=0}. These are the hypotheses and conclusions audited in A1873-A1878. Faithful-tail rigidity there gives V=0 implies U=0. The full-rank global comparison theorem A1866-A1871 applies with any 2/c-4<alpha<1, an available interval precisely because c>2/5. The quotient argument below independently reconstructs A1792-A1794.

## 2. A nonempty rank defect and an invariant component

Suppose U is nonzero. Then V is nonzero by faithful-tail rigidity. Homogeneity gives X.grad k=-ak, X.grad S=-bS and the same scalar scaling for E and |S|. Thus the comparison on S2 holds throughout D. If grad k cross grad S vanished throughout {S!=0}, the cited full-rank global comparison theorem would imply V=0. Hence

    Sigma={S!=0, grad k cross grad S!=0}

is nonempty and open. Actual vortical rank forces W=0 there; comparison forces V!=0 there. Choose a connected component O of int{W=0} meeting Sigma. The curl scaling preserves int{W=0}. For x in O the path F_t x, t in R, is a connected subset of this open set and contains x, so it remains in O. The inverse flow gives F_t O=O. This uses the explicit complete linear flow and makes no assumption about completeness of a nonlinear characteristic flow.

## 3. The quotient maximum principle

The differentiated contraction, with the transpose retained, is

    grad k=A^T V+DV^T X=-aV+X cross W.

Thus on O, V=-grad k/a and Delta k=0. In particular k is a globally defined harmonic scalar on O, even if O has nontrivial topology. Distributional harmonic regularity makes it smooth there.

Assume V vanishes at every boundary point of O relative to D. Then k=X.V vanishes there. Put m=a/c, sigma=omega/c, so 0<m<1, and

    q(x)=exp(sigma log|x| J)x/|x|.

The map x to (log|x|,q(x)) is a smooth product parametrization of D. Flow saturation identifies O with the product of the real radial coordinate and an open subset D0=O intersect S2 of S2. It also identifies their boundaries. Twisted homogeneity gives k(x)=|x|^(-m)Psi(q(x)), where Psi is the restriction of the globally continuous k to D0 and hence extends continuously to its compact closure. Under the contrary assumption its boundary values are zero.

Let Y be the smooth rotation vector field on S2. Since r partial_r acts as -m+sigma Y, the harmonic equation is

    [Delta_S2+sigma^2 Y^2+sigma(1-2m)Y+m(m-1)]Psi=0.

The principal quadratic form is |xi|^2+sigma^2(Y.xi)^2 and is positive uniformly on the compact sphere for each fixed finite omega. At an interior positive maximum all first derivatives vanish and the principal second derivative contribution is nonpositive. The zeroth-order term is strictly negative because m(m-1)<0. This contradicts the equation. Any positive value would attain such a maximum because the boundary value is zero and the closure is compact. Apply the same reasoning to -Psi. The argument covers D0=S2 as well. No boundary smoothness is needed. Thus Psi=k=V=0 on O, contradicting its intersection with Sigma.

Consequently some z in boundary O has V(z)!=0. The component and its boundary are flow invariant, and the flow rescales radius by exp(ct), so normalize |z|=1. Continuity from O gives W(z)=0. Every boundary point of O is in supp W: otherwise a connected ball around it lies in int{W=0}, meets O and belongs to the same component, a contradiction. This also proves boundary O is contained in boundary(int{W=0}), a detail needed by the stated corollaries.

## 4. The exact contact equations

Comparison and V(z)!=0 imply S(z)!=0. The Lamb identity gives grad k(z)=-aV(z)!=0. Actual rank extends from {W!=0} to supp W because grad k and grad S are continuous. Therefore grad S(z)=lambda V(z) for a scalar lambda. Contracting with X(z) and using the homogeneity of S gives

    lambda k(z)=-bS(z).

Its right side is nonzero, so both lambda and k(z) are nonzero. Substitution proves the displayed formula for grad S. The gradients of log|S| and log|k| are respectively -bV/k and -aV/k at z, proving their stated cancellation. Continuity of k,S makes both logarithms well defined in a neighborhood.

No derivative of W is used. At natural regularity this proof gives no DW(z), Hessian contact identity or sign of S(z). The point is on the boundary of O and need not be on the boundary of the smaller rank-defect set Sigma.

## 5. Conditional exclusion and scope

The constructed point belongs to S2 intersect boundary(int{W=0}) and has both k and S nonzero. Either proposed global boundary-zero condition therefore contradicts a nonzero U. The zero field satisfies the conditions. These are conditional theorems under the full momentum, global zero-helicity, natural U/DU bounds and two-sided comparison assumptions of Section 1.

The contact itself is not excluded. Neither comparison nor either boundary-zero condition has been derived from bare decay. The proof is valid for every finite omega; it does not require a numerical estimate uniform as |omega| tends to infinity. No sign or higher regularity conclusion is imported from the stronger B59-B61 results.

All five submitted sections and all eight sections of the earlier independent B62 audit were read. The source is pinned with its checksum. This informal argument precedes any formalization; no numerical computation or formal build was performed. Existing configured model agents remain the file collaborators, with actual provider runtime not independently attested.
