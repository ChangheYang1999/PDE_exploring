# Point tests for the later exact N-B candidates and axis corrections

Status: analytical identities and individual point certificates CONFIRMED (V107-V109). The stated global W3 requirements are REFUTED for A4, A5 and Mpen. This is not a global positivity certificate.

## 1. Exact inputs and tested quantities

Each candidate is the real finite potential reconstructed independently in topic19 from its own exact N-B JSON file. The source and canonical hashes identify the function. Its density is rho=-chi_xxy-chi_yyy and its canonical velocity is u=(-chi_xyy,chi_xxy). The previously proved compactification and canonical uniqueness apply. Center normalization and the stationary branch constraints are checked separately by exact rational arithmetic.

For every multi-index I=(i,j), the exact derivative identities are

    partial^I rho=-chi_(i+2,j+1)-chi_(i,j+3),
    partial^I u=(-chi_(i+1,j+2),chi_(i+2,j+1)).

An ordered tensor norm of order k is the square root of the sum over i=0,...,k with multiplicity binom(k,i). For the velocity, both vector components are included. This convention is the one used in W3. Squaring intervals is performed by integer powers, so no negative square root is introduced by treating a value as two independent intervals.

At a point X define A=[[rho_y,-rho_x/2],[-rho_x/2,0]], V=cX+u and

    M=(2c+1)I+sym Du+A,
    M_k=(1+c+V.D log omega_k)I-k sym(cI+Du)+A,
    omega1=(1+r^2)^(-1/10), omega2=(1+4r^2)^(2/5).

Here V.D log omega1=-(V.X)/(5(1+r^2)) and V.D log omega2=16(V.X)/(5(1+4r^2)). The factor16 in the latter formula includes differentiation of4r^2. Each symmetric2 by2 least eigenvalue is obtained from the trace-minus-discriminant formula.

The W3 tests are |Du|<=14/5, |D rho|<=16, <r>|D2u|<=3, <r>|D3u|<=16, |D2rho|<=3, <r>|D2rho|<=8, <r>^2|D3rho|<=32 and <r>^2|D4rho|<=512. W2 requires both M_k>=I/2. A certified violation at one point disproves the corresponding global requirement. Passing every selected point leaves that global requirement open.

Every point is evaluated both by Cartesian Taylor jets through order7 and by a separately differentiated polar polynomial recurrence. Both use the exact canonical coefficients, without importing the numerical producer's evaluator. The two enclosures must overlap and be finite before a result is recorded.

## 2. Residual point lower bounds

For the weighted space of topics16,18,20, the reference-independent inequality

    |g(X)|<=16 max(1,r)^(1/5) N_(s,R)(g)

holds for0<s<=2^-12 and R>=1. Therefore every certified nonzero value of the actual residual gives

    N_(s,R)(F)>=|F(X)|/[16 max(1,r)^(1/5)].

This is a lower bound on the complete norm. It gives no upper bound and does not imply nonexistence. The threshold compared below is eta=2^-35.

## 3. Correct axis identities

Write q(y)=rho(0,y), v(y)=u2(0,y). Parity and incompressibility give

    M(0,y)=diag(2c+1-v'(y)+q'(y),2c+1+v'(y)).

Consequently the second diagonal entry is the least eigenvalue if and only if q'(y)>=2v'(y). Diagonality by itself does not imply this ordering. The correct velocity derivative is

    psi_xy(0,y)=partial_y u2(0,y)=-partial_x u1(0,y).

In contrast, -partial_y u1=psi_yy, which vanishes on x=0 by oddness of psi in x. These correct the general statement in the numerical work's07:14 note. They do not dispute its individually evaluated second diagonal entries.

The missing ordering cannot be supplied from S1 parity and center normalization alone. To see this, start with the normalized original potential and add t times

    chi_b=(x^2/4)[(y-1)^2 zeta(x^2+(y-1)^2)
                      +(y+1)^2 zeta(x^2+(y+1)^2)],

where zeta is smooth, equals1 near0 and vanishes for arguments>=1/4. This is even in both coordinates, vanishes near the origin, and is compactly supported. Its density and stream are therefore canonical perturbations preserving the center and the entire far field. At(0,1), chi_b,xxyy=1 and chi_b,yyyy=0. Thus q'-2v' changes by-3t. For large positive t the first matrix entry is smaller. This is a counterexample to the claimed implication within smooth, normalized, sublinear S1 references.

Finally let

    rho=a0 y+b y^3+d x^2y+O(r^5),
    psi=(1-c)xy+Bxy^3+Cx^3y+O(r^6), lambda=2c-1.

Direct multiplication in F=(cX+u).D rho-rho gives

    F_3=(2b+a0B)y^3+(2lambda d+3a0C)x^2y.

This confirms the cubic identity in the numerics note. Cubic stationarity implies B=-2b/a0. Locally the second matrix entry is c+2+3By^2+O(y^4), and it is the smaller one near0 because the first origin value exceeds it when a0>=1 and c>9/5. A positive cubic density coefficient b is compatible with a strictly lower floor kappa<c+2 on a sufficiently small neighborhood. A sign conclusion b<=0 from this expansion requires the zero-margin floor kappa=c+2, or an additional quantitative neighborhood condition. Topic22 supplies the complete residual-aware axis inequalities.
