# Review resolutions and strengthened source linkage

The first completed actual Opus5.5 review accepts the rank-nullity proof
and arithmetic. Its reported-count sentence mixes the section names with
NJ values. The exact saved counts, at each ppc2,4,6, are:

| NJ | Fminus | Fminus_noJ | free | free_noJ |
| --- | ---: | ---: | ---: | ---: |
| 0 | 1866 | 1866 | 1882 | 1882 |
| 1 | 1847 | 1847 | 1863 | 1863 |

All exceed the proved bounds, so the slip does not affect the theorem.
The code and JSON use the correct mapping; the review's prose is not
accepted as data.

The supplemental selector audit now explicitly reconstructs all four
source-checked selectors for both unique metadata sets. It checks the
actual J index set equals{0}, verifies containment of every one of the
1440/4488 selected coordinates, and checks the actual selector counts.
This is more than matching an overall dimension. No selected spline is
removed by the noJ condition.

The actual current M24 raw Mh.npy member was captured and decoded twice:
Mh=24. Only this tiny member is pinned. The NPY headers of Mat, KP, TAU
and tails were read without array values; their dimensions have5257
function columns, two scalar columns and24 free-tail columns with the
same row count. This certifies current captured shapes, not historical
execution, a retained count, or numerical matrix entries.

A separate audit verifies local piecewise smoothness of all50992 stored
pieces across the two full function-column sets and their KP/TAU radial
pieces: coefficients and exponential parameters are finite, intervals
have strictly ordered endpoints, and no NaN endpoints occur. Their finite
angular combinations have finite value traces at every selected circle.
No additional constraint rank is assumed for those extra columns.

The M16 historical raw scalar linkage remains OPEN and is not needed for
the finite dimension theorem: it uses the saved pieces' actual circles
and their exact local jumps. The source-defined column sets and saved
report counts are the precise comparison. Intended continuous B-splines,
actual Q, conforming reconstruction and all PDE endpoints remain OPEN.
