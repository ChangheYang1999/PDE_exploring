# Snapshot gpu_v1 addendum 10 (test-only): checker v8 (companion parameter record for coefficient-only records); written 2026-10-29T07:53:01Z

g1_coverage_check.py e53bd772d7b7dfaa (v7, kept as .v7_e53bd772) -> 2ab42ffdec74c421 (v8): a coefficient-only record (sections G1_coef / G1_Jc_coef) takes its parameter columns and the drawn-column list from the companion G1 record of the same case in the same directory (gates_gpu_v1_<case>_G1v4.json, else gates_gpu_v1_<case>.json), whose harness convention governs those records (labelled 'gates.py v4 (companion record)'); the output names the companion file and its gates.py hash (parameter_source). Nothing else changes.

```
--- validation/g1_coverage_check.py.v7_e53bd772	2026-10-29 07:52:33.809120087 +0000
+++ validation/g1_coverage_check.py	2026-10-29 07:52:33.829120126 +0000
@@ -1,5 +1,8 @@
 #!/usr/bin/env python
-"""v7 (07:5xZ, specification v1.18 3.6 (k), lead 07:41Z): three outcomes per case and Jacobian: registered; with the post-result step rule (k) (a column or group that fails
+"""v8 (07:5xZ): a coefficient-only record (gates.py --sections G1_coef / G1_Jc_coef, no parameter columns) is combined with the parameter columns of the companion
+G1 record of the same case in the same directory (gates_gpu_v1_<case>_G1v4.json, then gates_gpu_v1_<case>.json): the parameter decisions come from that record
+(its file and gates.py hash are stated as parameter_source); the coefficient decisions from the coefficient-only record. Both files are named in the output.
+v7 (07:5xZ, specification v1.18 3.6 (k), lead 07:41Z): three outcomes per case and Jacobian: registered; with the post-result step rule (k) (a column or group that fails
 the registered ladder passes under (k) when the add-on validation/g1_step_addon_<case>.json shows the pair (1e-2 s_j, 1e-3 s_j) passing: both steps within tau,
 second order and five point, and the pair Richardson within tau; label "pass under the post-result step rule (k)", with the per-decade error ratio); with (k)
 and the small-amplitude rule (j). The add-on record must be on the same case and come from the same v5c coefficient record (input hash recorded).
@@ -101,7 +104,7 @@
     conv = str(rec.get("scaling_convention") or "")
     if conv.startswith("v5c"):
         return "v5c"
-    if any(conv.startswith(pfx) for pfx in SALVAGE_CONVENTIONS):
+    if any(conv.startswith(pfx) for pfx in SALVAGE_CONVENTIONS) or conv.startswith("gates.py v4") or conv.startswith("gates.py v3"):
         return "salvage"
     if CURRENT_HARNESS["hash"] in SALVAGE_HARNESS_HASHES:          # coefficient records of harness v4 carry no convention field; the file's recorded gates.py hash identifies them
         return "salvage"
@@ -280,7 +283,30 @@
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
+                                    for v in c[key].values():                       # the companion's own harness convention governs its records
+                                        if isinstance(v, dict) and not v.get("scaling_convention"):
+                                            v["scaling_convention"] = SALVAGE_HARNESS_HASHES.get(src_hash, "unknown") + " (companion record)"
+                        report["parameter_source"][cname] = dict(file=cand, gates_py=str((dd.get("code_sha256") or {}).get("validation/gates.py", ""))[:16], note="parameter columns taken from the companion G1 record (harness v4 parameter records decide; lead 07:18Z)")
+                        break
         for cname, c in entries.items():
             cres = {}
             for jac, pkey, ckey in JACS:
```
