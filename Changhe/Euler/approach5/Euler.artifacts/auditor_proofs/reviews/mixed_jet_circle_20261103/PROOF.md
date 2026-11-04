# Mixed higher vorticity jets on an exact local carrier circle

Status: independent reconstruction of LIT94, checked against the focused configured-model challenge. The final verdict is recorded in the auditor's ledger (AUDIT_LEDGER.md). This is local analytic existence and whole-germ nonextension, not an entire decaying profile.

## 1. Exact statement

Fix 0<c<1/2, an integer k>=3, R>0, Q!=0 and any real omega. Write

    a=1-2c, kappa=1+c, d=3c,
    lambda=(1+4c)/(k-2), D0=2c+lambda.

There is an analytic axisymmetric, swirl-free solution U,P of the complete rotating Euler equation on an annular tube about r=R,z=0. On that circle the carrier B=(cI-omega J)y+U has backward exponents (lambda,0,-d-lambda). For omega!=0 it is one periodic orbit with least period2pi/|omega|; for omega=0 it consists of equilibria. Its first nonzero vorticity derivative has order k, with leading polynomial

    W=lambda k^2 Q (r-R)^(k-1) z e_theta + higher degree.

The velocity has zero helicity. Its tube contains nonconstant closed vortex circles, so A014 forbids agreement with this entire germ by any global C2 uniformly sublinear profile in this c range, for every omega. This does not forbid a different germ with the same finite jet.

## 2. Convergent construction and incompressibility

For x near zero set

    q=Qx^k,
    psi=R^2+2R integral_0^x (1+Qs^k)^(-1) ds,
    r=sqrt(psi), r_x=R/[r(1+q)].

Shrink the interval until both the analytic denominator and the positive square root are defined. Since r(0)=R and r_x(0)=1, x=x(r) is an analytic local coordinate. Put

    A=-lambda R x/[r(1+q)], w=-kq/(1+q),
    D=D0-lambda kq/(1+q), F=A-cr,
    U=F e_r+D z e_z.

These are single-valued analytic Cartesian fields away from the axis. Direct differentiation gives

    A partial_r=-lambda x partial_x,
    A_r+A/r=-lambda(1+w),
    D=2c+lambda(1+w).

Thus div U=F_r+F/r+D=0. Also

    D_r=-lambda k^2 Q r x^(k-1)/[R(1+q)],
    W=-D_r z e_theta.

All equalities are exact analytic identities, including at x=0.

## 3. Full momentum and pressure

Axisymmetry of the Cartesian vector field means U(R_theta y)=R_theta U(y). Differentiation gives (Jy).grad U=JU. This actual equivariance identity cancels the two rotation terms for every omega; it does not omit the cylindrical basis derivative.

With X=cy+U and beta=c+D, the nongradient momentum N=(1-c)U+(X.grad)U has components

    N_r=(1-c)F+A F_r,
    N_theta=0,
    N_z=[D(1+D)+A D_r]z.

The identity lambda k=1+2D0 follows from the definition of lambda. Moreover

    A D_r=lambda^2 k^2 q/(1+q)^2.

Expanding D=D0-lambda kq/(1+q) and collecting powers gives

    D(1+D)+A D_r
      =D0(1+D0)+lambda k[lambda k-(1+2D0)]q/(1+q)
      =D0(1+D0).

Hence the analytic, single-valued pressure

    P(r,z)=-integral_R^r [(1-c)F(s)+A(s)F_r(s)] ds
              -D0(1+D0)z^2/2

cancels every momentum component. The result is the full Euler equation, not just its curl or pressure Poisson equation. The additive pressure constant is arbitrary and no normalization at infinity is asserted.

As a separate consistency check, chi=W_theta/r is proportional to x^(k-1)z/(1+q). Since Bx=-lambda x and Bz=beta z,

    Bchi/chi=-lambda(k-1)+lambda kq/(1+q)+beta
             =d-lambda(k-2)=-kappa.

The divided calculation holds off the zero set and extends across it by analyticity.

## 4. Derivative cocycle and the actual first jet

The carrier equations are r'=A(r), theta'=-omega and z'=(c+D(r))z. At the circle their radial and vertical linear rates are -lambda and d+lambda, while angular displacement has rate0. In the radial, angular and vertical basis at p0=(R,0,0), put M=diag(-lambda,0,d+lambda). The exact Cartesian cocycle is

    D Phi_s(p0)=exp(-omega sJ)exp(sM).

Differentiating this expression and using rotation equivariance of DB verifies its variational equation. The Cartesian rotating frame and its inverse remain bounded for all time. Thus the full derivative cocycle has these forward exponents, and reversing time gives the stated backward exponents. The instantaneous Cartesian eigenvalues are not used. For nonzero omega the normalized time measure on the circle is whole-flow ergodic and has time-one entropy zero; time-one ergodicity need not hold.

Write delta=r-R. The inverse coordinate is x=delta+O(delta^2). Consequently

    W=lambda k^2 Q delta^(k-1)z e_theta+O((|delta|+|z|)^(k+1)).

At a fixed circle point delta has linear part e_r dot h and z has linear part e_z dot h. Variation of e_theta contributes only one higher order. Therefore the Cartesian derivatives of W of orders below k vanish, whereas

    D^k W[e_r,...,e_r,e_z]=(k-1)! lambda k^2 Q e_theta !=0.

There are k-1 radial inputs and one vertical input. For omega!=0 the output e_theta spans the carrier line R B, and the uniform circle measure satisfies every hypothesis of A441. This realizes its flow-output resonance F_(k,k-1)=(kappa+d)/(k-2). At k=3 its value kappa+d equals the upper endpoint in A441, so that endpoint is compatible with the actual curl constraint and full local Euler. It is not a consequence of allowing an arbitrary independent tensor. For omega=0 the same tensor and equilibrium spectra hold, but A441 does not apply: B=0, and the zero-exponent direction is tangent to a circle of equilibria rather than spanned by B.

## 5. Scope and dependencies

At fixed x!=0,z!=0 inside the tube, W is a nonzero constant multiple of e_theta along its whole circle. This is a nonconstant closed orbit of the frozen-vorticity flow. It can be chosen arbitrarily close to the carrier circle. The A014 global vortex-period obstruction applies to any hypothetical uniformly sublinear global extension agreeing on this tube. No assumption about continuation to the axis is needed for that exclusion.

The construction supplies neither a smooth global extension nor decay. It does not establish completeness of arbitrary local trajectories. The carrier circle and its derivative cocycle themselves are defined for all time inside the tube. No computational step is needed for the convergent integral and exact identities above; the source's finite symbolic test is not being used as a substitute for them. Analytic inverse-function theory and the already audited A014 and A441 are the only external dependencies.
