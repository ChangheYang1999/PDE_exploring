"""Exact polar Laplacian; complete outward polynomial integration."""
from datetime import datetime, timezone
from hashlib import sha256
from pathlib import Path
import argparse
import json
import sys
import time
from flint import arb, arb_poly, fmpq as Q, fmpq_poly as Poly, ctx

sys.set_int_max_str_digits(0)
ROOT = Path(__file__).resolve().parents[3]
BASE = ROOT / 'research/candidate007_laplacian_fast'
SLOW = ROOT / 'research/candidate007_weighted_laplacian'
NAME = 'C1-N1-007-d2w-j7-e2bal'
sys.path.insert(0, str(ROOT / 'research/whole_plane_norms/code'))
from pipeline import load, source
from norms import ar, T, U


def digest(path):
    h = sha256()
    with Path(path).open('rb') as stream:
        for block in iter(lambda: stream.read(1 << 20), b''):
            h.update(block)
    return h.hexdigest()


def now():
    return datetime.now(timezone.utc).isoformat()


def write_new(path, content):
    with path.open('x') as stream:
        json.dump(content, stream, indent=2)
        stream.write('\n')


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('--seconds', type=float, default=430)
    parser.add_argument('--max-modes', type=int, default=10000)
    args = parser.parse_args()
    start = time.monotonic()
    ctx.prec = 2048
    src = source(NAME)
    assert digest(src) == '153c1adc6f48b28ab34c8e4aa670dcfdcb7c6faae8c13490a942e9a2319fa316'
    cache = ROOT / f'research/whole_plane_norms/data/{NAME}_D0.json.gz'
    assembly = ROOT / f'research/whole_plane_norms/verification/{NAME}_assembly.json'
    assembled = json.loads(assembly.read_text())
    assert assembled['source_sha256'] == digest(src)
    assert assembled['polynomial_sha256'] == digest(cache)
    raw = json.loads(src.read_text())
    c = Q(raw['cl'])
    delta = 1 - 1/c
    weights = sorted(set([Q(k, 5) for k in range(5)] + [Q(k, 4) for k in range(7)] + [1 + 1/c]))
    F = load(NAME, 0)[0, 0]
    assert all(kind == 's' and n > 0 for ell, kind, n in F)
    modes = sorted({n for ell, kind, n in F})
    paths = [src, cache, assembly, Path(__file__), BASE / 'PROOF.md',
             ROOT / 'research/whole_plane_norms/code/pipeline.py',
             ROOT / 'research/whole_plane_norms/code/norms.py',
             ROOT / 'research/radial_fourier/code/radial.py']
    manifest = {'candidate': NAME, 'precision_bits': ctx.prec, 'c': str(c),
                'weights': [str(a) for a in weights], 'modes': modes,
                'components': len(F), 'inputs': {str(p.relative_to(ROOT)): digest(p) for p in paths}}
    manifest_path = BASE / 'verification/manifest.json'
    if manifest_path.exists():
        assert json.loads(manifest_path.read_text()) == manifest
    else:
        write_new(manifest_path, manifest)
    mh = digest(manifest_path)
    print('loaded', len(F), 'components', len(modes), 'modes', time.monotonic()-start, flush=True)
    completed = {}
    fresh = 0
    unit_minus = arb_poly([1, -1])
    for n in modes:
        output = BASE / f'verification/modes/mode_{n:03d}.json'
        if output.exists():
            record = json.loads(output.read_text())
            assert record['manifest_sha256'] == mh and record['mode'] == n
            assert [row['a'] for row in record['weights']] == manifest['weights']
            completed[n] = record
            continue
        if time.monotonic()-start >= args.seconds or fresh >= args.max_modes:
            continue
        ms = time.monotonic()
        terms = []
        endpoints = []
        for (ell, kind, frequency), P in sorted(F.items()):
            if frequency != n:
                continue
            d = ell*delta/2
            def td(V):
                return (1-2*d*T)*V + 2*T*U*V.derivative()
            numerator = td(td(P))-n*n*P
            if not numerator:
                continue
            lap, remainder = divmod(numerator, T)
            assert not remainder
            end = lap(U)
            q = next(j for j, coefficient in enumerate(end) if coefficient)
            exact = Poly(list(end)[q:])
            assert ell*delta+2*q-2 > 0
            terms.append((ell, q, arb_poly([ar(x) for x in exact])))
            endpoints.append({'ell': ell, 'order': q, 'degree': exact.degree()})
        assert terms
        groups = {}
        for i, (ell, q, P) in enumerate(terms):
            for j in range(i, len(terms)):
                ell2, q2, V = terms[j]
                exponent = (ell+ell2)*delta/2 + q+q2-3
                assert exponent > -1
                product = unit_minus*P*V*(1 if i == j else 2)
                groups[exponent] = groups.get(exponent, arb_poly([])) + product
        moments = [(b+j+1, value) for b, P in groups.items() for j, value in enumerate(P)]
        assert all(b > 0 for b, value in moments)
        slow_path = SLOW / f'verification/modes/mode_{n:03d}.json'
        slow = json.loads(slow_path.read_text()) if slow_path.exists() else None
        slow_rows = {Q(row['a']): row for row in slow['weights']} if slow else {}
        rows = []
        for a in weights:
            energy = sum((value/ar(a+b) for b, value in moments), arb(0))*arb.pi()/2
            assert energy > 0, (n, str(a), energy)
            assert energy.rel_accuracy_bits() > 150, (n, str(a), energy.rel_accuracy_bits())
            checks = {}
            if a in slow_rows:
                checks['Cartesian_exact_product_energy_overlap'] = bool(energy.overlaps(arb(slow_rows[a]['energy'])))
                assert all(checks.values()), (n, a, checks)
            rows.append({'a': str(a), 'energy': energy.str(100), 'norm': energy.sqrt().str(100),
                         'relative_accuracy_bits': energy.rel_accuracy_bits(), 'checks': checks})
        record = {'utc': now(), 'mode': n, 'manifest_sha256': mh,
                  'endpoints': endpoints, 'groups': len(groups), 'moments': len(moments),
                  'weights': rows, 'elapsed_seconds': time.monotonic()-ms,
                  'Cartesian_record_sha256': digest(slow_path) if slow else None}
        write_new(output, record)
        completed[n] = record
        fresh += 1
        print('mode', n, 'seconds', record['elapsed_seconds'], 'total', time.monotonic()-start, flush=True)
    full = len(completed) == len(modes)
    rows = []
    for a in weights:
        energy = sum((arb(next(row['energy'] for row in rec['weights'] if Q(row['a']) == a))
                      for rec in completed.values()), arb(0))
        rows.append({'a': str(a), 'energy': energy.str(90),
                     'norm' if full else 'partial_norm_lower': energy.sqrt().str(90)})
    result = {'utc': now(), 'candidate': NAME, 'complete': full,
              'manifest_sha256': mh, 'completed_modes': sorted(completed),
              'missing_modes': [n for n in modes if n not in completed], 'weights': rows,
              'mode_record_sha256': {str(n): digest(BASE/f'verification/modes/mode_{n:03d}.json')
                                     for n in sorted(completed)},
              'stage_elapsed_seconds': time.monotonic()-start,
              'total_mode_seconds': sum(rec['elapsed_seconds'] for rec in completed.values()),
              'status': 'N4-origin, OPEN peer' if full else 'Partial lower bounds, no full upper norm'}
    if full:
        write_new(BASE/'verification/full.json', result)
    else:
        (BASE/'verification/progress.json').write_text(json.dumps(result, indent=2)+'\n')
    print('DONE', len(completed), '/', len(modes), 'full' if full else 'partial', flush=True)
    for row in rows:
        print(row['a'], row.get('norm', row.get('partial_norm_lower')), flush=True)


if __name__ == '__main__':
    main()
