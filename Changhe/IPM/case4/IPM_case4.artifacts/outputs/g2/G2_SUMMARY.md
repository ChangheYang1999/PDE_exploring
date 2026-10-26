# G2 evidence summary (generated 2026-10-24T10:49:39Z by bin/g2_summary_v3.py)

a step passes only if the runner verdict is ok, the step JSON passed field is true and no check record failed (SPEC v9.6 item 4)

Manifests: g2_v10 4b1f2091186da6da, g2_v11 50a41c858f0c4f49, g2_v4 6f0cf834c13b9bb3, g2_v5 a1bce3babc638565, g2_v6 aaaecdf9e8c02d15, g2_v7 479ac2b9e4357528, g2_v8 161f79cebc941422, g2_v9 64f8b0818b9b06d6

| manifest | step | runner verdict | guard success/rc | JSON passed | checks | failing checks | step passes | wall s | step JSON sha256 |
|---|---|---|---|---|---|---|---|---|---|
| g2_v4 | supplement | FAIL: step json passed is False (identity True required); failing checks: ['T2.6b_old_and_new_production_share_the_far_cancellation']; step json passed is False; failing checks: ['T2.6b_old_and_new_production_share_the_far_cancellation'] | True/0 | False | 12 | T2.6b_old_and_new_production_share_the_far_cancellation | NO (superseded) | 2599 | ceaa5c40e8c39a73 |
| g2_v4 | t0t1 | ok | True/0 | False | 58 | T0.5_low_evaluator_vs_old_core_matrices_envelope_rel_cl1.5000, T0.5_low_evaluator_cl_derivative_envelope_rel_cl2.5000, T0.5_low_evaluator_vs_old_core_matrices_envelope_rel_cl4.0000, T1.8_content_fields_bitwise_equal_after_json_normalization | NO (superseded) | 168 | f5a44573fd08172e |
| g2_v4 | t2 | ok | True/0 | True | 27 | - | PASS | 2237 | 0cb154bed1acba7f |
| g2_v4 | t26 | ok | True/0 | True | 152 | - | PASS | 1973 | 75321a92625c4a8a |
| g2_v4 | t27h | ok | True/0 | True | 20 | - | PASS | 1065 | 61cee98ae3ef2058 |
| g2_v4 | t27hx | ok | True/0 | True | 24 | - | PASS | 977 | ec023cce09f42957 |
| g2_v4 | t3 | ok | True/0 | True | 19 | - | PASS | 3516 | 2d729aa1bceed5be |
| g2_v5 | t0t1v2 | ok | True/0 | True | 58 | - | PASS | 210 | e8491e608f6f60ef |
| g2_v6 | t27hx2 | ok | True/0 | True | 24 | - | PASS | 1147 | c1b82a577cf54f10 |
| g2_v7 | t27hfloor | ok | True/0 | True | 10 | - | PASS | 422 | c42edaba373d52c9 |
| g2_v8 | kappa | FAIL: runner stopped: guard exit 2 (nonzero); chain stopped (rule 1) | None/None | None |  | - | NO (harness failure, no evidence) | 0 |  |
| g2_v9 | kappa | FAIL: runner stopped: guard exit 2 (nonzero); chain stopped (rule 1) | None/None | None |  | - | NO (harness failure, no evidence) | 0 |  |
| g2_v10 | kappa | ok | True/0 | True | 3 | - | PASS | 1057 | 7456adf666fd55ab |
| g2_v11 | supplement2 | ok | True/0 | True | 12 | - | PASS | 2769 | ce5d34be6d4b1531 |

## Notes

- farfield860.py and assess860.py are in the g2_v4 manifest but are NOT gated by G2 (lead checklist item 26); their v9.4 revisions (exact exponent grouping, F17) are pending files for the G3 manifest.
- T2.4 is a legacy order 20/24 origin overlap check; the production order 48 is gated by the T2.6c origin points, T2.7H and the section 13 monitor (order 48 vs 56).
- The SPEC v9.7 rounding calibration (production S_R per path, unrounded Rf_decimal, final rounding charged to the 2^-53 |R_f| term) is a postprocessing supplement before the G4 pilot manifest; it must cover the T2.6x, T2.6d and T3.6 R_f points or list the uncovered sets with a reason.
- g2_v4 t0t1 is superseded by g2_v5 t0t1v2 (identical library hashes).
- g2_v4 supplement (session s8) is superseded by g2_v11 supplement2 (identical library and closure hashes; lead strict read 10:45Z, review c4-lead/reviews/g2_v11_supplement_v2/REVIEW.md).
- g2_v8 and g2_v9 kappa are harness failures without evidence (guard exit 2 at step setup); the calibration evidence is g2_v10 kappa.

## Facts read from the step JSONs

```
{
 "T2.6d_remainder_block_nodes": {},
 "T2.7H_cl_values_with_floor_cases_over_300_needing_complete_sidecar": {
  "cl=2.0": 416,
  "cl=3.0": 562,
  "cl=10.0": 1323
 }
}
```

## Superseded steps

- g2_v4 t0t1 (passed=false: T0.5 old-route arbiter x3, T1.8 Decimal tails; harness scope per SPEC v9.6; superseded by g2_v5 t0t1v2, same library hashes)
- g2_v4 supplement (session s8): expected passed=false on T2.6b_old_and_new_production_share_the_far_cancellation (g2_supplement.py:129), whose premise predates the v7/v9 repairs (t26 gates the new R_f at e^32/e^44 at 6.0e-17 / 4.2e-17); superseded by tests/g2_supplement_v2.py (gate on the new R_f at e^32/e^44 <= 1e-11 plus a diagnostic without pass/fail) in a new supplement manifest (lead ruling 09:2xZ)
- g2_v8 kappa and g2_v9 kappa: harness failures (untranslated source-host epoch path; missing A_REF import), no result; replaced by g2_v10 kappa (tests/g2_kappa_v97d.py)

## Stated deviations (lead requests, SPEC v9.5 to v9.8)

- Files edited while a step ran (lead request 10:45Z). (a) During the g2_v10 kappa step, bin/g2_summary_v2.py (in the g2_v10 manifest as 2f4e95da99a107c7..., 9226 bytes) was edited to its present form c0baedcffa61f72a... (10372 bytes, listed as such in g2_v11); the g2_v10 bytes are not kept (no file in the lane carries the old hash). (b) During the g2_v11 supplement2 step, bin/run_g3_steps.sh (dd59bf980936b15b..., 8824 bytes in the g2_v11 manifest) and bin/runner_selftest_v5.py (629dd654d246052d..., 7524 bytes) were edited to 594450e9786e3f67... and a135485ccde3a1e6...; neither file was executed by the step (the step ran bin/run_g2_steps_v10.sh and tests/g2_supplement_v2.py); the before bytes are not kept (the lane holds no file with the old hashes). None of the three files is part of the library or the frozen 181 closure, so the library and closure hashes of g2_v10 and g2_v11 are unaffected. Rule adopted: no manifest-listed file is edited while any step runs; work goes to a renamed copy (this file bin/g2_summary_v3.py is the first such copy).
- T0.5 arbiter (v9.6): the 90-digit reference is rounded to binary64 before subtracting, a stated deviation of at most about 2^-52 of the envelope.
- T2.7H-X (v9.5): r_b is computed in binary64 from the correctly rounded exact delta, not in 50-digit arithmetic (at most about one ulp in the location of the added sampling point; at both binary64 neighbours of 3 the value is 9065.938286185034).
- FIELD_METHODS.cl_derivative_cancellation (frozen basis860 g2_v4) contains the false sentence "below 1e-40 for r >= 1e3": the stated absolute size 8 (j+1) u_ld / (c_l^2 R^2) is 4.3e-31 at j = 3, c_l = 2, r = 1e3; to be corrected at the next library manifest with the formula and its value, not a bound.
- bin/runner_selftest.sh does not include the verifier's two half-second mtime fixtures (before started_time, after finished_time); the verifier's 20-fixture run (c4-ver reviews/g2_runner_v3_*) covers them on the frozen runner.
- Metadata strings (basis860.VERSION, model860.Model860.version, origin orders in manifest text) are typed copies kept consistent by hand, not generated from the code constants (v9.5 item 2 asks for generated strings); the G2 audit checks them against ORIGIN_ORDER and R_SWITCH.
- T1.8 (v9.8): the floats poisson_max_abs and center_abs of hp_report_float_chart are binary64 records of exact-zero Decimal quantities and are gated by the 1e-60 rule instead of bitwise (flagged in the record).
- Policy and resources (lead 08:13Z): g2_v4 t3 was first run under g2_policy_v2 (family RSS ceiling 40,960 MiB) and was terminated by the guard at 68,070 MiB peak family RSS (sidecar outputs/g2/g2_v4/t3_rss_stop_sidecar.json); the relaunch (session s7) and the supplement (s8) run under g2_policy_v3.json, which raises only max_family_rss_mib to 163,840 (note outputs/g2_policy_v3.note.md). Before the G4 manifest the G3 benchmark records peak PSS (smaps_rollup) at the production worker count, or the guard reports PSS, so the G4 limit rests on a measurement.
- T2.7H-X2 (lead 08:13Z): the added points r_b, r_d, r_z are gated through added_points_worst_ratio_by_kind_and_field and added_points_worst_dcl_ratio_by_kind_and_field (12 c_l x 3 kinds x 7 fields, values and c_l derivatives, each at most 1e-11), read independently by the lead and the verifier; the aggregated check records in t27hx2.json take band maxima over base and added points together. From G3 on, each added point is gated per point.
- The step verdicts of the g2_v4 steps were produced by runner v3 (no step-JSON reading); their JSON passed fields and check records are read independently by this summary (and by the lead and verifier); g2_v5 used runner v4 and g2_v6 runner v5 (SPEC v9.10 strict verdict).
