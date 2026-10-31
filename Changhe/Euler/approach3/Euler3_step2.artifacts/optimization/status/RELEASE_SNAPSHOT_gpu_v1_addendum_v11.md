# Snapshot gpu_v1 addendum 11 (test-only): checker v9 e75ad8d910757c12 (V198 items 1 to 5, lead 07:53Z item 3); written 2026-10-29T08:02:42Z

g1_coverage_check.py e53bd772d7b7dfaa (v7) -> 2ab42ffdec74c421 (v8, companion parameter record; lived from 07:52Z to 08:01Z, kept as .v8_2ab42ffd) -> e75ad8d910757c12 (v9). The diff below is against v7. Summary: (1) the (k) decision is recomputed from the add-on's own column_test witnesses (two fresh steps, finite ladders, both rules at both steps, pair Richardson from the witness norms with eligibility, active sets at the base and the eight stencil points for J_cw/J_c); the add-on must name the case, derive from the record by hash, be built on the record's gates.py (v5c) and cover every column failing the registered rule; otherwise the (k) outcome is INVALID and the invalid evidence is listed; (2) with (k) requires exactly twenty distinct coefficient records equal to the drawn columns; len(ids) != 20 is INVALID in the registered outcome; (3) INVALID pair evidence stays INVALID in the amended and (k)+(j) outcomes (listed per group as coefficient_columns_invalid_evidence / parameter_columns_invalid_evidence; no small-amplitude exclusion of invalid records); (4) salvage records use complete pair witnesses first when present, a saved Richardson pair must be adjacent and both of its steps eligible, and the convention is decided by the gates.py hash of the file the record came from (companion parameter records carry _source_gates_py; a contradicting convention string is INVALID); (5) negative or non-finite physical-omega F0 Richardson witnesses (whole column or group) give REJUDGED_INVALID before any re-judgement. Companion rule (lead 07:53Z item 3): a coefficient-only record takes its parameter columns from gates_gpu_v1_<case>_G1v4.json, else gates_gpu_v1_<case>.json, bound by that file's sha256 and gates.py hash (parameter_source in the coverage file).

Outcomes on the seven records at 08:02Z (unchanged where decided before): v5c combined S01_own and S05_own: J_f, J_cw, J_c registered PASS 20/20, (k) PASS, (k)+(j) PASS; S09_own: registered FAIL (J_f 13/20, J_cw 15/20, J_c 15/20), (k) FAIL on the five near-origin small-amplitude columns 793, 873, 912, 1035, 1354 (J_f columns 186 and 189 pass under (k), error ratio 0.10 per decade), (k)+(j) PASS; v4 records: J_f as before (S01 PASS, S05 PASS, S09 FAIL 13/20 amended PASS, manu FAIL 8/20 amended OPEN gauge), J_cw/J_c INVALID (witness gap) in every outcome.

```
--- validation/g1_coverage_check.py.v7_e53bd772	2026-10-29 07:52:33.809120087 +0000
+++ validation/g1_coverage_check.py	2026-10-29 08:01:56.350266169 +0000
@@ -1,5 +1,16 @@
 #!/usr/bin/env python
-"""v7 (07:5xZ, specification v1.18 3.6 (k), lead 07:41Z): three outcomes per case and Jacobian: registered; with the post-result step rule (k) (a column or group that fails
+"""v9 (08:0xZ, V198 items 1-5): (1) the (k) decision is recomputed from the add-on's own column_test witnesses (two fresh steps 1e-2 s_j, 1e-3 s_j: finite
+error ladders, five-point and second-order rules at both steps, the pair Richardson from the witness norms with eligibility, active sets at the base and all
+eight stencil points for J_cw/J_c); the add-on must name the case, derive from the record (hash), be built on the record's gates.py, and cover every column
+that fails the registered rule in that Jacobian; otherwise the (k) outcome is INVALID; (2) with (k) requires exactly twenty distinct coefficient records that
+are the drawn columns; len(ids) != 20 is INVALID in the registered outcome; (3) INVALID pair evidence stays INVALID in every outcome (no small-amplitude
+exclusion of invalid records); (4) salvage records use complete pair witnesses first when present, the saved pair must be adjacent and eligible, and the
+convention is decided by the source gates.py hash of the file the record came from (companion records carry _source_gates_py), not by the convention string
+alone; (5) negative or non-finite physical-omega F0 Richardson witnesses (whole or group) are INVALID before any re-judgement.
+v8 (07:5xZ): a coefficient-only record (gates.py --sections G1_coef / G1_Jc_coef, no parameter columns) is combined with the parameter columns of the companion
+G1 record of the same case in the same directory (gates_gpu_v1_<case>_G1v4.json, then gates_gpu_v1_<case>.json): the parameter decisions come from that record
+(its file and gates.py hash are stated as parameter_source); the coefficient decisions from the coefficient-only record. Both files are named in the output.
+v7 (07:5xZ, specification v1.18 3.6 (k), lead 07:41Z): three outcomes per case and Jacobian: registered; with the post-result step rule (k) (a column or group that fails
 the registered ladder passes under (k) when the add-on validation/g1_step_addon_<case>.json shows the pair (1e-2 s_j, 1e-3 s_j) passing: both steps within tau,
 second order and five point, and the pair Richardson within tau; label "pass under the post-result step rule (k)", with the per-decade error ratio); with (k)
 and the small-amplitude rule (j). The add-on record must be on the same case and come from the same v5c coefficient record (input hash recorded).
@@ -97,14 +108,16 @@
 SALVAGE_CONVENTIONS = ("v4 (", "v3 (")      # recorded scaling_convention prefixes of pre-v5c harness versions whose records may be judged from the witnesses they have (separately labelled)
 SALVAGE_HARNESS_HASHES = {"918c2e06ba2bae2f": "gates.py v4", "549c21b0fac9ecfa": "gates.py v3"}   # explicit source-hash allowlist (V195 item 1): the record file's recorded gates.py hash
 CURRENT_HARNESS = {"hash": None}
+V5C_HASHES = {"5f4079926f1c757b"}                                        # gates.py v5c (frozen harness; full pair witnesses)
+K_STEPS = ["1e-02", "1e-03"]; K_PAIR = "1e-02->1e-03"
 def record_convention(rec):
-    conv = str(rec.get("scaling_convention") or "")
-    if conv.startswith("v5c"):
-        return "v5c"
-    if any(conv.startswith(pfx) for pfx in SALVAGE_CONVENTIONS):
-        return "salvage"
-    if CURRENT_HARNESS["hash"] in SALVAGE_HARNESS_HASHES:          # coefficient records of harness v4 carry no convention field; the file's recorded gates.py hash identifies them
-        return "salvage"
+    """V198 item 4: the convention is decided by the gates.py hash of the file the record came from (the record file, or the companion file for copied
+    parameter records); a convention string that contradicts the source is 'unknown' (INVALID)."""
+    src = str(rec.get("_source_gates_py") or CURRENT_HARNESS["hash"] or "")[:16]; conv = str(rec.get("scaling_convention") or "")
+    if src in SALVAGE_HARNESS_HASHES:
+        return "salvage" if (not conv or any(conv.startswith(pfx) for pfx in SALVAGE_CONVENTIONS)) else "unknown"
+    if src in V5C_HASHES:
+        return "v5c" if conv.startswith("v5c") else "unknown"
     return "unknown"
 def richardson_evidence(container, errs_by_label, tau, rec):
     """V195 items 1 and 3: v5c records need the full pair witnesses (INVALID otherwise); salvage records use the recorded finite non-negative scalar, labelled;
@@ -114,12 +127,25 @@
         rich, pair, okw, detail = recompute_richardson_from_witnesses(allp, errs_by_label, tau)
         return (rich, pair, "witnesses", detail) if okw else (None, None, "INVALID", detail)
     if conv == "salvage":
+        if isinstance(allp, dict):                                      # V198 item 4: complete norm witnesses first
+            rich, pair, okw, detail = recompute_richardson_from_witnesses(allp, errs_by_label, tau)
+            if okw:
+                return rich, pair, "witnesses (salvage record with complete pair witnesses)", detail
         r = container.get("richardson", container.get("richardson_error"))
         if r is None:                                                   # the harness stores no Richardson value when no adjacent pair passes the second-order rule:
             return None, None, "salvage (no passing pair: numerical failure, no Richardson value)", None   # a numerical FAIL, not missing evidence
         if not fin(r) or r < 0:
             return None, None, "INVALID", "salvage record with a non-finite or negative Richardson value"
-        return r, container.get("richardson_pair"), "salvage (recorded Richardson scalar; pre-v5c harness)", None
+        pair = container.get("richardson_pair")
+        if pair is not None:                                            # V198 item 4: a saved pair must be adjacent and both of its steps must pass the second-order rule
+            pl = pair if isinstance(pair, str) else "->".join(str(x) for x in pair)
+            if pl not in PAIR_LABELS:
+                return None, None, "INVALID", f"salvage record names a non-adjacent Richardson pair {pl}"
+            a, b = pl.split("->")
+            if not (fin(errs_by_label.get(a)) and fin(errs_by_label.get(b)) and errs_by_label[a] <= tau and errs_by_label[b] <= tau):
+                return None, None, "INVALID", f"salvage record names a Richardson pair {pl} whose steps do not both pass the second-order rule"
+            return r, pl, "salvage (recorded Richardson scalar of an adjacent eligible pair; pre-v5c harness)", None
+        return r, None, "salvage (recorded Richardson scalar; pre-v5c harness)", None
     return None, None, "INVALID", f"unknown recording convention '{rec.get('scaling_convention')}'"
 def recompute_whole(rec, tau=TAU_ALL):
     """V192/V193 item 4-5: whole-column decision recomputed from complete, finite, non-negative error ladders (equal to per_group[step][kind]['all']) and from the
@@ -203,7 +229,7 @@
     e' = (e * den / s) / max(|d|, |D|, F). Whole-column decision: two consecutive passing steps (second order and five point) in e'; the Richardson
     with F = 0 is scale-free (richardson_F0 <= tau suffices); otherwise RECOMPUTE_NEEDED. Returns dict(status, ...)."""
     s_ = rec.get("step_scale", 1.0); conv = str(rec.get("scaling_convention") or "")
-    if not (fin(s_) and 0 < s_ < 1.0) or rec.get("derivative_scale") is not None or not (conv.startswith("v3") or conv.startswith("v4")):
+    if not (fin(s_) and 0 < s_ < 1.0) or rec.get("derivative_scale") is not None or not (conv.startswith("v3") or conv.startswith("v4")) or record_convention(rec) != "salvage":
         return dict(status="NOT_APPLICABLE")               # only harness v3/v4 records scaled the physical derivative; v1/v2 and v5 records are in physical units
     pg = rec.get("per_group") or {}; hs = sorted(pg.keys(), key=lambda x: -float(x))
     def unscaled(h, g, kind):
@@ -218,11 +244,17 @@
         e2 = [unscaled(h, g, "2") for h in hs]; e4 = [unscaled(h, g, "4") for h in hs]
         p2 = any(e2[i] <= t and e2[i + 1] <= t for i in range(len(hs) - 1)); p4 = any(e4[i] <= t and e4[i + 1] <= t for i in range(len(hs) - 1))
         r0 = rec.get("richardson_error_F0") if g == "all" else ((rec.get("group_pass") or {}).get(g) or {}).get("richardson_error_F0")
-        rich_ok = fin(r0) and r0 <= t
-        st = "PASS" if (p2 and p4 and rich_ok) else ("RECOMPUTE_NEEDED" if (p2 and p4) else "FAIL")
+        if r0 is not None and (not fin(r0) or r0 < 0):                   # V198 item 5: negative or non-finite witnesses are INVALID before any re-judgement
+            st = "INVALID"; rich_ok = False
+        else:
+            rich_ok = fin(r0) and r0 <= t
+            st = "PASS" if (p2 and p4 and rich_ok) else ("RECOMPUTE_NEEDED" if (p2 and p4) else "FAIL")
         out["per_group"][g] = dict(e2_physical_units=e2, e4_physical_units=e4, pass_second_order=p2, pass_five_point=p4, richardson_F0=r0, status=st)
         ok_all = ok_all and st == "PASS"
-    out["status"] = "PASS" if ok_all else ("RECOMPUTE_NEEDED" if all(v["status"] in ("PASS", "RECOMPUTE_NEEDED") for v in out["per_group"].values()) else "FAIL")
+    if any(v["status"] == "INVALID" for v in out["per_group"].values()):
+        out["status"] = "INVALID"
+    else:
+        out["status"] = "PASS" if ok_all else ("RECOMPUTE_NEEDED" if all(v["status"] in ("PASS", "RECOMPUTE_NEEDED") for v in out["per_group"].values()) else "FAIL")
     return out
 def small_amplitude(rec, g):
     """v1.17 (iii), with the normalization of V187: the per-group norms stored by column_test v3 are SCALED by the step scale s_j, the whole-column norm
@@ -252,7 +284,7 @@
             return False
     return recompute_group(rec, g)["PASS"]
 def load_addon(cname, record_path):
-    """The (k) add-on record for the case, if present and derived from this record (input_record_sha256)."""
+    """The (k) add-on record for the case, if present, derived from this record (input_record_sha256), naming the case and built on the record's gates.py (V198 item 1)."""
     ap = os.path.join(os.path.dirname(record_path), f"g1_step_addon_{cname}.json")
     if not os.path.exists(ap):
         return None, "no (k) add-on record"
@@ -260,18 +292,70 @@
     import hashlib
     if a.get("input_record_sha256") != hashlib.sha256(open(record_path, "rb").read()).hexdigest():
         return None, f"add-on record {os.path.basename(ap)} was derived from another input record (hash mismatch)"
+    if a.get("case") != cname:
+        return None, f"add-on record names case {a.get('case')!r}, not {cname!r}"
+    ah = str((a.get("code_sha256") or {}).get("validation/gates.py", ""))[:16]
+    if not ah or ah != CURRENT_HARNESS["hash"] or ah not in V5C_HASHES:
+        return None, f"add-on gates.py hash {ah!r} is not the record's v5c harness {CURRENT_HARNESS['hash']!r}"
+    if not isinstance(a.get("jacobians"), dict):
+        return None, "add-on record has no jacobians"
     return a, ""
+def expected_k_labels(scale):
+    labs = {f"{0.0:+.1e}"}
+    for l in K_STEPS:
+        h = float(l) * scale
+        for t in (h, -h, 2 * h, -2 * h):
+            labs.add(f"{t:+.1e}")
+    return labs
+def k_decision(addon, jac, col, g, needs_active):
+    """V198 item 1: the (k) decision RECOMPUTED from the add-on's column_test witnesses at the two fresh steps; the stored PASS_k is only compared.
+    Returns dict(PASS, INVALID, reason, ratio, richardson, agrees_with_stored)."""
+    rec = ((addon.get("jacobians") or {}).get(jac) or {}).get("columns", {}).get(str(col)) if addon else None
+    if not isinstance(rec, dict):
+        return dict(PASS=False, INVALID=True, reason="column not re-evaluated in the add-on")
+    t = rec.get("column_test")
+    if not isinstance(t, dict) or rec.get("column") != col:
+        return dict(PASS=False, INVALID=True, reason="add-on column record without column_test witnesses or with a different column id")
+    sc = t.get("step_scale", 1.0)
+    if not fin(sc) or sc <= 0 or abs(sc - float(rec.get("step_scale", sc))) > 1e-12 * max(1.0, sc):
+        return dict(PASS=False, INVALID=True, reason="invalid or inconsistent step scale")
+    if g is None:
+        e2 = t.get("errors_second_order") or {}; e4 = t.get("errors_five_point") or {}; container = t; tau = TAU_ALL; stored = (rec.get("whole") or {}).get("PASS_k")
+    else:
+        pg = t.get("per_group") or {}
+        e2 = {h: (v.get("second_order") or {}).get(g) for h, v in pg.items()}; e4 = {h: (v.get("five_point") or {}).get(g) for h, v in pg.items()}
+        container = (t.get("group_pass") or {}).get(g); tau = TAU_GROUP; stored = ((rec.get("groups") or {}).get(g) or {}).get("PASS_k")
+        if not isinstance(container, dict):
+            return dict(PASS=False, INVALID=True, reason=f"group {g} absent from the add-on witnesses")
+    if sorted(e2.keys()) != sorted(K_STEPS) or sorted(e4.keys()) != sorted(K_STEPS) or any(not fin(v) or v < 0 for v in list(e2.values()) + list(e4.values())):
+        return dict(PASS=False, INVALID=True, reason="two-step error ladders incomplete or non-finite")
+    if needs_active:
+        a = t.get("active_sets")
+        if not isinstance(a, dict) or not t.get("active_set_base_recorded") or set(a.keys()) != expected_k_labels(sc):
+            return dict(PASS=False, INVALID=True, reason="add-on active-set records (base and eight stencil points) missing or mislabelled")
+        if len(set(json.dumps(v, sort_keys=True) for v in a.values())) != 1 or t.get("active_sets_identical") is not True:
+            return dict(PASS=False, INVALID=True, reason="add-on active sets differ among the base and the stencil points")
+    allp = container.get("richardson_all_pairs")
+    if not isinstance(allp, dict) or list(allp.keys()) != [K_PAIR]:
+        return dict(PASS=False, INVALID=True, reason="pair witness for 1e-02->1e-03 missing or mislabelled")
+    w = allp[K_PAIR]; vals = [w.get(k) for k in ("norm_diff_scaled", "norm_d_scaled", "norm_R_scaled", "floor")]
+    if any(not fin(x) or x < 0 for x in vals) or not fin(w.get("scale")) or w.get("scale") <= 0:
+        return dict(PASS=False, INVALID=True, reason="pair witness norms missing, non-finite, negative or scale invalid")
+    r = vals[0] / max(vals[1], vals[2], vals[3], 1e-300)
+    both2 = all(e2[l] <= tau for l in K_STEPS); both4 = all(e4[l] <= tau for l in K_STEPS)
+    ok = bool(both2 and both4 and r <= tau)
+    ratio = (e2["1e-02"] / e2["1e-03"]) if e2["1e-03"] > 0 else None
+    return dict(PASS=ok, INVALID=False, richardson=r, ratio=ratio, both_steps_second_order=both2, both_steps_five_point=both4, stored_PASS_k=stored, agrees_with_stored=(ok == bool(stored)))
+K_CTX = {"needs_active": False, "invalid": []}
 def k_pass(addon, jac, col, g=None):
-    """True if the add-on shows the pair (1e-2 s_j, 1e-3 s_j) passing for this column (whole column when g is None, else the group); returns (pass, ratio)."""
+    """(pass, ratio) of the recomputed (k) decision (k_decision); INVALID evidence counts as not passing and is collected in K_CTX['invalid']."""
     if not addon:
         return False, None
-    rec = ((addon.get("jacobians") or {}).get(jac) or {}).get("columns", {}).get(str(col))
-    if not rec:
-        return False, None
-    dec = rec["whole"] if g is None else (rec.get("groups") or {}).get(g)
-    if not isinstance(dec, dict):
+    d = k_decision(addon, jac, col, g, K_CTX["needs_active"])
+    if d.get("INVALID"):
+        K_CTX["invalid"].append(f"{col}:{g or 'all'}: {d.get('reason')}")
         return False, None
-    return bool(dec.get("PASS_k")), dec.get("error_ratio_1e2_over_1e3")
+    return bool(d["PASS"]), d.get("ratio")
 def main(files):
     for f in files:
         d = json.load(open(f)); entries = dict(d.get("cases", {}))
@@ -280,7 +364,31 @@
             if isinstance(v, dict) and v.get("partial") and k not in entries:
                 entries[k] = v
         report = dict(source=os.path.relpath(f), label=LABEL, threshold_small_amplitude=THRESH, min_coefficient_coverage=MIN_COEF, harness_gates_py=CURRENT_HARNESS["hash"],
-                      harness_salvage=SALVAGE_HARNESS_HASHES.get(CURRENT_HARNESS["hash"], "v5c or later" if CURRENT_HARNESS["hash"] else "unknown"), cases={})
+                      harness_salvage=SALVAGE_HARNESS_HASHES.get(CURRENT_HARNESS["hash"], "v5c or later" if CURRENT_HARNESS["hash"] else "unknown"), cases={}, parameter_source={})
+        # v8: coefficient-only records take their parameter columns from the companion G1 record of the case
+        for cname, c in list(entries.items()):
+            if any(k in c for k in ("G1_Jf_param_columns", "G1_Jcw_param_columns", "G1_Jc_param_columns")):
+                continue
+            for cand in (f"gates_gpu_v1_{cname}_G1v4.json", f"gates_gpu_v1_{cname}.json"):
+                cp = os.path.join(os.path.dirname(f), cand)
+                if os.path.exists(cp) and os.path.abspath(cp) != os.path.abspath(f):
+                    dd = json.load(open(cp)); ce = dict(dd.get("cases", {}))
+                    for k, v in dd.items():
+                        if isinstance(v, dict) and v.get("partial") and k not in ce:
+                            ce[k] = v
+                    comp = ce.get(cname)
+                    if comp and "G1_Jf_param_columns" in comp:
+                        src_hash = str((dd.get("code_sha256") or {}).get("validation/gates.py", ""))[:16]
+                        for key in ("G1_Jf_param_columns", "G1_Jcw_param_columns", "G1_Jc_param_columns", "G1_coefficient_columns_drawn"):
+                            if key in comp and key not in c:
+                                c[key] = comp[key]
+                                if key != "G1_coefficient_columns_drawn":
+                                    for v in c[key].values():                       # the companion file's gates.py hash governs its records (V198 item 4)
+                                        if isinstance(v, dict):
+                                            v["_source_gates_py"] = src_hash
+                        import hashlib as _hl
+                        report["parameter_source"][cname] = dict(file=cand, file_sha256=_hl.sha256(open(cp, "rb").read()).hexdigest(), gates_py=src_hash, note="parameter columns taken from the companion G1 record (harness v4 parameter records decide; lead 07:18Z)")
+                        break
         for cname, c in entries.items():
             cres = {}
             for jac, pkey, ckey in JACS:
@@ -321,7 +429,7 @@
                                   coefficient_count_as_registered=(distinct == N_COEF and len(ids) == N_COEF), ids_match_drawn=ids_match, drawn_columns=drawn, missing_parameter_columns=missing_params, recomputed_decisions=recomputed,
                                   physical_omega_rejudgement=rejudge.get("physical:omega"),
                                   PASS=(not missing_params) and distinct == N_COEF and len(ids) == N_COEF and bool(ids_match) and all(v in ("PASS",) or str(v).startswith("REJUDGED_PASS") for v in reg_param.values()) and all(v == "PASS" for v in reg_coef.values()),
-                                  INVALID=any(str(v).startswith("INVALID") or str(v).startswith("REJUDGED_RECOMPUTE") for v in list(reg_param.values()) + list(reg_coef.values())) or bool(missing_params) or distinct != N_COEF or not ids_match)
+                                  INVALID=any(str(v).startswith("INVALID") or str(v).startswith("REJUDGED_RECOMPUTE") or str(v).startswith("REJUDGED_INVALID") for v in list(reg_param.values()) + list(reg_coef.values())) or bool(missing_params) or distinct != N_COEF or len(ids) != N_COEF or not ids_match)
                 records_v2 = bool(cc) and all(isinstance(col_record(e, jac).get("per_group"), dict) for e in cc)
                 if not records_v2:
                     cres[jac] = dict(registered=registered, amended=dict(status="RECORDS_INSUFFICIENT", reason="compact v1 coefficient records: per-group norms absent"), label=LABEL)
@@ -335,30 +443,40 @@
                 gres = {}
                 for g in sorted(groups):
                     par_fail = [k for k in expected_params if k in pc and not group_pass(pc[k], g)] + [k for k in missing_params]
-                    sa, pass_cols, fail_cols = [], [], []
+                    sa, pass_cols, fail_cols, inv_cols = [], [], [], []
                     seen = set()
                     for e in cc:
                         r = col_record(e, jac); k = col_id(e, jac)
                         if k in seen:
                             continue
                         seen.add(k)
+                        if not comp_coef[k][0] or recompute_group(r, g).get("INVALID") or recompute_whole(r).get("INVALID"):   # V198 item 3: invalid evidence is never excluded as small-amplitude
+                            inv_cols.append(k); continue
                         if small_amplitude(r, g):
                             sa.append(k); continue
                         (pass_cols if group_pass(r, g) else fail_cols).append(k)
-                    status = "PASS" if (not par_fail and not fail_cols and len(set(pass_cols)) >= MIN_COEF) else "OPEN"
-                    gres[g] = dict(status=status, parameter_columns_failing_or_missing=par_fail, coefficient_columns_passing=pass_cols, coefficient_columns_failing_not_small_amplitude=fail_cols,
+                    par_inv = [k for k in expected_params if k in pc and (not comp_param[k][0] or recompute_group(pc[k], g).get("INVALID") or str(reg_param.get(k, "")).startswith("INVALID") or str(reg_param.get(k, "")).startswith("REJUDGED_INVALID"))]
+                    status = "INVALID" if (inv_cols or par_inv) else ("PASS" if (not par_fail and not fail_cols and len(set(pass_cols)) >= MIN_COEF) else "OPEN")
+                    gres[g] = dict(status=status, parameter_columns_failing_or_missing=par_fail, coefficient_columns_invalid_evidence=inv_cols, parameter_columns_invalid_evidence=par_inv, coefficient_columns_passing=pass_cols, coefficient_columns_failing_not_small_amplitude=fail_cols,
                                    coefficient_columns_small_amplitude_not_tested=sa, n_coverage_distinct=len(set(pass_cols)))
                 complete_all = all(c[0] for c in comp_param.values()) and all(c[0] for c in comp_coef.values()) and not missing_params and distinct == N_COEF and len(ids) == N_COEF
                 incomplete = {k: c[1] for k, c in list(comp_param.items()) + list(comp_coef.items()) if not c[0]}
                 phys_ok = all(v.get("status") in (None, "NOT_APPLICABLE", "PASS") for v in rejudge.values())
                 amended_pass = complete_all and bool(ids_match) and phys_ok and all(whole_param.values()) and all(whole_coef.values()) and bool(gres) and all(v["status"] == "PASS" for v in gres.values())
-                amended_status = "PASS" if amended_pass else ("INVALID (incomplete, ids not the drawn columns, or re-judgement pending)" if (not complete_all or not phys_ok or not ids_match) else "OPEN")
+                evidence_invalid = any(str(v).startswith("INVALID") or str(v).startswith("REJUDGED_INVALID") or str(v).startswith("REJUDGED_RECOMPUTE") for v in list(reg_param.values()) + list(reg_coef.values())) or any(v["status"] == "INVALID" for v in gres.values())
+                amended_pass = amended_pass and not evidence_invalid
+                amended_status = "PASS" if amended_pass else ("INVALID (incomplete, ids not the drawn columns, invalid pair evidence, or re-judgement pending)" if (not complete_all or not phys_ok or not ids_match or evidence_invalid) else "OPEN")
                 # ---- specification v1.18 3.6 (k): registered outcome with the post-result step rule, and with (k) and (j) together
                 addon, addon_note = load_addon(cname, f)
-                k_cols = {}; k_fail = []; k_ratios = {}
+                K_CTX["needs_active"] = needs_active; K_CTX["invalid"] = []
+                k_cols = {}; k_fail = []; k_ratios = {}; reg_failing_cols = []
                 for e in cc:
                     r = col_record(e, jac); k = col_id(e, jac)
                     rw = recompute_whole(r); rg = {g: recompute_group(r, g) for g in REQUIRED_GROUPS}
+                    if not (rw.get("PASS") and all(x.get("PASS") for x in rg.values())):
+                        reg_failing_cols.append(k)
+                    if rw.get("INVALID") or any(x.get("INVALID") for x in rg.values()):
+                        K_CTX["invalid"].append(f"{k}: invalid registered pair evidence")
                     ok_whole = rw.get("PASS") or (k_pass(addon, jac, k)[0] if comp_coef.get(k, (False, ""))[0] else False)
                     groups_ok = {}
                     for g in REQUIRED_GROUPS:
@@ -374,7 +492,13 @@
                     if not passed:
                         k_fail.append(k)
                 params_ok = (not missing_params) and all(v in ("PASS",) or str(v).startswith("REJUDGED_PASS") for v in reg_param.values())
-                with_k = dict(status=("PASS" if (params_ok and ids_match and bool(cc) and not k_fail and all(c[0] for c in comp_coef.values())) else ("INVALID" if registered["INVALID"] else "FAIL")),
+                addon_cols = set(int(x) for x in (((addon or {}).get("jacobians") or {}).get(jac) or {}).get("columns", {}).keys()) if addon else set()
+                addon_incomplete = bool(reg_failing_cols) and addon is not None and not set(reg_failing_cols) <= addon_cols
+                if addon_incomplete:
+                    K_CTX["invalid"].append(f"add-on does not cover the registered failing columns {sorted(set(reg_failing_cols) - addon_cols)}")
+                k_invalid = bool(K_CTX["invalid"]) or registered["INVALID"] or distinct != N_COEF or len(ids) != N_COEF or not ids_match
+                with_k = dict(status=("PASS" if (params_ok and ids_match and distinct == N_COEF and len(ids) == N_COEF and not k_fail and not k_invalid and all(c[0] for c in comp_coef.values())) else ("INVALID" if k_invalid else "FAIL")),
+                              invalid_evidence=list(K_CTX["invalid"]), registered_failing_columns=sorted(set(reg_failing_cols)), addon_columns=sorted(addon_cols),
                               failing_columns=k_fail, columns=k_cols, error_ratios_1e2_over_1e3=k_ratios, addon=(None if addon is None else os.path.basename(os.path.join(os.path.dirname(f), f"g1_step_addon_{cname}.json"))), addon_note=addon_note,
                               label="registered rule with the post-result step rule (k) (specification v1.18 3.6 (k))")
                 # (k) and (j): small-amplitude groups excluded as in the amended outcome, the remaining failures may pass under (k)
@@ -383,9 +507,9 @@
                     fails = [k for k in gv["coefficient_columns_failing_not_small_amplitude"] if not k_pass(addon, jac, k, g)[0]]
                     passes_k = [k for k in gv["coefficient_columns_failing_not_small_amplitude"] if k_pass(addon, jac, k, g)[0]]
                     cov = len(set(gv["coefficient_columns_passing"]) | set(passes_k))
-                    kj_groups[g] = dict(status=("PASS" if (not gv["parameter_columns_failing_or_missing"] and not fails and cov >= MIN_COEF) else "OPEN"), failing=fails, pass_under_k=passes_k, coverage=cov, small_amplitude_not_tested=gv["coefficient_columns_small_amplitude_not_tested"])
-                with_kj = dict(status=("PASS" if (complete_all and ids_match and phys_ok and all(whole_param.values()) and all((whole_coef[k] or k_pass(addon, jac, k)[0]) for k in whole_coef) and bool(kj_groups) and all(v["status"] == "PASS" for v in kj_groups.values())) else ("INVALID" if not (complete_all and ids_match and phys_ok) else "OPEN")),
-                               groups=kj_groups, label="post-result rules (k) and (j) together (specification v1.18 3.6 (k) (7))")
+                    kj_groups[g] = dict(status=("INVALID" if gv["status"] == "INVALID" else ("PASS" if (not gv["parameter_columns_failing_or_missing"] and not fails and cov >= MIN_COEF) else "OPEN")), failing=fails, pass_under_k=passes_k, coverage=cov, small_amplitude_not_tested=gv["coefficient_columns_small_amplitude_not_tested"])
+                with_kj = dict(status=("PASS" if (complete_all and ids_match and phys_ok and not evidence_invalid and not k_invalid and all(whole_param.values()) and all((whole_coef[k] or k_pass(addon, jac, k)[0]) for k in whole_coef) and bool(kj_groups) and all(v["status"] == "PASS" for v in kj_groups.values())) else ("INVALID" if (not (complete_all and ids_match and phys_ok) or evidence_invalid or k_invalid or any(v["status"] == "INVALID" for v in kj_groups.values())) else "OPEN")),
+                               invalid_evidence=list(K_CTX["invalid"]), groups=kj_groups, label="post-result rules (k) and (j) together (specification v1.18 3.6 (k) (7))")
                 cres[jac] = dict(registered=registered, with_k=with_k, with_k_and_j=with_kj, amended=dict(status=amended_status, incomplete_records=incomplete, whole_column_parameter=whole_param, whole_column_coefficient=whole_coef, missing_parameter_columns=missing_params, groups=gres,
                                                                      resolved_coverage_counts={g: v["n_coverage_distinct"] for g, v in gres.items()}), label=LABEL)
             report["cases"][cname] = cres
```
