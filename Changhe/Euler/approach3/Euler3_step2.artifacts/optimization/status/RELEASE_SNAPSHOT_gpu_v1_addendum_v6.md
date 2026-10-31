# Snapshot gpu_v1 addendum 6 (test-only, V192): gates.py v5c (Richardson witnesses with norms and floor) and checker v4; written 2026-10-29T07:17:22Z

gates.py 283fa237cb119ece (v5b, kept as gates.py.v5b_283fa237) -> 5f4079926f1c757b (v5c): richardson_witness() records, for every adjacent pair, ||R - d|| s, ||d|| s, ||R|| s, the floor F and the scale next to the Richardson error (richardson_all_pairs, whole column and per group, with and without the floor); same arithmetic as richardson_error. Checker g1_coverage_check.py 2c64f84c4a5b12cf (v3, kept as .v3_2c64f84c) -> b9e297dd37a49a49 (v4): (1) the twenty coefficient ids are matched against the case's G1_coefficient_columns_drawn and the per-Jacobian column list; (2) the registered row groups near_origin, core_intermediate, far and the whole-column 'all' witnesses are required with the five nominal step labels 1e-03..1e-07, finite non-negative norms and errors and valid scales; (3) for J_cw and J_c the raw active-set records (base and every stencil point, 2*5+1 entries) must exist and be identical (recomputed) with the base flag set before active_sets_identical is trusted; J_f uses the declared frozen-weight convention; (4) whole-column and per-group decisions (two consecutive passing steps second-order and five-point, Richardson from the pair witnesses: minimum over the passing pairs for v5 records, the recorded value for v4 records) are RECOMPUTED from the recorded errors and compared with the stored flags, which are reported but not authoritative; (5) REJUDGED_PASS counts as a registered pass. Consequence: coefficient records of harness v4 (rec_of without the raw active sets) are INVALID for J_cw and J_c under (3) unless the verifier accepts the v4 active_sets_identical (computed over base and stencil) as adequate; the G1_coef sections of the four cases are pre-queued on v5 right after the running v4 jobs.

## diff gates.py v5b -> v5c
```
--- validation/gates.py.v5b_283fa237	2026-10-29 07:15:22.264389186 +0000
+++ validation/gates.py	2026-10-29 07:15:22.314389203 +0000
@@ -216,13 +216,29 @@
     return float((R - dd).norm() / max(float(dd.norm()), float(R.norm()), F, 1e-300))
 
 
+def richardson_witness(lad, d, h_pair, mask=None, scale=1.0, ref=None, floor_rel=1e-10):
+    """v5c (V192 item 6, recording only): the Richardson comparison with its witnesses: ||R - d|| s, ||d|| s, ||R|| s and the floor F (same arithmetic as richardson_error)."""
+    h, hp = h_pair
+    Dh, Dhp = lad[h][0], lad[hp][0]
+    R = (Dhp + (Dhp - Dh) / 99.0) * scale; dd = d * scale
+    F = 0.0
+    if mask is not None:
+        R, dd = R[mask], dd[mask]
+        if ref is not None:
+            F = floor_rel * float(ref[mask].norm())
+    elif ref is not None:
+        F = floor_rel * float(ref.norm())
+    nd, nR, ndiff = float(dd.norm()), float(R.norm()), float((R - dd).norm())
+    return dict(richardson_error=ndiff / max(nd, nR, F, 1e-300), norm_diff_scaled=ndiff, norm_d_scaled=nd, norm_R_scaled=nR, floor=F, scale=scale)
+
+
 def best_richardson(lad, dcol, errs, hs, tau, scale, ref, mask=None, dscale=None):
     """v4 (V187, specification 3.0 (d)): over ALL adjacent pairs of ladder steps whose second-order errors are both within tau, the Richardson error (floored, scaled)
     is formed and the smallest is returned with its pair (None if no pair passes). The former harness took the first passing pair only."""
     best = None; best_pair = None; allp = {}
     for i in range(len(hs) - 1):
-        r = richardson_error(lad, dcol, (hs[i] * scale, hs[i + 1] * scale), mask=mask, scale=(scale if dscale is None else dscale), ref=ref)
-        allp[f"{hs[i]:.0e}->{hs[i + 1]:.0e}"] = dict(richardson_error=r, pair_passes_second_order=bool(errs[hs[i]] <= tau and errs[hs[i + 1]] <= tau))   # v5 (lead 06:59Z (b)): every pair recorded
+        w = richardson_witness(lad, dcol, (hs[i] * scale, hs[i + 1] * scale), mask=mask, scale=(scale if dscale is None else dscale), ref=ref); r = w["richardson_error"]
+        allp[f"{hs[i]:.0e}->{hs[i + 1]:.0e}"] = dict(w, pair_passes_second_order=bool(errs[hs[i]] <= tau and errs[hs[i + 1]] <= tau))   # v5c (lead 06:59Z (b), V192 item 6): every pair with its witnesses
         if errs[hs[i]] <= tau and errs[hs[i + 1]] <= tau and (best is None or r < best):
             best, best_pair = r, (f"{hs[i]:.0e}", f"{hs[i + 1]:.0e}")
     best_richardson.last_all = allp
@@ -294,7 +310,7 @@
                 active_set_base_recorded=bool(active) and (0.0 in active),
                 column_norm=float(dcol.norm()), active_sets_identical=active_same,
                 active_sets=({f"{t:+.1e}": a for t, a in active.items()} if active else None), step_scale=scale, derivative_scale=ds_,
-                scaling_convention="v5 (2026-10-29, V190: derivative_scale separate from step_scale; physical omega judged in physical units) v4 (V179, V187): base active set recorded and compared; Richardson over all adjacent passing pairs (3.0 (d)); v3: d and D_h multiplied by the step scale s_j against the fixed floor F = 1e-10 ||r_block|| (specification 3.0 (b')(1)); Richardson judged with F (3.0 (d)(iii)); the F = 0 variants are scale-free")
+                scaling_convention="v5c (2026-10-29, V190, V192: derivative_scale separate from step_scale; physical omega judged in physical units; every Richardson pair with its difference and extrapolated-vector norms and the floor) v4 (V179, V187): base active set recorded and compared; Richardson over all adjacent passing pairs (3.0 (d)); v3: d and D_h multiplied by the step scale s_j against the fixed floor F = 1e-10 ||r_block|| (specification 3.0 (b')(1)); Richardson judged with F (3.0 (d)(iii)); the F = 0 variants are scale-free")
 
 
 def run_case(case, quick=False, n_coef_cols=20, seed=11, save=None, sections=("G1", "G2G4", "G3", "G5")):
```

## diff checker v3 -> v4
```
--- validation/g1_coverage_check.py.v3_2c64f84c	2026-10-29 07:16:22.684528797 +0000
+++ validation/g1_coverage_check.py	2026-10-29 07:16:22.704528846 +0000
@@ -1,5 +1,10 @@
 #!/usr/bin/env python
-"""v3 (07:0xZ, V190): completeness schema before any classification: every record must have the five ladder steps, every required group, finite d, D, D4 and whole-column norms;
+"""v4 (07:2xZ, V192): (1) the twenty coefficient ids are matched against the case's drawn columns (G1_coefficient_columns_drawn) and the per-Jacobian column lists;
+(2) the registered row groups (near_origin, core_intermediate, far, far_anchor_block) and the whole-column 'all' witnesses are required, with the five nominal
+step labels, finite non-negative norms and errors and valid scales; (3) the raw base and stencil active records are validated (all equal) before
+active_sets_identical is trusted (J_f: frozen convention); (4) the second-order, five-point and Richardson decisions are RECOMPUTED from the recorded errors and
+pair witnesses and compared with the stored flags, which are reported but not authoritative; (5) REJUDGED_PASS counts as a registered pass.
+v3 (07:0xZ, V190): completeness schema before any classification: every record must have the five ladder steps, every required group, finite d, D, D4 and whole-column norms;
 exactly the registered number of distinct coefficient columns per Jacobian (20); explicit active-set validity for J_cw and J_c (the frozen-weight J_f has no changing
 weight active set: declared frozen convention); the registered outcome distinguishes INVALID (missing or incomplete evidence) from FAIL (numerical); a separate
 resolved-coverage count (>= 5) is kept. Physical-omega parameter records written by harness v3/v4 (derivative scaled by omega < 0.5 against the fixed floor,
@@ -23,30 +28,84 @@
     return entry.get("Jf") if (jac == "Jf" and isinstance(entry.get("Jf"), dict)) else entry
 def col_id(entry, jac):
     return entry.get("column", col_record(entry, jac).get("column"))
-N_STEPS = 5; N_COEF = 20
+N_STEPS = 5; N_COEF = 20; TAU_ALL = 1e-6; TAU_GROUP = 1e-5
+STEP_LABELS = ["1e-03", "1e-04", "1e-05", "1e-06", "1e-07"]
+REQUIRED_GROUPS = ["near_origin(r<=0.1R0)", "core_intermediate", "far(r>256R0)"]      # far_anchor_block is required when the case has anchors (it does for every battery case)
+def active_sets_valid(rec, needs_active):
+    """V192 item 3: the raw base and stencil active records must exist and be identical (recomputed), and the base flag must be set; J_f uses the frozen convention."""
+    if not needs_active:
+        return True, "frozen-weight convention (no changing active set)"
+    a = rec.get("active_sets")
+    if not isinstance(a, dict) or len(a) < 2 * N_STEPS + 1 or not rec.get("active_set_base_recorded"):
+        return False, "raw active-set records or the base record missing"
+    keys = set(json.dumps(v, sort_keys=True) for v in a.values())
+    if len(keys) != 1:
+        return False, "active sets differ among the stencil points and the base"
+    if rec.get("active_sets_identical") is not True:
+        return False, "stored active_sets_identical not True"
+    return True, ""
+def consecutive_pass(errs_by_label, tau):
+    labs = [l for l in STEP_LABELS if l in errs_by_label]
+    return any(fin(errs_by_label[labs[i]]) and fin(errs_by_label[labs[i + 1]]) and errs_by_label[labs[i]] <= tau and errs_by_label[labs[i + 1]] <= tau for i in range(len(labs) - 1))
+def recompute_whole(rec, tau=TAU_ALL):
+    """V192 item 4: whole-column decision recomputed from the recorded errors and Richardson pair witnesses (v5 records: richardson_all_pairs; v4: richardson_error)."""
+    e2 = rec.get("errors") or rec.get("errors_second_order") or {}; e4 = rec.get("errors_five_point") or {}
+    p2 = consecutive_pass(e2, tau); p4 = consecutive_pass(e4, tau)
+    allp = rec.get("richardson_all_pairs")
+    if isinstance(allp, dict) and allp:
+        rs = [v["richardson_error"] for v in allp.values() if v.get("pair_passes_second_order") and fin(v.get("richardson_error"))]
+        rich = min(rs) if rs else None
+    else:
+        rich = rec.get("richardson", rec.get("richardson_error"))
+    ok = bool(p2 and p4 and fin(rich) and rich <= tau)
+    return dict(pass_second_order=p2, pass_five_point=p4, richardson=rich, PASS=ok, stored_PASS=rec.get("PASS"), agrees_with_stored=(ok == bool(rec.get("PASS"))))
+def recompute_group(rec, g, tau=TAU_GROUP):
+    pg = rec.get("per_group") or {}
+    e2 = {h: (v.get("second_order") or {}).get(g) for h, v in pg.items()}; e4 = {h: (v.get("five_point") or {}).get(g) for h, v in pg.items()}
+    p2 = consecutive_pass(e2, tau); p4 = consecutive_pass(e4, tau)
+    gp = (rec.get("group_pass") or {}).get(g) or {}
+    allp = gp.get("richardson_all_pairs")
+    if isinstance(allp, dict) and allp:
+        rs = [v["richardson_error"] for v in allp.values() if v.get("pair_passes_second_order") and fin(v.get("richardson_error"))]
+        rich = min(rs) if rs else None
+    else:
+        rich = gp.get("richardson_error")
+    ok = bool(p2 and p4 and fin(rich) and rich <= tau)
+    return dict(pass_second_order=p2, pass_five_point=p4, richardson=rich, PASS=ok, stored_PASS=gp.get("PASS"), agrees_with_stored=(ok == bool(gp.get("PASS"))))
 def record_complete(rec, groups, needs_active):
-    """Completeness schema (V190): five steps, every required group with finite second-order and five-point norms, finite whole-column norm, decisions present,
-    and (for J_cw / J_c) explicit identical active sets. Returns (ok, reason)."""
+    """Completeness schema (V190, V192): the five nominal steps, the registered groups and the whole column with finite non-negative norms and errors, valid scales,
+    decisions present, and (for J_cw / J_c) validated identical active sets including the base. Returns (ok, reason)."""
     if not isinstance(rec, dict) or "PASS" not in rec or not isinstance(rec.get("group_pass"), dict):
         return False, "decision or group decisions missing"
     pg = rec.get("per_group")
-    if not isinstance(pg, dict) or len(pg) < N_STEPS:
-        return False, f"ladder steps recorded: {len(pg) if isinstance(pg, dict) else 0} (need {N_STEPS})"
+    if not isinstance(pg, dict) or sorted(pg.keys()) != sorted(STEP_LABELS):
+        return False, f"ladder step labels {sorted(pg.keys()) if isinstance(pg, dict) else None} (need {STEP_LABELS})"
+    for g in REQUIRED_GROUPS + ["all"]:
+        if g not in groups and g != "all":
+            return False, f"registered group {g} absent from the record"
+    sc = rec.get("step_scale", 1.0); dsc = rec.get("derivative_scale", sc)
+    if not (fin(sc) and sc > 0 and fin(dsc) and dsc > 0):
+        return False, "invalid step or derivative scale"
+    okA, whyA = active_sets_valid(rec, needs_active)
+    if not okA:
+        return False, whyA
     cn = rec.get("norm", rec.get("column_norm"))            # coefficient records store 'norm', parameter records (column_test output) 'column_norm'
     if not fin(cn) or cn <= 0:
         return False, "whole-column norm missing or non-finite"
     for h, v in pg.items():
-        for g in groups:
+        for g in list(groups) + ["all"]:
             for k in ("norm_d", "norm_fd", "norm_fd_five_point"):
                 x = (v.get(k) or {}).get(g)
-                if not fin(x):
-                    return False, f"group {g} step {h}: {k} missing or non-finite"
+                if not fin(x) or x < 0:
+                    return False, f"group {g} step {h}: {k} missing, non-finite or negative"
         for k in ("second_order", "five_point", "second_order_F0", "five_point_F0"):
-            for g in groups:
-                if not fin((v.get(k) or {}).get(g)):
-                    return False, f"group {g} step {h}: {k} missing or non-finite"
-    if needs_active and rec.get("active_sets_identical") is not True:
-        return False, f"active sets not explicitly identical ({rec.get('active_sets_identical')})"
+            for g in list(groups) + ["all"]:
+                x = (v.get(k) or {}).get(g)
+                if not fin(x) or x < 0:
+                    return False, f"group {g} step {h}: {k} missing, non-finite or negative"
+    for k in ("errors", "errors_second_order"):
+        if k in rec and (not isinstance(rec[k], dict) or sorted(rec[k].keys()) != sorted(STEP_LABELS)):
+            return False, "whole-column error ladder incomplete"
     return True, ""
 def record_valid(rec):
     """Validity for the decision functions: complete decisions and active sets not reported as different (the completeness schema is checked separately)."""
@@ -93,7 +152,7 @@
             return False
     return True
 def group_pass(rec, g):
-    """The stored per-group decision counts only for a valid record with finite norms for that group; otherwise the decision is a failure (fail closed)."""
+    """The per-group decision RECOMPUTED from the recorded errors and Richardson witnesses (V192 item 4); the stored flag is only compared. Fails closed."""
     if not record_valid(rec):
         return False
     gp = (rec.get("group_pass") or {}).get(g)
@@ -104,7 +163,7 @@
         vals = [(v.get(k) or {}).get(g) for k in ("norm_d", "norm_fd")]
         if any(not fin(x) for x in vals):
             return False
-    return bool(gp["PASS"])
+    return recompute_group(rec, g)["PASS"]
 def main(files):
     for f in files:
         d = json.load(open(f)); entries = dict(d.get("cases", {}))
@@ -130,31 +189,37 @@
                 comp_param = {k: record_complete(v, groups_req, needs_active) for k, v in pc.items()}
                 comp_coef = {col_id(e, jac): record_complete(col_record(e, jac), groups_req, needs_active) for e in cc}
                 ids = [col_id(e, jac) for e in cc]; distinct = len(set(ids))
+                drawn = c.get("G1_coefficient_columns_drawn"); listed = (c.get(ckey) or {}).get("columns")
+                ids_match = (drawn is not None and sorted(set(ids)) == sorted(drawn)) and (listed is None or sorted(listed) == sorted(drawn))
                 rejudge = {k: rejudge_physical_omega(v) for k, v in pc.items() if k == "physical:omega"}
+                recomputed = {}
                 def reg_state(k, v, comp):
                     ok, why = comp
                     if not ok:
                         return "INVALID: " + why
                     if k == "physical:omega" and rejudge.get(k, {}).get("status") not in (None, "NOT_APPLICABLE"):
                         return "REJUDGED_" + rejudge[k]["status"] + " (harness v3/v4 scaled the physical derivative by omega; physical-unit decision from witnesses)"
-                    return "PASS" if v.get("PASS") else "FAIL"
+                    rw = recompute_whole(v); rg = {g: recompute_group(v, g) for g in groups_req}
+                    recomputed[k if k is not None else v.get("column")] = dict(whole=rw, groups=rg)
+                    allok = rw["PASS"] and all(x["PASS"] for x in rg.values())
+                    return "PASS" if allok else "FAIL"
                 reg_param = {k: reg_state(k, v, comp_param[k]) for k, v in pc.items()}
                 reg_coef = {col_id(e, jac): reg_state(None, col_record(e, jac), comp_coef[col_id(e, jac)]) for e in cc}
                 registered = dict(parameter_columns=reg_param, coefficient_columns=reg_coef, n_coefficient_records=len(cc), n_distinct_coefficient_columns=distinct,
-                                  coefficient_count_as_registered=(distinct == N_COEF and len(ids) == N_COEF), missing_parameter_columns=missing_params,
+                                  coefficient_count_as_registered=(distinct == N_COEF and len(ids) == N_COEF), ids_match_drawn=ids_match, drawn_columns=drawn, missing_parameter_columns=missing_params, recomputed_decisions=recomputed,
                                   physical_omega_rejudgement=rejudge.get("physical:omega"),
-                                  PASS=(not missing_params) and distinct == N_COEF and len(ids) == N_COEF and all(v == "PASS" for v in reg_param.values()) and all(v == "PASS" for v in reg_coef.values()),
-                                  INVALID=any(str(v).startswith("INVALID") or str(v).startswith("REJUDGED_RECOMPUTE") for v in list(reg_param.values()) + list(reg_coef.values())) or bool(missing_params) or distinct != N_COEF)
+                                  PASS=(not missing_params) and distinct == N_COEF and len(ids) == N_COEF and bool(ids_match) and all(v in ("PASS",) or str(v).startswith("REJUDGED_PASS") for v in reg_param.values()) and all(v == "PASS" for v in reg_coef.values()),
+                                  INVALID=any(str(v).startswith("INVALID") or str(v).startswith("REJUDGED_RECOMPUTE") for v in list(reg_param.values()) + list(reg_coef.values())) or bool(missing_params) or distinct != N_COEF or not ids_match)
                 records_v2 = bool(cc) and all(isinstance(col_record(e, jac).get("per_group"), dict) for e in cc)
                 if not records_v2:
                     cres[jac] = dict(registered=registered, amended=dict(status="RECORDS_INSUFFICIENT", reason="compact v1 coefficient records: per-group norms absent"), label=LABEL)
                     continue
                 # amended outcome
-                whole_param = {k: bool(record_valid(v) and v.get("PASS")) for k, v in pc.items()}        # a parameter record counts only as a full valid PASS (V187)
+                whole_param = {k: bool(record_valid(v) and comp_param[k][0] and (recompute_whole(v)["PASS"] or str(reg_param.get(k, "")).startswith("REJUDGED_PASS")) and all(recompute_group(v, g)["PASS"] for g in groups_req)) for k, v in pc.items()}   # recomputed (V192 item 4)
                 whole_coef = {}
                 for e in cc:
-                    r = col_record(e, jac); pr = r.get("pass_rule") or {}
-                    whole_coef[col_id(e, jac)] = bool(record_valid(r) and pr.get("pass_second_order") and pr.get("pass_five_point") and fin(r.get("richardson")) and r.get("richardson") <= 1e-6)
+                    r = col_record(e, jac)
+                    whole_coef[col_id(e, jac)] = bool(record_valid(r) and comp_coef[col_id(e, jac)][0] and recompute_whole(r)["PASS"])
                 gres = {}
                 for g in sorted(groups):
                     par_fail = [k for k in expected_params if k in pc and not group_pass(pc[k], g)] + [k for k in missing_params]
```
