"""Exact conversion of a frozen Legendre representation, without producer code."""
from collections import defaultdict
from datetime import datetime, timezone
from hashlib import sha256
from math import comb
from pathlib import Path
import argparse, json, time
from flint import fmpq as Q

ROOT = Path(__file__).resolve().parents[3]
BASE = ROOT / 'research/legendre_exact_bridge'
C = Q(4076476460239181, 2251799813685248)
CHECKS = 0

def need(value, text=''):
    global CHECKS
    assert value, text
    CHECKS += 1

def stamp():
    return datetime.now(timezone.utc).strftime('%Y-%m-%dT%H:%M:%SZ')

def local(text):
    p = Path(text)
    need(not p.is_absolute() and '..' not in p.parts)
    return ROOT / p

def digest(path):
    return sha256(Path(path).read_bytes()).hexdigest()

def rational(value):
    need(type(value) is str)
    return Q(value)

def signature(row):
    n, h, d = (row[k] for k in ('n', 'h', 'd'))
    need(all(type(v) is int for v in (n, h, d)))
    need(n > 0 and n % 2 and h >= 0 and d >= 0)
    b, t = rational(row['b_exact']), rational(row['scale_exact'])
    need(t > 0 and n+2*h+2*b-2*d <= 4/C-3)
    return n, h, b, t, d

def polynomial_recurrence(maximum):
    polynomials = [[Q(1)], [Q(-1), Q(2)]]
    for k in range(1, maximum):
        current, previous = polynomials[-1], polynomials[-2]
        result = [Q(0)] * (k+2)
        for j, a in enumerate(current):
            result[j] -= (2*k+1)*a/(k+1)
            result[j+1] += 2*(2*k+1)*a/(k+1)
        for j, a in enumerate(previous):
            result[j] -= k*a/(k+1)
        polynomials.append(result)
    return polynomials

def elementary_ab(entries):
    A, B = Q(0), Q(0)
    for (n, h, b, t, d), a in entries.items():
        if n == 1 and h == 0:
            A += a*t**(-d)*(b-Q(d)/t)
        elif n == 1 and h == 1:
            A += a*t**(-d)
        elif n == 3 and h == 0:
            B += a*t**(-d)
    return A, B

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('--request', required=True)
    parser.add_argument('--tag', required=True)
    args = parser.parse_args()
    need(args.tag and all(c.isalnum() or c in '_-' for c in args.tag))
    folder = BASE/'verification'/args.tag
    folder.mkdir(exist_ok=False)
    started, tick = stamp(), time.monotonic()
    request_path = local(args.request)
    request = json.loads(request_path.read_text())
    item = request['inputs']['phi']
    original_path = local(item['path'])
    need(digest(original_path) == item['sha256'])
    document = json.loads(original_path.read_text())
    need(document['schema_version'] == 'ipm-potential-correction-v1')
    need(rational(document['c_exact']) == C)
    need(document['n_atoms_nonzero'] == len(document['atoms']))
    degrees = [row.get('legendre_degree', 0) for row in document['atoms']]
    need(all(type(k) is int and k >= 0 for k in degrees))
    polynomials = polynomial_recurrence(max(degrees))
    for k in set(degrees):
        expected = [Q((-1)**(k+j)*comb(k, j)*comb(k+j, j))
                    for j in range(k+1)]
        need(polynomials[k] == expected, 'Rodrigues versus recurrence')
        need(sum(expected, Q(0)) == 1, 'endpoint one')
        need(expected[0] == (-1)**k, 'endpoint zero')
        if k:
            need(expected[1] == (-1)**(k+1)*k*(k+1), 'endpoint derivative')
    merged, recurrence_merged = defaultdict(Q), defaultdict(Q)
    raw_leading, expanded_leading = defaultdict(Q), defaultdict(Q)
    A, B = Q(0), Q(0)
    mu, e = 4/C-3, 4/C-5
    signatures = set()
    expanded_terms = 0
    for row, k in zip(document['atoms'], degrees):
        n, h, b, t, d = key = signature(row)
        a = rational(row['coefficient_exact'])
        need(a != 0 and (*key, k) not in signatures)
        signatures.add((*key, k))
        tau = n+2*h+2*b-2*d
        need(rational(row['tau_exact']) == tau)
        for j in range(k+1):
            el = (n, h+j, b, t, d+j)
            merged[el] += a*(-1)**(k+j)*comb(k, j)*comb(k+j, j)
            recurrence_merged[el] += a*polynomials[k][j]
            expanded_terms += 1
        if n == 1 and h == 0:
            A += a*t**(-d)*(-1)**k*(b-Q(d+k*(k+1))/t)
        elif n == 1 and h == 1:
            A += a*t**(-d)*(-1)**k
        elif n == 3 and h == 0:
            B += a*t**(-d)*(-1)**k
        if tau == mu:
            raw_leading[n] += (C*e-1)*a*(n*n-mu*mu)
    merged = {k: v for k, v in merged.items() if v}
    recurrence_merged = {k: v for k, v in recurrence_merged.items() if v}
    need(merged == recurrence_merged)
    exported = {}
    for row in document['atoms_elementary']:
        key = signature(row)
        need(key not in exported)
        a = rational(row['coefficient_exact'])
        need(a != 0)
        exported[key] = a
    need(document['n_atoms_elementary'] == len(exported))
    need(merged == exported, 'complete exported elementary map')
    need(elementary_ab(merged) == (A, B), 'origin through two representations')
    for (n, h, b, t, d), a in merged.items():
        if n+2*h+2*b-2*d == mu:
            expanded_leading[n] += (C*e-1)*a*(n*n-mu*mu)
    for n in set(raw_leading) | set(expanded_leading):
        need(raw_leading[n] == expanded_leading[n])
    producer = {int(n): rational(v) for n, v in
                document['sector_e_correction']['added_sine_coefficients'].items()}
    for n in set(raw_leading) | set(producer):
        need(raw_leading[n] == producer.get(n, Q(0)))
    meta = document['exact_identities']
    base_slope = rational(document['center']['a0_base_exact'])
    for name, value in [('A_cubic', A), ('B_cubic', B), ('A_plus_3B', A+3*B),
                        ('ell_h_phi', 2*A+6*B),
                        ('origin_density_slope_h_phi', -8*A),
                        ('a_star_exact', base_slope-8*A)]:
        need(rational(meta[name]) == value, name)
    canonical = {k: v for k, v in document.items()
                 if k not in ('atoms', 'atoms_elementary', 'legendre_convention',
                              'n_atoms_elementary', 'n_atoms_nonzero', 'n_atoms_total')}
    canonical['atoms'] = [
        dict(coefficient_exact=str(a), n=n, h=h, b_exact=str(b),
             scale_exact=str(t), d=d, tau_exact=str(n+2*h+2*b-2*d))
        for (n, h, b, t, d), a in sorted(merged.items())
    ]
    canonical['n_atoms_nonzero'] = canonical['n_atoms_total'] = len(merged)
    record_path = folder/'result.json'
    canonical['equivalent_representation'] = dict(
        original_path=item['path'], original_sha256=item['sha256'],
        conversion_record=str(record_path.relative_to(ROOT)),
        scope='Exact identity of potentials and all derivatives; no refitting.')
    canonical_path = folder/'canonical_elementary.json'
    with canonical_path.open('x') as stream:
        json.dump(canonical, stream, indent=2)
        stream.write('\n')
    derived = json.loads(json.dumps(request))
    derived['created_utc'] = stamp()
    derived['inputs']['phi'] = {
        'path': str(canonical_path.relative_to(ROOT)), 'sha256': digest(canonical_path)}
    derived['proof_dependencies'] += [
        'research/legendre_exact_bridge/PROOF.md',
        str(record_path.relative_to(ROOT))]
    derived_path = folder/'structural_request.json'
    out = dict(
        started_utc=started, finished_utc=stamp(),
        elapsed_seconds=time.monotonic()-tick, checks=CHECKS, passed=True,
        code_sha256=digest(__file__),
        proof_sha256=digest(BASE/'PROOF.md'),
        request=args.request, request_sha256=digest(request_path),
        input=item['path'], input_sha256=item['sha256'],
        raw_atom_count=len(document['atoms']), maximum_legendre_degree=max(degrees),
        expanded_terms_before_merging=expanded_terms,
        elementary_atom_count=len(merged),
        canonical_path=str(canonical_path.relative_to(ROOT)),
        canonical_sha256=digest(canonical_path),
        A_exact=str(A), B_exact=str(B), origin_normalized=A+3*B == 0,
        producer_elementary_identity=True, independent_recurrence_identity=True,
        leading_metadata_identity=True,
        scope='Equivalent exact representation and finite identities. Norms and background OPEN.')
    with record_path.open('x') as stream:
        json.dump(out, stream, indent=2)
        stream.write('\n')
    with derived_path.open('x') as stream:
        json.dump(derived, stream, indent=2)
        stream.write('\n')
    print(out['finished_utc'], 'checks', CHECKS, 'seconds', out['elapsed_seconds'],
          'canonical atoms', len(merged), flush=True)

if __name__ == '__main__':
    main()
