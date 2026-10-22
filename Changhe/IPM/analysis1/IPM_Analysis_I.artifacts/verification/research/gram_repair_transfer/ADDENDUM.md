# Scalar constants and the remaining conditioning hypothesis

Both arithmetic methods confirm the following strict rational upper
bounds. All columns are normalized by their original broken energy norm.

| Selected section | Columns N | Synthesis error eta | Gram spectral-norm error |
| --- | ---: | ---: | ---: |
| M16 radial subset with angular copies | 1440 | 3.20541113e-13 | 2.43273601e-11 |
| M24 radial subset with angular copies | 4488 | 1.720100378e-12 | 2.304677761e-10 |

Here eta bounds the norm of the difference between the two synthesis
maps from Euclidean coefficient space into the common BROKEN Hilbert
space. The original columns need not be in X. The second bound compares
the exact broken Gram with the true X Gram of the repaired columns.
It is an absolute bound, not a relative conditioning estimate.

If a rigorous lower bound G >= gamma I is later established for this
exact original normalized Gram, and eta < sqrt(gamma), PROOF.md gives
the relative bound with epsilon=eta/sqrt(gamma). A public upper bound
for eta can replace eta in this sufficient condition. Neither gamma
nor an exact whitening matrix is established here. Floating quadrature
or eigenvalues cannot supply the hypothesis without their own bounds.
These estimates concern only the selected radial subsets, not the full
M16 or M24 sections with additional central and tail columns.

Arb512 direct square roots are independently checked by exact integer
square roots at scale 10^35 and rational squaring of the stored Arb
endpoints. The Gram bound is evaluated both by a rational formula and
an exact repeated sum. All 93 topic132 pins are unchanged. The latter
supplies the individual strict repair bounds and exact continuity.

The Hilbert-space proof is standalone. The constants do not bind any
actual numerical matrix or historical calculation. No matrix of the
IPM operator, canonical velocity, normalization, global inverse or
nonlinear closure is transferred. All PDE endpoints remain OPEN.
