# Exact local reductions and type of the coupled tail system

## 1. System and the zero-contraction branch

Fix 0<c<1/2, any finite omega, Jx=e3 cross x, X=(cI-omega J)x, L=(1-c)I+omega J, a=1-2c, b=2-2c, q=b/a and eta=1/q. The smooth local system under review on an open O in R3 minus{0} is

    X.grad V=-LV, div V=0, W=curl V, V.W=0,
    -Delta P=tr((DV)²), S=P-|V|²/2,
    X.grad S=-bS, W.grad S=0,
    k grad S=qS grad k on supp W, k=X.V.

Homogeneity gives grad k=X cross W-aV. Suppose k=0 and S<0 on O, and set H=-S. Where W=0 the gradient identity forces V=0. If W!=0 and V=0 at a point, then W is parallel to X; W.grad H=0 contradicts X.grad H=-bH!=0. At the remaining points W is orthogonal to both grad H and V, which are linearly independent since X.V=0 but X.grad H!=0. Thus W=mu grad H cross V, and substitution in aV=X cross W gives mu=eta/H. Hence

    curl(H^(-eta)V)=0, V=H^eta grad phi, X.grad phi=0

locally, with a smooth potential. Conversely smooth H>0, phi satisfying X.grad H=-bH and X.grad phi=0 automatically give homogeneity, k=0, helicity zero, scalar transport and rank with S=-H. The system is then exactly the two remaining equations

    div(H^eta grad phi)=0,
    Delta(-H+H^(2eta)|grad phi|²/2)+tr((DV)²)=0.       (1)

No global single-valued potential is asserted on a multiply connected patch.

## 2. The nonzero-contraction branch and its component restriction

Where k!=0, zero helicity gives

    grad k cross V=(X cross W) cross V=kW.

Thus curl(V/k)=0 and locally V=k grad phi with X.grad phi=1. On a connected component of {W!=0,k!=0}, rank further gives S=D|k|^q with a constant D. It is this component class to which the following two-equation reduction applies.

Conversely, start with k!=0, a constant D and smooth phi,k satisfying X.grad k=-ak and X.grad phi=1. Define

    V=k grad phi, S=D|k|^q, P=S+|V|²/2.

Then X.V=k, X.grad V=-LV, W=grad k cross grad phi, V.W=W.grad S=0, and the scalar homogeneity and rank hold. The remaining equations are exactly

    div(k grad phi)=0,
    Delta(D|k|^q+k²|grad phi|²/2)+tr((DV)²)=0.       (2)

In a flowbox X=partial_t, exp(at)k, exp(bt)H, and respectively phi-t or phi depend only on the two transverse variables. Eliminating t derivatives introduces only lower transverse orders. This yields two equations for two transverse functions within the stated branch classes. It does not impose the component power law on an arbitrary irrotational open patch.

## 3. Principal symbols by exact hand calculation

Give phi column weight2, k or H column weight1, and equations1 and2 row weights0 and1. The pressure equation in (1) or (2) has order3 in phi and order2 in the other variable. Linearization of tr((DV)²) has at most order2 in phi and order1 in k or H, so contributes no principal term at these weights.

Write rho=|xi|² and s=xi.grad phi. For (2) the principal matrix, using the displayed plus-Delta convention, is

    [ -k rho,                  i s                         ]
    [ -i k² s rho, -(qD|k|^(q-2)k+k|grad phi|²)rho          ].

Its determinant is

    rho[(qS+|V|²)rho-(V.xi)²]=rho Q(xi).             (3)

For (1) the matrix is

    [ -H^eta rho,             i eta H^(eta-1)s              ]
    [ -i H^(2eta)s rho,        (1-eta |V|²/H)rho            ].

Its determinant is eta H^(eta-1)rho Q(xi), with S=-H. Thus the positive prefactor in CO61 is H^(eta-1)/q exactly. No random-jet computation is needed to establish either identity. Reversing the sign of the full second equation changes the determinant sign but not its zero set or type.

## 4. Reduced type, including the equality cases

Reduced covectors satisfy xi(X)=0. Let Vperp be the orthogonal projection of V onto this plane. Since |Vperp|²=|V|²-k²/|X|², the two eigenvalues of Q there are

    lambda1=qS+k²/|X|²,
    lambda2=qS+|V|², lambda1<=lambda2.              (4)

If Vperp=0, both values coincide and there is no distinguished eigenvector. Otherwise the first corresponds to Vperp and the second to its perpendicular direction. The system is elliptic precisely when lambda1 lambda2>0. There are two distinct real characteristic lines precisely when

    -|V|²<qS<-k²/|X|².                            (5)

At equality in either endpoint there are also real characteristic covectors: one null line if Q has rank1, and every line if Q=0. Thus a shorthand saying that real characteristics exist if and only if (5) is false. CO61 Section3 correctly specifies two directions; the shorter team-note phrasing needs the same qualification.

For k=0, S<0 and R=|V|²/|S|, this is elliptic for R<q, has two distinct characteristic lines for R>q, and is degenerate at R=q. The gap1<=R<=b is elliptic because b=q/(q-1)<q. For S>0, and also S=0 with k!=0, both eigenvalues are positive. At the fixed-component contacts with |D||k|^(q-2)>=3(1-c)/(2|X|²), one has q|S|>k²/|X|² because 3q(1-c)/2=3(1-c)²/a>1. This makes lambda1 negative but alone does not determine lambda2. The exact local swirl has q|S|=((1+p)/(p-1))|V|²>|V|², so Q is negative definite on the transverse plane.

## 5. Exact countertest to dropping the vortical-component restriction

The following local example works for every target c with omega=0. Put p=(1-c)/c>1, lambda=1-p<0, and use cylindrical coordinates rho,theta,z on a small angular patch with rho>0 and cos(lambda theta)>0. Define the real smooth harmonic function

    h=rho^lambda cos(lambda theta), V=grad h,
    P=-|V|²/2, S=-|V|².

It is harmonic because the radial and angular terms of the two-dimensional Laplacian cancel. It is independent of z. Thus div V=0, W=0, and V has homogeneity degree lambda-1=-p. Moreover -Delta P=|DV|_F²=tr((DV)²), since DV is symmetric and Delta V=0. The scalar homogeneity holds because S has degree -2p. In fact the local nonrotating similarity momentum equation also holds: its linear terms vanish by homogeneity and V.grad V=grad(|V|²)/2 cancels grad P. Every other equation in Section1 is automatic: helicity and scalar transport vanish, and supp W is empty so rank is vacuous.

On the chosen patch,

    |V|²=lambda² rho^(-2p),
    k=c lambda rho^lambda cos(lambda theta)!=0.

Since lambda q=-2p,

    S/|k|^q=-lambda²/(c|lambda|)^q
                         times cos(lambda theta)^(-q). (6)

This is not constant on an open angular patch. Therefore a general k!=0 open set satisfying the tail system need not obey S=D|k|^q. The component restriction in Section2(a) is essential. This refutes only its unqualified extension to arbitrary irrotational patches. It is not a whole-space smooth decaying profile, a common-flat example, or a refutation of the correctly restricted reduction.

## 6. What the type calculation can establish about continuation

Equations(1)-(2) are exact within their branch classes. Additional identities in those classes must follow from the two equations, their homogeneity and boundary data, or stronger global information. The symbol calculation identifies a failure of ellipticity and a degeneracy as coefficients approach a common zero. It does not itself prove failure of unique continuation for this nonlinear coupled system.

The scalar wave example f(t-x), with f smooth, flat at0 and nonzero arbitrarily nearby, proves that some hyperbolic equations fail pointwise strong continuation. It is not a solution of (1) or (2). In particular the final claim that any exclusion must control the set(5) or use information beyond the local system is not established as a mathematical necessity: lower-order terms and the coupled equations themselves may impose further restrictions. A safe conclusion is that the displayed symbol alone supplies no continuation theorem, and a proof must address the complete coupled equations and their degeneracy. This is an unresolved methodological limitation, not a constructed Euler counterexample.

## 7. Audit conclusion

All four submitted sections were read and their algebra reconstructed. The two normal forms, their converses and exact principal determinants are confirmed with the component qualification. The real-characteristic equality cases must remain explicit. The local example(6) rules out any extension of the power law to arbitrary irrotational patches, throughout the target interval. Neither unique continuation for the coupled system nor the unrestricted campaign has been proved or disproved here. The configured model parent argument was compared directly; provider runtime remains unattested. No new computation or formal build was used.
