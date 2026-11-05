# Independent actual-source moment producer review

Reviewed `../finite_rank/certify_Q_source_constants.py`. Result: PASS for
the mathematical/enclosure method and assembly formulas. This is not a
claim that its live2303-panel run has completed.

The producer differentiates only the actual scalar density modes. Its
global-cap-aware frozen evaluator retains enough coefficients: density
series have degree chosen+5, two Laplacians consume four derivatives, and
the final radial derivative still retains degree chosen. The explicit
assertion checks every derived series before integration.

The source Cauchy bound is valid on r/8; on r/16 it gives k!M/(r/16)^k.
Combining those derivatives with |z|>=15r/16 proves the printed bounds
for Delta, radial/angular gradDelta, Delta² and gradDelta². In particular
the coefficient of f'/r4 in radial(Delta² f) is n4-10n²-3 and that of
f/r5 is -4(n4-4n²), agreeing with the implemented absolute bounds.

Each derived Taylor polynomial is squared as an Arb polynomial and
integrated exactly against r or r³. The stored interval includes every
polynomial coefficient error. Uniform remainder times sqrt(radial mass)
is added by Minkowski before squaring; the radial masses are exactly2rh
and2r³h+2rh³. Angular pi (or2pi for modezero) is correct, with no angular
truncation. Squaring uses multiplication, avoiding signed-ball powers.

The four unweighted core energies are the actual restricted norms of
Delta rho, gradDelta rho, Delta²rho, gradDelta²rho. The two weighted
energies are r times gradDelta and gradDelta². Origin/exterior tails
bound these same Laplacian expressions by their explicit Cartesian sums;
they do not apply a global Parseval identity on a restricted region.
Endpoint expansion degree20 gives N21, enough for the maximum physical
potential derivative order8. Every denominator in the tail integral is
asserted positive. The endpoint weighted-Hessian bound uses positive
origin powers or strictly negative shifted far powers, as required.

After complete whole-plane assembly, Parseval gives the intended B1..B4.
The coordinate formulas are exact:
\[
\|D^m(xb)\|²=\|r\nabla\Delta^{m/2}\rho\|²
+m²\|D^m\rho\|²,\qquad m=2,4.
\]
Thus totals4+4totals0 and totals5+16totals2 are correct. One independent
derivation differentiates b_hat=i xi rho_hat: integration by parts gives
||Dm(xb)||²=integral r^(2m+2)|grad rho_hat|²-2m||Dm rho||²;
the weighted gradDelta energy instead subtracts m(m+2)||Dm rho||².
Their difference is m²||Dm rho||². The actual fractional far growth makes
all boundary terms vanish at these orders; physical cutoffs give the same
identity by convergence in the stated derivative seminorms.

The H1 bound forms the three polar Hessian components before enclosure,
preserving cancellation of the linear mode at the origin. Their ordered
Frobenius norm is sqrt(rr²+2rtheta²+thetatheta²). Absolute harmonic sums
are valid uniform angular uppers. The source agent's separate exact-field
radial-versus-Cartesian checks provide additional independent convention
evidence and are saved in its `Q_source_radial_reduction_audit.json`.

Assembly checks full source/code bindings and complete base-index coverage.
Repeated identical rows are explicitly checked equal and included only once,
so no duplicate energy is counted. Every tail, moment, and displayed example
rate is containing Arb arithmetic. The source-commutator proof already
reviewed here supplies the correct interpolation constants and powers.
The displayed example R/M is an example only; the final existence join
must substitute the actual certified radii.

Full run completion, numerical envelope values, and final energy/inverse/
forcing/nonlinear assembly remain separate obligations.
