#!/usr/bin/env python3
"""Apply one committed trial event to the numerics documents: WORKLOG.md line, NUM_REPORT.md G5 table row and best-state sentence,
RESULTS_860.md section-5 row, OPTIMIZATION_860_LOG.md line. Idempotent (skips rows already present). Reader of the root; writer of the lane documents only.
Usage: trial_apply.py <campaign-root> <event-number> [--note "..."]"""
_artifact_root = str(next(p for p in __import__("pathlib").Path(__file__).resolve().parents if (p / "work" / "research860").is_dir() and (p / "outputs").is_dir()))
import json, sys, subprocess, time, re
from pathlib import Path
LANE = Path((_artifact_root)); root = Path(sys.argv[1]); n = int(sys.argv[2])
note = sys.argv[sys.argv.index('--note')+1] if '--note' in sys.argv else ''
out = subprocess.run([str(LANE/'env/bin/python'), '-B', str(LANE/'bin/trial_line.py'), str(root), str(n)], capture_output=True, text=True, check=True).stdout
lines = out.splitlines()
def after(tag):
    i = [k for k, l in enumerate(lines) if l.startswith(tag)][0]; return lines[i+1] if not lines[i][len(tag):].strip() else lines[i][len(tag):].strip()
wl = after('WORKLOG:'); nr = after('NUM_REPORT row:'); rr = after('RESULTS_860 row:'); ol = after('OPT_LOG row:')
ev = json.loads((root/'commits'/('event_%08d.json' % n)).read_text()); t = ev['trial']; trial = t['trial']; acc_after = t['accepted_after']
cutc = time.strftime('%Y-%m-%dT%H:%M:%SZ', time.gmtime((root/'commits'/('event_%08d.json' % n)).stat().st_mtime))
now = time.strftime('%Y-%m-%dT%H:%M:%SZ', time.gmtime())
# WORKLOG
p = LANE/'WORKLOG.md'; s = p.read_text()
if ('TRIAL %d ' % trial) not in s.split('SHIFT 7 START')[-1] or ('event %d;' % n) not in s:
    s = s.rstrip('\n') + '\n- %s (commit %s) %s%s\n' % (now, cutc, wl, (' ' + note) if note else ''); p.write_text(s); print('WORKLOG appended')
else: print('WORKLOG already has the line')
# NUM_REPORT: insert after the previous trial row (table rows start with two spaces and '| <trial> |')
p = LANE/'NUM_REPORT.md'; s = p.read_text()
if nr not in s:
    prev = None
    for k in range(trial-1, 0, -1):
        m = re.search(r'^  \| %d \| \d+ \| .*$' % k, s, re.M)
        if m: prev = m; break
    assert prev, 'no previous row'; j = prev.end()+1; s = s[:j] + nr + '\n' + s[j:]
    if t.get('accepted'):
        m = re.search(r'Best accepted state: snapshots/accepted_(\d{8})\.json \(sha256 [0-9a-f]{8}\.\.\.; J_abs [0-9.e+-]+, -[0-9.]+ percent vs the seed; c_l [0-9.]+, a_0 [0-9.]+, five-Taylor [0-9.e+-]+; not yet assessed\)\.', s)
        if m:
            import hashlib
            snap = root/'snapshots'/('accepted_%08d.json' % acc_after); sha = hashlib.sha256(snap.read_bytes()).hexdigest()[:8]
            seedJ = 4.2683726070956366e-09; J = t['trial_J_abs_independent']
            new = 'Best accepted state: snapshots/accepted_%08d.json (sha256 %s...; J_abs %r, %.2f percent vs the seed; c_l %r, a_0 %r, five-Taylor %.1e; not yet assessed).' % (acc_after, sha, J, 100*(J-seedJ)/seedJ, t['trial_cl'], t['trial_a0'], t['five_Taylor_max'])
            s = s[:m.start()] + new + s[m.end():]
    p.write_text(s); print('NUM_REPORT updated')
else: print('NUM_REPORT already has the row')
# RESULTS_860
p = LANE/'RESULTS_860.md'; s = p.read_text()
if rr not in s:
    prev = None
    for k in range(trial-1, 0, -1):
        m = re.search(r'^\| %d \(G5\) \| \d+ \| .*$' % k, s, re.M)
        if m: prev = m; break
    assert prev, 'no previous row'; j = prev.end()+1; s = s[:j] + rr + '\n' + s[j:]; p.write_text(s); print('RESULTS_860 updated')
else: print('RESULTS_860 already has the row')
# OPTIMIZATION_860_LOG
p = LANE/'OPTIMIZATION_860_LOG.md'; s = p.read_text()
if ('TRIAL %d ' % trial) not in s or ('event %d;' % n) not in s:
    s = s.rstrip('\n') + '\n' + ol.replace('- %s' % cutc, '- %s' % cutc[11:]) + ((' ' + note) if note else '') + '\n'; p.write_text(s); print('OPTIMIZATION_860_LOG appended')
else: print('OPTIMIZATION_860_LOG already has the line')
print(wl)
