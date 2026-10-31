# Snapshot gpu_v1 addendum 2 (test-only): gates.py coefficient-column records v2, scaled harness J_c closure step, sections G1_coef / G1_Jc_coef (specification v1.16 3.6 (j)(c),(d), lead 06:08Z); written 2026-10-29T06:17:10Z

validation/gates.py 8cb1c9ce7f1b109e (section addendum, used by the gpu_v1 runs of S01_own and S09_own) -> 19a86d4fcd69f404 (full sha256 19a86d4fcd69f404ee6a77b2c25ec5a90d289093f02fca155697ab1d4796a3f9); frozen copy of the previous file: validation/gates.py.gpu_v1_sections. No production source changes. Changes: (1) the coefficient-column tests (J_f, J_cw, J_c) live in run_coef_columns(which) and record, per column, the full column_test output: per group and step ||d||, ||D_h|| (second-order and five-point), floor and e (with the floor and with F = 0), the group decisions (PASS, PASS_rel, absolute_only, Richardson per group), the whole-column pass rules, active sets; (2) the harness J_c closure block uses the five-point step 1e-4 * s_j (s_j = the column's step scale max(1, 1e-7/||J_f col||/1e-3)) instead of the fixed 1e-4; the step is recorded (closure_block_step); (3) sections G1_coef (all three coefficient tests) and G1_Jc_coef (J_c only) can run alone; the summary carries their all_pass flags; (4) the G1 block itself calls run_coef_columns, so a full run is unchanged apart from the records and the closure step.

```
--- validation/gates.py.gpu_v1_sections	2026-10-29 06:14:41.946524734 +0000
+++ validation/gates.py	2026-10-29 06:16:42.186757304 +0000
@@ -306,6 +306,61 @@
     out["G3_direction_hashes"] = dict(raw_draws_sha256=hashlib.sha256(b"".join(np.ascontiguousarray(u, dtype=np.float64).tobytes() for u in g3_draws)).hexdigest(),
                                       scaled_directions_sha256=None, order=["random_scaled_0", "random_scaled_1", "random_scaled_2", "mixed_0", "mixed_1"])
     g1 = {}; g1w = {}; g1c = {}; g2 = {}; g4 = {}; g3 = {}; g5 = {}
+    def run_coef_columns(which):
+        """G1 coefficient columns (specification v1.16 3.6 (j)(c),(d), lead 06:08Z; test-only change of 2026-10-29T06:2xZ). Records per column the FULL column_test
+        output needed by the rounding-level and coverage checker: per group and step ||d||, ||D_h||, floor and e (per_group), the group decisions
+        (group_pass), the five-point errors, PASS, PASS_rel, active sets. The harness J_c closure block uses the five-point step 1e-4 * s_j, with s_j the
+        step scale of column j (was the fixed 1e-4: at rounding level for far-channel columns of norm 1e-11, diag_coef_S09_own). The PDE and closure rows
+        are at most quadratic in the coefficients, so the centered and five-point differences are exact up to rounding at any step."""
+        E = torch.zeros(len(cols), n, device=dev)
+        for i, k in enumerate(cols):
+            E[i, k] = 1.0
+        Jcols = torch.func.vmap(lambda ee: torch.func.jvp(fun, (zo,), (ee,))[1])(E).T          # (rows, ncols); also gives the step scales
+        hq = [1e-3, 1e-4, 1e-5, 1e-6] if quick else [1e-3, 1e-4, 1e-5, 1e-6, 1e-7]
+        sc_fun_o = lambda q: prob.objective_at(case.to_full_opt(q), need_aux=False)[0]
+        def coef_scale(i):
+            return max(1.0, 1e-7 / max(float(Jcols[:, i].norm()), 1e-300) / 1e-3)
+        def rec_of(k, t, extra=None):
+            r = dict(column=k, PASS=t["PASS"], PASS_rel=t["PASS_rel"], absolute_only=t["absolute_only"], errors=t["errors_second_order"], errors_five_point=t["errors_five_point"],
+                     errors_second_order_F0=t["errors_second_order_F0"], richardson=t["richardson_error"], richardson_F0=t["richardson_error_F0"], norm=t["column_norm"], step_scale=t["step_scale"],
+                     active_sets_identical=t["active_sets_identical"], per_group=t["per_group"], group_pass=t["group_pass"], pass_rule=t["pass_rule"], pass_rule_F0=t["pass_rule_F0"])
+            if extra:
+                r.update(extra)
+            return r
+        if "Jf" in which:
+            coef_res = []
+            for i, k in enumerate(cols):
+                e = torch.zeros_like(zo); e[k] = 1.0
+                t_f = column_test(case, f"G1 J_f coefficient column {k}", Jcols[:, i], fun, zo, e, hq, ref=case.r, scale=coef_scale(i))
+                coef_res.append(dict(column=k, Jf=rec_of(k, t_f)))
+            out["G1_Jf_coefficient_columns"] = dict(columns=cols, results=coef_res, all_pass=all(c["Jf"]["PASS"] for c in coef_res), record_version="v2 (full per-group records, 2026-10-29)")
+        if "Jcw" in which:
+            fun_w = lambda q: prob.residual_vector_wd(case.to_full_opt(q))
+            Jcols_w = torch.func.vmap(lambda ee: torch.func.jvp(fun_w, (zo,), (ee,))[1])(E).T
+            coef_w = []
+            for i, k in enumerate(cols):
+                e = torch.zeros_like(zo); e[k] = 1.0
+                t_w = column_test(case, f"G1 J_cw coefficient column {k}", Jcols_w[:, i], fun_w, zo, e, hq, ref=case.r, record_active=lambda q: act(case.to_full_opt(q)), scale=coef_scale(i))
+                coef_w.append(rec_of(k, t_w))
+            out["G1_Jcw_coefficient_columns"] = dict(columns=cols, results=coef_w, all_pass=all(c["PASS"] for c in coef_w), record_version="v2 (full per-group records, 2026-10-29)")
+        if "Jc" in which:
+            jc_coef = []
+            def jc_coef_column(k, scale):
+                def fun_wd(q):
+                    zz = case.to_full_opt(q); tabs = prob.pressure_tables_at(zz, differentiable=True); ev = prob.evaluate(zz, tables=tabs)
+                    return prob.residual_vector(zz, tables=tabs, nl_w=prob.nl_weights_from_ev(ev, differentiable=True), closure=prob.closure, ev=ev)
+                e = torch.zeros_like(zo); e[k] = 1.0
+                col = torch.func.jvp(fun_wd, (zo,), (e,))[1].clone()
+                if "closure" in case.block_slices:
+                    a0, a1 = case.block_slices["closure"]; h = 1e-4 * scale                    # scaled step (specification v1.16 3.6 (j)(d)); was the fixed 1e-4
+                    crow = lambda q: prob.closure_rows(case.to_full_opt(q), closure=prob.closure_state_at(case.to_full_opt(q)))
+                    col[a0:a1] = (8 * (crow(zo + h * e) - crow(zo - h * e)) - (crow(zo + 2 * h * e) - crow(zo - 2 * h * e))) / (12 * h)
+                return col
+            for i, k in enumerate(cols[: (3 if quick else 20)]):
+                e = torch.zeros_like(zo); e[k] = 1.0; sc = coef_scale(i)
+                t_c = column_test(case, f"G1 J_c coefficient column {k}", jc_coef_column(k, sc), sc_fun_o, zo, e, hq, ref=case.r, record_active=lambda q: act(case.to_full_opt(q)), scale=sc)
+                jc_coef.append(rec_of(k, t_c, extra=dict(closure_block_step=1e-4 * sc)))
+            out["G1_Jc_coefficient_columns"] = dict(columns=cols[: (3 if quick else 20)], results=jc_coef, all_pass=all(c["PASS"] for c in jc_coef), record_version="v2 (full per-group records; closure block step 1e-4 * s_j, 2026-10-29)")
     if "G1" in sections:
         # ---------------- G1: frozen-weight Jacobian J_f parameter columns (physical and optimizer coordinates) ----------------
         t0 = time.time()
@@ -359,56 +414,17 @@
                 scale = case.pair[1] if (coords == "physical" and pname == "omega" and case.pair[1] < 0.5) else 1.0
                 g1c[f"{coords}:{pname}"] = column_test(case, f"G1 J_c column {pname} ({coords}, self-consistent residual)", col, sc_fun, zc, e, hs, ref=case.r, record_active=lambda q, tf=to_full: act(tf(q)), scale=scale)
         out["G1_Jc_param_columns"] = g1c
-        # ---------------- G1: random coefficient columns (J_f vs residual_vector; J_c vs objective_at) ----------------
-        # (rng, cols and fun are defined once before the sections; same draws, same order)
-
-
-        E = torch.zeros(len(cols), n, device=dev)
-        for i, k in enumerate(cols):
-            E[i, k] = 1.0
-        Jcols = torch.func.vmap(lambda ee: torch.func.jvp(fun, (zo,), (ee,))[1])(E).T          # (rows, ncols)
-        hq = [1e-3, 1e-4, 1e-5, 1e-6] if quick else [1e-3, 1e-4, 1e-5, 1e-6, 1e-7]
-        coef_res = []
-        sc_fun_o = lambda q: prob.objective_at(case.to_full_opt(q), need_aux=False)[0]
-        # Coefficient columns: the PDE and closure rows are at most QUADRATIC in the coefficients (U linear, U.grad U and grad P quadratic), so centered
-        # differences are exact up to roundoff at any step; columns of the far-field channels (B, D, E) have norms down to 1e-11 (the conditioning
-        # problem of the basis) while the roundoff noise of r is about 2e-15, so their steps are scaled up: h_base = max(1e-3, 1e-7 / ||J col||).
-        def coef_scale(i):
-            return max(1.0, 1e-7 / max(float(Jcols[:, i].norm()), 1e-300) / 1e-3)
-        for i, k in enumerate(cols):
-            e = torch.zeros_like(zo); e[k] = 1.0
-            t_f = column_test(case, f"G1 J_f coefficient column {k}", Jcols[:, i], fun, zo, e, hq, ref=case.r, scale=coef_scale(i))
-            coef_res.append(dict(column=k, Jf=dict(PASS=t_f["PASS"], errors=t_f["errors_second_order"], richardson=t_f["richardson_error"], norm=t_f["column_norm"], step_scale=t_f["step_scale"])))
-        out["G1_Jf_coefficient_columns"] = dict(columns=cols, results=coef_res, all_pass=all(c["Jf"]["PASS"] for c in coef_res))
-        fun_w = lambda q: prob.residual_vector_wd(case.to_full_opt(q))
-        Jcols_w = torch.func.vmap(lambda ee: torch.func.jvp(fun_w, (zo,), (ee,))[1])(E).T
-        coef_w = []
-        for i, k in enumerate(cols):
-            e = torch.zeros_like(zo); e[k] = 1.0
-            t_w = column_test(case, f"G1 J_cw coefficient column {k}", Jcols_w[:, i], fun_w, zo, e, hq, ref=case.r, record_active=lambda q: act(case.to_full_opt(q)), scale=coef_scale(i))
-            coef_w.append(dict(column=k, PASS=t_w["PASS"], errors=t_w["errors_second_order"], richardson=t_w["richardson_error"], active_sets_identical=t_w["active_sets_identical"], step_scale=t_w["step_scale"], norm=t_w["column_norm"]))
-        out["G1_Jcw_coefficient_columns"] = dict(columns=cols, results=coef_w, all_pass=all(c["PASS"] for c in coef_w))
-        # J_c coefficient columns: weights differentiable + closure block by differences (at most 5 columns, cost)
-        jc_coef = []
-        def jc_coef_column(k):
-            def fun_wd(q):
-                zz = case.to_full_opt(q); tabs = prob.pressure_tables_at(zz, differentiable=True); ev = prob.evaluate(zz, tables=tabs)
-                return prob.residual_vector(zz, tables=tabs, nl_w=prob.nl_weights_from_ev(ev, differentiable=True), closure=prob.closure, ev=ev)
-            e = torch.zeros_like(zo); e[k] = 1.0
-            col = torch.func.jvp(fun_wd, (zo,), (e,))[1].clone()
-            if "closure" in case.block_slices:
-                a0, a1 = case.block_slices["closure"]; h = 1e-4
-                crow = lambda q: prob.closure_rows(case.to_full_opt(q), closure=prob.closure_state_at(case.to_full_opt(q)))
-                col[a0:a1] = (8 * (crow(zo + h * e) - crow(zo - h * e)) - (crow(zo + 2 * h * e) - crow(zo - 2 * h * e))) / (12 * h)
-            return col
-        for i, k in enumerate(cols[: (3 if quick else 20)]):
-            e = torch.zeros_like(zo); e[k] = 1.0
-            t_c = column_test(case, f"G1 J_c coefficient column {k}", jc_coef_column(k), sc_fun_o, zo, e, hq, ref=case.r, record_active=lambda q: act(case.to_full_opt(q)), scale=coef_scale(i))
-            jc_coef.append(dict(column=k, PASS=t_c["PASS"], errors=t_c["errors_second_order"], richardson=t_c["richardson_error"], active_sets_identical=t_c["active_sets_identical"]))
-        out["G1_Jc_coefficient_columns"] = dict(results=jc_coef, all_pass=all(c["PASS"] for c in jc_coef))
+        # ---------------- G1: random coefficient columns (J_f vs residual_vector; J_cw vs residual_vector_wd; J_c vs objective_at) ----------------
+        run_coef_columns(("Jf", "Jcw", "Jc"))
         out["t_G1"] = time.time() - t0
         if save:
             save(out)
+    if ("G1_coef" in sections or "G1_Jc_coef" in sections) and "G1" not in sections:          # coefficient-column sections alone (specification v1.16 3.6 (j)(d))
+        t0 = time.time()
+        run_coef_columns(("Jf", "Jcw", "Jc") if "G1_coef" in sections else ("Jc",))
+        out["t_G1_coef"] = time.time() - t0
+        if save:
+            save(out)
     if "G2G4" in sections:
         # ---------------- G2 (a): assembly identity for d_p R_u; (c) U_p, DU_p vs differences; G4 (a)(b): pressure derivative ----------------
         t0 = time.time()
@@ -634,6 +650,10 @@
     if "G1" in sections:
         summ.update(G1_Jf=all(v["PASS"] for v in g1.values()), G1_Jcw_production=all(v["PASS"] for v in g1w.values()), G1_Jc=all(v["PASS"] for v in g1c.values()), G1_coef_Jf=out["G1_Jf_coefficient_columns"]["all_pass"],
                     G1_coef_Jcw=out["G1_Jcw_coefficient_columns"]["all_pass"], G1_coef_Jc=out["G1_Jc_coefficient_columns"]["all_pass"])
+    if "G1" not in sections:
+        for key, name in (("G1_Jf_coefficient_columns", "G1_coef_Jf"), ("G1_Jcw_coefficient_columns", "G1_coef_Jcw"), ("G1_Jc_coefficient_columns", "G1_coef_Jc")):
+            if key in out:
+                summ[name] = out[key]["all_pass"]
     if "G2G4" in sections:
         summ.update(G2a=all(v["PASS"] for k, v in g2.items() if k.startswith("G2a")), G2c=all(v["PASS"] for k, v in g2.items() if k.startswith("G2c")),
                     G4a=all(v["PASS"] for k, v in g4.items() if k.startswith("G4a")), G4b=all(v["PASS"] for k, v in g4.items() if k.startswith("G4b")))
@@ -649,7 +669,7 @@
     ap = argparse.ArgumentParser()
     ap.add_argument("--tag", required=True); ap.add_argument("--cases", default="S01_own,S05_own,S01_shift_a,S05_shift_c,manu_small_omega,manu_large_omega,manu_near_edge,manu_a,manu_allm_c")
     ap.add_argument("--quick", action="store_true"); ap.add_argument("--device", default=("cuda:0" if torch.cuda.is_available() else "cpu"))
-    ap.add_argument("--sections", default="G1,G2G4,G3,G5", help="specification v1.11 3.5 (d): comma-separated subset of G1,G2G4,G3,G5 (control flow only)")
+    ap.add_argument("--sections", default="G1,G2G4,G3,G5", help="specification v1.11 3.5 (d) / v1.16 3.6 (j): comma-separated subset of G1,G2G4,G3,G5, or the coefficient-column sections G1_coef (J_f, J_cw, J_c) and G1_Jc_coef (J_c only)")
     a = ap.parse_args()
     dev = a.device
     t_all = time.time()
```
