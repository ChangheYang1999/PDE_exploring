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
from fields import Rat, ScaledRadial, TR, VR, T, V, SCALES, ar, field_hash

ROOT = Path(__file__).resolve().parents[3]
BASE = ROOT/'research/scaled_weak_backend'
sys.set_int_max_str_digits(0)


def module(name, path):
    spec = importlib.util.spec_from_file_location(name, path)
    out = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(out)
    return out


old = module('n4_previous_weak', ROOT/'research/successor_weak_probes/code/check.py')
moments = module('n4_rational_moments', ROOT/'research/rational_pole_moments/code/moments.py')
PROBES = old.PROBES


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


def construct(model, P, n):
    P = Rat(P)
    radial = (1-4*TR)*P+2*TR*VR*P.derivative()
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


def point_checks(model, P, n, fields):
    out = []
    for xs, ys in [('1/2', '1/2'), ('3', '4'), ('60', '80')]:
        x, y = ar(Q(xs)), ar(Q(ys))
        vals = model.evaluate(xs, ys)
        r2 = x*x+y*y
        r = r2.sqrt()
        v, t = 1/(1+r2), r2/(1+r2)
        z = acb(x/r, y/r)**n
        p = Rat(P).evaluate(t, v)
        radial = (1-4*t)*p+2*t*v*Rat(P.derivative()).evaluate(t, v)
        pr, pt = v*v*radial*z.imag, n*v*v*p*z.real
        px, py = x/r*pr-y/r*pt, y/r*pr+x/r*pt
        phi = r*v*v*p*z.imag
        expected = [(2*ar(model.c)+1)*phi+(ar(model.c)*x+vals['u1'])*px+
                    (ar(model.c)*y+vals['u2'])*py,
                    phi*vals['rho_x'], phi*vals['rho_y']]
        checks = [evaluate(f, model, x, y).overlaps(e) for f, e in zip(fields, expected)]
        assert all(checks), (xs, ys, checks)
        out.append({'x': xs, 'y': ys, 'M_Cx_Cy_overlap': checks})
    return out


def integrate_groups(groups, delta, offset, label):
    total, records = arb(0), []
    for index, (ell, A) in enumerate(sorted(groups.items())):
        tick = time.monotonic()
        b = offset+ell*delta/2
        assert b > -1
        factors = [(a, k) for a, k in zip(SCALES, A.powers) if k]
        value, info = moments.integral(b, V*A.numerator_v(), factors)
        assert value.rel_accuracy_bits() > 150 or not A
        total += value
        info.update({'ell': ell, 'numerator_degree': A.P.degree()+1,
                     'integral': value.str(90),
                     'elapsed_seconds': time.monotonic()-tick})
        records.append(info)
        print(label, index+1, '/', len(groups), 'ell', ell,
              'bits', value.rel_accuracy_bits(), 'seconds', info['elapsed_seconds'], flush=True)
    return arb.pi()/2*total, records


def energy(fields, model, label):
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
    value, records = integrate_groups(groups, model.delta, Q(1), label)
    assert value > 0 and value.rel_accuracy_bits() > 150
    return value, records, count, field_hash(groups)


def pairing_parts(model, Mfield):
    rho = {}
    for (j, n), A in model.rho.items():
        rho.setdefault(n, []).append((j+1, A.divide_t(2)))
    groups, count = {}, 0
    for (ell, kind, n), A in Mfield.items():
        assert kind == 's'
        for ell2, B in rho.get(n, []):
            add(groups, ell+ell2, A*B)
            count += 1
    answer, records = integrate_groups(groups, model.delta, Q(-1), 'Iparts')
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


def run(name, modes, bits):
    start = time.monotonic()
    ctx.prec = bits
    if name.startswith('C1-N1-010-'):
        src = ROOT/f'research/candidate_audits/data/{name}/d2w_j7_n4_X3bal_legqs_mid180_exact.json'
        audit_path = ROOT/f'research/generator_sector_audit/verification/{name}_direct.json'
        audit = json.loads(audit_path.read_text())
        assert digest(src) == audit['generator_sha256']
        assert audit['sector_summary']['all_forbidden_zero'] and audit['B0n_exact']
    else:
        src = ROOT/f'research/candidate_audits/data/{name}/canonical.json'
        audit_path = ROOT/f'research/candidate_audits/verification/{name}.json'
        audit = json.loads(audit_path.read_text())
        assert digest(src) == audit['canonical_sha256']
        assert audit['all_forbidden_zero'] and audit['snapshot_hashes_confirmed']
    model = ScaledRadial(src)
    calibration_points = {}
    if name.startswith('C1-N1-010-'):
        values = model.evaluate(*audit['point'])
        calibration_points = {key: values[key].overlaps(arb(value))
                              for key, value in audit['fields'].items() if key in values}
        assert len(calibration_points) == 6 and all(calibration_points.values())
    print('PREPARED', name, 'seconds', time.monotonic()-start, flush=True)
    for n in modes:
        tick = time.monotonic()
        dest = BASE/f'verification/{name}_n{n}.json'
        assert not dest.exists(), dest
        probe_rel, probe_sha, calibration_rel = PROBES[n]
        probe_path = ROOT/probe_rel
        assert digest(probe_path) == probe_sha
        frozen = json.loads(probe_path.read_text())
        assert Q(frozen['a']) == 0 and Q(frozen['C_U_exact']) == 1
        P = sum((Q(value)*T**int(k) for k, value in frozen['probe_coefficients'].items()), Poly([]))
        assert all(P[k] == 0 for k in range((n-1)//2))
        H = Q(frozen['H_upper_exact'])
        cover = old.helper.gradient_cover(P, n, H)
        fields = construct(model, P, n)
        exact_calibration = {}
        if name.startswith('C1-N1-007-'):
            oldmodel = old.Radial(src)
            oldfields = old.helper.construct(oldmodel, P, n)
            for i, (ours, theirs) in enumerate(zip(fields, oldfields)):
                exact_calibration[str(i)] = set(ours) == set(theirs) and all(
                    ours[k] == Rat(P0) for k, P0 in theirs.items())
            assert all(exact_calibration.values())
        print('FIELDS n', n, [len(f) for f in fields], 'seconds', time.monotonic()-tick, flush=True)
        points = point_checks(model, P, n, fields)
        Iparts, parts_records, parts_pairs, parts_hash = pairing_parts(model, fields[0])
        projection, projection_pairs = project(model, n)
        Idirect, direct_records = integrate_groups(
            {ell: A*P for ell, A in projection.items()}, model.delta, Q(-1), 'Idirect')
        assert min(Idirect.rel_accuracy_bits(), Iparts.rel_accuracy_bits()) > 150
        assert Idirect.overlaps(Iparts), (Idirect, Iparts)
        print('PAIRINGS AGREE', Idirect.str(24), 'seconds', time.monotonic()-tick, flush=True)
        M2, mrecords, mpairs, mhash = energy(fields[:1], model, 'M2')
        C2, crecords, cpairs, chash = energy(fields[1:], model, 'C2')
        M, C = M2.sqrt(), C2.sqrt()
        radius = 2*abs(Idirect)/(M+C+((M+C)**2+4*ar(H)*abs(Idirect)).sqrt())
        newton = abs(Idirect)/(M+C)
        floor, newton_floor = old.strict_floor(radius), old.strict_floor(newton)
        calibration = {}
        if name.startswith('C1-N1-007-'):
            previous = json.loads((ROOT/calibration_rel).read_text())
            calibration = {key: value.overlaps(arb(previous[key]))
                           for key, value in [('pairing', Idirect), ('M', M), ('C', C), ('radius', radius)]}
            assert all(calibration.values())
        paths = [src, audit_path, probe_path, Path(__file__), BASE/'PROOF.md', BASE/'code/fields.py',
                 ROOT/'research/rational_pole_moments/code/moments.py',
                 ROOT/'research/rational_pole_moments/PROOF.md',
                 ROOT/'research/angular_probe_audit/code/check.py',
                 ROOT/'research/optimized_probe_audit/code/check.py',
                 ROOT/'research/successor_weak_probes/code/check.py']
        if calibration:
            paths.append(ROOT/calibration_rel)
        out = {'utc': datetime.now(timezone.utc).isoformat(), 'candidate': name, 'angular_mode': n,
               'bits': ctx.prec, 'inputs': {str(p.relative_to(ROOT)): digest(p) for p in paths},
               'c_exact': str(model.c), 'candidate_field_counts': {k: len(f) for k, (f, _, _) in model.fields.items()},
               'candidate_field_sha256': {k: field_hash(f) for k, (f, _, _) in model.fields.items()},
               'independent_Cartesian_point_calibration': calibration_points,
               'point_checks': points, 'field_counts': [len(f) for f in fields],
               'field_sha256': [field_hash(f) for f in fields],
               'candidate007_field_calibration': exact_calibration,
               'pairing': Idirect.str(100), 'pairing_parts': Iparts.str(100), 'pairing_paths_overlap': True,
               'pairing_accuracy_bits': [Idirect.rel_accuracy_bits(), Iparts.rel_accuracy_bits()],
               'direct_moments': direct_records, 'parts_moments': parts_records,
               'projection_sha256': field_hash(projection), 'projection_pairs': projection_pairs,
               'parts_pair_count': parts_pairs, 'parts_sha256': parts_hash,
               'M': M.str(100), 'C': C.str(100), 'M2_moments': mrecords, 'C2_moments': crecords,
               'M_radial_pairs': mpairs, 'C_radial_pairs': cpairs, 'M_product_sha256': mhash, 'C_product_sha256': chash,
               'H_upper_exact': str(H), 'H_cover': cover, 'H_cover_tiles_unit_interval': True,
               'radius': radius.str(100), 'strict_lower_exact': str(floor),
               'newton_radius': newton.str(100), 'newton_strict_lower_exact': str(newton_floor),
               'strict_floors_verified': True, 'candidate007_calibration': calibration,
               'elapsed_seconds': time.monotonic()-tick, 'candidate_elapsed_seconds': time.monotonic()-start,
               'status': 'OPEN independent peer reproduction of scaled backend'}
        with dest.open('x') as f:
            json.dump(out, f, indent=2)
            f.write('\n')
        print('DONE', name, 'n', n, 'radius', radius.str(24), 'seconds', out['elapsed_seconds'], flush=True)


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('candidate', nargs='+')
    parser.add_argument('--modes', nargs='+', type=int, default=[7, 1])
    parser.add_argument('--bits', type=int, default=2048)
    args = parser.parse_args()
    assert args.bits >= 1024 and all(n in PROBES for n in args.modes)
    for name in args.candidate:
        run(name, args.modes, args.bits)
