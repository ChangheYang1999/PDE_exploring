# Addendum v14 (2026-10-29T09:10:32Z): checker v12 candidate 26f54476e947177e (validation/g1_coverage_check.py), ACCEPTED as the deciding checker (lead 09:28Z item 1 after V224: 103 controls, diff limited to the expected-scale argument, release outputs identical)

Finding (numerics, 09:0xZ, on the first 3.1 full-battery records of harness v5c 5f4079926f1c757b: S01_shift_a, manu_small_omega; both at omega 0.3):
checker v11 marks the physical omega parameter column INVALID with "pair 1e-03->1e-04: witness scale 1.0 differs from the record's step scale 0.3".
The harness v5c (V190, V192) scales the physical-omega STEP by omega (step_scale 0.3) but judges the derivative in physical units
(derivative_scale 1.0; gates.py best_richardson passes dscale into richardson_witness, so the witness field "scale" is the derivative scale).
Checker v11 rule (4) compared the witness scale with the step scale, which coincide for every column except physical omega at omega < 1.
The release cases' parameter columns (S05_own, S09_own at omega 0.3) came from the harness-v4 G1v4 records through the re-judgement path, so the
rule never met a v5c physical-omega record before. Effect of the rule: a false INVALID (conservative), never a false PASS.

Change (two lines, both calls of recompute_richardson_from_witnesses in the registered-record path): expected_scale = rec.get("derivative_scale",
rec.get("step_scale", 1.0)) instead of rec.get("step_scale", 1.0). For records without a derivative_scale field (harness v3/v4) the behaviour is
unchanged. The (k) add-on path (coefficient columns; witness scale = step scale = derivative scale) is unchanged.

Status: candidate. Outputs of v12 are labelled "checker v12 candidate" until the lead accepts it and the verifier replays its controls; the
release basis (four cases, checker v11) is unaffected. Backup validation/g1_coverage_check.py.v11_1914b39a.

Status update 2026-10-29T09:31:58Z: accepted as deciding (lead 09:28:39Z, V224). The 'candidate' tag is dropped; the logs validation/logs/checker_v12cand_*.log keep their names.
