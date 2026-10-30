"""Compare the exact radial Green split against the frozen N1 diagnostic."""
from pathlib import Path
from datetime import datetime, timezone
from fractions import Fraction
from hashlib import sha256
import ast
import json
import time
from flint import arb, ctx

ROOT = Path(__file__).resolve().parents[3]
BASE = ROOT/'research/negative_norm_split'

def digest(path):
    return sha256(path.read_bytes()).hexdigest()

def exact_float(value):
    q = Fraction(value)
    return arb(q.numerator)/q.denominator

start = time.monotonic()
ctx.prec = 512
path = BASE/'verification/d2_R8356.474846731926_2048.json'
log = ROOT/'research/negative_norm_tail_audit/source/N1_d2_v4.out'
prior = ROOT/'research/whole_plane_norms/verification/d2_Hminus1_ball_2048.json'
data = json.loads(path.read_text())
old = ast.literal_eval(next(line for line in log.read_text().splitlines() if line.startswith("{'inner':")))
exact = {key: arb(value) for key, value in data['squared_norm_contributions'].items()}
assert (exact['inner']+exact['cross']+exact['outer']).overlaps(exact['full'])
assert exact['full'].sqrt().overlaps(arb(json.loads(prior.read_text())['norm_ball']))
corrected = {key: exact_float(old[key])*(2 if key == 'outer' else 1) for key in ['inner','cross','outer']}
errors = {key: corrected[key]-exact[key] for key in corrected}
total_error = sum(errors.values(), arb(0))
assert total_error > 0
corrected_full = sum(corrected.values(), arb(0))
assert (corrected_full-exact['full']).overlaps(total_error)
result = {
    'utc': datetime.now(timezone.utc).isoformat(timespec='seconds'),
    'exact_split_sha256': digest(path), 'frozen_log_sha256': digest(log),
    'prior_full_norm_sha256': digest(prior), 'code_sha256': digest(Path(__file__)),
    'precision_bits': ctx.prec, 'radius_exact': data['radius_exact'],
    'logged_values_interpreted_as': 'Exact binary64 values represented by the Python log literals.',
    'exact_squared_norm_contributions': data['squared_norm_contributions'],
    'logged_minus_exact_after_outer_factor_repair': {key: value.str(70) for key,value in errors.items()},
    'total_squared_norm_error': total_error.str(70),
    'relative_squared_norm_errors': {key: (errors[key]/exact[key]).str(50) for key in errors},
    'fraction_total_error_from_inner': (errors['inner']/total_error).str(50),
    'corrected_H': corrected_full.sqrt().str(70),
    'corrected_H_minus_exact': (corrected_full.sqrt()-exact['full'].sqrt()).str(60),
    'elapsed_seconds': time.monotonic()-start,
    'scope': 'Error localization for one frozen diagnostic and one radius. No bound for other meshes or candidates, and no separation of interpolation, field roundoff and quadrature error inside the inner contribution.',
}
dest = BASE/'verification/N1_v4_comparison.json'
assert not dest.exists()
dest.write_text(json.dumps(result,indent=2)+'\n')
for key,value in errors.items(): print(key,'error',value.str(22))
print('H error',result['corrected_H_minus_exact'])
print('inner share',result['fraction_total_error_from_inner'])
