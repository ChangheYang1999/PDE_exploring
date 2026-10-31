# Snapshot gpu_v1 addendum 3 (test-only): gates.py v3 = registered scaling convention and floored Richardson (specification 3.0 (b')(1), 3.0 (d)(iii); V179; lead 06:22Z item 3); checker v1.17; written 2026-10-29T06:32:46Z

validation/gates.py 19a86d4fcd69f404 (v2, addendum 2) -> 549c21b0fac9ecfa (full sha256 549c21b0fac9ecfa6183169f14817bc7f02b95644f49aa3c9109ca6f8ac86e41); previous file kept as validation/gates.py.v2_19a86d4f. Changes: column_test multiplies the tested column d and the differences D_h, D4_h by the column's step scale s_j and compares them against the FIXED floor F = 1e-10 ||r_block|| (Case.group_errors unchanged; s_j = 1 for parameter columns in optimizer coordinates and for physical c_l; s_j = omega for the physical omega column when omega < 0.5; s_j = max(1, 1e-7/||J_f col||/1e-3) for coefficient columns); richardson_error takes the scale and the reference and judges |R - d| s_j against max(|d| s_j, |R| s_j, F) over the rows (whole column and per group); the F = 0 variants are scale-free; every column record states scaling_convention v3. Consequence (3.6 (j)(4)(iv)): G1 records made with the earlier convention do not count; the G1 sections of S01_own and S09_own are rerun (tags gpu_v1_S01_own_G1v3, gpu_v1_S09_own_G1v3) and S05_own and manu_large_omega restart their full batteries; the G2 to G5 sections of S01_own and S09_own are unaffected.

validation/g1_coverage_check.py e48327ddcfb01e62: specification v1.17 small-amplitude group, post-result rule: registered and amended outcomes side by side per case and Jacobian; parameter columns never classified and all four required to pass every group; small-amplitude only when every step's norms are finite and below 1e-6 of the column norm; distinct column ids; whole-column decisions retained in the amended outcome; missing or non-finite records fail closed.

## diff gates.py v2 -> v3
```
--- validation/gates.py.v2_19a86d4f	2026-10-29 06:31:10.738605124 +0000
+++ validation/gates.py	2026-10-29 06:31:10.768605180 +0000
@@ -196,26 +196,31 @@
     return dict(pass_second_order=ok2, pass_five_point=ok4, ratios_second_order=ratios, min_e=min(errs.values()), min_e4=min(errs4.values()))
 
 
-def richardson_error(lad, d, h_pair, mask=None):
-    """Richardson value D_h' + (D_h' - D_h)/99 from the second-order pair (h, h' = h/10) against d."""
+def richardson_error(lad, d, h_pair, mask=None, scale=1.0, ref=None, floor_rel=1e-10):
+    """Richardson value D_h' + (D_h' - D_h)/99 from the second-order pair (h, h' = h/10) against d, judged with the registered floor F = floor_rel * ||ref||
+    over the rows (specification 3.0 (d)(iii)); d and the Richardson value are multiplied by the step scale s_j of the column (3.0 (b')(1)); v3 2026-10-29 (V179)."""
     h, hp = h_pair
     Dh, Dhp = lad[h][0], lad[hp][0]
-    R = Dhp + (Dhp - Dh) / 99.0
+    R = (Dhp + (Dhp - Dh) / 99.0) * scale; dd = d * scale
+    F = 0.0
     if mask is not None:
-        R, dd = R[mask], d[mask]
-    else:
-        dd = d
-    return float((R - dd).norm() / max(float(dd.norm()), float(R.norm()), 1e-300))
+        R, dd = R[mask], dd[mask]
+        if ref is not None:
+            F = floor_rel * float(ref[mask].norm())
+    elif ref is not None:
+        F = floor_rel * float(ref.norm())
+    return float((R - dd).norm() / max(float(dd.norm()), float(R.norm()), F, 1e-300))
 
 
 def column_test(case, label, dcol, fun, z, e, h_steps, tau_all=1e-6, tau_group=1e-5, ref=None, record_active=None, scale=1.0):
     """G1-type test of a derivative column dcol against the ladder of fun along e (direction with |e| = 1 in the perturbed coordinate; step h*scale)."""
     lad, active = stencil_ladder(fun, z, e, [h * scale for h in h_steps], record_active)
     errs = {}; errs4 = {}; per_group = {}; errs0 = {}; errs40 = {}
-    for h in h_steps:
-        D, D4 = lad[h * scale]
-        ge = case.group_errors(dcol, D, ref=ref); ge4 = case.group_errors(dcol, D4, ref=ref)
-        ge0 = case.group_errors(dcol, D, ref=None); ge40 = case.group_errors(dcol, D4, ref=None)        # F = 0 (specification 3.0 (c): PASS_rel; lead 23:24Z item 3)
+    dcol_s = dcol * scale                                   # specification 3.0 (b')(1) (V179; v3 2026-10-29): the column and the differences are multiplied by the step scale s_j
+    for h in h_steps:                                       # of the column and compared against the FIXED floor F = 1e-10 ||r_block|| (unchanged for s_j = 1)
+        D, D4 = lad[h * scale]; D = D * scale; D4 = D4 * scale
+        ge = case.group_errors(dcol_s, D, ref=ref); ge4 = case.group_errors(dcol_s, D4, ref=ref)
+        ge0 = case.group_errors(dcol_s, D, ref=None); ge40 = case.group_errors(dcol_s, D4, ref=None)        # F = 0 (specification 3.0 (c): PASS_rel; lead 23:24Z item 3)
         errs[h] = ge["all"]["e"]; errs4[h] = ge4["all"]["e"]; errs0[h] = ge0["all"]["e"]; errs40[h] = ge40["all"]["e"]
         per_group[f"{h:.0e}"] = dict(second_order={k: v["e"] for k, v in ge.items()}, five_point={k: v["e"] for k, v in ge4.items()},
                                    second_order_F0={k: v["e"] for k, v in ge0.items()}, five_point_F0={k: v["e"] for k, v in ge40.items()},
@@ -228,11 +233,11 @@
     rich = None
     for i in range(len(hs) - 1):
         if errs[hs[i]] <= tau_all and errs[hs[i + 1]] <= tau_all:
-            rich = richardson_error(lad, dcol, (hs[i] * scale, hs[i + 1] * scale)); break
+            rich = richardson_error(lad, dcol, (hs[i] * scale, hs[i + 1] * scale), scale=scale, ref=ref); break        # with the floor (3.0 (d)(iii))
     rich0 = None
     for i in range(len(hs) - 1):
         if errs0[hs[i]] <= tau_all and errs0[hs[i + 1]] <= tau_all:
-            rich0 = richardson_error(lad, dcol, (hs[i] * scale, hs[i + 1] * scale)); break
+            rich0 = richardson_error(lad, dcol, (hs[i] * scale, hs[i + 1] * scale), scale=scale, ref=None); break      # F = 0 variant
     # group pass: every group and block within tau_group at two consecutive steps (second order) and five point; the same with F = 0 (PASS_rel)
     group_pass = {}
     for gname in ["all"] + case.group_names + (["far_anchor_block"] if (hasattr(case, "anchor_mask") and bool(case.anchor_mask.any())) else []):
@@ -256,14 +261,14 @@
             gi = case.group_names.index(gname); mask = case.row_group == gi
         for i in range(len(hs) - 1):
             if eg[hs[i]] is not None and eg[hs[i]] <= t and eg[hs[i + 1]] <= t:
-                gp["richardson_error"] = richardson_error(lad, dcol, (hs[i] * scale, hs[i + 1] * scale), mask=mask); break
+                gp["richardson_error"] = richardson_error(lad, dcol, (hs[i] * scale, hs[i + 1] * scale), mask=mask, scale=scale, ref=ref); break
         gp["PASS"] = bool(gp["pass_second_order"] and gp["pass_five_point"] and gp["richardson_error"] is not None and gp["richardson_error"] <= t)
         # the same decision with F = 0 (Richardson is floor-free already; its pair is the first passing F = 0 pair)
         eg0 = {h: per_group[f"{h:.0e}"]["second_order_F0"].get(gname) for h in hs}
         gp["richardson_error_F0"] = None
         for i in range(len(hs) - 1):
             if eg0[hs[i]] is not None and eg0[hs[i]] <= t and eg0[hs[i + 1]] <= t:
-                gp["richardson_error_F0"] = richardson_error(lad, dcol, (hs[i] * scale, hs[i + 1] * scale), mask=mask); break
+                gp["richardson_error_F0"] = richardson_error(lad, dcol, (hs[i] * scale, hs[i + 1] * scale), mask=mask, scale=scale, ref=None); break
         gp["PASS_rel"] = bool(gp["pass_second_order_F0"] and gp["pass_five_point_F0"] and gp["richardson_error_F0"] is not None and gp["richardson_error_F0"] <= t)
         gp["absolute_only"] = bool(gp["PASS"] and not gp["PASS_rel"])          # specification 3.0 (c): passes only because of the floor (lead 23:24Z item 3)
     active_same = None
@@ -276,7 +281,8 @@
                 errors_second_order_F0={f"{h:.0e}": errs0[h] for h in hs}, errors_five_point_F0={f"{h:.0e}": errs40[h] for h in hs},
                 pass_rule=pr, richardson_error=rich, pass_rule_F0=pr0, richardson_error_F0=rich0, group_pass=group_pass, PASS=bool(ok), PASS_rel=bool(ok_rel), absolute_only=bool(ok and not ok_rel),
                 column_norm=float(dcol.norm()), active_sets_identical=active_same,
-                active_sets=({f"{t:+.1e}": a for t, a in active.items()} if active else None), step_scale=scale)
+                active_sets=({f"{t:+.1e}": a for t, a in active.items()} if active else None), step_scale=scale,
+                scaling_convention="v3 (2026-10-29, V179): d and D_h multiplied by the step scale s_j against the fixed floor F = 1e-10 ||r_block|| (specification 3.0 (b')(1)); Richardson judged with F (3.0 (d)(iii)); the F = 0 variants are scale-free")
 
 
 def run_case(case, quick=False, n_coef_cols=20, seed=11, save=None, sections=("G1", "G2G4", "G3", "G5")):
```

## g1_coverage_check.py (full text, new file)
```
#!/usr/bin/env python
"""specification v1.17 3.6 (j) "small-amplitude group, post-result rule" (lead 06:22Z; V180, V183): per battery case and Jacobian (J_f, J_cw, J_c harness) the checker
writes the REGISTERED outcome and the AMENDED outcome side by side. Fails closed: missing or non-finite records count as failures, never as small-amplitude.
Registered outcome (3.0 (b'), (d)): every parameter column passes (whole column and every group) and every coefficient column passes (whole column and every group).
Amended outcome: (i) the whole-column test is retained for every column; (ii) parameter columns are never classified: both parameters, in both coordinate systems,
must pass every group; (iii) a coefficient-column group is small-amplitude when max(||d_g||, ||D_g,h|| second-order and five-point) < 1e-6 ||column|| at EVERY
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
def small_amplitude(rec, g):
    pg = rec.get("per_group"); cn = rec.get("norm")
    if not isinstance(pg, dict) or not pg or not fin(cn) or cn <= 0:
        return False                                   # fail closed: cannot be classified small
    for h, v in pg.items():
        vals = [(v.get(k) or {}).get(g) for k in ("norm_d", "norm_fd", "norm_fd_five_point")]
        if any(not fin(x) for x in vals):
            return False
        if max(vals) >= THRESH * cn:
            return False
    return True
def group_pass(rec, g):
    gp = (rec.get("group_pass") or {}).get(g)
    return bool(gp.get("PASS")) if isinstance(gp, dict) and "PASS" in gp else False      # missing decision = failure
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
                whole_param = {k: bool(((v.get("pass_rule") or {}).get("pass_second_order") and (v.get("pass_rule") or {}).get("pass_five_point") and fin(v.get("richardson_error")) and v.get("richardson_error") <= 1e-6)) for k, v in pc.items()}
                whole_coef = {}
                for e in cc:
                    r = col_record(e, jac); pr = r.get("pass_rule") or {}
                    whole_coef[col_id(e, jac)] = bool(pr.get("pass_second_order") and pr.get("pass_five_point") and fin(r.get("richardson")) and r.get("richardson") <= 1e-6)
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
