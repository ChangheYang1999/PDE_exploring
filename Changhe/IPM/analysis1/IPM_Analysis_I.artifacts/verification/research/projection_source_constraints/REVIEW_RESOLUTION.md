# Mandatory refinement of the exact source-constraint statement

Written 2026-10-21T20:45:00.625512+00:00 after reading the complete first actual Opus5.5 review. This
supplement resolves the review within the intended restricted scope and adds
checks before the supplemental code is written.

1. C_NJ means the EXACT-ARITHMETIC INTERPRETATION of the frozen source recipe.
The binary64 matrix seen by an SVD is generally different. Every statement and
final verdict is about the explicit (frozen-column family, stored vector) pair.
The missing join/pickle-hash metadata in the new vectors is not repaired by
label matching. No claim about their historical producer execution is made.

2. The primary checker already raises ValueError on a nonzero alpha*s, missing
metadata identity, overlapping pieces or repeated endpoint. Any such failure
prevents checks.json from being created and voids that attempted certificate.
Its first completed run checked all515 contributing endpoint incidences and
7812 exact traces. There is no fallback interpretation. A supplemental checker
also reads Mh from the same old source-vector archive as the two joins and
lists every row's nonzero-entry count. A zero row must be listed as zero;
it cannot be silently dropped. No assertion that all rows are nonzero precedes
the data check.

3. For each matrix row define S=sum_i |x_i T_ri| exactly. If S>0 the number
eta=|(Cx)_r|/S lies in[0,1] by the triangle inequality and measures the degree
of cancellation in this specified pair. If S=0 then (Cx)_r=0 and we report
eta undefined, not zero. We will recompute S by Fraction and fmpq, and verify
eta by exact cross multiplication. This is a literal diagnostic, not a
roundoff-error theorem or distance-to-kernel estimate. All positive S and eta
will be supplied as exact rationals; no comparison to source join_residual.

4. The primary exact two-method computation imports or executes no producer
function. To verify the interpretation of the frozen conventions separately,
a supplemental diagnostic may compile ONLY the already inspected complete
pure piece_jet function and ExpPolyBasis class from their frozen source text,
with a namespace containing NumPy. It may compare finite manufactured examples
and actual endpoint values against independently computed expressions. No
producer module is imported. These floating checks are diagnostics and do not
replace the exact trace proof. This limited diagnostic supersedes the blanket
no-execution sentence of PROOF.md only for the supplemental convention test.
The common frozen pickle and source interpretation remain shared assumptions,
explicitly disclosed. Arithmetic, vector decoding and summation algorithms
remain distinct; they are not wholly independent mathematical definitions.

A manufactured signed example: on(-infinity,0), use exp(3t)(2+5t);
on[0,1), use 7-2t; outside, use0. The left-minus-right traces at0 are
value -5 and derivative18. At1 they are value5 and derivative-2.
For evaluation away from endpoints, compare values and derivatives to the
product rule with the correct anchor. A finite piece with alpha=2 ending at1
has alpha*s=2 and MUST be rejected by the rational-endpoint gate. Also test
an endpoint one binary64 ulp away from the chosen join: the source endpoint
matcher omits it, so our exact endpoint membership check must agree.

5. A nonzero source-only defect neither proves nor disproves continuity of the
full field. The KP/TAU/free-tail traces may cancel those of the function part.
Conversely a zero source-only defect would not establish that full continuity.
All physical trace, global norm, projection-error and inverse claims remain OPEN.

6. The review's general assertion about the p2/p4/p6 pickle hashes was not
verified in this topic and is not used. Its phrase that nonzero rounding defects
are essentially guaranteed is not a mathematical theorem; no such claim is
used. Hash equality here proves byte identity, with previously accepted results
used only through their stated scope.
