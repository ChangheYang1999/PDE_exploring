# Owned artifact path audit

Declared 2026-10-31T19:08:38.927523+00:00, after the failed lexical scan and before its classified rerun.

Claim. The two matches in runs/validation/artifacts-mid-1905.json consist of one concrete project-root traceback and one generic path-rejection expression. Removing the root from that one traceback preserves every line and all failure information apart from that location. The frozen source guard identifies no concrete local file. A classified full rerun must find no other match.

Method and complete argument. Compare the pipeline log before and after the existing public_diagnostic transformation, require equal line counts and exactly line 250 changed, and retain hashes and byte counts. Parse the source guard as an assertion on a generator comparison and require its tuple to equal exactly the four generic forbidden roots. Pin the full source and line hashes. The second checker accepts this one source line only when both hashes still agree; it reports every other lexical match. The earlier failed scan is retained. The guard source stays unchanged because earlier declarations pin it.

Dependencies. check_owned_artifacts.py supplies the earlier lexical scan; check_owned_artifacts_v2.py performs the classified rerun; artifact_io.public_diagnostic performs the existing path redaction. verification/redaction.json records hashes. This is a filesystem hygiene result, not evidence about game performance.

Scope. The scan covers owned project text extensions and counts all owned file bytes plus the lane. Compressed records, files outside these roots and changes after the scan are outside the text claim. Generic root tokens are explicitly distinguished from concrete machine paths.
