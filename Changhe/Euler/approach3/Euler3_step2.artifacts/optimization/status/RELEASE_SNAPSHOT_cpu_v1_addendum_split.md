# Snapshot cpu_v1 addendum: gates.py section option (specification v1.11 3.5 (d), lead 04:05Z item 3); written 2026-10-29T04:12:47Z

Frozen snapshot: status/RELEASE_SNAPSHOT_cpu_v1_20261029T031921Z.md; validation/gates.py there: 73aedf35e6a3ebca (copy kept as validation/gates.py.cpu_v1_frozen).
New validation/gates.py: 8cb1c9ce7f1b109e (full sha256 8cb1c9ce7f1b109ee4b540546cd281b5e1eb1ba28816753dc68accfa5cd491e7). Nothing else in the snapshot changes (python scripts/source_state.py differs from the frozen table in this one line).

Change (control flow only): run_case(sections=("G1", "G2G4", "G3", "G5")) and main --sections. The coefficient-column draw and the five G3 normal draws are taken from one generator before the sections in the original order (cols, then 3 + 2 normals), so a part that skips G1 reproduces the directions of the unsplit run; every part records out["G1_coefficient_columns_drawn"] and out["G3_direction_hashes"] (raw_draws_sha256 in every part; scaled_directions_sha256 where G3 runs, since the scaled directions also divide by the column norms of J). The four section blocks are indented under 'if <name> in sections'; the summary and the printing tolerate absent sections. Runs of the unsplit battery already in progress (S01_own, S09_own, manu_large_omega) use the frozen file (loaded before the change).

## Unified diff ignoring whitespace changes (the substantive lines; the rest of the diff is the indentation of the four blocks)
```
--- validation/gates.py.cpu_v1_frozen	2026-10-29 04:10:13.131340068 +0000
+++ validation/gates.py	2026-10-29 04:11:54.881554954 +0000
@@ -279,7 +279,7 @@
                 active_sets=({f"{t:+.1e}": a for t, a in active.items()} if active else None), step_scale=scale)
 
 
-def run_case(case, quick=False, n_coef_cols=20, seed=11, save=None):
+def run_case(case, quick=False, n_coef_cols=20, seed=11, save=None, sections=("G1", "G2G4", "G3", "G5")):
     """save: optional callable(out) invoked after every gate section (progressive saving; both full chains of 2026-10-28 lost their results to a crash in G5)."""
     prob, model, tc, pm = case.prob, case.model, case.tc, case.pm
     dev = case.device
@@ -293,6 +293,20 @@
     def act(zz_full):
         ev = prob.evaluate(zz_full, tables=prob.pressure_tables_at(zz_full))
         return prob.nl_active_set(ev) | dict(geometry=prob.pressure.geometry_id)
+    # D6FP 2026-10-29 (specification v1.11 3.5 (d), lead 04:05Z item 3): section selection, CONTROL FLOW ONLY. The coefficient-column draw and the five G3
+    # normal draws come from one generator in the original order (cols first, then the 3 + 2 normals), so a part that skips G1 reproduces exactly
+    # the G3 directions of the unsplit run; every part records the drawn columns and SHA-256 hashes of the raw draws (and of the scaled directions,
+    # which also need the column norms of J, where G3 runs). No numerical value changes.
+    sections = tuple(sections); out["sections_run"] = list(sections)
+    rng = np.random.default_rng(seed)
+    cols = sorted(rng.choice(n - 2, size=min(n_coef_cols, n - 2), replace=False).tolist())
+    g3_draws = [rng.normal(size=n) for _ in range(5)]                                  # consumed by G3 in order: random_scaled_0..2, mixed_0..1
+    fun = lambda q: prob.residual_vector(case.to_full_opt(q))
+    out["G1_coefficient_columns_drawn"] = cols
+    out["G3_direction_hashes"] = dict(raw_draws_sha256=hashlib.sha256(b"".join(np.ascontiguousarray(u, dtype=np.float64).tobytes() for u in g3_draws)).hexdigest(),
+                                      scaled_directions_sha256=None, order=["random_scaled_0", "random_scaled_1", "random_scaled_2", "mixed_0", "mixed_1"])
+    g1 = {}; g1w = {}; g1c = {}; g2 = {}; g4 = {}; g3 = {}; g5 = {}
+    if "G1" in sections:
     # ---------------- G1: frozen-weight Jacobian J_f parameter columns (physical and optimizer coordinates) ----------------
     t0 = time.time()
     g1 = {}
@@ -346,9 +360,9 @@
             g1c[f"{coords}:{pname}"] = column_test(case, f"G1 J_c column {pname} ({coords}, self-consistent residual)", col, sc_fun, zc, e, hs, ref=case.r, record_active=lambda q, tf=to_full: act(tf(q)), scale=scale)
     out["G1_Jc_param_columns"] = g1c
     # ---------------- G1: random coefficient columns (J_f vs residual_vector; J_c vs objective_at) ----------------
-    rng = np.random.default_rng(seed)
-    cols = sorted(rng.choice(n - 2, size=min(n_coef_cols, n - 2), replace=False).tolist())
-    fun = lambda q: prob.residual_vector(case.to_full_opt(q))
+        # (rng, cols and fun are defined once before the sections; same draws, same order)
+
+
     E = torch.zeros(len(cols), n, device=dev)
     for i, k in enumerate(cols):
         E[i, k] = 1.0
@@ -395,6 +409,7 @@
     out["t_G1"] = time.time() - t0
     if save:
         save(out)
+    if "G2G4" in sections:
     # ---------------- G2 (a): assembly identity for d_p R_u; (c) U_p, DU_p vs differences; G4 (a)(b): pressure derivative ----------------
     t0 = time.time()
     g2 = {}; g4 = {}
@@ -469,6 +484,7 @@
     out["G2"] = g2; out["G4"] = g4; out["t_G2_G4"] = time.time() - t0
     if save:
         save(out)
+    if "G3" in sections:
     # ---------------- G3: complete loss gradient vs directional differences of O1 ----------------
     t0 = time.time()
     J = jacobian_fwd(fun, zo, chunk=256)
@@ -499,9 +515,10 @@
     e = torch.zeros_like(zo); e[n - 2] = 1.0; E["e_zc(optimizer)"] = e
     e = torch.zeros_like(zo); e[n - 1] = 1.0; E["e_zw(optimizer)"] = e
     for i in range(3):
-        u = torch.tensor(rng.normal(size=n), device=dev); u = u / u.norm(); E[f"random_scaled_{i}"] = u / colnorm        # unit norm in the SCALED coordinates D X
+            u = torch.tensor(g3_draws[i], device=dev); u = u / u.norm(); E[f"random_scaled_{i}"] = u / colnorm        # unit norm in the SCALED coordinates D X
     for i in range(2):
-        u = torch.tensor(rng.normal(size=n), device=dev); u = u / u.norm(); u[-2] = 0.3; u[-1] = 0.3; u = u / u.norm(); E[f"mixed_{i}"] = u / colnorm   # mixed: unit scaled norm with parameter components
+            u = torch.tensor(g3_draws[3 + i], device=dev); u = u / u.norm(); u[-2] = 0.3; u[-1] = 0.3; u = u / u.norm(); E[f"mixed_{i}"] = u / colnorm   # mixed: unit scaled norm with parameter components
+        out["G3_direction_hashes"]["scaled_directions_sha256"] = hashlib.sha256(b"".join(E[k].detach().cpu().numpy().tobytes() for k in E)).hexdigest()   # order: e_zc, e_zw, random_scaled_0..2, mixed_0..1
     g3 = {}
     def act_o(q):
         return act(case.to_full_opt(q))
@@ -563,6 +580,7 @@
     if save:
         save(out)
     del J, Jw
+    if "G5" in sections:
     # ---------------- G5 (a)(b): field consistency at sample points ----------------
     t0 = time.time()
     rng5 = np.random.default_rng(seed + 1)
@@ -612,10 +630,18 @@
     out["G5"] = g5; out["t_G5"] = time.time() - t0
     if save:
         save(out)
-    out["summary"] = dict(G1_Jf=all(v["PASS"] for v in g1.values()), G1_Jcw_production=all(v["PASS"] for v in g1w.values()), G1_Jc=all(v["PASS"] for v in g1c.values()), G1_coef_Jf=out["G1_Jf_coefficient_columns"]["all_pass"], G1_coef_Jcw=out["G1_Jcw_coefficient_columns"]["all_pass"],
-                          G1_coef_Jc=out["G1_Jc_coefficient_columns"]["all_pass"], G2a=all(v["PASS"] for k, v in g2.items() if k.startswith("G2a")), G2c=all(v["PASS"] for k, v in g2.items() if k.startswith("G2c")),
-                          G3=all(v["PASS"] for k, v in g3.items() if isinstance(v, dict) and "PASS" in v), G4a=all(v["PASS"] for k, v in g4.items() if k.startswith("G4a")),
-                          G4b=all(v["PASS"] for k, v in g4.items() if k.startswith("G4b")), G5a=g5["G5a_PASS"], G5b=g5["G5b_PASS"])
+    summ = {}
+    if "G1" in sections:
+        summ.update(G1_Jf=all(v["PASS"] for v in g1.values()), G1_Jcw_production=all(v["PASS"] for v in g1w.values()), G1_Jc=all(v["PASS"] for v in g1c.values()), G1_coef_Jf=out["G1_Jf_coefficient_columns"]["all_pass"],
+                    G1_coef_Jcw=out["G1_Jcw_coefficient_columns"]["all_pass"], G1_coef_Jc=out["G1_Jc_coefficient_columns"]["all_pass"])
+    if "G2G4" in sections:
+        summ.update(G2a=all(v["PASS"] for k, v in g2.items() if k.startswith("G2a")), G2c=all(v["PASS"] for k, v in g2.items() if k.startswith("G2c")),
+                    G4a=all(v["PASS"] for k, v in g4.items() if k.startswith("G4a")), G4b=all(v["PASS"] for k, v in g4.items() if k.startswith("G4b")))
+    if "G3" in sections:
+        summ.update(G3=all(v["PASS"] for k, v in g3.items() if isinstance(v, dict) and "PASS" in v))
+    if "G5" in sections:
+        summ.update(G5a=g5["G5a_PASS"], G5b=g5["G5b_PASS"])
+    out["summary"] = summ
     return out
 
 
@@ -623,10 +649,11 @@
     ap = argparse.ArgumentParser()
     ap.add_argument("--tag", required=True); ap.add_argument("--cases", default="S01_own,S05_own,S01_shift_a,S05_shift_c,manu_small_omega,manu_large_omega,manu_near_edge,manu_a,manu_allm_c")
     ap.add_argument("--quick", action="store_true"); ap.add_argument("--device", default=("cuda:0" if torch.cuda.is_available() else "cpu"))
+    ap.add_argument("--sections", default="G1,G2G4,G3,G5", help="specification v1.11 3.5 (d): comma-separated subset of G1,G2G4,G3,G5 (control flow only)")
     a = ap.parse_args()
     dev = a.device
     t_all = time.time()
-    results = dict(tag=a.tag, ts=time.strftime("%Y-%m-%dT%H:%M:%SZ", time.gmtime()), host=platform.node(), precision_mode=__import__("src.optimization.problem", fromlist=["PRECISION_MODE"]).PRECISION_MODE, jacobian_precision=("dd" if __import__("src.optimization.problem", fromlist=["PRECISION_MODE"]).PRECISION_MODE == "dd" else "fp64"), residual_precision=("fp64" if __import__("src.optimization.problem", fromlist=["PRECISION_MODE"]).PRECISION_MODE == "fp64" else "dd"), gpu=((torch.cuda.get_device_name(0) if torch.cuda.is_available() else "cpu") if torch.cuda.is_available() else "cpu"),
+    results = dict(tag=a.tag, sections=a.sections, ts=time.strftime("%Y-%m-%dT%H:%M:%SZ", time.gmtime()), host=platform.node(), precision_mode=__import__("src.optimization.problem", fromlist=["PRECISION_MODE"]).PRECISION_MODE, jacobian_precision=("dd" if __import__("src.optimization.problem", fromlist=["PRECISION_MODE"]).PRECISION_MODE == "dd" else "fp64"), residual_precision=("fp64" if __import__("src.optimization.problem", fromlist=["PRECISION_MODE"]).PRECISION_MODE == "fp64" else "dd"), gpu=((torch.cuda.get_device_name(0) if torch.cuda.is_available() else "cpu") if torch.cuda.is_available() else "cpu"),
                    cuda_visible=os.environ.get("CUDA_VISIBLE_DEVICES"), torch=torch.__version__, code_sha256=code_hashes(), tf32=dict(matmul=torch.backends.cuda.matmul.allow_tf32, cudnn=torch.backends.cudnn.allow_tf32),
                    ladder=H_LADDER, pairs=PAIRS, cases={})
     defs = {
@@ -649,17 +676,17 @@
         def _save(o, _name=case.name):
             results[_name] = dict(o, partial=True)
             json.dump(results, open(os.path.join(ROOT, "validation", f"gates_{a.tag}.json"), "w"), indent=1, default=str)
-        res_ = run_case(case, quick=a.quick, save=_save)
+        res_ = run_case(case, quick=a.quick, save=_save, sections=tuple(a.sections.split(",")))
         res_["seconds"] = time.time() - t0; res_["peak_GB"] = (torch.cuda.max_memory_allocated() if torch.cuda.is_available() else 0) / 2 ** 30 if torch.cuda.is_available() else 0.0
         results["cases"][cname] = res_
         print(f"  summary {json.dumps(res_['summary'])}  ({res_['seconds']:.0f}s)", flush=True)
-        for k, v in res_["G1_Jf_param_columns"].items():
+        for k, v in (res_.get("G1_Jf_param_columns") or {}).items():
             print(f"  G1 J_f {k}: e2 {json.dumps({kk: f'{vv:.1e}' for kk, vv in v['errors_second_order'].items()})} rich {v['richardson_error']} PASS {v['PASS']}", flush=True)
-        for k, v in res_["G1_Jcw_param_columns"].items():
+        for k, v in (res_.get("G1_Jcw_param_columns") or {}).items():
             print(f"  G1 J_cw(prod) {k}: e2 {json.dumps({kk: f'{vv:.1e}' for kk, vv in v['errors_second_order'].items()})} rich {v['richardson_error']} PASS {v['PASS']}", flush=True)
-        for k, v in res_["G1_Jc_param_columns"].items():
+        for k, v in (res_.get("G1_Jc_param_columns") or {}).items():
             print(f"  G1 J_c {k}: e2 {json.dumps({kk: f'{vv:.1e}' for kk, vv in v['errors_second_order'].items()})} rich {v['richardson_error']} active-sets-identical {v['active_sets_identical']} PASS {v['PASS']}", flush=True)
-        for k, v in res_["G3"].items():
+        for k, v in (res_.get("G3") or {}).items():
             if isinstance(v, dict) and "PASS" in v:
                 print(f"  G3 {k}: e2 {json.dumps({kk: f'{vv:.1e}' for kk, vv in v['errors_second_order'].items()})} rich {v.get('richardson_error')} PASS {v['PASS']}", flush=True)
         json.dump(results, open(os.path.join(ROOT, "validation", f"gates_{a.tag}.json"), "w"), indent=1, default=str)
```

## Full unified diff
```
--- validation/gates.py.cpu_v1_frozen	2026-10-29 04:10:13.131340068 +0000
+++ validation/gates.py	2026-10-29 04:11:54.881554954 +0000
@@ -279,7 +279,7 @@
                 active_sets=({f"{t:+.1e}": a for t, a in active.items()} if active else None), step_scale=scale)
 
 
-def run_case(case, quick=False, n_coef_cols=20, seed=11, save=None):
+def run_case(case, quick=False, n_coef_cols=20, seed=11, save=None, sections=("G1", "G2G4", "G3", "G5")):
     """save: optional callable(out) invoked after every gate section (progressive saving; both full chains of 2026-10-28 lost their results to a crash in G5)."""
     prob, model, tc, pm = case.prob, case.model, case.tc, case.pm
     dev = case.device
@@ -293,329 +293,355 @@
     def act(zz_full):
         ev = prob.evaluate(zz_full, tables=prob.pressure_tables_at(zz_full))
         return prob.nl_active_set(ev) | dict(geometry=prob.pressure.geometry_id)
-    # ---------------- G1: frozen-weight Jacobian J_f parameter columns (physical and optimizer coordinates) ----------------
-    t0 = time.time()
-    g1 = {}
-    for coords, zc, to_full in (("optimizer", zo, case.to_full_opt), ("physical", zp, case.to_full_phys)):
-        pfun = lambda q: prob.residual_vector(to_full(q), differentiable_pressure=True)
-        frozen_fun = lambda q: prob.residual_vector_rebuild(to_full(q))             # frozen weights and closure target, tables rebuilt, same layout
-        Jp = param_columns(pfun, zc, [n - 2, n - 1])
-        for j, pname in enumerate(("c_l", "omega") if coords == "physical" else ("z_c", "z_w")):
-            e = torch.zeros_like(zc); e[n - 2 + j] = 1.0
-            scale = 1.0
-            if coords == "physical" and pname == "omega" and case.pair[1] < 0.5:
-                scale = case.pair[1]                                                   # relative step at small omega (specification 3.0 (b))
-            g1[f"{coords}:{pname}"] = column_test(case, f"G1 J_f column {pname} ({coords})", Jp[:, j], frozen_fun, zc, e, hs, ref=case.r, scale=scale)
-    out["G1_Jf_param_columns"] = g1
-    # ---------------- G1: PRODUCTION Jacobian J_cw (weights differentiated, closure target lagged) parameter columns ----------------
-    g1w = {}
-    for coords, zc, to_full in (("optimizer", zo, case.to_full_opt), ("physical", zp, case.to_full_phys)):
-        pfun_w = lambda q: prob.residual_vector_wd(to_full(q), differentiable_pressure=True)
-        ref_w = lambda q: prob.residual_vector_rebuild_wd(to_full(q))
-        Jpw = param_columns(pfun_w, zc, [n - 2, n - 1])
-        for j, pname in enumerate(("c_l", "omega") if coords == "physical" else ("z_c", "z_w")):
-            e = torch.zeros_like(zc); e[n - 2 + j] = 1.0
-            scale = case.pair[1] if (coords == "physical" and pname == "omega" and case.pair[1] < 0.5) else 1.0
-            g1w[f"{coords}:{pname}"] = column_test(case, f"G1 J_cw column {pname} ({coords}, production: weights differentiated)", Jpw[:, j], ref_w, zc, e, hs, ref=case.r, record_active=lambda q, tf=to_full: act(tf(q)), scale=scale)
-    out["G1_Jcw_param_columns"] = g1w
-    # ---------------- G1: complete Jacobian J_c parameter columns vs the self-consistent residual ----------------
-    g1c = {}
-    def jc_param_column(zc, to_full, j):
-        # weights differentiable (forward mode), closure block by five-point differences of the fresh closure rows (production uses centered h = 1e-4)
-        def fun_wd(q):
-            zz = to_full(q)
-            tabs = prob.pressure_tables_at(zz, differentiable=True)
-            ev = prob.evaluate(zz, tables=tabs)
-            nl_w = prob.nl_weights_from_ev(ev, differentiable=True)
-            return prob.residual_vector(zz, tables=tabs, nl_w=nl_w, closure=prob.closure, ev=ev)
-        e = torch.zeros_like(zc); e[n - 2 + j] = 1.0
-        col = torch.func.jvp(fun_wd, (zc,), (e,))[1]
-        if "closure" in case.block_slices:
-            a0, a1 = case.block_slices["closure"]
-            def crow(q):
-                zz = to_full(q); return prob.closure_rows(zz, closure=prob.closure_state_at(zz))
-            h = 1e-4
-            col = col.clone(); col[a0:a1] = (8 * (crow(zc + h * e) - crow(zc - h * e)) - (crow(zc + 2 * h * e) - crow(zc - 2 * h * e))) / (12 * h)
-        return col
-    for coords, zc, to_full in (("optimizer", zo, case.to_full_opt), ("physical", zp, case.to_full_phys)):
-        sc_fun = lambda q: prob.objective_at(to_full(q), need_aux=False)[0]
-        for j, pname in enumerate(("c_l", "omega") if coords == "physical" else ("z_c", "z_w")):
-            col = jc_param_column(zc, to_full, j)
-            e = torch.zeros_like(zc); e[n - 2 + j] = 1.0
-            scale = case.pair[1] if (coords == "physical" and pname == "omega" and case.pair[1] < 0.5) else 1.0
-            g1c[f"{coords}:{pname}"] = column_test(case, f"G1 J_c column {pname} ({coords}, self-consistent residual)", col, sc_fun, zc, e, hs, ref=case.r, record_active=lambda q, tf=to_full: act(tf(q)), scale=scale)
-    out["G1_Jc_param_columns"] = g1c
-    # ---------------- G1: random coefficient columns (J_f vs residual_vector; J_c vs objective_at) ----------------
+    # D6FP 2026-10-29 (specification v1.11 3.5 (d), lead 04:05Z item 3): section selection, CONTROL FLOW ONLY. The coefficient-column draw and the five G3
+    # normal draws come from one generator in the original order (cols first, then the 3 + 2 normals), so a part that skips G1 reproduces exactly
+    # the G3 directions of the unsplit run; every part records the drawn columns and SHA-256 hashes of the raw draws (and of the scaled directions,
+    # which also need the column norms of J, where G3 runs). No numerical value changes.
+    sections = tuple(sections); out["sections_run"] = list(sections)
     rng = np.random.default_rng(seed)
     cols = sorted(rng.choice(n - 2, size=min(n_coef_cols, n - 2), replace=False).tolist())
+    g3_draws = [rng.normal(size=n) for _ in range(5)]                                  # consumed by G3 in order: random_scaled_0..2, mixed_0..1
     fun = lambda q: prob.residual_vector(case.to_full_opt(q))
-    E = torch.zeros(len(cols), n, device=dev)
-    for i, k in enumerate(cols):
-        E[i, k] = 1.0
-    Jcols = torch.func.vmap(lambda ee: torch.func.jvp(fun, (zo,), (ee,))[1])(E).T          # (rows, ncols)
-    hq = [1e-3, 1e-4, 1e-5, 1e-6] if quick else [1e-3, 1e-4, 1e-5, 1e-6, 1e-7]
-    coef_res = []
-    sc_fun_o = lambda q: prob.objective_at(case.to_full_opt(q), need_aux=False)[0]
-    # Coefficient columns: the PDE and closure rows are at most QUADRATIC in the coefficients (U linear, U.grad U and grad P quadratic), so centered
-    # differences are exact up to roundoff at any step; columns of the far-field channels (B, D, E) have norms down to 1e-11 (the conditioning
-    # problem of the basis) while the roundoff noise of r is about 2e-15, so their steps are scaled up: h_base = max(1e-3, 1e-7 / ||J col||).
-    def coef_scale(i):
-        return max(1.0, 1e-7 / max(float(Jcols[:, i].norm()), 1e-300) / 1e-3)
-    for i, k in enumerate(cols):
-        e = torch.zeros_like(zo); e[k] = 1.0
-        t_f = column_test(case, f"G1 J_f coefficient column {k}", Jcols[:, i], fun, zo, e, hq, ref=case.r, scale=coef_scale(i))
-        coef_res.append(dict(column=k, Jf=dict(PASS=t_f["PASS"], errors=t_f["errors_second_order"], richardson=t_f["richardson_error"], norm=t_f["column_norm"], step_scale=t_f["step_scale"])))
-    out["G1_Jf_coefficient_columns"] = dict(columns=cols, results=coef_res, all_pass=all(c["Jf"]["PASS"] for c in coef_res))
-    fun_w = lambda q: prob.residual_vector_wd(case.to_full_opt(q))
-    Jcols_w = torch.func.vmap(lambda ee: torch.func.jvp(fun_w, (zo,), (ee,))[1])(E).T
-    coef_w = []
-    for i, k in enumerate(cols):
-        e = torch.zeros_like(zo); e[k] = 1.0
-        t_w = column_test(case, f"G1 J_cw coefficient column {k}", Jcols_w[:, i], fun_w, zo, e, hq, ref=case.r, record_active=lambda q: act(case.to_full_opt(q)), scale=coef_scale(i))
-        coef_w.append(dict(column=k, PASS=t_w["PASS"], errors=t_w["errors_second_order"], richardson=t_w["richardson_error"], active_sets_identical=t_w["active_sets_identical"], step_scale=t_w["step_scale"], norm=t_w["column_norm"]))
-    out["G1_Jcw_coefficient_columns"] = dict(columns=cols, results=coef_w, all_pass=all(c["PASS"] for c in coef_w))
-    # J_c coefficient columns: weights differentiable + closure block by differences (at most 5 columns, cost)
-    jc_coef = []
-    def jc_coef_column(k):
-        def fun_wd(q):
-            zz = case.to_full_opt(q); tabs = prob.pressure_tables_at(zz, differentiable=True); ev = prob.evaluate(zz, tables=tabs)
-            return prob.residual_vector(zz, tables=tabs, nl_w=prob.nl_weights_from_ev(ev, differentiable=True), closure=prob.closure, ev=ev)
-        e = torch.zeros_like(zo); e[k] = 1.0
-        col = torch.func.jvp(fun_wd, (zo,), (e,))[1].clone()
-        if "closure" in case.block_slices:
-            a0, a1 = case.block_slices["closure"]; h = 1e-4
-            crow = lambda q: prob.closure_rows(case.to_full_opt(q), closure=prob.closure_state_at(case.to_full_opt(q)))
-            col[a0:a1] = (8 * (crow(zo + h * e) - crow(zo - h * e)) - (crow(zo + 2 * h * e) - crow(zo - 2 * h * e))) / (12 * h)
-        return col
-    for i, k in enumerate(cols[: (3 if quick else 20)]):
-        e = torch.zeros_like(zo); e[k] = 1.0
-        t_c = column_test(case, f"G1 J_c coefficient column {k}", jc_coef_column(k), sc_fun_o, zo, e, hq, ref=case.r, record_active=lambda q: act(case.to_full_opt(q)), scale=coef_scale(i))
-        jc_coef.append(dict(column=k, PASS=t_c["PASS"], errors=t_c["errors_second_order"], richardson=t_c["richardson_error"], active_sets_identical=t_c["active_sets_identical"]))
-    out["G1_Jc_coefficient_columns"] = dict(results=jc_coef, all_pass=all(c["PASS"] for c in jc_coef))
-    out["t_G1"] = time.time() - t0
-    if save:
-        save(out)
-    # ---------------- G2 (a): assembly identity for d_p R_u; (c) U_p, DU_p vs differences; G4 (a)(b): pressure derivative ----------------
-    t0 = time.time()
-    g2 = {}; g4 = {}
-    def fields_and_pressure(zp_):
-        zz = case.to_full_phys(zp_)
-        F = model.fields_grid(zz, need_vort=False)
-        tabs = prob.pressure_tables_at(zz, differentiable=True)
-        src = res.pressure_source(F["GU"])
-        P, gradP, _, _ = prob.pressure.solve(src, tables=tabs["main"])
-        mt = res.momentum_terms(F, gradP)
-        return F["U"], F["GU"], gradP, mt["sum"], src, F["c_l"], F["omega"]
-    U, GU, gradP, Ru, src, cl_t, om_t = fields_and_pressure(zp)
-    yv = res.yvec(model.y); Jy = res.Jvec(yv)
-    W = cl_t * yv - om_t * Jy + U
-    groups_pde = torch.where(model.r <= 0.1 * model.R0, 0, torch.where(model.r <= 2.0 ** 8 * model.R0, 1, 2))   # per node
-    def per_group_rel(a, b, resolved_only=False):
-        """relative difference per radial group of (3, Nr, Na) tensors."""
-        o = {}
-        for gi, gname in enumerate(case.group_names[:3]):
-            m = groups_pde == gi
-            if not m.any():
-                continue
-            da, db = a[:, m], b[:, m]
-            o[gname] = float((da - db).norm() / max(float(db.norm()), 1e-300))
-        return o
-    for j, pname in enumerate(("c_l", "omega")):
-        e = torch.zeros_like(zp); e[n - 2 + j] = 1.0
-        (U_, GU_, gP_, Ru_, src_, _, _), (Up, GUp, gPp, Rup, srcp, _, _) = torch.func.jvp(fields_and_pressure, (zp,), (e,))
-        # (a) formula of specification 2.4
-        if pname == "c_l":
-            lhs = -U + (1 - cl_t) * Up + torch.einsum('m...,mi...->i...', yv + Up, GU) + torch.einsum('m...,mi...->i...', W, GUp) + om_t * res.Jvec(Up) + gPp
-        else:
-            lhs = (1 - cl_t) * Up + torch.einsum('m...,mi...->i...', -Jy + Up, GU) + torch.einsum('m...,mi...->i...', W, GUp) + res.Jvec(U) + om_t * res.Jvec(Up) + gPp
-        g2[f"G2a_identity_{pname}"] = dict(per_group=per_group_rel(lhs, Rup), all=float((lhs - Rup).norm() / Rup.norm()), threshold=1e-10)
-        g2[f"G2a_identity_{pname}"]["PASS"] = all(v <= 1e-10 for v in g2[f"G2a_identity_{pname}"]["per_group"].values())
-        # (c) U_p, DU_p vs differences of U, DU at fixed a
-        def Ufun(q):
-            F = model.fields_grid(case.to_full_phys(q), need_vort=False); return torch.cat([F["U"].reshape(-1), F["GU"].reshape(-1)])
-        dcol = torch.cat([Up.reshape(-1), GUp.reshape(-1)])
-        scale = case.pair[1] if (pname == "omega" and case.pair[1] < 0.5) else 1.0
-        lad, _ = stencil_ladder(Ufun, zp, e, [h * scale for h in hs])
-        errs = {}; errs4 = {}
-        nU = U.numel()
-        node_of_U = torch.arange(nU, device=dev) // model.Na % model.Nr; node_of_G = torch.arange(GU.numel(), device=dev) // model.Na % model.Nr
-        gidx = torch.cat([groups_pde[node_of_U], groups_pde[node_of_G]])
-        pg = {}
-        for h in hs:
-            D, D4 = lad[h * scale]
-            errs[h] = float((dcol - D).norm() / max(float(D.norm()), float(dcol.norm()))); errs4[h] = float((dcol - D4).norm() / max(float(D4.norm()), float(dcol.norm())))
-            pg[f"{h:.0e}"] = {case.group_names[gi]: float((dcol[gidx == gi] - D[gidx == gi]).norm() / max(float(D[gidx == gi].norm()), 1e-300)) for gi in range(3) if (gidx == gi).any()}
-        pr = pass_rule(errs, errs4, 1e-6)
-        g2[f"G2c_Up_DUp_{pname}"] = dict(errors_second_order={f"{h:.0e}": errs[h] for h in hs}, errors_five_point={f"{h:.0e}": errs4[h] for h in hs}, per_group=pg, pass_rule=pr,
-                                        PASS=pr["pass_second_order"] and pr["pass_five_point"], step_scale=scale)
-        # G4 (a): grad P_p vs differences of grad P (tables rebuilt at each stencil point, fixed layout); per group, resolved range
-        def gPfun(q):
-            zz = case.to_full_phys(q); F = model.fields_grid(zz, need_vort=False); tabs = prob.pressure_tables_at(zz)
-            return prob.pressure.solve(res.pressure_source(F["GU"]), tables=tabs["main"])[1].reshape(-1)
-        dcol = gPp.reshape(-1); lad, _ = stencil_ladder(gPfun, zp, e, [h * scale for h in hs])
-        errs = {}; errs4 = {}; pg = {}
-        gi_g = groups_pde[node_of_U]
-        for h in hs:
-            D, D4 = lad[h * scale]
-            m = gi_g == 1
-            errs[h] = float((dcol[m] - D[m]).norm() / max(float(D[m].norm()), 1e-300)); errs4[h] = float((dcol[m] - D4[m]).norm() / max(float(D4[m].norm()), 1e-300))
-            pg[f"{h:.0e}"] = {case.group_names[gi]: float((dcol[gi_g == gi] - D[gi_g == gi]).norm() / max(float(D[gi_g == gi].norm()), 1e-300)) for gi in range(3) if (gi_g == gi).any()}
-        pr = pass_rule(errs, errs4, 1e-6)
-        g4[f"G4a_gradP_{pname}"] = dict(resolved_range_errors_second_order={f"{h:.0e}": errs[h] for h in hs}, resolved_range_errors_five_point={f"{h:.0e}": errs4[h] for h in hs}, per_group=pg, pass_rule=pr,
-                                       PASS=pr["pass_second_order"] and pr["pass_five_point"], note="resolved range = core_intermediate group; other groups reported")
-        # G4 (b): the derivative source 2 tr(DU DU_p) vs the jvp of the source actually used
-        fp = 2.0 * torch.einsum('mi...,im...->...', GU, GUp)
-        g4[f"G4b_source_{pname}"] = dict(rel=float((fp - srcp).norm() / srcp.norm()), PASS=bool(float((fp - srcp).norm() / srcp.norm()) <= 1e-12))
-    out["G2"] = g2; out["G4"] = g4; out["t_G2_G4"] = time.time() - t0
-    if save:
-        save(out)
-    # ---------------- G3: complete loss gradient vs directional differences of O1 ----------------
-    t0 = time.time()
-    J = jacobian_fwd(fun, zo, chunk=256)
-    Jp = param_columns(lambda q: prob.residual_vector(case.to_full_opt(q), differentiable_pressure=True), zo, [n - 2, n - 1])
-    J[:, n - 2] = Jp[:, 0]; J[:, n - 1] = Jp[:, 1]
-    colnorm = (J * J).sum(0).clamp_min(1e-30).sqrt()
-    g_frozen = J.T @ case.r
-    # the PRODUCTION Jacobian J_cw (weights differentiated) for the floor of G3 (specification 3.0 (c): F = 1e-3 ||r|| ||J v|| with the complete J; the closure target
-    # part of J_c is lagged in J_cw, weight 1e-3) and for the frozen-model comparison
-    fun_w2 = lambda q: prob.residual_vector_wd(case.to_full_opt(q))
-    Jw = jacobian_fwd(fun_w2, zo, chunk=256)
-    Jpw = param_columns(lambda q: prob.residual_vector_wd(case.to_full_opt(q), differentiable_pressure=True), zo, [n - 2, n - 1])
-    Jw[:, n - 2] = Jpw[:, 0]; Jw[:, n - 1] = Jpw[:, 1]
-    g_cw = Jw.T @ case.r
-    def grad_complete_opt(zo_):
-        zz = zo_.detach().clone().requires_grad_(True)
-        rr = prob.objective_graph(case.to_full_opt(zz)); c = 0.5 * (rr @ rr)
-        g, = torch.autograd.grad(c, zz); g = g.detach().clone()
-        gfull, parts = prob.complete_gradient(case.to_full_opt(zo_).detach(), return_parts=True)
-        d = pm.describe(zo_)
-        if parts["pattern_fd"] is not None:
-            g[-2] += float(parts["pattern_fd"][0]) * d["dcl_dzc"]; g[-1] += float(parts["pattern_fd"][1]) * d["domega_dzw"]
-        return g, gfull
-    g_c, g_c_full = grad_complete_opt(zo)
-    O1 = lambda q: 0.5 * float((lambda rr: rr @ rr)(prob.objective_at(case.to_full_opt(q), need_aux=False)[0]))
-    dirs = {"e_zc": None, "e_zw": None}
-    E = {}
-    e = torch.zeros_like(zo); e[n - 2] = 1.0; E["e_zc(optimizer)"] = e
-    e = torch.zeros_like(zo); e[n - 1] = 1.0; E["e_zw(optimizer)"] = e
-    for i in range(3):
-        u = torch.tensor(rng.normal(size=n), device=dev); u = u / u.norm(); E[f"random_scaled_{i}"] = u / colnorm        # unit norm in the SCALED coordinates D X
-    for i in range(2):
-        u = torch.tensor(rng.normal(size=n), device=dev); u = u / u.norm(); u[-2] = 0.3; u[-1] = 0.3; u = u / u.norm(); E[f"mixed_{i}"] = u / colnorm   # mixed: unit scaled norm with parameter components
-    g3 = {}
-    def act_o(q):
-        return act(case.to_full_opt(q))
-    for dname, v in E.items():
-        dpred = float(g_c @ v); dfro = float(g_frozen @ v)
-        c0 = case.cost
-        vals = {}; act_rec = {}
-        def f(t):
-            if t not in vals:
-                vals[t] = O1(zo + t * v); act_rec[t] = act_o(zo + t * v)
-            return vals[t]
-        errs = {}; errs4 = {}; Ds = {}
-        Fl = 1e-3 * float(case.r.norm()) * float((Jw @ v).norm())
-        D4s = {}
-        for h in hs:
-            D = (f(h) - f(-h)) / (2 * h); D4 = (8 * (f(h) - f(-h)) - (f(2 * h) - f(-2 * h))) / (12 * h)
-            errs[h] = abs(D - dpred) / max(abs(dpred), abs(D), Fl); errs4[h] = abs(D4 - dpred) / max(abs(dpred), abs(D4), Fl); Ds[f"{h:.0e}"] = D; D4s[f"{h:.0e}"] = D4
-        sc = scalar_decisions(Ds, D4s, dpred, Fl, hs)
-        keys = set(json.dumps(a, sort_keys=True) for a in act_rec.values())
-        g3[dname] = dict(derivative_complete=dpred, derivative_frozen_model=dfro, derivative_Jcw_model=float(g_cw @ v), rel_diff_frozen_vs_complete=abs(dfro - dpred) / max(abs(dpred), 1e-300),
-                         rel_diff_Jcw_vs_complete=abs(float(g_cw @ v) - dpred) / max(abs(dpred), 1e-300),
-                         fd_values={k: float(v_) for k, v_ in Ds.items()}, fd_values_five_point={k: float(v_) for k, v_ in D4s.items()}, errors_second_order={f"{h:.0e}": errs[h] for h in hs}, errors_five_point={f"{h:.0e}": errs4[h] for h in hs},
-                         floor=Fl, active_sets_identical=(len(keys) == 1), active_sets={f"{t:+.1e}": a for t, a in act_rec.items()}, **sc,
-                         PASS=bool(sc["PASS_floor_rule"] and len(keys) == 1), PASS_rel=bool(sc["PASS_rel_rule"] and len(keys) == 1))
-        g3[dname]["absolute_only"] = bool(g3[dname]["PASS"] and not g3[dname]["PASS_rel"])
-    # physical coordinates for the two parameter directions
-    g_phys = {}
-    dsc = pm.describe(zo)
-    g3["complete_gradient_parameters"] = dict(optimizer=dict(z_c=float(g_c[-2]), z_w=float(g_c[-1])), physical=dict(c_l=float(g_c[-2]) / dsc["dcl_dzc"], omega=float(g_c[-1]) / dsc["domega_dzw"]),
-                                              frozen_model_optimizer=dict(z_c=float(g_frozen[-2]), z_w=float(g_frozen[-1])),
-                                              scaled_complete={"z_c": float(g_c[-2] / (colnorm[-2] * case.r.norm())), "z_w": float(g_c[-1] / (colnorm[-1] * case.r.norm()))},
-                                              rel_diff_frozen_vs_complete_full_vector=float((g_frozen - g_c).norm() / g_c.norm()))
-    # physical-coordinate directional test for c_l and omega (fixed a): O1 as a function of z_phys
-    O1p = lambda q: 0.5 * float((lambda rr: rr @ rr)(prob.objective_at(case.to_full_phys(q), need_aux=False)[0]))
-    for j, pname in enumerate(("c_l", "omega")):
-        e = torch.zeros_like(zp); e[n - 2 + j] = 1.0
-        chain = dsc["dcl_dzc"] if j == 0 else dsc["domega_dzw"]
-        dpred = float(g_c[-2 + j]) / chain                       # dO1/dp at FIXED REDUCED coordinates a (the physical reference O1(tc.expand(z_phys)))
-        scale = case.pair[1] if (pname == "omega" and case.pair[1] < 0.5) else 1.0
-        errs = {}; errs4 = {}; Ds = {}; act_rec = {}
-        vals = {}
-        def f(t):
-            if t not in vals:
-                vals[t] = O1p(zp + t * e); act_rec[t] = act(case.to_full_phys(zp + t * e))
-            return vals[t]
-        Fl = 1e-3 * float(case.r.norm()) * float(Jpw[:, j].norm()) / chain
-        D4s = {}
-        for h in hs:
-            hh = h * scale
-            D = (f(hh) - f(-hh)) / (2 * hh); D4 = (8 * (f(hh) - f(-hh)) - (f(2 * hh) - f(-2 * hh))) / (12 * hh)
-            errs[h] = abs(D - dpred) / max(abs(dpred), abs(D), Fl); errs4[h] = abs(D4 - dpred) / max(abs(dpred), abs(D4), Fl); Ds[f"{h:.0e}"] = D; D4s[f"{h:.0e}"] = D4
-        sc = scalar_decisions(Ds, D4s, dpred, Fl, hs)
-        keys = set(json.dumps(a, sort_keys=True) for a in act_rec.values())
-        g3[f"e_{pname}(physical)"] = dict(derivative_complete=dpred, derivative_complete_full_z=float(g_c_full[-2 + j]), fd_values=Ds, fd_values_five_point=D4s, errors_second_order={f"{h:.0e}": errs[h] for h in hs},
-                                        errors_five_point={f"{h:.0e}": errs4[h] for h in hs}, floor=Fl, active_sets_identical=(len(keys) == 1), **sc,
-                                        PASS=bool(sc["PASS_floor_rule"] and len(keys) == 1), PASS_rel=bool(sc["PASS_rel_rule"] and len(keys) == 1), step_scale=scale)
-        g3[f"e_{pname}(physical)"]["absolute_only"] = bool(g3[f"e_{pname}(physical)"]["PASS"] and not g3[f"e_{pname}(physical)"]["PASS_rel"])
-    out["G3"] = g3; out["t_G3"] = time.time() - t0
-    if save:
-        save(out)
-    del J, Jw
-    # ---------------- G5 (a)(b): field consistency at sample points ----------------
-    t0 = time.time()
-    rng5 = np.random.default_rng(seed + 1)
-    radii = np.concatenate([[0.0], model.R0 * np.logspace(-3, np.log10(65536.0 / model.R0), 24)])
-    pts = []
-    for rr_ in radii:
-        if rr_ == 0.0:
-            pts.append([0.0, 0.0, 0.0]); continue
-        th = math.acos(rng5.uniform(-1, 1)); ph = rng5.uniform(0, 2 * math.pi)
-        pts.append([rr_ * math.sin(th) * math.cos(ph), rr_ * math.sin(th) * math.sin(ph), rr_ * math.cos(th)])
-    pts += [[0.0, 0.0, 0.05 * model.R0], [0.0, 0.0, 3.0 * model.R0], [0.0, 0.0, -400.0 * model.R0]]       # axis points
-    pts = torch.tensor(pts, dtype=DT, device=dev)
-    rp = pts.norm(dim=1)
-    def Upts(q, P):
-        F = model.fields_points(case.to_full_phys(q), P, need_vort=False); return F["U"], F["GU"]
-    Up_, GUp_ = Upts(zp, pts)
-    g5 = dict(points=pts.cpu().numpy().tolist(), seed=seed + 1)
-    # (a) spatial differences of U vs DU: displacement eps * max(r, 1e-3 R0) along each axis; best over eps
-    best = {0: [], 1: [], 2: []}
-    for ip in range(pts.shape[0]):
-        y0 = pts[ip]; hbase = max(float(rp[ip]), 1e-3 * model.R0)
-        errs_eps = []
-        for eps in (1e-3, 1e-4, 1e-5, 1e-6):
-            hh = eps * hbase
-            G_fd = torch.zeros(3, 3, device=dev)
-            for i in range(3):
-                e3 = torch.zeros(3, device=dev); e3[i] = hh
-                Up1, _ = Upts(zp, torch.stack([y0 + e3, y0 - e3])); G_fd[i] = (Up1[:, 0] - Up1[:, 1]) / (2 * hh)
-            errs_eps.append(float((G_fd - GUp_[:, :, ip]).norm() / max(float(GUp_[:, :, ip].norm()), 1e-300)))
-        gi = 0 if rp[ip] <= 0.1 * model.R0 else (1 if rp[ip] <= 256 * model.R0 else 2)
-        best[gi].append(min(errs_eps))
-    g5["G5a_spatial_FD_vs_DU_best_rel_per_group"] = {case.group_names[gi]: (max(v) if v else None) for gi, v in best.items()}
-    g5["G5a_PASS"] = all((max(v) if v else 0.0) <= 5e-7 for v in best.values())
-    # (b) divergence of U and of U_p at every point
-    divU = (GUp_[0, 0] + GUp_[1, 1] + GUp_[2, 2]).abs() / GUp_.reshape(9, -1).norm(dim=0).clamp_min(1e-300)
-    e = torch.zeros_like(zp); e[n - 2] = 1.0
-    (_, _), (Upc, GUpc) = torch.func.jvp(lambda q: Upts(q, pts), (zp,), (e,))
-    e = torch.zeros_like(zp); e[n - 1] = 1.0
-    (_, _), (Upw, GUpw) = torch.func.jvp(lambda q: Upts(q, pts), (zp,), (e,))
-    divc = (GUpc[0, 0] + GUpc[1, 1] + GUpc[2, 2]).abs() / GUpc.reshape(9, -1).norm(dim=0).clamp_min(1e-300)
-    divw = (GUpw[0, 0] + GUpw[1, 1] + GUpw[2, 2]).abs() / GUpw.reshape(9, -1).norm(dim=0).clamp_min(1e-300)
-    g5["G5b_div_rel_max"] = dict(U=float(divU.max()), U_c=float(divc.max()), U_w=float(divw.max()))
-    g5["G5b_PASS"] = bool(max(float(divU.max()), float(divc.max()), float(divw.max())) <= 1e-10)
-    # (c) second part: the source tr(DU^2) used by the pressure equals the one recomputed from the DU used in the residual (same tensor in this code)
-    Fg = model.fields_grid(zf, need_vort=False); s1 = res.pressure_source(Fg["GU"]); s2 = torch.einsum('mi...,im...->...', Fg["GU"], Fg["GU"])
-    g5["G5c_source_consistency_rel"] = float((s1 - s2).norm() / s2.norm())
-    out["G5"] = g5; out["t_G5"] = time.time() - t0
-    if save:
-        save(out)
-    out["summary"] = dict(G1_Jf=all(v["PASS"] for v in g1.values()), G1_Jcw_production=all(v["PASS"] for v in g1w.values()), G1_Jc=all(v["PASS"] for v in g1c.values()), G1_coef_Jf=out["G1_Jf_coefficient_columns"]["all_pass"], G1_coef_Jcw=out["G1_Jcw_coefficient_columns"]["all_pass"],
-                          G1_coef_Jc=out["G1_Jc_coefficient_columns"]["all_pass"], G2a=all(v["PASS"] for k, v in g2.items() if k.startswith("G2a")), G2c=all(v["PASS"] for k, v in g2.items() if k.startswith("G2c")),
-                          G3=all(v["PASS"] for k, v in g3.items() if isinstance(v, dict) and "PASS" in v), G4a=all(v["PASS"] for k, v in g4.items() if k.startswith("G4a")),
-                          G4b=all(v["PASS"] for k, v in g4.items() if k.startswith("G4b")), G5a=g5["G5a_PASS"], G5b=g5["G5b_PASS"])
+    out["G1_coefficient_columns_drawn"] = cols
+    out["G3_direction_hashes"] = dict(raw_draws_sha256=hashlib.sha256(b"".join(np.ascontiguousarray(u, dtype=np.float64).tobytes() for u in g3_draws)).hexdigest(),
+                                      scaled_directions_sha256=None, order=["random_scaled_0", "random_scaled_1", "random_scaled_2", "mixed_0", "mixed_1"])
+    g1 = {}; g1w = {}; g1c = {}; g2 = {}; g4 = {}; g3 = {}; g5 = {}
+    if "G1" in sections:
+        # ---------------- G1: frozen-weight Jacobian J_f parameter columns (physical and optimizer coordinates) ----------------
+        t0 = time.time()
+        g1 = {}
+        for coords, zc, to_full in (("optimizer", zo, case.to_full_opt), ("physical", zp, case.to_full_phys)):
+            pfun = lambda q: prob.residual_vector(to_full(q), differentiable_pressure=True)
+            frozen_fun = lambda q: prob.residual_vector_rebuild(to_full(q))             # frozen weights and closure target, tables rebuilt, same layout
+            Jp = param_columns(pfun, zc, [n - 2, n - 1])
+            for j, pname in enumerate(("c_l", "omega") if coords == "physical" else ("z_c", "z_w")):
+                e = torch.zeros_like(zc); e[n - 2 + j] = 1.0
+                scale = 1.0
+                if coords == "physical" and pname == "omega" and case.pair[1] < 0.5:
+                    scale = case.pair[1]                                                   # relative step at small omega (specification 3.0 (b))
+                g1[f"{coords}:{pname}"] = column_test(case, f"G1 J_f column {pname} ({coords})", Jp[:, j], frozen_fun, zc, e, hs, ref=case.r, scale=scale)
+        out["G1_Jf_param_columns"] = g1
+        # ---------------- G1: PRODUCTION Jacobian J_cw (weights differentiated, closure target lagged) parameter columns ----------------
+        g1w = {}
+        for coords, zc, to_full in (("optimizer", zo, case.to_full_opt), ("physical", zp, case.to_full_phys)):
+            pfun_w = lambda q: prob.residual_vector_wd(to_full(q), differentiable_pressure=True)
+            ref_w = lambda q: prob.residual_vector_rebuild_wd(to_full(q))
+            Jpw = param_columns(pfun_w, zc, [n - 2, n - 1])
+            for j, pname in enumerate(("c_l", "omega") if coords == "physical" else ("z_c", "z_w")):
+                e = torch.zeros_like(zc); e[n - 2 + j] = 1.0
+                scale = case.pair[1] if (coords == "physical" and pname == "omega" and case.pair[1] < 0.5) else 1.0
+                g1w[f"{coords}:{pname}"] = column_test(case, f"G1 J_cw column {pname} ({coords}, production: weights differentiated)", Jpw[:, j], ref_w, zc, e, hs, ref=case.r, record_active=lambda q, tf=to_full: act(tf(q)), scale=scale)
+        out["G1_Jcw_param_columns"] = g1w
+        # ---------------- G1: complete Jacobian J_c parameter columns vs the self-consistent residual ----------------
+        g1c = {}
+        def jc_param_column(zc, to_full, j):
+            # weights differentiable (forward mode), closure block by five-point differences of the fresh closure rows (production uses centered h = 1e-4)
+            def fun_wd(q):
+                zz = to_full(q)
+                tabs = prob.pressure_tables_at(zz, differentiable=True)
+                ev = prob.evaluate(zz, tables=tabs)
+                nl_w = prob.nl_weights_from_ev(ev, differentiable=True)
+                return prob.residual_vector(zz, tables=tabs, nl_w=nl_w, closure=prob.closure, ev=ev)
+            e = torch.zeros_like(zc); e[n - 2 + j] = 1.0
+            col = torch.func.jvp(fun_wd, (zc,), (e,))[1]
+            if "closure" in case.block_slices:
+                a0, a1 = case.block_slices["closure"]
+                def crow(q):
+                    zz = to_full(q); return prob.closure_rows(zz, closure=prob.closure_state_at(zz))
+                h = 1e-4
+                col = col.clone(); col[a0:a1] = (8 * (crow(zc + h * e) - crow(zc - h * e)) - (crow(zc + 2 * h * e) - crow(zc - 2 * h * e))) / (12 * h)
+            return col
+        for coords, zc, to_full in (("optimizer", zo, case.to_full_opt), ("physical", zp, case.to_full_phys)):
+            sc_fun = lambda q: prob.objective_at(to_full(q), need_aux=False)[0]
+            for j, pname in enumerate(("c_l", "omega") if coords == "physical" else ("z_c", "z_w")):
+                col = jc_param_column(zc, to_full, j)
+                e = torch.zeros_like(zc); e[n - 2 + j] = 1.0
+                scale = case.pair[1] if (coords == "physical" and pname == "omega" and case.pair[1] < 0.5) else 1.0
+                g1c[f"{coords}:{pname}"] = column_test(case, f"G1 J_c column {pname} ({coords}, self-consistent residual)", col, sc_fun, zc, e, hs, ref=case.r, record_active=lambda q, tf=to_full: act(tf(q)), scale=scale)
+        out["G1_Jc_param_columns"] = g1c
+        # ---------------- G1: random coefficient columns (J_f vs residual_vector; J_c vs objective_at) ----------------
+        # (rng, cols and fun are defined once before the sections; same draws, same order)
+
+
+        E = torch.zeros(len(cols), n, device=dev)
+        for i, k in enumerate(cols):
+            E[i, k] = 1.0
+        Jcols = torch.func.vmap(lambda ee: torch.func.jvp(fun, (zo,), (ee,))[1])(E).T          # (rows, ncols)
+        hq = [1e-3, 1e-4, 1e-5, 1e-6] if quick else [1e-3, 1e-4, 1e-5, 1e-6, 1e-7]
+        coef_res = []
+        sc_fun_o = lambda q: prob.objective_at(case.to_full_opt(q), need_aux=False)[0]
+        # Coefficient columns: the PDE and closure rows are at most QUADRATIC in the coefficients (U linear, U.grad U and grad P quadratic), so centered
+        # differences are exact up to roundoff at any step; columns of the far-field channels (B, D, E) have norms down to 1e-11 (the conditioning
+        # problem of the basis) while the roundoff noise of r is about 2e-15, so their steps are scaled up: h_base = max(1e-3, 1e-7 / ||J col||).
+        def coef_scale(i):
+            return max(1.0, 1e-7 / max(float(Jcols[:, i].norm()), 1e-300) / 1e-3)
+        for i, k in enumerate(cols):
+            e = torch.zeros_like(zo); e[k] = 1.0
+            t_f = column_test(case, f"G1 J_f coefficient column {k}", Jcols[:, i], fun, zo, e, hq, ref=case.r, scale=coef_scale(i))
+            coef_res.append(dict(column=k, Jf=dict(PASS=t_f["PASS"], errors=t_f["errors_second_order"], richardson=t_f["richardson_error"], norm=t_f["column_norm"], step_scale=t_f["step_scale"])))
+        out["G1_Jf_coefficient_columns"] = dict(columns=cols, results=coef_res, all_pass=all(c["Jf"]["PASS"] for c in coef_res))
+        fun_w = lambda q: prob.residual_vector_wd(case.to_full_opt(q))
+        Jcols_w = torch.func.vmap(lambda ee: torch.func.jvp(fun_w, (zo,), (ee,))[1])(E).T
+        coef_w = []
+        for i, k in enumerate(cols):
+            e = torch.zeros_like(zo); e[k] = 1.0
+            t_w = column_test(case, f"G1 J_cw coefficient column {k}", Jcols_w[:, i], fun_w, zo, e, hq, ref=case.r, record_active=lambda q: act(case.to_full_opt(q)), scale=coef_scale(i))
+            coef_w.append(dict(column=k, PASS=t_w["PASS"], errors=t_w["errors_second_order"], richardson=t_w["richardson_error"], active_sets_identical=t_w["active_sets_identical"], step_scale=t_w["step_scale"], norm=t_w["column_norm"]))
+        out["G1_Jcw_coefficient_columns"] = dict(columns=cols, results=coef_w, all_pass=all(c["PASS"] for c in coef_w))
+        # J_c coefficient columns: weights differentiable + closure block by differences (at most 5 columns, cost)
+        jc_coef = []
+        def jc_coef_column(k):
+            def fun_wd(q):
+                zz = case.to_full_opt(q); tabs = prob.pressure_tables_at(zz, differentiable=True); ev = prob.evaluate(zz, tables=tabs)
+                return prob.residual_vector(zz, tables=tabs, nl_w=prob.nl_weights_from_ev(ev, differentiable=True), closure=prob.closure, ev=ev)
+            e = torch.zeros_like(zo); e[k] = 1.0
+            col = torch.func.jvp(fun_wd, (zo,), (e,))[1].clone()
+            if "closure" in case.block_slices:
+                a0, a1 = case.block_slices["closure"]; h = 1e-4
+                crow = lambda q: prob.closure_rows(case.to_full_opt(q), closure=prob.closure_state_at(case.to_full_opt(q)))
+                col[a0:a1] = (8 * (crow(zo + h * e) - crow(zo - h * e)) - (crow(zo + 2 * h * e) - crow(zo - 2 * h * e))) / (12 * h)
+            return col
+        for i, k in enumerate(cols[: (3 if quick else 20)]):
+            e = torch.zeros_like(zo); e[k] = 1.0
+            t_c = column_test(case, f"G1 J_c coefficient column {k}", jc_coef_column(k), sc_fun_o, zo, e, hq, ref=case.r, record_active=lambda q: act(case.to_full_opt(q)), scale=coef_scale(i))
+            jc_coef.append(dict(column=k, PASS=t_c["PASS"], errors=t_c["errors_second_order"], richardson=t_c["richardson_error"], active_sets_identical=t_c["active_sets_identical"]))
+        out["G1_Jc_coefficient_columns"] = dict(results=jc_coef, all_pass=all(c["PASS"] for c in jc_coef))
+        out["t_G1"] = time.time() - t0
+        if save:
+            save(out)
+    if "G2G4" in sections:
+        # ---------------- G2 (a): assembly identity for d_p R_u; (c) U_p, DU_p vs differences; G4 (a)(b): pressure derivative ----------------
+        t0 = time.time()
+        g2 = {}; g4 = {}
+        def fields_and_pressure(zp_):
+            zz = case.to_full_phys(zp_)
+            F = model.fields_grid(zz, need_vort=False)
+            tabs = prob.pressure_tables_at(zz, differentiable=True)
+            src = res.pressure_source(F["GU"])
+            P, gradP, _, _ = prob.pressure.solve(src, tables=tabs["main"])
+            mt = res.momentum_terms(F, gradP)
+            return F["U"], F["GU"], gradP, mt["sum"], src, F["c_l"], F["omega"]
+        U, GU, gradP, Ru, src, cl_t, om_t = fields_and_pressure(zp)
+        yv = res.yvec(model.y); Jy = res.Jvec(yv)
+        W = cl_t * yv - om_t * Jy + U
+        groups_pde = torch.where(model.r <= 0.1 * model.R0, 0, torch.where(model.r <= 2.0 ** 8 * model.R0, 1, 2))   # per node
+        def per_group_rel(a, b, resolved_only=False):
+            """relative difference per radial group of (3, Nr, Na) tensors."""
+            o = {}
+            for gi, gname in enumerate(case.group_names[:3]):
+                m = groups_pde == gi
+                if not m.any():
+                    continue
+                da, db = a[:, m], b[:, m]
+                o[gname] = float((da - db).norm() / max(float(db.norm()), 1e-300))
+            return o
+        for j, pname in enumerate(("c_l", "omega")):
+            e = torch.zeros_like(zp); e[n - 2 + j] = 1.0
+            (U_, GU_, gP_, Ru_, src_, _, _), (Up, GUp, gPp, Rup, srcp, _, _) = torch.func.jvp(fields_and_pressure, (zp,), (e,))
+            # (a) formula of specification 2.4
+            if pname == "c_l":
+                lhs = -U + (1 - cl_t) * Up + torch.einsum('m...,mi...->i...', yv + Up, GU) + torch.einsum('m...,mi...->i...', W, GUp) + om_t * res.Jvec(Up) + gPp
+            else:
+                lhs = (1 - cl_t) * Up + torch.einsum('m...,mi...->i...', -Jy + Up, GU) + torch.einsum('m...,mi...->i...', W, GUp) + res.Jvec(U) + om_t * res.Jvec(Up) + gPp
+            g2[f"G2a_identity_{pname}"] = dict(per_group=per_group_rel(lhs, Rup), all=float((lhs - Rup).norm() / Rup.norm()), threshold=1e-10)
+            g2[f"G2a_identity_{pname}"]["PASS"] = all(v <= 1e-10 for v in g2[f"G2a_identity_{pname}"]["per_group"].values())
+            # (c) U_p, DU_p vs differences of U, DU at fixed a
+            def Ufun(q):
+                F = model.fields_grid(case.to_full_phys(q), need_vort=False); return torch.cat([F["U"].reshape(-1), F["GU"].reshape(-1)])
+            dcol = torch.cat([Up.reshape(-1), GUp.reshape(-1)])
+            scale = case.pair[1] if (pname == "omega" and case.pair[1] < 0.5) else 1.0
+            lad, _ = stencil_ladder(Ufun, zp, e, [h * scale for h in hs])
+            errs = {}; errs4 = {}
+            nU = U.numel()
+            node_of_U = torch.arange(nU, device=dev) // model.Na % model.Nr; node_of_G = torch.arange(GU.numel(), device=dev) // model.Na % model.Nr
+            gidx = torch.cat([groups_pde[node_of_U], groups_pde[node_of_G]])
+            pg = {}
+            for h in hs:
+                D, D4 = lad[h * scale]
+                errs[h] = float((dcol - D).norm() / max(float(D.norm()), float(dcol.norm()))); errs4[h] = float((dcol - D4).norm() / max(float(D4.norm()), float(dcol.norm())))
+                pg[f"{h:.0e}"] = {case.group_names[gi]: float((dcol[gidx == gi] - D[gidx == gi]).norm() / max(float(D[gidx == gi].norm()), 1e-300)) for gi in range(3) if (gidx == gi).any()}
+            pr = pass_rule(errs, errs4, 1e-6)
+            g2[f"G2c_Up_DUp_{pname}"] = dict(errors_second_order={f"{h:.0e}": errs[h] for h in hs}, errors_five_point={f"{h:.0e}": errs4[h] for h in hs}, per_group=pg, pass_rule=pr,
+                                            PASS=pr["pass_second_order"] and pr["pass_five_point"], step_scale=scale)
+            # G4 (a): grad P_p vs differences of grad P (tables rebuilt at each stencil point, fixed layout); per group, resolved range
+            def gPfun(q):
+                zz = case.to_full_phys(q); F = model.fields_grid(zz, need_vort=False); tabs = prob.pressure_tables_at(zz)
+                return prob.pressure.solve(res.pressure_source(F["GU"]), tables=tabs["main"])[1].reshape(-1)
+            dcol = gPp.reshape(-1); lad, _ = stencil_ladder(gPfun, zp, e, [h * scale for h in hs])
+            errs = {}; errs4 = {}; pg = {}
+            gi_g = groups_pde[node_of_U]
+            for h in hs:
+                D, D4 = lad[h * scale]
+                m = gi_g == 1
+                errs[h] = float((dcol[m] - D[m]).norm() / max(float(D[m].norm()), 1e-300)); errs4[h] = float((dcol[m] - D4[m]).norm() / max(float(D4[m].norm()), 1e-300))
+                pg[f"{h:.0e}"] = {case.group_names[gi]: float((dcol[gi_g == gi] - D[gi_g == gi]).norm() / max(float(D[gi_g == gi].norm()), 1e-300)) for gi in range(3) if (gi_g == gi).any()}
+            pr = pass_rule(errs, errs4, 1e-6)
+            g4[f"G4a_gradP_{pname}"] = dict(resolved_range_errors_second_order={f"{h:.0e}": errs[h] for h in hs}, resolved_range_errors_five_point={f"{h:.0e}": errs4[h] for h in hs}, per_group=pg, pass_rule=pr,
+                                           PASS=pr["pass_second_order"] and pr["pass_five_point"], note="resolved range = core_intermediate group; other groups reported")
+            # G4 (b): the derivative source 2 tr(DU DU_p) vs the jvp of the source actually used
+            fp = 2.0 * torch.einsum('mi...,im...->...', GU, GUp)
+            g4[f"G4b_source_{pname}"] = dict(rel=float((fp - srcp).norm() / srcp.norm()), PASS=bool(float((fp - srcp).norm() / srcp.norm()) <= 1e-12))
+        out["G2"] = g2; out["G4"] = g4; out["t_G2_G4"] = time.time() - t0
+        if save:
+            save(out)
+    if "G3" in sections:
+        # ---------------- G3: complete loss gradient vs directional differences of O1 ----------------
+        t0 = time.time()
+        J = jacobian_fwd(fun, zo, chunk=256)
+        Jp = param_columns(lambda q: prob.residual_vector(case.to_full_opt(q), differentiable_pressure=True), zo, [n - 2, n - 1])
+        J[:, n - 2] = Jp[:, 0]; J[:, n - 1] = Jp[:, 1]
+        colnorm = (J * J).sum(0).clamp_min(1e-30).sqrt()
+        g_frozen = J.T @ case.r
+        # the PRODUCTION Jacobian J_cw (weights differentiated) for the floor of G3 (specification 3.0 (c): F = 1e-3 ||r|| ||J v|| with the complete J; the closure target
+        # part of J_c is lagged in J_cw, weight 1e-3) and for the frozen-model comparison
+        fun_w2 = lambda q: prob.residual_vector_wd(case.to_full_opt(q))
+        Jw = jacobian_fwd(fun_w2, zo, chunk=256)
+        Jpw = param_columns(lambda q: prob.residual_vector_wd(case.to_full_opt(q), differentiable_pressure=True), zo, [n - 2, n - 1])
+        Jw[:, n - 2] = Jpw[:, 0]; Jw[:, n - 1] = Jpw[:, 1]
+        g_cw = Jw.T @ case.r
+        def grad_complete_opt(zo_):
+            zz = zo_.detach().clone().requires_grad_(True)
+            rr = prob.objective_graph(case.to_full_opt(zz)); c = 0.5 * (rr @ rr)
+            g, = torch.autograd.grad(c, zz); g = g.detach().clone()
+            gfull, parts = prob.complete_gradient(case.to_full_opt(zo_).detach(), return_parts=True)
+            d = pm.describe(zo_)
+            if parts["pattern_fd"] is not None:
+                g[-2] += float(parts["pattern_fd"][0]) * d["dcl_dzc"]; g[-1] += float(parts["pattern_fd"][1]) * d["domega_dzw"]
+            return g, gfull
+        g_c, g_c_full = grad_complete_opt(zo)
+        O1 = lambda q: 0.5 * float((lambda rr: rr @ rr)(prob.objective_at(case.to_full_opt(q), need_aux=False)[0]))
+        dirs = {"e_zc": None, "e_zw": None}
+        E = {}
+        e = torch.zeros_like(zo); e[n - 2] = 1.0; E["e_zc(optimizer)"] = e
+        e = torch.zeros_like(zo); e[n - 1] = 1.0; E["e_zw(optimizer)"] = e
+        for i in range(3):
+            u = torch.tensor(g3_draws[i], device=dev); u = u / u.norm(); E[f"random_scaled_{i}"] = u / colnorm        # unit norm in the SCALED coordinates D X
+        for i in range(2):
+            u = torch.tensor(g3_draws[3 + i], device=dev); u = u / u.norm(); u[-2] = 0.3; u[-1] = 0.3; u = u / u.norm(); E[f"mixed_{i}"] = u / colnorm   # mixed: unit scaled norm with parameter components
+        out["G3_direction_hashes"]["scaled_directions_sha256"] = hashlib.sha256(b"".join(E[k].detach().cpu().numpy().tobytes() for k in E)).hexdigest()   # order: e_zc, e_zw, random_scaled_0..2, mixed_0..1
+        g3 = {}
+        def act_o(q):
+            return act(case.to_full_opt(q))
+        for dname, v in E.items():
+            dpred = float(g_c @ v); dfro = float(g_frozen @ v)
+            c0 = case.cost
+            vals = {}; act_rec = {}
+            def f(t):
+                if t not in vals:
+                    vals[t] = O1(zo + t * v); act_rec[t] = act_o(zo + t * v)
+                return vals[t]
+            errs = {}; errs4 = {}; Ds = {}
+            Fl = 1e-3 * float(case.r.norm()) * float((Jw @ v).norm())
+            D4s = {}
+            for h in hs:
+                D = (f(h) - f(-h)) / (2 * h); D4 = (8 * (f(h) - f(-h)) - (f(2 * h) - f(-2 * h))) / (12 * h)
+                errs[h] = abs(D - dpred) / max(abs(dpred), abs(D), Fl); errs4[h] = abs(D4 - dpred) / max(abs(dpred), abs(D4), Fl); Ds[f"{h:.0e}"] = D; D4s[f"{h:.0e}"] = D4
+            sc = scalar_decisions(Ds, D4s, dpred, Fl, hs)
+            keys = set(json.dumps(a, sort_keys=True) for a in act_rec.values())
+            g3[dname] = dict(derivative_complete=dpred, derivative_frozen_model=dfro, derivative_Jcw_model=float(g_cw @ v), rel_diff_frozen_vs_complete=abs(dfro - dpred) / max(abs(dpred), 1e-300),
+                             rel_diff_Jcw_vs_complete=abs(float(g_cw @ v) - dpred) / max(abs(dpred), 1e-300),
+                             fd_values={k: float(v_) for k, v_ in Ds.items()}, fd_values_five_point={k: float(v_) for k, v_ in D4s.items()}, errors_second_order={f"{h:.0e}": errs[h] for h in hs}, errors_five_point={f"{h:.0e}": errs4[h] for h in hs},
+                             floor=Fl, active_sets_identical=(len(keys) == 1), active_sets={f"{t:+.1e}": a for t, a in act_rec.items()}, **sc,
+                             PASS=bool(sc["PASS_floor_rule"] and len(keys) == 1), PASS_rel=bool(sc["PASS_rel_rule"] and len(keys) == 1))
+            g3[dname]["absolute_only"] = bool(g3[dname]["PASS"] and not g3[dname]["PASS_rel"])
+        # physical coordinates for the two parameter directions
+        g_phys = {}
+        dsc = pm.describe(zo)
+        g3["complete_gradient_parameters"] = dict(optimizer=dict(z_c=float(g_c[-2]), z_w=float(g_c[-1])), physical=dict(c_l=float(g_c[-2]) / dsc["dcl_dzc"], omega=float(g_c[-1]) / dsc["domega_dzw"]),
+                                                  frozen_model_optimizer=dict(z_c=float(g_frozen[-2]), z_w=float(g_frozen[-1])),
+                                                  scaled_complete={"z_c": float(g_c[-2] / (colnorm[-2] * case.r.norm())), "z_w": float(g_c[-1] / (colnorm[-1] * case.r.norm()))},
+                                                  rel_diff_frozen_vs_complete_full_vector=float((g_frozen - g_c).norm() / g_c.norm()))
+        # physical-coordinate directional test for c_l and omega (fixed a): O1 as a function of z_phys
+        O1p = lambda q: 0.5 * float((lambda rr: rr @ rr)(prob.objective_at(case.to_full_phys(q), need_aux=False)[0]))
+        for j, pname in enumerate(("c_l", "omega")):
+            e = torch.zeros_like(zp); e[n - 2 + j] = 1.0
+            chain = dsc["dcl_dzc"] if j == 0 else dsc["domega_dzw"]
+            dpred = float(g_c[-2 + j]) / chain                       # dO1/dp at FIXED REDUCED coordinates a (the physical reference O1(tc.expand(z_phys)))
+            scale = case.pair[1] if (pname == "omega" and case.pair[1] < 0.5) else 1.0
+            errs = {}; errs4 = {}; Ds = {}; act_rec = {}
+            vals = {}
+            def f(t):
+                if t not in vals:
+                    vals[t] = O1p(zp + t * e); act_rec[t] = act(case.to_full_phys(zp + t * e))
+                return vals[t]
+            Fl = 1e-3 * float(case.r.norm()) * float(Jpw[:, j].norm()) / chain
+            D4s = {}
+            for h in hs:
+                hh = h * scale
+                D = (f(hh) - f(-hh)) / (2 * hh); D4 = (8 * (f(hh) - f(-hh)) - (f(2 * hh) - f(-2 * hh))) / (12 * hh)
+                errs[h] = abs(D - dpred) / max(abs(dpred), abs(D), Fl); errs4[h] = abs(D4 - dpred) / max(abs(dpred), abs(D4), Fl); Ds[f"{h:.0e}"] = D; D4s[f"{h:.0e}"] = D4
+            sc = scalar_decisions(Ds, D4s, dpred, Fl, hs)
+            keys = set(json.dumps(a, sort_keys=True) for a in act_rec.values())
+            g3[f"e_{pname}(physical)"] = dict(derivative_complete=dpred, derivative_complete_full_z=float(g_c_full[-2 + j]), fd_values=Ds, fd_values_five_point=D4s, errors_second_order={f"{h:.0e}": errs[h] for h in hs},
+                                            errors_five_point={f"{h:.0e}": errs4[h] for h in hs}, floor=Fl, active_sets_identical=(len(keys) == 1), **sc,
+                                            PASS=bool(sc["PASS_floor_rule"] and len(keys) == 1), PASS_rel=bool(sc["PASS_rel_rule"] and len(keys) == 1), step_scale=scale)
+            g3[f"e_{pname}(physical)"]["absolute_only"] = bool(g3[f"e_{pname}(physical)"]["PASS"] and not g3[f"e_{pname}(physical)"]["PASS_rel"])
+        out["G3"] = g3; out["t_G3"] = time.time() - t0
+        if save:
+            save(out)
+        del J, Jw
+    if "G5" in sections:
+        # ---------------- G5 (a)(b): field consistency at sample points ----------------
+        t0 = time.time()
+        rng5 = np.random.default_rng(seed + 1)
+        radii = np.concatenate([[0.0], model.R0 * np.logspace(-3, np.log10(65536.0 / model.R0), 24)])
+        pts = []
+        for rr_ in radii:
+            if rr_ == 0.0:
+                pts.append([0.0, 0.0, 0.0]); continue
+            th = math.acos(rng5.uniform(-1, 1)); ph = rng5.uniform(0, 2 * math.pi)
+            pts.append([rr_ * math.sin(th) * math.cos(ph), rr_ * math.sin(th) * math.sin(ph), rr_ * math.cos(th)])
+        pts += [[0.0, 0.0, 0.05 * model.R0], [0.0, 0.0, 3.0 * model.R0], [0.0, 0.0, -400.0 * model.R0]]       # axis points
+        pts = torch.tensor(pts, dtype=DT, device=dev)
+        rp = pts.norm(dim=1)
+        def Upts(q, P):
+            F = model.fields_points(case.to_full_phys(q), P, need_vort=False); return F["U"], F["GU"]
+        Up_, GUp_ = Upts(zp, pts)
+        g5 = dict(points=pts.cpu().numpy().tolist(), seed=seed + 1)
+        # (a) spatial differences of U vs DU: displacement eps * max(r, 1e-3 R0) along each axis; best over eps
+        best = {0: [], 1: [], 2: []}
+        for ip in range(pts.shape[0]):
+            y0 = pts[ip]; hbase = max(float(rp[ip]), 1e-3 * model.R0)
+            errs_eps = []
+            for eps in (1e-3, 1e-4, 1e-5, 1e-6):
+                hh = eps * hbase
+                G_fd = torch.zeros(3, 3, device=dev)
+                for i in range(3):
+                    e3 = torch.zeros(3, device=dev); e3[i] = hh
+                    Up1, _ = Upts(zp, torch.stack([y0 + e3, y0 - e3])); G_fd[i] = (Up1[:, 0] - Up1[:, 1]) / (2 * hh)
+                errs_eps.append(float((G_fd - GUp_[:, :, ip]).norm() / max(float(GUp_[:, :, ip].norm()), 1e-300)))
+            gi = 0 if rp[ip] <= 0.1 * model.R0 else (1 if rp[ip] <= 256 * model.R0 else 2)
+            best[gi].append(min(errs_eps))
+        g5["G5a_spatial_FD_vs_DU_best_rel_per_group"] = {case.group_names[gi]: (max(v) if v else None) for gi, v in best.items()}
+        g5["G5a_PASS"] = all((max(v) if v else 0.0) <= 5e-7 for v in best.values())
+        # (b) divergence of U and of U_p at every point
+        divU = (GUp_[0, 0] + GUp_[1, 1] + GUp_[2, 2]).abs() / GUp_.reshape(9, -1).norm(dim=0).clamp_min(1e-300)
+        e = torch.zeros_like(zp); e[n - 2] = 1.0
+        (_, _), (Upc, GUpc) = torch.func.jvp(lambda q: Upts(q, pts), (zp,), (e,))
+        e = torch.zeros_like(zp); e[n - 1] = 1.0
+        (_, _), (Upw, GUpw) = torch.func.jvp(lambda q: Upts(q, pts), (zp,), (e,))
+        divc = (GUpc[0, 0] + GUpc[1, 1] + GUpc[2, 2]).abs() / GUpc.reshape(9, -1).norm(dim=0).clamp_min(1e-300)
+        divw = (GUpw[0, 0] + GUpw[1, 1] + GUpw[2, 2]).abs() / GUpw.reshape(9, -1).norm(dim=0).clamp_min(1e-300)
+        g5["G5b_div_rel_max"] = dict(U=float(divU.max()), U_c=float(divc.max()), U_w=float(divw.max()))
+        g5["G5b_PASS"] = bool(max(float(divU.max()), float(divc.max()), float(divw.max())) <= 1e-10)
+        # (c) second part: the source tr(DU^2) used by the pressure equals the one recomputed from the DU used in the residual (same tensor in this code)
+        Fg = model.fields_grid(zf, need_vort=False); s1 = res.pressure_source(Fg["GU"]); s2 = torch.einsum('mi...,im...->...', Fg["GU"], Fg["GU"])
+        g5["G5c_source_consistency_rel"] = float((s1 - s2).norm() / s2.norm())
+        out["G5"] = g5; out["t_G5"] = time.time() - t0
+        if save:
+            save(out)
+    summ = {}
+    if "G1" in sections:
+        summ.update(G1_Jf=all(v["PASS"] for v in g1.values()), G1_Jcw_production=all(v["PASS"] for v in g1w.values()), G1_Jc=all(v["PASS"] for v in g1c.values()), G1_coef_Jf=out["G1_Jf_coefficient_columns"]["all_pass"],
+                    G1_coef_Jcw=out["G1_Jcw_coefficient_columns"]["all_pass"], G1_coef_Jc=out["G1_Jc_coefficient_columns"]["all_pass"])
+    if "G2G4" in sections:
+        summ.update(G2a=all(v["PASS"] for k, v in g2.items() if k.startswith("G2a")), G2c=all(v["PASS"] for k, v in g2.items() if k.startswith("G2c")),
+                    G4a=all(v["PASS"] for k, v in g4.items() if k.startswith("G4a")), G4b=all(v["PASS"] for k, v in g4.items() if k.startswith("G4b")))
+    if "G3" in sections:
+        summ.update(G3=all(v["PASS"] for k, v in g3.items() if isinstance(v, dict) and "PASS" in v))
+    if "G5" in sections:
+        summ.update(G5a=g5["G5a_PASS"], G5b=g5["G5b_PASS"])
+    out["summary"] = summ
     return out
 
 
@@ -623,10 +649,11 @@
     ap = argparse.ArgumentParser()
     ap.add_argument("--tag", required=True); ap.add_argument("--cases", default="S01_own,S05_own,S01_shift_a,S05_shift_c,manu_small_omega,manu_large_omega,manu_near_edge,manu_a,manu_allm_c")
     ap.add_argument("--quick", action="store_true"); ap.add_argument("--device", default=("cuda:0" if torch.cuda.is_available() else "cpu"))
+    ap.add_argument("--sections", default="G1,G2G4,G3,G5", help="specification v1.11 3.5 (d): comma-separated subset of G1,G2G4,G3,G5 (control flow only)")
     a = ap.parse_args()
     dev = a.device
     t_all = time.time()
-    results = dict(tag=a.tag, ts=time.strftime("%Y-%m-%dT%H:%M:%SZ", time.gmtime()), host=platform.node(), precision_mode=__import__("src.optimization.problem", fromlist=["PRECISION_MODE"]).PRECISION_MODE, jacobian_precision=("dd" if __import__("src.optimization.problem", fromlist=["PRECISION_MODE"]).PRECISION_MODE == "dd" else "fp64"), residual_precision=("fp64" if __import__("src.optimization.problem", fromlist=["PRECISION_MODE"]).PRECISION_MODE == "fp64" else "dd"), gpu=((torch.cuda.get_device_name(0) if torch.cuda.is_available() else "cpu") if torch.cuda.is_available() else "cpu"),
+    results = dict(tag=a.tag, sections=a.sections, ts=time.strftime("%Y-%m-%dT%H:%M:%SZ", time.gmtime()), host=platform.node(), precision_mode=__import__("src.optimization.problem", fromlist=["PRECISION_MODE"]).PRECISION_MODE, jacobian_precision=("dd" if __import__("src.optimization.problem", fromlist=["PRECISION_MODE"]).PRECISION_MODE == "dd" else "fp64"), residual_precision=("fp64" if __import__("src.optimization.problem", fromlist=["PRECISION_MODE"]).PRECISION_MODE == "fp64" else "dd"), gpu=((torch.cuda.get_device_name(0) if torch.cuda.is_available() else "cpu") if torch.cuda.is_available() else "cpu"),
                    cuda_visible=os.environ.get("CUDA_VISIBLE_DEVICES"), torch=torch.__version__, code_sha256=code_hashes(), tf32=dict(matmul=torch.backends.cuda.matmul.allow_tf32, cudnn=torch.backends.cudnn.allow_tf32),
                    ladder=H_LADDER, pairs=PAIRS, cases={})
     defs = {
@@ -649,17 +676,17 @@
         def _save(o, _name=case.name):
             results[_name] = dict(o, partial=True)
             json.dump(results, open(os.path.join(ROOT, "validation", f"gates_{a.tag}.json"), "w"), indent=1, default=str)
-        res_ = run_case(case, quick=a.quick, save=_save)
+        res_ = run_case(case, quick=a.quick, save=_save, sections=tuple(a.sections.split(",")))
         res_["seconds"] = time.time() - t0; res_["peak_GB"] = (torch.cuda.max_memory_allocated() if torch.cuda.is_available() else 0) / 2 ** 30 if torch.cuda.is_available() else 0.0
         results["cases"][cname] = res_
         print(f"  summary {json.dumps(res_['summary'])}  ({res_['seconds']:.0f}s)", flush=True)
-        for k, v in res_["G1_Jf_param_columns"].items():
+        for k, v in (res_.get("G1_Jf_param_columns") or {}).items():
             print(f"  G1 J_f {k}: e2 {json.dumps({kk: f'{vv:.1e}' for kk, vv in v['errors_second_order'].items()})} rich {v['richardson_error']} PASS {v['PASS']}", flush=True)
-        for k, v in res_["G1_Jcw_param_columns"].items():
+        for k, v in (res_.get("G1_Jcw_param_columns") or {}).items():
             print(f"  G1 J_cw(prod) {k}: e2 {json.dumps({kk: f'{vv:.1e}' for kk, vv in v['errors_second_order'].items()})} rich {v['richardson_error']} PASS {v['PASS']}", flush=True)
-        for k, v in res_["G1_Jc_param_columns"].items():
+        for k, v in (res_.get("G1_Jc_param_columns") or {}).items():
             print(f"  G1 J_c {k}: e2 {json.dumps({kk: f'{vv:.1e}' for kk, vv in v['errors_second_order'].items()})} rich {v['richardson_error']} active-sets-identical {v['active_sets_identical']} PASS {v['PASS']}", flush=True)
-        for k, v in res_["G3"].items():
+        for k, v in (res_.get("G3") or {}).items():
             if isinstance(v, dict) and "PASS" in v:
                 print(f"  G3 {k}: e2 {json.dumps({kk: f'{vv:.1e}' for kk, vv in v['errors_second_order'].items()})} rich {v.get('richardson_error')} PASS {v['PASS']}", flush=True)
         json.dump(results, open(os.path.join(ROOT, "validation", f"gates_{a.tag}.json"), "w"), indent=1, default=str)
```
