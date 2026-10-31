# Independent checks (subset)

This folder is a subset of the independent verifier's archive, which held 15,616 files (349 MB; manifest SHA-256
0837f4a23bd9fa348002d3ab9e2750907e2bf1aa3fe922796ee41ac4214a58a6) and is not published in full because of its size.
The subset keeps machine-readable records, code and proofs; it omits arrays, compressed originals, source diffs and
files above 512 KB.

- records/final_outcome_review_v1, records/final_outcome_signoff_v1 : the review and the sign-off of the final
  outcome category (C with qualifier D for the P1 and F2 ends; P3 C, its D conditional on the saved factors).
- records/phase_iv_cohorts, records/phase_iv_plan_v3, records/final_operation_observations : the frozen cohort,
  the registered plan and the observed operations of the final test (section 8 of the report).
- records/P1_segment*_holdout_v1.json, records/P1_segment4_*, records/P1_s4_widths_v1, records/F2m3_*,
  records/P3_matched_*, records/P3_pair_accounting_v1, records/P2_s6_late_holdout_review_v1, records/P2s6_late_freeze_v1,
  records/F1m3_*, records/P3_origin_v1 : independent holdout recomputations, freezes, widths, pair comparisons and
  origin checks of the end states quoted in the report.
- code/src : the independent field, pressure and residual code.
- research/ : the mathematical arguments used by the checks (each topic states hypotheses and scope in its
  PROOF.md) with their verification notes. These are informal arguments; no formal certification was performed.
- records/inputs/P3_INITIAL_raw_v1 : the decoded coefficient vector of the P3 initial state with its checkpoint hash.
- derivative_standard.md : the derivative-validation standard registered before any production result.
- final_result_review.md : the verifier's final review of the results.

Scripts copied inside the records refer to the original locations as RUN_ROOT/verifier and RUN_ROOT/numerics (see
../README.md) and need the complete archive and the campaign data to rerun. Relative links in some notes point to
records of the complete archive that are not in this subset.
