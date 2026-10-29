#!/usr/bin/env python3
"""Read-only audit of a frozen primary figure snapshot and job provenance."""
from pathlib import Path
from datetime import datetime, timezone
import ast
import csv
import hashlib
import json
import time

LANE = Path(__file__).resolve().parents[1]
PRIMARY = LANE.parent / 'e4-num' / 'axisymmetric_euler_24h'
SNAPSHOT = Path((LANE / 'axisymmetric_euler_24h/results/latest_figure_audit.txt').read_text().strip())
NOW = datetime.now(timezone.utc)
OUT = LANE / 'report_audits' / ('primary_scope_' + NOW.strftime('%Y%m%dT%H%M%S.%fZ'))
OUT.mkdir()
START = time.perf_counter()
INPUTS, CHECKS = {}, []

def freeze(src, name):
    data = src.read_bytes()
    if data != src.read_bytes():
        raise RuntimeError('Mutable input changed: ' + str(src))
    dst = OUT / name
    dst.parent.mkdir(parents=True, exist_ok=True)
    dst.write_bytes(data)
    INPUTS[name] = {'source': str(src), 'sha256': hashlib.sha256(data).hexdigest(), 'bytes': len(data)}
    return data

def check(name, passed):
    CHECKS.append({'name': name, 'passed': bool(passed)})
    if not passed:
        raise AssertionError(name)

def readcsv(path):
    with path.open(newline='') as f:
        return list(csv.DictReader(f))

for name in ['FAILURE_MAP.csv', 'F1_residual_vs_resolution.csv', 'F5_cl_continuation.csv', 'F1_caption.txt', 'F5_caption.txt', 'figures_F1_F5.py', 'failure_map.py']:
    freeze(SNAPSHOT / name, name)
freeze(PRIMARY / 'scripts/class_counts.py', 'class_counts.py')
freeze(PRIMARY / 'docs/CLASS_COUNTS.md', 'CLASS_COUNTS.md')
freeze(PRIMARY / 'FAILURE_MAP.md', 'current_FAILURE_MAP.md')
rows = readcsv(OUT / 'FAILURE_MAP.csv')
byid = {r['job_id']: r for r in rows}
check('unique CSV job identities', len(byid) == len(rows))
meta = {}
for row in rows:
    jid = row['job_id']
    job = json.loads(freeze(PRIMARY / 'runs' / jid / 'job.json', 'jobs/' + jid + '.json'))
    check('job identity ' + jid, job['job_id'] == jid)
    cfg = job['cfg']
    shells = cfg.get('shells', [])
    radius = float(shells[-1][0]) if shells else float(cfg['R1'])
    name_radius = 20 if 'Rm20' in jid or 'rm20' in jid else (5 if jid.startswith('rm5') else 10)
    meta[jid] = {'R_outer': radius, 'name_inferred_radius': name_radius, 'D': cfg['D'], 'nmax': cfg['nmax'], 'shells': shells,
                 'q0_pin': cfg.get('q0_pin'), 's1_constraint': cfg.get('s1_constraint'), 'parent': job.get('parent'),
                 'from_state': job.get('from_state'), 'branch': job.get('branch'), 'tags': job.get('tags')}

# Confirm the exact source predicates before reconstructing them independently.
tree = ast.parse((OUT / 'failure_map.py').read_text())
functions = {n.name: n for n in tree.body if isinstance(n, ast.FunctionDef)}
stage_prefixes = ('lad2', 'lad3', 'lad4', 'chain', 'fmA', 'fmB', 'refl', 't1lad2_cl0p740', 't1seed', 'rm5')
extra_prefixes = ('fmC', 'fmD', 'fmE', 'fmF', 'fmap', 'freecl', 't1lad')
for fname, prefix in [('is_stage2', stage_prefixes), ('is_t1', extra_prefixes)]:
    tuples = [ast.literal_eval(n) for n in ast.walk(functions[fname]) if isinstance(n, ast.Tuple)]
    check('audited literal selector ' + fname, prefix in tuples)
class_tree = ast.parse((OUT / 'class_counts.py').read_text())
class_func = next(n for n in class_tree.body if isinstance(n, ast.FunctionDef) and n.name == 'cls')
class_tuples = [ast.literal_eval(n) for n in ast.walk(class_func) if isinstance(n, ast.Tuple)]
check('audited direct-seed class literal', ('t1seed', 'freecl_t1seed', 'freeclwide_t1seed', 'freeclmid_t1seed', 'fmD', 'fmE', 'fmF') in class_tuples)
check('audited continuation class literal', ('chain', 'fmA', 'fmB', 'fmC', 'fmap', 'lad2c07', 'lad3c07', 'freecl_fmC') in class_tuples)

pinned = lambda r: r['q0_pin'] not in ('', 'None', 'null')
kept = lambda r: float(r['s_core']) >= .05 and float(r['s_far']) >= .05
current = [r for r in rows if pinned(r) and r['job_id'].startswith(stage_prefixes + extra_prefixes)]
expanded = [r for r in rows if pinned(r) and r['job_id'].startswith(stage_prefixes + extra_prefixes + ('fmE', 'fmF', 'freeclwide'))]
omitted = [r for r in expanded if r not in current]
for r in omitted:
    check('omitted chain is source constrained ' + r['job_id'], meta[r['job_id']]['s1_constraint'] is True)
    check('omitted chain keeps q0 pin ' + r['job_id'], float(r['q0_pin']) == meta[r['job_id']]['q0_pin'])

f1, f5 = readcsv(OUT / 'F1_residual_vs_resolution.csv'), readcsv(OUT / 'F5_cl_continuation.csv')
plotted = []
for figure, plot in [('F1', f1), ('F5', f5)]:
    for r in plot:
        if not r['job_id']:
            continue
        m = meta[r['job_id']]
        plotted.append({'figure': figure, 'kind': r.get('kind'), 'job': r['job_id'], 'R_outer': m['R_outer']})
        if r.get('D'):
            check('basis degree ' + figure + ':' + r['job_id'], int(r['D']) == m['D'])
        if r.get('level'):
            check('angular degree ' + figure + ':' + r['job_id'], r['level'].startswith('D' + str(m['D']) + 'n' + str(m['nmax']) + 'K'))
        if r.get('kind') == 'floor_per_cl_level':
            eligible = [s for s in rows if kept(s) and meta[s['job_id']]['R_outer'] == 10 and int(r['D']) == meta[s['job_id']]['D'] and round(float(s['cl_final']), 4) == float(r['cl'])]
            check('floor with actual radius ' + r['job_id'], min(float(s['rho_max']) for s in eligible) == float(r['rho_max']))
series = {}
for r in f1:
    series.setdefault(r['series'], []).append(r)
sequence = []
for name, rr in series.items():
    rr = sorted(rr, key=lambda r: float(r['D']) if r['D'] else float(r['level'].split()[1]))
    ys = [float(r['rho_max']) for r in rr]
    sequence.append({'series': name, 'values': ys, 'all_steps_strictly_decrease': all(b < a for a, b in zip(ys, ys[1:])), 'jobs': [r['job_id'] for r in rr]})

result = {
    'started_utc': NOW.isoformat(), 'completed_utc': datetime.now(timezone.utc).isoformat(),
    'wall_seconds': time.perf_counter() - START, 'source_sha256': hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
    'figure_snapshot': str(SNAPSHOT), 'csv_rows': len(rows),
    'current_t1_count': len(current), 'current_t1_retaining': sum(map(kept, current)),
    'expanded_t1_count': len(expanded), 'expanded_t1_retaining': sum(map(kept, expanded)), 'omitted_t1_rows': omitted,
    'radius_name_mismatches': [{'job': j, **m} for j, m in meta.items() if m['R_outer'] != m['name_inferred_radius']],
    'plotted_non10_radius': [r for r in plotted if r['R_outer'] != 10], 'plotted_rows_with_jobs': len(plotted),
    'f1_sequences': sequence, 'metadata': meta, 'inputs': INPUTS, 'checks': CHECKS,
    'all_consistency_checks_pass': all(c['passed'] for c in CHECKS),
    'scope': 'Provenance and selection audit. No primary code execution or new PDE evaluation. The current expanded selector is explicit; no assertion that it exhausts future T1 naming conventions.'
}
(OUT / 'results.json').write_text(json.dumps(result, indent=2) + '\n')
(LANE / 'axisymmetric_euler_24h/results/latest_primary_scope_audit.txt').write_text(str(OUT) + '\n')
print(json.dumps({k: result[k] for k in ['completed_utc', 'wall_seconds', 'csv_rows', 'current_t1_count', 'current_t1_retaining', 'expanded_t1_count', 'expanded_t1_retaining', 'plotted_non10_radius', 'plotted_rows_with_jobs', 'all_consistency_checks_pass']}, indent=2))
print('omitted', [r['job_id'] for r in omitted], 'radius issues', [(r['job'], r['R_outer']) for r in result['radius_name_mismatches']])
print('checks', len(CHECKS), 'output', OUT)
