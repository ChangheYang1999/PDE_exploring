# Implementation review and corrections before the whole run

The first implementation review used actual Claude Opus5.5 and ended
2026-10-21T03:29:24Z. It independently reconstructed and accepted all
propagation signs, indices, tail denominators and comparisons. Its
statement that no artifact run existed described the submitted bundle;
the11-boundary smoke finished while the review was running. The original
source is retained as evidence/check_boundaries_v1.py, matching that
request and smoke. No whole boundary claim follows from the smoke.

The current partial status is OPEN_PARTIAL_DIAGNOSTIC. The previous
PASS_PARTIAL_ENGINE_LINKAGE label already stated its restricted scope,
but the new name makes it harder to mistake for full acceptance. Explicit
float64 dtype assertions were also added. The actual target artifact is
float64, so this does not alter its arithmetic. A fresh smoke will use
the final source. The final gate accepts only complete coverage.

The separate final auditor implements the K128 Arb1024 anchored Taylor
method from AUDIT_METHOD.md, reconstructs coverage and selected endpoint
comparisons, and checks overlap with the accepted old180 enclosures.
A separate replay checks whole-span stream digests for span0, span1557
and two further deterministic spans selected from the input hash. Span0
is necessarily among resumed rows whenever at least one completed span
is reused. The replay is diagnostic and uses the frozen complete-method
code; the third method remains independently implemented.

The review asks that the final auditor not trust self-reported counters.
It checks their exact required values and index ranges against the
partition, and freshly recomputes the selected entries and whole spans.
No finite sample can logically prove the omitted entries correct. The
full proof still rests on the two complete interval algorithms, their
source audit, pinned inputs and their recorded execution. Neither hashes,
counts, sampling nor a review vote substitutes for that computation.
A resumed record is part of the same pinned computation, with explicit
order, geometry and source checks; it is never accepted on a hash alone.

Manufactured tests are extended to translated midpoint polynomials and
backward J propagation. Nonfinite and exact endpoint classification
faults remain mandatory. Latest-process cache and tail metrics are
explicitly diagnostic, not aggregates claimed over a resumed run.
