#!/usr/bin/env python3
"""One-screen status of an 860 campaign root (no numerical imports). Usage: status860.py <campaign-root>"""
import json, sys, time, os, glob
from pathlib import Path
root = Path(sys.argv[1]); st = json.loads((root/'state.json').read_text()) if (root/'state.json').exists() else {}
hb = (root/'HEARTBEAT.json'); hbj = json.loads(hb.read_text()) if hb.exists() else {}
pid = (root/'SUPERVISOR_PID').read_text().strip() if (root/'SUPERVISOR_PID').exists() else None
alive = pid and os.path.exists('/proc/'+pid)
events = sorted(glob.glob(str(root/'commits'/'event_*.json'))); rows = [json.loads(l) for l in (root/'trajectory.jsonl').read_text().splitlines()] if (root/'trajectory.jsonl').exists() else []
trials = [r for r in rows if 'trial' in r and 'trial_wall_seconds' in r]
acc = [r for r in trials if r.get('accepted')]
du = sum(f.stat().st_size for f in root.rglob('*') if f.is_file())/2**20
print(json.dumps({'root': str(root), 'utc': time.strftime('%Y-%m-%dT%H:%M:%SZ', time.gmtime()), 'supervisor_pid': pid, 'supervisor_alive': bool(alive), 'status': st.get('status'), 'slices': st.get('slices'),
  'trials': st.get('trials'), 'accepted': st.get('accepted'), 'rejected': st.get('rejected'), 'consecutive_rejections': st.get('consecutive_rejections'),
  'J_mesh': st.get('objective'), 'J_abs_independent': (st.get('validation') or {}).get('J_abs'), 'error_abs': (st.get('validation') or {}).get('error_abs'), 'cl': (st.get('P') or [None])[0], 'radius': st.get('radius'),
  'events': len(events), 'last_heartbeat': hbj.get('utc'), 'elapsed_worker_seconds': st.get('elapsed_worker_seconds'), 'solver_cpu_seconds': st.get('solver_cpu_seconds'),
  'median_trial_wall_s': sorted(r['trial_wall_seconds'] for r in trials)[len(trials)//2] if trials else None, 'acceptance_rate': (len(acc)/len(trials)) if trials else None,
  'last_trial': {k: trials[-1].get(k) for k in ('trial', 'accepted', 'gain_ratio', 'predicted_decrease', 'actual_mesh_decrease', 'failure', 'trial_wall_seconds')} if trials else None,
  'disk_mib': du, 'widths': (st.get('widths_history') or [None])[-1]}, indent=1))
