# Preflight review gate and closure obligations

Actual Claude Opus5.5 completed the preflight review at
2026-10-21T04:02:29.479045+00:00, request78301dba-dfe9-4920-98c8-98b782c5e060.
It accepted readiness to queue, conditional on the preflight manifest pinning
the producer, independent auditor, replay, stage runner, shell wait, all three
diagnostic tests, the four proof and review documents, exact partition and
archive audit. The freeze script checks each named file and the current whole
review input bundles. The manifest is produced after this review, so its
contents must be verified by the script, not inferred from review acceptance.

Two clarifications to the review are recorded. The predetermined sample set
has192 hash-derived triples plus63 special triples, with duplicates removed
and explicitly checked by both programs. Its actual cardinality is255, not
the review's approximate213. These finite samples do not replace the full
16,242,720 coefficient computation. The independent auditor reports span0
(or the first selected span in a partial diagnostic) and both restart
neighbors. The replay program additionally includes the last and two
hash-selected spans. At final closure, cross-check the auditor's
replay_required_spans against replay.mandatory_restart_spans and independently
recompute the complete union, including every actual restart. The queue's
status by itself does not establish this cross-check.

The restart diagnostic had no next span because its one span was complete.
The two-neighbor case remains an actual-run closure obligation if any resume
occurs mid-run. The full producer is initially invoked with --resume even
when the output does not exist; this records a zero-row event and requires
span0. That event does not indicate an interrupted calculation.

The claim concerns exact child-left coordinates c_q. The floating tb is only
an enclosing coordinate box, not the expansion point. Downstream canonical
membership must use that exact convention. No global flow or a posteriori
IPM result is implied. Timeouts and missing footer or output audits remain
OPEN and require resumed work with preserved evidence.
