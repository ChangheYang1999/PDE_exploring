# The analytic value-trace hypothesis is not automatic from harmonicity on one side

Status: a complete local counterexample to deleting the value-trace hypothesis in166. This is not a counterexample B2 solution and does not decide the full smooth equations.

## Statement

There are a rectangle R about(0,0) in physical orthonormal coordinates(u,v), and a C-infinity field W on R, such that:

* div W=4, W(0)=0 and DW(0)=diag(0,4).
* The local zero set is exactly{(u,0):u<=0}; the normal nullcline is v=0 and its reduced horizontal field is exp(-1/sqrt(u)) for u>0 and0 for u<=0.
* curl W=0 on the entire right half-rectangle. In particular every transverse curl trace v -> curl W(u,v), u>0, is analytic on one common interval.
* Both value traces v -> W_1(0,v) and v -> W_2(0,v) fail to be analytic on every interval about0, although W_1(0,v) and W_2(0,v)-4v are flat at0.

Thus transverse analytic curl, constant divergence, an outgoing zero-arc endpoint and an analytic full jet at that endpoint do not imply the missing analytic value traces. The conclusion concerns these partial local hypotheses. It does not show that the full B2 equations cannot force those traces. The local field is also the explicit endpoint field already embedded in the nonprofile construction161.

## Construction and smoothness

Choose pi/2<theta0<theta1<pi and a smooth even angular cutoff kappa that equals1 for |arg z|<=theta0 and0 for |arg z|>=theta1. For z=u+iv in the slit plane, take the principal square root and put

    g(z)=exp(-z^(-1/2)),
    P(z)=z int_0^1 exp(-(tz)^(-1/2)) dt.

On closed sectors |arg z|<=theta1, Re(z^(-1/2))>=cos(theta1/2)|z|^(-1/2)>0. Hence g and every fixed derivative decay faster than every power as z tends0, uniformly on that sector. Differentiating the integral gives

    P'(z)=int_0^1 d_t[t g(tz)]dt=g(z),

because the t=0 boundary term vanishes. The same exponential estimates justify differentiation and show P and all its derivatives are flat at0. Define H=kappa(arg z) Im P(z), set it to0 outside the sector, and set H(0)=0. Derivatives of the angular cutoff cost fixed powers of |z|^-1, which are absorbed by the exponential. Thus H extends smoothly across0 and is flat there. It is odd in v by conjugation symmetry. Set

    W=(H_v, 4v-H_u).

Equality of mixed derivatives gives div W=4 everywhere, and flatness gives W(0)=0 and DW(0)=diag(0,4). On |arg z|<theta0, the Cauchy-Riemann equations give

    W=(Re g(z), 4v-Im g(z)),       curl W=-Delta H=0.

The sector contains the entire right half-plane. Near every negative-axis point, H=0. Choose a small rectangle inside the construction disk. Because H is flat, |H_uv|<1 on this rectangle. Since W_2 is odd in v,

    W_2(u,v)=v int_0^1 [4-H_uv(u,tv)]dt,

so its second factor is greater than3. Its only zeros are v=0. Along that line, H_v(u,0)=g(u)>0 for u>0 and H_v(u,0)=0 for u<=0. This proves the exact zero-set and outgoing assertions.

## The value traces are flat and nonanalytic

For v!=0, put a=1/sqrt(2|v|). The vertical line is inside the sector where kappa=1, and the principal branch gives

    g(iv)=exp(-a)[cos a + i sign(v) sin a].

Consequently

    W_1(0,v)=exp(-a) cos a,
    W_2(0,v)-4v=-sign(v) exp(-a) sin a.

Both extend smoothly by0 and have every derivative zero at0, by the exponential bounds above. They are not identically zero on any interval about0. Indeed for positive integers n let

    v_n=1/[2(2 pi n)^2],
    w_n=1/[2(pi/2+2 pi n)^2].

Then v_n,w_n tend0 and

    W_1(0,v_n)=exp(-2 pi n)>0,
    W_2(0,w_n)-4w_n=-exp[-(pi/2+2 pi n)]<0.

An analytic function with zero Taylor series at0 is identically zero on some neighborhood. The displayed sequences contradict that property for each trace after subtracting its analytic linear part. Both traces are therefore nonanalytic at0.

## Scope and dependencies

Taking constant temperature M makes the thermal equation exact locally and makes both beta2 equations exact on the right half-rectangle, where Omega=-curl W=0. No full-neighborhood vorticity equation is asserted here. The same H and W are used in161 sections3-6, where the construction is embedded with the actual center jet and canonical whole-plane inverse and the vorticity residual is proved nonzero in every endpoint neighborhood. That global nonprofile supplies an additional application, not a premise of the local counterexample just proved.

The proof uses elementary complex differentiation, a smooth angular cutoff, the Cauchy-Riemann equations and analytic uniqueness. There is no claim of a bound uniform in derivative order, Gevrey regularity of arbitrary B2 fields, or failure of unique continuation for a B2 solution. The issue is exactly the extra analytic value-trace assumption in166.

Written UTC 2026-10-21T12:55:39.487209+00:00, before manufactured controls.
