#!/usr/bin/env python3
"""Append the g2_v4-and-supplements result tables to EMBEDDING_TESTS.md from the step JSONs (numbers read from the records; nothing recomputed).
Usage: embedding_tables_v2.py [--write]  (without --write, prints the markdown)"""
_artifact_root = str(next(p for p in __import__("pathlib").Path(__file__).resolve().parents if (p / "work" / "research860").is_dir() and (p / "outputs").is_dir()))
import json, sys, time
from pathlib import Path
LANE = Path((_artifact_root)); G2 = LANE/'outputs/g2'
def load(tag, step):
    p = G2/tag/(step+'.json'); return json.loads(p.read_text()) if p.exists() else None
def fmt(v): return ('%.3e' % v) if isinstance(v, float) else str(v)
md = ['', '## G2 evidence under frozen manifests g2_v4 (base) and supplements (appended %s by bin/embedding_tables_v2.py)' % time.strftime('%Y-%m-%dT%H:%M:%SZ', time.gmtime()), '',
      'Verdict rule (SPEC v9.6 item 4): a step passes only if the runner verdict is ok, the step JSON passed field is true and no check record failed. The per-step table with sha256 values is outputs/g2/G2_SUMMARY.md. Numbers below are copied from the step JSONs.', '']
# t0t1v2
d = load('g2_v5', 't0t1v2')
if d:
    md += ['### T0/T1 (g2_v5 t0t1v2, SPEC v9.6/v9.8): passed = %s, %d checks' % (d['passed'], len(d['checks'])), '', '| check | value | tolerance |', '|---|---|---|']
    for c in d['checks']:
        if any(k in c['check'] for k in ('T0.2', 'T0.3', 'T0.4', 'T0.5_low', 'T1.8', 'T1.1', 'T1.2', 'T1.3', 'T1.5', 'T1.6', 'T1.7')): md.append('| %s | %s | %s |' % (c['check'], fmt(c['value']), fmt(c['tolerance']) if c['tolerance'] is not None else 'boolean'))
    md.append('')
# t2
d = load('g2_v4', 't2')
if d: md += ['### T2.1 to T2.4 fields and c_l derivatives at four c_l values (g2_v4 t2): passed = %s, %d checks; worst check value / tolerance = %s' % (d['passed'], len(d['checks']), fmt(max((c['value']/c['tolerance'] for c in d['checks'] if isinstance(c['value'], float) and c['tolerance']), default=0.))), '']
# t26
d = load('g2_v4', 't26')
if d:
    md += ['### T2.6b/c/d/x residual and complete columns, three shapes (g2_v4 t26): passed = %s, %d checks' % (d['passed'], len(d['checks'])), '', '| band | R_f ratio (single/batch/stateless) | columns ratio (single/batch/stateless) |', '|---|---|---|']
    vals = {c['check']: c['value'] for c in d['checks']}
    for b in ('origin', 'b1', 'b2', 'b3', 'b4', 'b5'):
        rf = [vals.get('T2.6c_%s_Rf_%s' % (b, sh)) for sh in ('single', 'batch', 'stateless')]; co = [vals.get('T2.6c_%s_all_raw_columns_%s' % (b, sh)) for sh in ('single', 'batch', 'stateless')]
        md.append('| %s | %s | %s |' % (b, ' / '.join(fmt(v) for v in rf), ' / '.join(fmt(v) for v in co)))
    for pt in ('e24', 'e32', 'e44', 'rmax_training', 'rmax_refined'):
        rf = [vals.get('T2.6b_%s_Rf_%s' % (pt, sh)) for sh in ('single', 'batch', 'stateless')]; co = [vals.get('T2.6b_%s_all_raw_columns_%s' % (pt, sh)) for sh in ('single', 'batch', 'stateless')]
        md.append('| %s | %s | %s |' % (pt, ' / '.join(fmt(v) for v in rf), ' / '.join(fmt(v) for v in co)))
    md += ['', 'T2.6d: largest configuration difference of R_f %s; training-sized call %s; T2.6x (c_l = 2, 3, 2(1+2^-20), 3(1-2^-20)) worst R_f %s, worst columns %s.' % (fmt(d.get('T2.6d_largest_configuration_difference_Rf')), json.dumps(d.get('T2.6d_training_sized_call')), fmt(max(c['value'] for c in d['checks'] if c['check'].startswith('T2.6x') and c['check'].endswith('_Rf'))), fmt(max(c['value'] for c in d['checks'] if c['check'].startswith('T2.6x') and c['check'].endswith('columns')))), '']
# t27h, t27hx, t27hx2, t27hfloor
for tag, step, key in (('g2_v4', 't27h', 'T2.7H'), ('g2_v4', 't27hx', 'T2.7H-X'), ('g2_v6', 't27hx2', 'T2.7H-X2'), ('g2_v7', 't27hfloor', 'T2.7H_floor')):
    d = load(tag, step)
    if not d: continue
    md += ['### %s (%s %s): passed = %s, %d checks' % (key, tag, step, d['passed'], len(d['checks'])), '', '| c_l | worst field ratio | worst c_l-derivative ratio | floor cases |', '|---|---|---|---|']
    for lab, s_ in d[key].items(): md.append('| %s | %s | %s | %s |' % (lab.replace('cl=', ''), fmt(s_['worst_field_ratio']), fmt(s_['worst_dcl_ratio']), s_.get('floor_cases_count')))
    md.append('')
# t3
d = load('g2_v4', 't3')
if d:
    md += ['### T3/T4.1/T5 seed reproduction (g2_v4 t3): passed = %s, %d checks' % (d['passed'], len(d['checks'])), '', '| check | value | tolerance |', '|---|---|---|']
    for c in d['checks']: md.append('| %s | %s | %s |' % (c['check'], fmt(c['value']), fmt(c['tolerance']) if c['tolerance'] is not None else 'boolean'))
    md += ['', 'Timings (s): %s' % json.dumps({k: round(v) for k, v in d.get('timings', {}).items()}), 'Replay reference: %s (sha256 %s).' % (d.get('replay_reference_file'), (d.get('replay_reference_sha256') or '')[:16]), '']
# kappa, supplement2 (when present)
for tag, step, title in (('g2_v10', 'kappa', 'SPEC v9.7 rounding calibration (g2_v10 kappa)'), ('g2_v11', 'supplement2', 'Supplement v2 (g2_v11 supplement2)')):
    d = load(tag, step)
    if d:
        md += ['### %s: passed = %s, %d checks' % (title, d['passed'], len(d['checks'])), '']
        if step == 'kappa': md += ['rho_max = %s at %s; kappa = %s; coverage %s.' % (fmt(d.get('rho_max')), json.dumps(d.get('rho_argmax')), d.get('kappa'), json.dumps(d.get('coverage'), default=str)[:600]), '']
        else: md += ['| check | value | tolerance |', '|---|---|---|']+['| %s | %s | %s |' % (c['check'], fmt(c['value']), fmt(c['tolerance']) if c['tolerance'] is not None else 'boolean') for c in d['checks']]+['']
text = '\n'.join(md)+'\n'
if '--write' in sys.argv: (LANE/'EMBEDDING_TESTS.md').open('a').write(text); print('appended %d lines to EMBEDDING_TESTS.md' % len(md))
else: print(text)
