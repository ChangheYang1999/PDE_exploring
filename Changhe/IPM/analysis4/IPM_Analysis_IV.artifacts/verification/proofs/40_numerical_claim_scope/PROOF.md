# What the finite growth and residual experiments establish

Status: scope audit. This does not challenge the independently verified finite coefficients or residuals.

## Claims and conditions

The retained numerical report contains experiments at fixed inputs through finite orders, including the exact stored Candidate parameter, and direct truncated residuals at radii 16, 32, 64 and 128. Its opening classification correctly says that finite computations do not prove infinite convergence. Several later sentences nevertheless state infinite conclusions:

- Section5.5b says the exterior radius lies between 16 and 32.
- Section6 says direct residual evaluation confirms convergence at R>=32 and divergence at R=16.
- Section5.11 says the full logarithmic polynomial converges geometrically for every fixed radius with the same rate, based on a finite prefix and four sampled log radii.
- Section5.7 calls the nearest singularity modulus 1/L, where L is estimated from finite fits.

Each should be read and written as numerical evidence under its stated finite conditions. The infinite stored-rational continuation remains open. In particular, the observed growth at R=16 does not exclude a change after the computed order, and finite residual decay at R=32 does not supply a uniform all-order bound.

## Why finite evidence does not close the assertion

A finite scalar coefficient prefix is compatible both with an entire extension and with extensions of any specified finite radius, or radius zero. One can set all later coefficients to zero, set later coefficients to A^n, or set them to n!. Therefore the finite values alone cannot imply any of these analytic alternatives. The stationary recurrence restricts the allowable continuation, so these scalar sequences are not counterexamples to the IPM recurrence. They identify the missing logical ingredient: an all-order estimate using that recurrence. The Brjuno theorem supplies such an estimate at its admissible irrational parameters, but it does not settle the exact stored rational parameter after resonance.

Similarly, a sampled angular residual is a measurement of the chosen truncation. Even a rigorous uniform bound on finitely many such residuals would not prove convergence without a Cauchy estimate on the approximants or another existence argument. The independently certified finite residual enclosures remain valid within their own scope.

## Parameter-specific bound and implementation wording

Section5.8 compares the observed raw Candidate growth at its own stored delta with A<12725638. That constant is the Brjuno bound at the different exact value delta=1/sqrt(5). At the stored rational parameter, the independently certified finite-order bound is A_rat<13178350 and applies only before its exceptional order. A comparison across nearby parameters can be informative, but it must name both parameters and cannot apply the irrational bound to the stored rational recursion.

Section2 still describes the pure implementation as setting the resonant stream coefficient to zero and recording its numerator. The repaired implementation distinguishes exact compatibility, certified incompatibility and undecided intervals, and stops on the latter two cases rather than silently continuing. The report should describe the repaired behavior and retain the old behavior only when explaining explicitly labelled artificial continuations.

## Verdict and scope

The logical inference from the finite experiments to those infinite conclusions is unsupported. The infinite stored-rational convergence, exact full-series radius, and logarithmic convergence remain OPEN. No finite coefficient or residual number is refuted by this scope audit. The correct classification is NUMERICAL EVIDENCE for the observed prefixes and radii, with PROVED reserved for the separately established all-order theorems and finite exact identities.
