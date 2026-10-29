#!/usr/bin/env python3
"""Freeze and audit T1 report populations and continuation provenance.
Read-only primary inputs; no primary imports, tensor loading, or PDE execution.
"""
from pathlib import Path
import ast
import csv
import hashlib
import io
import json
from datetime import datetime, timezone

ROOT = Path(__file__).resolve().parents[1]
PRIMARY = ROOT.parent / 'e4-num' / 'axisymmetric_euler_24h'
LEAD = ROOT.parent / 'e4-lead'
OLD = ('lad2', 'lad3', 'lad4', 'chain', 'fmA', 'fmB', 'refl', 't1lad2_cl0p740', 't1seed', 'rm5')
EXPANDED = ('lad2', 'lad3', 'lad4', 'chain', 'fm', 'refl', 't1lad', 't1seed', 'rm5', 'freecl_')
now = datetime.now(timezone.utc)
OUT = ROOT / 'report_audits' / ('t1_population_' + now.strftime('%Y%m%dT%H%M%S.%fZ'))
OUT.mkdir(parents=True, exist_ok=False)
manifest, checks = {}, []

def freeze(src, target):
    data = src.read_bytes()
    assert src.read_bytes() == data, ('changed while reading', str(src))
    dst = OUT / target
    dst.parent.mkdir(parents=True, exist_ok=True)
    dst.write_bytes(data)
    manifest[target] = {'source': str(src), 'sha256': hashlib.sha256(data).hexdigest(), 'bytes': len(data)}
    return data

def check(name, condition):
    checks.append({'name': name, 'pass': bool(condition)})
    assert condition, name

def pinned(row):
    return row['q0_pin'] not in ('', 'None', 'null')

def keep(row):
    return float(row['s_core']) >= .05 and float(row['s_far']) >= .05

def table(pop):
    groups = {}
    for row in pop:
        groups.setdefault(round(float(row['cl_final']), 4), []).append(row)
    result = []
    for cl, group in sorted(groups.items()):
        ok = [r for r in group if keep(r) and r['rho_max'] not in ('', 'None')]
        best = min(ok, key=lambda r: float(r['rho_max'])) if ok else None
        result.append({'c_l': cl, 'runs': len(group), 'swirl_retaining': len(ok),
                       'best_rho_max': float(best['rho_max']) if best else None,
                       'best_job': best['job_id'] if best else None})
    return result

raw = freeze(PRIMARY / 'FAILURE_MAP.csv', 'FAILURE_MAP.csv')
rows = list(csv.DictReader(io.StringIO(raw.decode())))
source = freeze(PRIMARY / 'scripts/failure_map.py', 'primary_failure_map.py').decode()
freeze(PRIMARY / 'FAILURE_MAP.md', 'primary_FAILURE_MAP.md')
freeze(LEAD / 'FINAL_REPORT.md', 'lead_FINAL_REPORT.md')
func = next(n for n in ast.walk(ast.parse(source)) if isinstance(n, ast.FunctionDef) and n.name == 'is_stage2')
tuples = [ast.literal_eval(n) for n in ast.walk(func) if isinstance(n, ast.Tuple)]
check('source selector prefix tuple matches the audited OLD tuple', OLD in tuples)
check('unique completed job identifiers in frozen CSV', len({r['job_id'] for r in rows}) == len(rows))
old = [r for r in rows if pinned(r) and r['job_id'].startswith(OLD)]
expanded = [r for r in rows if pinned(r) and r['job_id'].startswith(EXPANDED)]
for r in expanded:
    check('magnitude filter matches saved B2 flag: ' + r['job_id'], keep(r) == (r['B2'] == 'True'))
omitted = [r for r in expanded if r not in old]

special = ['t1seed_cl0p74_q2p5', 't1seedC_cl0p74_q2p5', 't1seedL2_cl0p74_q2p5',
           't1seedCL2_cl0p74_q2p5', 'freecl_t1seedC_cl0p74',
           'lad2wide_t1lad2_cl0p740_q2p5_freecl_lm']
jobs = sorted(set(special + [r['job_id'] for r in omitted] +
                  [r['job_id'] for r in expanded if r['free_cl'] == 'True']))
records = {}
for job in jobs:
    src = PRIMARY / 'runs' / job / 'result.json'
    if not src.exists():
        continue
    d = json.loads(freeze(src, 'runs/' + job + '/result.json'))
    check('result job_id: ' + job, d['job_id'] == job)
    v = d['validation']
    records[job] = {'c_l': d['cl'], 'initial_c_l': d['cfg']['cl'],
                    'bounds': d['cfg'].get('cl_bounds'), 'free_cl': d['cfg']['free_cl'],
                    'q0_pin': d['cfg'].get('q0_pin'), 'D': d['cfg']['D'],
                    'rho_max': v['rho_max'], 's_core': v['s_core'], 's_far': v['s_far'],
                    'from_state': d.get('from_state'), 'finished': d['finished'],
                    'n_iter': d['n_iter'], 'tags': d.get('tags')}
    csvrow = next((r for r in rows if r['job_id'] == job), None)
    if csvrow:
        for key, got in [('cl_final', d['cl']), ('rho_max', v['rho_max']), ('s_core', v['s_core']), ('s_far', v['s_far'])]:
            check('CSV result scalar: ' + job + ':' + key, float(csvrow[key]) == got)

first = records['t1seed_cl0p74_q2p5']
continuation = records['t1seedC_cl0p74_q2p5']
level = records['t1seedL2_cl0p74_q2p5']
later_level = records['t1seedCL2_cl0p74_q2p5']
check('first D48 parent is the first D36 state', Path(level['from_state']).parent.name == 't1seed_cl0p74_q2p5')
check('continued D36 parent is the first D36 state', Path(continuation['from_state']).parent.name == 't1seed_cl0p74_q2p5')
check('later D48 parent is the continued D36 state', Path(later_level['from_state']).parent.name == 't1seedC_cl0p74_q2p5')
free = [dict(job=job, **r) for job, r in records.items() if r['free_cl']]
nonupper = [r for r in free if abs(r['c_l'] - r['bounds'][1]) > 1e-10]
result = {'recorded_utc': now.isoformat(), 'completed_utc': datetime.now(timezone.utc).isoformat(),
          'script_sha256': hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
          'csv_rows': len(rows), 'old_prefixes': OLD, 'expanded_prefixes': EXPANDED,
          'old_count': len(old), 'old_retaining': sum(map(keep, old)),
          'expanded_count': len(expanded), 'expanded_retaining': sum(map(keep, expanded)),
          'old_table': table(old), 'expanded_table': table(expanded),
          'omitted_rows': omitted, 'selected_records': records, 'free_nonupper': nonupper,
          'checks': checks, 'all_checks_pass': all(c['pass'] for c in checks), 'inputs': manifest,
          'scope': 'Source-provenance and population audit, not independent field or residual evaluation. The expanded prefix selector is explicit and is not claimed to exhaust every possible T1-related job.'}
(OUT / 'results.json').write_text(json.dumps(result, indent=2) + '\n')
(ROOT / 'axisymmetric_euler_24h/results/latest_t1_population_audit.txt').write_text(str(OUT) + '\n')
print(json.dumps({k: result[k] for k in ['csv_rows', 'old_count', 'old_retaining', 'expanded_count', 'expanded_retaining', 'all_checks_pass']}, indent=2))
print('checks', len(checks), 'out', OUT)
print('nonupper', [(r['job'], r['c_l']) for r in nonupper])
print('seed74', {k: records[k]['rho_max'] for k in special if k in records})
