"""Merge exact radial coverage for the audited middle-circle certificate."""
from pathlib import Path
from datetime import datetime, timezone
from flint import arb, ctx
from certify_far_circles import upper_decimal
import argparse, hashlib, json
ctx.prec = 192
ROOT = Path(__file__).resolve().parents[1]

def main():
    p = argparse.ArgumentParser()
    p.add_argument('chunks', nargs='+')
    p.add_argument('--out', required=True)
    a = p.parse_args()
    data = [json.loads((ROOT/name).read_text()) for name in a.chunks]
    assert data
    data.sort(key=lambda z: z['row_start'])
    first = data[0]
    nr = first['radial_cells']; m = first['phase_intervals']
    index = 0
    for obj in data:
        for key in ['precision_bits','angles_per_half','radial_cells','phase_intervals','integer_unit','plan_trials','source_hashes']:
            assert obj[key] == first[key], key
        assert obj['row_start'] == index
        assert obj['row_stop'] > index
        index = obj['row_stop']
        assert [r['alpha'] for r in obj['rows']] == [r['alpha'] for r in first['rows']]
        for r in obj['rows']:
            assert len(r['middle_phase_intervals']) == len(r['residual_intervals']) == m+1
    assert index == nr
    for name, digest in first['source_hashes'].items():
        assert hashlib.sha256((ROOT/name).read_bytes()).hexdigest() == digest, name
    rows = []
    for k, r in enumerate(first['rows']):
        values = [sum((arb(obj['rows'][k]['middle_phase_intervals'][j]) for obj in data),arb(0)) for j in range(m+1)]
        residuals = [sum((arb(obj['rows'][k]['residual_intervals'][j]) for obj in data),arb(0)) for j in range(m+1)]
        assert all(v.is_finite() and v >= 0 for v in values)
        rows.append(dict(alpha=r['alpha'],middle_phase_intervals=[v.str(40,more=True) for v in values],safe_middle_upper=[upper_decimal(v) for v in values],residual_intervals=[v.str(36,more=True) for v in residuals]))
    result = dict(time_utc=datetime.now(timezone.utc).isoformat(),precision_bits=ctx.prec,angles_per_half=first['angles_per_half'],radial_cells=nr,phase_intervals=m,integer_unit=first['integer_unit'],plan_trials=first['plan_trials'],rows=rows,input_hashes={name:hashlib.sha256((ROOT/name).read_bytes()).hexdigest() for name in a.chunks},source_hashes=first['source_hashes'],merger_sha256=hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),status='Full middle-region bound with exact radial coverage and common source hashes checked. Requires other regions and phase interpolation.')
    (ROOT/a.out).write_text(json.dumps(result,indent=2)+'\n')
    for r in rows:
        print(r['alpha'], r['safe_middle_upper'])
if __name__ == '__main__':
    main()
