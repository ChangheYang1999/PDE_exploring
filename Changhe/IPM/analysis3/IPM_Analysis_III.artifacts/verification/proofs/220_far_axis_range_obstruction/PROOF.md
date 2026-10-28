# A far-axis range obstruction in the common Holder target

## Exact statement

Fix 0<alpha<1 and 4k<gamma<2. Use the exact joined normalized modal trial rho0, k=1615536043799051/9007199254740992, ell=1/k, and the space

 Y=E2 intersect L2((1+r^2)^(-gamma/2)dX),
 ||h||Y=||h||infinity+[h]_x,alpha+[h]_(y,2,alpha)+||h||L2(w_gamma),
 [h]_(y,2,alpha)=sup |h(x,y)-h(x,y')|/(x^2|y-y'|^alpha).

Every input has physical parity even in x and odd in y, and vanishes on x=0. Let

 V=ell X+U[rho0], T=V.grad-1,
 D_Y={h in Y:V.grad h is in Y distributionally},
 A0=T+C0, C0h=U[h].grad rho0+c[h]M0,
 L_ren=T+C_ren, C_renh=U[h].grad rho0+c[h]H0,

with the canonical velocity and the exact finite moving-tail column M0 of proof 217. The compact column H0 is the one in proof 214. These operators have the closed maximal realization of topics214 and217.

The algebraic quotients Y/Range(A0), Y/Range(L_ren), and Y/Range(T) are all infinite dimensional. In particular none of these operators is onto Y or Fredholm on this graph. Their failure of surjectivity remains if the domain is restricted by any additional homogeneous normalization conditions.

There are explicit smooth forcings f_b in D_Y with J(f_b)=c[f_b]=0, indexed by any infinite set of distinct b in (1/2,1), whose cosets are linearly independent in each quotient. The obstruction occurs on a strip near the vertical axis at infinity. It does not contradict the local extension inverses or the global bounded-coupling and closedness statements. It is a failure of this precise common target and maximal domain. It does not imply that the actual residual F0 is outside the range, exclude inverses on other spaces, settle the high/low Sobolev injectivity condition (I), or prove nonexistence of a profile.

All estimates below are qualitative. There is no numerical inverse or residual calculation.

## Background estimates and forward characteristics

The exact outer modal formulas imply, uniformly for large r, including smooth angular division across the axes,

 |U1[rho0](X)/x|+|U2[rho0](X)/y|<=C r^(k-1).       (1)

The quotients at zero coordinates are continuous limits. To justify (1), each leading density term is a finite angular polynomial times r^q with q<=k<1. Its canonical modal Green velocity has the same leading power, with smooth finite angular factors; logarithmic matching terms have a strict lower power and can be absorbed in r^k. The exterior harmonic terms decay. No growing harmonic velocity is admitted in this convention. The velocity components have respectively odd-x and odd-y parity. Division of their finite angular sums by cos(theta) and sin(theta) is bounded on their respective vanishing subspaces, giving (1). Equivalently the exact homogeneous Green formulas of proof 35 and the outer expansion of proof 117 give these estimates after one angular division. This uses the velocity, not an assumed Riesz bound on the growing rho0 in Y.

Choose R large enough that the entire region y>=R lies in the outer formula and C R^(k-1)<=ell/2 in (1). For a starting point (x,Y), with 0<x<1 and Y>=R fixed, write its forward actual characteristic as (x_t,y_t). The field preserves the first quadrant because V1=x(ell+U1[rho0]/x) and V2=y(ell+U2[rho0]/y), with continuous locally Lipschitz coefficients. On y>=R, y_t increases at least as Y exp(ell t/2), so the trajectory stays in this region. It exists for all t>=0 because V has at most linear growth.

Along this trajectory, the integrals of both errors V1/x-ell and V2/y-ell are absolutely bounded, uniformly in t and 0<x<1:

 integral_0^infinity C r_t^(k-1)dt
 <=C Y^(k-1) integral_0^infinity exp(-ell(1-k)t/2)dt<infinity.

Exponentiating the two scalar equations therefore gives constants a_Y,B_Y>0 such that

 a_Y x exp(ell t)<=x_t<=B_Y x exp(ell t),
 a_Y Y exp(ell t)<=y_t<=B_Y Y exp(ell t),
 a_Y Y exp(ell t)<=r_t<=2 B_Y Y exp(ell t),          (2)

for every t>=0 and 0<x<1, after enlarging B_Y. Exact exponent ell is retained. Replacing it by ell plus a fixed error would lose the critical estimate used below.

If h and Th are continuous and the transport equation holds distributionally, it holds along these characteristics in the usual integral form. Indeed a smooth flow-box change of variables reduces the distributional equation to a one-dimensional derivative with continuous right side; the resulting integral identity, initially for almost every transverse coordinate, extends to every coordinate by continuity. Such boxes cover each finite trajectory segment. For bounded h, taking the endpoint time to infinity gives

 h(x,Y)=-integral_0^infinity exp(-t)(Th)(x_t,y_t)dt. (3)

For equations A0h=f or L_ren h=f, the right side Th=f-C[h] is bounded and continuous by topics214/217, so (3) applies. The endpoint term exp(-t)h(x_t,y_t) tends to zero by boundedness of h.

## The nonlocal term has only a logarithmic divided characteristic bound

Put M=||h||Y. Proof 214 proves globally

 ||U1[h]/x||infinity<=C M,
 |U[h](X)|<=C M(1+log(2+r)).                       (4)

Its exact divided density coefficients satisfy on the outer region

 |rho0_x/x|<=C r^(k-2), |rho0_y/x^2|<=C r^(k-3),
 |grad rho0|<=C r^(k-1).                           (5)

Thus the unnormalized coupling B[h]=U[h].grad rho0 has both bounds

 |B[h](X)|<=C M x^2 r^(k-2),
 |B[h](X)|<=C M r^(k-1)(1+log r),                 (6)

for sufficiently large r. For the first, divide by x^2 to get (rho0_x/x)(U1[h]/x)+(rho0_y/x^2)U2[h]. The second term is absorbed in r^(k-2) because (1+log r)/r is bounded. No derivative of h is used, and the first estimate holds at every angle, including large x.

Insert (2) into both estimates (6). Since ell k=1 exactly,

 exp(-t)|B[h](x_t,y_t)|
       <=C_Y M min(x^2, (1+t)exp(-ell t)).          (7)

For 0<x<1/2 split the time integral at t_x=2log(1/x)/ell. The first term of (7) gives C_Y M x^2 t_x before t_x. The second gives at most C_Y M(1+t_x)exp(-ell t_x) afterwards. Consequently

 integral_0^infinity exp(-t)|B[h](x_t,y_t)|dt
       <=C_Y M x^2(1+log(1/x)).                    (8)

This estimate controls the whole future trajectory, including the part after it leaves the strip x<=1. Discarding that part without a bound would not justify a range obstruction for the full nonlocal operator.

Take R larger also than the support of H0 and the chart cutoff transitions. Proof 217 gives

 |M0(X)/x^2|<=C r^(2k-3)(1+log r),                 (9)

on this outer region, with smooth division across the vertical axis. Since |c[h]|<=4M/pi, (2) and (9) give

 exp(-t)|c[h]M0(x_t,y_t)|
       <=C_Y M x^2(1+t)exp((1-ell)t).

This is integrable because ell>1. Its time integral is O_Y(M x^2). The compact H0 term is zero along these trajectories. Combining with (8), for either C=C0 or C=C_ren,

 |integral_0^infinity exp(-t)C[h](x_t,y_t)dt|
       <=C_Y M x^2(1+log(1/x)).                    (10)

The same bound holds trivially for C=0. This is the quantitative reason the coupling and the exact moving-tail column cannot cancel the forcing constructed next. Small output tails alone would not give (10).

## Smooth forcings in the actual target and graph

Fix a smooth even nonnegative phi on R with phi=1 on |x|<=1 and phi=0 on |x|>=2. Fix a smooth odd function g_b, zero for |y|<=2R, positive for y>2R, and equal y^(-b) for y>=3R, with its odd reflection for negative y. A common smooth cutoff times sign(y)|y|^(-b) supplies these functions for every b in (1/2,1). Set

 F_b(x,y)=x^2 phi(x)g_b(y).                         (11)

It is smooth, has physical parity, vanishes near the physical origin, and has J(F_b)=0. Its supremum and horizontal Lipschitz norm are bounded. Its divided vertical cofactor is phi(x)g_b(y), a bounded Lipschitz function of y uniformly in x. Hence F_b belongs to E2 for every alpha<1. Its far weighted L2 integral is bounded by a constant times

 integral_(3R)^infinity y^(-2b-gamma)dy,

which is finite because 2b+gamma>1. In the common range gamma>4k>0, every b>1/2 suffices. Thus F_b belongs to Y.

It also belongs to D_Y. On |x|<=2, y>=3R, direct differentiation of (11) gives a divided transport image of size O(y^(-b)), with bounded first derivatives and the same square-integrable tail. In detail the terms after division by x^2 are (2V1/x-1)phi g_b, V1 phi' g_b, and V2 phi g_b'. The exact coefficients (1) and their differentiated outer bounds give the asserted orders. The compact transition regions give finite smooth bounds. The physical parities and x^2 factor are preserved. These estimates check the actual transport graph, not just input membership.

Choose a fixed smooth compact physical-parity q, supported in an annulus below radius R, with J(q)=0 and c[q]=1. Such q is explicitly constructed in proof 204; it belongs to D_Y by proof 214. The bounded strain of (11) is well defined. Put

 f_b=F_b-c[F_b]q.                                  (12)

Then f_b belongs to D_Y, is smooth, and satisfies c[f_b]=J(f_b)=0. The correction vanishes on every characteristic starting at y=Y>=3R, because y_t never decreases below Y. It therefore has no effect on the next estimates. Neither the forcing nor its image is assumed compact in the y direction.

## Failure of surjectivity

Fix b in (1/2,1), fix Y>=3R, and suppose A0 h=f_b for some h in D_Y. The same argument will cover L_ren or T. For all forward times the forcing along the trajectory is nonnegative and its correction q is zero. Until x_t reaches1, (2) and (11) give

 f_b(x_t,y_t)>=a_Y^2 B_Y^(-b)Y^(-b)
                             x^2 exp(ell(2-b)t).

In particular this holds for 0<=t<=tau_x=log(1/(B_Y x))/ell when x<1/B_Y. Let Q_b=ell(2-b)-1. Since b<1 and ell>1, Q_b>0. Integration and ell k=1 yield

 I_b(x,Y):=integral_0^infinity exp(-t)f_b(x_t,y_t)dt
       >=c_Y,b x^2(exp(Q_b tau_x)-1)
       >=d_Y,b x^(k+b)-C_Y,b x^2,                 (13)

where d_Y,b>0. The forcing remains nonnegative after tau_x, so ignoring it there is legitimate.

Equation (3) with Th=f_b-C0h and (10) gives

 |h(x,Y)|>=I_b(x,Y)
          -C_Y M x^2(1+log(1/x)).                  (14)

On the other hand, oddness in y and the defining weighted seminorm imply

 |h(x,Y)|<=M x^2 Y^alpha.                          (15)

Combining (13)-(15) and dividing by x^2 would bound d_Y,b x^(k+b-2) by a constant times 1+log(1/x). This is impossible as x tends to zero, because k+b<k+1<2. Thus no such h exists. The coupling estimate (10) also covers L_ren and T, proving failure of surjectivity for all three operators. The forcings already have exact zero strain and zero cubic normalization.

## Infinite algebraic codimension and scope

Choose distinct b_j in (1/2,1). Consider a nonzero finite combination f=sum_j a_j f_(b_j), and let b_* be the least exponent with a_j nonzero. Change the overall sign if necessary so its coefficient is positive. For all sufficiently large y, the scalar tail sum satisfies

 sum_j a_j y^(-b_j)>=(a_*/2)y^(-b_*)>0.

Choose the starting height Y larger than this threshold and 3R. The correction q still vanishes on the entire trajectory. The forcing is now nonnegative there and obeys the same lower bound (13) with b_* and a different positive constant. Equations (10),(14),(15) give the identical contradiction. Therefore no nonzero finite combination belongs to the range of any of the three operators. Their cosets are linearly independent, proving that all three algebraic cokernels are infinite dimensional.

A Fredholm operator has finite-dimensional algebraic cokernel and closed range, so these operators are not Fredholm, irrespective of whether their ranges are closed. No closed-range claim is made here. Restricting the domain can only shrink the range and cannot restore surjectivity onto Y.

The theorem concerns this common Holder target, whose allowed slowly decaying strip forcings are responsible for (13). It does not identify the range of the particular residual F0, construct a kernel, bound an inverse on the range, or address the other weighted Sobolev spaces of the S2 campaign. A different far-axis target condition could exclude (11). The local inverses and bounded cutoff maps remain valid, but they cannot be patched into a right inverse onto this Y for the full actual linearization.

Dependencies: topics35 and117 for canonical outer velocity powers; proof 50 for exact differentiated density and joins; topics213/214 for Y, canonical global velocity bounds and the actual maximal graph; proof 217 for the exact moving-tail column and its divided far bound; proof 204 for the compact strain correction. The flow estimates, full-trajectory coupling integral, forcing membership, noncancellation and infinite-codimension argument are independently proved above. No computation or new certified numerical constant is used.
