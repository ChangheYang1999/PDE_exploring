# Finite exact tests for the homogeneous negative norm

Written 2026-10-29T15:13:18.859853+00:00. This is an analytic audit of the prospective N4 dual
certificate. No candidate016 numerical dual value is accepted here.

## Statement and hypotheses

Let F be a real smooth function on R2 with a finite sine expansion
F(r,theta)=sum_(n in E) f_n(r)sin(n theta), where E contains distinct
positive integers, and suppose rF belongs to Lebesgue L2(R2). Define

 H(F)=sup_(phi in C_c^infinity, ||grad phi||2<=1)|integral F phi|.

Equivalently this is the continuous functional norm on the completion
of C_c^infinity in the gradient norm, once finiteness has been proved.
Fix finitely many distinct positive odd integers n. For each n choose
finitely many rational numbers x_i, rational beta_i>3/2, and integers
k_i>=-1 satisfying 3+2k_i>=n. Set

 psi_n=sum_i x_i r^3(1+r^2)^(-beta_i)
                    (r^2/(1+r^2))^k_i sin(n theta).

Suppose every ordinary pairing p_n=integral F psi_n is absolutely
integrable and let d_n=||grad psi_n||2^2>0. Then

               H(F)^2 >= sum_n p_n^2/d_n.                (1)

There is no optimality, solver convergence or Gram conditioning
hypothesis. Each proposed rational vector defines a test, regardless
of how it was obtained. Numerical use requires a complete independent
pairing, an outward energy enclosure with positive denominator, and
source identification of F and all exact test parameters.

## Boundedness of the functional

Define A=-e_theta r sum_(n in E) f_n(r)cos(n theta)/n. Then

 ||A||2^2=pi sum_(n in E) n^-2 int_0^infinity r^3 f_n(r)^2 dr
           <=||rF||2^2.

Angular integration by parts on annuli gives div A=F. There is no
radial flux through either annular boundary, since A is tangential.
At the origin one may take the limit against a smooth compact test:
A is locally L2 and F is smooth, so the missing disk contributes
zero to both integrals. Thus the equality holds in distributions
on R2. Cauchy-Schwarz yields |int F phi|<=||A||2||grad phi||2,
so H(F)<=||A||2<=||rF||2 is finite. The completion is used as a
Hilbert space of gradient limits; no unjustified pointwise trace or
choice of a homogeneous Sobolev representative is required.

The absence of mode zero is essential for this particular field.
The candidate016 application must verify its complete odd sine
content and finite rF norm. A partial angular sum gives a lower
witness by (1), but cannot give this upper bound for all of F.

## Origin, infinity and admissibility

Each basis element equals
r^(3+2k) (1+r^2)^(-beta-k) sin(n theta). The integer
3+2k-n is even and nonnegative because n is odd. Therefore
r^(3+2k)sin(n theta) equals a nonnegative integer power of x^2+y^2
times Im((x+iy)^n), a polynomial. The factor (1+r^2)^(-beta-k)
is smooth. This includes k=-1 only when the origin condition allows
it; for n=1 it gives a smooth linear leading term.

At infinity the function is O(r^(3-2beta)) and its gradient is
O(r^(2-2beta)). Its squared gradient tail is O(R^(6-4beta)).
For a radial cutoff chi_R with |grad chi_R|<=C/R, supported on
r<=2R and equal to one on r<=R, the squared L2 norm of
psi_n grad chi_R is also O(R^(6-4beta_min)), after summing the
finite basis, where beta_min is the smallest retained beta.
Both squared quantities tend to zero. The corresponding gradient
norms have order O(R^(3-2beta_min)), rather than O(R^(6-4beta_min)).
Hence chi_R psi_n is smooth compactly supported and converges to
psi_n in the gradient completion. Absolute integrability of F psi_n
and dominated convergence identify its functional value with p_n.

## Orthogonality and the dual bound

For distinct positive n and m, both int sin(n theta)sin(m theta)
and int cos(n theta)cos(m theta) vanish. The radial and angular
terms in the gradient inner product therefore give
int grad psi_n.grad psi_m=0. For arbitrary real a_n,

 |sum_n a_n p_n| <= H(F)(sum_n a_n^2 d_n)^(1/2).

If all pairings vanish, (1) is immediate. Otherwise choose
a_n=p_n/d_n and divide by the positive square root of
sum p_n^2/d_n. This proves (1). Omitting further modes only weakens
the bound. Repeating the same mode would invalidate this diagonal
sum; same-mode tests require their full Gram matrix instead.

## Exact polar energy and pairing formulas

Put t=r^2/(1+r^2), v=1-t, b=beta-1, and
P_b(t)=sum_(i:beta_i-1=b) x_i t^(k_i+1). Since k_i>=-1,
P_b is a polynomial. The radial amplitude is r sum_b v^b P_b(t).
Using dt/dr=2r v^2, direct differentiation gives

 d/dr(r v^b P)=v^b D_b P,
 D_b P=(1-2bt)P+2t(1-t)P'.

Since r dr=dt/(2v^2) and int sin^2(n theta)=int cos^2(n theta)=pi,

 d_n/pi=(1/2) sum_(b,c) int_0^1 v^(b+c-2)
                [(D_b P_b)(D_c P_c)+n^2 P_b P_c]dt.       (2)

All ordered pairs must be included. The exponent b+c-2 is greater
than -1 because each beta exceeds3/2. After t=1-v, every integrand
is a finite polynomial times that rational power, with exact integral
int_0^1 v^(e+j)dv=1/(e+j+1). Thus d_n/pi is exactly rational.
Individual expanded cross coefficients may be negative, although
the complete d_n is a nonnegative squared norm. A nonzero gradient
or an exact positive final value establishes d_n>0.

If the complete projected residual has form

 f_n(r)=r sum_ell v^(ell delta/2)A_(ell,n)(t),

then angular integration and the same Jacobian give

 p_n=(pi/2)sum_(ell,b) int_0^1
             v^(ell delta/2+b-3)t A_(ell,n)(t)P_b(t)dt.    (3)

Suppose the A are exact rational functions with only positive
factors 1+a v in their denominator, and each complete numerator
has an exact factored power v^q. Requiring
ell delta/2+b-3+q>-1 makes that complete group absolutely
integrable at v=0. Denominator positivity controls the whole closed
interval, and t=0 introduces no singularity because the original
origin-compatible expression is polynomial there. These sufficient
conditions justify (3), termwise integration and dominated convergence.
If cancellations are needed, extract them before evaluating separate
moments; divergent pieces cannot be assigned values by continuation.
The numerical partial-fraction implementation requires its separately
verified reconstruction identities and directed moment enclosures.

## Directed arithmetic and optional energy ordering

For each distinct mode, if a computed ball encloses p_n and a positive
ball encloses d_n, a certified rational l_n>0 satisfying
l_n<=|p_n|/sqrt(d_n) implies H(F)^2>=sum_n l_n^2. Reject a pairing
ball crossing zero unless its contribution is conservatively set to
zero. Never square an arbitrary negative lower endpoint as if it were
a lower bound for the squared norm. Bounds for signed quotient values
must first be converted to a valid lower bound on their absolute value.

For exact positive constants A,B,C, the energy
E(F)^2=P2(F)^2+A G1(F)^2+B G0(F)^2+C H(F)^2
admits the lower bound formed from independently accepted nonnegative
component floors and (1). To compare E(F016) with E(F007), its lower
bound must exceed a valid upper bound for E(F007) using exactly the
same definitions and coefficients. Two lower bounds do not order
the actual energies. Neither ordering compares stationary-correction
distances or proves a closure theorem.

A lower H witness below a claimed upper H value is consistent with
that upper value. It does not confirm the upper bound. The angular
vector field and a complete upper enclosure of its L2 norm establish
the upper bound independently. This distinguishes the consistency
check in N3's 15:05 note from the actual upper-bound proof.

## Audit verdict and dependencies

CONFIRMED: the analytic prospective N4 dual proof, formulas (1)--(3),
its domain, its exact-vector use and the scope of its energy comparison.
Its cutoff sentence should identify R^(6-4beta) as a squared gradient
bound, which this proof does explicitly. The original theorem is
unaffected by that wording clarification.

OPEN: all new candidate016 numerical p_n, d_n, dual H and actual E2
ordering until N4's independent calculation passes. The earlier
accepted full G0/G1/P2 calculation is a distinct premise. No peer
program, solver or field integration is executed in this audit.
The frozen prospective proof and Hardy proof are in source/. Their
hashes and the manual claim-by-claim audit are recorded in
verification/analytic_review.json.
