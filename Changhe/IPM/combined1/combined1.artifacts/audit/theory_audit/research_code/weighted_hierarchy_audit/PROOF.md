# Audit of the additional weighted-derivative claims

This note audits Remarks R2 to R5 of the T2 theory worker the review of T4-194. The main
weighted-gradient theorem was accepted separately in T4-237. The review
and its exact helper are frozen in
../weighted_gradient_velocity/reviews/T2_194/. No new numerical profile
calculation is used here.

## 1. Definitions and conclusions

Let w_p(X)=(1+|X|^2/R^2)^(p/2), R>0. Let U=(-R1R2,R1^2) be the canonical
IPM velocity and let B have symbol (xi1-i xi2)^2/|xi|^2. All input tests
are real, smooth, compactly supported and S1, even in x and odd in y.
D^j means the full ordered Cartesian tensor. A row estimate means a
constant C, independent of the test, in

    ||w_p D^j U[h]||2 <= C ||w_p D^j h||2.             (1)

The following parts of the review are CONFIRMED.

* For the gradient row the optimal constant C*_p is at least1. On the
  radial sine-one family its exact squared ratio is (1+E_g/E_f)/8.
* For 0<=p<3 the frozen negative-mode gradient ratio is the stated
  decreasing Mellin multiplier, with supremum at zero frequency. The
  resulting S1 lower bound is valid.
* The scalar row at weight p and gradient row at weight p+1 both hold
  precisely when -2<p<2. This is a statement about both separate rows.
* For j odd a necessary interval for (1) is -1<p<j+2. For j even,
  including j=0, it is -2<p<j+2. The review's known sufficient intervals
  follow from the already audited scalar and gradient estimates.

Two unqualified formulations need correction. The frozen ratio is not
decreasing for negative p. The usable gradient residual range for007
is the intersection -1<p<-e_F, not the whole range p<-e_F. The stated
finite grid comparison near factor1.51 is FLOAT, not a certified uniform
operator-constant comparison.

## 2. Lower bounds and the sine-one formula

In unweighted L2 the exact velocity symbol gives

    ||grad U[h]||2^2=||partial_x h||2^2.

Take h_N=phi(x,y)cos(Nx), with a nonzero compact smooth S1 envelope phi.
Its x derivative has norm of orderN and its y derivative has bounded
norm, so its unweighted velocity ratio tends to1. For any fixed h_N,
replace it by h_N(X/epsilon). In dimension two the gradient L2 norm is
scale invariant. The compactly supported input weighted norm tends to
its unweighted norm as epsilon tends to zero. If p>=0, the output
weighted norm is at least its unweighted norm. If p<0, after scaling its
squared integrand is w_p(epsilon X)^2 |grad U[h_N](X)|^2; it converges to
the unweighted integrand and is bounded by it. Dominated convergence
therefore applies. These facts prove C*_p>=1 whenever it is finite;
if a test has infinite output the lower bound is automatic.

For h=f(r)sin(theta), write

    h=(f e^(i theta)-f e^(-i theta))/(2i).

The canonical B sends the first term to f e^(-i theta) and the second
to g e^(-3i theta), by the gradient theorem's mode equation. Thus
h+B h=(f e^(i theta)-g e^(-3i theta))/(2i). Angular orthogonality and
U2+iU1=-(h+B h)/2 give the exact squared ratio

    ||w_p grad U[h]||2^2/||w_p grad h||2^2=(1+E_g/E_f)/8.

Here E_f is the radial gradient energy of frequency1 and E_g that of
frequency-3. The factor1/8 accounts for the two equal input modes and
the velocity factor1/2.

For a negative input mode m=-M and pure power weight r^p, the substitution
F=e^(pt)f, G=e^(pt)g, t=log r, turns the canonical radial equation into
a constant-coefficient first-order equation. Fourier transformation and
the gradient energies give

    S(tau)=[tau^2+p^2+(M+2)^2][tau^2+(M+p)^2]
             /([tau^2+(M+2-p)^2][tau^2+p^2+M^2]).       (2)

If p>=0, the excess of numerator over denominator in the first ratio
is2p(M+2), and in the second it is2Mp. Each ratio is nonincreasing in
tau^2. In the gradient range 0<=p<3 all denominators for M>=1 are
positive, so its supremum is S(0). Slowly varying smooth bumps in t
concentrate at frequency zero. Translating each bump far enough outward
makes the inhomogeneous weight agree with r^p, with arbitrarily small
relative error in both input and output energies. One can take the
translation limit for each fixed bump first, then its width limit.
The canonical output decays fast enough because p<M+2. This proves
the review's lower bound and attainment as a supremum when 0<=p<=1.

For p=-1/2 and M=1, formula(2) instead gives S(0)=37/245<1 and
lim_(|tau|->infinity) S(tau)=1. Both factors are strictly increasing.
This exact counterexample refutes the unqualified monotonicity claim.
The corrected positive-p argument above does not use it.

## 3. All derivative-row necessary endpoints

It is enough to set R=1 by spatial scaling. For the upper endpoint,
choose h=f(r)sin(theta), with a nonzero nonnegative radial bump supported
in1<r<2. Outside its support the positive mode's B output is zero and
the negative mode is a nonzero multiple of r^-3 e^(-3i theta). Thus the
complex velocity is a nonzero multiple of z^-3 there. Its full jth
Cartesian derivative is nonzero with size a positive constant times
r^(-3-j). The weighted squared exterior integral is a nonzero constant
times integral r^(2p-5-2j)dr, which diverges exactly for p>=j+2. The
compact input has finite norm for every p.

For the lower endpoint fix a smooth nonnegative radial bump chi supported
in1<r<2. If m>=3 is odd and h_*=chi(r)sin(m theta), its complex B output
inside r<1 is exactly a nonzero multiple of z^(m-2). The negative mode
is zero there. This follows by integrating the first-order mode equation:
the positive coefficient is a nonzero multiple of

    (m-1) integral_1^2 chi(s) s^(-(m-1)) ds.

The coefficient is nonzero because chi is nonnegative and not zero.
Therefore the complex velocity is also a nonzero multiple of this
polynomial inside the ball.

If j is odd, choose m=j+2 and h_L=L^j h_*(X/L), L>=2. Then D^j U[h_L]
is the same fixed nonzero constant tensor on |X|<1, independent ofL.
The derivative input is supported in L<r<2L and its weighted norm is
bounded above and below by fixed positive constants times L^(p+1).
For p<-1 the input tends to zero while the output has a fixed positive
local norm. At p=-1 take the sum of the firstN such inputs at scales
L=4^k. Their derivative supports are disjoint, so the input norm is
at most C sqrt(N). On |X|<1 the output tensors add to N times the same
nonzero tensor, giving an output norm at least cN. No uniform row
estimate is possible at the endpoint either.

If j is even, choose m=j+3 and h_L=L^(j+1) h_*(X/L). In |X|<1,
D^j U[h_L] is now the same nonzero linear tensor field, independent ofL.
Its local L2 norm is positive. The input norm is comparable to L^(p+2).
For p<-2 the same vanishing-input argument applies. At p=-2 the same
disjoint dyadic sum gives input O(sqrt(N)) and local output at least cN.
This also covers j=0. Thus both stated lower endpoints are excluded.

All these tests have S1 parity. Their velocities are the full canonical
ones, including the local identity term; the input vanishes on the
regions used for the lower bound, so that local term is zero there.

## 4. Sufficiency already available and residual scope

For j even, each component of D^j h is centrally odd. The audited
weighted scalar estimate gives (1) on -2<p<2, with constant at most
2/(2-|p|). For j odd, apply the audited gradient estimate to every
component of D^(j-1)h and sum their squares. This proves (1) on
-1<p<3, with exactly the gradient constant. The tensor multiplicities
are those of the full ordered derivatives, so this step has no missing
binomial factor. T4-242 separately proposes the additional point p=2
for j=2; that new theorem still needs independent review.

For the pair of scalar/gradient rows with weights p,p+1, the audited
necessary and sufficient intervals are respectively -2<p<2 and
-1<p+1<3. They coincide. At p=4/5 the constants5/3 and2 in R3 are
correct: at gradient exponent9/5, A=17/2 and B=2.

The statement in R5 that every p<-e_F is available for the007 gradient
row omits its necessary condition p>-1. For example p=-2 satisfies
p<2.790445 but the odd-j endpoint argument above rules out a uniform
gradient estimate. With the review's already established nonzero smooth
leading residual term, the usable intersection is -1<p<-e_F. This
correction changes no candidate closure verdict.

Dependencies: the audited T4-177 and T4-194 estimates, the canonical
mode equation proved in T4-194, and elementary Fourier orthogonality,
scaling and dominated convergence. The endpoint constructions and
counterexample above are complete and require no numerical scan.
