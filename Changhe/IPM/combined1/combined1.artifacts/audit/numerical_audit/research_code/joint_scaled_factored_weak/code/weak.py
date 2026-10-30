"""Complete whole-plane weak tests for exact mixed radial scales."""
from pathlib import Path
from datetime import datetime, timezone
from hashlib import sha256
import argparse
import importlib.util
import json
import sys
import time
from flint import fmpq as Q, fmpq_poly as Poly, arb, acb, ctx
from fields_joint import Rat, ScaledRadial, TR, VR, T, V, SCALES, ar, field_hash

ROOT = Path(__file__).resolve().parents[3]
BASE = ROOT/'research/joint_scaled_factored_weak'
sys.set_int_max_str_digits(0)


def module(name, path):
    spec = importlib.util.spec_from_file_location(name, path)
    out = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(out)
    return out


moments = module('n4_factored_rational_moments', ROOT/'research/factored_pole_moments/code/moments.py')


def digest(path):
    h = sha256()
    with Path(path).open('rb') as f:
        for block in iter(lambda: f.read(1 << 20), b''):
            h.update(block)
    return h.hexdigest()


def add(out, key, value):
    if value:
        out[key] = out.get(key, Rat()) + value


def put(out, ell, kind, n, value):
    if kind == 's' and n == 0:
        return
    if n < 0:
        n, value = -n, (-value if kind == 's' else value)
    add(out, (ell, kind, n), value)


def construct(model, n, K):
    assert n >= 1 and n%2 and K >= (n-1)//2
    P = Rat(1)
    radial = (2*K+1)-(2*K+4)*TR
    px = [(n+1, (radial-n*P)/2), (n-1, (radial+n*P)/2)]
    py = [(n-1, (radial+n*P)/2), (n+1, (n*P-radial)/2)]
    M, Cx, Cy = {}, {}, {}
    put(M, 0, 's', n, (2*model.c+1)*P+model.c*radial)
    for (j, l), A in model.u1.items():
        for freq, W in px:
            G = A.divide_t(2)*W/2
            put(M, j+1, 's', freq+l, G)
            put(M, j+1, 's', freq-l, G)
    for (j, l), A in model.u2.items():
        for freq, W in py:
            G = A.divide_t(2)*W/2
            put(M, j+1, 's', l+freq, G)
            put(M, j+1, 's', l-freq, G)
    for (j, l), A in model.rx.items():
        G = A.divide_t(2)*P/2
        put(Cx, j+1, 'c', n-l, G)
        put(Cx, j+1, 'c', n+l, -G)
    for (j, l), A in model.ry.items():
        G = A.divide_t(2)*P/2
        put(Cy, j+1, 's', n+l, G)
        put(Cy, j+1, 's', n-l, G)
    return [{k: A for k, A in f.items() if A} for f in [M, Cx, Cy]]


def evaluate(field, model, x, y):
    r2 = x*x+y*y
    r = r2.sqrt()
    v, t = 1/(1+r2), r2/(1+r2)
    z = acb(x/r, y/r)
    powers = [acb(1)]
    for i in range(max(k[2] for k in field)):
        powers.append(powers[-1]*z)
    return r*v*v*sum((v**ar(ell*model.delta/2)*A.evaluate(t, v)*
                    (powers[n].imag if kind == 's' else powers[n].real)
                    for (ell, kind, n), A in field.items()), arb(0))


def point_checks(model, n, K, fields):
    out = []
    for xs, ys in [('1/2', '1/2'), ('3', '4'), ('60', '80')]:
        x, y = ar(Q(xs)), ar(Q(ys))
        vals = model.evaluate(xs, ys)
        r2 = x*x+y*y
        r = r2.sqrt()
        v, t = 1/(1+r2), r2/(1+r2)
        z = acb(x/r, y/r)**n
        factor = t**K
        radial = (2*K+1)-(2*K+4)*t
        pr, pt = v*v*factor*radial*z.imag, n*v*v*factor*z.real
        px, py = x/r*pr-y/r*pt, y/r*pr+x/r*pt
        phi = r*v*v*factor*z.imag
        expected = [(2*ar(model.c)+1)*phi+(ar(model.c)*x+vals['u1'])*px+
                    (ar(model.c)*y+vals['u2'])*py,
                    phi*vals['rho_x'], phi*vals['rho_y']]
        checks = [(factor*evaluate(f, model, x, y)).overlaps(e)
                  for f, e in zip(fields, expected, strict=True)]
        assert all(checks), (xs, ys, checks)
        out.append({'x': xs, 'y': ys, 'M_Cx_Cy_overlap': checks})
    return out

def integrate_groups(groups, delta, offset, localization, label):
    total, records = arb(0), []
    for index, (ell, A) in enumerate(sorted(groups.items())):
        tick = time.monotonic()
        b = offset+ell*delta/2
        assert b > -1
        factors = [(a, k) for a, k in zip(SCALES, A.powers) if k]
        value, info = moments.integral(b, localization, A.numerator_v(), factors)
        assert value.rel_accuracy_bits() > 150 or not A
        total += value
        info.update({'ell': ell, 'numerator_degree': A.P.degree(),
                     'integral': value.str(90),
                     'elapsed_seconds': time.monotonic()-tick})
        records.append(info)
        print(label, index+1, '/', len(groups), 'ell', ell,
              'bits', value.rel_accuracy_bits(), 'seconds', info['elapsed_seconds'], flush=True)
    return arb.pi()/2*total, records


def energy(fields, model, K, label):
    groups, count = {}, 0
    for field in fields:
        angular = {}
        for (ell, kind, n), A in field.items():
            assert n > 0 and n%2 == 1
            angular.setdefault((kind, n), []).append((ell, A))
        for terms in angular.values():
            for i, (ell, A) in enumerate(terms):
                for j in range(i+1):
                    ell2, B = terms[j]
                    add(groups, ell+ell2, A*B*(1 if i == j else 2))
                    count += 1
    print(label, 'assembled', len(groups), 'groups', count, 'pairs', flush=True)
    value, records = integrate_groups(groups, model.delta, Q(1), 2*K+1, label)
    assert value > 0 and value.rel_accuracy_bits() > 150
    return value, records, count, field_hash(groups)


def pairing_parts(model, Mfield, K):
    rho = {}
    for (j, n), A in model.rho.items():
        rho.setdefault(n, []).append((j+1, A.divide_t(2)))
    groups, count = {}, 0
    for (ell, kind, n), A in Mfield.items():
        assert kind == 's'
        for ell2, B in rho.get(n, []):
            add(groups, ell+ell2, A*B)
            count += 1
    answer, records = integrate_groups(groups, model.delta, Q(-1), K+1, 'Iparts')
    return -answer, records, count, field_hash(groups)


def project(model, target):
    result = {}
    for (j, n), A in model.rho.items():
        if n == target:
            TA = TR*A.derivative()
            L = model.c*(2*TA-3*A+2*TR*(model.p[j]*A-TA))-A
            add(result, j+1, L.divide_t(2))
    quadratic, counts = {}, []
    for C, S in [(model.u1, model.rx), (model.ry, model.u2)]:
        count = 0
        for (i, n), A in C.items():
            for (j, m), B in S.items():
                twice = int(m+n == target)+int(m-n == target)-int(m-n == -target)
                if twice:
                    add(quadratic, i+j+2, A*B*Q(twice, 2))
                    count += 1
        counts.append(count)
    for ell, A in quadratic.items():
        add(result, ell, A.divide_t(4))
    return {k: A for k, A in result.items() if A}, counts

