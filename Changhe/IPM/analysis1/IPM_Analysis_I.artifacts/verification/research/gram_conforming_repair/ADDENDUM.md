# Certified repair of the finite selected columns

All90 M16 and187 M24 selected radial splines admit the exact affine
endpoint repair of PROOF.md. Every piece is consecutive, every repaired
value trace agrees exactly, and the two support traces are zero. Both
arithmetic methods check all4432 repaired endpoint traces. Each first-piece
nonzero coefficient of degree>=2 is unchanged. Distinct support starts
therefore prove independence of the repaired radial functions, and angular
replication gives1440 and4488 independent functions in X, respectively.
They belong to a new space, not the original encoded span of topic131.

Uniform strict upper bounds, for every selected single radial column and
every single angular mode m, are:

| quantity | M16 | M24 |
| --- | ---: | ---: |
| relative broken energy change | 8.447e-15 | 2.5676e-14 |
| sup_t |Bhat-B| | 1.98e-16 | 1.8e-16 |
| piecewise sup_t |Bhat'-B'| | 3.752e-15 | 1.2642e-14 |

All displayed decimals are exact rational ceilings. The relative bound is
for the square root of the energy integral, as a norm would be. The
numerator uses PIECEWISE derivatives of the difference. It is not a weak
X norm or an X distance from the discontinuous original function. The
bound is not asserted uniformly for arbitrary linear combinations;
near cancellation and Gram conditioning require separate control.

For every piece, evidence/compute.json and independent.json give exact
support endpoints, matched values beta, the affine correction coefficients
and the integrated original/error polynomial squares. They also store
per-column weight-sum and ratio intervals. The compact summary checks all
columns again and records the extremizers: zero-based50 for M16,95 for M24.
The endpoints of the monotone weight are enclosed by Arb512 and mpmath.iv
at120 decimal digits, using different formulas for the positive power.
Original-square integration uses convolution then integration versus a
direct monomial double sum; affine-error integration uses convolution
versus the endpoint moment formula w(l^2+lr+r^2)/3.

The first method's initial trace test failed because an inherited helper
converted NEW exact rational correction coefficients through binary64.
That attempt produced no output certificate. Its code and failure are
preserved. The corrected helper preserves Fraction inputs, and the second
method independently recomputes all repairs and integrals without that
helper. No source dataset or earlier pinned result changed.

This is a constructive conformity result. It does not transfer the raw
matrix or its singular values to the repaired space. The canonical velocity,
operator action, scalar normalization, full column set, matrix perturbation,
Gram whitening and inverse remain unverified for this repair. Only C0
regularity is established at joins. It is not a PDE solution or endpoint.
