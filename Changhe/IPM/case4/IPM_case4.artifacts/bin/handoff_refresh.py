#!/usr/bin/env python3
"""Read-only refresh of the numbers listed in HANDOFF_860.md section 11: process family, latest checkpoint and its SHA-256 values, latest guard sample,
run directory size and free space, guarded hours of the 250 h budget, markers, last events. Usage: handoff_refresh.py [campaign-root]"""
_artifact_root = str(next(p for p in __import__("pathlib").Path(__file__).resolve().parents if (p / "work" / "research860").is_dir() and (p / "outputs").is_dir()))
import json, os, sys, glob, hashlib, time, subprocess, shutil
LANE = (_artifact_root); root = sys.argv[1] if len(sys.argv) > 1 else LANE + '/outputs/campaign860/pilot_g4_v2'
now = time.time(); print('refresh at', time.strftime('%Y-%m-%dT%H:%M:%SZ', time.gmtime(now)), 'root', root)
def sha(p):
    h = hashlib.sha256()
    with open(p, 'rb') as f:
        for b in iter(lambda: f.read(1 << 20), b''): h.update(b)
    return h.hexdigest()
def sh(cmd): return subprocess.run(cmd, shell=True, capture_output=True, text=True).stdout.strip()
pidf = os.path.join(root, 'SUPERVISOR_PID'); spid = open(pidf).read().strip() if os.path.exists(pidf) else None
print('supervisor pid file', spid, 'alive', bool(spid and os.path.exists('/proc/' + spid)), '|', sh('ps -o pid=,ppid=,pgid=,sid=,ni=,etimes=,args= -p %s' % spid)[:140] if spid else '')
print('family:'); print(sh("pgrep -af 'pilot_g4_v[2]' | grep -v shell-snapshots | cut -c1-150"))
hb = os.path.join(root, 'HEARTBEAT.json'); hbj = json.loads(open(hb).read()) if os.path.exists(hb) else {}
print('heartbeat', {k: hbj.get(k) for k in ('phase', 'slice', 'trials', 'accepted', 'phase_trial', 'utc', 'pid', 'guard_run_id')}, 'age s', round(now - (hbj.get('epoch') or now)))
print('markers:', [m for m in ('STOP', 'STOPPED_FOR_DIAGNOSIS', 'FAULTED', 'DRIVER_REFUSED', 'SESSION_BUDGET_EXHAUSTED') if os.path.exists(os.path.join(root, m))])
print('supervisor.log tail:'); print('\n'.join('   ' + l[:200] for l in open(os.path.join(root, 'supervisor.log')).read().splitlines()[-3:]))
st = json.loads(open(os.path.join(root, 'state.json')).read())
print('state.json: trials %s accepted %s rejected %s slices %s status %s objective %r J_abs_independent %r cl %r radius %r iteration_wall_max %r' % (st.get('trials'), st.get('accepted'), st.get('rejected'), st.get('slices'), st.get('status'), st.get('objective'), (st.get('validation') or {}).get('J_abs'), (st.get('P') or [None])[0], st.get('radius'), st.get('iteration_wall_max_seconds')))
snaps = sorted(glob.glob(os.path.join(root, 'snapshots', 'accepted_*.json')))
if snaps:
    sj = snaps[-1]; sn = sj[:-5] + '.npz'; cand = json.loads(open(sj).read())
    print('latest checkpoint', os.path.basename(sj), 'mtime', time.strftime('%Y-%m-%dT%H:%M:%SZ', time.gmtime(os.path.getmtime(sj))), 'sha256', sha(sj)); print('   npz', os.path.basename(sn), 'sha256', sha(sn) if os.path.exists(sn) else 'missing')
    print('   a0', cand.get('a0'), 'objectives', cand.get('objectives'), 'accepted_trials', cand.get('accepted_trials'), 'total_trials', cand.get('total_trials'))
evs = sorted(glob.glob(os.path.join(root, 'commits', 'event_*.json'))); print('events', len(evs), 'last', os.path.basename(evs[-1]) if evs else None, 'mtime', time.strftime('%Y-%m-%dT%H:%M:%SZ', time.gmtime(os.path.getmtime(evs[-1]))) if evs else None)
runs = sorted(glob.glob(os.path.join(root, 'guard_session', 'runs', '*')), key=os.path.getmtime)
if runs:
    r = runs[-1]; res = os.path.join(r, 'resources.jsonl'); last = None
    if os.path.exists(res):
        with open(res) as f:
            for l in f:
                if l.strip(): last = l
        if last:
            s = json.loads(last).get('snapshot') or {}; print('latest guard run', os.path.basename(r), 'sample:', {k: s.get(k) for k in ('family_rss_mib', 'family_threads', 'load_1m', 'load_per_cpu', 'disk_free_gib', 'available_mib', 'memory_psi_full_avg10')}, 'elapsed', json.loads(last).get('elapsed_seconds'))
    rj = os.path.join(r, 'result.json')
    if os.path.exists(rj): d = json.loads(open(rj).read()); print('   result.json', {k: d.get(k) for k in ('success', 'returncode', 'stop_reasons', 'wall_seconds', 'peak_family_rss_mib')})
    else: print('   result.json not yet written (run in progress)')
tot = 0
for dp, dn, fn in os.walk(root):
    for f in fn:
        try: tot += os.path.getsize(os.path.join(dp, f))
        except FileNotFoundError: pass
du = shutil.disk_usage((_artifact_root)); print(('run dir %.1f MiB; ' + _artifact_root + ' free %.1f GiB of %.0f GiB') % (tot / 2**20, du.free / 2**30, du.total / 2**30))
led = os.path.join(root, 'guard_session', 'session_ledger.jsonl'); rows = [json.loads(l) for l in open(led) if l.strip()] if os.path.exists(led) else []
tw = sum(x.get('wall_seconds') or 0 for x in rows); print('guard ledger: %d completed runs, %.0f s = %.2f h of the 250 h cumulative budget (max_session_seconds 900000)' % (len(rows), tw, tw / 3600))
al = os.path.join(root, 'assessments', 'ledger.jsonl'); arows = [json.loads(l) for l in open(al) if l.strip()] if os.path.exists(al) else []
print('assessment ledger rows', len(arows), 'last:', {k: arows[-1].get(k) for k in ('utc', 'reason', 'accepted', 'J_abs', 'failed', 'scientific_stop', 'output_sha256')} if arows else None)
