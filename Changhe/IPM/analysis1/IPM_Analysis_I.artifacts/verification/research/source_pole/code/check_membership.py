"""Exact membership in the independently proved frozen-source parameter box."""
import json, hashlib
from pathlib import Path
from fractions import Fraction as Q
from datetime import datetime, timezone
base = Path(__file__).resolve().parents[1]
lane = base.parents[1]
p = lane/'research/modal_source/evidence/source_result.json'
expected = '51f283cd4ea7145f633e5449236cdd0bc2879b9ccf922d9fbadb6a609afa4691'
assert hashlib.sha256(p.read_bytes()).hexdigest() == expected
values = json.loads(p.read_text())['final_values']
rows = []
for name, key, shift, lo, hi in [('A','A_trial',Q(0),Q(10),Q(51,5)), ('mu','mu_minus_1',Q(1),Q(99,100),Q(101,100)), ('g','g',Q(0),Q(29),Q(30))]:
    left = Q(values[key]['lower_exact']) + shift
    right = Q(values[key]['upper_exact']) + shift
    assert lo <= left <= right <= hi
    rows.append(dict(parameter=name, lower_exact=str(left), upper_exact=str(right), box_lower=str(lo), box_upper=str(hi), verdict='CONTAINED'))
out = dict(utc=datetime.now(timezone.utc).isoformat(), status='PASS', scalar_result_sha256=expected, code_sha256=hashlib.sha256(Path(__file__).read_bytes()).hexdigest(), parameters=rows, scope='Membership of already independently confirmed modal-trial scalars. This is not a new scalar integration.')
(base/'evidence/membership.json').write_text(json.dumps(out,indent=2)+'\n')
print(json.dumps(out))
