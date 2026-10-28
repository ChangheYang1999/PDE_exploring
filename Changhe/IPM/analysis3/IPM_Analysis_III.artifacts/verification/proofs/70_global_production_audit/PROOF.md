# Production coverage, directed aggregation and zero-box audit

## Claims and limits

The numerics team exports interval-derived floating endpoints for the
normalized exact modal background on1569 radial cells and64 angular
cells. This audit addresses which global conclusions follow from
these exports and whether the actual files satisfy the requirements.
It does not replace an independent original-data reconstruction of
all coefficient intervals. That additional task is proof 68.

Each finite float is interpreted as its exact dyadic value. If a
stored lower endpoint l_i is valid on a cell C_i, then min_i l_i is
valid on their union. Upper endpoints aggregate by maximum. These
steps involve comparisons of exact dyadic values, not new numerical
integration. A positive minimum over a proper subset of the domain
is not a global certificate.

## Complete cover

The radial cover is reconstructed directly from the original knot
vector, not from the exported decimal metadata: the1558 exact spline
spans, four finite inner cells at offsets1/2,1,2,4, five finite outer
cells at offsets1/2,1,2,4,8, and the two remaining half-lines. Every
adjacent finite endpoint agrees exactly. The angular intervals are
[i*pi/128,(i+1)*pi/128], i=0,...,63. Their union is the closed quadrant.
Parity extends all the scalar margins and norms to the whole plane.

Every applicable entry must be finite. A per-cell test of only the
first angular entry is insufficient. The two parts must have exactly
one owner for each radial cell and no owner overlap, and all merged
arrays must agree entrywise with that owner. Refined margins require
finite leaf bounds and complete leaf coverage. In this production,
if every NREF entry is1 and the refined values equal the unrefined
values, there is no hidden refinement tree to audit.

Weighted axis quantities are checked only on their stated half-line
of t. Every cell meeting t<=0 must carry the left bound, and every
cell meeting t>=0 must carry the right bound. A cell crossing0 must
carry both. Irrelevant NaN entries outside these sets do not signal
failure; missing or infinite entries on them do.

## Directed summaries and decimal display

Every summary extremum is recomputed from the full exported arrays.
A sum of upper endpoints is checked by exact rational addition.
The eventual decimal statement must be rounded outward again.
For example a lower bound3.037693... allows3.0376, not3.0377, and an
upper bound1075.515568... allows1075.516, not1075.5. Numerical
proximity is not an enclosure argument.

The identity residual n Q_n-P_n-P_n'/2 is a consistency check on the
Green representation. Its small radius does not justify deleting a
coefficient. The exact zero deletions at the inner endpoint require
the normalization identity of proof 04 and the modal Green identity
proved in proof 51. These exact identities are already independently
established.

## Additional zeros

For each cell with a strictly positive valid lower bound on |V|/r,
there is no zero with r>0. Each cell with nonpositive lower endpoint
must instead be contained in an independently verified uniqueness
patch or refined further. Proof 66 supplies the source rectangle
[p_- -1/2,p_+ +1/2] times[-1/2,1/2]. The exact polar containment
conditions are proved in proof 69 and are evaluated with Arb here.

The origin is handled by the positive inner half-line field bound
if that bound is valid. A collection of boxes with |V|/r<0.1 does
not automatically lie in the source rectangle. No geometric
conclusion is drawn from a small-value label alone.

## Acceptance

A successful result confirms the cover and the conditional global
aggregation of the exported bounds. The verifier records separately
whether each original-data interval computation has been reproduced,
and whether the zero boxes are all contained in the uniqueness patch.
These are logically different conclusions.
