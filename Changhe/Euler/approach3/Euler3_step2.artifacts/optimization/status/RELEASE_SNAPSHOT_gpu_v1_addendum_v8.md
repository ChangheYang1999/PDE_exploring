# Snapshot gpu_v1 addendum 8 (test-only, V195): checker v6; written 2026-10-29T07:39:37Z

g1_coverage_check.py ed1899e4248c9f2c (v5, kept as .v5_ed1899e4) -> d4a78f1339a5ebf6 (v6): (1) v5c records need the full pair witnesses of all four nominal pairs (no fallback to a scalar summary); older records are judged from their recorded witnesses only through an explicit allowlist (recorded scaling_convention v3/v4 or the record file's gates.py hash 918c2e06ba2bae2f / 549c21b0fac9ecfa), separately labelled 'salvage'; a missing convention field with an unknown harness hash is INVALID; (2) each of the six registered group decisions must exist on every record (iterated from REQUIRED_GROUPS); (3) non-finite, missing or negative pair evidence is INVALID (negative legacy Richardson scalars rejected); a missing Richardson value where no adjacent pair passed the second-order rule is a numerical FAIL, not missing evidence; discrepancies between recomputed decisions and stored summaries remain visible (agrees_with_stored).

```
--- validation/g1_coverage_check.py.v5_ed1899e4	2026-10-29 07:38:25.977303466 +0000
+++ validation/g1_coverage_check.py	2026-10-29 07:39:36.577444187 +0000
@@ -1,5 +1,10 @@
 #!/usr/bin/env python
-"""v5 (07:3xZ, V193): (1) ids_match is part of the amended aggregate too; (2) the closure, gauge and far-anchor-block groups are required for every battery case
+"""v6 (07:4xZ, V195): (1) a record whose convention is v5c must carry full pair witnesses for all four nominal pairs (no fallback to a scalar summary); salvage of
+older records is allowed only through an explicit allowlist of recorded conventions (v4 and earlier), separately labelled, with the witnesses actually present
+(a recorded Richardson scalar must be finite and non-negative); missing fields never make a record "old"; (2) each of the six registered group decisions
+(group_pass) must exist on every record, iterated from REQUIRED_GROUPS; (3) non-finite, missing or negative pair evidence is INVALID (not FAIL); discrepancies
+between recomputed decisions and stored summaries are reported.
+v5 (07:3xZ, V193): (1) ids_match is part of the amended aggregate too; (2) the closure, gauge and far-anchor-block groups are required for every battery case
 in addition to the three radial groups; (3) the raw active-set records must carry the exact base label and the twenty stencil labels (+-h s, +-2h s for the
 five nominal steps at the recorded step scale) and their signatures must agree; (4) every Richardson error is recomputed from the witness norms
 (norm_diff_scaled, norm_d_scaled, norm_R_scaled, floor, scale) for the four adjacent nominal pairs and each pair's eligibility from the errors at those steps;
@@ -85,6 +90,33 @@
     return any(fin(errs_by_label[labs[i]]) and fin(errs_by_label[labs[i + 1]]) and errs_by_label[labs[i]] <= tau and errs_by_label[labs[i + 1]] <= tau for i in range(len(labs) - 1))
 def ladder_ok(errs):
     return isinstance(errs, dict) and sorted(errs.keys()) == sorted(STEP_LABELS) and all(fin(v) and v >= 0 for v in errs.values())
+SALVAGE_CONVENTIONS = ("v4 (", "v3 (")      # recorded scaling_convention prefixes of pre-v5c harness versions whose records may be judged from the witnesses they have (separately labelled)
+SALVAGE_HARNESS_HASHES = {"918c2e06ba2bae2f": "gates.py v4", "549c21b0fac9ecfa": "gates.py v3"}   # explicit source-hash allowlist (V195 item 1): the record file's recorded gates.py hash
+CURRENT_HARNESS = {"hash": None}
+def record_convention(rec):
+    conv = str(rec.get("scaling_convention") or "")
+    if conv.startswith("v5c"):
+        return "v5c"
+    if any(conv.startswith(pfx) for pfx in SALVAGE_CONVENTIONS):
+        return "salvage"
+    if CURRENT_HARNESS["hash"] in SALVAGE_HARNESS_HASHES:          # coefficient records of harness v4 carry no convention field; the file's recorded gates.py hash identifies them
+        return "salvage"
+    return "unknown"
+def richardson_evidence(container, errs_by_label, tau, rec):
+    """V195 items 1 and 3: v5c records need the full pair witnesses (INVALID otherwise); salvage records use the recorded finite non-negative scalar, labelled;
+    unknown conventions are INVALID. Returns (rich, pair, status, detail): status in PASS_EVIDENCE / INVALID."""
+    conv = record_convention(rec); allp = container.get("richardson_all_pairs")
+    if conv == "v5c":
+        rich, pair, okw, detail = recompute_richardson_from_witnesses(allp, errs_by_label, tau)
+        return (rich, pair, "witnesses", detail) if okw else (None, None, "INVALID", detail)
+    if conv == "salvage":
+        r = container.get("richardson", container.get("richardson_error"))
+        if r is None:                                                   # the harness stores no Richardson value when no adjacent pair passes the second-order rule:
+            return None, None, "salvage (no passing pair: numerical failure, no Richardson value)", None   # a numerical FAIL, not missing evidence
+        if not fin(r) or r < 0:
+            return None, None, "INVALID", "salvage record with a non-finite or negative Richardson value"
+        return r, container.get("richardson_pair"), "salvage (recorded Richardson scalar; pre-v5c harness)", None
+    return None, None, "INVALID", f"unknown recording convention '{rec.get('scaling_convention')}'"
 def recompute_whole(rec, tau=TAU_ALL):
     """V192/V193 item 4-5: whole-column decision recomputed from complete, finite, non-negative error ladders (equal to per_group[step][kind]['all']) and from the
     Richardson pair witnesses (v5c records: witness norms; v4 records: the recorded value, labelled as such). Missing data -> not a pass (INVALID at the schema)."""
@@ -96,13 +128,9 @@
         if l in pg and (abs((pg[l].get("second_order") or {}).get("all", float("nan")) - e2[l]) > 1e-12 * max(1.0, e2[l]) or abs((pg[l].get("five_point") or {}).get("all", float("nan")) - e4[l]) > 1e-12 * max(1.0, e4[l])):
             return dict(PASS=False, reason=f"whole-column errors contradict per_group['all'] at step {l}", stored_PASS=rec.get("PASS"), agrees_with_stored=False)
     p2 = consecutive_pass(e2, tau); p4 = consecutive_pass(e4, tau)
-    allp = rec.get("richardson_all_pairs"); source = "v5c witnesses"
-    if isinstance(allp, dict) and allp and all(isinstance(v, dict) and "norm_diff_scaled" in v for v in allp.values()):
-        rich, pair, okw, detail = recompute_richardson_from_witnesses(allp, e2, tau)
-        if not okw:
-            return dict(PASS=False, reason=detail, stored_PASS=rec.get("PASS"), agrees_with_stored=False)
-    else:
-        rich = rec.get("richardson", rec.get("richardson_error")); pair = rec.get("richardson_pair"); detail = None; source = "recorded Richardson value (pre-v5c record; no witness norms)"
+    rich, pair, source, detail = richardson_evidence(rec, e2, tau, rec)
+    if source == "INVALID":
+        return dict(PASS=False, INVALID=True, reason=detail, stored_PASS=rec.get("PASS"), agrees_with_stored=False)
     ok = bool(p2 and p4 and fin(rich) and rich <= tau)
     return dict(pass_second_order=p2, pass_five_point=p4, richardson=rich, richardson_pair=pair, richardson_source=source, pairs=detail, PASS=ok, stored_PASS=rec.get("PASS"), agrees_with_stored=(ok == bool(rec.get("PASS"))))
 def recompute_group(rec, g, tau=TAU_GROUP):
@@ -111,14 +139,12 @@
     if not (ladder_ok(e2) and ladder_ok(e4)):
         return dict(PASS=False, reason="group error ladder incomplete or non-finite", stored_PASS=((rec.get("group_pass") or {}).get(g) or {}).get("PASS"), agrees_with_stored=False)
     p2 = consecutive_pass(e2, tau); p4 = consecutive_pass(e4, tau)
-    gp = (rec.get("group_pass") or {}).get(g) or {}
-    allp = gp.get("richardson_all_pairs"); source = "v5c witnesses"
-    if isinstance(allp, dict) and allp and all(isinstance(v, dict) and "norm_diff_scaled" in v for v in allp.values()):
-        rich, pair, okw, detail = recompute_richardson_from_witnesses(allp, e2, tau)
-        if not okw:
-            return dict(PASS=False, reason=detail, stored_PASS=gp.get("PASS"), agrees_with_stored=False)
-    else:
-        rich = gp.get("richardson_error"); pair = gp.get("richardson_pair"); detail = None; source = "recorded Richardson value (pre-v5c record)"
+    gp = (rec.get("group_pass") or {}).get(g)
+    if not isinstance(gp, dict) or "PASS" not in gp:
+        return dict(PASS=False, INVALID=True, reason=f"group decision for {g} missing", stored_PASS=None, agrees_with_stored=False)
+    rich, pair, source, detail = richardson_evidence(gp, e2, tau, rec)
+    if source == "INVALID":
+        return dict(PASS=False, INVALID=True, reason=detail, stored_PASS=gp.get("PASS"), agrees_with_stored=False)
     ok = bool(p2 and p4 and fin(rich) and rich <= tau)
     return dict(pass_second_order=p2, pass_five_point=p4, richardson=rich, richardson_pair=pair, richardson_source=source, PASS=ok, stored_PASS=gp.get("PASS"), agrees_with_stored=(ok == bool(gp.get("PASS"))))
 def record_complete(rec, groups, needs_active):
@@ -134,6 +160,12 @@
     for g in REQUIRED_GROUPS + ["all"]:
         if g not in present:
             return False, f"registered group {g} absent from the record"
+    gpd = rec.get("group_pass") or {}
+    for g in REQUIRED_GROUPS:                                               # V195 item 2: each registered group DECISION must exist
+        if not (isinstance(gpd.get(g), dict) and "PASS" in gpd[g]):
+            return False, f"group decision for {g} missing"
+    if record_convention(rec) == "unknown":
+        return False, f"unknown recording convention '{rec.get('scaling_convention')}' (neither v5c nor an allowlisted older harness)"
     sc = rec.get("step_scale", 1.0); dsc = rec.get("derivative_scale", sc)
     if not (fin(sc) and sc > 0 and fin(dsc) and dsc > 0):
         return False, "invalid step or derivative scale"
@@ -218,10 +250,12 @@
 def main(files):
     for f in files:
         d = json.load(open(f)); entries = dict(d.get("cases", {}))
+        CURRENT_HARNESS["hash"] = str((d.get("code_sha256") or {}).get("validation/gates.py", ""))[:16]
         for k, v in d.items():
             if isinstance(v, dict) and v.get("partial") and k not in entries:
                 entries[k] = v
-        report = dict(source=os.path.relpath(f), label=LABEL, threshold_small_amplitude=THRESH, min_coefficient_coverage=MIN_COEF, cases={})
+        report = dict(source=os.path.relpath(f), label=LABEL, threshold_small_amplitude=THRESH, min_coefficient_coverage=MIN_COEF, harness_gates_py=CURRENT_HARNESS["hash"],
+                      harness_salvage=SALVAGE_HARNESS_HASHES.get(CURRENT_HARNESS["hash"], "v5c or later" if CURRENT_HARNESS["hash"] else "unknown"), cases={})
         for cname, c in entries.items():
             cres = {}
             for jac, pkey, ckey in JACS:
@@ -250,8 +284,10 @@
                         return "INVALID: " + why
                     if k == "physical:omega" and rejudge.get(k, {}).get("status") not in (None, "NOT_APPLICABLE"):
                         return "REJUDGED_" + rejudge[k]["status"] + " (harness v3/v4 scaled the physical derivative by omega; physical-unit decision from witnesses)"
-                    rw = recompute_whole(v); rg = {g: recompute_group(v, g) for g in groups_req}
+                    rw = recompute_whole(v); rg = {g: recompute_group(v, g) for g in REQUIRED_GROUPS}
                     recomputed[k if k is not None else v.get("column")] = dict(whole=rw, groups=rg)
+                    if rw.get("INVALID") or any(x.get("INVALID") for x in rg.values()):
+                        return "INVALID: " + str(rw.get("reason") or next((x.get("reason") for x in rg.values() if x.get("INVALID")), "pair evidence"))
                     allok = rw["PASS"] and all(x["PASS"] for x in rg.values())
                     return "PASS" if allok else "FAIL"
                 reg_param = {k: reg_state(k, v, comp_param[k]) for k, v in pc.items()}
@@ -266,7 +302,7 @@
                     cres[jac] = dict(registered=registered, amended=dict(status="RECORDS_INSUFFICIENT", reason="compact v1 coefficient records: per-group norms absent"), label=LABEL)
                     continue
                 # amended outcome
-                whole_param = {k: bool(record_valid(v) and comp_param[k][0] and (recompute_whole(v)["PASS"] or str(reg_param.get(k, "")).startswith("REJUDGED_PASS")) and all(recompute_group(v, g)["PASS"] for g in groups_req)) for k, v in pc.items()}   # recomputed (V192 item 4)
+                whole_param = {k: bool(record_valid(v) and comp_param[k][0] and (recompute_whole(v)["PASS"] or str(reg_param.get(k, "")).startswith("REJUDGED_PASS")) and all(recompute_group(v, g)["PASS"] for g in REQUIRED_GROUPS)) for k, v in pc.items()}   # recomputed (V192 item 4)
                 whole_coef = {}
                 for e in cc:
                     r = col_record(e, jac)
```
