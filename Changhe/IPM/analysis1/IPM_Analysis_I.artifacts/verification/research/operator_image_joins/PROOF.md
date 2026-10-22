# Derivative joins of the linearized IPM image

## Statement and hypotheses

Let rho be a real function in W^{2,infinity}_loc(R^2), let c_l be a nonzero real number, and suppose the canonical IPM velocity U[rho] belongs to W^{1,infinity}_loc(R^2) and has distributional divergence zero. Write V=c_l X+U[rho] and G=X dot grad rho. These are hypotheses on a background, not the assertion that it solves the stationary equation. They hold for a canonical C^{2,alpha} background with the required local velocity regularity. Let h be continuous, compactly supported in an annulus 0<R_-<r<R_+, and C2 up to each side of finitely many circular interfaces. Assume h is C2 away from those interfaces, including the two support circles when the zero exterior is counted as a piece. Its parity may be fixed to even in x and odd in y.

Define the canonical order-zero velocity U[h] on L2 by the Fourier multiplier

    Uhat[h](xi)=(xi_1 xi_2,-xi_1^2) hhat(xi)/|xi|^2,

with the value at xi=0 irrelevant. Since h vanishes near0, its stream function is harmonic there and the canonical scalar Sigma(h)=psi[h]_xy(0) exists. Define the linearized expression

    Lh=V dot grad h-h+U[h] dot grad rho+(Sigma(h)/3)G.

The following statements concern local weak H1 regularity, not the complete global weighted norm.

1. At a circle r=R, Lh belongs to H1 across that circle if and only if

       V_r(R,theta) [partial_r h](R,theta)=0 for every theta.       (1)

   Brackets denote the outer trace minus the inner trace. Values and derivatives on the circle itself have no effect on this condition.
2. Suppose on each radial piece

       h=r^3 sum_{m=0}^M B_m(log r) Phi_m(theta),
       Phi_m=cos(theta)^2 sin(theta) cos(2m theta),

   with each B_m C2 up to the endpoints. Exact continuity of h implies exact continuity of every B_m. Then Lh is H1 locally across every interface if and only if every B_m has matching first t derivatives at every interface. In particular, exact C0 joins alone do not generally suffice, even though they suffice for h itself to be H1. This applies to internal polynomial joins as well as to external support joins.
3. Consider the exact C0 repair of a compact radial polynomial column described in topic132. If any of its first t derivative traces fails to match, then its product with any one Phi_m has an image outside H1 locally for every background satisfying the hypotheses above. This is a conditional theorem on the indicated backgrounds; a finite computation will determine which of the selected repaired columns meet its premise.

No assertion about the retained numerical singular vectors, their exact joins, the actual matrix spectra, global invertibility or a PDE endpoint follows merely from these statements.

## The lower-order terms have a weak H1 derivative

Continuity cancels all boundary measures in the first distributional derivative of h. Its piecewise derivatives are bounded on its compact support, so h is in H1(R^2). The squared norm of the displayed vector multiplier is xi_1^2/|xi|^2, at most1. Applying Plancherel to h and its weak derivatives proves that U[h] belongs to H1(R^2). This construction agrees with the canonical decaying velocity of the compact density: its Fourier divergence is zero and its curl is -partial_x h, with no additional affine strain. The value Sigma(h) is finite because the support is a positive distance from0 and the differentiated Poisson kernel is smooth there. Its value plays no role in the jump calculation.

On every compact set, grad rho and its first weak derivatives are bounded. The weak product rule therefore puts U[h] dot grad rho in H1 locally. The same is true of -h and of the scalar multiple of G, because G belongs to W^{1,infinity}_loc. Hence

    Q=-h+U[h] dot grad rho+(Sigma(h)/3)G

belongs to H1 locally. It creates no circle measure in its first derivative. This argument does not require a pointwise trace of the singular integral to be computed numerically.

## The exact jump criterion

Put S=V dot grad h on each piece. It has a bounded piecewise weak gradient since V is locally W^{1,infinity} and h is piecewise C2. Integration by parts shows

    grad S=(grad S)_pieces+[S] nu delta_{r=R}

near a single interface, where nu is the radial unit normal. Equality of the two C2 value traces of h implies equality of their tangential derivatives. Thus [grad h]=nu[partial_r h]. The locally Lipschitz field V has a single trace, and consequently

    [S]=V_r[partial_r h].                                   (2)

If this continuous coefficient vanishes, the piecewise gradient is the weak gradient and is locally L2. If it does not vanish, choose a smooth nonnegative angular test supported on an arc where it has fixed nonzero sign. Extend the test in the radial direction with a cutoff of width d, value1 at R, and multiply it by nu. Its L2 norm is O(sqrt(d)), while its pairing with the circle term has a nonzero limit and the bounded piecewise contribution is O(d). An L2 weak gradient would have pairing tending to zero, a contradiction. Thus S is H1 across the circle exactly when (2) vanishes. Since Q is H1 locally, Lh=S+Q has this property exactly when S does. This proves1.

The same proof applies to finitely many disjoint circles, including the support ends, by testing each separately. It does not use a distributional square of a delta measure.

## Radial flux and finite angular sums

By the divergence theorem on the disk, using div V=2c_l,

    integral_0^{2pi} V_r(R,theta) dtheta=2pi c_l R.           (3)

The right side is nonzero. Continuity of V_r gives a nonempty open angular interval on which it is nonzero. Therefore (1) forces [partial_r h] to vanish on that interval.

The functions Phi_m are linearly independent. On any arc where cos(theta)^2 sin(theta) is nonzero, their linear relation reduces to a finite cosine polynomial. Multiplying its complex exponential expression by exp(2Mi theta) gives an ordinary polynomial in exp(2i theta). A polynomial vanishing at infinitely many points of an open arc is identically zero. Its coefficients vanish. This also proves that any finite sum of the Phi_m vanishing on an open arc vanishes everywhere, including across their isolated common zeros.

At a fixed circle the value trace difference is

    [h]=R^3 sum_m [B_m] Phi_m.

Its vanishing implies [B_m]=0 for every m. With t=log r, differentiation gives

    partial_r h= r^2 sum_m (3B_m+B_m') Phi_m,
    [partial_r h]=R^2 sum_m [B_m'] Phi_m.                    (4)

Equations(1), (3) and the polynomial argument show that every coefficient [B_m'] vanishes. Conversely, if every coefficient vanishes, (4) and1 give H1 regularity of Lh across the circle. This proves2 and its one-mode specialization3. The argument uses only nonzero c_l and incompressibility; it does not assert that V_r has one sign at every angle.

## What radial difference rows see at a jump

This elementary model explains the limitation of image rows computed from differences. Let f(t)=f_-+a_-t for t<0 and f(t)=f_++a_+t for t>0, with jump J=f_+-f_-. At the two nodes -d/2,d/2 the secant is exactly

    (f(d/2)-f(-d/2))/d = J/d+(a_++a_-)/2.                 (5)

For fixed nonzero J the squared secant is asymptotic to J^2/d^2. Multiplying by a quadrature interval length d gives asymptotic J^2/d, which diverges. A positive smooth weight has the same conclusion. The numerics lane's unweighted sum of such rows is a discrete functional; a small nonzero jump can be numerically invisible on a given mesh and still exclude weak H1 membership. Equation(5) is not an assertion that the existing finite grid crosses every internal interface, or that any particular floating singular vector has a jump.

## Application and verification scope

Topic132 defines exactly continuous repairs by affine changes on every selected saved spline piece. Affine changes need not match the first derivative. Its proof and quantitative norm comparison only claimed C0. A new finite audit will reconstruct all repaired derivative traces from the exact saved binary64 coefficients and rational corrections, using two distinct rational methods. Each nonzero trace then gives statement3, without an additional whole-plane velocity computation. The audit does not manufacture a C1 repair, certify the original discontinuous columns, or transfer any matrix to another function space.

These notes are standalone mathematical proofs. No Lean or LaTeX build is attempted, as the run forbids Lean/Lake and has no TeX target. The conclusions remain separate from the needed full inverse, validated nonlinear remainder, and closing inequality.
