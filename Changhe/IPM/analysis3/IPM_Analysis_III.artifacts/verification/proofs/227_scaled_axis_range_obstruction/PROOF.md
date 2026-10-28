# The locally quadratic, isotropically scaled target still has infinite cokernel

## Exact statement

Use the exact joined normalized trial rho0 and canonical IPM velocity U, strain c, columns H0,M0, k=1615536043799051/9007199254740992 and ell=1/k. Fix

 0<alpha<1, 2k-1<beta<k, gamma>4k.

Let Z=Z_(alpha,beta,gamma) be exactly proof 222's space: the fixed local norm ||chi h||E2 with chi=1 on B2 and chi=0 outside B4; the overlapping isotropic annular C^alpha norm of growth beta; and L2((1+r^2)^(-gamma/2)dX). Every h is even in x, odd in y, continuous, and zero on x=0. In particular the quadratic vertical-axis control is imposed only through chi h, whereas outside B4 the norm requires ordinary C^alpha regularity and axis vanishing.

On the exact maximal domain

 D_Z={h in Z: V.grad h is in Z distributionally},
 V=ell X+U[rho0], T=V.grad-1,

consider the three closed operators T, Lren=T+U[.].grad rho0+c[.]H0 and A0=T+U[.].grad rho0+c[.]M0 of proof 222. Then

 Z/Range(T), Z/Range(Lren), Z/Range(A0)

are all infinite dimensional as algebraic vector spaces. None is onto or Fredholm. This holds even before imposing a cubic normalization or any other domain restriction.

The representatives below are compactly supported elements of D_Z, are smooth near the origin and have exact J=c=0. They have a fractional transverse power on a distant segment of the vertical axis and need not be globally smooth. The actual residual F0 is not shown to be outside any range. This theorem does not contradict the genuine auxiliary exterior inverse of proof 223: its exterior domain does not impose the local quadratic condition near the physical origin. It does not settle the distinct Sobolev condition (I), disprove existence of a profile, or rule out spaces that retain an appropriate quadratic axis condition throughout the outgoing vertical separatrix. All constants are qualitative.

## Actual characteristics starting near the interior vertical axis

Fix y0=1/2. The actual field has exactly the three zeros 0 and (+/-p,0), with no nonzero zero on the vertical axis (proof 88, taking its perturbation to be zero). Near0 its vertical rate is D>0. By continuity, parity and absence of another vertical-axis zero,

 V2(0,y)>0 for every y>0.                         (1)

Its scalar vertical orbit starting at y0 reaches every fixed large height R in finite time. Only this axis sign is needed, not a global planar limit-set assertion.

For large r, the finite modal formulas, including division by the parity factors, give

 |V1(x,y)/x-ell|+|V2(x,y)/y-ell|<=C r^(k-1).       (2)

The quotients are continuous on their axes. Choose R so large that (2)'s error is at most ell/2 for y>=R. Let T_* be a finite time at which the axis orbit from y0 lies above 2R. Continuous dependence on the initial point implies that, for some x0>0, every orbit Phi_t(x,y0)=(x_t,y_t), 0<x<x0, stays in a fixed compact annular neighborhood of this axis segment for 0<=t<=T_* and has y_(T_*)>R. The quotient V1/x is bounded on that compact neighborhood, so x_t/x is bounded above and below by positive constants there. Also y_t and r_t are bounded above and away from zero there.

For t>=T_*, (2) gives y_t>=y_(T_*) exp(ell(t-T_*)/2). Its error terms have absolutely bounded integrals because k<1. Integrating the two scalar quotient equations, and combining with the finite initial segment, yields constants a,B>0, independent of 0<x<x0 and all t>=0, such that

 a x exp(ell t)<=x_t<=B x exp(ell t),
 a exp(ell t)<=y_t<=B exp(ell t),
 a exp(ell t)<=r_t<=2B exp(ell t).                (3)

After decreasing x0, also x_t/y_t<= (B/a)x <1/4 for every t>=0. The orbit stays in a fixed narrow cone about the positive vertical axis for all future time. It may cross many spline knots; global C1 regularity suffices for the flow and the scalar equations.

## The whole coupling integral has higher transverse order

Write N=||h||Z. Proof 222 proves the scaled velocity estimate

 ||U[h]||Linf(A_r)+r^alpha[U[h]]_(C^alpha(A_r))
 <=C N r^beta,                                  (4)

on fixed comparable-radius annuli for r>=2. The same estimate with a changed constant holds on the fixed compact annular region containing the initial trajectory segment: local C^alpha control and the separated far kernel prove it exactly as in proof 222. Thus (4) can be used along (3), with r bounded away from zero.

U1 is odd in x and vanishes on x=0. Comparing (x_t,y_t) with (0,y_t), which has comparable radius, gives

 |U1[h](x_t,y_t)|<=C N x_t^alpha r_t^(beta-alpha),
 |U2[h](x_t,y_t)|<=C N r_t^beta.                 (5)

No derivative of h or Lipschitz bound for U1 is assumed. The exact background has, by its finite angular divisions and local regularity,

 |rho0_x(x_t,y_t)|<=C x_t r_t^(k-2),
 |rho0_y(x_t,y_t)|<=C x_t^2 r_t^(k-3).           (6)

For the bounded initial annular segment the powers merely change the constant. Equations (3),(5),(6) imply

 |U[h].grad rho0(x_t,y_t)|
 <=C N (x^(1+alpha)+x^2) exp(ell(beta+k-1)t).

Since ell k=1, integration against exp(-t) is convergent with exponent ell(beta-1)<0. Hence the ENTIRE future trajectory satisfies

 integral_0^infinity exp(-t)|U[h].grad rho0(Phi_t(x,y0))|dt
 <=C N (x^(1+alpha)+x^2).                        (7)

The compact H0 is quadratically divisible by x, so its characteristic integral is O(x^2); its intersection with this trajectory occurs in a uniformly bounded time interval. For M0, proof 217 and its sharp tail clarification give

 |M0(x,y)/x^2|<=C r^(2k-3)(1+log r)

for large r, with a finite bound on the compact initial segment. The strain obeys |c[h]|<=C N by proof 222. Inserting (3), its tail integral is bounded by

 C N x^2 integral_0^infinity (1+t)exp(ell(k-1)t)dt<infinity.

Consequently, for C equal to C0, Cren, or zero,

 integral_0^infinity exp(-t)|C[h](Phi_t(x,y0))|dt
 <=C N x^(1+alpha), 0<x<min(x0,1),               (8)

where x^2<=x^(1+alpha) because alpha<1. This bound includes the exact moving-tail column and the complete nonlocal velocity, including the part of the orbit at infinity. It is not an estimate obtained by discarding the remote trajectory.

## Compact forcing classes with exact zero strain

Choose a large Y>4 and a nonnegative smooth function g_+ supported in (Y,2Y) and positive on a closed subinterval. Let g be its odd extension. Choose an even smooth cutoff phi(x), equal one for |x|<=1 and zero for |x|>=2. For every exponent

 alpha<sigma<1+alpha

put

 F_sigma(x,y)=|x|^sigma phi(x)g(y).              (9)

This is compactly supported away from B4, has the physical parities and vanishes on x=0. It belongs to C^alpha, hence to Z; its local E2 factor is zero and its weighted L2 norm is finite. It is identically zero near the origin, so its ordinary local cubic coefficient J exists and is zero.

It also belongs to D_Z. On its compact support, write V1=x a1(x,y) with C^1 a1. In the distributional transport derivative, the potentially singular horizontal derivative is multiplied by x:

 V1 partial_x |x|^sigma=sigma a1(x,y)|x|^sigma.

This is C^alpha. The cutoff and vertical derivatives have the same regularity. No axis distribution occurs, since |x|^sigma is locally absolutely continuous and sigma>0. Thus T F_sigma is compactly supported C^alpha, zero near0, and belongs to Z.

Fix one smooth compact physical-parity q, supported away from B4 and away from a fixed cone about the vertical axis, with c[q]=1. It exists by placing a nonnegative bump in a first-quadrant angle where sin(3theta) is nonzero, reflecting with the density parities, and dividing by its nonzero strain integral. Such a q has J(q)=0 and is in D_Z. Define

 f_sigma=F_sigma-c[F_sigma]q.                    (10)

All these forcings have exact c[f_sigma]=J(f_sigma)=0 and belong to D_Z. The strain is absolutely defined because their support avoids the origin. By decreasing x0 further, the entire trajectory (3) avoids the support of q.

## Characteristic contradiction and independent range cosets

For any h in D_Z, the continuous distributional equation along the C1 flow gives the ordinary characteristic identity. The growth bound |h(Phi_t X)|<=C N exp(ell beta t), together with beta<k, makes the endpoint exp(-t)h(Phi_t X) tend to zero. If (T+C)h=f_sigma, then

 h(x,y0)=-integral_0^infinity exp(-t)f_sigma(Phi_t(x,y0))dt
          +integral_0^infinity exp(-t)C[h](Phi_t(x,y0))dt.  (11)

The distributional justification is the flow-box argument in proof 223's audit clarification: integrate on almost every transverse orbit, extend by continuity, then take the infinite-time endpoint using the displayed bound.

The forcing integral in (11) has an exact leading transverse asymptotic

 integral_0^infinity exp(-t)f_sigma(Phi_t(x,y0))dt
   =a_sigma x^sigma+o(x^sigma), a_sigma>0.        (12)

Indeed the q contribution is zero. The times at which the orbit meets the support of g lie in a common bounded interval, since the axis orbit crosses that compact vertical interval with positive speed and nearby trajectories do likewise. On this interval, x_t/x converges uniformly as x tends to zero to the positive scalar variational factor along the axis orbit, and y_t converges uniformly to that orbit. Also phi(x_t)=1 for all sufficiently small x. Dominated convergence proves (12), and positivity of g on a subinterval proves a_sigma>0. The assertion about a common bounded interval also follows from (3) for late times and compact positive vertical speed during the crossing. No sign contribution appears outside it.

Because chi=1 near (0,y0), the local E2 condition and odd-y parity give

 |h(x,y0)|<=N x^2 |y0|^alpha                     (13)

for small x. Equations (8),(11)-(13) are impossible: sigma<1+alpha<2, so dividing by x^sigma makes both (13) and (8) tend to zero, whereas (12) tends to a_sigma>0. Thus f_sigma has no preimage under any of the three operators.

Take any finite nonzero linear combination of distinct f_sigma. Its characteristic forcing integral is dominated, as x tends to zero, by the nonzero coefficient of the least exponent sigma, using (12). The same contradiction applies. Hence their cosets are linearly independent for every infinite set of distinct exponents in (alpha,1+alpha), proving the infinite algebraic cokernel statements.

The obstruction is transverse regularity transported along the actual outgoing vertical axis. Ordinary scaled far Holder control removes the previous global-weight obstruction but permits forcings incompatible with the retained local quadratic axis condition. Retaining a suitable scaled quadratic axis norm globally is a candidate next space, not an inverse theorem. The exact residual is smoother along that axis than the constructed representatives, so no actual-residual range failure has been proved.

## Dependencies and verification scope

Proof 88 supplies the already independently certified absence of a nonzero vertical-axis zero; only its unperturbed case is used. Topics35/117 and220 give the exact far quotient bounds. Proof 222 supplies Z, bounded strain, scaled velocity bounds, full mapping and the closed maximal domain. Proof 217 supplies the exact moving-tail divided bound and local regularity. Proof 223 supplies the explicitly justified characteristic identities. Every other step, the forcing/image memberships and the full characteristic integral are derived above. There is no numerical computation or new certified number.
