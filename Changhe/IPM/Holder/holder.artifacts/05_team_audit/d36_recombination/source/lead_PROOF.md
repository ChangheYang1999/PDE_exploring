# Theorem 3.6 bounds for D_alpha from the direct Theorem 3.7 certificates

## Statement

Let D_alpha be the norm of R_1^2 = T_xx - I/2 on the real homogeneous Euclidean Holder seminorm (setup of the report,
Section 1). Then

| alpha | D_alpha upper | previous best (Table 1) |
|---|---:|---:|
| 1/5 | 4.1832609515 | 4.186079 (Theorem 3.5) |
| 99/100 | 42.6825968459 | 42.711662 (Theorem 3.5) |

The same recombination at 1/1000, 1/100, 1/20, 1/10 gives 637.4728288550, 64.5207793576, 13.6176426276, 7.2868514121,
which are weaker than the current Table 1 values (637.427298, 64.495459, 13.614688, 7.285961) and are not proposed.

## Proof

This is Theorem 3.6 of the report, unchanged:

    D_alpha <= 2^(1-alpha) A_alpha/alpha + 1/2 + sec(pi/(4m)) max_{0<=j<=m} (W_alpha + X_alpha + E_alpha)(phi_j),   m = 16,

with every term taken from data that is already accepted:

- W_alpha(phi_j): the middle-circle bin costs of the direct Theorem 3.7 certificates (scratch/table37/mid/, 512 bins,
  512 cells per half, plans chosen at the exponent), summed over the 512 bins with the exact-coverage and source-hash
  checks of table37.py, then lowered at each phase by the accepted middle-arc residual gain of the same certificates
  (V171, the verification work 08_improved_upper_bounds/middle_circle_transport/balanced_residual/table37/verification/). The script
  rechecks gain_j = max(0, old_source_lower_j - new_residual_upper_j) exactly. In Theorem 3.7 the same W_alpha(phi_j)
  enters the C bound; Theorem 3.6 allows any admissible middle plan, so W_alpha may be used there too.
- X_alpha(phi_j): the pole-disk (cross) integral of Theorem 3.4, from the verification work data/cross_disk_certificate.json
  (512 x 512 polar cells, 160 bits), the same file used for the accepted Theorem 3.6 values at 3/10, 1/2, 3/4, 9/10.
- E_alpha(phi_j): at each phase the smaller upper endpoint of two accepted exterior-circle certificates at the exponent,
  scratch/table37/far/far_<alpha>.json (used in the accepted direct Theorem 3.7 values) and the verification work
  data/far_circle_certificate_fine.json (used in the accepted Theorem 3.6 values). Each bounds the exterior functional
  at that phase, so their minimum does. At the worst phases of the two proposed values both choose the table37 file.

The phase argument needs the summed bound at each node to bound the norm of the full regular functional at that node;
the three terms are bounded at the same node phi_j before the maximum, as in the accepted middle-composite combination
(the verification work code/combine_middle_upper.py). The near term 2^(1-alpha) A_alpha/alpha + 1/2 is uniform in phase.

## Evaluation

combine_d36.py, 256-bit ball arithmetic; the decimals are upper endpoints rounded up at ten places. Output
results/d36.json with all source sha256. Worst phases: j = 11 at 1/5 and at 99/100. The pending column
pending_interpolated_D_upper uses the not yet accepted exact phase interpolation (the verification work phase_interpolation/PROOF.md)
and is not proposed here; it would lower the two values by about 3.6e-5 and 2.5e-4.
