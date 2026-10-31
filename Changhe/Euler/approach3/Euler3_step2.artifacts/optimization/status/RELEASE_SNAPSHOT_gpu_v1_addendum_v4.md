# Snapshot gpu_v1 addendum 4 (test-only): gates.py v4 and g3_addon v2 (V187: base active set, Richardson over all adjacent passing pairs), checker v2 (normalization by s_j, validity); written 2026-10-29T06:41:31Z

validation/gates.py 549c21b0fac9ecfa (v3) -> 918c2e06ba2bae2f (v4; previous file kept as validation/gates.py.v3_549c21b0): (a) stencil_ladder records the BASE active set (t = 0) and every stencil point is compared with it (active_sets_identical now includes the base; record field active_set_base_recorded); (b) best_richardson(): over ALL adjacent pairs of ladder steps whose second-order errors pass, the floored, scaled Richardson error is formed and the smallest counts, with its pair recorded (richardson_pair, per column and per group, with and without the floor); the former harness stopped at the first passing pair, which could cause false failures (specification 3.0 (d) allows any adjacent valid pair); (c) scalar_decisions (G3) inspects every adjacent passing pair in the same way. validation/g3_addon.py (v1 kept as g3_addon.py.v1) -> 613531ee6767166b: the same change for the seven-step ladder (over consecutive VALID pairs). validation/g1_coverage_check.py -> 87d4e0bd397f40cd (v2): the per-group norms stored by column_test are scaled by s_j and are divided by s_j before the comparison with 1e-6 of the unscaled column norm; a record is valid evidence only if its active sets are identical (now including the base) and its decisions exist; parameter columns count only as full valid passes; non-finite or missing norms fail closed (V187).

## diff gates.py v3 -> v4
```
--- validation/gates.py.v3_549c21b0	2026-10-29 06:40:54.829827982 +0000
+++ validation/gates.py	2026-10-29 06:40:54.859828049 +0000
@@ -154,6 +154,8 @@
     plus active-set records when record_active(z) is given (called at every stencil point)."""
     out = {}; active = {}
     cache = {}
+    if record_active is not None:
+        active[0.0] = record_active(z)                     # v4 (V187): the BASE active set is recorded too; every stencil point must agree with it
     def f(t):
         if t not in cache:
             cache[t] = fun(z + t * e)
@@ -175,10 +177,12 @@
         e4 = {h: abs(D4s[f"{h:.0e}"] - dpred) / max(abs(dpred), abs(D4s[f"{h:.0e}"]), F) for h in hs}
         pr = pass_rule(e2, e4, tau)
         hs_sorted = sorted(e2.keys(), reverse=True); rich = None; pair = None
-        for i in range(len(hs_sorted) - 1):
+        for i in range(len(hs_sorted) - 1):                                      # v4 (V187): every adjacent passing pair is inspected; the smallest Richardson error counts
             if e2[hs_sorted[i]] <= tau and e2[hs_sorted[i + 1]] <= tau:
                 h, hp = hs_sorted[i], hs_sorted[i + 1]; R = Ds[f"{hp:.0e}"] + (Ds[f"{hp:.0e}"] - Ds[f"{h:.0e}"]) / 99.0
-                rich = abs(R - dpred) / max(abs(dpred), abs(R), F); pair = (f"{h:.0e}", f"{hp:.0e}"); break
+                r_ = abs(R - dpred) / max(abs(dpred), abs(R), F)
+                if rich is None or r_ < rich:
+                    rich = r_; pair = (f"{h:.0e}", f"{hp:.0e}")
         return pr, rich, pair, bool(pr["pass_second_order"] and pr["pass_five_point"] and rich is not None and rich <= tau), e2, e4
     pr, rich, pair, ok, _, _ = decide(Fl)
     pr0, rich0, pair0, ok0, e20, e40 = decide(0.0)
@@ -212,6 +216,18 @@
     return float((R - dd).norm() / max(float(dd.norm()), float(R.norm()), F, 1e-300))
 
 
+def best_richardson(lad, dcol, errs, hs, tau, scale, ref, mask=None):
+    """v4 (V187, specification 3.0 (d)): over ALL adjacent pairs of ladder steps whose second-order errors are both within tau, the Richardson error (floored, scaled)
+    is formed and the smallest is returned with its pair (None if no pair passes). The former harness took the first passing pair only."""
+    best = None; best_pair = None
+    for i in range(len(hs) - 1):
+        if errs[hs[i]] <= tau and errs[hs[i + 1]] <= tau:
+            r = richardson_error(lad, dcol, (hs[i] * scale, hs[i + 1] * scale), mask=mask, scale=scale, ref=ref)
+            if best is None or r < best:
+                best, best_pair = r, (f"{hs[i]:.0e}", f"{hs[i + 1]:.0e}")
+    return best, best_pair
+
+
 def column_test(case, label, dcol, fun, z, e, h_steps, tau_all=1e-6, tau_group=1e-5, ref=None, record_active=None, scale=1.0):
     """G1-type test of a derivative column dcol against the ladder of fun along e (direction with |e| = 1 in the perturbed coordinate; step h*scale)."""
     lad, active = stencil_ladder(fun, z, e, [h * scale for h in h_steps], record_active)
@@ -229,15 +245,9 @@
                                    max_comp={k: v.get("max_comp") for k, v in ge.items()}, floor_above_norms={k: v.get("absolute_only") for k, v in ge.items()})
     pr = pass_rule(errs, errs4, tau_all); pr0 = pass_rule(errs0, errs40, tau_all)
     hs = sorted(errs.keys(), reverse=True)
-    # Richardson on the first passing consecutive pair (second order)
-    rich = None
-    for i in range(len(hs) - 1):
-        if errs[hs[i]] <= tau_all and errs[hs[i + 1]] <= tau_all:
-            rich = richardson_error(lad, dcol, (hs[i] * scale, hs[i + 1] * scale), scale=scale, ref=ref); break        # with the floor (3.0 (d)(iii))
-    rich0 = None
-    for i in range(len(hs) - 1):
-        if errs0[hs[i]] <= tau_all and errs0[hs[i + 1]] <= tau_all:
-            rich0 = richardson_error(lad, dcol, (hs[i] * scale, hs[i + 1] * scale), scale=scale, ref=None); break      # F = 0 variant
+    # Richardson: the best over all adjacent passing second-order pairs (v4; with the floor, 3.0 (d)(iii)), and the F = 0 variant
+    rich, rich_pair = best_richardson(lad, dcol, errs, hs, tau_all, scale, ref)
+    rich0, rich0_pair = best_richardson(lad, dcol, errs0, hs, tau_all, scale, None)
     # group pass: every group and block within tau_group at two consecutive steps (second order) and five point; the same with F = 0 (PASS_rel)
     group_pass = {}
     for gname in ["all"] + case.group_names + (["far_anchor_block"] if (hasattr(case, "anchor_mask") and bool(case.anchor_mask.any())) else []):
@@ -259,16 +269,13 @@
             mask = case.anchor_mask
         else:
             gi = case.group_names.index(gname); mask = case.row_group == gi
-        for i in range(len(hs) - 1):
-            if eg[hs[i]] is not None and eg[hs[i]] <= t and eg[hs[i + 1]] <= t:
-                gp["richardson_error"] = richardson_error(lad, dcol, (hs[i] * scale, hs[i + 1] * scale), mask=mask, scale=scale, ref=ref); break
+        eg_f = {h: (v if v is not None else float("inf")) for h, v in eg.items()}
+        gp["richardson_error"], gp["richardson_pair"] = best_richardson(lad, dcol, eg_f, hs, t, scale, ref, mask=mask)
         gp["PASS"] = bool(gp["pass_second_order"] and gp["pass_five_point"] and gp["richardson_error"] is not None and gp["richardson_error"] <= t)
         # the same decision with F = 0 (Richardson is floor-free already; its pair is the first passing F = 0 pair)
         eg0 = {h: per_group[f"{h:.0e}"]["second_order_F0"].get(gname) for h in hs}
-        gp["richardson_error_F0"] = None
-        for i in range(len(hs) - 1):
-            if eg0[hs[i]] is not None and eg0[hs[i]] <= t and eg0[hs[i + 1]] <= t:
-                gp["richardson_error_F0"] = richardson_error(lad, dcol, (hs[i] * scale, hs[i + 1] * scale), mask=mask, scale=scale, ref=None); break
+        eg0_f = {h: (v if v is not None else float("inf")) for h, v in eg0.items()}
+        gp["richardson_error_F0"], gp["richardson_pair_F0"] = best_richardson(lad, dcol, eg0_f, hs, t, scale, None, mask=mask)
         gp["PASS_rel"] = bool(gp["pass_second_order_F0"] and gp["pass_five_point_F0"] and gp["richardson_error_F0"] is not None and gp["richardson_error_F0"] <= t)
         gp["absolute_only"] = bool(gp["PASS"] and not gp["PASS_rel"])          # specification 3.0 (c): passes only because of the floor (lead 23:24Z item 3)
     active_same = None
@@ -279,10 +286,11 @@
     ok_rel = pr0["pass_second_order"] and pr0["pass_five_point"] and (rich0 is not None and rich0 <= tau_all) and all(v["PASS_rel"] for v in group_pass.values()) and (active_same is not False)
     return dict(label=label, errors_second_order={f"{h:.0e}": errs[h] for h in hs}, errors_five_point={f"{h:.0e}": errs4[h] for h in hs}, per_group=per_group,
                 errors_second_order_F0={f"{h:.0e}": errs0[h] for h in hs}, errors_five_point_F0={f"{h:.0e}": errs40[h] for h in hs},
-                pass_rule=pr, richardson_error=rich, pass_rule_F0=pr0, richardson_error_F0=rich0, group_pass=group_pass, PASS=bool(ok), PASS_rel=bool(ok_rel), absolute_only=bool(ok and not ok_rel),
+                pass_rule=pr, richardson_error=rich, richardson_pair=rich_pair, pass_rule_F0=pr0, richardson_error_F0=rich0, richardson_pair_F0=rich0_pair, group_pass=group_pass, PASS=bool(ok), PASS_rel=bool(ok_rel), absolute_only=bool(ok and not ok_rel),
+                active_set_base_recorded=bool(active) and (0.0 in active),
                 column_norm=float(dcol.norm()), active_sets_identical=active_same,
                 active_sets=({f"{t:+.1e}": a for t, a in active.items()} if active else None), step_scale=scale,
-                scaling_convention="v3 (2026-10-29, V179): d and D_h multiplied by the step scale s_j against the fixed floor F = 1e-10 ||r_block|| (specification 3.0 (b')(1)); Richardson judged with F (3.0 (d)(iii)); the F = 0 variants are scale-free")
+                scaling_convention="v4 (2026-10-29, V179, V187): base active set recorded and compared; Richardson over all adjacent passing pairs (3.0 (d)); v3: d and D_h multiplied by the step scale s_j against the fixed floor F = 1e-10 ||r_block|| (specification 3.0 (b')(1)); Richardson judged with F (3.0 (d)(iii)); the F = 0 variants are scale-free")
 
 
 def run_case(case, quick=False, n_coef_cols=20, seed=11, save=None, sections=("G1", "G2G4", "G3", "G5")):
```

## diff g3_addon.py v1 -> v2
```
--- validation/g3_addon.py.v1	2026-10-29 06:41:30.999906496 +0000
+++ validation/g3_addon.py	2026-10-29 06:41:31.039906580 +0000
@@ -28,7 +28,7 @@
 
 def ladder_report(vals, g0_vals, dpred, Fl, hs, subtract_gauge, valid):
     """vals[t] = O1(X + t v), g0_vals[t] = gauge row at t, valid[h] = all four stencil points of step h share the base active set.
-    Returns errors of both stencils, Richardson (first passing pair of consecutive valid steps), pass flags, absolute-only flag, OPEN flag."""
+    Returns errors of both stencils, Richardson (the best over all passing pairs of consecutive valid steps; v2), pass flags, absolute-only flag, OPEN flag."""
     def O(t):
         o = vals[t]
         if subtract_gauge:
@@ -41,9 +41,11 @@
         errs = {h: abs(D2[h] - dpred) / max(abs(dpred), abs(D2[h]), F) for h in hs}; errs4 = {h: abs(D4s[h] - dpred) / max(abs(dpred), abs(D4s[h]), F) for h in hs}
         ok2, ok4, pairs = pass_rule(errs, errs4, hs, valid)
         rich = None; pair = None
-        for a, b in pairs:
+        for a, b in pairs:                                                   # v2 (V187, specification 3.0 (d)): every adjacent passing valid pair is inspected; the smallest Richardson error counts
             if errs[a] <= 1e-6 and errs[b] <= 1e-6:
-                R = D2[b] + (D2[b] - D2[a]) / 99.0; rich = abs(R - dpred) / max(abs(dpred), abs(R), F); pair = (a, b); break
+                R = D2[b] + (D2[b] - D2[a]) / 99.0; r_ = abs(R - dpred) / max(abs(dpred), abs(R), F)
+                if rich is None or r_ < rich:
+                    rich = r_; pair = (a, b)
         open_ = len(pairs) == 0
         return errs, errs4, ok2, ok4, pairs, rich, pair, open_, bool((not open_) and ok2 and ok4 and rich is not None and rich <= 1e-6)
     errs, errs4, ok2, ok4, pairs, rich, pair, open_, PASS = decide(Fl)                     # the registered decision (with the floor)
```

## g1_coverage_check.py v2 (full text)
```
#!/usr/bin/env python
"""v2 (06:4xZ, V187): per-group norms divided by s_j before the comparison; records with non-identical active sets or missing decisions are invalid (fail closed).
specification v1.17 3.6 (j) "small-amplitude group, post-result rule" (lead 06:22Z; V180, V183): per battery case and Jacobian (J_f, J_cw, J_c harness) the checker
writes the REGISTERED outcome and the AMENDED outcome side by side. Fails closed: missing or non-finite records count as failures, never as small-amplitude.
Registered outcome (3.0 (b'), (d)): every parameter column passes (whole column and every group) and every coefficient column passes (whole column and every group).
Amended outcome: (i) the whole-column test is retained for every column; (ii) parameter columns are never classified: both parameters, in both coordinate systems,
must pass every group with complete valid records (active sets identical); (iii) a coefficient-column group is small-amplitude when max(||d_g||, ||D_g,h|| second-order and five-point) < 1e-6 ||column|| at EVERY
valid step (any absent or non-finite norm: not small-amplitude); it is reported as "not tested on that column"; (iv) a group counts only if, in the same case and
Jacobian, it passes on all parameter columns and on at least five DISTINCT coefficient columns where it is not small-amplitude, and fails on none where it is
not small-amplitude; otherwise OPEN. Usage: python validation/g1_coverage_check.py validation/gates_gpu_v1_<case>*.json -> prints markdown; writes <file>_coverage.json."""
import json, sys, glob, os, math
JACS = (("Jf", "G1_Jf_param_columns", "G1_Jf_coefficient_columns"), ("Jcw", "G1_Jcw_param_columns", "G1_Jcw_coefficient_columns"), ("Jc", "G1_Jc_param_columns", "G1_Jc_coefficient_columns"))
THRESH = 1e-6; MIN_COEF = 5; LABEL = "small-amplitude group, post-result rule (specification v1.17 3.6 (j))"
def fin(x):
    return isinstance(x, (int, float)) and math.isfinite(x)
def col_record(entry, jac):
    return entry.get("Jf") if (jac == "Jf" and isinstance(entry.get("Jf"), dict)) else entry
def col_id(entry, jac):
    return entry.get("column", col_record(entry, jac).get("column"))
def record_valid(rec):
    """A column record is valid evidence only if it is complete and its active sets are identical at every stencil point (V187)."""
    return isinstance(rec, dict) and rec.get("active_sets_identical") is not False and isinstance(rec.get("group_pass"), dict) and "PASS" in rec
def small_amplitude(rec, g):
    """v1.17 (iii), with the normalization of V187: the per-group norms stored by column_test v3 are SCALED by the step scale s_j, the whole-column norm
    (rec['norm']) is not; the group norms are divided by s_j before the comparison with 1e-6 of the column norm. Fails closed on anything missing or
    non-finite (then not small-amplitude, and the record counts as tested)."""
    pg = rec.get("per_group"); cn = rec.get("norm"); sj = rec.get("step_scale", 1.0)
    if not record_valid(rec) or not isinstance(pg, dict) or not pg or not fin(cn) or cn <= 0 or not fin(sj) or sj <= 0:
        return False
    for h, v in pg.items():
        vals = [(v.get(k) or {}).get(g) for k in ("norm_d", "norm_fd", "norm_fd_five_point")]
        if any(not fin(x) for x in vals):
            return False
        if max(vals) / sj >= THRESH * cn:
            return False
    return True
def group_pass(rec, g):
    """The stored per-group decision counts only for a valid record with finite norms for that group; otherwise the decision is a failure (fail closed)."""
    if not record_valid(rec):
        return False
    gp = (rec.get("group_pass") or {}).get(g)
    if not (isinstance(gp, dict) and "PASS" in gp):
        return False
    pg = rec.get("per_group") or {}
    for h, v in pg.items():
        vals = [(v.get(k) or {}).get(g) for k in ("norm_d", "norm_fd")]
        if any(not fin(x) for x in vals):
            return False
    return bool(gp["PASS"])
def main(files):
    for f in files:
        d = json.load(open(f)); entries = dict(d.get("cases", {}))
        for k, v in d.items():
            if isinstance(v, dict) and v.get("partial") and k not in entries:
                entries[k] = v
        report = dict(source=os.path.relpath(f), label=LABEL, threshold_small_amplitude=THRESH, min_coefficient_coverage=MIN_COEF, cases={})
        for cname, c in entries.items():
            cres = {}
            for jac, pkey, ckey in JACS:
                pc = c.get(pkey) or {}; cc = (c.get(ckey) or {}).get("results") or []
                expected_params = ["optimizer:z_c", "optimizer:z_w", "physical:c_l", "physical:omega"]
                missing_params = [k for k in expected_params if k not in pc]
                groups = set()
                for v in pc.values():
                    groups |= set((v.get("group_pass") or {}).keys())
                for e in cc:
                    groups |= set((col_record(e, jac).get("group_pass") or {}).keys())
                groups.discard("all")
                # registered outcome: every column (whole and groups) passes
                reg_param = {k: bool(v.get("PASS")) for k, v in pc.items()}
                reg_coef = {col_id(e, jac): bool(col_record(e, jac).get("PASS")) for e in cc}
                registered = dict(parameter_columns=reg_param, coefficient_columns=reg_coef, n_coefficient_columns=len(cc),
                                  PASS=(not missing_params) and bool(cc) and all(reg_param.values()) and all(reg_coef.values()))
                records_v2 = bool(cc) and all(isinstance(col_record(e, jac).get("per_group"), dict) for e in cc)
                if not records_v2:
                    cres[jac] = dict(registered=registered, amended=dict(status="RECORDS_INSUFFICIENT", reason="compact v1 coefficient records: per-group norms absent"), label=LABEL)
                    continue
                # amended outcome
                whole_param = {k: bool(record_valid(v) and v.get("PASS")) for k, v in pc.items()}        # a parameter record counts only as a full valid PASS (V187)
                whole_coef = {}
                for e in cc:
                    r = col_record(e, jac); pr = r.get("pass_rule") or {}
                    whole_coef[col_id(e, jac)] = bool(record_valid(r) and pr.get("pass_second_order") and pr.get("pass_five_point") and fin(r.get("richardson")) and r.get("richardson") <= 1e-6)
                gres = {}
                for g in sorted(groups):
                    par_fail = [k for k in expected_params if k in pc and not group_pass(pc[k], g)] + [k for k in missing_params]
                    sa, pass_cols, fail_cols = [], [], []
                    seen = set()
                    for e in cc:
                        r = col_record(e, jac); k = col_id(e, jac)
                        if k in seen:
                            continue
                        seen.add(k)
                        if small_amplitude(r, g):
                            sa.append(k); continue
                        (pass_cols if group_pass(r, g) else fail_cols).append(k)
                    status = "PASS" if (not par_fail and not fail_cols and len(set(pass_cols)) >= MIN_COEF) else "OPEN"
                    gres[g] = dict(status=status, parameter_columns_failing_or_missing=par_fail, coefficient_columns_passing=pass_cols, coefficient_columns_failing_not_small_amplitude=fail_cols,
                                   coefficient_columns_small_amplitude_not_tested=sa, n_coverage_distinct=len(set(pass_cols)))
                amended_pass = (not missing_params) and all(whole_param.values()) and all(whole_coef.values()) and bool(gres) and all(v["status"] == "PASS" for v in gres.values())
                cres[jac] = dict(registered=registered, amended=dict(status=("PASS" if amended_pass else "OPEN"), whole_column_parameter=whole_param, whole_column_coefficient=whole_coef, missing_parameter_columns=missing_params, groups=gres), label=LABEL)
            report["cases"][cname] = cres
        outp = f[:-5] + "_coverage.json"; json.dump(report, open(outp, "w"), indent=1)
        print(f"\n### {os.path.basename(f)} -> {os.path.basename(outp)} ({LABEL})")
        for cname, cres in report["cases"].items():
            for jac, v in cres.items():
                am = v["amended"]
                print(f"- {cname} {jac}: registered {'PASS' if v['registered']['PASS'] else 'FAIL'} ({sum(v['registered']['coefficient_columns'].values())}/{v['registered']['n_coefficient_columns']} coefficient columns, parameters {all(v['registered']['parameter_columns'].values()) if v['registered']['parameter_columns'] else 'missing'}); amended {am.get('status')}" + (f" ({am.get('reason')})" if am.get("reason") else ""))
                for g, gv in (am.get("groups") or {}).items():
                    print(f"    - {g}: {gv['status']}; coverage {gv['n_coverage_distinct']} distinct columns {gv['coefficient_columns_passing']}; failing (not small-amplitude) {gv['coefficient_columns_failing_not_small_amplitude']}; small-amplitude (not tested) {gv['coefficient_columns_small_amplitude_not_tested']}; parameter columns failing or missing {gv['parameter_columns_failing_or_missing']}")
if __name__ == "__main__":
    main([f for a in sys.argv[1:] for f in glob.glob(a) if not (f.endswith("_label.json") or f.endswith("_coverage.json") or f.endswith("_flags.json"))])
```
