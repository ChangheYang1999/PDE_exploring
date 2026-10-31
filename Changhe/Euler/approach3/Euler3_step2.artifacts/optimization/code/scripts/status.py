#!/usr/bin/env python
"""Print the campaign status (from status/STATUS.json and the ledger)."""
import sys, os, json, time
ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
sys.path.insert(0, ROOT)
from src.campaign import ledger
p = os.path.join(ROOT, "status", "STATUS.json")
if os.path.exists(p):
    st = json.load(open(p))
    print(f"status written {st['ts']}  elapsed {st['elapsed_hours']:.2f} h  stage {st['stage']}  pending {st['pending']} running {len(st['running'])} done {st['done']} failed {st['failed']}  starts {st['starts_completed']}  best rms {st['best_rms']}")
    for k, v in st["running"].items():
        print(f"  running {k}: gpu {v['gpu']} pid {v['pid']} {v['minutes']} min heartbeat age {v['heartbeat_age_s']}")
    print("  gpus:", st.get("gpus"), " disk free GB:", st.get("disk_free_GB"), " lane GB:", st.get("lane_usage_GB"))
    hb = json.load(open(os.path.join(ROOT, "status", "supervisor_heartbeat.json")))
    print(f"  supervisor heartbeat age {time.time()-hb['epoch']:.0f}s pid {hb['pid']}")
else:
    print("no STATUS.json yet")
recs = ledger.read(os.path.join(ROOT, "status", "ledger.jsonl"))
ver = sys.argv[2] if len(sys.argv) > 2 else "latest"
board = ledger.leaderboard(recs, n=int(sys.argv[1]) if len(sys.argv) > 1 else 10, solver_version=ver)
print(f"leaderboard restricted to solver_version={ver} (pass 'all' as second argument for every version)")
print(f"ledger: {len(recs)} records, {sum(1 for r in recs if r.get('kind')=='start_result')} start results")
for b in board:
    ru = b.get('rho_u_max'); rnl = b.get('rho_nl_max')
    print(f"  key={b['rank_key']:.3e} rho_u={('%.2e' % ru) if ru is not None else '  n/a  '} rho_nl={('%.2e' % rnl) if rnl is not None else '  n/a  '} {b['job_id']}/{b['start']} {b['family']:8s} c_l={b['c_l']:.3f} om={b['omega']:+.2f} L={b['L']} {b['formulation']}{'+nlw' if b.get('nl_weighting') else ''} |Om|={b['max_abs_Omega']:.1e} e_F={b.get('e_F', b['tail_nonaxi']):.2f} N_core={b.get('N_core', float('nan')):.1e} lamS={b.get('lambda_max_S', float('nan')):.2f} r_core={b.get('r_core', float('nan')):.2g} r_tail={b.get('r_tail')} {b['status']}")
