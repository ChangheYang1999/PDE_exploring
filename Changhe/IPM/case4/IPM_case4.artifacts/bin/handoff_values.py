#!/usr/bin/env python3
"""Machine-readable values for HANDOFF_860.md from one read of the G5 run (reader only; writes one JSON file).
Records the SHA-256 of every reader before and after the read, the process family by ancestry with a nanosecond capture time, the
latest accepted checkpoint with recomputed hashes, per-slice walls, the last complete slice's resources, guard ledger counts, exact
clock offsets, disk figures, and the ETA record given on the command line.
Version 3 (lead review of HANDOFF v11, c4-lead/reviews/handoff_860_v11_review.md e8493447, findings 1, 3, 5, 7 with the lead's
corrections of 00:55Z and the verifier's creation-time note of 01:03Z):
 - finding 7: the supervisor counts as running only if the process named by SUPERVISOR_PID has arguments containing
   bin/supervise860_v4.sh and the run root (family.supervisor_identity_ok); otherwise family.supervisor is None and
   family.supervisor_unrelated_process is True;
 - finding 3: a run directory without result.json and without a ledger row is the run in progress only if the PID in its running.json
   field supervisor_pid (the guard) is alive with arguments containing hardware/guard.py and the guard session directory, the worker
   named by running.json is alive with PPID equal to the guard PID and IPM_RESOURCE_RUN (its environment and running.json
   controlled_environment) naming that run directory, the process creation times are consistent with the running.json start (the guard
   was created at most 600 s before started_time and not after it; the worker was created not before started_time and not after the
   running.json write; 2 s tolerance for the 1 s resolution of btime), and the creation ticks are stable across the read (PID reuse);
   every other directory without result.json is reported and not counted (run_dir_checks);
 - finding 1: at_cut restates the trial counts, the radius changes, the guard ledger (rows whose result.json finished_time is before
   the cut), the run in progress at the cut and its uncharged time to the cut, and lists every trial event and ledger row at or after
   the cut (valid only when the read is after the cut);
 - finding 5: the cut rule skips an accepted event without post_state.last_epoch (listed in handoff_state_skipped_events, as the
   launcher does) and, with no accepted event before the cut, writes handoff_state None with handoff_state_error instead of stopping.
Version 4 (verifier note 2026-10-26T01:27:00Z, lead request 01:32Z): a trial event whose post_state.last_epoch is missing or null is kept as
evidence with an unknown time (trial_events_unknown_time), excluded from every time computation (clock offsets, cut filter, at-cut lists)
and labelled 'unknown time', never 'at or after the cut'; the cut comparisons are exact (Fraction(last_epoch) < cut and integer
st_mtime_ns < cut in nanoseconds; the binary64 result of the launcher's rule is recorded beside it as before_cut_both_times_binary64).
Version 5 (verifier audit e223b67a (C) and qualifications, lead 01:42Z): walls.current_slice_complete says whether the latest slice of
state.json is in the completed population (a slice that completed while an assessment runs is included); family members carry their own
arguments and a kind (guard.py, campaign860.py slice worker, assess_cadence860.py assessment worker, or other such as sleep); utc(None) is
'unknown'; trial_block tolerates an empty gain population; active_runs_count is exported.
Version 6 (lead review of v13/v5, c4-lead/reviews/handoff_860_v13_review.md 4a3aef61, findings 8 to 10; lead request 02:25Z): the cadence
values use the last VALID full ledger row as assess_cadence860.py does (valid_full: failed False, mode full, is_full_assessment True,
returncode 0): assessments.last_valid, next_threshold_half_last_valid from it, halving_states from valid rows only, failed or
unvalidated rows listed apart (assessments.invalid_rows), the latest row's status kept separate (assessments.last, last_row_valid_full).
Version 7 (verifier audit a46e21f8 of v6): the threshold tests J_abs with 'is not None' instead of truthiness (a valid zero would otherwise be dropped).
Version 8 (lead request 04:10Z, verifier wording 04:04:43Z): trials.step_radius exact check: over the accepted trials the largest relative difference
|step_norm - radius_before| / radius_before as an exact rational (and its binary64 value) with the trial where it occurs, and whether all are within 1e-12.
Usage: handoff_values.py <root> <eta_record.json> <out.json> [--cut-epoch <epoch>]"""
_artifact_root = str(next(p for p in __import__("pathlib").Path(__file__).resolve().parents if (p / "work" / "research860").is_dir() and (p / "outputs").is_dir()))
import json, glob, os, sys, time, hashlib, statistics, subprocess, shutil
from fractions import Fraction
LANE = (_artifact_root)
root, eta_path, out = sys.argv[1], sys.argv[2], sys.argv[3]
root_abs = os.path.abspath(root)
CUT_ARG = sys.argv[sys.argv.index('--cut-epoch') + 1] if '--cut-epoch' in sys.argv else '1792987200'   # FINAL data cut 2026-10-26T04:00:00Z (lead rule 16:00:25Z)
CUT_FR = Fraction(CUT_ARG); CUT = float(CUT_FR); CUT_NS = CUT_FR * 10 ** 9
def before_cut(le, stt):
    """exact rule: Fraction(post_state.last_epoch) < cut and integer st_mtime_ns < cut in ns; None (missing or null last_epoch) is never before the cut"""
    return le is not None and Fraction(le) < CUT_FR and Fraction(stt.st_mtime_ns) < CUT_NS
def before_cut_binary64(le, stt):
    return le is not None and le < CUT and stt.st_mtime < CUT
READERS = ['bin/handoff_values.py', 'bin/handoff_read.sh', 'bin/handoff_apply.py', 'bin/handoff_refresh.py', 'bin/handoff_walls.py', 'bin/eta_observed860.py',
           'bin/launch_handoff_assess.sh', 'bin/trial_line.py', 'work/research/hardware/guard.py', 'work/research860/campaign860.py', 'work/research860/assess860.py', 'outputs/manifests/code_manifest_g4_v2.json', 'outputs/dev_policy_assess8_psi60.json']
def sha(p):
    h = hashlib.sha256()
    with open(p, 'rb') as f:
        for b in iter(lambda: f.read(1 << 20), b''): h.update(b)
    return h.hexdigest()
def reader_hashes():
    return {r: (sha(os.path.join(LANE, r)) if os.path.exists(os.path.join(LANE, r)) else None) for r in READERS}
def sh(cmd):
    return subprocess.run(cmd, shell=True, capture_output=True, text=True).stdout
def utc(e): return 'unknown' if e is None else time.strftime('%Y-%m-%dT%H:%M:%SZ', time.gmtime(e))
V = {'schema': 'handoff_values_v3', 'root': root_abs, 'lane': LANE}
V['readers_before'] = reader_hashes()
t0 = time.time_ns(); V['captured_epoch_ns'] = t0; V['captured_utc'] = time.strftime('%Y-%m-%dT%H:%M:%S', time.gmtime(t0 / 1e9)) + ('.%09dZ' % (t0 % 1000000000))
# process helpers
def psrow(pid):
    o = sh('ps -o pid=,ppid=,pgid=,sid=,ni=,etimes= -p %s' % pid).split()
    return dict(zip(('pid', 'ppid', 'pgid', 'sid', 'nice', 'etimes'), [int(x) for x in o])) if len(o) == 6 else None
def psargs(pid):
    return sh('ps -o args= -p %s' % pid).strip() if pid else ''
BTIME = int([l for l in open('/proc/stat') if l.startswith('btime')][0].split()[1]); HZ = os.sysconf('SC_CLK_TCK')
def proc_start_ticks(pid):
    try: return int(open('/proc/%s/stat' % pid).read().rsplit(')', 1)[1].split()[19])   # field 22 of /proc/<pid>/stat: creation time in clock ticks since boot
    except Exception: return None
def ticks_to_epoch(t): return None if t is None else BTIME + t / HZ
def proc_environ(pid):
    try: return dict(x.split('=', 1) for x in open('/proc/%s/environ' % pid, 'rb').read().decode(errors='replace').split('\0') if '=' in x)
    except Exception: return {}
# process family by ancestry
spid = open(os.path.join(root, 'SUPERVISOR_PID')).read().strip() if os.path.exists(os.path.join(root, 'SUPERVISOR_PID')) else None
fam = {'supervisor_pid': int(spid) if spid else None, 'supervisor': psrow(spid) if spid else None}
fam['supervisor_args'] = psargs(spid)[:240] if spid else ''
fam['supervisor_identity_ok'] = bool(fam['supervisor']) and ('bin/supervise860_v4.sh' in fam['supervisor_args']) and (root_abs in fam['supervisor_args'])   # finding 7
fam['supervisor_unrelated_process'] = bool(fam['supervisor']) and not fam['supervisor_identity_ok']
if fam['supervisor_unrelated_process']: fam['supervisor'] = None
g = sh('pgrep -P %s' % spid).split() if (spid and fam['supervisor']) else []
fam['guard'] = psrow(g[0]) if g else None; fam['guard_count'] = len(g); fam['guard_args'] = psargs(g[0])[:240] if g else ''
fam['guard_child_is_guard_py'] = bool(g) and ('hardware/guard.py' in fam['guard_args'])
w = sh('pgrep -P %s' % g[0]).split() if g else []
fam['worker'] = psrow(w[0]) if w else None; fam['worker_count'] = len(w); fam['worker_args'] = psargs(w[0])[:240] if w else ''
def proc_kind(args):
    if 'hardware/guard.py' in args: return 'guard (hardware/guard.py)'
    if 'research860/campaign860.py' in args: return 'slice worker (campaign860.py)'
    if 'research860/assess_cadence860.py' in args: return 'cadence assessment worker (assess_cadence860.py)'
    if 'research860/assess860.py' in args: return 'assessment (assess860.py)'
    return 'other (%s)' % (args.split()[0] if args else 'no process')
fam['guard_kind'] = proc_kind(fam['guard_args']) if g else None; fam['worker_kind'] = proc_kind(fam['worker_args']) if w else None
fam['pool_children'] = [int(x) for x in sh('pgrep -P %s' % w[0]).split()] if w else []
fam['affinity_supervisor'] = sh('taskset -cp %s' % spid).strip().split(':')[-1].strip() if (spid and fam['supervisor']) else None
fam['affinity_worker'] = sh('taskset -cp %s' % w[0]).strip().split(':')[-1].strip() if w else None
hb = json.load(open(os.path.join(root, 'HEARTBEAT.json'))) if os.path.exists(os.path.join(root, 'HEARTBEAT.json')) else {}
fam['heartbeat'] = hb; fam['heartbeat_pid_equals_worker'] = bool(w) and hb.get('pid') == int(w[0])
fam['markers'] = [m for m in ('STOP', 'STOPPED_FOR_DIAGNOSIS', 'FAULTED', 'DRIVER_REFUSED', 'SESSION_BUDGET_EXHAUSTED') if os.path.exists(os.path.join(root, m))]
V['family'] = fam
# state.json
st = json.load(open(os.path.join(root, 'state.json')))
V['state'] = {k: st.get(k) for k in ('trials', 'accepted', 'rejected', 'slices', 'objective', 'radius', 'iteration_wall_max_seconds', 'status', 'last_epoch')}
V['state']['validation_J_abs'] = (st.get('validation') or {}).get('J_abs'); V['state']['cl'] = (st.get('P') or [None])[0]
V['reserve_seconds'] = max(900.0, 1.5 * st['iteration_wall_max_seconds'])
# events
paths = sorted(glob.glob(os.path.join(root, 'commits', 'event_*.json'))); ev = [(p, json.load(open(p))) for p in paths]
V['events'] = {'count': len(ev), 'last_file': os.path.basename(paths[-1]), 'last_mtime_utc': utc(os.stat(paths[-1]).st_mtime), 'contiguous': [int(os.path.basename(p)[6:14]) for p in paths] == list(range(1, len(paths) + 1))}
tr = [(p, e) for p, e in ev if isinstance(e.get('trial'), dict) and 'accepted' in e['trial'] and 'iteration_wall_seconds' in e['trial']]
acc = [(p, e) for p, e in tr if e['trial']['accepted']]
def acc_record(p, e):
    t = e['trial']; ps = e['post_state']; stt = os.stat(p); cand = ps['candidate_path']; arrs = ps['arrays_path']; cs = sha(cand); ars = sha(arrs); le = ps.get('last_epoch')
    return {'event_file': os.path.basename(p), 'event_sequence': int(t['event_sequence']), 'trial': t['trial'], 'state': ps['accepted'],
    'event_mtime': stt.st_mtime, 'event_mtime_repr': repr(stt.st_mtime), 'event_mtime_ns': stt.st_mtime_ns, 'event_mtime_utc_ms': time.strftime('%Y-%m-%dT%H:%M:%S', time.gmtime(stt.st_mtime)) + '.%03dZ' % int((stt.st_mtime % 1) * 1000),
    'last_epoch': le, 'last_epoch_repr': repr(le), 'candidate_path': cand, 'candidate_sha256': cs, 'candidate_sha256_equals_post_state': cs == ps['candidate_sha256'],
    'arrays_path': arrs, 'arrays_sha256': ars, 'arrays_sha256_equals_post_state': ars == ps['arrays_sha256'], 'J_abs_independent': t['trial_J_abs_independent'], 'cl': t['trial_cl'], 'a0': t['trial_a0'],
    'five_Taylor_max': t['five_Taylor_max'], 'radius_after': t['radius_after'], 'percent_below_seed': 100.0 * (1.0 - t['trial_J_abs_independent'] / 4.2683726070956366e-09),
    'before_cut_both_times': bool(before_cut(le, stt)), 'before_cut_both_times_binary64': bool(before_cut_binary64(le, stt))}
p, e = max(acc, key=lambda pe: int(pe[1]['trial']['event_sequence'])); V['latest_accepted'] = acc_record(p, e)
# the cut rule (finding 5: skip an event without last_epoch as the launcher does; no stop when nothing qualifies)
V['handoff_state_skipped_events'] = [int(e_['trial']['event_sequence']) for _, e_ in acc if e_['post_state'].get('last_epoch') is None]
cutacc = [(p_, e_) for p_, e_ in acc if before_cut(e_['post_state'].get('last_epoch'), os.stat(p_))]
V['cut_rule'] = 'exact: Fraction(post_state.last_epoch) < cut and st_mtime_ns < cut * 10**9; an event with missing or null last_epoch is excluded from the time arithmetic and listed in trial_events_unknown_time'
V['trial_events_unknown_time'] = [{'event_file': os.path.basename(p_), 'event_sequence': int(e_['trial']['event_sequence']), 'trial': e_['trial']['trial'], 'accepted': bool(e_['trial']['accepted']), 'last_epoch_field': ('missing' if 'last_epoch' not in e_['post_state'] else 'null'), 'event_mtime_utc': utc(os.stat(p_).st_mtime), 'label': 'unknown time (no post_state.last_epoch; kept as evidence, excluded from the time arithmetic)'} for p_, e_ in tr if e_['post_state'].get('last_epoch') is None]
if cutacc:
    pc, ec = max(cutacc, key=lambda pe: int(pe[1]['trial']['event_sequence'])); V['handoff_state'] = acc_record(pc, ec); V['handoff_state_error'] = None
else:
    V['handoff_state'] = None; V['handoff_state_error'] = 'no accepted trial event with post_state.last_epoch and file mtime both before the cut %s' % utc(CUT)
V['cut_epoch'] = CUT; V['cut_epoch_exact'] = CUT_ARG; V['cut_utc'] = utc(CUT); V['read_after_cut'] = bool(Fraction(t0, 10 ** 9) >= CUT_FR)
V['handoff_state_equals_latest_accepted'] = bool(V['handoff_state']) and (V['handoff_state']['event_sequence'] == V['latest_accepted']['event_sequence'])
t = e['trial']; ps = e['post_state']
trials = [e['trial'] for _, e in tr]
def trial_block(trials_):
    return {'count': len(trials_), 'accepted': sum(1 for t in trials_ if t['accepted']), 'rejected': [t['trial'] for t in trials_ if not t['accepted']],
    'radius_changes': [{'trial': t['trial'], 'before': t['radius_before'], 'after': t['radius_after'], 'accepted': bool(t['accepted']), 'gain': t['gain_ratio']} for t in trials_ if t['radius_before'] != t['radius_after']],
    'gains_accepted_from_11': ({'min': min((t['gain_ratio'], t['trial']) for t in trials_ if t['accepted'] and t['trial'] >= 11), 'max': max((t['gain_ratio'], t['trial']) for t in trials_ if t['accepted'] and t['trial'] >= 11)} if any(t['accepted'] and t['trial'] >= 11 for t in trials_) else {'min': (None, None), 'max': (None, None)}),
    'last_trials': [{'trial': t['trial'], 'accepted': bool(t['accepted']), 'gain': t['gain_ratio'], 'radius_before': t['radius_before'], 'radius_after': t['radius_after']} for t in trials_[-12:]]}
V['trials'] = trial_block(trials)
def step_radius_check(trials_):
    worst = (Fraction(0), None); n = 0
    for t in trials_:
        if not t.get('accepted') or t.get('step_norm') is None or t.get('radius_before') in (None, 0): continue
        n += 1; rel = abs(Fraction(t['step_norm']) - Fraction(t['radius_before'])) / Fraction(t['radius_before'])
        if rel > worst[0]: worst = (rel, t['trial'])
    return {'accepted_trials_checked': n, 'max_relative_difference_exact': '%d/%d' % (worst[0].numerator, worst[0].denominator), 'max_relative_difference': float(worst[0]), 'at_trial': worst[1], 'all_within_1e-12': bool(worst[0] <= Fraction(1, 10 ** 12)), 'rule': 'exact rational |step_norm - radius_before| / radius_before over accepted trial events'}
V['trials']['step_radius'] = step_radius_check(trials)
# slices: complete ones from completion records
comp = [json.load(open(c)) for c in sorted(glob.glob(os.path.join(root, 'slice_completion', 'slice_*.json')))]
complete = sorted(c['slice'] for c in comp); cur = st.get('slices')
g5 = [t for t in trials if t['trial'] >= 14 and t['slice'] in complete]
sl = {}
for t in g5: sl.setdefault(t['slice'], []).append(t)
V['walls'] = {'domain_trials': [g5[0]['trial'], g5[-1]['trial']] if g5 else None, 'count': len(g5), 'complete_slices': [s for s in sorted(sl)], 'current_slice': cur, 'current_slice_complete': cur in complete, 'current_slice_end_utc': next((c_.get('utc') for c_ in comp if c_['slice'] == cur), None),
    'current_slice_commits': sum(1 for t in trials if t['slice'] == cur), 'min': min(t['iteration_wall_seconds'] for t in g5), 'max': max(t['iteration_wall_seconds'] for t in g5),
    'median': statistics.median(t['iteration_wall_seconds'] for t in g5), 'cpu_min': min(t['trial_cpu_seconds'] for t in g5), 'cpu_max': max(t['trial_cpu_seconds'] for t in g5),
    'rss_min': min(t['peak_rss_mib'] for t in g5), 'rss_max': max(t['peak_rss_mib'] for t in g5),
    'per_slice': [{'slice': s, 'trials': len(sl[s]), 'min': min(t['iteration_wall_seconds'] for t in sl[s]), 'max': max(t['iteration_wall_seconds'] for t in sl[s]), 'accepted': sum(1 for t in sl[s] if t['accepted'])} for s in sorted(sl)]}
# last complete slice
c = comp[-1]; rid = c['guard_run_id']; rdir = os.path.join(root, 'guard_session', 'runs', rid)
rows = [json.loads(l)['snapshot'] for l in open(os.path.join(rdir, 'resources.jsonl')) if l.strip()]; rj = json.load(open(os.path.join(rdir, 'result.json')))
starts = [e['trial'] for _, e in ev if e.get('trial', {}).get('kind') == 'slice_start' and e['trial'].get('slice') == c['slice']]
ends = [e['trial'] for _, e in ev if e.get('trial', {}).get('kind') == 'slice_end' and e['trial'].get('slice') == c['slice']]
ld = [r['load_1m'] for r in rows]
V['last_slice'] = {'slice': c['slice'], 'run_id': rid, 'start_utc': utc(starts[0]['epoch']) if starts else None, 'end_utc': c.get('utc'), 'status': c.get('status'), 'trials': c.get('trials_this_slice'),
    'accepted_this_slice': sum(1 for t in trials if t['slice'] == c['slice'] and t['accepted']), 'samples': len(rows), 'load_min': min(ld), 'load_max': max(ld), 'load_per_cpu_min': min(ld) / 96, 'load_per_cpu_max': max(ld) / 96,
    'psi_full_avg10_max': max(r.get('memory_psi_full_avg10') or 0 for r in rows), 'swap_used_max_mib': max(r.get('swap_used_mib') or 0 for r in rows), 'guard_success': rj.get('success'), 'guard_wall': rj.get('wall_seconds'),
    'peak_family_rss_mib': rj.get('peak_family_rss_mib'), 'solver_cpu_increment': (ends[0].get('solver_cpu_seconds_increment') if ends else None), 'worker_seconds': (ends[0].get('elapsed_worker_seconds_increment') if ends else None)}
# all slice runs: PSI history max
psi_hist = 0.0
for cc in comp:
    rf = os.path.join(root, 'guard_session', 'runs', cc['guard_run_id'], 'resources.jsonl')
    if os.path.exists(rf): psi_hist = max([psi_hist] + [json.loads(l)['snapshot'].get('memory_psi_full_avg10') or 0 for l in open(rf) if l.strip()])
V['psi_full_avg10_history_max'] = psi_hist
# guard ledger
led = [json.loads(l) for l in open(os.path.join(root, 'guard_session', 'session_ledger.jsonl')) if l.strip()]
kind = lambda r: 'slice' if 'slice' in r['run_id'] else ('assess_full' if r['wall_seconds'] > 100 else 'assess_check')
def ledger_block(led_):
    return {'rows': len(led_), 'total_seconds': sum(r['wall_seconds'] for r in led_), 'hours': sum(r['wall_seconds'] for r in led_) / 3600, 'slices': sum(1 for r in led_ if kind(r) == 'slice'),
    'pilot_slices': sum(1 for r in led_ if kind(r) == 'slice' and 'pilot' in r['run_id']), 'full_assessments': sum(1 for r in led_ if kind(r) == 'assess_full'), 'cadence_checks': sum(1 for r in led_ if kind(r) == 'assess_check'),
    'check_wall_min': min([r['wall_seconds'] for r in led_ if kind(r) == 'assess_check'] or [0]), 'check_wall_max': max([r['wall_seconds'] for r in led_ if kind(r) == 'assess_check'] or [0]),
    'full_wall_min': min([r['wall_seconds'] for r in led_ if kind(r) == 'assess_full'] or [0]), 'full_wall_max': max([r['wall_seconds'] for r in led_ if kind(r) == 'assess_full'] or [0]),
    'pilot_seconds': sum(r['wall_seconds'] for r in led_ if 'pilot' in r['run_id']), 'budget_seconds': 900000.0, 'hours_left_at_most': 250.0 - sum(r['wall_seconds'] for r in led_) / 3600}
V['guard_ledger'] = ledger_block(led)
cont = [json.loads(l) for l in open(os.path.join(root, 'continuations.jsonl')) if l.strip()]
V['continuations'] = {'rows': len(cont), 'all_bitwise': all(r.get('bitwise') for r in cont), 'max_residual_difference_norm': max(r.get('residual_difference_norm') or 0 for r in cont), 'last_utc': utc(cont[-1]['epoch']), 'last_trials': cont[-1].get('trials')}
al = [json.loads(l) for l in open(os.path.join(root, 'assessments', 'ledger.jsonl')) if l.strip()]
def valid_full(row): return isinstance(row, dict) and row.get('failed') is False and row.get('mode') == 'full' and row.get('is_full_assessment') is True and type(row.get('returncode')) is int and row.get('returncode') == 0   # assess_cadence860.py line 36
last_valid = next((x for x in reversed(al) if valid_full(x)), None)
rowkeys = ('utc', 'reason', 'accepted', 'J_abs', 'failed', 'scientific_stop', 'mode', 'returncode', 'output_sha256')
V['assessments'] = {'rows': len(al), 'last': {k: al[-1].get(k) for k in rowkeys}, 'last_row_valid_full': valid_full(al[-1]), 'last_valid': ({k: last_valid.get(k) for k in rowkeys} if last_valid else None),
    'valid_full_rows': sum(1 for a in al if valid_full(a)), 'invalid_rows': [{k: a.get(k) for k in rowkeys} for a in al if not valid_full(a)],
    'next_threshold_half_last_valid': (0.5 * last_valid['J_abs'] if (last_valid and last_valid.get('J_abs') is not None) else None), 'next_threshold_rule': 'half of the J_abs of the last valid full ledger row (assess_cadence860.py lines 36, 41 and 49), or 100 accepted trials since that row',
    'halving_states': [a['accepted'] for a in al if a.get('reason') == 'J_abs_halved' and valid_full(a)], 'halving_states_invalid': [a.get('accepted') for a in al if a.get('reason') == 'J_abs_halved' and not valid_full(a)]}
# clock offsets exact
offs = []
for p, e in tr:
    le = e['post_state'].get('last_epoch'); s_ = os.stat(p)
    if le is None: continue   # unknown time: listed in trial_events_unknown_time, excluded here
    offs.append(((Fraction(le) - Fraction(s_.st_mtime_ns, 10 ** 9)) * 1000, (le - s_.st_mtime) * 1000.0, int(e['trial']['event_sequence']), le, s_.st_mtime_ns))
mn = min(offs); mx = max(offs)
V['clock_offsets_ms'] = {'trial_events': len(offs), 'trial_events_unknown_time_excluded': len(tr) - len(offs), 'min_exact': float(mn[0]), 'min_event': mn[2], 'min_binary64_display': mn[1], 'max_exact': float(mx[0]), 'max_event': mx[2], 'max_binary64_display': mx[1], 'max_last_epoch_repr': repr(mx[3]), 'max_st_mtime_ns': mx[4],
    'arithmetic': 'Fraction(last_epoch) - Fraction(st_mtime_ns, 10**9), in ms; binary64 display = (last_epoch - st_mtime) * 1000'}
# disk
du = shutil.disk_usage((_artifact_root)); V['disk'] = {'mnt_build_free_gib': du.free / 2**30, 'mnt_build_total_gib': du.total / 2**30, 'run_dir_mib': int(sh('du -sm %s' % root).split()[0]), 'lane': sh('du -sh %s' % LANE).split()[0]}
# ETA record
ej = json.load(open(eta_path)); V['eta'] = {'path': os.path.relpath(eta_path, LANE), 'sha256': sha(eta_path), 'utc': ej.get('utc'), 'trials': ej.get('trials'), 'median': ej.get('iteration_wall_median'), 'mean': ej.get('iteration_wall_mean'), 'max': ej.get('iteration_wall_max'),
    'trials_per_slice': ej.get('trials_per_slice_model'), 'slice_wall': ej.get('slice_wall_estimate_seconds'), 'trials_per_hour': ej.get('trials_per_hour_model'), 'reserve_used': ej.get('reserve_seconds'), 'script_sha256': V['readers_before']['bin/eta_observed860.py']}
# launcher dry run (creates nothing)
dry = sh('cd %s && bash bin/launch_handoff_assess.sh --dry-run 2>&1' % LANE).splitlines()
V['launcher_dry_run'] = {'lines': [l for l in dry if not l.startswith('command:')][:6], 'script_sha256': V['readers_before']['bin/launch_handoff_assess.sh']}
# measured throughput over the complete G5 slices and all G5 guarded runs (lead review 4d30f1b0 finding 1)
def run_start_epoch(rid):
    try: return int(rid.split('_')[1]) / 1e9
    except Exception: return None
def run_finish_epoch(r):
    rp = os.path.join(root, 'guard_session', 'runs', r['run_id'], 'result.json')
    if os.path.exists(rp):
        j = json.load(open(rp))
        if j.get('finished_time') is not None: return j['finished_time']
        if j.get('started_time') is not None: return j['started_time'] + r['wall_seconds']
    s_ = run_start_epoch(r['run_id']); return (s_ + r['wall_seconds']) if s_ is not None else None
comp_g5 = [c for c in comp if 'g5' in c['guard_run_id']]
led_by_id = {r['run_id']: r for r in led}
# the genuinely active guarded run (finding 3): a run directory of the root's guard session without result.json and without a ledger row,
# whose running.json names a live guard (PID, arguments) and a live worker bound to that directory, with creation times consistent with the
# running.json start and stable across the read
SESSION_DIR = os.path.join(root_abs, 'guard_session')
def live_run_check(rdir_abs):
    rid_ = os.path.basename(rdir_abs); rjp = os.path.join(rdir_abs, 'running.json'); info = {'run_id': rid_, 'running_json': os.path.exists(rjp)}
    if not info['running_json']:
        info.update(live=False, counted=False, report='stale run directory %s (no live guard; no running.json)' % rid_); return info
    rj_ = json.load(open(rjp)); gp = rj_.get('supervisor_pid'); wp = rj_.get('worker_pid'); st_t = rj_.get('started_time'); rj_m = os.stat(rjp).st_mtime
    g_t1 = proc_start_ticks(gp) if gp else None; w_t1 = proc_start_ticks(wp) if wp else None
    g_row = psrow(gp) if gp else None; w_row = psrow(wp) if wp else None; g_args = psargs(gp) if gp else ''; w_env = proc_environ(wp) if wp else {}
    g_t2 = proc_start_ticks(gp) if gp else None; w_t2 = proc_start_ticks(wp) if wp else None
    g_s = ticks_to_epoch(g_t1); w_s = ticks_to_epoch(w_t1)
    checks = {'guard_alive': bool(g_row), 'guard_args_contain_guard_py': 'hardware/guard.py' in g_args, 'guard_args_contain_session_dir': SESSION_DIR in g_args,
        'guard_created_not_after_started_time': (g_s is not None and st_t is not None and g_s <= st_t + 2.0), 'guard_created_at_most_600s_before_started_time': (g_s is not None and st_t is not None and g_s >= st_t - 600.0),
        'worker_alive': bool(w_row), 'worker_ppid_is_guard': bool(w_row) and gp is not None and w_row['ppid'] == gp,
        'worker_env_IPM_RESOURCE_RUN_is_run_dir': w_env.get('IPM_RESOURCE_RUN') == rdir_abs, 'running_json_controlled_env_names_run_dir': (rj_.get('controlled_environment') or {}).get('IPM_RESOURCE_RUN') == rdir_abs,
        'worker_created_between_started_time_and_running_json_write': (w_s is not None and st_t is not None and (st_t - 2.0) <= w_s <= (rj_m + 2.0)),
        'creation_ticks_stable_across_read': (g_t1 is not None and w_t1 is not None and g_t1 == g_t2 and w_t1 == w_t2)}
    live = all(checks.values()); guard_ok = checks['guard_alive'] and checks['guard_args_contain_guard_py'] and checks['guard_args_contain_session_dir']
    info.update(guard_pid=gp, worker_pid=wp, started_time=st_t, started_time_utc=(utc(st_t) if st_t else None), running_json_mtime=rj_m, guard_created_epoch=g_s, worker_created_epoch=w_s, guard_args=g_args[:300], checks=checks, checks_passed=sum(1 for v in checks.values() if v), checks_total=len(checks), live=live, counted=live,
        report=('live guard %s bound to run directory %s (all %d checks passed)' % (gp, rid_, len(checks))) if live else (('stale run directory %s (no live guard)' % rid_) if not guard_ok else ('run directory %s not counted (guard %s alive but binding failed: %s)' % (rid_, gp, ', '.join(k for k, v in checks.items() if not v)))))
    return info
ledger_ids = {r['run_id'] for r in led}
no_result = [dd for dd in sorted(glob.glob(os.path.join(root_abs, 'guard_session', 'runs', '*'))) if os.path.isdir(dd) and not os.path.exists(os.path.join(dd, 'result.json')) and os.path.basename(dd) not in ledger_ids]
V['active_run_dirs_without_result'] = [os.path.basename(dd) for dd in no_result]
V['run_dir_checks'] = [live_run_check(dd) for dd in no_result]
active = [ck['run_id'] for ck in V['run_dir_checks'] if ck['live']]
V['stale_run_dirs'] = [ck['report'] for ck in V['run_dir_checks'] if not ck['live']]
guard_alive = bool(active)   # a live guard bound to a run directory (the supervisor's first child alone is not used: between slices it can be a sleep, and a guard can survive its supervisor)
V['active_runs'] = active; V['active_runs_count'] = len(active)
cur_start = run_start_epoch(active[-1]) if active else None
V['active_run'] = {'run_id': active[-1], 'start_utc': utc(cur_start), 'kind': ('assessment' if 'assess' in active[-1] else 'slice'), 'heartbeat_run_id_equals_active': hb.get('guard_run_id') == active[-1], 'guard_pid': [ck for ck in V['run_dir_checks'] if ck['run_id'] == active[-1]][0]['guard_pid'], 'checks_passed': [ck for ck in V['run_dir_checks'] if ck['run_id'] == active[-1]][0]['checks_passed'], 'checks_total': [ck for ck in V['run_dir_checks'] if ck['run_id'] == active[-1]][0]['checks_total']} if active else None
cap_s = t0 / 1e9
def throughput(led_, comp_g5_, trials_, cur_start_, at_s, cur_id):
    slice_rows = [led_by_id[c['guard_run_id']] for c in comp_g5_ if c['guard_run_id'] in led_by_id and led_by_id[c['guard_run_id']] in led_]
    g5_rows = [r for r in led_ if 'g5' in r['run_id']]
    g5_trials_complete = sum(1 for t in trials_ if t['trial'] >= 14 and t['slice'] in [c['slice'] for c in comp_g5_])
    slice_wall_sum = sum(r['wall_seconds'] for r in slice_rows); g5_wall_sum = sum(r['wall_seconds'] for r in g5_rows)
    starts_ = [run_start_epoch(r['run_id']) for r in g5_rows]; ends_ = [run_start_epoch(r['run_id']) + r['wall_seconds'] for r in g5_rows]
    clock_span = max(ends_) - min(starts_) if g5_rows else None
    uncharged_h = (at_s - cur_start_) / 3600 if cur_start_ else 0.0
    left_ledger_h = (900000.0 - sum(r['wall_seconds'] for r in led_)) / 3600
    left_after_h = left_ledger_h - uncharged_h
    rate_slice = g5_trials_complete / (slice_wall_sum / 3600) if slice_wall_sum else None
    rate_all = g5_trials_complete / (g5_wall_sum / 3600) if g5_wall_sum else None
    frac = g5_wall_sum / clock_span if clock_span else None
    end_not_before = (cur_start_ + left_ledger_h * 3600) if cur_start_ else None
    end_at_fraction = (cur_start_ + left_ledger_h * 3600 / frac) if (cur_start_ and frac) else None
    return {'complete_g5_slices': [c['slice'] for c in comp_g5_], 'trials_in_complete_g5_slices': g5_trials_complete, 'slice_guard_wall_seconds': slice_wall_sum, 'trials_per_slice_hour': rate_slice,
    'g5_guarded_runs': len(g5_rows), 'g5_full_assessments': sum(1 for r in g5_rows if 'assess' in r['run_id'] and r['wall_seconds'] > 100), 'g5_cadence_checks': sum(1 for r in g5_rows if 'assess' in r['run_id'] and r['wall_seconds'] <= 100),
    'g5_guarded_wall_seconds': g5_wall_sum, 'trials_per_hour_all_g5_guarded': rate_all, 'guarded_fraction_of_clock': frac, 'hours_left_by_ledger': left_ledger_h,
    'current_run_start_utc': utc(cur_start_) if cur_start_ else None, 'current_run_id': cur_id, 'current_run_uncharged_hours': uncharged_h, 'hours_left_after_uncharged': left_after_h,
    'further_trials_min': (left_after_h * rate_all) if rate_all else None, 'further_trials_max': (left_after_h * rate_slice) if rate_slice else None,
    'budget_end_not_before_utc': time.strftime('%Y-%m-%dT%H:%M:%SZ', time.gmtime(end_not_before)) if end_not_before else None,
    'budget_end_at_fraction_utc': time.strftime('%Y-%m-%dT%H:%M:%SZ', time.gmtime(end_at_fraction)) if end_at_fraction else None,
    'budget_end_at_fraction_utc_minute': time.strftime('%Y-%m-%dT%H:%MZ', time.gmtime(end_at_fraction)) if end_at_fraction else None}
tp = throughput(led, comp_g5, trials, cur_start, cap_s, (active[-1] if active else None))
ej2 = json.load(open(eta_path)); ov = ej2.get('slice_overhead_seconds') or []
med = ej2.get('iteration_wall_median'); ov_mean = statistics.mean(ov) if ov else None; ov_resume = statistics.mean(ov[1:]) if len(ov) > 1 else None
limits = []
for n in (6, 5, 4):
    lim = 5000.0 - ov_mean - (n - 1) * med if (ov_mean is not None and med) else None
    limits.append({'starts': n, 'reserve_at_most': lim, 'stored_max_wall_at_most': (lim / 1.5 if lim else None), 'model_trials_per_slice_hour': (n / ((ov_mean + n * med + 15.0) / 3600) if lim else None)})
tp.update({'guard_alive_at_read': guard_alive, 'reserve_seconds': V['reserve_seconds'], 'overhead_mean_all_slices': ov_mean, 'overhead_count': len(ov), 'overhead_first': (ov[0] if ov else None), 'overhead_resume_mean': ov_resume, 'start_limits': limits})
V['throughput'] = tp
# values AT THE CUT (finding 1): trial events with both times before the cut; ledger rows finished before the cut; the run in progress at the cut
def both_before(p_, e_):
    return before_cut(e_['post_state'].get('last_epoch'), os.stat(p_))
tr_cut = [(p_, e_) for p_, e_ in tr if both_before(p_, e_)]; trials_cut = [e_['trial'] for _, e_ in tr_cut]
ev_after = [{'event_file': os.path.basename(p_), 'event_sequence': int(e_['trial']['event_sequence']), 'trial': e_['trial']['trial'], 'accepted': bool(e_['trial']['accepted']), 'last_epoch_utc': utc(e_['post_state']['last_epoch']), 'event_mtime_utc': utc(os.stat(p_).st_mtime)} for p_, e_ in tr if e_['post_state'].get('last_epoch') is not None and not both_before(p_, e_)]
led_fin = [(r, run_finish_epoch(r)) for r in led]
led_cut = [r for r, f in led_fin if f is not None and f < CUT]
led_after = [{'run_id': r['run_id'], 'wall_seconds': r['wall_seconds'], 'start_utc': utc(run_start_epoch(r['run_id'])) if run_start_epoch(r['run_id']) else None, 'finished_utc': utc(f) if f else None} for r, f in led_fin if not (f is not None and f < CUT)]
prog_cut = [r['run_id'] for r, f in led_fin if run_start_epoch(r['run_id']) is not None and run_start_epoch(r['run_id']) < CUT and (f is None or f >= CUT)] + [a for a in active if run_start_epoch(a) is not None and run_start_epoch(a) < CUT]
comp_g5_cut = [c for c in comp_g5 if c['guard_run_id'] in led_by_id and run_finish_epoch(led_by_id[c['guard_run_id']]) is not None and run_finish_epoch(led_by_id[c['guard_run_id']]) < CUT]
cur_start_cut = run_start_epoch(prog_cut[-1]) if prog_cut else None
V['at_cut'] = {'valid': V['read_after_cut'], 'cut_utc': utc(CUT), 'note': ('values at the cut, restated from events with both times before the cut, ledger rows whose result.json finished_time is before the cut, and the run in progress at the cut' if V['read_after_cut'] else 'the read is before the cut: not computed as cut values (the cut is in the future)'),
    'trials': (dict(trial_block(trials_cut), step_radius=step_radius_check(trials_cut)) if trials_cut else None), 'last_trial_event_sequence_before_cut': max([int(e_['trial']['event_sequence']) for _, e_ in tr_cut] or [0]), 'trial_events_at_or_after_cut': ev_after, 'trial_events_unknown_time': V['trial_events_unknown_time'],
    'guard_ledger': ledger_block(led_cut), 'ledger_rows_at_or_after_cut': led_after, 'run_in_progress_at_cut': (prog_cut[-1] if prog_cut else None), 'runs_in_progress_at_cut_all': prog_cut,
    'throughput': throughput(led_cut, comp_g5_cut, trials_cut, cur_start_cut, CUT, (prog_cut[-1] if prog_cut else None)) if (trials_cut and led_cut) else None}
V['readers_after'] = reader_hashes(); V['readers_unchanged_during_read'] = V['readers_before'] == V['readers_after']
t1 = time.time_ns(); V['captured_end_utc'] = time.strftime('%Y-%m-%dT%H:%M:%S', time.gmtime(t1 / 1e9)) + ('.%09dZ' % (t1 % 1000000000))
json.dump(V, open(out, 'w'), indent=1); print('wrote', out, sha(out))
