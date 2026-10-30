"""Small scalar audit; candidate field intervals are previously peer-certified."""
from pathlib import Path
from fractions import Fraction as Q
from datetime import datetime, timezone
import hashlib
import json
import time
from flint import arb, ctx

root = Path(__file__).resolve().parents[3]
topic = root / 'research/theory_v03_audit'
started = datetime.now(timezone.utc).isoformat()
t0 = time.perf_counter()
ctx.prec = 512
source = root / 'research/optimized_probe_007/verification/n7_a0.json'
raw = source.read_bytes()
assert hashlib.sha256(raw).hexdigest() == '2a268c62e9e45096d2b745679a49adeee0cb9a3da532a06e4b89faaffdb3ef1f'
j = json.loads(raw)
inputs = {k: j[k] for k in ['pairing', 'M', 'C']}
I, M, C = (arb(str(inputs[k])) for k in ['pairing', 'M', 'C'])
D = M + C
assert I > 0 and D > 0
radius = arb(47694) / 10000000
I0 = arb(17647) / 1000000000
checks = {'newton_bound': bool(I / D > radius),
          'heldout_left_endpoint': bool(I > I0),
          'heldout_right_endpoint': bool(I - D * radius > 0)}
A = m = B = Q(1)
mu = Q(3)
linear = mu - A*m - B
emax = (linear*linear - 4*A*B*m)/(4*A)
checks['defect_counterexample'] = linear > 0 and emax == Q(-3,4)
gamma = Q(2251799813685248,4076476460239181)
max_tail_power = 4*gamma-5
checks['tail_kernel_is_L2'] = max_tail_power < -1
assert all(checks.values()), checks
result = {
    'started_utc': started,
    'finished_utc': datetime.now(timezone.utc).isoformat(),
    'elapsed_seconds': time.perf_counter()-t0,
    'precision_bits': ctx.prec,
    'source_sha256': hashlib.sha256(raw).hexdigest(),
    'proof_sha256': hashlib.sha256((topic/'PROOF.md').read_bytes()).hexdigest(),
    'theory_v03_sha256': hashlib.sha256((topic/'source/theory_v03.md').read_bytes()).hexdigest(),
    'inputs': inputs,
    'I_over_D': str(I/D),
    'I_minus_I0': str(I-I0),
    'I_minus_D_radius': str(I-D*radius),
    'radius_rational': '23847/5000000',
    'I0_rational': '17647/1000000000',
    'defect_counterexample': {'A': '1','m': '1','B': '1','mu': '3','epsilon_max': str(emax)},
    'max_tail_density_power': str(max_tail_power),
    'checks': checks,
}
(topic/'verification/result.json').write_text(json.dumps(result, indent=2)+'\n')
print(json.dumps({k:result[k] for k in ['elapsed_seconds','I_over_D','I_minus_D_radius','checks']},indent=2))
