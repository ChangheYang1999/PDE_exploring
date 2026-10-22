"""Analytic manufactured checks independent of the Green construction."""
import os
for name in ('OMP_NUM_THREADS', 'OPENBLAS_NUM_THREADS', 'MKL_NUM_THREADS', 'NUMEXPR_NUM_THREADS'):
    os.environ[name] = '1'
os.environ['PYTHONDONTWRITEBYTECODE'] = '1'
import datetime, hashlib, json, resource, time
from fractions import Fraction
from pathlib import Path
from flint import arb, ctx
from certified_eval import LocalInverse, rational, store
resource.setrlimit(resource.RLIMIT_AS, (2 * 1024**3, 2 * 1024**3))
resource.setrlimit(resource.RLIMIT_CPU, (150, 155))
ctx.prec = 768
ctx.threads = 1
HERE = Path(__file__).resolve().parent


def manufacture(C):
    p = [0] * (len(C) + 8)
    for i, c in enumerate(C):
        for j, v in ((0, 1), (4, -2), (8, 1)):
            p[i + j] += 4 * c * v
    q = [4 * c for c in C]
    moment = sum((Fraction(c, j - 7) for j, c in enumerate(p) if j != 7), Fraction())
    return {'beta': 2, 'M': 1, 'N': len(C), 'denominator': 1,
            'A': [[0, 0, 1]], 'C': [C],
            'modes': [{'k': 1, 'L': 7, 'J': 1, 'P': p, 'Q': q,
                       'moment': [moment.numerator, moment.denominator]}]}


def rational_reference(x, y):
    s = x*x + y*y
    d = 1 + s
    hxx = -6*x*y/d**2 + 8*x**3*y/d**3
    hyy = -6*x*y/d**2 + 8*x*y**3/d**3
    hxy = 1/d - 2*s/d**2 + 8*x*x*y*y/d**3
    return {'Psi': x*y/d, 'U1': -x/d + 2*x*y*y/d**2,
            'U2': y/d - 2*x*x*y/d**2, 'Psi_xx': hxx, 'Psi_xy': hxy,
            'Psi_yy': hyy, 'Omega': 12*x*y/d**2 - 8*x*y*s/d**3,
            'Theta': x*x*y/d**2, 'Theta_x': 2*x*y/d**2-4*x**3*y/d**3,
            'Theta_y': x*x/d**2-4*x*x*y*y/d**3}


def log_reference(x, y):
    s = x*x + y*y
    r = s.sqrt()
    I = (s - 2*(1+s).log() - 1/(1+s) + 1)/4
    O = 1 / (4 * (1+s))
    h = (I/s + s*O)/4
    hp = (-I/r**3 + r*O)/2
    sin2, cos2 = 2*x*y/s, (x*x-y*y)/s
    ur = -2*h*cos2/r
    up = hp*sin2
    return {'Psi': h*sin2, 'U1': (x*ur-y*up)/r, 'U2': (y*ur+x*up)/r,
            'Omega': x*y/(1+s)**2}

start = time.process_time()
record = {'started_utc': datetime.datetime.now(datetime.timezone.utc).isoformat(),
          'precision_bits': ctx.prec, 'tests': [], 'limitations': 'Manufactured checks validate implementation identities; arithmetic soundness relies on Arb.'}
for name, C, reference in [('rational_stream', [0,0,0,4,0,0,0,8], rational_reference),
                           ('logarithmic_inverse', [0,0,0,1], log_reference)]:
    comp = manufacture(C)
    inv = LocalInverse(comp, 3, 4)
    for x0, y0 in [('1', '.5'), ('1.4', '.2'), ('.25', '.3')]:
        x, y = arb(x0), arb(y0)
        observed = inv.evaluate(x, y)
        expected = reference(x,y)
        overlap = {k: observed[k].overlaps(v) for k,v in expected.items()}
        sharp = {k: observed[k].rad() < arb('1e-60') for k in expected}
        if not (all(overlap.values()) and all(sharp.values())):
            print(name,x0,y0,overlap,sharp, {k: str(observed[k]) for k in expected},flush=True)
        assert all(overlap.values()) and all(sharp.values())
        assert observed['elliptic_identity_interval'].contains(0)
        box = inv.evaluate(x+arb(0,arb('1e-4')), y+arb(0,arb('1e-4')))
        corner_gates = []
        for sx in (-1, 1):
            for sy in (-1, 1):
                vals = reference(x+sx*arb('1e-4'), y+sy*arb('1e-4'))
                corner_gates.extend(box[k].contains(v) for k,v in vals.items())
        assert all(corner_gates)
        record['tests'].append({'case': name, 'x': x0, 'y': y0,
            'overlap': overlap, 'sharp_under_1e_minus60': sharp,
            'box_corner_containment': all(corner_gates),
            'nonzero_log_coefficient': comp['modes'][0]['P'][7] != 0,
            'elliptic_interval_contains_zero': True})
record['completed_utc'] = datetime.datetime.now(datetime.timezone.utc).isoformat()
record['cpu_seconds'] = time.process_time()-start
record['all_pass'] = True
record['source_sha256'] = hashlib.sha256((HERE/'certified_eval.py').read_bytes()).hexdigest()
(HERE/'verification/manufactured.json').write_text(json.dumps(record, indent=2)+'\n')
print(json.dumps(record, indent=2))
