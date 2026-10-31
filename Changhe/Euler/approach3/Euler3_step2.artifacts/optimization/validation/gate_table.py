#!/usr/bin/env python
"""D6FP: markdown gate table (SPEC 3, CPU-reduced release battery v1.9) from validation/gates_<tag>*.json files (one per case or several cases
per file). Every entry states PASS (floor rule, the registered decision), PASS_rel (F = 0) and absolute_only (PASS and not PASS_rel) where the
record carries them. Usage: python validation/gate_table.py validation/gates_cpu_v1_*.json"""
import json, sys, glob, os
files = sorted(set(f for a in sys.argv[1:] for f in glob.glob(a))) or sorted(glob.glob(os.path.join(os.path.dirname(__file__), "gates_cpu_v1_*.json")))
files = [f for f in files if not f.endswith("_flags.json")]
def flag(v):
    if not isinstance(v, dict) or "PASS" not in v:
        return "n/a"
    s = "PASS" if v["PASS"] else "FAIL"
    if "PASS_rel" in v:
        s += "" if (v["PASS_rel"] or not v["PASS"]) else " (absolute_only)" if v.get("absolute_only") else " (PASS_rel False)"
    if v.get("active_sets_identical") is False:
        s += " [active sets differ]"
    return s
def e2(v):
    try:
        return " ".join(f"{float(h):.0e}:{err:.1e}" for h, err in v["errors_second_order"].items())
    except Exception:
        return ""
def rich(v):
    r = v.get("richardson_error") if isinstance(v, dict) else None
    return "n/a" if r is None else f"{r:.1e}"
for f in files:
    d = json.load(open(f))
    entries = dict(d.get("cases", {}))
    for k, v in d.items():                      # progressive saves: results[<case>] = dict(record, partial=True) until the case completes
        if isinstance(v, dict) and v.get("partial") and k not in entries:
            entries[k] = v
    for name, c in entries.items():
        if not isinstance(c, dict) or "summary" not in c and "G1_Jf_param_columns" not in c:
            print(f"\n### {name} ({os.path.basename(f)}): incomplete record (keys {list(c.keys())[:8]})"); continue
        print(f"\n### case {name}{' (PARTIAL: sections so far)' if c.get('partial') else ''} (file {os.path.basename(f)}; precision {d.get('precision_mode', c.get('precision_mode', 'see record'))}; device {d.get('gpu', d.get('device', '?'))}; "
              f"pair {c.get('pair')}; n_opt {c.get('n_opt')}; rows {c.get('n_rows')}; cost {c.get('cost')}; wall {c.get('seconds', float('nan')):.0f} s)")
        print("summary: " + json.dumps(c.get("summary")))
        print("\n| test | direction / item | second-order errors per step | Richardson | verdict |\n|---|---|---|---|---|")
        for key, label in (("G1_Jf_param_columns", "G1 J_f parameter columns"), ("G1_Jcw_param_columns", "G1 J_cw (production) parameter columns"), ("G1_Jc_param_columns", "G1 J_c parameter columns")):
            for dname, v in (c.get(key) or {}).items():
                print(f"| {label} | {dname} | {e2(v)} | {rich(v)} | {flag(v)} |")
        for key, label in (("G1_Jf_coefficient_columns", "G1 J_f coefficient columns"), ("G1_Jcw_coefficient_columns", "G1 J_cw coefficient columns"), ("G1_Jc_coefficient_columns", "G1 J_c coefficient columns")):
            v = c.get(key)
            if v:
                res = v.get("results", []); npass = sum(1 for r in res if (r.get("PASS") if "PASS" in r else r.get("Jf", {}).get("PASS")))
                print(f"| {label} | {len(res)} columns | | | {npass}/{len(res)} PASS; all_pass {v.get('all_pass')} |")
        for key in ("G2", "G4"):
            for dname, v in (c.get(key) or {}).items():
                vals = v.get("per_group") or v.get("max_rel") or v.get("errors_second_order") or {k: vv for k, vv in v.items() if isinstance(vv, (int, float))}
                print(f"| {key} | {dname} | {json.dumps(vals)[:120] if not isinstance(vals, (int, float)) else f'{vals:.1e}'} | {rich(v)} | {flag(v)} |")
        for dname, v in (c.get("G3") or {}).items():
            if isinstance(v, dict) and "PASS" in v:
                print(f"| G3 complete gradient | {dname} | {e2(v)} | {rich(v)} | {flag(v)} |")
        g5 = c.get("G5") or {}
        if g5:
            print(f"| G5a spatial FD vs DU (best relative per group) | | {json.dumps(g5.get('G5a_spatial_FD_vs_DU_best_rel_per_group'))[:120]} | | {'PASS' if g5.get('G5a_PASS') else 'FAIL'} |")
            print(f"| G5b divergence | | {g5.get('G5b_div_rel_max')} | | {'PASS' if g5.get('G5b_PASS') else 'FAIL'} |")
            if "G5c_source_consistency_rel" in g5:
                print(f"| G5c source consistency | | {g5.get('G5c_source_consistency_rel')} | | see entrywise test |")
        print(f"\nwall: G1 {c.get('t_G1', float('nan')):.0f} s, G2+G4 {c.get('t_G2_G4', float('nan')):.0f} s, G3 {c.get('t_G3', float('nan')):.0f} s, G5 {c.get('t_G5', float('nan')):.0f} s")
