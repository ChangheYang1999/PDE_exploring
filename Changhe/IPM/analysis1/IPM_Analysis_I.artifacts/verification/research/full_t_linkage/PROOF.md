# Membership of every finite-annulus spline Taylor coefficient

Status at creation: OPEN, proof and acceptance criterion only. No full
computation has run. This proof was written before its checker.

The exact trial is defined by data_exact/modal_v2.json, SHA256
57f67a53c1ee5c8fd5ede8480428f1a5584123ac4e54b6d3530d091ea2a67ca6.
On the spline annulus it has

 rho = r^3 cos(theta)^2 sin(theta) sum_(m=0)^259 a_m(t) cos(2m theta),
 t = log r, a_m(t) = sum_i S_(m,i) N_(i,7)(t).

Every stored hexadecimal float in S and the knots is an exact dyadic
rational. N denotes the degree-seven B-spline defined by the recurrence
below. The normalization repair changes the exterior leading coefficient
and exterior joining corrections; it does not change these spline data.
The proposed comparison target is the fixed numerical file
../ipmA-num/data/cert_green.npz, SHA256
c2c2e4f73f5ac6ee49fd0052b81700fc88ee68d01a5a526691cf03c2b82c2ef1.
The arrays T_mid,T_rad have dimensions (7809,8,260). Their intended exact
values are coefficients, not derivatives: for each cell with left endpoint
c, a_m(c+u) = sum_(j=0)^7 T_(cell,j,m) u^j on that cell.

The accepted canonical archive is
research/middle_residual/evidence/original_knots.jsonl.gz, SHA256
c762afdbea381b750f2c9e382ef2315b2652df9781ccf69511237d944e102648.
For each of 1558 original nonempty knot spans [a,b], it provides enclosing
balls for the coefficients of H_j(t), j=0,...,261, in powers of
x=t-(a+b)/2. It also provides the exact equal subdivision count and first
cell index. H_261 is exactly zero. The archive's accepted canonical moment
integration is an explicit dependency of method A, not recomputed here.

## Exact statement and acceptance hypotheses

Assume the named source hashes, finite float64 target arrays with
nonnegative radii, the stated array dimensions, and complete ordered
coverage of the exact nonempty knot spans. Parent indices must agree with
the archive. For each span with n children, the exact boundaries are
c_q=a+(b-a)q/n, q=0,...,n. Every c_q must belong to the corresponding
exported tb plus or minus tb_rad interval. No floating parent assignment,
rounded child width or approximate equality is used.

The following checks, if all completed, imply that every true spline
Taylor coefficient belongs to its exported T interval:

1. Reconstruct it by method A below with outward Arb balls; require that
   whole resulting ball to be contained in the target dyadic interval.
2. Reconstruct it independently by method B below with exact rational
   arithmetic; require the exact rational to belong to the target.
3. Require the exact result of method B to belong to method A's ball.
4. Reconstruct every original-span H polynomial from the exact method B
   polynomial by the forward angular identity; require every coefficient
   to belong to its original archive ball.

A completed run must cover all 7809*8*260 = 16,242,720 Taylor coefficients,
with no omitted zero or high modes, and all 1558*262*8 = 3,265,568 archive
H coefficients. These checks do not prove the remaining radial ODE
models or any flow inequality. They do not prove a global IPM inverse or
an a posteriori endpoint. They concern the normalized modal trial, not
the original X3 coefficients, and do not modify the trial.

## Angular identity and a stable collected inverse

The trigonometric product identity

 cos(theta)^2 sin(theta) cos(2m theta)
 = [sin((1+2m)theta)+sin((1-2m)theta)
    +sin((3+2m)theta)+sin((3-2m)theta)]/8

follows by two applications of 2sin(A)cos(B)=sin(A+B)+sin(A-B).
After collecting signed odd frequencies it gives

 H_0 = a_0/4 - a_2/8,
 H_1 = (2a_0+a_1-a_2-a_3)/8,
 H_j = (a_(j-1)+a_j-a_(j+1)-a_(j+2))/8, j>=2,

where a_m=0 outside 0<=m<=259. Thus H_260=a_259/8 and H_261=0.
Starting with the top mode, these triangular equations uniquely recover
all a_m, m>=1. The generating series inverse of
1+z-z^2-z^3=(1-z)(1+z)^2 has coefficients
c_l=(-1)^l(floor(l/2)+1). Indeed multiplication by the polynomial gives
constant coefficient 1 and zero at every positive degree, either by the
displayed factorization or by checking the two parities. Consequently

 a_m = 8 sum_(j=m+1)^260 c_(j-m-1) H_j, 1<=m<=259,
 a_0 = 4H_0 + a_2/2.

This identity is polynomial in the inputs and holds separately for each
power of t. To avoid repeated interval dependency in triangular
substitution, collect repeated H terms first. Let S_p=sum H_j and
R_p=sum j H_j over j>m having parity p. Then

 a_m = 4 [R_opposite - (m-1) S_opposite - R_same + m S_same].

To prove this formula, for j opposite to m the coefficient c equals
(j-m+1)/2, whereas for j with the same parity it equals -(j-m)/2.
The finite sums can be accumulated from high j downwards. Arb's outward
operations preserve inclusion of every exact H coefficient, hence every
reconstructed a coefficient. This inclusion does not require independent
errors in H. The unused H_1 relation is checked separately by the full
forward reconstruction in check 4 above.

If p_k are the recovered coefficients in x=t-(a+b)/2, expansion at c_q
has coefficient

 T_l = sum_(k=l)^7 binom(k,l) p_k [c_q-(a+b)/2]^(k-l).

This is the binomial theorem and gives method A. All shifts are exact
rationals converted with directed rounding. It has no truncation tail.

## Exact rational method B: values and interpolation

The defining scalar recurrence is

 N_(i,0)(t) = 1 if k_i <= t < k_(i+1), and 0 otherwise,
 N_(i,p)(t) = (t-k_i)/(k_(i+p)-k_i) N_(i,p-1)(t)
             +(k_(i+p+1)-t)/(k_(i+p+1)-k_(i+1)) N_(i+1,p-1)(t).

A summand with zero denominator is defined as zero. This is also the
convention at repeated clamped knots. For any nonempty span [a,b] and
strictly interior point t, exactly the active indices ell-7,...,ell
can contribute, where k_ell=a and k_(ell+1)=b. Induction in p proves both
this support assertion and that every N_(i,7) is a polynomial of degree
at most seven on the open span. Its continuous one-sided polynomial
extension covers both endpoints for the coefficient comparison.

Choose eight nodes z_i=(2i+1)/16, i=0,...,7, so t_i=a+(b-a)z_i is
strictly inside the span. Evaluate the eight active basis functions
exactly at these nodes by the defining scalar recurrence. An additional
exact de Boor evaluation is used as a computationally different check:
start with the eight coordinate vectors d_j, then for r=1,...,7 and
j=7,...,r replace

 d_j <- (1-alpha)d_(j-1) + alpha d_j,
 alpha=(t_i-k_(ell-7+j))/(k_(ell+1+j-r)-k_(ell-7+j)).

Its final vector is accepted only if all eight components equal those
from the defining scalar recurrence. Thus the proof does not assume an
unverified implementation of the de Boor identity. Actual nonzero
denominators and exact equality are checked at every node and span.
Apply the checked vector to the eight S coefficients for every mode.
All resulting values are exact rationals.

Let L_i(z)=product_(j!=i)(z-z_j)/(z_i-z_j). The polynomial
sum_i a_m(t_i)L_i(z) has degree at most seven and agrees with a_m(a+hz)
at the eight distinct nodes. The difference has eight roots and degree
at most seven, so is identically zero. This proves the interpolation
identity without a numerical condition-number or interpolation-error
assumption. If its exact coefficients are Z_k, then

 T_l = h^(-l) sum_(k=l)^7 binom(k,l) Z_k (q/n)^(k-l), h=b-a.

This second binomial expansion takes place entirely in exact rational
arithmetic, independently of all archive H balls and Arb operations.
Exact matrices may batch the finite sums; they do not change the
mathematics. Neither method imports the numerical producer's spline,
modal or interval routines.

To check every original H ball independently, first translate the exact
Z polynomial to x=t-(a+b)/2 using q/n=1/2 and the displayed formula.
Then apply the signed-frequency product identity directly to its exact
a_m coefficients. This gives check 4. It is a complete alternative
verification of the finite spline H polynomials, not of the archive's
I/J integration or exterior tails.

## Independent output audit and scope of execution evidence

Source review, exact manufactured cases, decoder faults and a limited
smoke test precede any full run. Save complete per-span counts, exact
worst margins with original endpoints, hashes of complete comparison
streams, predetermined sampled full records, source hashes and the
archive footer. Reject missing or duplicate spans, a truncated footer,
nonfinite endpoints, reversed intervals and a changed resume header.
A diagnostic partial run must remain labelled OPEN, never CONFIRMED.

A separate output auditor does not import the producing checker. It
verifies coverage and source pins and recomputes predetermined coefficient
records by exact Newton finite differences at different nodes. For the
eight nodes z_j=(j+1)/9, let v_j=a_m(a+hz_j), exactly evaluated from the
scalar basis definition. With x=9z-1, the interpolant is

 a_m(a+hz) = sum_(r=0)^7 Delta^r v_0 binom(x,r).

Here binom(x,r)=product_(i=0)^(r-1)(x-i)/r! and binom(x,0)=1.
At integer x=0,...,7 the forward-difference formula follows from the
binomial inversion identity; equality of degree-seven polynomials
follows from their values at eight nodes. Substituting
x=9q/n-1+9u/h and multiplying these linear factors gives independently
the requested coefficient at c_q+u. Require equality to the saved exact
result and membership in both its saved Arb enclosure and target box.
Additional complete-span replay includes the first span after any resume.

Saved counters and hashes do not prove omitted calculations. Acceptance
rests on the reviewed exact algorithms, their complete execution with
recorded provenance, full stream accounting, independent finite checks
and the separate output audit. A final verifier closure is required even
if every executable returns success. No final theorem is claimed in
this proof-first document before these obligations are discharged.
