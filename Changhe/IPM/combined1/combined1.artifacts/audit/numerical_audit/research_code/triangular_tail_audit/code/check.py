"""Cartesian polynomial endpoints and exact complex Laurent convolutions."""
from pathlib import Path
from datetime import datetime, timezone
from hashlib import sha256
import json
import sys
import time
from flint import fmpq as Q

ROOT = Path(__file__).resolve().parents[3]
BASE = ROOT / 'research/triangular_tail_audit'
sys.path.insert(0, str(ROOT/'research/radial_fourier/code'))
from radial import Radial
sys.set_int_max_str_digits(0)
ZERO = (Q(0), Q(0))
H = lambda p: sha256(Path(p).read_bytes()).hexdigest()


def add(*terms):
    out = {}
    for term in terms:
        for n, (a, b) in term.items():
            x, y = out.get(n, ZERO)
            out[n] = (x+a, y+b)
    return {n: z for n, z in out.items() if z != ZERO}


def scale(term, q):
    return {n: (a*q, b*q) for n, (a, b) in term.items() if q and (a or b)}


def multiply(left, right):
    out = {}
    for n, (a, b) in left.items():
        for m, (c, d) in right.items():
            x, y = out.get(n+m, ZERO)
            out[n+m] = (x+a*c-b*d, y+a*d+b*c)
    return {n: z for n, z in out.items() if z != ZERO}


def derivative(term):
    return {n: (-n*b, n*a) for n, (a, b) in term.items() if n and (a or b)}


def endpoint(field, branch, kind):
    out = {}
    for (j, n), P in field.items():
        if j != branch:
            continue
        a = P(Q(1))
        if not a:
            continue
        if n == 0:
            assert kind == 'c'
            out = add(out, {0: (a, Q(0))})
        elif kind == 'c':
            out = add(out, {n: (a/2, Q(0)), -n: (a/2, Q(0))})
        else:
            out = add(out, {n: (Q(0), -a/2), -n: (Q(0), a/2)})
    return out


def sine_map(term):
    assert 0 not in term
    result = {}
    for n, (a, b) in term.items():
        assert n%2 in (0, 1) and a == 0
        assert term[-n] == (a, -b)
        if n > 0:
            result[str(n)] = str(-2*b)
    return dict(sorted(result.items(), key=lambda x: int(x[0])))


def emit(term):
    return {str(n): [str(a), str(b)] for n, (a, b) in sorted(term.items())}


def main():
    start = time.monotonic()
    src = ROOT/'research/candidate_audits/data/C1-N1-007-d2w-j7-e2bal/canonical.json'
    candidate_audit = ROOT/'research/candidate_audits/verification/C1-N1-007-d2w-j7-e2bal.json'
    prior = json.loads(candidate_audit.read_text())
    manifest = json.loads((BASE/'source/MANIFEST.json').read_text())
    for name, item in manifest['files'].items():
        assert H(BASE/'source'/name) == item['sha256']
    peer = json.loads((BASE/'source/T4_result.json').read_text())
    profiles = json.loads((BASE/'source/T4_exact_profiles.json').read_text())
    assert H(src) == prior['canonical_sha256'] == peer['source_sha256']
    assert H(BASE/'source/T4_PROOF.md') == peer['proof_sha256']
    assert H(BASE/'source/T4_check.py') == peer['code_sha256']
    assert H(BASE/'source/T4_exact_profiles.json') == peer['exact_profiles_sha256']
    model = Radial(src)
    assert model.state['source_sha256'] == prior['generator_sha256']
    c, gamma, delta = model.c, model.g, model.delta
    assert Q(1, 2) < gamma < Q(3, 5) and (2/delta).floor() == 4
    exponents = {j: gamma-j*delta for j in range(5)}
    assert exponents[3] > -1 > exponents[4]
    cosine = {1: (Q(1, 2), Q(0)), -1: (Q(1, 2), Q(0))}
    sine = {1: (Q(0), Q(-1, 2)), -1: (Q(0), Q(1, 2))}
    fields = {}
    rows = []
    for j in range(4):
        e = exponents[j]
        rho = endpoint(model.rho, j, 's')
        psi = endpoint(model.deriv(1, 1), j, 's')
        u1, u2 = endpoint(model.u1, j, 'c'), endpoint(model.u2, j, 's')
        rx, ry = endpoint(model.rx, j, 's'), endpoint(model.ry, j, 'c')
        radial = add(multiply(cosine, u1), multiply(sine, u2))
        angular = add(scale(multiply(sine, u1), -1), multiply(cosine, u2))
        assert radial == scale(derivative(psi), -1)
        assert angular == scale(psi, e+1)
        assert rx == add(scale(multiply(cosine, rho), e), scale(multiply(sine, derivative(rho)), -1))
        assert ry == add(scale(multiply(sine, rho), e), multiply(cosine, derivative(rho)))
        lap = {n: (a*((e+1)**2-n*n), b*((e+1)**2-n*n)) for n, (a, b) in psi.items()}
        lap = {n: z for n, z in lap.items() if z != ZERO}
        assert lap == scale(rx, -1)
        own_rho, own_psi = sine_map(rho), sine_map(psi)
        assert all(int(n)%2 == 1 for n in own_rho)
        assert all(int(n)%2 == 0 for n in own_psi)
        assert own_rho == profiles['density_profiles'][str(j)]
        assert own_psi == profiles['stream_profiles'][str(j)]
        fields[j] = dict(rho=rho, psi=psi, u1=u1, u2=u2, rx=rx, ry=ry, radial=radial, angular=angular)
        rows.append({'branch': j, 'e': str(e), 'poisson_exact': True,
                     'Cartesian_polar_velocity_exact': True, 'Cartesian_polar_gradient_exact': True,
                     'full_peer_density_equal': True, 'full_peer_stream_equal': True,
                     'density_modes': len(own_rho), 'stream_modes': len(own_psi)})
    recurrence = []
    for j in range(1, 4):
        direct, polar = {}, {}
        for ell in range(j):
            m = j-1-ell
            a, b = fields[ell], fields[m]
            direct = add(direct, multiply(a['u1'], b['rx']), multiply(a['u2'], b['ry']))
            polar = add(polar, scale(multiply(a['radial'], b['rho']), exponents[m]),
                        multiply(a['angular'], derivative(b['rho'])))
        assert direct == polar
        residual = add(direct, scale(fields[j]['rho'], -j*(c-1)))
        assert not residual
        frequencies = sorted(n for n in set(direct)|set(fields[j]['rho']) if n > 0)
        assert frequencies == list(range(1, 20*(j+1), 2))
        predicted = sine_map(scale(direct, 1/(j*(c-1))))
        assert predicted == profiles['predicted_density_profiles'][str(j)]
        recurrence.append({'branch': j, 'coefficients_checked': len(frequencies),
                           'maximum_frequency': max(frequencies), 'Cartesian_polar_products_equal': True,
                           'all_coefficients_exact_zero': True, 'full_peer_prediction_equal': True})
    assert sum(row['coefficients_checked'] for row in recurrence) == 90
    own_profiles = {'c': str(c), 'gamma': str(gamma), 'exponents': {str(j): str(e) for j, e in exponents.items()},
                    'density_profiles': {str(j): sine_map(f['rho']) for j, f in fields.items()},
                    'stream_profiles': {str(j): sine_map(f['psi']) for j, f in fields.items()},
                    'Cartesian_endpoint_profiles': {str(j): {k: emit(v) for k, v in f.items() if k in ['u1', 'u2', 'rx', 'ry']} for j, f in fields.items()}}
    dest = BASE/'verification/exact_profiles.json'
    with dest.open('x') as f:
        json.dump(own_profiles, f, indent=2)
        f.write('\n')
    inputs = [src, candidate_audit, BASE/'source/MANIFEST.json', BASE/'source/T4_result.json',
              BASE/'source/T4_exact_profiles.json', BASE/'PROOF.md', Path(__file__),
              ROOT/'research/radial_fourier/code/radial.py']
    out = {'utc': datetime.now(timezone.utc).isoformat(), 'candidate': 'C1-N1-007-d2w-j7-e2bal',
           'method': 'full Cartesian derivative polynomial endpoints and exact complex Laurent convolutions',
           'source_sha256': H(src), 'raw_source_sha256': prior['generator_sha256'],
           'inputs': {str(p.relative_to(ROOT)): H(p) for p in inputs},
           'branch_checks': rows, 'triangular_checks': recurrence, 'all_90_exact_zero': True,
           'exact_profiles_sha256': H(dest), 'elapsed_seconds': time.monotonic()-start,
           'verdict': 'CONFIRMED independent numerical reproduction of T4-235; T4-234 theorem review separate'}
    with (BASE/'verification/result.json').open('x') as f:
        json.dump(out, f, indent=2)
        f.write('\n')
    print(json.dumps(out, indent=2), flush=True)


if __name__ == '__main__':
    main()
