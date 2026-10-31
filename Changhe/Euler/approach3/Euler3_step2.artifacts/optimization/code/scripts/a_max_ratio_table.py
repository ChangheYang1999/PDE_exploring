#!/usr/bin/env python
"""Lead 18:31:20Z item 5: both core a_max start values from a start-reference record (record_63a) and the ratios at every recorded end of the lineage
(FREE and FIXED), with rho_u^max against the start, and the 6.3 (a) (g) predicate as fixed at 17:55:21Z item 2 (either weight above 2 x start while
rho_u^max below start). Reads only. Usage: python scripts/a_max_ratio_table.py <start-reference record json> <run dir> [<run dir> ...]"""
import json, os, sys, hashlib
ROOT = os.path.abspath(os.path.join(os.path.dirname(os.path.abspath(__file__)), ".."))
ref_path = sys.argv[1]; ref = json.load(open(ref_path)); b = ref["battery"]
ac0, au0, ru0 = b.get("a_max_core"), b.get("a_max_core_upper"), b.get("rho_u_max")
print(f"start reference {ref.get('tag')} ({os.path.relpath(ref_path, ROOT)}, sha256 {hashlib.sha256(open(ref_path, 'rb').read()).hexdigest()[:16]}; tool {str(ref.get('script_sha256'))[:16]}; F-projected {((ref.get('state') or {}).get('F_projected'))}): "
      f"a_max_core {ac0}, a_max_core_upper {au0}, rho_u_max {ru0}, a_eff {b.get('a_eff')}, max_U {b.get('max_U')}, U_L2 {b.get('U_L2_r_lt_1')}")
print("| run | label | it | rho_u_max | rho_u below start | a_max_core | ratio | a_max_core_upper | ratio | (g) raised |")
print("|---|---|---:|---:|---|---:|---:|---:|---:|---|")
for rd in sys.argv[2:]:
    p = os.path.join(rd, "results.jsonl")
    if not os.path.isfile(p):
        print(f"| {os.path.basename(rd)} | no results.jsonl | | | | | | | | |"); continue
    r = [json.loads(l) for l in open(p) if l.strip()]; r = [x for x in r if x.get("kind") == "start_result"][-1]
    ac, au, ru = r.get("a_max_core"), r.get("a_max_core_upper"), r.get("rho_u_max")
    rc = (ac / ac0) if (ac is not None and ac0) else None; rup = (au / au0) if (au is not None and au0) else None
    down = (ru < ru0) if (ru is not None and ru0 is not None) else None
    g = (down and ((rc is not None and rc > 2.0) or (rup is not None and rup > 2.0))) if (down is not None and (rc is not None or rup is not None)) else None
    f = lambda v, fmt="%.4f": (fmt % v) if isinstance(v, (int, float)) else "n/a"
    print(f"| {os.path.basename(rd)[:34]} | {r.get('label')} | {r.get('iterations')} | {f(ru, '%.5f')} | {down} | {f(ac)} | {f(rc, '%.3f')} | {f(au)} | {f(rup, '%.3f')} | {g} |")
