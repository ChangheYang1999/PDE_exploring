# Reading order

1. [REVIEW.md](REVIEW.md) gives the completed frr7/frr8 outcomes, exact comparison scope, source and timing limits, and the dated report correction.
2. [record_audit_final_001.json](record_audit_final_001.json) records all 158 inspected new and comparison games, full-specification joins, raw event arithmetic, complete canonical-history comparisons and exact missing-condition lists. [aggregate_records.py](aggregate_records.py) is the independent standard-library reader.
3. [supplementary_checks_final_001.json](supplementary_checks_final_001.json) reproduces every campaign summary table and checks policy entry-point identities. [supplementary_checks.py](supplementary_checks.py) performs those source/record checks.
4. [report_discrepancy_001.json](report_discrepancy_001.json) preserves the inspected +4470 report sentence and its +1250 raw-record correction. [root_report_discrepancy_001.json](root_report_discrepancy_001.json) is a distinct parent verification, not part of Astra's original assertion.
5. [af5_matrix_extension/INDEX.md](af5_matrix_extension/INDEX.md) leads through the standalone informal proof, exact retained matrix, input authentication and rational certificate. Its scope includes arbitrary stated completions of unplayed fortress edges, not presumed draws or full-game optimality.
6. [input_manifest_initial_001.json](input_manifest_initial_001.json), [input_manifest_frr7_complete_001.json](input_manifest_frr7_complete_001.json) and [input_manifest_final_001.json](input_manifest_final_001.json) preserve successively dated observations, including incomplete campaigns. Compressed content-addressed inputs retain original hashes and lengths; final outcomes do not overwrite partial evidence.
7. [seal_001.json](seal_001.json) binds the final review outputs and verifies all archive edges and current closed-record/source identities.

No policy, constructor, Engine, replay, existing game checker or new game is executed by these readers. Exact arithmetic on JSON is distinguished from an engine replay, a private-state audit and a proof of future behavior.
