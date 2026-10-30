# Integrity audit for selected final evidence records

## Claim and scope

The exact finite list in source/selection_v01.json identifies selected
N4 final-report evidence records by their ledger-cited SHA256 digest,
claim identifier and retained proof. This audit checks byte integrity
and local availability. It proves no new PDE theorem and repeats no
expensive integral or optimization. A passing integrity check preserves
an existing mathematical status; it cannot promote an OPEN condition.

For each selected root record, check its digest against the cited value.
Check each explicitly recorded local input in its inputs and own_inputs
maps. Check the local files listed in frozen_or_retained_sources against
their stored digests; for a gzip entry also hash the decoded byte stream
against its original digest. These are the documented direct dependency
edges of this integrity audit. Peer-only path labels are provenance,
not permission to execute or fetch files in another lane. The audit
reads only this lane and follows a symlink only when its resolved target
is also in this lane. A retained symlink is acceptable if its resolved
bytes match the recorded digest. No original file identity or historical
filesystem timestamp is inferred from that equality.

The checker inventories proof paths as retained current files, reporting
their hashes. When an existing evidence record already binds that proof,
the recorded binding is checked as an ordinary dependency edge. It does
not pretend that a newly observed digest is an earlier recorded digest.
Any mismatch, missing file, unsupported binding value or external local
path is reported explicitly. File integrity of unlisted transitive
inputs, mathematical soundness and fresh execution reproducibility are
outside this finite audit. The root record's own proof and original
verification describe the full mathematical dependency requirements.

## Finite verification argument

A digest comparison checks equality with the recorded digest, under the
usual SHA256 integrity assumption. For each finite edge, read the actual
bytes, compute the digest and compare it. If all edges pass, the assertion
that every listed local edge matches is true by exhaustive enumeration.
Failure of an edge establishes only that the corresponding current local
binding is unavailable or mismatched; it is not itself a mathematical
counterexample. Stored and decoded gzip digests have distinct meanings
and must not be interchanged. A streaming decode hashes the full decoded
stream, not its prefix. Repeated paths may share a cached digest only if
the filesystem signature is unchanged before and after the audit.

The result records every checked edge, any errors and all source hashes,
with actual start/end times. The audit runs serially with the long
production job paused, then resumes that job even if an error occurs.
All accepted original outputs remain immutable.
