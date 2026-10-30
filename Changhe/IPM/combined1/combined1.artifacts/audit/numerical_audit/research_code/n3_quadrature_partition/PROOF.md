# Radial partition audit for the N3 synthetic quadrature check

## Exact statement and scope

The frozen legqs_quadcheck.py constructs the following 57 radial panels
in t=r^2/(1+r^2):

 [0,1/2];
 [1-2^(-k),1-2^(-(k+1))], k=1,...,45;
 [2^(-(k+1)),2^(-k)], k=1,...,11.

They do not form a partition. Their exact sum of indicator functions is

 1_[0,1-2^-46] + 1_[2^-12,1/2]

away from the finitely many endpoints. In particular, a constant
integrand is integrated with total panel mass

 3/2-2^-12-2^-46,

rather than the covered interval length 1-2^-46. The discrepancy is
1/2-2^-12. This refutes the claimed composite-partition interpretation.
It does not refute N3's distinct rational radial integrator, nor establish
a particular error size for its six-generator residual.

## Proof

Consecutive upper panels meet because the right endpoint for index k
is the left endpoint for k+1. Their union is [1/2,1-2^-46] and their
interiors are disjoint. The initial panel [0,1/2] joins them to form
[0,1-2^-46]. Similarly the eleven lower panels have disjoint interiors
and union [2^-12,1/2], which is already contained in the initial panel.
This proves the indicator identity. Integrating the identity against
any integrable scalar function g gives

 sum_panels integral_panel g
 = integral_0^(1-2^-46) g + integral_(2^-12)^(1/2) g.

For g=1 it gives the exact panel mass above. An ideal Gauss rule of
positive order integrates constants exactly on each panel, so it
already fails this global constant check by the stated positive amount.
Floating quadrature weights can perturb this equality; they cannot
make the panel list an exact partition.

For a nonnegative squared-residual radial integrand the duplicated
continuous contribution is nonnegative and is strictly positive when
the integrand is positive on a set of positive measure in the overlap.
The actual computed quadrature also has local numerical error and
omits [1-2^-46,1]. No error estimate for the actual residual follows
merely from this sign or the constant example.

## Concrete repair and remaining conditions

Replace the first panel [0,1/2] by [0,2^-12], retaining the same upper
and lower panels. Then the lower panels join [0,2^-12] exactly to
[0,1/2], and the upper panels extend this to [0,1-2^-46]. This is a
57-panel partition with positive lengths and disjoint interiors.
The resulting composite Gauss rule still requires a quadrature error
bound and a bound for the final omitted interval before it can certify
a whole-plane integral. In the present program it is a FLOAT cross-check
against a separate full-plane analytic certificate.

## Verification and dependencies

Freeze the source and its failing log before running the own checker.
The checker reads the source as text, reconstructs the exact rational
panel list from the stated constants, enumerates every endpoint cell,
and verifies the full multiplicity function and constant-integral
identity. It also checks the proposed corrected partition. No N3 code
is executed for this audit. The field equation and model coefficients
are not needed for a domain-partition result. All evidence and writes
remain inside the N4 numerical auditor; no servers, JavaScript or remote compute are used.
