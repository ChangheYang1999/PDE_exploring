# Quantitative motion and data of the source under a perturbation

## Statement, notation, and dependencies

The canonical IPM law is -Delta psi = partial_x rho,
U[rho]=(-partial_y psi,partial_x psi), with the sublinear canonical
inverse. Write sigma[rho]=partial_xy psi(0), c_l=(1+sigma[rho])/3 and
V[rho]=c_l X+U[rho]. These are the physical signs checked in topic80.
Let rho0 be the exact normalized modal_v2 trial, k its exact parameter,
V0=V[rho0], w(x)=V0_1(x,0), mu0(x)=partial_y V0_2(x,0),
G(x)=partial_y rho0(x,0). Let P=(p,0) be its source from topics17 and89.
The narrow source bracket in modal_source is contained in the bracket in89;
both are zeros of the identical canonical trial, so uniqueness from89
identifies their sources. The checker repeats this exact interval inclusion.

Use the independently audited high precision source data of modal_source,
not a floating evaluation at the midpoint of the wider bracket:

 |mu0(p)-1+2.2528046115e-8| < 4.7e-19,
 |G(p)-29.7494906633335090153| < 9.2e-20,
 A0=w'(p)=2/k-mu0(p) in [10.150725243,10.150725244].

Topics84,85 prove on the entire source disc B_R0(P), R0=99/2000,
||D^2 V0||_F < MV=743/2500 and ||D^2 rho0||_F < Mrho=5059/10000.
The trial is at least C6 on this disc, including its spline interfaces;
C-infinity is unnecessary and is not asserted. The checker verifies all
imported frozen hashes and exact interval consequences. These data are
explicit dependencies, not new whole-integral computations here.

Let h be even in x and odd in y. Assume the canonical linear quantities
U[h] and sigma[h] exist, and impose the stated local regularity whenever
its derivatives are used. Set W=U[h]+sigma[h]X/3. Then V[rho0+h]=V0+W.
No stationarity is assumed unless explicitly stated below.

## Source motion

For 0<R<R0 put I=[p-R,p+R], m=A0-MV R, and

 e0=sup_I|W1(x,0)|, e1=sup_I|partial_x W1(x,0)|,
 e2=sup_I|partial_y W2(x,0)|, e3=sup_I|partial_y h(x,0)|.

Terms involving derivatives require that these derivatives exist with
appropriate continuity, or the equivalent Lipschitz bounds used below.
If W1 is continuous and e0<mR, there is a zero p_h of
V[rho0+h]_1 on the interior of I. Every zero there satisfies
|p_h-p|<=e0/m. If W1 is C1 on I and e1<m, this zero is unique in I.
For every such R, m>10.1360138 and 1/m<0.09866.

Proof. The Hessian bound and the fundamental theorem of calculus give
|w'(x)-A0|<=MV|x-p|, hence w'>=m>0 and
|w(x)|>=m|x-p|. At p-R the perturbed function is negative, and at p+R
it is positive. Continuity gives a zero; evaluating w=-W1 there gives
the distance bound. Under the derivative assumption, w'+W1'>=m-e1>0,
which proves uniqueness.

With d=|p_h-p| the first-order formula is

 p_h-p=-W1(p,0)/abar,
 abar=int_0^1 (w'+partial_x W1)(p+t(p_h-p),0) dt,
 |abar-A0|<=MV d/2+e1,
 |p_h-p+W1(p,0)/A0|
 <= |W1(p,0)|(MV d/2+e1)/[A0(A0-MV d/2-e1)].

The fundamental theorem proves the formula, including the case p_h=p.
Its denominator is positive: e1<m=A0-MV R and d<=R imply
A0-MV d/2-e1>MV(R-d/2)>=0. If MV=0, e1<A0 gives positivity directly.
The error follows by subtracting the reciprocals of abar and A0.

## Parity, divergence, and data at the moved point

The canonical stream function is odd in x and odd in y, by the radial
inverse and the parity of partial_x rho. Thus U1 is odd in x and even in
y, while U2 is even in x and odd in y. On the x-axis V2=partial_x V2=
partial_y V1=rho=partial_x rho=0, wherever these derivatives exist.
Since div U=0, div V=2/k+2sigma[h]/3. Therefore at P_h=(p_h,0),

 V(P_h)=0, DV(P_h)=diag(A_h,mu_h),
 A_h+mu_h=2/k+2sigma[h]/3,
 grad(rho0+h)(P_h)=(0,g_h), g_h=G(p_h)+h_y(p_h,0).

The Hessian bounds and segment integration give

 |mu_h-mu0(p)|<=MV d+e2,
 |g_h-G(p)|<=Mrho d+e3.

Consequently all three source data lie in
[10,51/5] x [99/100,101/100] x [29,30] if

 MV e0/m+e2<=.0099999,
 (2/3)|sigma[h]|+MV e0/m+e2<=.0492747,
 Mrho e0/m+e3<=.2505.

The checker proves the numerical margins directly from the exact frozen
source intervals. In particular the safe symmetric mu margin is
.01-2.2528046115e-8-4.7e-19. The lead's displayed
.01-2.2528046e-8 is slightly larger and is not a justified symmetric
margin. This correction does not change the sufficient ceiling .0099999.
The source box says nothing about the required coefficient norms or a
global inverse.

## An obstruction following the perturbed source

Assume rho=rho0+h is C1 near P_h, V is differentiable there, rho is an
exact stationary solution near P_h, and g_h is nonzero. Then mu_h=1.
Indeed rho(P_h)=0 and V(P_h)=0. Along P_h+t e2, differentiability and
continuity of grad rho give

 V.grad rho=t mu_h g_h+o(t), rho=t g_h+o(t).

The stationary identity implies (mu_h-1)g_h=0. No C2 hypothesis is needed.
It follows that e2+MV e0/m >= 1-mu0(p)>2.2528046e-8. Hence no exact
solution satisfying the hypotheses has e0,e2<=2.1886e-8, provided the
source-existence condition e0<mR also holds. Indeed the checker proves,
using only m>10.1360138,

 2.1886e-8 (1+MV/m) < 2.2528046e-8-4.7e-19.

The sufficient assumption e3<=29 guarantees g_h is nonzero:
|g_h-G(p)|<=29+Mrho R0<G(p). The last inequality is checked exactly.
This is a narrow velocity-distance obstruction about the modal trial.
It gives no useful numerical uncertainty ball about X3 and is not a
nonexistence endpoint.

## Velocity estimates from Sobolev and tail norms

Use the unitary two-dimensional Fourier convention with inverse factor
(2pi)^(-1), and ||v||_Hr^2=int <xi>^(2r)|vhat|^2 dxi.
Fourier inversion and Cauchy-Schwarz give, for r>1 and r>2 respectively,

 ||v||_infty<=alpha_r||v||_Hr,
 ||grad v||_infty<=beta_r||v||_Hr,
 alpha_r=1/[2sqrt(pi(r-1))],
 beta_r=1/[2sqrt(pi(r-1)(r-2))].

To prove the gradient assertion directly, apply Cauchy-Schwarz to the
vector integral, bounding its Euclidean length by the integral of
|xi||vhat|. Polar integration with u=|xi|^2 gives
int(1+|xi|^2)^(-r) dxi=pi/(r-1) and
int|xi|^2(1+|xi|^2)^(-r) dxi=pi/[(r-1)(r-2)].
The component symbols of U are xi1 xi2/|xi|^2 and -xi1^2/|xi|^2;
both have modulus at most one. In fact the sum of their squared moduli
is xi1^2/|xi|^2<=1. Therefore each component, or the whole vector in
its vector Sobolev norm, is bounded by ||v||_Hr.

Use the cutoffs and weighted tail norm N of topic77 at delta=33/2000.
Precisely, zeta=1 on B_(5delta/2)(P), supported in B_(3delta)(P),
N=int_(|X-P|>=5delta/2)|h|/|X-P|^2
 +int_(R2 outside B_(3delta)(P))|h|/|X|^3.
The proven off-diagonal bound on B_(9delta/4)(P) is
|D^j U_i[(1-zeta)h]|<=k_j N,
k_j=100(j+1)!/(2pi)(4/delta)^j.
The physical strain bound, with h(0)=grad h(0)=0, is
|sigma[h]|<=Cc Hh+N/pi,
Cc=3delta/[sqrt(pi)(p-3delta)^3],
Hh=||h||_(H^(r-1)(B_(3delta)(P))).
These are imported proved inequalities, with the same cutoff and domain
hypotheses as77 and corrected physical sign as80.

For R<=9delta/4, the near and far split of U and the embeddings give

 e0<=alpha_r||zeta h||_Hr+k0 N+(p+R)|sigma[h]|/3,
 e1,e2<=beta_r||zeta h||_Hr+k1 N+|sigma[h]|/3,
 e3<=beta_r||zeta h||_Hr.

The last equality uses zeta=1 on a neighbourhood of I. At r=31/10,
alpha_r<.194664 and beta_r<.185605, proved by two directed engines.
All tail quantities must be finite. These formulas are conditional norm
estimates and do not evaluate the perturbation norms of X3 minus rho0.

## Local source estimate for the transported linear family

Consider A_h u=(V0+W[h]).grad u-u+W[u].grad rho0. Its background density
is rho0, so the relevant transverse gradient is G(p_h), without h_y.
Assume the source-existence and uniqueness hypotheses above and the first
two source-box inequalities, plus Mrho e0/m<=.2505. Assume W[h] is C4 on
B_R0(P) and ||D^2 W[h]||_F<=m2 there. Put
d_h=|p_h-p|<R0 and delta_h=(R0-d_h)/3. For 0<delta'<=delta_h the open
ball B_(3delta')(P_h) lies in B_R0(P), and

 MV'<=MV+m2, Mrho'<=Mrho,
 E<=[41.7(MV+m2)+3Mrho]delta'.

Parity and the preceding box bounds give all source data hypotheses of
77. The trial's C6 regularity gives the required C5 background and C4
velocity; W[h] provides the remaining regularity. Also delta'<=1 and
3delta'<p_h/2 because p_h>p-R0>8.55 while 3delta'<=R0. Divergence of the
new velocity is still constant, so the same divergence cancellation in
the cutoff error applies. The source estimate therefore holds when E<
kappa=1687/500, with K1=1/(kappa-E). This is its local forcing coefficient.
At delta'<=33/2000 the exact checker tests the proposed ceilings for m2=1
and2, and gives the exact m2 threshold for positivity at the largest delta.

For r>3 the same Fourier argument applied to the complete Hessian tensor
of U[v] gives

 sup||D^2 U[v]||_F<=gamma_r||v||_Hr,
 gamma_r=1/sqrt(2pi(r-1)(r-2)(r-3)).

Indeed the squared symbol sum is |xi|^4 sum_i|sigma_i|^2<=|xi|^4,
and polar integration gives
int|xi|^4(1+|xi|^2)^(-r) dxi=2pi/[(r-1)(r-2)(r-3)].
This bounds only a near part where a suitable global cutoff is inserted.
Topic77's far bound on B_(9delta/4)(P) does not cover all B_R0(P);
a separate cutoff and tail estimate are needed there. The uniform
K2,K3,K4 coefficients, auxiliary inverse, strain denominator, outer
matching, full inverse and nonlinear contraction remain OPEN.

This standalone proof was written before the checker.
