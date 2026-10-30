# Candidate 017: independent audit of the two-endpoint dyadic exclusion

Written UTC 2026-10-29T15:03:57.980622+00:00 before the finite checker.

## Exact statement and numerical premises

Fix C1-N1-017-legqs50-quot013, raw SHA256
7dc30181e2d29c8c9706cf396a1be2334f53b2a19ca00e4fad756ff98ec59114,
c=4076476460239181/2251799813685248, gamma=1/c, delta=1-gamma,
S=1+r^2, t=r^2/S, v=1/S. Its exact rational generators define chi;
rho=-partial_y Delta chi, u=(-chi_xyy,chi_xxy), V=cX+u and
F=V.grad rho-rho. Pi_n is the full-circle sine projection with
coefficient normalization 1/pi. Put

 J(a)^2=sum_(n=1,3) int_R2 S^(2-a)|Delta Pi_n F|^2 dX.

Orthogonality gives J(a)<=||S^((2-a)/2)Delta F||2, even if the latter
is infinite. Every background mode contributing to the selected output
modes is retained in the N4 production. No upper norm is asserted.

The audited numerical premises are the complete N4-389 projected
energies at a=1/4,7/4, their exact differentiation and moment certificates,
and their agreement with two containing squared-norm displays from the
independent N3 construction. The present finite replay does not repeat
field differentiation or radial integration. Its original source hashes
are checked before freezing, and exact origin derivatives, endpoint
integrability, group sums and all cell bounds are independently replayed.

Under all assumptions below, this reference fails the sufficient closure
conditions of FW-T-DYADIC-Y-v1 for every 0<a<2, 0<s<1 and fixed finite
Rw>0. All seven ratios exceed 1221854480167/10^12=1.221854480167.
The smallest is on [1/4,1/2]. This is a conditional scheme obstruction,
not nonexistence of a stationary profile or existence closure.

## The norm, operator and assumptions retained

All functions are real S1, even in x and odd in y. Put q=2+s and
w=(1+r^2/Rw^2)^(-a/2). Fix the smooth radial cutoffs of the framework:
chi0=1 for r<=2, supported in r<4, and chi=1 on 1<=r<=2, supported
in 1/2<r<4, both valued in [0,1]. Use unitary Fourier normalization.
The norm is

 Y(h)^2=||w h||2^2+||chi0 h||Hq^2+||chi0 U[h]||Hq^2
   +sum_(j>=1)2^(2(1-a)j)(||chi(.)h(2^j .)||Hq^2
                            +||chi(.)U[h](2^j .)||Hq^2),       (3)

where U=(-R1R2,R1^2) is the canonical weighted extension; the velocity
is not a free unknown. Vector norms sum component squares. Retain a
valid weighted bound ||w U[h]||2<=C_U||w h||2. Necessarily C_U>=1,
as localized high-frequency S1 packets with nearly horizontal frequency
make the Euclidean symbol norm approach one in a fixed weight region.

Let L=V.grad-1+U[.].grad rho have the injective maximal distributional
low realization in L2(w^2 dX). Assume its core energy inequality has
rate beta>0 and all graph, completeness and bounded-coupling hypotheses
needed for that realization. Assume V is globally Lipschitz, u is
sublinear, and grad rho is bounded. For some integer m>q, assume
D^k V is bounded for 1<=k<=m+2 and D^k grad rho for 0<=k<=m+1.
The finite reference generators supply these coefficient regularities.
The positive low rate and high inverse remain scheme hypotheses.

Assume the normalized origin identities

 V(0)=0, DV(0)=diag(2c-1,1), grad rho(0)=(0,a0),
 chi_xxyy(0)=1-c, 1<c<2, a0>=5c-4.                         (4)

The inverse hypothesis is the actual one: for every k with Y(k)<=R
and c[k]=partial_y U2[k](0)=0, and every f in Y with f_y(0)=0,
the low inverse of A_k=L+U[k].grad exists in Y and

 Y(A_k^(-1)f)<=M Y(f).

It includes k=0. The canonical strain c[k] retains its local/contact
term -k_y(0)/4. No output projection onto ker c is substituted. The
closure inequalities used here are

 M Y(F)<=R,
 C_U C1 R < beta-a C1 R, C1=[4 pi s(1+s)]^(-1/2).             (5)

The further slope condition C1 R<a0 can only restrict the scheme more.
All fixed partition, weighted-velocity and absorption assumptions of
the frozen framework remain in force.

## Analytic necessary inequality and complete cells

The accepted origin inverse theorem, whose proof and Opus review are
frozen, applies to (3)-(4) on the actual input hyperplane. It requires
0<s<c-1 and M>=1/(c-1-s). Its localized approximate eigenvectors have
strain removed with a vanishing correction; the forcing derivative is
then exactly zero. No high inverse is proved by a low energy estimate.
The accepted far-field energy packets give beta<=1+c-ca.

Combining these with (5) and C_U>=1 gives

 Y(F)<H(c-1)(1+c-ca)/(1+a), 0<a<1+1/c,
 H(d)=max_(0<s<d)(d-s)sqrt(4 pi s(1+s)).                     (6)

The strictness comes from the contraction inequality in (5). The
maximum is explicit: the derivative of (d-s)^2 s(1+s) is
(d-s)[d+(2d-3)s-4s^2]. Its unique positive critical point is

 s*=(2d-3+sqrt((2d-3)^2+16d))/8, 0<s*<d.                    (7)

Both endpoints have value zero. Directed evaluation of (7) encloses
H(d); no sampled maximization is used.

The norm (3) also gives Y(F)>=5^((a-2)/2) J(a). To verify the constant,
on r<=2 the weight (1+r^2)^(2-a) is at most 5^(2-a), and the core
Hq term controls the L2 Laplacian on its plateau. On each disjoint
2^j<=r<=2^(j+1), j>=1, the shell Hq term controls
2^(2(2-a)j) times the physical Laplacian energy. The physical weight
is at most 5^(2-a)2^(2(2-a)j) there. Sum the disjoint regions, then use
angular orthogonality. Cutoff derivative terms vanish on the relevant
plateaux. This comparison is independent of the low weight scale Rw.

J(a) decreases in a, since the weight in its nonnegative integral
decreases. Put A=1+1/c. The right-side fraction b(a)=(1+c-ca)/(1+a)
has derivative -(1+2c)/(1+a)^2<0. For a in a cell [l,h] and any
e>=h, the left side of the necessary inequality is at least
5^((l-2)/2)J(e), and its right side is at most H(c-1)b(l). Hence

 5^((l-2)/2)J(e) / [H(c-1)b(l)] > 1                         (8)

excludes the complete cell. Use [0,1/4],...,[5/4,3/2],[3/2,A],
with e=1/4 on the first cell and e=7/4 on every remaining cell. This covers [0,A].
For A<=a<2 the required beta>0 already fails its far-field bound.
Values of s outside (0,c-1) fail the inverse requirement. Thus no
unexamined open cell, s endpoint or finite Rw remains in the claim.


## Independent exact origin reconstruction

Write H_m=Re(x+iy)^(2m), p_j=(3+gamma-j delta)/2. A raw generator is

 b H_m S^(p_j-m) t_R^w v_R^q P_N(2t_R-1),
 t_R=r^2/(R^2+r^2), v_R=R^2/(R^2+r^2),

with P_N(1)=1. For a mono generator take N=q=0,R=1; for leg take
q=0,R=1; for legq take R=1. The legqs generator supplies R explicitly.
All indices are nonnegative integers and R>0. The finite identity

 P_N(2t_R-1)=sum_(k=0)^N (-1)^(N+k) binom(N,k)binom(N+k,k)t_R^k

shows that only m+w+k<=2 contribute to the quartic jet. For
n=2-m-w-k and d=w+q+k, their scalar coefficient multiplying
H_m(r^2)^(2-m) is

 b (-1)^(N+k)binom(N,k)binom(N+k,k) R^(-2(w+k))
   *sum_(i=0)^n binom(p_j-m,i)binom(-d,n-i)R^(-2(n-i)).

This follows by multiplying the two Taylor series at r^2=0; it uses
only finitely many exact rational operations. Let B_m be these summed
coefficients for m=0,1,2. Then the x^2y^2 coefficient is
A22=2B0-6B2, the y^4 coefficient is A04=B0-B1+B2, and
chi_xxyy(0)=4A22, a0=-4A22-24A04. The independent reconstruction
checks c+4A22=1 and a0>=5c-4. S1 parity and smoothness give V(0)=0
and grad rho(0)=(0,a0); the velocity derivatives then give
DV(0)=diag(2c-1,1). No distant residual sample establishes these jets.

## Endpoint and complete energy checks

The accepted rational projection has
Pi_n F=r sum_ell v^(ell delta/2)P_(ell,n)(t)sin(n theta), where the
rational denominator is a product of (1+b v)^k with b in
{99,624,2499,9999}. For017 only b=2499 occurs. All denominators are
positive on [0,1]. Define T_zP=(1-2zt)P+2t(1-t)P'. Direct radial
and angular differentiation gives

 Delta[r v^z P(t)sin(n theta)]=r v^(z+1)L(t)sin(n theta),
 tL=T_z(T_zP)-n^2P.

The accepted exact Cartesian trace and mixed derivative identities
check this expression, including denominator derivatives. Writing
L(1-v)=v^qell Qell(v)/Dell(v), the complete projected energy is

 (pi/2)sum_(ell,k) int_0^1
 v^(a+(ell+k)delta/2+qell+qk-3)(1-v)Qell(v)Qk(v)/(Dell Dk) dv.

The factor pi/2 follows from the angular integral pi and the radial
change of variables. All 16 diagonal margins ell delta+2qell-2 are
positive; their pairwise averages prove every exponent is greater
than -1 at a=0 and hence at both positive weights. All136 unordered
pairs, with factor2 off the diagonal, produce51 distinct exponents.
The finite audit independently reconstructs that exponent set, verifies
every group label and re-sums the saved group integral balls before
multiplication by pi/2. Decimal display rounding may widen this sum;
interval agreement with the saved energy is required, not false exact
equality. The printed group records do not reproduce the unprinted
internal 2048-bit enclosures.

The production's partial fractions reconstruct exactly and its
positive-pole moment algorithm is a retained, separately audited
dependency. The current replay records these source-bound assertions
and checks their complete counts; it does not independently reconstruct
large partial-fraction numerators from hash strings. The007 calibration
contains all six exact field comparisons and both prior energy matches
for each selected mode; it is additional evidence, not a substitute for
the017 calculation and its independent N3 comparison.

Only the N3 cells ending at1/4 and7/4 are compared as containing squared
norm displays. The five unused endpoint energies and N3 internal
1024-bit endpoint strings are outside this acceptance. All seven new
cells instead follow from the two selected norms and monotonicity as
proved above. No L2-distance lower bound enters this deduction.

## Evidence and acceptance boundary

The manifest freezes the two complete production proofs, source code
for inspection, all four mode records, wrapper start/result, acceptance
manifest, two N3 source files, prior007 energy records, the raw017 JSON
compressed without alteration, origin comparison fields, and the exact
framework/origin theorem with its retained Opus reviews. The external
47-source hash observation is dated and binds the original production;
it establishes file identity at the observation time, not an inference
about historical execution. Only own checker code is executed.

The checker must pass before these numerical conclusions are accepted.
The high inverse, low realization, input hyperplane, canonical velocity,
fixed partition, plateau and absorption assumptions remain explicit.
No independent numerical inverse or full residual upper bound is supplied.
