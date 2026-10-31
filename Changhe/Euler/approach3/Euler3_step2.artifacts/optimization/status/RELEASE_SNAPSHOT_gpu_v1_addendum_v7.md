# Snapshot gpu_v1 addendum 7 (test-only, V193): checker v5; written 2026-10-29T07:28:33Z

g1_coverage_check.py b9e297dd37a49a49 (v4, kept as .v4_b9e297dd) -> ed1899e4248c9f2c (v5): (1) ids_match in the amended aggregate; (2) closure, gauge and far_anchor_block required for every battery case besides the three radial groups (present in the record, not only in the union); (3) the raw active-set records must carry the exact base label and the twenty stencil labels of the recorded step scale and agree; (4) every Richardson error recomputed from the witness norms (norm_diff_scaled, norm_d_scaled, norm_R_scaled, floor, positive scale) for the four adjacent nominal pairs, eligibility from the errors at those steps; stored values are comparisons; pre-v5c records use the recorded value, labelled; (5) complete finite non-negative whole-column ladders equal to per_group[step][kind]['all'] required; missing data INVALID.

```
--- validation/g1_coverage_check.py.v4_b9e297dd	2026-10-29 07:28:02.005982915 +0000
+++ validation/g1_coverage_check.py	2026-10-29 07:28:02.045983004 +0000
@@ -1,5 +1,10 @@
 #!/usr/bin/env python
-"""v4 (07:2xZ, V192): (1) the twenty coefficient ids are matched against the case's drawn columns (G1_coefficient_columns_drawn) and the per-Jacobian column lists;
+"""v5 (07:3xZ, V193): (1) ids_match is part of the amended aggregate too; (2) the closure, gauge and far-anchor-block groups are required for every battery case
+in addition to the three radial groups; (3) the raw active-set records must carry the exact base label and the twenty stencil labels (+-h s, +-2h s for the
+five nominal steps at the recorded step scale) and their signatures must agree; (4) every Richardson error is recomputed from the witness norms
+(norm_diff_scaled, norm_d_scaled, norm_R_scaled, floor, scale) for the four adjacent nominal pairs and each pair's eligibility from the errors at those steps;
+stored values are comparisons only; (5) the whole-column ladders must be complete, finite, non-negative and equal to per_group[step][kind]['all'].
+v4 (07:2xZ, V192): (1) the twenty coefficient ids are matched against the case's drawn columns (G1_coefficient_columns_drawn) and the per-Jacobian column lists;
 (2) the registered row groups (near_origin, core_intermediate, far, far_anchor_block) and the whole-column 'all' witnesses are required, with the five nominal
 step labels, finite non-negative norms and errors and valid scales; (3) the raw base and stencil active records are validated (all equal) before
 active_sets_identical is trusted (J_f: frozen convention); (4) the second-order, five-point and Richardson decisions are RECOMPUTED from the recorded errors and
@@ -30,48 +35,92 @@
     return entry.get("column", col_record(entry, jac).get("column"))
 N_STEPS = 5; N_COEF = 20; TAU_ALL = 1e-6; TAU_GROUP = 1e-5
 STEP_LABELS = ["1e-03", "1e-04", "1e-05", "1e-06", "1e-07"]
-REQUIRED_GROUPS = ["near_origin(r<=0.1R0)", "core_intermediate", "far(r>256R0)"]      # far_anchor_block is required when the case has anchors (it does for every battery case)
+REQUIRED_GROUPS = ["near_origin(r<=0.1R0)", "core_intermediate", "far(r>256R0)", "far_anchor_block", "closure", "gauge"]      # every registered battery case has anchors, closure rows and the gauge row (V193 item 2)
+PAIR_LABELS = [f"{STEP_LABELS[i]}->{STEP_LABELS[i + 1]}" for i in range(len(STEP_LABELS) - 1)]
+def expected_stencil_labels(scale):
+    """The labels column_test writes: f'{t:+.1e}' for t = 0 and t = +-h s, +-2h s over the five nominal steps (V193 item 3)."""
+    labs = {f"{0.0:+.1e}"}
+    for l in STEP_LABELS:
+        h = float(l) * scale
+        for t in (h, -h, 2 * h, -2 * h):
+            labs.add(f"{t:+.1e}")
+    return labs
 def active_sets_valid(rec, needs_active):
-    """V192 item 3: the raw base and stencil active records must exist and be identical (recomputed), and the base flag must be set; J_f uses the frozen convention."""
+    """V192 item 3 / V193 item 3: the raw base and the twenty stencil active records (exact labels for the recorded step scale) must exist and agree (recomputed);
+    the base flag must be set; J_f uses the declared frozen convention."""
     if not needs_active:
         return True, "frozen-weight convention (no changing active set)"
-    a = rec.get("active_sets")
-    if not isinstance(a, dict) or len(a) < 2 * N_STEPS + 1 or not rec.get("active_set_base_recorded"):
+    a = rec.get("active_sets"); sc = rec.get("step_scale", 1.0)
+    if not isinstance(a, dict) or not rec.get("active_set_base_recorded"):
         return False, "raw active-set records or the base record missing"
+    exp = expected_stencil_labels(sc)
+    if set(a.keys()) != exp:
+        return False, f"active-set labels do not match the stencil of the recorded step scale (have {len(a)}, expected {len(exp)}; missing {sorted(exp - set(a.keys()))[:4]})"
     keys = set(json.dumps(v, sort_keys=True) for v in a.values())
     if len(keys) != 1:
         return False, "active sets differ among the stencil points and the base"
     if rec.get("active_sets_identical") is not True:
         return False, "stored active_sets_identical not True"
     return True, ""
+def recompute_richardson_from_witnesses(allp, errs_by_label, tau):
+    """V193 item 4: every one of the four adjacent nominal pairs must be present with finite non-negative norm_diff_scaled, norm_d_scaled, norm_R_scaled, floor and
+    a positive scale; the error is recomputed as norm_diff / max(norm_d, norm_R, floor); eligibility from the errors at the two steps. Returns (best, pair, ok, detail)."""
+    if not isinstance(allp, dict) or sorted(allp.keys()) != sorted(PAIR_LABELS):
+        return None, None, False, "pair witnesses missing or mislabelled"
+    best = None; best_pair = None; detail = {}
+    for pl in PAIR_LABELS:
+        w = allp[pl]; a, b = pl.split("->")
+        vals = [w.get(k) for k in ("norm_diff_scaled", "norm_d_scaled", "norm_R_scaled", "floor")]
+        if any(not fin(x) or x < 0 for x in vals) or not fin(w.get("scale")) or w.get("scale") <= 0:
+            return None, None, False, f"pair {pl}: witness norms missing, non-finite, negative or scale invalid"
+        nd_, nd, nR, F = vals
+        r = nd_ / max(nd, nR, F, 1e-300)
+        elig = fin(errs_by_label.get(a)) and fin(errs_by_label.get(b)) and errs_by_label[a] <= tau and errs_by_label[b] <= tau
+        detail[pl] = dict(recomputed=r, stored=w.get("richardson_error"), eligible=elig, stored_eligible=w.get("pair_passes_second_order"))
+        if elig and (best is None or r < best):
+            best, best_pair = r, pl
+    return best, best_pair, True, detail
 def consecutive_pass(errs_by_label, tau):
     labs = [l for l in STEP_LABELS if l in errs_by_label]
     return any(fin(errs_by_label[labs[i]]) and fin(errs_by_label[labs[i + 1]]) and errs_by_label[labs[i]] <= tau and errs_by_label[labs[i + 1]] <= tau for i in range(len(labs) - 1))
+def ladder_ok(errs):
+    return isinstance(errs, dict) and sorted(errs.keys()) == sorted(STEP_LABELS) and all(fin(v) and v >= 0 for v in errs.values())
 def recompute_whole(rec, tau=TAU_ALL):
-    """V192 item 4: whole-column decision recomputed from the recorded errors and Richardson pair witnesses (v5 records: richardson_all_pairs; v4: richardson_error)."""
+    """V192/V193 item 4-5: whole-column decision recomputed from complete, finite, non-negative error ladders (equal to per_group[step][kind]['all']) and from the
+    Richardson pair witnesses (v5c records: witness norms; v4 records: the recorded value, labelled as such). Missing data -> not a pass (INVALID at the schema)."""
     e2 = rec.get("errors") or rec.get("errors_second_order") or {}; e4 = rec.get("errors_five_point") or {}
+    if not (ladder_ok(e2) and ladder_ok(e4)):
+        return dict(PASS=False, reason="whole-column error ladder incomplete or non-finite", stored_PASS=rec.get("PASS"), agrees_with_stored=False)
+    pg = rec.get("per_group") or {}
+    for l in STEP_LABELS:
+        if l in pg and (abs((pg[l].get("second_order") or {}).get("all", float("nan")) - e2[l]) > 1e-12 * max(1.0, e2[l]) or abs((pg[l].get("five_point") or {}).get("all", float("nan")) - e4[l]) > 1e-12 * max(1.0, e4[l])):
+            return dict(PASS=False, reason=f"whole-column errors contradict per_group['all'] at step {l}", stored_PASS=rec.get("PASS"), agrees_with_stored=False)
     p2 = consecutive_pass(e2, tau); p4 = consecutive_pass(e4, tau)
-    allp = rec.get("richardson_all_pairs")
-    if isinstance(allp, dict) and allp:
-        rs = [v["richardson_error"] for v in allp.values() if v.get("pair_passes_second_order") and fin(v.get("richardson_error"))]
-        rich = min(rs) if rs else None
+    allp = rec.get("richardson_all_pairs"); source = "v5c witnesses"
+    if isinstance(allp, dict) and allp and all(isinstance(v, dict) and "norm_diff_scaled" in v for v in allp.values()):
+        rich, pair, okw, detail = recompute_richardson_from_witnesses(allp, e2, tau)
+        if not okw:
+            return dict(PASS=False, reason=detail, stored_PASS=rec.get("PASS"), agrees_with_stored=False)
     else:
-        rich = rec.get("richardson", rec.get("richardson_error"))
+        rich = rec.get("richardson", rec.get("richardson_error")); pair = rec.get("richardson_pair"); detail = None; source = "recorded Richardson value (pre-v5c record; no witness norms)"
     ok = bool(p2 and p4 and fin(rich) and rich <= tau)
-    return dict(pass_second_order=p2, pass_five_point=p4, richardson=rich, PASS=ok, stored_PASS=rec.get("PASS"), agrees_with_stored=(ok == bool(rec.get("PASS"))))
+    return dict(pass_second_order=p2, pass_five_point=p4, richardson=rich, richardson_pair=pair, richardson_source=source, pairs=detail, PASS=ok, stored_PASS=rec.get("PASS"), agrees_with_stored=(ok == bool(rec.get("PASS"))))
 def recompute_group(rec, g, tau=TAU_GROUP):
     pg = rec.get("per_group") or {}
     e2 = {h: (v.get("second_order") or {}).get(g) for h, v in pg.items()}; e4 = {h: (v.get("five_point") or {}).get(g) for h, v in pg.items()}
+    if not (ladder_ok(e2) and ladder_ok(e4)):
+        return dict(PASS=False, reason="group error ladder incomplete or non-finite", stored_PASS=((rec.get("group_pass") or {}).get(g) or {}).get("PASS"), agrees_with_stored=False)
     p2 = consecutive_pass(e2, tau); p4 = consecutive_pass(e4, tau)
     gp = (rec.get("group_pass") or {}).get(g) or {}
-    allp = gp.get("richardson_all_pairs")
-    if isinstance(allp, dict) and allp:
-        rs = [v["richardson_error"] for v in allp.values() if v.get("pair_passes_second_order") and fin(v.get("richardson_error"))]
-        rich = min(rs) if rs else None
+    allp = gp.get("richardson_all_pairs"); source = "v5c witnesses"
+    if isinstance(allp, dict) and allp and all(isinstance(v, dict) and "norm_diff_scaled" in v for v in allp.values()):
+        rich, pair, okw, detail = recompute_richardson_from_witnesses(allp, e2, tau)
+        if not okw:
+            return dict(PASS=False, reason=detail, stored_PASS=gp.get("PASS"), agrees_with_stored=False)
     else:
-        rich = gp.get("richardson_error")
+        rich = gp.get("richardson_error"); pair = gp.get("richardson_pair"); detail = None; source = "recorded Richardson value (pre-v5c record)"
     ok = bool(p2 and p4 and fin(rich) and rich <= tau)
-    return dict(pass_second_order=p2, pass_five_point=p4, richardson=rich, PASS=ok, stored_PASS=gp.get("PASS"), agrees_with_stored=(ok == bool(gp.get("PASS"))))
+    return dict(pass_second_order=p2, pass_five_point=p4, richardson=rich, richardson_pair=pair, richardson_source=source, PASS=ok, stored_PASS=gp.get("PASS"), agrees_with_stored=(ok == bool(gp.get("PASS"))))
 def record_complete(rec, groups, needs_active):
     """Completeness schema (V190, V192): the five nominal steps, the registered groups and the whole column with finite non-negative norms and errors, valid scales,
     decisions present, and (for J_cw / J_c) validated identical active sets including the base. Returns (ok, reason)."""
@@ -80,8 +129,10 @@
     pg = rec.get("per_group")
     if not isinstance(pg, dict) or sorted(pg.keys()) != sorted(STEP_LABELS):
         return False, f"ladder step labels {sorted(pg.keys()) if isinstance(pg, dict) else None} (need {STEP_LABELS})"
+    pg0 = pg[STEP_LABELS[0]] if isinstance(pg, dict) and STEP_LABELS[0] in pg else {}
+    present = set((pg0.get("second_order") or {}).keys())
     for g in REQUIRED_GROUPS + ["all"]:
-        if g not in groups and g != "all":
+        if g not in present:
             return False, f"registered group {g} absent from the record"
     sc = rec.get("step_scale", 1.0); dsc = rec.get("derivative_scale", sc)
     if not (fin(sc) and sc > 0 and fin(dsc) and dsc > 0):
@@ -239,8 +290,8 @@
                 complete_all = all(c[0] for c in comp_param.values()) and all(c[0] for c in comp_coef.values()) and not missing_params and distinct == N_COEF and len(ids) == N_COEF
                 incomplete = {k: c[1] for k, c in list(comp_param.items()) + list(comp_coef.items()) if not c[0]}
                 phys_ok = all(v.get("status") in (None, "NOT_APPLICABLE", "PASS") for v in rejudge.values())
-                amended_pass = complete_all and phys_ok and all(whole_param.values()) and all(whole_coef.values()) and bool(gres) and all(v["status"] == "PASS" for v in gres.values())
-                amended_status = "PASS" if amended_pass else ("INVALID (incomplete or re-judgement pending)" if (not complete_all or not phys_ok) else "OPEN")
+                amended_pass = complete_all and bool(ids_match) and phys_ok and all(whole_param.values()) and all(whole_coef.values()) and bool(gres) and all(v["status"] == "PASS" for v in gres.values())
+                amended_status = "PASS" if amended_pass else ("INVALID (incomplete, ids not the drawn columns, or re-judgement pending)" if (not complete_all or not phys_ok or not ids_match) else "OPEN")
                 cres[jac] = dict(registered=registered, amended=dict(status=amended_status, incomplete_records=incomplete, whole_column_parameter=whole_param, whole_column_coefficient=whole_coef, missing_parameter_columns=missing_params, groups=gres,
                                                                      resolved_coverage_counts={g: v["n_coverage_distinct"] for g, v in gres.items()}), label=LABEL)
             report["cases"][cname] = cres
```
