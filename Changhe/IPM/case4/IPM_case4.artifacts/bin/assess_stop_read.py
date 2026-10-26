#!/usr/bin/env python3
"""Read-only reader for the spot-rule sections of an 860 cadence assessment record (SPEC v9.9 (b), v9.12 to v9.14): lists every node or point whose
stored ratio exceeds a threshold (default 1.0, the scientific-stop rule) with all stored fields, plus the worst ratios, the origin truncation monitor,
the completeness flags and the stop flags. Intended for the pre-registered diagnosis after a STOPPED_FOR_DIAGNOSIS marker (lead ruling 2026-10-25T13:06:30Z
item 3(c)): it only extracts what the record stores; it computes nothing new. Usage: assess_stop_read.py <assessment_record.json> [--threshold 1.0] [--top 10]"""
import json, sys, hashlib
from pathlib import Path
p = Path(sys.argv[1]); thr = float(sys.argv[sys.argv.index('--threshold')+1]) if '--threshold' in sys.argv else 1.0
top = int(sys.argv[sys.argv.index('--top')+1]) if '--top' in sys.argv else 10
d = json.loads(p.read_text()); print('record', p, 'sha256', hashlib.sha256(p.read_bytes()).hexdigest())
print('candidate', d.get('candidate_path'), d.get('candidate_sha256'), '| cl', d.get('cl'), 'a0', d.get('a0'), '| began', d.get('began_utc'), 'finished', d.get('finished_utc'))
print('flags: failed', d.get('failed'), 'scientific_stop', d.get('scientific_stop'), 'mode', d.get('mode'), 'sampled_only', d.get('sampled_only'))
om = d.get('origin_truncation_monitor') or {}; print('origin_truncation_monitor: worst_band_relative', om.get('worst_band_relative'), 'scientific_stop', om.get('scientific_stop'))
comp = d.get('completeness_v913') or {}; print('completeness_v913:', json.dumps({k: v for k, v in comp.items() if k != 'checks'})[:400]); print('  checks:', comp.get('checks'))
def show(rec, keys):
    for k in keys:
        if k in rec: print('      %s = %r' % (k, rec[k]))
rs = d.get('rf_reference_spot_check') or {}
print('\nrf_reference_spot_check: kappa', rs.get('kappa'), 'u', rs.get('u'), 'worst_ratio', rs.get('worst_ratio'), 'scientific_stop', rs.get('scientific_stop'), 'configurations', rs.get('configurations'), 'points', len(rs.get('points') or []))
pts = rs.get('points') or []
def worst(pt):
    return max([v for k, v in pt.items() if k.startswith('ratio_') and isinstance(v, (int, float))] or [float('nan')])
bad = [pt for pt in pts if worst(pt) > thr]
print('  points above %.3g: %d' % (thr, len(bad)))
for pt in sorted(pts, key=worst, reverse=True)[:max(len(bad), min(top, 3))]:
    print('    point', pt.get('point'), 'worst ratio %r' % worst(pt)); show(pt, ['x', 'y', 'r', 'Rf_decimal_85'] + sorted(k for k in pt if k.startswith(('Rf_', 'S_R_', 'abs_error_', 'bound_', 'ratio_')) and k != 'Rf_decimal_85'))
sp = d.get('rf_spot_nodes_v912_v914') or {}
print('\nrf_spot_nodes_v912_v914: worst_ratio_random', sp.get('worst_ratio_random'), 'worst_ratio_targeted', sp.get('worst_ratio_targeted'), 'scientific_stop', sp.get('scientific_stop'), 'nodes', len(sp.get('nodes') or []), 'random_failures', sp.get('random_failures'), 'limit_on_failing_fraction_95pct', sp.get('limit_on_failing_fraction_95pct'))
print('  arrays_source:', json.dumps(sp.get('arrays_source'))[:300]); print('  targeted:', sp.get('targeted')); print('  seed:', sp.get('seed'))
nodes = sp.get('nodes') or []
badn = [nd for nd in nodes if (nd.get('ratio_worst') if nd.get('ratio_worst') is not None else worst(nd)) > thr]
print('  nodes above %.3g: %d' % (thr, len(badn)))
for nd in sorted(nodes, key=lambda nd: (nd.get('ratio_worst') if nd.get('ratio_worst') is not None else worst(nd)), reverse=True)[:max(len(badn), min(top, 3))]:
    print('    node index', nd.get('index'), 'band', nd.get('band'), 'kinds', nd.get('kinds'), 'ratio_worst %r' % nd.get('ratio_worst')); show(nd, ['x', 'y', 'r', 'Rf_decimal_85'] + sorted(k for k in nd if k.startswith(('Rf_', 'S_R_', 'abs_error_', 'bound_', 'ratio_')) and k not in ('Rf_decimal_85', 'ratio_worst')))
print('\nPre-registered diagnosis (lead 13:06:30Z item 3(c)), to be done by the lead/verifier with exact arithmetic at the run\'s coordinates of each failing node: (1) is RN(R_f) a preimage of the stored h under the recorded weighting, with ratio <= 1; (2) does the stateless ratio pass. This reader does not perform it.')
