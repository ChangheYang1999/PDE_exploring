# Planar harmonic germs and third derivatives of the rank field


Audit completed 2026-11-03T18:12:23.335190+00:00; verdicts A1995-A1999 in the auditor's ledger (AUDIT_LEDGER.md). Exact positive statements are CONFIRMED; the excluded extensions remain OPEN.
Independent audit of LIT280. This proof allows a nonzero harmonic pressure remainder. Its global conclusion retains an upper scalar comparison and global C4 tail regularity.

## 1. Exact local theorem

Fix 0<c<1/2 and any finite real omega. Put a=1-2c, d=1-c, b=2d, q=b/a>2, Jx=e3 cross x, A=cI-omega J, X=Ax and L=dI+omega J. Let x*!=0 and let real functions f in C5 and Q in C4 on a neighborhood of x* satisfy

    Delta f=Delta Q=0, X.grad f=-af, X.grad Q=-bQ.

Suppose f(x*)!=0 and g(x*)!=0, where g=grad f. Suppose f is independent of one fixed Euclidean direction on that neighborhood. Write H=D2f, e=|g|^2, E=e/a^2, S=Q-E and F=g cross grad S. Then it is impossible that F=DF=D2F=D3F=0 at x*. No sign or vanishing condition on Q is imposed.

The proof below is a finite-jet proof. It also applies to one-sided limiting jets obeying the displayed identities to the required orders. This distinction matters in Section 5, where no analytic continuation across an interface is available.

## 2. Rank jets and homogeneous scalar dependence

Since g(x*)!=0, the inverse function theorem gives local coordinates (s,u,v) with s=f. The Euclidean Hodge star identifies F with df wedge dS, with smooth invertible coefficient transformations. A tensor and all its derivatives through order3 vanish at a point if and only if the same holds after a smooth change of coordinates. In the chosen coordinates df wedge dS has coefficients partial_u S and partial_v S. All derivatives of S through order4 involving u or v therefore vanish at x*.

Choose a polynomial h(s) whose derivatives through order4 equal the pure s derivatives of S at the point. The scalar S-h(f) has zero fourth jet. The homogeneities of f and g give X.grad E=-bE and hence X.grad S=-bS. Applying X.grad+b to S-h(f) consumes one derivative, so

    -a s h'(s)+b h(s)

has zero third jet at s*=f(x*)!=0. Repeated differentiation gives the four recurrences

    a s* h^(j+1)(s*)=(b-a j)h^(j)(s*), 0<=j<=3.

For D0=h(s*)/|s*|^q these are exactly the derivatives through order4 of D0|s|^q. It follows that S-D0|f|^q has zero fourth jet. This conclusion asserts finite scalar dependence at one point, not scalar dependence on an open set.

## 3. The pressure equation gives a negative logarithmic Laplacian

The harmonic identities give

    Delta S=-(2/a^2)|H|^2,
    Delta |f|^q=q(q-1)|f|^(q-2)e

near x*, where f and e are nonzero. Taking the Laplacian of the fourth-jet equality from Section 2 and dividing by the nonzero e yields equality through order2 between

    (2/a^2)|H|^2/e
    and -D0 q(q-1)|f|^(q-2).

Differentiate X.grad f=-af to obtain HX=-Lg. The matrix L is invertible, since its symmetric part is dI with d>0. Thus H(x*)!=0. The left side above is positive and D0<0. Both comparison functions are positive on a smaller neighborhood and have equal second jets, so their logarithms have equal second jets as well. Constants drop out of the Laplacian, giving

    Delta log(|H|^2/e)(x*)
      =(q-2)Delta log|f|(x*)
      =-(q-2)e(x*)/f(x*)^2<0.

The logarithmic expression uses at most the fourth jet of f and fourth jet of Q. The fifth derivative of f is needed to give the initially imposed third derivative of F its ordinary classical meaning, since F contains H.

## 4. Planarity gives zero for the same Laplacian

Choose orthonormal coordinates (u,v,w) so that f is independent of w. Harmonicity makes f a planar harmonic function. Locally zeta=f_u-i f_v is holomorphic in u+i v. At the point zeta!=0 because e!=0, and zeta'!=0 because H!=0. On a smaller neighborhood these inequalities persist. The exact Euclidean norm identities are

    e=|zeta|^2, |H|^2=2|zeta'|^2.

Consequently log(|H|^2/e)=log 2+2 log|zeta'/zeta| is harmonic in u,v and independent of w. Its three-dimensional Laplacian is zero, contradicting Section 3. Only a local logarithm of a nonvanishing holomorphic function is used. The direction of planarity need not be the rotation axis. If the two are incompatible, the hypotheses already restrict the possible f; the argument does not assume their compatibility.

## 5. Global theorem and supported contact

Now let 1/3<c<1/2. On D=R3 minus{0} let V,P be C4 and satisfy

    div V=0, DV X=-LV,
    X.grad P=-bP, Delta P=-tr((DV)^2),
    grad k cross grad S=0 on {W!=0},
    k=X.V, W=curl V, S=P-|V|^2/2.

Suppose |V|^2<=r_+|S| on S2 with finite r_+>0. Then there is no nonempty open irrotational germ with V nonzero and V.e0=0 for a fixed unit vector e0.

To prove this, let O be the connected component of int{W=0} containing the germ. The exact Lamb identity grad k=-aV+X cross W gives f=k and grad f=-aV on O. Divergence freedom makes f harmonic. Unique continuation for the harmonic function e0.grad f extends its vanishing from the germ throughout O. Curl homogeneity follows by differentiating the vector homogeneity, and its zero set is invariant under the complete F_t flow. The continuous path in t cannot switch components of its open interior, so O is invariant for every real t. On O the field V is harmonic with symmetric derivative. Thus Q=P+|V|^2/2 is harmonic: Delta(|V|^2/2)=|DV|^2 and tr((DV)^2)=|DV|^2 there. Its scalar degree is -b, while f has degree -a.

There is a relative boundary point x* of O with V(x*)!=0. Here is the full maximum-principle check. If V vanished on the entire relative boundary, k would vanish there. Set m=a/c in (0,1), sigma=omega/c, pi(x)=exp(sigma log|x| J)x/|x|. Invariance identifies O with (0,infinity) times an angular open set B under this quotient, and f=r^(-m)Psi(pi(x)). The angular equation for harmonic f is

    [Delta_S2+sigma^2 Y^2+sigma(1-2m)Y
                               +m(m-1)]Psi=0,
    Y=(Jn).grad_S2.

It follows directly from Delta=r^(-2)[(r partial_r)^2+r partial_r+Delta_S2], since r partial_r acts by -m+sigma Y. The principal part is elliptic and m(m-1)<0. Continuity on the compact angular closure and zero boundary values force any positive maximum or negative minimum to be attained inside, where the equation is impossible. If B is the entire sphere the same argument applies without a boundary. Therefore f=0 and V=0 on O, contradicting the germ. This proves the asserted nonzero boundary point without requiring any regularity of that boundary.

At this point W=0 by continuity from O, and x* belongs to supp W. Otherwise a ball where W=0 would connect to O and make x* an interior point of the same component. The upper comparison extends from S2 by homogeneity; it gives S(x*)!=0. The rank relation holds at x* by continuity from {W!=0}. Since grad k=-aV!=0 there, write grad S=lambda grad k. Contracting with X gives -bS=-a lambda k. Therefore k(x*)!=0, supplying the local theorem's other nonvanishing hypothesis.

## 6. One-sided fourth and fifth jets, verdict and limits

The actual global rank field F=grad k cross grad S is C3 because V,P are C4. It vanishes on the open set {W!=0}; all its derivatives through order3 therefore vanish on its closure, which contains x*. On O, grad f=-aV gives f one additional derivative: f has continuous derivatives through order5 up to x* from that side, obtained from the global derivatives of V through order4. Q has continuous derivatives through order4 there. Harmonicity, homogeneity and planarity and their needed derivatives hold on O and pass to these limiting jets.

The rank-jet argument in Section 2 can be read purely as invertible transformations of finite Taylor polynomials. A polynomial having the limiting fifth jet of f has nonzero gradient at x*, so it supplies a local coordinate change with exactly those jets even if f has no fifth derivative on the other side. The harmonic identities in Sections 3-4 are algebraic equalities of these jets, inherited as limits from O. In particular the logarithmic planar identity uses only fourth derivatives of f and its denominators stay nonzero. Thus the same contradictory negative and zero Laplacians hold for the one-sided jets. No derivative of W across a nonsmooth interface and no analytic extension across it is assumed.

The local theorem and the global matching exclusion are therefore established in their exact stated classes. The upper comparison is used only to give S!=0 at the nonzero supported contact, which then gives k!=0. C4 global tail regularity is used for the third supported rank jet; it is not supplied by natural C1,alpha tail convergence. The theorem excludes the planar velocity germs used by LIT279, even when Q is nonzero, from this narrower global class. LIT279's sector solutions remain valid. General three-dimensional harmonic germs with nonzero Q, matching at natural regularity, and the unrestricted campaign conjecture remain OPEN.

All six sections of the source were read and pinned in the team records. The proof reconstructs the quotient maximum principle already audited for B62. Other dependencies are elementary finite jets, local holomorphic calculus and harmonic unique continuation. No numerical computation or formal build was used. Continued comparison with existing configured model agents uses files; actual provider model execution remains independently unattested.
