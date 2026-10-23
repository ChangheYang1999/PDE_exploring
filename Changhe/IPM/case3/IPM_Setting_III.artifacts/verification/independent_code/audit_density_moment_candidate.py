"""Independent source-primitive check of the saved N32 coefficient vector."""
from pathlib import Path
from datetime import datetime, timezone
from fractions import Fraction
import argparse
import hashlib
import json
import time
import numpy as np
import mpmath as mp
from smooth_basis import SmoothBasis
from smooth_mp_primitives import SmoothMP, rational
from smooth_density_moment_inverse import DensityMomentInverse

ap = argparse.ArgumentParser()
ap.add_argument('--input', default='evidence/smooth_exact_jets/common1000_cl2.5_N32M28/exact_input.json')
ap.add_argument('--radii', nargs='+', default=['.03', '3', '300', '3000'])
ap.add_argument('--digits', type=int, default=80)
ap.add_argument('--orders', nargs='+', type=int, default=[72, 108, 162])
args = ap.parse_args()
start = time.monotonic()
data = json.loads(Path(args.input).read_text())
model = SmoothMP(data, args.digits)
basis = SmoothBasis(model.N, model.M, float(model.p), float(model.L))
co = np.array([[float(v) for v in row] for row in model.coeff]).reshape(-1)
root = Path('research/smooth_density_moment_inverse/verification')
out = root / ('CANDIDATE_N%d_M%d_d%d.json' % (model.N, model.M, args.digits))
result = dict(started_utc=datetime.now(timezone.utc).isoformat(), arguments=vars(args),
              input_sha256=hashlib.sha256(Path(args.input).read_bytes()).hexdigest(),
              source_sha256=hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
              inverse_sha256=hashlib.sha256(Path('independent_code/smooth_density_moment_inverse.py').read_bytes()).hexdigest(),
              status='RUNNING', rows=[])
for rs in args.radii:
    r = float(rs)
    theta = .37
    x, y = float(r*np.cos(theta)), float(r*np.sin(theta))
    # Decimal coordinates are passed identically to the independent MP model.
    ref = model.fields(repr(x), repr(y))
    reference = np.array([float(ref[k]) for k in ['psi', 'U1', 'U2']])
    v, gx, gy = basis.evaluate([x], [y], True)
    rho, rx, ry = (float(z[0] @ co) for z in [v, gx, gy])
    row = dict(radius=rs, x=repr(x), y=repr(y), source_primitive=ref,
               density_errors={k: abs(z-float(ref[k]))/max(1., abs(float(ref[k])))
                               for k, z in zip(['rho', 'rho_x', 'rho_y'], [rho, rx, ry])},
               orders=[])
    for order in args.orders:
        inv = DensityMomentInverse(basis, order, composite=True)
        matrices = inv.stream_velocity_at_radius(r, [theta])
        got = np.array([matrix[0] @ co for matrix in matrices])
        scaled = np.array([r*r, r, r])
        err = float(np.max(abs((got-reference)/scaled))/max(1., np.max(abs(reference/scaled))))
        tx = (float(model.ell)*x+got[1])*rx
        ty = (float(model.ell)*y+got[2])*ry
        R = tx+ty-rho
        nf = abs(tx)+abs(ty)+abs(rho)
        nv = abs(rho)+abs(x*rx+y*ry)+abs(got[1]*rx+got[2]*ry)
        row['orders'].append(dict(order=order, scaled_inverse_error=err,
                                  psi=float(got[0]), U1=float(got[1]), U2=float(got[2]),
                                  rho=rho, rho_x=rx, rho_y=ry, R=R, Nf=nf, Nv=nv,
                                  R_Nf=abs(R)/nf, R_Nv=abs(R)/nv,
                                  normalized_R_error=abs(R-float(ref['R']))/float(ref['Nf'])))
    result['rows'].append(row)
    result['updated_utc'] = datetime.now(timezone.utc).isoformat()
    out.write_text(json.dumps(result, indent=2)+'\n')
result['max_finest_inverse_error'] = max(row['orders'][-1]['scaled_inverse_error'] for row in result['rows'])
result['max_finest_normalized_R_error'] = max(row['orders'][-1]['normalized_R_error'] for row in result['rows'])
result['status'] = 'PASS' if result['max_finest_inverse_error'] < 1e-10 and result['max_finest_normalized_R_error'] < 1e-10 else 'FAIL'
result['elapsed_seconds'] = time.monotonic()-start
result['scope'] = 'Finite comparisons at supplied points and precisions, without interval enclosure or optimizer run.'
out.write_text(json.dumps(result, indent=2)+'\n')
print(json.dumps({k: result[k] for k in ['updated_utc', 'status', 'elapsed_seconds', 'max_finest_inverse_error', 'max_finest_normalized_R_error']}))
if result['status'] != 'PASS':
    raise ArithmeticError('Candidate inverse comparison failed')
