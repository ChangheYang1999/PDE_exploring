# Candidate017: conditional total acceptance and residual identity audit

## Statement, exact conventions and source hypotheses

Fix C1-N1-017-legqs50-quot013, raw SHA256
7dc30181e2d29c8c9706cf396a1be2334f53b2a19ca00e4fad756ff98ec59114,
with c=4076476460239181/2251799813685248 and delta=1-1/c.
On the real plane with Lebesgue measure use
rho=-partial_y Delta chi, U=(-chi_xyy,chi_xxy) and
F=(cX+U).grad rho-rho. These canonical derivatives include the local
velocity contribution. No substitute candidate or changed scale is used.
Let H(F) be the supremum of |int F phi| over smooth real compactly
supported phi with ||grad phi||2<=1. Set G0=||F||2, G1=||grad F||2,
P2=||(1+4r^2)^(2/5)D2F||2, with the full Euclidean Hessian norm, and
E2^2=P2^2+2^14 G1^2+2^18 G0^2+(20/21)2^18 H^2.

Assume C1, C2 and C3 of the frozen N4-413 proof. Explicitly:

* C1: the actual F is smooth and L2, with only the 160 odd sine modes
  n=1,3,...,319. Each actual q_n=pi int r^3 f_n(r)^2 dr lies in the
  frozen Hardy record's complete rF_n_sq ball.
* C2: at each of the sixteen distinct frequencies 1,3,...,31, the
  frozen dual trial is admissible in homogeneous H1, and its actual
  quotient |int F_n psi|/||grad psi||2 belongs to its complete LB ball.
  The separately chosen residual trial has actual gradient norm and
  ||r(F_n+Delta psi)||2 enclosed by grad_psi and residual_r_g. It is
  smooth, has gradient and r Delta psi in L2, and has smooth radial
  cutoff approximation in gradient norm.
* C3: the actual G0,G1,P2 belong between the lower endpoint of norm_lower
  and the upper endpoint of norm_upper in the frozen norm record,
  with exactly the definitions above.

Then the frozen finite interval data imply

  0.6144195987 < H017 < 0.6165956396,
  605.4068697 < E2017 < 605.9589546.

Using the previously accepted E2007>606.818151 also gives
E2007-E2017>0.8591964>0.8591. The source assumptions C1-C3 remain OPEN
here. This is a conditional norm comparison, not an existence theorem.
The algebraic and analytic residual identity in the queued N4 replay
is correct under the admissibility and integrability assumptions below.

## Complete argument for the conditional total

For a sine mode F_n=f_n(r)sin(n theta), the vector field
A_n=-r f_n(r)cos(n theta)e_theta/n has distributional divergence F_n
and squared L2 norm q_n/n^2. Angular integration proves the divergence
identity on annuli. The vector field has no radial flux, so no atom is
introduced at the origin. C1 supplies smoothness of F_n and finite q_n.
The weak divergence identity yields H(F_n)<=sqrt(q_n)/n.

The sine projections of a compact smooth test are compact and smooth:
they are rotation averages with smooth angular weights. Distinct
frequencies are orthogonal in the gradient inner product. For a finite
sine sum, angular projection and Cauchy-Schwarz therefore give
H(F)^2<=sum H(F_n)^2. Conversely, choose near-maximizing compact tests
for each frequency, project them to that sine frequency and combine
them with coefficients proportional to their pairings. Orthogonality
and passage to the supremum yield the reverse inequality. All modal
norms are finite by the Hardy bound; no infinite sum or density claim
outside the gradient completion is needed. Thus H(F)^2=sum H(F_n)^2.

For an admissible residual trial, write g_n=F_n+Delta psi_n. Integration
by parts gives H(Delta psi_n)<=||grad psi_n||2. Test against smooth
radial cutoffs of psi_n, whose gradients converge, to obtain equality.
The triangle inequality then gives

 H(F_n)<=||grad psi_n||2+||r g_n||2/n.

At each of the sixteen tested frequencies, choose the smaller of the
square of this upper bound and q_n/n^2. At all 144 other frequencies
use q_n/n^2. Sum their upper endpoints to obtain U2>=H(F)^2.
Let l_n be the nonnegative lower endpoint of the dual LB ball at each
of the sixteen frequencies. Then L2=sum l_n^2<=H(F)^2. The nine-beta
dual trial and the eight-beta residual trial at a single frequency are
alternative tests of that same frequency. Their contributions are not
added as if they were orthogonal modes.

Insert L2 and the component lower endpoints into the positive E2 square;
insert U2 and upper endpoints for the upper square. Exact rational
squaring verifies the stated coarse endpoints. The accepted007 lower
endpoint gives the displayed difference by exact subtraction. An overlap
between two representations is only a consistency check, not a proof
of C1-C3. In particular, the lower endpoint of an interval formed from
upper estimates is not used as a lower bound on the actual H.

The N4-413 revision correctly compares the recomputed U2 against the
square of the more conservative stored H_upper_new. Requiring that
stored upper endpoint to lie inside the primitive interval would be
unnecessary. The precise sufficient comparison is
U2 < stored_H_upper_new^2 < 0.6165956396^2.

## Independent residual identity and endpoint check

Fix an odd positive n. Write psi=u(r)sin(n theta) and y=log r. Suppose
u is a finite sum of exact real multiples of
r^3(1+r^2)^(-beta)(r^2/(1+r^2))^k, where beta>3/2,
k>=-1 is an integer and 3+2k-n is even and nonnegative. At the origin,
r^n sin(n theta) is a harmonic polynomial and the remaining factor is
smooth in r^2. At infinity u,u_y,u_yy=O(r^(3-2 beta_min)). This gives
grad psi,r Delta psi in L2. The squared cutoff gradient error is
O(R^(6-4 beta_min)), which tends to zero. The analogous radial powers
at zero are at least r^n. Consequently the boundary term u_y u vanishes
at both ends, as do the other integration-by-parts terms below.

Define d=||grad psi||2^2, p=int F_n psi and
Z=-u_r sin(n theta)e_r-u_yy cos(n theta)e_theta/(nr).
Put a=||Z||2^2, b=<A_n,Z> and Q=||rF_n||2^2. Assume Q finite and the
pairings absolutely convergent. Angular integration gives

 d=pi int (u_y^2+n^2u^2)dy,
 a=(pi/n^2) int (n^2u_y^2+u_yy^2)dy,
 p=pi int r f_n u dr,
 b=(pi/n^2) int r f_n u_yy dr.

Since r^2 Delta psi=(u_yy-n^2u)sin(n theta), integration by parts yields
||r Delta psi||2^2=n^2(a+d). Direct substitution yields
int r^2 F_n Delta psi=n^2(b-p). Therefore

 R^2=||r(F_n+Delta psi)||2^2=Q+2n^2(b-p)+n^2(a+d).

No sign of p or b is assumed. The forward and reverse triangle
inequalities, and the admissible dual test, give

 max(0,sqrt(d)-R/n,|p|/sqrt(d))<=H(F_n)<=sqrt(d)+R/n.

For distinct frequencies, testing the finite sum of cutoff trials with
coefficients p_n/d_n proves H(F)^2>=sum p_n^2/d_n whenever d_n>0.
This lower bound does not require a finite full Hardy sum; the pairings
and admissibility suffice, even if H(F) is infinite.

To check the radial formulas independently, put t=r^2/(1+r^2), v=1-t,
b=beta-1 and u=r sum_b v^b P_b(t). Then r d/dr acts on r v^b P as
r v^b D_bP, where D_bP=(1-2bt)P+2t(1-t)P'. Hence

 d/pi=(1/2)sum_(b,c) int_0^1 v^(b+c-2)
             ((D_bP_b)(D_cP_c)+n^2P_bP_c)dt,
 a/pi=(1/2)sum_(b,c) int_0^1 v^(b+c-2)
             ((D_bP_b)(D_cP_c)+(D_b^2P_b)(D_c^2P_c)/n^2)dt.

For f_n=r sum_ell v^(ell delta/2)A_ell(t), the p, b and Q formulas
in the queued proof follow respectively from r^3 dr=t dt/(2v^3)
and r^5 dr=t^2 dt/(2v^4). Equal exponents must be grouped before endpoint
orders are tested. Positive denominator factors and exact grouped orders
are hypotheses of the proposed moment evaluations, not certified by
this argument alone. The coefficient engine and any future017 execution
require their own source-specific acceptance.

A manufactured exact fixture takes n=1, u=r(1+r^2)^(-2), so beta=3 and
k=-1 in the original r^3 representation. Let F=lambda Delta psi for any
real lambda. Integration by parts gives p=-lambda d, b=lambda a and
Q=lambda^2(a+d); the residual identity gives
R^2=(lambda+1)^2(a+d). This tests both signs and exact cancellation at
lambda=-1. The checker integrates the polynomial radial expressions by
exact rational beta integrals. This fixture is not a candidate017 norm.

## Evidence and scope

The proof is written before its checker. Exact JSON registers parameters
and frozen inputs. Thirteen source files are frozen, with gzip used only
as lossless storage. Their raw hashes match the originals. All29 bindings
in N4-413 were independently rehashed before freezing. Both peer programs
are read as text and never imported or executed. All160 mode labels,
primitive bounds, complete tails and positive E2 terms are reconstructed
with exact rational endpoint arithmetic. The historical residual program
hash differs from the available copied program hash and remains unobserved.
Incomplete diagnostic strings are rejected as interval certificates.

CONFIRMED means the conditional theorem, residual identity and finite
arithmetic under C1-C3. OPEN means the missing actual017 source integrals,
full component norms, complete upper and comparison with007. A successful
replay of sixteen duals and two residual trials cannot establish all
sixteen residual uppers, all160 Hardy squares or G0,G1,P2. No inverse,
normalization, scaling-mode control, correction distance, nonlinear
closure or existence is inferred.
