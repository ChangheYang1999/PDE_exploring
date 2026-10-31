# Snapshot gpu_v1 addendum 12 (test-only): checker v10 6924dad5699d1720 (V202 items 1 to 5); written 2026-10-29T08:14:33Z

g1_coverage_check.py e75ad8d910757c12 (v9, kept as .v9_e75ad8d9) -> 6924dad5699d1720 (v10). (1) A salvage record whose Richardson pair dictionary is present but not valid evidence (missing, non-finite or negative norms, wrong scale) is INVALID; there is no fallback to the recorded scalar. (2) Provenance (_source_gates_py) is set by the checker from the file each record came from (the record file's gates.py hash, or the companion file's), overwriting anything present in the input. (3) An add-on marked complete=false or partial=true, a per-Jacobian count that disagrees with its column records, or a column record that is missing, mislabelled or marked incomplete, is rejected (the (k) outcome is then INVALID with the reason). (4) The pair witness scale must equal the record's step scale, for the add-on (column_test step_scale) and for registered v5c and salvage pair witnesses. (5) The add-on's whole-column errors must equal per_group[step]['all'] at both steps. Outcomes on the eight records are unchanged from v9 (S01, S05 PASS everywhere; S09 registered FAIL, (k) FAIL on five small-amplitude columns, (k)+(j) PASS; manu registered FAIL, (k) FAIL on small-amplitude columns, (k)+(j) PASS, amended OPEN; v4 J_cw/J_c INVALID).

```
--- validation/g1_coverage_check.py.v9_e75ad8d9	2026-10-29 08:14:03.931769414 +0000
+++ validation/g1_coverage_check.py	2026-10-29 08:14:03.971769497 +0000
@@ -1,5 +1,9 @@
 #!/usr/bin/env python
-"""v9 (08:0xZ, V198 items 1-5): (1) the (k) decision is recomputed from the add-on's own column_test witnesses (two fresh steps 1e-2 s_j, 1e-3 s_j: finite
+"""v10 (08:1xZ, V202 items 1-5): (1) a salvage record whose pair dictionary is present but invalid is INVALID (no fallback to the scalar); (2) provenance
+(_source_gates_py) is set by the checker from the file each record came from, overwriting anything in the input; (3) an add-on marked complete=false, or whose
+per-Jacobian count disagrees with its columns, is rejected; (4) pair witness scale must equal the record's step scale (add-on and registered records);
+(5) add-on whole-column errors must equal per_group[step]['all'] at both steps.
+v9 (08:0xZ, V198 items 1-5): (1) the (k) decision is recomputed from the add-on's own column_test witnesses (two fresh steps 1e-2 s_j, 1e-3 s_j: finite
 error ladders, five-point and second-order rules at both steps, the pair Richardson from the witness norms with eligibility, active sets at the base and all
 eight stencil points for J_cw/J_c); the add-on must name the case, derive from the record (hash), be built on the record's gates.py, and cover every column
 that fails the registered rule in that Jacobian; otherwise the (k) outcome is INVALID; (2) with (k) requires exactly twenty distinct coefficient records that
@@ -82,7 +86,7 @@
     if rec.get("active_sets_identical") is not True:
         return False, "stored active_sets_identical not True"
     return True, ""
-def recompute_richardson_from_witnesses(allp, errs_by_label, tau):
+def recompute_richardson_from_witnesses(allp, errs_by_label, tau, expected_scale=None):
     """V193 item 4: every one of the four adjacent nominal pairs must be present with finite non-negative norm_diff_scaled, norm_d_scaled, norm_R_scaled, floor and
     a positive scale; the error is recomputed as norm_diff / max(norm_d, norm_R, floor); eligibility from the errors at the two steps. Returns (best, pair, ok, detail)."""
     if not isinstance(allp, dict) or sorted(allp.keys()) != sorted(PAIR_LABELS):
@@ -93,6 +97,8 @@
         vals = [w.get(k) for k in ("norm_diff_scaled", "norm_d_scaled", "norm_R_scaled", "floor")]
         if any(not fin(x) or x < 0 for x in vals) or not fin(w.get("scale")) or w.get("scale") <= 0:
             return None, None, False, f"pair {pl}: witness norms missing, non-finite, negative or scale invalid"
+        if expected_scale is not None and fin(expected_scale) and abs(w["scale"] - expected_scale) > 1e-12 * max(1.0, abs(expected_scale)):   # V202 item 4
+            return None, None, False, f"pair {pl}: witness scale {w['scale']} differs from the record's step scale {expected_scale}"
         nd_, nd, nR, F = vals
         r = nd_ / max(nd, nR, F, 1e-300)
         elig = fin(errs_by_label.get(a)) and fin(errs_by_label.get(b)) and errs_by_label[a] <= tau and errs_by_label[b] <= tau
@@ -124,13 +130,14 @@
     unknown conventions are INVALID. Returns (rich, pair, status, detail): status in PASS_EVIDENCE / INVALID."""
     conv = record_convention(rec); allp = container.get("richardson_all_pairs")
     if conv == "v5c":
-        rich, pair, okw, detail = recompute_richardson_from_witnesses(allp, errs_by_label, tau)
+        rich, pair, okw, detail = recompute_richardson_from_witnesses(allp, errs_by_label, tau, expected_scale=rec.get("step_scale", 1.0))
         return (rich, pair, "witnesses", detail) if okw else (None, None, "INVALID", detail)
     if conv == "salvage":
-        if isinstance(allp, dict):                                      # V198 item 4: complete norm witnesses first
-            rich, pair, okw, detail = recompute_richardson_from_witnesses(allp, errs_by_label, tau)
+        if isinstance(allp, dict):                                      # V198 item 4: complete norm witnesses first; V202 item 1: invalid witnesses are INVALID, no fallback
+            rich, pair, okw, detail = recompute_richardson_from_witnesses(allp, errs_by_label, tau, expected_scale=rec.get("step_scale", 1.0))
             if okw:
                 return rich, pair, "witnesses (salvage record with complete pair witnesses)", detail
+            return None, None, "INVALID", f"salvage record with a pair dictionary that is not valid evidence: {detail}"
         r = container.get("richardson", container.get("richardson_error"))
         if r is None:                                                   # the harness stores no Richardson value when no adjacent pair passes the second-order rule:
             return None, None, "salvage (no passing pair: numerical failure, no Richardson value)", None   # a numerical FAIL, not missing evidence
@@ -299,6 +306,15 @@
         return None, f"add-on gates.py hash {ah!r} is not the record's v5c harness {CURRENT_HARNESS['hash']!r}"
     if not isinstance(a.get("jacobians"), dict):
         return None, "add-on record has no jacobians"
+    if a.get("complete") is False or a.get("partial") is True:         # V202 item 3
+        return None, "add-on record marked incomplete"
+    for jn, jv in a["jacobians"].items():
+        cols = (jv or {}).get("columns")
+        if not isinstance(cols, dict) or (jv.get("n_columns_reevaluated") is not None and jv.get("n_columns_reevaluated") != len(cols)):
+            return None, f"add-on jacobian {jn}: column count disagrees with its records"
+        for ck, cr in cols.items():
+            if not isinstance(cr, dict) or str(cr.get("column")) != str(ck) or cr.get("complete") is False:
+                return None, f"add-on jacobian {jn}: column record {ck} missing, mislabelled or incomplete"
     return a, ""
 def expected_k_labels(scale):
     labs = {f"{0.0:+.1e}"}
@@ -329,6 +345,12 @@
             return dict(PASS=False, INVALID=True, reason=f"group {g} absent from the add-on witnesses")
     if sorted(e2.keys()) != sorted(K_STEPS) or sorted(e4.keys()) != sorted(K_STEPS) or any(not fin(v) or v < 0 for v in list(e2.values()) + list(e4.values())):
         return dict(PASS=False, INVALID=True, reason="two-step error ladders incomplete or non-finite")
+    if g is None:                                                      # V202 item 5: whole-column errors must equal per_group[step]['all']
+        pg = t.get("per_group") or {}
+        for l in K_STEPS:
+            a2 = ((pg.get(l) or {}).get("second_order") or {}).get("all"); a4 = ((pg.get(l) or {}).get("five_point") or {}).get("all")
+            if not fin(a2) or not fin(a4) or abs(a2 - e2[l]) > 1e-12 * max(1.0, e2[l]) or abs(a4 - e4[l]) > 1e-12 * max(1.0, e4[l]):
+                return dict(PASS=False, INVALID=True, reason=f"add-on whole-column errors contradict per_group['all'] at step {l}")
     if needs_active:
         a = t.get("active_sets")
         if not isinstance(a, dict) or not t.get("active_set_base_recorded") or set(a.keys()) != expected_k_labels(sc):
@@ -341,6 +363,8 @@
     w = allp[K_PAIR]; vals = [w.get(k) for k in ("norm_diff_scaled", "norm_d_scaled", "norm_R_scaled", "floor")]
     if any(not fin(x) or x < 0 for x in vals) or not fin(w.get("scale")) or w.get("scale") <= 0:
         return dict(PASS=False, INVALID=True, reason="pair witness norms missing, non-finite, negative or scale invalid")
+    if abs(w["scale"] - sc) > 1e-12 * max(1.0, sc):                      # V202 item 4
+        return dict(PASS=False, INVALID=True, reason=f"pair witness scale {w['scale']} differs from the column step scale {sc}")
     r = vals[0] / max(vals[1], vals[2], vals[3], 1e-300)
     both2 = all(e2[l] <= tau for l in K_STEPS); both4 = all(e4[l] <= tau for l in K_STEPS)
     ok = bool(both2 and both4 and r <= tau)
@@ -365,6 +389,16 @@
                 entries[k] = v
         report = dict(source=os.path.relpath(f), label=LABEL, threshold_small_amplitude=THRESH, min_coefficient_coverage=MIN_COEF, harness_gates_py=CURRENT_HARNESS["hash"],
                       harness_salvage=SALVAGE_HARNESS_HASHES.get(CURRENT_HARNESS["hash"], "v5c or later" if CURRENT_HARNESS["hash"] else "unknown"), cases={}, parameter_source={})
+        # V202 item 2: provenance is set here from the record file itself; any _source_gates_py in the input is overwritten
+        for cname, c in list(entries.items()):
+            for jac, pkey, ckey in JACS:
+                for v in (c.get(pkey) or {}).values():
+                    if isinstance(v, dict):
+                        v["_source_gates_py"] = CURRENT_HARNESS["hash"]
+                for e in ((c.get(ckey) or {}).get("results") or []):
+                    r = col_record(e, jac)
+                    if isinstance(r, dict):
+                        r["_source_gates_py"] = CURRENT_HARNESS["hash"]
         # v8: coefficient-only records take their parameter columns from the companion G1 record of the case
         for cname, c in list(entries.items()):
             if any(k in c for k in ("G1_Jf_param_columns", "G1_Jcw_param_columns", "G1_Jc_param_columns")):
```
