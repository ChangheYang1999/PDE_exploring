# Local velocity of exactly strain-compensated exterior corrections

Status: complete informal proof before the new scalar computation.
No stationary-profile endpoint or exclusion neighborhood is claimed.

## 1. Definitions and statement

Use exactly the topic105 single-tail construction, with all its mandatory
addenda. Its exponent is beta=2k-1, k=1615536043799051/9007199254740992.
Its angular density is H(theta)=cos^2(theta)sin(theta)Q(cos2theta), where
||Q||infinity < N=38.37961982 is the already verified strict upper bound.
Let h_T=rho_T-rho0 and u_T=U[h_T]. The canonical strain of h_T is exactly
zero and h_T vanishes for r<=T. Throughout T>=max(R_b,L,1).

For j=0,1,2,3 put

 S_j=sum_(m=0)^infinity (2m+3)_j 4^(-m),
 C_j=4 N S_j/(3-beta),                                      (1)

where (v)_j=v(v-1)...(v-j+1) and (v)_0=1. For any R>0 with 2R<=T,
any Cartesian multiindex alpha of length j and i=1,2, we claim

 sup_(|X|<=R) |partial^alpha (u_T)_i(X)|
 <= C_j R^(3-j) T^(beta-3).                                 (2)

These are individual component/derivative bounds, not Frobenius norms.
The geometric sums are exact rational numbers and will be checked by
two separate methods. Their first two are S0=4/3 and S1=44/9.

A proposed numerical specialization to be verified below is

 R=9, T>=3000: |(u_T)_1(P)|<1e-8,
                  |partial_y (u_T)_2(P)|<1e-8,               (3)

where P=(p,0) is the existing exactly defined trial source and p<9.
The exact R_b is greater than3000, to be checked independently again,
so every admissible topic105 cutoff satisfies this specialization.
Using the existing topic76 source-jet certificate, (3) implies

 |partial_y F(rho_T,c0)(P)| > 3.69e-7.                       (4)

This asserts that every member of this explicitly specified family has
a local nonzero defect. It excludes no surrounding neighborhood and
does not address the existence of a nearby corrected stationary profile.

For the topic106 higher-tail construction, the analogous component
bounds with finite unevaluated constants imply u_T ->0 in C^3 on every
fixed compact set, with rate O(T^(beta-3)). Its residual converges to
the original residual in C^2 on each fixed compact set. No numerical
source bound for that higher-tail family is claimed here.

## 2. Canonical interior harmonic coefficients

For a finite angular density q(r,theta)=sum_(j>=0)D_j(r)
sin((2j+1)theta), direct Cartesian differentiation gives the coefficient
of sin(2n theta) in partial_x q as

 f_n=(D'_(n-1)+D'_n)/2
       -((2n-1)D_(n-1)-(2n+1)D_n)/(2r).                     (5)

Suppose q vanishes on r<=1 and grows as r^a with a<1, with the finite
smooth cutoff and differentiated tails used here. The canonical Green
formula on r<1 gives

 psi_n(r)=r^(2n)/(4n) integral_1^infinity s^(1-2n)f_n(s)ds.

Integrating the derivatives in(5) by parts produces no endpoint terms:
D_j vanishes at1 and s^(1-2n)D_j(s) tends to0 at infinity, since
1-2n+a<0. The D_(n-1) terms cancel and the D_n terms add to2n. Hence

 psi_n(r)=(r^(2n)/2) integral_1^infinity s^(-2n)D_n(s)ds.    (6)

This uses the canonical full-plane Green formula. No arbitrary harmonic
polynomial is inserted. The finite harmonics are analytic on the whole
interior disc. By continuity the resulting estimates apply on closed
subdiscs.

Write H(theta)=sum h_j sin((2j+1)theta). For the unscaled tail
q=chi(r)r^a H(theta), the integral in(6) is h_n J_(a,n), where

 J_(a,n)=integral_1^infinity chi(s)s^(a-2n)ds,
 0<J_(a,n)<=1/(2n-a-1).                                    (7)

The compact compensator is a multiple of r^3 cos^2(theta)sin(theta)b(r).
Since cos^2(theta)sin(theta)=(sin(theta)+sin3theta)/4, it has only
D0,D1. Therefore it changes only n=1 in(6). Its exact strain
compensation cancels that entire n=1 quadratic harmonic. Every remaining
interior stream term is

 (h_n J_(a,n)/2) Im (x+i y)^(2n), n>=2.                     (8)

The corresponding velocity is

 (-n h_n J_(a,n) Re (x+i y)^(2n-1),
   n h_n J_(a,n) Im (x+i y)^(2n-1)).                        (9)

All sums are finite. This explicitly verifies the cubic first possible
velocity order after strain compensation, including its sign and index.

## 3. Scaling and derivative estimates

For the T-scaled density, (6) gains the factor T^(a-2n+1), by the
substitution s=Tz. Equivalently the velocity is T^a times the unscaled
velocity at X/T. This scaling is canonical: the whole-plane Green
integrals transform with that factor and no homogeneous affine gauge
is changed. It is also consistent with the exactly scaled compensator.

For every multiindex alpha of length j, differentiating z^m gives
partial^alpha z^m=i^(alpha_y)(m)_j z^(m-j). Applying this to(9), then
using(7), yields

 |partial^alpha (u_T)_i(X)|
 <= sum_(n>=2) [n |h_n| (2n-1)_j/(2n-a-1)]
                 T^(a-2n+1) R^(2n-1-j), |X|<=R.

For 2R<=T, this is at most R^(3-j)T^(a-3) times

 K_j(a,H)=sum_(n>=2) [n |h_n| (2n-1)_j/(2n-a-1)]4^(2-n).    (10)

The absence of n=1 is essential. No claim that a T-scaling exponent by
itself controls spatial growth is used.

For the single-tail case, a=beta lies in(-1,1). Its Fourier coefficients
satisfy |h_n|<=2||H||infinity<2N, since |cos^2 theta sin theta|<=1.
For n>=2, n/(2n-beta-1)<=2/(3-beta), equivalent to
(beta+1)(n-2)>=0. Extend the positive finite sum in(10) to infinity and
put m=n-2. This gives K_j<=C_j and proves(2).

For topic106 there are three fixed finite angular functions and
exponents beta,3k-2,k-2, all below1. Apply(10) separately to each
strain-compensated term and add. Each K_j is finite, and beta is the
largest exponent, so the C^3 local rate is O(T^(beta-3)) for T>=1.
All corrections vanish in any fixed compact set once T is large. On
that set the residual difference is exactly u_T.grad rho0. The base
density is C6 locally, so Leibniz differentiation gives convergence in
C2 there. The unchanged scaling coefficient is c0=1/k.

## 4. Certified source consequence for the single-tail family

The topic76 source identity, with the exact base source P, states that
for h preserving normalization, writing z=h_y(P),v=h_xy(P),u=U[h]_1(P)
and w=partial_y U[h]_2(P), the derivative change is

 (mu-1)z+g w+g' u+w z+u v,

because sigma[h]=0 here. For every admissible T, p<R_b<=T, so z=v=0.
The prior certificate gives D=|(mu-1)g|>6.70197e-7 and
|mu-1|+|g|+|g'|<30.0230. Once(3) is verified, the triangle inequality
in particular gives

 |partial_y F(rho_T,c0)(P)|
 > 6.70197e-7 - 30.0230*1e-8 - 2*(1e-8)^2 > 3.69e-7.       (11)

The quadratic term is zero for this family, but retaining it makes the
use of the prior four-jet inequality direct and conservative. P need
not be a source of the repaired velocity to use this fixed-point jet
identity. The density and velocity are sufficiently regular there.

## 5. Verification and scope

Before accepting the numerical specialization, two interval methods
must separately enclose all C_j, R^3 C0 3000^(beta-3),
R^2 C1 3000^(beta-3), and R_b. One derives the geometric sums by rational
generating functions and uses Arb512. The other sums a positive finite
series with a proved geometric-polynomial tail and uses mpmath.iv180.
The powers, constants and the strict final rational margin must all
have outward endpoint checks. Exact symbolic differentiation checks the
coefficient and sign formulas. Recheck the complete topic76,105,106
pin maps and the original exact k and tplus. The numeric assertions
stay conditional until those computations and review pass.

This is constructive local control of an explicit nonstationary trial
family. The family can be changed further, and its unchanged source
residual is not a nonexistence theorem in any meaningful neighborhood.
No full-flow certificate, linear inverse or closing inequality follows.
