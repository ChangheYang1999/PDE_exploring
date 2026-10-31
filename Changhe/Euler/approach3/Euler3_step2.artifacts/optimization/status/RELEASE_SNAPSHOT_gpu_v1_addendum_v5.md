# Snapshot gpu_v1 addendum 5 (test-only): gates.py v5, g8_controls v4, g3_addon v3, checker v3 (V190); written 2026-10-29T07:05:07Z

gates.py 918c2e06ba2bae2f (v4, kept as gates.py.v4_918c2e06) -> 07c5842eb600e214 (v5): column_test(deriv_scale): the derivative normalization scale is separate from the stencil step scale; coefficient columns use s_j for both (3.0 (b')(1)); the physical omega column at omega < 0.5 uses omega for the step only and 1 for the derivative (physical units; V190 item 2); every G1 parameter-column call passes deriv_scale=1.0; the coefficient records (rec_of) keep the raw active sets, the base flag, the Richardson pairs (with and without the floor) and the five-point F = 0 errors; the native G3 loops record the base active set (optimizer and physical directions). g8_controls.py 8ca7ae0f984ddb66 (v3, kept as .v3_8ca7ae0f) -> 15882759c83d7aea: deriv_scale=1.0 for the physical omega control columns. g3_addon.py 613531ee6767166b (v2, kept as .v2_613531ee) -> 729f11b5ae110def: S09_own, S11_own and S20_own in the case table. g1_coverage_check.py 87d4e0bd397f40cd (v2, kept as .v2_87d4e0bd) -> 2c64f84c4a5b12cf (v3): completeness schema before classification (five steps, every group with finite second-order, five-point and whole-column norms, explicit active-set identity for J_cw and J_c, the frozen-weight convention for J_f, exactly 20 distinct coefficient columns); the registered outcome distinguishes INVALID (incomplete evidence) from FAIL (numerical) and PASS; resolved-coverage counts kept separately; physical-omega records of harness v3/v4 are re-judged in physical units from the saved witnesses (exact per-step errors; scale-free F = 0 Richardson; otherwise RECOMPUTE_NEEDED). The v4 runs in progress are not restarted (lead 06:48Z, verifier 06:54Z): their physical-omega columns are re-judged by the checker; every later launch uses v5.

## diff validation/gates.py.v4_918c2e06 -> validation/gates.py
```
--- validation/gates.py.v4_918c2e06	2026-10-29 07:02:13.482567531 +0000
+++ validation/gates.py	2026-10-29 07:02:13.532567639 +0000
@@ -216,25 +216,28 @@
     return float((R - dd).norm() / max(float(dd.norm()), float(R.norm()), F, 1e-300))
 
 
-def best_richardson(lad, dcol, errs, hs, tau, scale, ref, mask=None):
+def best_richardson(lad, dcol, errs, hs, tau, scale, ref, mask=None, dscale=None):
     """v4 (V187, specification 3.0 (d)): over ALL adjacent pairs of ladder steps whose second-order errors are both within tau, the Richardson error (floored, scaled)
     is formed and the smallest is returned with its pair (None if no pair passes). The former harness took the first passing pair only."""
     best = None; best_pair = None
     for i in range(len(hs) - 1):
         if errs[hs[i]] <= tau and errs[hs[i + 1]] <= tau:
-            r = richardson_error(lad, dcol, (hs[i] * scale, hs[i + 1] * scale), mask=mask, scale=scale, ref=ref)
+            r = richardson_error(lad, dcol, (hs[i] * scale, hs[i + 1] * scale), mask=mask, scale=(scale if dscale is None else dscale), ref=ref)
             if best is None or r < best:
                 best, best_pair = r, (f"{hs[i]:.0e}", f"{hs[i + 1]:.0e}")
     return best, best_pair
 
 
-def column_test(case, label, dcol, fun, z, e, h_steps, tau_all=1e-6, tau_group=1e-5, ref=None, record_active=None, scale=1.0):
-    """G1-type test of a derivative column dcol against the ladder of fun along e (direction with |e| = 1 in the perturbed coordinate; step h*scale)."""
+def column_test(case, label, dcol, fun, z, e, h_steps, tau_all=1e-6, tau_group=1e-5, ref=None, record_active=None, scale=1.0, deriv_scale=None):
+    """G1-type test of a derivative column dcol against the ladder of fun along e (direction with |e| = 1 in the perturbed coordinate; step h*scale).
+    deriv_scale (v5, V190): the factor by which d and D_h are multiplied before the comparison with the fixed floor F; None = scale (coefficient columns, specification
+    3.0 (b')(1)); 1.0 for the physical omega column at small omega, whose step is relative (h omega) but whose derivative is judged in physical units."""
+    ds_ = scale if deriv_scale is None else deriv_scale
     lad, active = stencil_ladder(fun, z, e, [h * scale for h in h_steps], record_active)
     errs = {}; errs4 = {}; per_group = {}; errs0 = {}; errs40 = {}
-    dcol_s = dcol * scale                                   # specification 3.0 (b')(1) (V179; v3 2026-10-29): the column and the differences are multiplied by the step scale s_j
-    for h in h_steps:                                       # of the column and compared against the FIXED floor F = 1e-10 ||r_block|| (unchanged for s_j = 1)
-        D, D4 = lad[h * scale]; D = D * scale; D4 = D4 * scale
+    dcol_s = dcol * ds_                                     # specification 3.0 (b')(1) (V179; v3): the column and the differences are multiplied by the derivative scale (s_j for
+    for h in h_steps:                                       # coefficient columns; 1 for parameter columns) and compared against the FIXED floor F = 1e-10 ||r_block||
+        D, D4 = lad[h * scale]; D = D * ds_; D4 = D4 * ds_
         ge = case.group_errors(dcol_s, D, ref=ref); ge4 = case.group_errors(dcol_s, D4, ref=ref)
         ge0 = case.group_errors(dcol_s, D, ref=None); ge40 = case.group_errors(dcol_s, D4, ref=None)        # F = 0 (specification 3.0 (c): PASS_rel; lead 23:24Z item 3)
         errs[h] = ge["all"]["e"]; errs4[h] = ge4["all"]["e"]; errs0[h] = ge0["all"]["e"]; errs40[h] = ge40["all"]["e"]
@@ -246,8 +249,8 @@
     pr = pass_rule(errs, errs4, tau_all); pr0 = pass_rule(errs0, errs40, tau_all)
     hs = sorted(errs.keys(), reverse=True)
     # Richardson: the best over all adjacent passing second-order pairs (v4; with the floor, 3.0 (d)(iii)), and the F = 0 variant
-    rich, rich_pair = best_richardson(lad, dcol, errs, hs, tau_all, scale, ref)
-    rich0, rich0_pair = best_richardson(lad, dcol, errs0, hs, tau_all, scale, None)
+    rich, rich_pair = best_richardson(lad, dcol, errs, hs, tau_all, scale, ref, dscale=ds_)
+    rich0, rich0_pair = best_richardson(lad, dcol, errs0, hs, tau_all, scale, None, dscale=ds_)
     # group pass: every group and block within tau_group at two consecutive steps (second order) and five point; the same with F = 0 (PASS_rel)
     group_pass = {}
     for gname in ["all"] + case.group_names + (["far_anchor_block"] if (hasattr(case, "anchor_mask") and bool(case.anchor_mask.any())) else []):
@@ -270,12 +273,12 @@
         else:
             gi = case.group_names.index(gname); mask = case.row_group == gi
         eg_f = {h: (v if v is not None else float("inf")) for h, v in eg.items()}
-        gp["richardson_error"], gp["richardson_pair"] = best_richardson(lad, dcol, eg_f, hs, t, scale, ref, mask=mask)
+        gp["richardson_error"], gp["richardson_pair"] = best_richardson(lad, dcol, eg_f, hs, t, scale, ref, mask=mask, dscale=ds_)
         gp["PASS"] = bool(gp["pass_second_order"] and gp["pass_five_point"] and gp["richardson_error"] is not None and gp["richardson_error"] <= t)
         # the same decision with F = 0 (Richardson is floor-free already; its pair is the first passing F = 0 pair)
         eg0 = {h: per_group[f"{h:.0e}"]["second_order_F0"].get(gname) for h in hs}
         eg0_f = {h: (v if v is not None else float("inf")) for h, v in eg0.items()}
-        gp["richardson_error_F0"], gp["richardson_pair_F0"] = best_richardson(lad, dcol, eg0_f, hs, t, scale, None, mask=mask)
+        gp["richardson_error_F0"], gp["richardson_pair_F0"] = best_richardson(lad, dcol, eg0_f, hs, t, scale, None, mask=mask, dscale=ds_)
         gp["PASS_rel"] = bool(gp["pass_second_order_F0"] and gp["pass_five_point_F0"] and gp["richardson_error_F0"] is not None and gp["richardson_error_F0"] <= t)
         gp["absolute_only"] = bool(gp["PASS"] and not gp["PASS_rel"])          # specification 3.0 (c): passes only because of the floor (lead 23:24Z item 3)
     active_same = None
@@ -289,8 +292,8 @@
                 pass_rule=pr, richardson_error=rich, richardson_pair=rich_pair, pass_rule_F0=pr0, richardson_error_F0=rich0, richardson_pair_F0=rich0_pair, group_pass=group_pass, PASS=bool(ok), PASS_rel=bool(ok_rel), absolute_only=bool(ok and not ok_rel),
                 active_set_base_recorded=bool(active) and (0.0 in active),
                 column_norm=float(dcol.norm()), active_sets_identical=active_same,
-                active_sets=({f"{t:+.1e}": a for t, a in active.items()} if active else None), step_scale=scale,
-                scaling_convention="v4 (2026-10-29, V179, V187): base active set recorded and compared; Richardson over all adjacent passing pairs (3.0 (d)); v3: d and D_h multiplied by the step scale s_j against the fixed floor F = 1e-10 ||r_block|| (specification 3.0 (b')(1)); Richardson judged with F (3.0 (d)(iii)); the F = 0 variants are scale-free")
+                active_sets=({f"{t:+.1e}": a for t, a in active.items()} if active else None), step_scale=scale, derivative_scale=ds_,
+                scaling_convention="v5 (2026-10-29, V190: derivative_scale separate from step_scale; physical omega judged in physical units) v4 (V179, V187): base active set recorded and compared; Richardson over all adjacent passing pairs (3.0 (d)); v3: d and D_h multiplied by the step scale s_j against the fixed floor F = 1e-10 ||r_block|| (specification 3.0 (b')(1)); Richardson judged with F (3.0 (d)(iii)); the F = 0 variants are scale-free")
 
 
 def run_case(case, quick=False, n_coef_cols=20, seed=11, save=None, sections=("G1", "G2G4", "G3", "G5")):
@@ -337,7 +340,9 @@
         def rec_of(k, t, extra=None):
             r = dict(column=k, PASS=t["PASS"], PASS_rel=t["PASS_rel"], absolute_only=t["absolute_only"], errors=t["errors_second_order"], errors_five_point=t["errors_five_point"],
                      errors_second_order_F0=t["errors_second_order_F0"], richardson=t["richardson_error"], richardson_F0=t["richardson_error_F0"], norm=t["column_norm"], step_scale=t["step_scale"],
-                     active_sets_identical=t["active_sets_identical"], per_group=t["per_group"], group_pass=t["group_pass"], pass_rule=t["pass_rule"], pass_rule_F0=t["pass_rule_F0"])
+                     active_sets_identical=t["active_sets_identical"], per_group=t["per_group"], group_pass=t["group_pass"], pass_rule=t["pass_rule"], pass_rule_F0=t["pass_rule_F0"],
+                     active_sets=t.get("active_sets"), active_set_base_recorded=t.get("active_set_base_recorded"), richardson_pair=t.get("richardson_pair"), richardson_pair_F0=t.get("richardson_pair_F0"),
+                     errors_five_point_F0=t.get("errors_five_point_F0"), derivative_scale=t.get("derivative_scale"), scaling_convention=t.get("scaling_convention"))
             if extra:
                 r.update(extra)
             return r
@@ -388,7 +393,7 @@
                 scale = 1.0
                 if coords == "physical" and pname == "omega" and case.pair[1] < 0.5:
                     scale = case.pair[1]                                                   # relative step at small omega (specification 3.0 (b))
-                g1[f"{coords}:{pname}"] = column_test(case, f"G1 J_f column {pname} ({coords})", Jp[:, j], frozen_fun, zc, e, hs, ref=case.r, scale=scale)
+                g1[f"{coords}:{pname}"] = column_test(case, f"G1 J_f column {pname} ({coords})", Jp[:, j], frozen_fun, zc, e, hs, ref=case.r, scale=scale, deriv_scale=1.0)
         out["G1_Jf_param_columns"] = g1
         # ---------------- G1: PRODUCTION Jacobian J_cw (weights differentiated, closure target lagged) parameter columns ----------------
         g1w = {}
@@ -399,7 +404,7 @@
             for j, pname in enumerate(("c_l", "omega") if coords == "physical" else ("z_c", "z_w")):
                 e = torch.zeros_like(zc); e[n - 2 + j] = 1.0
                 scale = case.pair[1] if (coords == "physical" and pname == "omega" and case.pair[1] < 0.5) else 1.0
-                g1w[f"{coords}:{pname}"] = column_test(case, f"G1 J_cw column {pname} ({coords}, production: weights differentiated)", Jpw[:, j], ref_w, zc, e, hs, ref=case.r, record_active=lambda q, tf=to_full: act(tf(q)), scale=scale)
+                g1w[f"{coords}:{pname}"] = column_test(case, f"G1 J_cw column {pname} ({coords}, production: weights differentiated)", Jpw[:, j], ref_w, zc, e, hs, ref=case.r, record_active=lambda q, tf=to_full: act(tf(q)), scale=scale, deriv_scale=1.0)
         out["G1_Jcw_param_columns"] = g1w
         # ---------------- G1: complete Jacobian J_c parameter columns vs the self-consistent residual ----------------
         g1c = {}
@@ -426,7 +431,7 @@
                 col = jc_param_column(zc, to_full, j)
                 e = torch.zeros_like(zc); e[n - 2 + j] = 1.0
                 scale = case.pair[1] if (coords == "physical" and pname == "omega" and case.pair[1] < 0.5) else 1.0
-                g1c[f"{coords}:{pname}"] = column_test(case, f"G1 J_c column {pname} ({coords}, self-consistent residual)", col, sc_fun, zc, e, hs, ref=case.r, record_active=lambda q, tf=to_full: act(tf(q)), scale=scale)
+                g1c[f"{coords}:{pname}"] = column_test(case, f"G1 J_c column {pname} ({coords}, self-consistent residual)", col, sc_fun, zc, e, hs, ref=case.r, record_active=lambda q, tf=to_full: act(tf(q)), scale=scale, deriv_scale=1.0)
         out["G1_Jc_param_columns"] = g1c
         # ---------------- G1: random coefficient columns (J_f vs residual_vector; J_cw vs residual_vector_wd; J_c vs objective_at) ----------------
         run_coef_columns(("Jf", "Jcw", "Jc"))
@@ -555,7 +560,7 @@
         for dname, v in E.items():
             dpred = float(g_c @ v); dfro = float(g_frozen @ v)
             c0 = case.cost
-            vals = {}; act_rec = {}
+            vals = {}; act_rec = {0.0: act_o(zo)}                                   # v5 (V190): the base active set is part of the comparison
             def f(t):
                 if t not in vals:
                     vals[t] = O1(zo + t * v); act_rec[t] = act_o(zo + t * v)
@@ -588,7 +593,7 @@
             chain = dsc["dcl_dzc"] if j == 0 else dsc["domega_dzw"]
             dpred = float(g_c[-2 + j]) / chain                       # dO1/dp at FIXED REDUCED coordinates a (the physical reference O1(tc.expand(z_phys)))
             scale = case.pair[1] if (pname == "omega" and case.pair[1] < 0.5) else 1.0
-            errs = {}; errs4 = {}; Ds = {}; act_rec = {}
+            errs = {}; errs4 = {}; Ds = {}; act_rec = {0.0: act(case.to_full_phys(zp))}      # v5 (V190): base active set
             vals = {}
             def f(t):
                 if t not in vals:
```

## diff validation/g8_controls.py.v3_8ca7ae0f -> validation/g8_controls.py
```
--- validation/g8_controls.py.v3_8ca7ae0f	2026-10-29 07:02:13.482567531 +0000
+++ validation/g8_controls.py	2026-10-29 07:02:13.532567639 +0000
@@ -30,7 +30,7 @@
         for j, pname in enumerate(("c_l", "omega")):
             e = torch.zeros_like(zp); e[n - 2 + j] = 1.0
             scale = case.pair[1] if (pname == "omega" and case.pair[1] < 0.5) else 1.0
-            t = column_test(case, f"G8 {name} {pname}", Jp[:, j], frozen_fun, zp, e, hs, ref=case.r, scale=scale)
+            t = column_test(case, f"G8 {name} {pname}", Jp[:, j], frozen_fun, zp, e, hs, ref=case.r, scale=scale, deriv_scale=1.0)   # v5 (V190): physical omega judged in physical units
             omitted_rel = float((Jp[:, j] - Jp_ok[:, j]).norm() / Jp_ok[:, j].norm())
             omitted_per_group = {}                                            # lead 06:23Z: the omitted part's norm per group and block, relative to the column
             for gi, gname in enumerate(case.group_names):
```

## diff validation/g3_addon.py.v2_613531ee -> validation/g3_addon.py
```
--- validation/g3_addon.py.v2_613531ee	2026-10-29 07:02:13.482567531 +0000
+++ validation/g3_addon.py	2026-10-29 07:02:13.532567639 +0000
@@ -144,7 +144,7 @@
 def main():
     ap = argparse.ArgumentParser(); ap.add_argument("--tag", required=True); ap.add_argument("--cases", default="S01_own,S05_own,manu_small_omega,manu_large_omega"); ap.add_argument("--quick", action="store_true")
     a = ap.parse_args(); dev = ("cuda:0" if torch.cuda.is_available() else "cpu")      # CPU after the GPU revocation of 2026-10-29T00:57:59Z
-    defs = {"S01_own": dict(start=os.path.join(ROOT, "starts", "S01_nest6_cl0.45_om1.0_p0.pt")), "S05_own": dict(start=os.path.join(ROOT, "starts", "S05_nest6_cl0.45_om0.3_p0.pt")),
+    defs = {"S01_own": dict(start=os.path.join(ROOT, "starts", "S01_nest6_cl0.45_om1.0_p0.pt")), "S09_own": dict(start=os.path.join(ROOT, "starts", "S09_d6w_cl0.45_om0.3_R1.pt")), "S11_own": dict(start=os.path.join(ROOT, "starts", "S11_nest6_cl0.42_om0.3_p0.pt")), "S20_own": dict(start=os.path.join(ROOT, "starts", "S20_s4allm_cl0.45_om1.0.pt")), "S05_own": dict(start=os.path.join(ROOT, "starts", "S05_nest6_cl0.45_om0.3_p0.pt")),
             "S01_shift_a": dict(start=os.path.join(ROOT, "starts", "S01_nest6_cl0.45_om1.0_p0.pt"), pair=PAIRS["a"]), "S05_shift_c": dict(start=os.path.join(ROOT, "starts", "S05_nest6_cl0.45_om0.3_p0.pt"), pair=PAIRS["c"]),
             "manu_a": dict(pair=PAIRS["a"], seed=3), "manu_small_omega": dict(pair=PAIRS["small_omega"], seed=5), "manu_large_omega": dict(pair=PAIRS["large_omega"], seed=6),
             "manu_near_edge": dict(pair=PAIRS["near_edge"], seed=7), "manu_allm_c": dict(pair=PAIRS["c"], seed=8, m_parity="all")}
```

## diff validation/g1_coverage_check.py.v2_87d4e0bd -> validation/g1_coverage_check.py
```
--- validation/g1_coverage_check.py.v2_87d4e0bd	2026-10-29 07:03:27.122734293 +0000
+++ validation/g1_coverage_check.py	2026-10-29 07:05:07.162961812 +0000
@@ -1,5 +1,11 @@
 #!/usr/bin/env python
-"""v2 (06:4xZ, V187): per-group norms divided by s_j before the comparison; records with non-identical active sets or missing decisions are invalid (fail closed).
+"""v3 (07:0xZ, V190): completeness schema before any classification: every record must have the five ladder steps, every required group, finite d, D, D4 and whole-column norms;
+exactly the registered number of distinct coefficient columns per Jacobian (20); explicit active-set validity for J_cw and J_c (the frozen-weight J_f has no changing
+weight active set: declared frozen convention); the registered outcome distinguishes INVALID (missing or incomplete evidence) from FAIL (numerical); a separate
+resolved-coverage count (>= 5) is kept. Physical-omega parameter records written by harness v3/v4 (derivative scaled by omega < 0.5 against the fixed floor,
+V190 item 2) are re-judged in physical units from the saved witnesses: per-step second-order and five-point errors are recomputed exactly from the stored
+scaled norms and errors; the F = 0 Richardson is scale-free; a floored-only Richardson pass is marked RECOMPUTE_NEEDED (not a pass).
+v2 (06:4xZ, V187): per-group norms divided by s_j before the comparison; records with non-identical active sets or missing decisions are invalid (fail closed).
 specification v1.17 3.6 (j) "small-amplitude group, post-result rule" (lead 06:22Z; V180, V183): per battery case and Jacobian (J_f, J_cw, J_c harness) the checker
 writes the REGISTERED outcome and the AMENDED outcome side by side. Fails closed: missing or non-finite records count as failures, never as small-amplitude.
 Registered outcome (3.0 (b'), (d)): every parameter column passes (whole column and every group) and every coefficient column passes (whole column and every group).
@@ -17,14 +23,66 @@
     return entry.get("Jf") if (jac == "Jf" and isinstance(entry.get("Jf"), dict)) else entry
 def col_id(entry, jac):
     return entry.get("column", col_record(entry, jac).get("column"))
+N_STEPS = 5; N_COEF = 20
+def record_complete(rec, groups, needs_active):
+    """Completeness schema (V190): five steps, every required group with finite second-order and five-point norms, finite whole-column norm, decisions present,
+    and (for J_cw / J_c) explicit identical active sets. Returns (ok, reason)."""
+    if not isinstance(rec, dict) or "PASS" not in rec or not isinstance(rec.get("group_pass"), dict):
+        return False, "decision or group decisions missing"
+    pg = rec.get("per_group")
+    if not isinstance(pg, dict) or len(pg) < N_STEPS:
+        return False, f"ladder steps recorded: {len(pg) if isinstance(pg, dict) else 0} (need {N_STEPS})"
+    cn = rec.get("norm", rec.get("column_norm"))            # coefficient records store 'norm', parameter records (column_test output) 'column_norm'
+    if not fin(cn) or cn <= 0:
+        return False, "whole-column norm missing or non-finite"
+    for h, v in pg.items():
+        for g in groups:
+            for k in ("norm_d", "norm_fd", "norm_fd_five_point"):
+                x = (v.get(k) or {}).get(g)
+                if not fin(x):
+                    return False, f"group {g} step {h}: {k} missing or non-finite"
+        for k in ("second_order", "five_point", "second_order_F0", "five_point_F0"):
+            for g in groups:
+                if not fin((v.get(k) or {}).get(g)):
+                    return False, f"group {g} step {h}: {k} missing or non-finite"
+    if needs_active and rec.get("active_sets_identical") is not True:
+        return False, f"active sets not explicitly identical ({rec.get('active_sets_identical')})"
+    return True, ""
 def record_valid(rec):
-    """A column record is valid evidence only if it is complete and its active sets are identical at every stencil point (V187)."""
+    """Validity for the decision functions: complete decisions and active sets not reported as different (the completeness schema is checked separately)."""
     return isinstance(rec, dict) and rec.get("active_sets_identical") is not False and isinstance(rec.get("group_pass"), dict) and "PASS" in rec
+def rejudge_physical_omega(rec, tau=1e-6, tau_group=1e-5):
+    """V190 item 2: a physical-omega record of harness v3/v4 (step_scale omega < 0.5, no derivative_scale field) scaled d and D_h by omega against the fixed floor.
+    From the stored scaled norms and errors the unscaled per-step errors are recomputed exactly: |d - D| s = e * max(|d| s, |D| s, F), so
+    e' = (e * den / s) / max(|d|, |D|, F). Whole-column decision: two consecutive passing steps (second order and five point) in e'; the Richardson
+    with F = 0 is scale-free (richardson_F0 <= tau suffices); otherwise RECOMPUTE_NEEDED. Returns dict(status, ...)."""
+    s_ = rec.get("step_scale", 1.0); conv = str(rec.get("scaling_convention") or "")
+    if not (fin(s_) and 0 < s_ < 1.0) or rec.get("derivative_scale") is not None or not (conv.startswith("v3") or conv.startswith("v4")):
+        return dict(status="NOT_APPLICABLE")               # only harness v3/v4 records scaled the physical derivative; v1/v2 and v5 records are in physical units
+    pg = rec.get("per_group") or {}; hs = sorted(pg.keys(), key=lambda x: -float(x))
+    def unscaled(h, g, kind):
+        v = pg[h]; nd = v["norm_d"][g]; e = v["second_order"][g] if kind == "2" else v["five_point"][g]; F = (v.get("floor") or {}).get(g, 0.0)
+        nf = v["norm_fd"][g] if kind == "2" else v["norm_fd_five_point"][g]
+        den = max(nd, nf, F); diff = e * den / s_
+        return diff / max(nd / s_, nf / s_, F, 1e-300)
+    out = dict(status=None, per_group={})
+    ok_all = True
+    for g in ["all"] + [g for g in pg[hs[0]]["second_order"] if g != "all"]:
+        t = tau if g == "all" else tau_group
+        e2 = [unscaled(h, g, "2") for h in hs]; e4 = [unscaled(h, g, "4") for h in hs]
+        p2 = any(e2[i] <= t and e2[i + 1] <= t for i in range(len(hs) - 1)); p4 = any(e4[i] <= t and e4[i + 1] <= t for i in range(len(hs) - 1))
+        r0 = rec.get("richardson_error_F0") if g == "all" else ((rec.get("group_pass") or {}).get(g) or {}).get("richardson_error_F0")
+        rich_ok = fin(r0) and r0 <= t
+        st = "PASS" if (p2 and p4 and rich_ok) else ("RECOMPUTE_NEEDED" if (p2 and p4) else "FAIL")
+        out["per_group"][g] = dict(e2_physical_units=e2, e4_physical_units=e4, pass_second_order=p2, pass_five_point=p4, richardson_F0=r0, status=st)
+        ok_all = ok_all and st == "PASS"
+    out["status"] = "PASS" if ok_all else ("RECOMPUTE_NEEDED" if all(v["status"] in ("PASS", "RECOMPUTE_NEEDED") for v in out["per_group"].values()) else "FAIL")
+    return out
 def small_amplitude(rec, g):
     """v1.17 (iii), with the normalization of V187: the per-group norms stored by column_test v3 are SCALED by the step scale s_j, the whole-column norm
     (rec['norm']) is not; the group norms are divided by s_j before the comparison with 1e-6 of the column norm. Fails closed on anything missing or
     non-finite (then not small-amplitude, and the record counts as tested)."""
-    pg = rec.get("per_group"); cn = rec.get("norm"); sj = rec.get("step_scale", 1.0)
+    pg = rec.get("per_group"); cn = rec.get("norm", rec.get("column_norm")); sj = rec.get("step_scale", 1.0)
     if not record_valid(rec) or not isinstance(pg, dict) or not pg or not fin(cn) or cn <= 0 or not fin(sj) or sj <= 0:
         return False
     for h, v in pg.items():
@@ -66,11 +124,27 @@
                 for e in cc:
                     groups |= set((col_record(e, jac).get("group_pass") or {}).keys())
                 groups.discard("all")
-                # registered outcome: every column (whole and groups) passes
-                reg_param = {k: bool(v.get("PASS")) for k, v in pc.items()}
-                reg_coef = {col_id(e, jac): bool(col_record(e, jac).get("PASS")) for e in cc}
-                registered = dict(parameter_columns=reg_param, coefficient_columns=reg_coef, n_coefficient_columns=len(cc),
-                                  PASS=(not missing_params) and bool(cc) and all(reg_param.values()) and all(reg_coef.values()))
+                # completeness schema (V190) and the registered outcome, distinguishing INVALID evidence from a numerical FAIL
+                needs_active = jac in ("Jcw", "Jc")                     # J_f: frozen weights, no changing active set (declared frozen convention)
+                groups_req = sorted(groups)
+                comp_param = {k: record_complete(v, groups_req, needs_active) for k, v in pc.items()}
+                comp_coef = {col_id(e, jac): record_complete(col_record(e, jac), groups_req, needs_active) for e in cc}
+                ids = [col_id(e, jac) for e in cc]; distinct = len(set(ids))
+                rejudge = {k: rejudge_physical_omega(v) for k, v in pc.items() if k == "physical:omega"}
+                def reg_state(k, v, comp):
+                    ok, why = comp
+                    if not ok:
+                        return "INVALID: " + why
+                    if k == "physical:omega" and rejudge.get(k, {}).get("status") not in (None, "NOT_APPLICABLE"):
+                        return "REJUDGED_" + rejudge[k]["status"] + " (harness v3/v4 scaled the physical derivative by omega; physical-unit decision from witnesses)"
+                    return "PASS" if v.get("PASS") else "FAIL"
+                reg_param = {k: reg_state(k, v, comp_param[k]) for k, v in pc.items()}
+                reg_coef = {col_id(e, jac): reg_state(None, col_record(e, jac), comp_coef[col_id(e, jac)]) for e in cc}
+                registered = dict(parameter_columns=reg_param, coefficient_columns=reg_coef, n_coefficient_records=len(cc), n_distinct_coefficient_columns=distinct,
+                                  coefficient_count_as_registered=(distinct == N_COEF and len(ids) == N_COEF), missing_parameter_columns=missing_params,
+                                  physical_omega_rejudgement=rejudge.get("physical:omega"),
+                                  PASS=(not missing_params) and distinct == N_COEF and len(ids) == N_COEF and all(v == "PASS" for v in reg_param.values()) and all(v == "PASS" for v in reg_coef.values()),
+                                  INVALID=any(str(v).startswith("INVALID") or str(v).startswith("REJUDGED_RECOMPUTE") for v in list(reg_param.values()) + list(reg_coef.values())) or bool(missing_params) or distinct != N_COEF)
                 records_v2 = bool(cc) and all(isinstance(col_record(e, jac).get("per_group"), dict) for e in cc)
                 if not records_v2:
                     cres[jac] = dict(registered=registered, amended=dict(status="RECORDS_INSUFFICIENT", reason="compact v1 coefficient records: per-group norms absent"), label=LABEL)
@@ -97,15 +171,21 @@
                     status = "PASS" if (not par_fail and not fail_cols and len(set(pass_cols)) >= MIN_COEF) else "OPEN"
                     gres[g] = dict(status=status, parameter_columns_failing_or_missing=par_fail, coefficient_columns_passing=pass_cols, coefficient_columns_failing_not_small_amplitude=fail_cols,
                                    coefficient_columns_small_amplitude_not_tested=sa, n_coverage_distinct=len(set(pass_cols)))
-                amended_pass = (not missing_params) and all(whole_param.values()) and all(whole_coef.values()) and bool(gres) and all(v["status"] == "PASS" for v in gres.values())
-                cres[jac] = dict(registered=registered, amended=dict(status=("PASS" if amended_pass else "OPEN"), whole_column_parameter=whole_param, whole_column_coefficient=whole_coef, missing_parameter_columns=missing_params, groups=gres), label=LABEL)
+                complete_all = all(c[0] for c in comp_param.values()) and all(c[0] for c in comp_coef.values()) and not missing_params and distinct == N_COEF and len(ids) == N_COEF
+                incomplete = {k: c[1] for k, c in list(comp_param.items()) + list(comp_coef.items()) if not c[0]}
+                phys_ok = all(v.get("status") in (None, "NOT_APPLICABLE", "PASS") for v in rejudge.values())
+                amended_pass = complete_all and phys_ok and all(whole_param.values()) and all(whole_coef.values()) and bool(gres) and all(v["status"] == "PASS" for v in gres.values())
+                amended_status = "PASS" if amended_pass else ("INVALID (incomplete or re-judgement pending)" if (not complete_all or not phys_ok) else "OPEN")
+                cres[jac] = dict(registered=registered, amended=dict(status=amended_status, incomplete_records=incomplete, whole_column_parameter=whole_param, whole_column_coefficient=whole_coef, missing_parameter_columns=missing_params, groups=gres,
+                                                                     resolved_coverage_counts={g: v["n_coverage_distinct"] for g, v in gres.items()}), label=LABEL)
             report["cases"][cname] = cres
         outp = f[:-5] + "_coverage.json"; json.dump(report, open(outp, "w"), indent=1)
         print(f"\n### {os.path.basename(f)} -> {os.path.basename(outp)} ({LABEL})")
         for cname, cres in report["cases"].items():
             for jac, v in cres.items():
                 am = v["amended"]
-                print(f"- {cname} {jac}: registered {'PASS' if v['registered']['PASS'] else 'FAIL'} ({sum(v['registered']['coefficient_columns'].values())}/{v['registered']['n_coefficient_columns']} coefficient columns, parameters {all(v['registered']['parameter_columns'].values()) if v['registered']['parameter_columns'] else 'missing'}); amended {am.get('status')}" + (f" ({am.get('reason')})" if am.get("reason") else ""))
+                rg = v["registered"]; npass = sum(1 for x in rg["coefficient_columns"].values() if x == "PASS")
+                print(f"- {cname} {jac}: registered {'PASS' if rg['PASS'] else ('INVALID' if rg.get('INVALID') else 'FAIL')} ({npass}/{rg['n_distinct_coefficient_columns']} distinct coefficient columns PASS; parameters {rg['parameter_columns']}); amended {am.get('status')}" + (f" ({am.get('reason')})" if am.get("reason") else "") + (f"; incomplete: {am.get('incomplete_records')}" if am.get("incomplete_records") else ""))
                 for g, gv in (am.get("groups") or {}).items():
                     print(f"    - {g}: {gv['status']}; coverage {gv['n_coverage_distinct']} distinct columns {gv['coefficient_columns_passing']}; failing (not small-amplitude) {gv['coefficient_columns_failing_not_small_amplitude']}; small-amplitude (not tested) {gv['coefficient_columns_small_amplitude_not_tested']}; parameter columns failing or missing {gv['parameter_columns_failing_or_missing']}")
 if __name__ == "__main__":
```


## addendum 5b (2026-10-29T07:06:18Z): gates.py 07c5842eb600e214 (v5a, kept as gates.py.v5a_07c5842e) -> 283fa237cb119ece (v5): best_richardson records every adjacent pair's floored/scaled Richardson error with the pair's second-order pass flag (richardson_all_pairs, richardson_all_pairs_F0; whole column and per group), as the lead's 06:59Z (b) asks; rec_of carries them. No arithmetic change.
```
--- validation/gates.py.v5a_07c5842e	2026-10-29 07:06:18.253134271 +0000
+++ validation/gates.py	2026-10-29 07:06:18.273134310 +0000
@@ -219,12 +219,13 @@
 def best_richardson(lad, dcol, errs, hs, tau, scale, ref, mask=None, dscale=None):
     """v4 (V187, specification 3.0 (d)): over ALL adjacent pairs of ladder steps whose second-order errors are both within tau, the Richardson error (floored, scaled)
     is formed and the smallest is returned with its pair (None if no pair passes). The former harness took the first passing pair only."""
-    best = None; best_pair = None
+    best = None; best_pair = None; allp = {}
     for i in range(len(hs) - 1):
-        if errs[hs[i]] <= tau and errs[hs[i + 1]] <= tau:
-            r = richardson_error(lad, dcol, (hs[i] * scale, hs[i + 1] * scale), mask=mask, scale=(scale if dscale is None else dscale), ref=ref)
-            if best is None or r < best:
-                best, best_pair = r, (f"{hs[i]:.0e}", f"{hs[i + 1]:.0e}")
+        r = richardson_error(lad, dcol, (hs[i] * scale, hs[i + 1] * scale), mask=mask, scale=(scale if dscale is None else dscale), ref=ref)
+        allp[f"{hs[i]:.0e}->{hs[i + 1]:.0e}"] = dict(richardson_error=r, pair_passes_second_order=bool(errs[hs[i]] <= tau and errs[hs[i + 1]] <= tau))   # v5 (lead 06:59Z (b)): every pair recorded
+        if errs[hs[i]] <= tau and errs[hs[i + 1]] <= tau and (best is None or r < best):
+            best, best_pair = r, (f"{hs[i]:.0e}", f"{hs[i + 1]:.0e}")
+    best_richardson.last_all = allp
     return best, best_pair
 
 
@@ -249,8 +250,8 @@
     pr = pass_rule(errs, errs4, tau_all); pr0 = pass_rule(errs0, errs40, tau_all)
     hs = sorted(errs.keys(), reverse=True)
     # Richardson: the best over all adjacent passing second-order pairs (v4; with the floor, 3.0 (d)(iii)), and the F = 0 variant
-    rich, rich_pair = best_richardson(lad, dcol, errs, hs, tau_all, scale, ref, dscale=ds_)
-    rich0, rich0_pair = best_richardson(lad, dcol, errs0, hs, tau_all, scale, None, dscale=ds_)
+    rich, rich_pair = best_richardson(lad, dcol, errs, hs, tau_all, scale, ref, dscale=ds_); rich_all = dict(best_richardson.last_all)
+    rich0, rich0_pair = best_richardson(lad, dcol, errs0, hs, tau_all, scale, None, dscale=ds_); rich0_all = dict(best_richardson.last_all)
     # group pass: every group and block within tau_group at two consecutive steps (second order) and five point; the same with F = 0 (PASS_rel)
     group_pass = {}
     for gname in ["all"] + case.group_names + (["far_anchor_block"] if (hasattr(case, "anchor_mask") and bool(case.anchor_mask.any())) else []):
@@ -273,12 +274,12 @@
         else:
             gi = case.group_names.index(gname); mask = case.row_group == gi
         eg_f = {h: (v if v is not None else float("inf")) for h, v in eg.items()}
-        gp["richardson_error"], gp["richardson_pair"] = best_richardson(lad, dcol, eg_f, hs, t, scale, ref, mask=mask, dscale=ds_)
+        gp["richardson_error"], gp["richardson_pair"] = best_richardson(lad, dcol, eg_f, hs, t, scale, ref, mask=mask, dscale=ds_); gp["richardson_all_pairs"] = dict(best_richardson.last_all)
         gp["PASS"] = bool(gp["pass_second_order"] and gp["pass_five_point"] and gp["richardson_error"] is not None and gp["richardson_error"] <= t)
         # the same decision with F = 0 (Richardson is floor-free already; its pair is the first passing F = 0 pair)
         eg0 = {h: per_group[f"{h:.0e}"]["second_order_F0"].get(gname) for h in hs}
         eg0_f = {h: (v if v is not None else float("inf")) for h, v in eg0.items()}
-        gp["richardson_error_F0"], gp["richardson_pair_F0"] = best_richardson(lad, dcol, eg0_f, hs, t, scale, None, mask=mask, dscale=ds_)
+        gp["richardson_error_F0"], gp["richardson_pair_F0"] = best_richardson(lad, dcol, eg0_f, hs, t, scale, None, mask=mask, dscale=ds_); gp["richardson_all_pairs_F0"] = dict(best_richardson.last_all)
         gp["PASS_rel"] = bool(gp["pass_second_order_F0"] and gp["pass_five_point_F0"] and gp["richardson_error_F0"] is not None and gp["richardson_error_F0"] <= t)
         gp["absolute_only"] = bool(gp["PASS"] and not gp["PASS_rel"])          # specification 3.0 (c): passes only because of the floor (lead 23:24Z item 3)
     active_same = None
@@ -289,7 +290,7 @@
     ok_rel = pr0["pass_second_order"] and pr0["pass_five_point"] and (rich0 is not None and rich0 <= tau_all) and all(v["PASS_rel"] for v in group_pass.values()) and (active_same is not False)
     return dict(label=label, errors_second_order={f"{h:.0e}": errs[h] for h in hs}, errors_five_point={f"{h:.0e}": errs4[h] for h in hs}, per_group=per_group,
                 errors_second_order_F0={f"{h:.0e}": errs0[h] for h in hs}, errors_five_point_F0={f"{h:.0e}": errs40[h] for h in hs},
-                pass_rule=pr, richardson_error=rich, richardson_pair=rich_pair, pass_rule_F0=pr0, richardson_error_F0=rich0, richardson_pair_F0=rich0_pair, group_pass=group_pass, PASS=bool(ok), PASS_rel=bool(ok_rel), absolute_only=bool(ok and not ok_rel),
+                pass_rule=pr, richardson_error=rich, richardson_pair=rich_pair, richardson_all_pairs=rich_all, pass_rule_F0=pr0, richardson_error_F0=rich0, richardson_pair_F0=rich0_pair, richardson_all_pairs_F0=rich0_all, group_pass=group_pass, PASS=bool(ok), PASS_rel=bool(ok_rel), absolute_only=bool(ok and not ok_rel),
                 active_set_base_recorded=bool(active) and (0.0 in active),
                 column_norm=float(dcol.norm()), active_sets_identical=active_same,
                 active_sets=({f"{t:+.1e}": a for t, a in active.items()} if active else None), step_scale=scale, derivative_scale=ds_,
@@ -342,7 +343,8 @@
                      errors_second_order_F0=t["errors_second_order_F0"], richardson=t["richardson_error"], richardson_F0=t["richardson_error_F0"], norm=t["column_norm"], step_scale=t["step_scale"],
                      active_sets_identical=t["active_sets_identical"], per_group=t["per_group"], group_pass=t["group_pass"], pass_rule=t["pass_rule"], pass_rule_F0=t["pass_rule_F0"],
                      active_sets=t.get("active_sets"), active_set_base_recorded=t.get("active_set_base_recorded"), richardson_pair=t.get("richardson_pair"), richardson_pair_F0=t.get("richardson_pair_F0"),
-                     errors_five_point_F0=t.get("errors_five_point_F0"), derivative_scale=t.get("derivative_scale"), scaling_convention=t.get("scaling_convention"))
+                     errors_five_point_F0=t.get("errors_five_point_F0"), derivative_scale=t.get("derivative_scale"), scaling_convention=t.get("scaling_convention"),
+                     richardson_all_pairs=t.get("richardson_all_pairs"), richardson_all_pairs_F0=t.get("richardson_all_pairs_F0"))
             if extra:
                 r.update(extra)
             return r
```
