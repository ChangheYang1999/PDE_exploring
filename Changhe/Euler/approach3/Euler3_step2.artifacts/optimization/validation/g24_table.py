#!/usr/bin/env python
"""Markdown rows for the NUM_REPORT G2 (c)/G4 (a) completion table from validation/g24_complete_*.json (reading only). Usage: python validation/g24_table.py"""
import json, glob, os, hashlib
ORDER = ["S01_own", "S09_own", "S05_own", "manu_large_omega", "S01_shift_a", "S05_shift_c", "S20_own", "S11_own", "manu_a", "manu_allm_c", "manu_small_omega", "manu_near_edge"]
rows = {}
for f in glob.glob(os.path.join(os.path.dirname(os.path.abspath(__file__)), "g24_complete_*.json")):
    d = json.load(open(f)); sha = hashlib.sha256(open(f, "rb").read()).hexdigest()[:16]
    cells = []
    for pn in ("c_l", "omega"):
        v = d["parameters"][pn]; g2 = v["G2c"]; g4 = v["G4a"]; w2 = g2["decision_whole"]; w4 = g4["decision_whole"]
        cells.append(f"{pn}: G2 (c) {'PASS' if g2['complete_PASS'] else 'FAIL'} (whole (i) {w2['pair_i']}, (ii) {w2['pair_ii']}, Richardson {w2['richardson_pair']} {w2['richardson_error']:.1e}; groups {'all PASS' if all(x['PASS_any'] for x in g2['decision_per_group'].values()) else [g for g, x in g2['decision_per_group'].items() if not x['PASS_any']]}); G4 (a) {'PASS' if g4['complete_PASS'] else 'FAIL'} (resolved (i) {w4['pair_i']}, (ii) {w4['pair_ii']}, Richardson {w4['richardson_pair']} {w4['richardson_error']:.1e}; outside the resolved range {'PASS' if all(g4['groups_outside_resolved_range'].values()) else g4['groups_outside_resolved_range']})")
    rows[d["case"]] = f"| {d['case']} | {d['status']} (worst tie {d['worst_tie_rel_diff']:.1e}; case tie {d['case_tie']['ok']}) | {'PASS' if d['complete_PASS_all'] else 'FAIL'} | {' / '.join(cells)} | {d['ts']} ({d['seconds']:.0f} s) | {os.path.basename(f)} ({sha}); arrays {', '.join(v['arrays_sha256'][:8] for v in d['parameters'].values())} in the frozen copy |"
for c in ORDER:
    if c in rows:
        print(rows[c])
for c in rows:
    if c not in ORDER:
        print(rows[c])
