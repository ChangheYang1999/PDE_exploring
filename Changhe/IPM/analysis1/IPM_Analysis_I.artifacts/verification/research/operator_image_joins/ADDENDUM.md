# Exact derivative traces of the continuous repairs

2026-10-21. Two rational engines agree on all 277 selected radial columns, all 2216 pieces, all 4432 first-derivative traces, and all 2493 joins. Every join is nonzero, including the two support joins of every column. The 4432 value traces remain exactly continuous as proved in topic132.

| Saved collection | Radial columns | Nonzero derivative joins | Single angular columns whose image is outside local H1 | Strict upper bound on every absolute t-derivative jump |
| --- | ---: | ---: | ---: | ---: |
| M16 | 90 | 810 | 1440 | 1.073359e-14 |
| M24 | 187 | 1683 | 4488 | 2.423895e-14 |

The decimals in the last column are exact rationals, rounded strictly upward from the exact maximum. They are upper bounds, not the assertion that every jump has that size. Each nonzero witness is stored exactly in evidence/compute.json, with its source column, radial endpoint, two derivative traces and jump. The theorem needs only a nonzero jump and supplies no numerical lower bound on an operator norm.

The first engine uses exact Fraction conversions of saved binary64 values and Horner evaluation of the repaired derivative polynomial. The second decodes all 24376 relevant binary64 numbers from sign, exponent and significand bits, evaluates original values and derivatives by direct monomial sums, reconstructs the affine repair from averaged original endpoint values, and compares every trace and jump. It does not use the first engine's corrections as its calculation. Both read only frozen local source metadata and verify their inherited hashes. Both include the zero exterior at support joins. Twenty-four signed rational examples additionally check the elementary secant identity; they do not certify a finite difference grid.

Thus the precisely defined topic132 repair gives continuous trial functions in X, but every selected single angular column has an image outside local weak H1 under the hypotheses in PROOF.md. A linear combination can cancel jumps, so this statement does not identify a numerical retained singular vector or bound the dimension of a kernel. These finite facts do not refute a floating matrix computation. To represent the linearized operator on this repaired class with H1 images, all first derivatives must match exactly at all radial joins, or a different rigorously specified domain and image norm must be used. The existing finite row values alone do not resolve this regularity requirement.
