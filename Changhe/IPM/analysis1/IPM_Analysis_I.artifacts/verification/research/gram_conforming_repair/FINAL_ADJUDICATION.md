# Final adjudication of the exact continuous repair

2026-10-21. CONFIRMED_CONTINUOUS_SPLINE_REPAIR_AND_SINGLE_COLUMN_BROKEN_ENERGY_BOUNDS.
Read PROOF.md, ADDENDUM.md and REVIEW_RESOLUTIONS.md with this adjudication.
All integrals here are on the full plane, with angular range [0,2pi].

The exact affine endpoint repair constructs 90 and 187 independent
continuous compactly supported radial polynomials from the selected
M16 and M24 metadata columns. Angular replication gives 1440 and 4488
independent functions in the weighted weak-gradient space X. Every
repaired join is exactly continuous, including both support endpoints.
The repaired space differs from the exact encoded space in topic131.
Only C0 regularity is proved; derivative jumps can remain.

For each selected column and every single angular mode, the relative
BROKEN energy error is strictly below 8.447e-15 for M16 and 2.5676e-14
for M24. These exact rational ceilings apply to the square root of the
energy integral. The coefficient sup error is strictly below 1.98e-16
and 1.8e-16, and the piecewise t-derivative sup error is strictly below
3.752e-15 and 1.2642e-14, respectively. The ratio-bound extremizers have
zero-based column indices 50 and 95. This is not an X distance from an
original discontinuous function and is not a relative bound for arbitrary
linear combinations.

Exact rational Horner evaluation, convolution and integration with Arb512
endpoint weights are independently checked by a NumPy-free binary64 bit
reader, direct monomial sums, affine endpoint moments and mpmath.iv120
weights evaluated with exp/log. All 4432 traces, all 2216 pieces, all 277
column bounds and all strict public ceilings agree. The summary checks
every exact repair record and both engines' bounds. The X weight and
polar identity are stated explicitly in REVIEW_RESOLUTIONS; the exact
weight exponents are additionally checked against the frozen definition.

Two authenticated actual Claude Opus 5.5 reviews completed with end_turn.
The follow-up independently resolved the norm dependency. Its incidental
uncertainty about the integration domain is removed by the full-plane
convention above. No remaining objection refutes the restricted theorem.
The original reviewed text is preserved; the authoritative correctly
rendered table is in REVIEW_RESOLUTIONS. The failed rational-roundtrip
attempt remains as evidence and is not used for any claim.

This result supplies a possible continuity repair and quantifies its
single-column broken energy error. It does not transfer the original raw
matrix, velocities, operator action or Gram whitening to the repaired
space. The complete trial space, normalization, matrix perturbation,
conditioning, spectrum, global inverse and nonlinear closure remain OPEN.
It is neither a YES nor a NO endpoint for the IPM task.
