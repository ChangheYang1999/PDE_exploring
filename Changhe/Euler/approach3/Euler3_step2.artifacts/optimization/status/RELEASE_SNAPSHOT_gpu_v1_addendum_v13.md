# Snapshot gpu_v1 addendum 13 (test-only): checker v11 1914b39adb2ffd63 (V205); written 2026-10-29T08:22:46Z

g1_coverage_check.py 6924dad5699d1720 (v10, kept as .v10_6924dad5) -> 1914b39adb2ffd63 (v11): a (k) add-on file that is present but rejected by load_addon (hash mismatch, wrong case, wrong harness, incomplete) makes the (k) and (k)+(j) outcomes INVALID with the reason listed in invalid_evidence; only a missing file leaves (k) equal to the registered outcome. Outcomes of the four combined v5c records are unchanged. Side effect, correct and conservative: on the four v4 records (gates_gpu_v1_<case>_G1v4.json, gates_gpu_v1_S05_own.json, gates_gpu_v1_manu_large_omega.json) the (k) and (k)+(j) outcomes are now INVALID because the case's add-on file derives from the v5c record of the same case (hash mismatch); their registered and amended outcomes are unchanged and the release inputs are the combined v5c coverage files.

```
--- validation/g1_coverage_check.py.v10_6924dad5	2026-10-29 08:22:12.702767391 +0000
+++ validation/g1_coverage_check.py	2026-10-29 08:22:12.742767469 +0000
@@ -1,5 +1,6 @@
 #!/usr/bin/env python
-"""v10 (08:1xZ, V202 items 1-5): (1) a salvage record whose pair dictionary is present but invalid is INVALID (no fallback to the scalar); (2) provenance
+"""v11 (08:2xZ, V205): a (k) add-on file that is present but rejected (hash, case, harness, completeness) makes the (k) and (k)+(j) outcomes INVALID with the reason; only a missing file leaves (k) equal to the registered outcome.
+v10 (08:1xZ, V202 items 1-5): (1) a salvage record whose pair dictionary is present but invalid is INVALID (no fallback to the scalar); (2) provenance
 (_source_gates_py) is set by the checker from the file each record came from, overwriting anything in the input; (3) an add-on marked complete=false, or whose
 per-Jacobian count disagrees with its columns, is rejected; (4) pair witness scale must equal the record's step scale (add-on and registered records);
 (5) add-on whole-column errors must equal per_group[step]['all'] at both steps.
@@ -503,6 +504,8 @@
                 # ---- specification v1.18 3.6 (k): registered outcome with the post-result step rule, and with (k) and (j) together
                 addon, addon_note = load_addon(cname, f)
                 K_CTX["needs_active"] = needs_active; K_CTX["invalid"] = []
+                if addon is None and addon_note != "no (k) add-on record":        # V205: a present but rejected add-on makes the (k) outcomes INVALID, never "as absent"
+                    K_CTX["invalid"].append("add-on present but rejected: " + addon_note)
                 k_cols = {}; k_fail = []; k_ratios = {}; reg_failing_cols = []
                 for e in cc:
                     r = col_record(e, jac); k = col_id(e, jac)
```
