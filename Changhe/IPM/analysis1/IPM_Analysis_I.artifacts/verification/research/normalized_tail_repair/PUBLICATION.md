# Exactly normalized trials with a square-integrable residual

Read PROOF.md and the mandatory ADDENDUM.md. Status is pending final
whole-bundle review and the verdict in evidence/verdict.json.

For every T>=max(exp(tplus),L,1), the explicit rho_T defined in (5)
preserves the center factor a(0)=1, all required parities, the exact
canonical center strain, and c0=1/k. It equals rho0 as a density inside T.
Its nonlocal velocity changes there. Its residual belongs to unweighted
L2(R2). The correction itself does not belong to unweighted L2.

For the exact weight W=(1+(r/L)^2)^((k-3)/2), the certificate gives

 sup |(rho_T-rho0)/(x^2 y W)| < 0.334616 T^(k-1).

Both independent interval engines give N<38.37961982 and
|I_H|<0.03893786140; substituting these strict ceilings in formula(6)
still gives C<0.334616. The sharp computed sum constant, without
substituting the two printed ceilings, lies in
(0.334615938777,0.334615938779). N is the absolute coefficient sum
of a 521-term Chebyshev quotient, and I_H is its density's signed
sin(3theta) coefficient. No division by a small sampled angular factor
is used.

The following are strict upper bounds for the displayed weighted norm.
Every listed T exceeds exp(tplus), L and1 by directed checks.

| T | Weighted factor norm below |
|---:|---:|
| 10000 | 0.0001746 |
| 1000000 | 0.000003988 |
| 100000000 | 0.00000009109 |
| 10000000000 | 0.000000002081 |
| 1000000000000 | 0.00000000004752 |
| 10000000000000000 | 0.00000000000002480 |

The small factor cost is obtained by moving a non-L2 tail correction
outward. No finite upper bound for the L2 residual norm is supplied;
it need not become small as T increases. The leading r^k angular profile
is unchanged, so this construction does not repair the leading-tail
separation between X3 and the modal trial. It establishes neither
stationarity, an uncertainty class around X3, source estimates, a global
inverse, nor a nonlinear closing inequality. It is not a decisive endpoint.

The primary uses Arb512 with exact collected integer inverse-sine forms.
The independent method uses mpmath.iv180 with three Laurent synthetic
divisions and independently decoded NPZ scalars. Their distinct input
vectors are the two complete 522-frequency certificates of topic42.
An exact rational audit reconstructs the entire triangular linear map,
checks every quotient enclosure from each input vector, its absolute
coefficient norm, all transition polynomial moments and source data.
The T examples use Arb768 and mpmath.iv200 separately. All printed
ceilings are checked as exact rationals, with finite exact decimal export.
