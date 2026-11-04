# A local all-rotation shear and the missing global rank constraint

## 1. Exact statement

For every 0<c<1/2 and omega in R, put p=(1-c)/c>1, tau=omega/c, a=1-2c, b=2(1-c), J(x,y,z)=(-y,x,0), A=cI-omega J. On D={rho=sqrt(x²+y²)>0}, define

    h(theta)=exp(-1/sin²(theta)) when sin(theta)!=0, and zero otherwise,
    theta=phi+tau log rho modulo 2pi,
    u=rho^(-p)h(theta), V=u e3, P2=0,
    W=curl V, S=-u²/2, k=(Ax).V=czu.

Then V,P2 are smooth on D and solve the full rotating similarity equation and stationary Euler there. All velocity and scalar jets vanish on each sheet theta=0 modulo pi, and every such point belongs to supp_D W. They satisfy the local homogeneity, helicity, pressure and scalar-transport identities but violate grad k cross grad S=0 wherever W!=0.

The velocity has no continuous extension across the rotation axis and fails decay in the z direction. Every nonconstant W trajectory has a finite maximal interval in both time directions, with its endpoints on the missing axis. Thus it is an exact local countertest of an inference from local equations to the global-tail rank identity. It is not a whole-space counterexample.

## 2. Smoothness, flatness and support

Every derivative of exp(-1/t²) is a polynomial in 1/t times that exponential, so it tends to zero faster than every power at t=0. The chain rule gives smoothness and flatness of h at pi Z. Periodicity makes u single-valued despite using angular charts. The function theta is smooth locally and grad theta=(tau e_rho+e_phi)/rho is nonzero. Therefore V,S,k and P2 have all zero jets on the stated sheets.

Polar differentiation gives

    u_rho=rho^(-p-1)(-p h+tau h'),
    u_phi/rho=rho^(-p-1)h',
    W=(u_y,-u_x,0).

If h>0, both derivatives cannot vanish: h'=0 leaves -p h!=0. If h=0, every derivative vanishes. Hence {W!=0}={h>0}, an open dense subset of D. In particular x0=(1,0,0) is a supported infinitely flat common V,W,S zero.

## 3. Exact similarity and pressure equations

Under exp(tA), rho becomes exp(ct)rho, phi becomes phi-omega t and z becomes exp(ct)z. Thus theta is unchanged, V scales by exp(-(1-c)t), S and P2 by exp(-bt), and k by exp(-at). Rotation fixes e3, so these are the full twisted vector and scalar laws.

Because u is independent of z, div V=0, (V.grad)V=0 and JV=0. Also

    (Ax).grad u=(c rho partial_rho-omega partial_phi)u=-(1-c)u.

Consequently

    (1-c)V+DV(Ax+V)+omega JV+grad P2=0

identically. Stationary Euler holds as well. The matrix DV has only its third row nonzero and its third column zero, so (DV)²=0. Thus -Delta P2=tr((DV)²)=0 exactly. There is no omitted pressure or momentum residual.

## 4. The exact rank defect

Directly V.W=0, W.grad u=0, W.grad S=0 and W.grad k=0. Homogeneity gives X.grad S=-bS and X.grad k=-ak, with X=Ax. The vector identity can be checked without inference:

    X cross W=(cz u_x,cz u_y,cp u),
    grad k=(cz u_x,cz u_y,cu)=X cross W-aV.

Here cp-a=c. Also grad k cross V=kW. However

    grad k cross grad S=cu² W.

This is nonzero at every point of {W!=0}. Equivalently the third component of k grad S-(b/a)S grad k is (cb/(2a))u³, also nonzero. Thus full local rotating momentum and zero helicity do not imply the rank equation used for actual global HF/natural tails. A proof that imports that rank equation must retain its global derivation and hypotheses.

## 5. The pressure ratio and two global failures

At each nonzero point, S/|V|²=-1/2 and P2=0. Every neighborhood of a flat sheet contains P2<delta|V|² for every fixed delta>0, so the positive-pressure exclusion does not apply.

For any fixed horizontal point with u>0, letting z tend to infinity leaves V unchanged. This violates whole-space decay. To test the axis, take rho down to zero and phi=pi/2-tau log rho modulo 2pi, with z fixed. Then h=exp(-1), so |V|=exp(-1)rho^(-p) tends to infinity, while the points tend to the axis. This works for every finite omega, including omega=0. No cutoff or regularization is asserted to preserve the equations.

## 6. Exact maximal lifetime of vorticity trajectories

Along a nonconstant W orbit, u=U0>0 and z are constant. In polar coordinates,

    rho_dot=rho^(-p-1)h',
    phi_dot=rho^(-p-2)(p h-tau h'),
    theta_dot=p rho^(-p-2)h=pU0/rho²>0.

Choose the lifted theta in the component (0,pi). The level relation and time change are

    rho=(h(theta)/U0)^(1/p),
    dt/dtheta=h(theta)^(2/p)/(p U0^(1+2/p)).

The total time is exactly

    T(U0)=(p U0^(1+2/p))^(-1) integral_0^pi h(theta)^(2/p)dtheta.

It is finite and positive. Both endpoints have rho tending to zero. Even when the unwrapped angle phi=theta-tau log rho winds infinitely often, the physical horizontal point tends to zero. Smooth ODE continuation within D is possible at every intermediate theta, and impossible at either endpoint because the limiting point is outside D. Hence this is the full maximal time interval. There is no appeal to a recurrence or completeness theorem on the punctured domain.

## 7. Audit verdict and dependencies

All seven source sections of LIT230 were read and pinned; Sections2-6 above independently verify every formula. The construction is confirmed in its local scope. It refutes the implication from the displayed local equations to the global-tail rank identity. It neither refutes nor settles the smooth decaying whole-space conjecture. No computation, external theorem, formal build or new model client was needed. Comparison through the existing configured model agents is requested; provider runtime remains unattested.
