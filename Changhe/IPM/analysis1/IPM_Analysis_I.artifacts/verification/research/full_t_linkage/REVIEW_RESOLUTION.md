# Code review correction and launch gates

Actual Opus5.5 code review, request edf9d8f4-858f-4535-90a7-7335c3379837,
completed2026-10-21T03:51:42Z. It correctly rejected the first producer's
hardcoded count512 for de Boor/Cox component equalities. There are eight
nodes and eight components, hence64 equalities per span. The revised
code increments an actual counter inside the component comparisons and
returns it with the polynomial. Saved rows require64. The first code and
its diagnostics are retained as v1 evidence; no full run used that code.
This accounting error did not alter the spline or interval formulas, but
the incorrect count was unacceptable execution evidence.

The manufactured matrix-versus-loop binomial comparison is labelled as a
consistency check. It is not an independent proof of the shift formula.
The test's exact parent polynomial is independently prescribed by the
analytic Bernstein identity in ADDENDUM; the separate Newton auditor is
also tested on independently prescribed polynomials and different nodes.

No production queue is launched before full output auditing and complete
span replay are implemented and tested. Every restart records the number
of saved spans, last saved span, next span, producer and header hashes in
an fsynced event file. The summary pins that file. Replay must include
span0 for a full run, both neighbors of every recorded restart, the final
span and two hash-selected spans. A diagnostic partial run replays only
selected spans, still including its first selected span. It remains OPEN.
The independent output auditor validates the events and reports the
mandatory replay set. A queue returncode is never a final verdict.
