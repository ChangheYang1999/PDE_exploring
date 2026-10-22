# Finite rank result and comparison scope

All hypotheses of PROOF.md pass on the two unique frozen metadata sets
from topic130. There are90 selected radial splines for M16 and187 for M24.
Their first internal breakpoints are distinct. Exact rational Horner checks
4005 and17391 upper-triangle zeros respectively. Every diagonal is nonzero.
The independently computed determinants modulo prime1000000007 are
549419639 for M16 and248484184 for M24. Primality was checked by trial
division through its integer square root. Direct bit-decoded rational
power sums match every exact diagonal. All5928 selected mode copies have
identical per-piece structure and endpoint/coefficient bits.

The jump map has rank at least1440 for M16 and4488 for M24. Consequently:

| encoded span | M16 conforming dimension at most | M24 at most |
| --- | ---: | ---: |
| Fminus | 515 | 771 |
| Fminus_noJ | 514 | 770 |
| free | 531 | 795 |
| free_noJ | 530 | 794 |

These are upper bounds, not asserted exact dimensions. No external-join
constraint, SVD rank threshold, eigenvalue truncation, or numerical Q rank
is required for them. Extra KP, TAU and free-tail columns can add at most
their number of coefficient dimensions. Their own jumps need not be known.
All actual functions are finite piecewise smooth near the selected circles.

The six saved H1m JSON reports for M16/s16, ppc2/4/6, NJ0/1 have retained
counts exceeding the corresponding upper bound in all four sections.
For example, Fminus reports1866 columns at NJ0 versus upper bound515.
Thus it is impossible for that many functions INSIDE THE EXACT ENCODED
SPAN to be an X-orthonormal list. If an actual floating list of that length
lies in X, it must be dependent. This does not determine which columns
are nonconforming or dependent, and it does not numerically refute any
matrix SVD. The reported JSON values are finite data, not an authenticated
historical execution. There is no M24 retained-count comparison yet.

The argument applies to the saved polynomial-piece functions. It does not
apply to an intended, exactly continuous B-spline space, or a separately
constructed conforming approximation to the computed list. Such a repair
may be tiny pointwise, but its quantitative effect on a rigorous operator
or spectral statement needs proved bounds. Neither that repair nor any
PDE endpoint has been established.

Methods are independent in the arithmetic that certifies rank: rational
Horner matrix entries versus structural exact zeros and modular dyadic
evaluation, with independent direct rational power sums as a crosscheck.
The independent reader imports no NumPy. A supplemental structured-copy
audit explicitly checks piece and coefficient counts before comparing
bits, strengthening the concatenated-byte comparison without altering
its earlier output. The full list of pivot fractions and column indices
is in both evidence/compute.json and evidence/independent.json.
