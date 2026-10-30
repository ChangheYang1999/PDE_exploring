# Candidate016: negative-norm lower bounds from exact test functions

## Exact statement and scope

Let c=4076476460239181/2251799813685248, delta=1-1/c, and let
chi be the exact potential C1-N1-016-legqs25-quot013 whose coefficient
SHA256 is a0345b4eee060ea8f6b0b6e21719cf606b04174704e0a26f516c645081208f42.
Set rho=-partial_y Delta chi, u=(-chi_xyy,chi_xxy), and
F=(cX+u).grad rho-rho. All norms and integrals use Lebesgue measure on
the entire plane, with angular interval [0,2pi].

Define H(F) as the norm of the functional phi -> integral F phi on the
completion of smooth compactly supported functions for ||grad phi||_2.
The accepted finite rF norm and the angular-divergence proof in
../candidate016_mode_hardy/PROOF.md imply H(F)<=||rF||_2<infinity.
This implication does not require the sharper mode-Hardy computation.

For distinct positive odd integers n, choose exact rational coefficients
x_i, exact rational beta_i>3/2 and integers k_i>=-1 satisfying
3+2k_i>=n. Define

 psi_n(r,theta)=sum_i x_i r^3 (1+r^2)^(-beta_i)
                         (r^2/(1+r^2))^k_i sin(n theta).

The parity condition is automatic because n is odd. If
d_n=||grad psi_n||_2^2>0 and p_n=integral F psi_n, then

 H(F)^2 >= sum_n p_n^2/d_n.                                      (1)

A successful own computation of p_n and d_n, with strictly positive
directed quotient floors, gives a lower bound for H. Neither a numerical
linear solver nor its conditioning enters (1). The coefficients are
treated as proposed exact data and every pairing and energy is recomputed.
No claim of an optimal test function is made.

## Admissibility and the finite-dimensional dual inequality

At zero each basis function is r^(3+2k) sin(n theta) times a smooth
function of r^2. Since 3+2k-n is a nonnegative even integer, it is smooth
in Cartesian coordinates. At infinity its size is O(r^(3-2beta)) and
gradient size O(r^(2-2beta)). Hence the gradient square is integrable when
beta>3/2. Multiplying by smooth cutoffs equal to one on r<=R and zero
on r>=2R gives convergence in the gradient norm: both the gradient tail
and the cutoff derivative term are O(R^(6-4beta)), which tends to zero.
Thus each psi_n represents an element of the stated completion.

Every nonzero pairing term in the calculation below must pass absolute
endpoint integrability. Dominated convergence then identifies the
functional value with the ordinary displayed integral. The continuity
already obtained from rF gives the same limit for the cutoffs.

The gradients of distinct angular modes are orthogonal, by the sine and
cosine orthogonality relations. For arbitrary real a_n, continuity gives

 |sum_n a_n p_n| <= H(F) (sum_n a_n^2 d_n)^(1/2).

Choose a_n=p_n/d_n and square, obtaining (1), with the zero-pairing case
immediate. The conclusion does not require a separate numerical Fourier
transform or an unproved identity for the negative norm.

## Independent polar gradient energy

Put t=r^2/(1+r^2) and v=1-t. Group the exact test coefficients by
b=beta-1 and let P_b(t)=sum_(i:beta_i-1=b) x_i t^(k_i+1).
Then the radial amplitude is r sum_b v^b P_b(t).
Define

 D_b P=(1-2bt)P+2t(1-t)P'.

Direct differentiation gives d/dr(r v^b P)=v^b D_b P.
Consequently

 d_n/pi = (1/2) sum_(b,c) integral_0^1
   v^(b+c-2) [(D_b P_b)(D_c P_c)+n^2 P_b P_c] dt.                (2)

All ordered pairs are retained. The exponent b+c-2 is greater than -1
because beta_i,beta_j>3/2. The integrands have rational polynomials and
rational exponents. After substituting t=1-v each monomial is integrated
exactly as integral_0^1 v^(e+j)dv=1/(e+j+1). Thus (2) is an exact rational
number times pi. It must agree exactly with the peer's saved rational
gradient energy, if that field is supplied.

This is an independent polar formula, not the peer's Cartesian derivative
Gram matrix or its linear solver.

## Complete residual pairing

Reconstruct the complete projected residual directly from the exact
potential using the own algorithm in ../joint_scaled_factored_weak:

 f_n(r)=r sum_ell v^(ell delta/2) A_(ell,n)(t).

The functions A are exact rational functions with denominators consisting
only of positive factors 1+a v, a in {99,624,2499,9999}. Actual016 uses
only624. Bind the reconstructed projected coefficient hash to the own
previously accepted complete mode record for modes1 and3, or to a fresh
direct reconstruction check for any additional mode.

Angular integration and r dr=dt/(2v^2) give

 p_n=(pi/2) sum_(ell,b) integral_0^1
            v^(ell delta/2+b-3) t A_(ell,n)(t) P_b(t) dt.          (3)

For each complete rational group extract the exact numerator power v^q.
Require ell delta/2+b-3+q>-1 before evaluating it. The denominators are
positive on [0,1]. Require finite, sufficiently accurate outward balls
from the own exact partial-fraction and positive-pole moment algorithm in
../rational_pole_moments/PROOF.md. Its reconstruction identity is replayed.
Sum every group. No cutoff, quadrature, omitted frequency interaction or
analytic continuation is used.

For comparison, the peer's per-basis pairings may be summed using its
exact vector, and its saved total pairing and gradient energy may be
checked. The own bound depends on (2), (3) and the exact proposed vector.
It does not depend on the peer's claimed solver residual or optimality.

## Directed bounds and optional energy ordering

Interpret all saved Arb balls as containing intervals. If an own quotient
ball |p_n|/sqrt(d_n) has a positive rational lower floor l_n, then
H(F)>=sqrt(sum_n l_n^2). Require distinct modes. Do not square a possibly
negative lower endpoint. A comparison with the peer's containing
quotient ball is a consistency check, not the source of the lower bound.

Once independent component acceptances are bound, define exactly

 E2(F)^2=P2^2+2^14 G1^2+2^18 G0^2+(20/21)2^18 H(F)^2,

where G0=||F||_2, G1=||grad F||_2, and
P2=||(1+4r^2)^(2/5)D^2F||_2. Inserting the accepted component lower
bounds and (1) gives a lower bound for this energy. It orders the actual
007 and016 energies only if it is strictly greater than the independently
accepted upper bound for007 with the same exact definition and weights.
This comparison remains OPEN until that directed inequality is executed.
It would not order stationary correction distances, inverse norms, or
other energies with different weights.

## Evidence and execution

Write and review this argument before the checker. Freeze the selected
small peer certificate containing the exact vector, labels, pairings and
denominator, together with its source hashes and code as text. Never copy
the large peer residual cache or import peer code. Rebuild the own
projection from the frozen raw candidate, bind every own module/proof and
accepted calibration, and recheck hashes after the calculation. Record
partial failures and actual times. The computation is OPEN until every
required check passes.
