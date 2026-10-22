# Results of the literal row-density audit

2026-10-21T18:52:32.900562+00:00

All percentages below use the EARLIER saved value as denominator. Numbers in the next table are outward ceilings for the maximum absolute relative change of the five saved entries. These certify literal arithmetic only.

| Functional | ppc2 to4 | ppc4 to6 |
|---|---:|---:|
| L2 | 0.408190099737 | 0.219647341792 |
| L2q | 0.000221296947 | 2.4468378e-05 |
| H1 | 0.405370663772 | 0.217300594549 |
| H1q | 0.000323989111 | 6.7594531e-05 |

For the smallest entry, the unweighted L2 increases are 40.54482884 and 21.76144668 percent; H1 increases are 38.82682161 and 20.53447454 percent. These decimal percentages are approximations to the exact fractions in the evidence. The numerics 18:31 note saying 22 to29 percent per step does not describe these increases using the earlier value as denominator. Using the newer value produces different percentages and must be labeled separately.

There are 228 exact selected-array comparisons across twelve source NPZ files, totaling 2508480 payload bytes. The nineteen selected arrays, including A0, Bm, the column labels, trial scalars and partial Gram columns/diagonal, are byte-identical across all twelve archives. Three opaque metadata pickle files are byte-identical. Neither checker executes their pickle contents. Retained counts match the source report. No actual retained basis is saved here, so basis/subspace equality is not certified.

The bound 2.2e-4 in the two-digit descriptive note approximates the exact L2q maximum 0.0002212969460092758; similarly 3.2e-4 approximates the H1q maximum 0.0003239891105944552. If upper bounds are intended, use the outward ceilings in this table.

No spectral recomputation was performed. No singular minimum, continuous norm convergence, operator coercivity or IPM endpoint is certified.
