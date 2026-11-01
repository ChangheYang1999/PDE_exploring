# Interval compatibility needs three possible verdicts

Status: CONFIRMED diagnostic defect in the original retained numerics source. The subsequent three-state repair is independently CONFIRMED. This does not refute any separately verified exact nonzero compatibility coefficient.

## Claim and counterexample

At `delta=1/2`, order `n=8` has `p_n=-3`, `P_n=-2` and a stream resonance at `j=1`. If `a_0` is the coefficient of `sin(theta)` in `f_8`, the doubled forcing numerator in the numerics code is `-4 a_0`. The exact compatibility condition is `a_0=0`.

Consider an interval representation `a_0=[-epsilon,epsilon]`, where `epsilon>0`. This is consistent both with the compatible exact value zero and with incompatible nonzero values. Its interval numerator contains zero but is not the singleton interval zero. No valid inference of incompatibility follows from this enclosure.

The audited `ffcore.py` records `num_zero = num.is_zero()` at an exact resonance. The `step` method labels every record with `num_zero=False` as a failed exact compatibility condition. It therefore misclassifies this example. The independent script `code/interval_resonance_audit.py` reproduces the result with Arb 256-bit arithmetic and `epsilon=10^-30`, and also checks the exact-zero and definite-nonzero controls.

## Correct decision rule

There are three cases:

- An independently proved exact zero gives COMPATIBLE.
- An interval excluding zero gives INCOMPATIBLE.
- An interval containing zero without an exact-zero proof gives OPEN and requires more precision or exact arithmetic.

Stopping when the result is OPEN is appropriate for a certified numerical run. Calling it a mathematical obstruction is not. An exact rational calculation can settle a cancellation that interval arithmetic does not recognize.

## Evidence and scope

The source snapshot and its SHA-256 are retained with `verification/three_state_check.json`. The code computes the numerator at the exact rational resonance, so uncertainty in the denominator does not enter this example. This is a unit counterexample to the classification logic. It does not assert that a particular leading datum in the ongoing experiment produces zero compatibility.

The mathematical dependency is the independently derived Poisson equation in topic 01. The counterexample requires no unproved numerical assumptions or formal proof assistant.

## Repair verification

The later source with SHA-256 `309573a431e4d8f07944098808a5cba508603ef1796125e0cfd1d05c8d37459c` uses the three-state decision. The independent script `code/interval_resonance_repair_audit.py` verifies exact zero, an interval containing zero, a positive exact value, a negative exact value and a positive interval. All five checks pass. The ambiguous case raises a precision error and makes no obstruction claim. The original counterexample remains retained as historical evidence; the repair certificate is `verification/repair_check.json`.
