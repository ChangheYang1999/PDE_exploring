#!/usr/bin/env python3
"""Copy the far-field monitor row of one accepted state from outputs/dev_v9/farfield_states/TABLE.md into
RESULTS_860.md section 5a (table row after the previous state, "Computed ..." header extension, observation sentence)
and into the NUM_REPORT.md FAR-FIELD MONITOR bullet. Checks the two monotone claims (exponent decreasing since state 51,
E1 fraction falling since state 61) and refuses to write the sentence pattern if either fails (prints a warning instead).
Usage: farfield_apply.py <state-number> [--results FILE] [--numreport FILE] [--dry-run]"""
_artifact_root = str(next(p for p in __import__("pathlib").Path(__file__).resolve().parents if (p / "work" / "research860").is_dir() and (p / "outputs").is_dir()))
import sys, re, datetime
from pathlib import Path
LANE = Path((_artifact_root))
n = int(sys.argv[1])
results = Path(sys.argv[sys.argv.index('--results')+1]) if '--results' in sys.argv else LANE/'RESULTS_860.md'
numrep = Path(sys.argv[sys.argv.index('--numreport')+1]) if '--numreport' in sys.argv else LANE/'NUM_REPORT.md'
dry = '--dry-run' in sys.argv
table = (LANE/'outputs/dev_v9/farfield_states/TABLE.md').read_text().split('\n')
def row_of(k):
    key = f'| accepted_{k:08d} |'
    r = [l for l in table if l.startswith(key)]
    if len(r) != 1: sys.exit(f'TABLE.md: {len(r)} rows for state {k}')
    return r[0]
row, prev = row_of(n), row_of(n-1)
def parse(r):
    c = [x.strip() for x in r.strip('|').split('|')]
    return dict(state=c[0], J=float(c[1]), cl=float(c[2]), a0=float(c[3]), ex=float(c[4]), growth=c[5],
                E1=float(c[6]), E1p=float(c[7]), E2=float(c[8]), E2p=float(c[9]), E3=float(c[10]), E3p=float(c[11]))
d, dp = parse(row), parse(prev)
if d['growth'] != 'grows': sys.exit('growth flag is not "grows": inspect by hand')
frac = 100*d['E1p']/d['E1']; fracp = 100*dp['E1p']/dp['E1']
warn = []
if not d['ex'] < dp['ex']: warn.append(f'exponent did not decrease ({dp["ex"]} -> {d["ex"]})')
if not frac < fracp: warn.append(f'E1 fraction did not fall ({fracp:.3f} -> {frac:.3f} percent)')
# guard run id: newest farfield run dir whose running/result mentions this snapshot
runs = sorted((LANE/'outputs/dev_sessions/20261026_farfield/runs').glob('*_farfield'))
run_id = None
for rd in reversed(runs):
    txt = ''.join(p.read_text() for p in rd.glob('*.json') if p.is_file())
    if f'accepted_{n:08d}.json' in txt: run_id = rd.name; break
if run_id is None: sys.exit('no farfield guard run mentions this snapshot')
hhmm = datetime.datetime.strptime(run_id[:16], '%Y%m%dT%H%M%SZ').strftime('%H:%M') + 'Z'
sent = (f' State {n} ({hhmm}, after the cut): exponent {d["ex"]:.7f}, E1 {d["E1"]:.5f} with part above 19 {d["E1p"]:.6f} '
        f'({frac:.3f} percent), E2 part {d["E2p"]:.5f} ({100*d["E2p"]/d["E2"]:.3f} percent), E3 part {d["E3p"]:.4f} ({100*d["E3p"]/d["E3"]:.3f} percent).')
# RESULTS_860
R = results.read_text().split('\n')
idx = [i for i,l in enumerate(R) if l.startswith(f'| accepted_{n-1:08d} |')]
if len(idx) != 1: sys.exit(f'RESULTS: {len(idx)} rows for state {n-1}')
if any(l.startswith(f'| accepted_{n:08d} |') for l in R): sys.exit('RESULTS already has this state')
R.insert(idx[0]+1, row)
hdr = [i for i,l in enumerate(R) if l.startswith('Computed 2026-10-25T08:11Z')]
if len(hdr) != 1: sys.exit('RESULTS: Computed header not unique')
R[hdr[0]] = R[hdr[0]].rstrip() + f' {hhmm} (state {n}; guard run {run_id})'
obs = [i for i,l in enumerate(R) if l.startswith('Observation 14:10Z') and f'State {n-1} (' in l]
if len(obs) != 1: sys.exit('RESULTS: observation line not found')
tailtxt = ' Measured trends on the finite basis; no mechanism claimed.'
if not R[obs[0]].endswith(tailtxt): sys.exit('RESULTS: observation line tail changed')
R[obs[0]] = R[obs[0]][:-len(tailtxt)] + sent + tailtxt
# NUM_REPORT bullet
N = numrep.read_text().split('\n')
b = [i for i,l in enumerate(N) if l.startswith('- FAR-FIELD MONITOR per accepted state')]
if len(b) != 1: sys.exit('NUM_REPORT: bullet not unique')
L = N[b[0]]
subs = [
 (rf'seed -> state {n-1} \(states 31 to {n-1} added 13:12Z to 2026-10-26T\d\d:\d\dZ\)', f'seed -> state {n} (states 31 to {n} added 13:12Z to 2026-10-26T{hhmm})'),
 (rf'-> {dp["ex"]:.7f} \(state {n-1}; positive', f'-> {d["ex"]:.7f} (state {n}; positive'),
 (rf'slight decreases at states 51 to {n-1}\)', f'slight decreases at states 51 to {n})'),
 (rf'E1 L2 0\.44035 -> {dp["E1"]:.5f}, E2 6\.3631 -> {dp["E2"]:.4f}, E3 31\.721 -> {dp["E3"]:.3f}', f'E1 L2 0.44035 -> {d["E1"]:.5f}, E2 6.3631 -> {d["E2"]:.4f}, E3 31.721 -> {d["E3"]:.3f}'),
 (rf'-> {dp["E1p"]:.6f} \(state {n-1}; the fraction', f'-> {d["E1p"]:.6f} (state {n}; the fraction'),
 (rf'{fracp:.3f} percent at state {n-1}\)', f'{frac:.3f} percent at state {n})'),
 (rf'E2 0\.00184 -> 0\.04515 -> {dp["E2p"]:.4f}, E3 0\.00397 -> 0\.2527 -> {dp["E3p"]:.3f}', f'E2 0.00184 -> 0.04515 -> {d["E2p"]:.4f}, E3 0.00397 -> 0.2527 -> {d["E3p"]:.3f}'),
]
for pat, rep in subs:
    L2, k = re.subn(pat, rep, L)
    if k != 1: sys.exit(f'NUM_REPORT: pattern matched {k} times: {pat}')
    L = L2
N[b[0]] = L
if warn:
    print('WARNING (monotone claim fails; nothing written):'); [print(' ', w) for w in warn]; sys.exit(2)
if dry:
    print('DRY RUN'); print(row); print(sent); print(L); sys.exit(0)
results.write_text('\n'.join(R)); numrep.write_text('\n'.join(N))
print(f'RESULTS_860 and NUM_REPORT updated for state {n} (guard run {run_id}, {hhmm})'); print(sent.strip())
