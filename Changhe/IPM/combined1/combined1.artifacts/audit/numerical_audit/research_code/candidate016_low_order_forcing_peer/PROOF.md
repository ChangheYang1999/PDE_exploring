# Candidate016: reciprocal acceptance of the low-order forcing obstruction

## Statement and conventions

Fix the exact potential of C1-N1-016-legqs25-quot013, with coefficient
SHA256 a0345b4eee060ea8f6b0b6e21719cf606b04174704e0a26f516c645081208f42
and c=4076476460239181/2251799813685248. Put
rho=-partial_y Delta chi, u=(-chi_xyy,chi_xxy), and
F=(cX+u).grad rho-rho on R^2. These are the canonical real S1 conventions
of ../joint_scaled_factored_weak/PROOF.md. Every L2 norm uses Lebesgue
measure on R^2. Derivatives are weak Cartesian derivatives and the
Hessian has its ordered tensor norm. Use the unitary Fourier transform,
J=(1-Delta)^(1/2), Lambda=(-Delta)^(1/2), and
omega=(1+4|X|^2)^(2/5).

For positive weights w1,w2 define, allowing value +infinity,

 X_(s,w)(F)^2 = ||omega D^2 J^s F||2^2
                    + w1 ||D J^s F||2^2 + w2 ||J^s F||2^2,
 N_s(F)^2 = X_(s,(2^14,2^18))(F)^2
                    + 2^18(20/21)||Lambda^(-1)J^s F||2^2.

The legacy X3 norm is X_(s,(2^14,2^18)). If a displayed distribution
does not define an L2 function with its indicated weight, its squared
norm is +infinity. Thus failure of finite regularity cannot make the
smallness test pass.

Let ell0 and ell1 be the exact rational lower endpoints accepted in
N4-373, as transcribed into ../candidate016_low_order_forcing/source/components.json:

 ell0 = 0.308886445142524736777066916039,
 ell1 = 3.726906948019883998020959016407.

N4-341 and N4-373 independently establish F in H^1(R^2),
||F||2 > ell0 and ||DF||2 > ell1. For every s>=0 and w1,w2>0,

 X_(s,w)(F) > L_w := sqrt(w1 ell1^2 + w2 ell0^2),
 N_s(F) > L_(2^14,2^18).                                      (1)

The exact ten registered instances, their weights and sufficient
thresholds are in ../candidate016_low_order_forcing/source/parameters.json. A passing scalar checker
establishes a strict lower bound for each L_w/threshold exceeding one.
Consequently each of those ten sufficient forcing smallness conditions
fails for the actual candidate. This conclusion uses no unaccepted
P2, H, higher derivative or fractional upper enclosure. It is not a
nonexistence theorem for stationary corrections and does not exclude a
different forcing norm, inverse estimate or sufficient threshold.

## Proof of the lower comparison

Plancherel gives, with extended integrals when necessary,

 ||J^s F||2^2 = integral (1+|xi|^2)^s |Fhat(xi)|^2 dxi,
 ||D J^s F||2^2 = integral |xi|^2(1+|xi|^2)^s |Fhat(xi)|^2 dxi.

For s>=0, the multiplier (1+|xi|^2)^s is at least one. These two
identities therefore imply ||J^s F||2>=||F||2 and
||D J^s F||2>=||DF||2. Dropping the nonnegative weighted Hessian
square, and the nonnegative homogeneous negative norm square in N_s,
gives (1). Strictness follows from the already accepted strict positive
component lower endpoints and the positive weights. The argument needs
no commutator estimate, since it only uses the two unweighted entries.
If a norm is infinite the same inequality is immediate.

## Numerical evaluation and source fidelity

The scalar evaluation first binds the complete N4-373 acceptance input
graph, its own proof and code, the exact parameter transcription, the
N4-332 source-formula audit and that audit's original local inputs. It
requires both accepted component lower endpoints to match the copied
rational inputs exactly, verifies their strict direction against the
accepted own containing balls, and uses only these endpoints in (1).
The previous N4-332 conditional component assumptions are not used.
That record supplies previously checked formula and threshold provenance.
In particular the exact rebalanced threshold is 3/327680 and the legacy
X3 threshold is 1/163840; their rounded decimal alternatives are ignored.

At 1024 bits, Arb contains each positive rational weighted sum, its square
root and the quotient by the positive exact source threshold. Every
reported integer factor and decimal lower bound is rounded downward
from the ball's lower endpoint and then checked strictly against the
entire ball. All input hashes are rechecked after arithmetic. The
checker imports no field construction or peer implementation and repeats
no spatial integration. Only its successful result authorizes numerical
claims from this proof; preparation alone leaves them OPEN.

## Scope

This establishes failure of named sufficient scalar forcing conditions
at the fixed exact candidate. The separate weak-distance and pointwise
arguments establish their own correction-ball exclusions. No L2
correction-distance bound is silently transferred to a dyadic space.
There is no inverse certificate, contraction proof or existence claim.
The full P2 integration and angular-divergence upper bound for H remain
separate jobs, regardless of whether the present scalar test passes.

## Reciprocal review of T4-451

T4-451 independently proves the same Plancherel inequality and evaluates all ten exact rational lower squares. Its finite checker also sums the saved31 complete moment groups for G0 and G1. This summation is a consistency check of already accepted integrals, not a third independent integration. Acceptance binds every input in its manifest, its checker, result and current source attestation. Files originally copied from this lane can be reused only when their content hashes agree. All other required foreign files are copied before arithmetic.

For each component, compare the exact directed endpoints and the independent norm ball from the saved integrals with the own accepted balls. For each of the ten exact parameter rows, recompute the positive rational square w1 ell1^2+w2 ell0^2, its square root and its ratio to the exact threshold. Require equality of exact squares, strict directed endpoints and integer factors and overlap of each independent ball. Every original own N4-374 input is rehashed and compared with the peer's59-file attestation. This attests the current retained bytes; it does not retrospectively observe their historical loading. Read the entire87-line peer proof and74-line checker as text. No peer source is executed.

Only passing finite comparisons accept T4-451. All named sufficient tests fail; correction-ball nonexistence, dyadic norm claims, H equality and a fractional upper enclosure remain outside this result. The ten exact spaces, weights, thresholds and proof hypotheses above govern the reciprocal acceptance. Full agreement of1024 endpoint bits remains unasserted because the saved norm balls contain only100 decimal digits.
