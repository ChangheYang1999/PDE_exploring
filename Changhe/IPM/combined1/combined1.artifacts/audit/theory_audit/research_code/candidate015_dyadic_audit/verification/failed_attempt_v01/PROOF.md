# Candidate 015: independent audit of the conditional dyadic exclusion

Written at 2026-10-29T14:49:41.701710+00:00, before the finite checker.

## Exact quantities and conditional statement

Fix the immutable C1-N1-015-pairQ-quot013 potential chi at
c=4076476460239181/2251799813685248, gamma=1/c and delta=1-gamma.
The raw, canonical JSON and coefficient-serialization hashes are distinct
and recorded in data/parameters.json. Define rho=-partial_y Delta chi,
u=(-chi_xyy,chi_xxy), V=cX+u and F=V.grad rho-rho. Let Pi_n be the
complete full-circle sine projection onto sin(n theta), with the usual
coefficient normalization 1/pi. Lebesgue measure is dX on R2. Define

 J(a)^2=sum_(n=1,3) int_R2 (1+r^2)^(2-a)|Delta Pi_n F|^2 dX.       (1)

The independently constructed complete projection energies in N4-382,
and their exact N3 comparisons, are the numerical premises audited here.
All contributing background modes are retained for each selected output
mode. Orthogonality gives J(a)<=||(1+r^2)^((2-a)/2)Delta F||2. This is
a lower witness; omission of the other output modes prevents a full
upper-norm interpretation.

Under every assumption of the specified FW-T-DYADIC-Y-v1 framework,
its origin inverse theorem and the realization described below, the
candidate fails that scheme's sufficient closure conditions for every
0<a<2, 0<s<1 and fixed finite Rw>0. The finite part is strict: the
smallest of the seven certified cell ratios exceeds

 621461129537/500000000000 = 1.242922259074.                    (2)

This excludes simultaneous satisfaction of a particular scheme's
hypotheses and closure inequalities. It proves no nonexistence of exact
profiles and no obstruction in all possible weighted spaces.

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
with e=h on the first six and e=7/4 on the last. This covers [0,A].
For A<=a<2 the required beta>0 already fails its far-field bound.
Values of s outside (0,c-1) fail the inverse requirement. Thus no
unexamined open cell, s endpoint or finite Rw remains in the claim.

## Independent exact origin and endpoint checks

The canonical basis term is b H_m(X) r^(2k)(1+r^2)^(p_j-m-k),
p_j=(3+gamma-j delta)/2, H_m=Re(x+iy)^(2m). Its homogeneous
quartic contribution vanishes unless m+k<=2. In that case it is

 b binom(p_j-m-k,2-m-k) H_m(X)(r^2)^(2-m).

The coefficients of x^2 y^2 for m=0,1,2 are 2,0,-6; those of y^4
are 1,-1,1. Therefore four times the summed first coefficients is
chi_xxyy(0), and a0=-chi_xxyy(0)-24 times the summed second
coefficients. The checker recomputes both exactly from all 1922
canonical coefficients and compares the saved origin values.

The accepted projected field has the finite exact form
Pi_n F=r sum_ell v^(ell delta/2) P_(ell,n)(t) sin(n theta),
t=r^2/(1+r^2), v=1-t. For d=ell delta/2, radial differentiation uses
T_d P=(1-2dt)P+2t(1-t)P'. Then

 Delta[r v^d P(t) sin(n theta)]=r v^(d+1)L(t) sin(n theta),
 tL=T_d^2 P-n^2 P.

The accepted production checks zero remainder in division by t and
independent Cartesian Laplacian and mixed derivative identities.
If L(1-v)=v^qell Qell(v), each ordered radial cross term in its energy
has measure

 (pi/2) v^(a+(ell+k)delta/2+qell+qk-3)(1-v)Qell Qk dv.

The strict diagonal inequalities ell delta+2qell-2>0 at a=0 imply
all cross-term integrability by averaging. The finite checker checks
every stored diagonal endpoint order. The production, not this audit,
performed the complete exact differentiation and radial integrations.

## Finite evidence and limits

The checker recomputes the sorted nonzero reduced-rational coefficient
serialization and rejects duplicates. It distinguishes that hash from
the JSON file hash and binds both to the already accepted T4/N4
termwise canonical agreement. It reads exact N3 mode energies divided
by pi, verifies positivity and exact addition, and compares all 14
positive-weight energies and all seven sums with independently formed
N4 containing intervals. It checks every displayed endpoint, recomputes
(7)-(8), and proves all strict floors with outward arithmetic.

Large coefficient tables and energy rationals remain in compressed
exact JSON. Direct source hashes and decoded hashes are registered as
inputs. This is an independent finite arithmetic and theoretical audit,
not another field integration. The missing historical N3 cache and
unobservable historical import versions remain provenance limitations;
the independent N4 physical construction supplies the field link.
No peer program is executed. The initial N4 comparison of two different
serialization hashes failed before integration and was repaired in its
explicit version 2 supplement. That failure changes no accepted energy.

The present deduction uses no L2 correction-distance bound. In
particular T4-460 is not a premise for the dyadic exclusion. The
statement retains the entire specified scheme, origin inverse, domain,
range, input hyperplane and normalization assumptions, and proves no
stationary profile nonexistence or successful a posteriori closure.
