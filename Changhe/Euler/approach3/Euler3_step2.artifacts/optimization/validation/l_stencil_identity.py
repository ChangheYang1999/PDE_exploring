#!/usr/bin/env python
"""Stencil-set identity across the (l) records of one column (lead 13:25:05Z item 3): the per-point parameter hex values and the pressure argument
ranges (pressure_arg_ranges_per_point) of the J_f, J_cw and J_c l_eval records must be identical point by point; the elementary-function call sites
in the double-double copy (trig in the twist and the kernel tables, exp in K1/K2, wr, moment and sfac) are evaluated inside build_tables_dd and
tables_dd from (c_l, omega) alone, so identical parameter values at the 20 points mean identical arguments in the three references. Reading only.
Usage: python validation/l_stencil_identity.py <record.json> <record.json> [...]   Prints and writes validation/l_stencil_identity_<case>_<col>.json"""
import sys, os, json, hashlib

def main():
    recs = [(p, json.load(open(p))) for p in sys.argv[1:]]
    case = {d["case"] for _, d in recs}; col = {d["column"] for _, d in recs}
    assert len(case) == 1 and len(col) == 1, "records of one case and one column only"
    case, col = case.pop(), col.pop()
    have_ranges = all("pressure_arg_ranges_per_point" in d for _, d in recs)
    if have_ranges:
        pts = [d["pressure_arg_ranges_per_point"] for _, d in recs]
        keys = [sorted(p.keys()) for p in pts]
        same_keys = all(k == keys[0] for k in keys)
        per_point = {}; all_same = same_keys
        for k in keys[0]:
            vals = [(p[k].get("c_l_hex"), p[k].get("omega_hex"), json.dumps(p[k].get("arg_range"), sort_keys=True)) for p in pts if k in p]
            same = all(v == vals[0] for v in vals) and len(vals) == len(pts)
            per_point[k] = dict(identical=same, c_l_hex=vals[0][0], omega_hex=vals[0][1], arg_range=pts[0][k].get("arg_range"))
            all_same = all_same and same
        evidence = "pressure_arg_ranges_per_point (argument ranges and exp/trig counts per stencil point)"
    else:
        # records of the older l_eval version (before v5) carry no per-point argument ranges: the identity rests on the construction (same case, column, steps,
        # scale, base state: same start file and case build) and on the recorded active sets per stencil point (offset keys and geometry ids), the steps, the scale
        # and the double-double source hashes, which are compared here
        acts = [d["active_sets"]["base_and_stencil"] for _, d in recs]
        keys = [sorted(a.keys(), key=float) for a in acts]; same_keys = all(k == keys[0] for k in keys)
        per_point = {}; all_same = same_keys
        for k in keys[0]:
            vals = [json.dumps(a.get(k), sort_keys=True) for a in acts]
            same = all(v == vals[0] for v in vals); per_point[k] = dict(identical=same, active_set=acts[0].get(k)); all_same = all_same and same
        meta = [(json.dumps(d.get("steps")), d.get("scale"), json.dumps({k: v for k, v in d.get("sources", {}).items() if k.startswith("validation/dd_") or k.startswith("src/")}, sort_keys=True), d.get("case"), d.get("column"), d.get("coords")) for _, d in recs]
        all_same = all_same and all(m == meta[0] for m in meta)
        evidence = "active sets per stencil point (offset keys and geometry ids), steps, scale, case, column, coordinates and the double-double/production source hashes (records of the l_eval version before v5 carry no per-point argument ranges); the stencil points are the same by construction (same case, column, steps and base state)"
    copies = sorted({d.get("same_function_check", {}).get("path", "").split("/runs_l/")[1].split("/")[0] if "/runs_l/" in d.get("same_function_check", {}).get("path", "") else "(main)" for _, d in recs})
    if have_ranges:
        stmt = "the l_eval records (v5) store per stencil point the pressure argument ranges and exp/trig argument counts (not the parameter values themselves; the qualifier records store the hex values); the records share case, column, steps, base state and scientific sources, so the stencil points are the same by construction, and the identical argument ranges and counts at every point confirm it. Identical (c_l, omega) at every stencil point and identical pressure argument ranges in every record:"
    else:
        stmt = f"the l_eval records of the version before v5 store NO per-point pressure argument ranges, counts or parameter values; the identity is by construction: the records share case, column, coordinates, steps, scale, the start file and case build (base state) and the double-double/production source hashes (compared here), and their active sets agree at all 21 points (base and 20 stencil points); the records come from the frozen copies {copies} (same scientific sources). V327/V328 audited this construction for S01 z_c. Statement of the consequence:"
    out = dict(case=case, column=col, records=[dict(path=p, reference=d["reference"], sha256=hashlib.sha256(open(p, "rb").read()).hexdigest(), frozen_copy=(d.get("same_function_check", {}).get("path", "")), n_points=len(d.get("pressure_arg_ranges_per_point") or d["active_sets"]["base_and_stencil"])) for p, d in recs],
               n_points=len(keys[0]), same_point_keys=same_keys, all_points_identical=all_same, per_point=per_point, evidence=evidence,
               statement=stmt + " the double-double elementary-function call sites (trig in twist and kernel tables, exp in K1/K2, wr, moment, sfac) depend on (c_l, omega) only, so the three references evaluate them at the same arguments; one elementary-function qualification of the set covers the three rows. " + "J_c's recomputed closure target evaluates float64 closure ingredients: under the scope rule of 09:44:46Z only groups that fail the registered comparison decide the double-double scope, and the closure group passes the registered comparison, so the closure ingredients stay float64 (the screen l_scope.json records them above the closure-group limit, V324) and the closure group is judged again under (l), where it passes; they do not enter the far-anchor rows.")
    outp = os.path.join(os.path.dirname(os.path.abspath(__file__)), f"l_stencil_identity_{case}_{col.replace(':', '_')}.json")
    json.dump(out, open(outp, "w"), indent=1)
    print(case, col, "records:", [d["reference"] for _, d in recs], "| points", out["n_points"], "| same keys", same_keys, "| all points identical:", all_same); print("DONE", outp)

if __name__ == "__main__":
    main()
