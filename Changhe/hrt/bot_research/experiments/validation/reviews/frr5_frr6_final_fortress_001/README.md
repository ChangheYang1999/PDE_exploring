# Final fortress extension review

Read in this order:

1. [REVIEW.md](REVIEW.md) gives the completed frr5/frr6 findings, exact conditions, source limits and reporting advice. It is written after the final campaign finishes.
2. [INSPECTION_001.md](INSPECTION_001.md) preserves the earlier dated inspection, when frr6 was incomplete. Its partial counts are historical snapshots, not the final result.
3. [record_audit_final.json](record_audit_final.json) records the full-specification joins, complete raw-record arithmetic checks, per-condition outcomes and v46/v48 canonical-history comparisons. [aggregate_records.py](aggregate_records.py) is the independent stdlib reader.
4. [supplementary_checks_final.json](supplementary_checks_final.json) reproduces summary tables, compares entry-point bytes and checks exact finite-matrix rows. [supplementary_checks.py](supplementary_checks.py) implements those record-only checks.
5. [finite_matrix_extension/PROOF.md](finite_matrix_extension/PROOF.md) proves zero equilibrium weight for both added fortress rows for any unplayed mutual entry in a skew-symmetric matrix completion. [The exact row certificate](finite_matrix_extension/verification/row_certificate.json) binds the independently joined source rows and rational witness. The proof states its dependence on the earlier frr1 theorem and its empirical provenance limits.
6. [input_manifest_initial.json](input_manifest_initial.json), [input_manifest_supporting.json](input_manifest_supporting.json) and [input_manifest_final.json](input_manifest_final.json) bind exact compressed source, report and record inputs. The `inputs/` archives are content addressed; manifests give both compressed and original SHA256 identities and lengths. Earlier snapshots are retained unchanged.
7. [source_diff_v46_v48.patch](source_diff_v46_v48.patch) shows the actual implementation differences. [seal_001.json](seal_001.json) binds the review outputs and final archive/source rechecks.

No policy, game engine, project checker, simulation, server or new experiment is run by this review. The reader scripts use only the Python standard library on retained artifacts. An arithmetic consistency check is not an independent engine replay or proof of uninterrupted historical source immutability.
