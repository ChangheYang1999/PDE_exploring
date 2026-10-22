# Source audit and first review resolutions

The current verdict is about the frozen-source mathematical constraint
matrix supplied with the captured M24 scalar endpoints and piece records.
The actual historical C, N and Q matrices are not stored or recomputed.
No claim of exact historical execution is made. Naming corresponding
files and observing unchanged size/mtime cannot establish that provenance.

The first actual Opus5.5 review accepted the exact jump and weak-gradient
argument but requested source links. The supplemental check now compares
the COMPLETE AST bodies of constraints and piece_jet with independently
stated reference functions. Only the piece_jet docstring is omitted. Thus:

* constraints has precisely its external tmin,t00 loops and no extra rows;
* tmin=float(d['tmin']), t00=float(d['t0']), cols=meta['cols'];
* piece_jet checks exact endpoint equality, otherwise continues to its final
  zero return. There is no tolerance window or extrapolation off support;
* the one C=constraints(NJ,sel) call feeds the immediately following SVD
  nullspace branch. The four exact section selectors and J-label exclusion
  all include column16 labelled sp8;
* the source reads the corresponding _cols.pkl name, and the producer
  writes (m,b.pieces,lab) metadata in that order;
* the documented angular factor and the actual single-mode angular
  coefficient construction give x^2y B(log r) for mode0.

NumPy separately rereads the two frozen .npy scalars that the second method
extracted and decoded using struct. Both agree exactly with the witness
endpoints. This closes the stated mathematical input binding, not a full
raw matrix certificate. The initial compute.json deliberately retains its
then-open scalar-linkage status; independent.json and source_check.json
supply the later result. They do not rewrite history.

Here X means the space of functions with weak gradient and norm squared

    integral (h^2+r^2 |grad h|^2) m(r)^(-2)
             (1+r^2/L^2)^(-3/2) dX,
    m(r)=(r/L)^3 (1+r^2/L^2)^((k-3)/2), L>0.

For finite positive r all weights are finite and positive, and on every
compact annulus they and their reciprocals are bounded. This proves the
local nondegeneracy used in PROOF.md without requiring any global endpoint
estimate. The conclusion would not apply to a space defined using broken
piecewise derivatives; the source's piecewise Gram remains a finite
matrix diagnostic in that distinct interpretation.

The all-column count tests all piece endpoints. They are internal to the
external annulus but may include each column's support boundary. Only the
named witness needs, and has, a jump strictly inside its support. We do
not infer from aggregate counts that every column has such a strict
interior jump. Intended continuous B-splines can be interpreted differently
from the stored rounded polynomial pieces, but that requires a separate
reconstruction and an error estimate for a rigorous spectrum statement.

The source-audit first attempt compared Store and Load AST contexts on the
section-loop target and failed before output. The corrected target lookup
uses its syntax, while all substantive AST comparisons stay complete.
Both this failure and the earlier absent-M16-raw attempt are preserved.
