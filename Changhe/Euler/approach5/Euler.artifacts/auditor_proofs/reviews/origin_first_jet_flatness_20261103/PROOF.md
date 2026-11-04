# First vorticity flatness at a zero-velocity origin

Status: CONFIRMED A472 at the exact hypotheses below after independent reconstruction, full postwrite inspection and the complete focused configured-model review. The global decay-only conjecture remains open.

## 1. Exact statement

Let U in C2(R3;R3), P in C1 solve

    div U=0, (1-c)U+B.grad U+omega JU+grad P=0,
    A=cI-omega J, B=Ay+U, W=curl U,
    0<c<1/2, omega in R.

Assume U=o(|y|) uniformly and U.W=0 everywhere. If U(0)=W(0)=0, then DW(0)=0. Moreover O={W!=0} is never dense on a neighborhood of0. If0 lies in closure(O), then M=DU(0)!=0, and every limiting direction x of O at0 lies in the proper closed algebraic cone (Mx) cross (Gx)=0, with G given in(1).

For a negative-covector exceptional support from A444-A445, a carrier equilibrium at the spatial origin belonging to that support satisfies U=W=0 and is therefore first-vorticity-flat. A regular support point whose coordinates happen to be zero need not have U=0 and is not covered by this application. The independent A464 excludes that zero-velocity support equilibrium, and A467 excludes the exceptional measure. These stronger dependencies are distinct from the pointwise result proved here. No growth bound for a general carrier equilibrium follows.

## 2. The Hessian rank consequence

Set a=1-2c, kappa=1+c,

    H=P+|U|^2/2+(Ay).U, g=U.B,
    M=DU(0), N=DB(0)=A+M, K=DW(0).

The Lamb identity grad H=-aU+B cross W makes H C2, and g is C2. Since U(0)=B(0)=W(0)=0, M is real symmetric and trace-free, and

    grad H(0)=grad g(0)=0, Hess H(0)=-a M,
    G:=Hess g(0)=M^T N+N^T M
                 =2M^2+2cM+omega(JM-MJ).                (1)

Only two derivatives of U are needed: in differentiating g twice, all terms involving U(0) or B(0) vanish.

Assume first that O is dense in a neighborhood of0. The confirmed A413 identity dH wedge dg=0 on O extends continuously throughout that neighborhood. At y=t x, the C2 first-gradient Taylor expansions, divided by t^2, give

    (Mx) cross (Gx)=0 for every x.                       (2)

If M is nonzero, its symmetry and zero trace imply rank M>=2. The following elementary fact then yields G=rho M for some real rho: whenever linear maps L,Q have rank L>=2 and Lx,Qx are dependent for every x, Q is a scalar multiple of L. Choose x1,x2 with independent L images. Comparing x1,x2 and x1+x2 equates their scalar factors. Every other nonzero L image is independent of at least one of these, fixing the same factor. If Lx=0, comparison at x+x1 and x+x2 puts Qx in two independent image lines, so Qx=0.

Taking traces in(1) now gives

    0=rho tr M=tr G=2 tr(M^2).

The commutator has trace zero. Symmetry of M implies tr(M^2)=|M|_F^2, so M=0, a contradiction to the assumed nonzero M. Hence local density implies DU(0)=0.

## 3. Nonzero DW supplies density and contradicts transport

Suppose K!=0. Some scalar component of W has nonzero differential at0 and remains a submersion on a neighborhood. Its zero set is a C1 embedded surface of empty interior. The common zero set of W is contained in this surface, so O is dense in that neighborhood. Section2 therefore gives M=0 and N=A.

At the equilibrium0, the differentiated Cauchy identity is

    K e^(tN)=e^(-kappa t)e^(tN)K,
    N K-K N=kappa K.                                    (3)

The first identity follows by one spatial derivative of Cauchy transport; the flow-Hessian term is multiplied by W(0)=0. The second follows by differentiating in time. Alternatively insert W(y)=Ky+o(|y|), B(y)=Ny+o(|y|), DB(y)=N+o(1) and DW(y)=K+o(1) into DB W-DW B=kappa W and compare first-order terms. This gives the same commutator without differentiating the flow. No second derivative of W is taken.

With N=cI-omega J, the commutator in(3) is T K-K T for the real skew matrix T=-omega J. Its Frobenius inner product with K is zero:

    tr(K^T T K)-tr(K^T K T)=0,

since cyclically the two traces pair a skew matrix with the symmetric matrices KK^T and K^T K. Taking the inner product of(3) with K gives kappa|K|_F^2=0. As kappa>0, K=0, contradicting the assumption. Thus DW(0)=0 in all cases.

## 4. A zero velocity derivative forces local irrotationality

Suppose U(0)=0 and DU(0)=0. Choose r>0 so ||DU(y)||<=c/2 on the closed ball Bbar(r). Then |U(y)|<=(c/2)|y| and

    y.B(y)>=c|y|^2/2.

The closed ball is forward invariant for the backward carrier field -B. A trajectory starting there is defined for every nonnegative backward time: it stays in this compact ball, and local existence and uniqueness extend it through each finite time. Let v(t)=D Psi_t(x)v0. Its variational equation and the symmetric-part bound give

    d|v(t)|^2/dt=-2v.DB v>=-3c|v(t)|^2,
    |D Psi_t(x)v0|>=exp(-3ct/2)|v0|.

Here the skew rotational part contributes zero; no bound for omega is used. Cauchy transport implies

    |W(Psi_t x)|>=exp((kappa-3c/2)t)|W(x)|
                  =exp((1-c/2)t)|W(x)|.

Since c<1/2, the exponent is positive. W is bounded on the compact ball, so W(x)=0 for every x there. Thus U(0)=DU(0)=0 forces local irrotationality. The argument itself only needs the displayed Cauchy law and local C1 carrier regularity; the global hypotheses enter elsewhere.

If O were dense on a neighborhood of0, Section2 would give M=0 and the preceding paragraph would give W=0 on a smaller ball. This contradicts density. Hence the earlier conditional density implication is true but vacuous. If0 belongs to closure(O), then M cannot vanish.

## 5. The proper cone of approach directions

Assume0 belongs to closure(O). For any sequence y_n in O tending to0 with y_n/|y_n| tending to x, Taylor expansion of the two gradients at0 and the exact rank identity at y_n imply

    (Mx) cross (Gx)=0.

This does not require O to be dense on a whole neighborhood. The three components of this cross product are homogeneous quadratic polynomials in x, so their common zero set is a closed algebraic cone. If the cone were all of R3, the rank-at-least-two proportionality and trace argument of Section2 would force M=0. Section4 excludes this. The cone is therefore proper.

More precisely, every open neighborhood in the unit sphere of the cone's intersection with that sphere contains all sufficiently small nonzero directions of O. Otherwise a sequence of violating directions has a convergent subsequence, and its limit both satisfies the cone equation and lies in the closed complement, a contradiction. No fixed positive opening angle or rate of tangency is asserted.

## 6. Dependencies and limits

A413 is applied only on O and, when density is supplied by the hypothetical nonzero K, on a whole neighborhood. Membership of one point in closure(O) alone gives the cone constraint, not the all-directions Taylor identity. Nonzero K supplies neighborhood density through a submersion, and that density is impossible.

An equilibrium with U=0 can occur only at spatial0 because A is invertible. Nonzero equilibria with U=-Ay!=0 are outside the pointwise origin statement. The actual conclusions are DW(0)=0, impossible local vortical density, and nonzero DU(0) with restricted approach directions when0 lies in closure(O). No upper bound for DU(0) or its backward growth follows. First-vorticity flatness alone is not a claim of local irrotationality; the separate DU(0)=0 assumption is essential to Section4.

The full focused coordinator review independently supplies Section4's strengthening and checks all earlier steps. No computation is needed or used for this reconstruction. Source pins retain the initial submission alongside current reviewed evidence. Pressure normalization and a third velocity derivative are unnecessary.
