# Independent full-plane signed L2 certificate for d2

## 1. Claim and exact input

Let rho and U[rho] be the exact d2 canonical fields obtained from the finite rational potential in data/d2_canonical.json. The exponent is c=4076476460239181/2251799813685248 and delta=1-1/c. Put

    theta(X)=(sqrt(rho_x(X)^2+rho_y(X)^2)-rho_y(X))/2.

The target is theta(X)<=2/25 everywhere. A completed successful certificate below proves this target. An unfinished cover or failed interval test gives no counterexample and no global conclusion.

The input potential and its identification with d2 were independently checked in the earlier refit and background audits. The present code uses T4's polar density reconstruction, not N4's fourth-derivative evaluator. It compares the resulting rational gradient polynomials exactly with the frozen N4 fourth-derivative polynomials before any interval calculation.

## 2. Independent density-gradient representation

Write t=r^2/(1+r^2), u=1-t, z=cos(2theta). The reconstructed density has the finite form

    rho=r sum_(j,n) u^a R_(j,n)(t) sin(n theta),
    a=(j+1)delta/2,

where n is odd and each R is rational. The radial derivative uses

    T_(a,1)R=(1-2at)R+2t(1-t)R'.

Consequently the contribution of this density mode to rho_x is

    (u^a/2)[(T_(a,1)R-nR)sin((n+1)theta)
             +(T_(a,1)R+nR)sin((n-1)theta)],

and its contribution to rho_y is

    (u^a/2)[(T_(a,1)R+nR)cos((n-1)theta)
             +(-T_(a,1)R+nR)cos((n+1)theta)].

Use cos(2m theta)=T_m(z) and sin(2m theta)=sin(2theta)U_(m-1)(z), with the term at m=0 in the sine expression equal to zero. This gives rational bivariate polynomials X_j,Y_j with

    rho_x=sin(2theta) sum_j u^a X_j(t,z),
    rho_y=sum_j u^a Y_j(t,z).

The code checks coefficientwise that X_j=-(chi31_j+chi13_j) and Y_j=-(chi22_j+chi04_j) in N4's independent representation. No sampled equality is used.

## 3. A scalar Schur test

For tau=2/25 the target is equivalent to

    [[tau+rho_y,-rho_x/2],[-rho_x/2,tau]] >=0.

Since tau>0, it suffices and is equivalent that

    tau(tau+rho_y)-rho_x^2/4>=0.

On a cell [a,b] times[c,d] in (t,z), let Y_min be a lower bound for sum u^a Y_j and Q_max an upper bound for the modulus of sum u^a X_j. Let z_min=0 if the cell contains zero, and otherwise min(|c|,|d|). Then the following is a rigorous sufficient test:

    tau(tau+Y_min)-(1-z_min^2)Q_max^2/4>=0.                 (1)

This test differs from N4's numerical eigenvalue formula. Both concern the same matrix target.

## 4. Polynomial interval enclosure

Each cell is mapped affinely to [0,1]^2. The affine coefficient matrix and the power-to-Bernstein matrix are constructed explicitly with binomial coefficients. For a degree-N polynomial p(x)=sum p_k x^k, its Bernstein coefficient at i is

    sum_(k<=i) p_k binom(i,k)/binom(N,k).

Nonnegativity and partition of unity of the Bernstein basis enclose a polynomial by the extreme coefficients. Apply this separately in each coordinate.

There are two enclosures. The first bounds each u^a independently over the cell, multiplies by the branch polynomial range and sums the resulting intervals. It is valid even at t=1.

For b<1, a sharper correlated enclosure expands each u^a to degree8 at the radial midpoint. Put u0=1-(a+b)/2, kappa=(b-a)/(2u0), and x=(t-a)/(b-a). Then

    u^q=u0^q(1+kappa(1-2x))^q.

The degree8 Taylor polynomial is multiplied by the branch polynomial in the local x coordinate before conversion to degree-(N+8) Bernstein form. This preserves radial dependence. Taylor's theorem bounds the error by

    |binom(q,9)| u0^q kappa^9
        max((1-kappa)^(q-9),(1+kappa)^(q-9)).               (2)

In this data all q are positive and less than9, so the maximum is the first term. Multiply (2) by the maximum absolute Bernstein coefficient of the original branch polynomial and sum over branches. Adding and subtracting this nonnegative error gives a complete enclosure. The intersection of the independent and correlated bounds remains valid. Every operation uses outward Arb arithmetic.

## 5. Coverage, boundaries and stopping

The initial cells are the rational binary paths in N4's frozen complete cover. The code does not trust that cover flag: it independently checks the tree by repeatedly collapsing deepest sibling pairs until only the root remains. It rejects duplicate paths and invalid branch letters. Every failed cell is replaced by its two exact radial or angular halves; accepted and pending leaves are checked again at each checkpoint. Thus successful exhaustion of the queue certifies the complete rectangle [0,1] times[-1,1]. Every boundary is included in a closed interval.

The compactified rectangle covers a quadrant at all finite radii and its limiting points at the origin and infinity. The exact fields extend there through the displayed formulas. S1 reflection changes only the sign of rho_x; the matrix eigenvalues are unchanged. Hence a completed certificate proves the target on R2.

## 6. Scope and status

Combining this target with the independently confirmed d2 Hilbert-Schmidt interval kappa gives the signed low rate c+1-2/25-kappa. The code encloses this final comparison separately. This proves only the signed L2 condition. It does not prove the unweighted first-derivative matrix condition, the fourth-derivative caps, residual smallness, or existence of a nearby stationary profile.

The output records exact source hashes, complete coverage, all cell tests, precision and actual computation time. Until that output has no pending cells and every accepted cell passes, the numerical global assertion remains open. No formal proof-assistant build is run.
