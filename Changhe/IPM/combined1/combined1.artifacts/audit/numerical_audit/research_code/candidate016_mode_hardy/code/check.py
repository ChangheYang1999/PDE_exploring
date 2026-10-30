"""Own complete angular-divergence Hardy bound; no peer implementation imports."""
from pathlib import Path
from datetime import datetime, timezone
from hashlib import sha256
import importlib.util, json, sys, time
from flint import fmpq as Q, arb, ctx

R = Path(__file__).resolve().parents[3]
B = R / 'research/candidate016_mode_hardy'
CANDIDATE = 'C1-N1-016-legqs25-quot013'
RAW_SHA = 'a0345b4eee060ea8f6b0b6e21719cf606b04174704e0a26f516c645081208f42'
sys.set_int_max_str_digits(0)
sha = lambda p: sha256(Path(p).read_bytes()).hexdigest()
now = lambda: datetime.now(timezone.utc).isoformat()

def log(*args):
    print(now(), *args, flush=True)

def exclusive(path, data):
    with Path(path).open('x') as f:
        json.dump(data, f, indent=2)
        f.write('\n')

def load(name, path):
    spec = importlib.util.spec_from_file_location(name, path)
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module

def polyhash(poly):
    h = sha256()
    h.update(str(len(poly)).encode() + b'\n')
    for q in poly:
        h.update(str(q).encode() + b'\n')
    return h.hexdigest()

def fieldrecord(field):
    h = sha256()
    records = []
    for key, A in sorted(field.items()):
        record = {'key': list(key), 'degree': A.P.degree(), 'powers': list(A.powers),
                  'numerator_sha256': polyhash(A.P)}
        h.update(json.dumps(record, sort_keys=True, separators=(',', ':')).encode() + b'\n')
        records.append(record)
    return {'representation_sha256': h.hexdigest(), 'component_count': len(field),
            'components': records}

def contains_wide(text, value):
    wide = arb(text)
    assert wide.is_finite() and value.is_finite()
    assert wide.lower() < value.lower() and value.upper() < wide.upper(), (text, value.str(45))

def main():
    ctx.prec = 2048
    started = time.monotonic()
    inputs = {}
    def bind(p, expected=None):
        p = Path(p)
        actual = sha(p)
        assert expected is None or actual == expected, (str(p), actual, expected)
        rel = str(p.relative_to(R))
        assert rel not in inputs or inputs[rel] == actual
        inputs[rel] = actual
        return p
    def read(p, expected=None):
        return json.loads(bind(p, expected).read_text())
    prepared = read(B / 'verification/PROOF_FIRST.json')
    bind(B / 'PROOF.md', prepared['proof_sha256'])
    bind(Path(__file__))
    for name, record in prepared['files'].items():
        bind(B / 'source' / name, record['sha256'])
    peer = read(B / 'source/N3_hardy.json')
    assert peer['id'] == CANDIDATE and peer['source_sha256'] == RAW_SHA
    assert peer['code_sha256'] == sha(B / 'source/N3_legqs_hardy.py')
    fixture = read(R / 'research/scaled_product_norms/verification/fixtures.json',
                   'f1327e153ac724c3674ccc1498650817136e37bca51970ade359fa20d619006c')
    for rel, h in fixture['inputs'].items():
        bind(R / rel, h)
    acceptance = read(R / 'research/candidate016_scaled_norm_peer/verification/comparison_G0_rF_v01.json',
                      '31b509e033d0a59f1826b3c5336e35123bab25a2bce280f063f0e273ed256cfa')
    assert acceptance['verdict'].startswith('CONFIRMED') and all(acceptance['checks'].values())
    for rel, h in acceptance['inputs'].items():
        bind(R / rel, h)
    own = read(R / 'research/candidate016_scaled_norm_peer/source/N4_norms_partial_v01.json',
               '7e7b51a4473936d0ee9803fb12df45851ab42a10c0974787feed7c6728e0a58c')
    for rel, h in own['inputs'].items():
        bind(R / rel, h)
    assert own['candidate'] == CANDIDATE and own['raw_sha256'] == RAW_SHA
    assert own['point_checks']['value_count'] == 33
    assert own['point_checks']['minimum_accuracy_bits'] > 150
    rawpaths = list((R / 'research/candidate_audits/data' / CANDIDATE).glob('*_exact.json'))
    assert len(rawpaths) == 1
    rawp = bind(rawpaths[0], RAW_SHA)
    raw = json.loads(rawp.read_text())
    shared = R.parent / 'c1-shared/candidate_snapshots' / CANDIDATE
    assert sha(shared / rawp.name) == RAW_SHA
    local_manifest = rawp.parent / 'MANIFEST.json'
    shared_manifest = shared / 'MANIFEST.json'
    if local_manifest.exists():
        bind(local_manifest)
        if shared_manifest.exists():
            assert sha(local_manifest) == sha(shared_manifest)
    # Explicit own executable graph, bound before importing any own arithmetic.
    modules = {
        'packed': 'research/scaled_product_norms/code/packed.py',
        'radial': 'research/joint_scaled_factored_weak/code/fields_joint.py',
        'moments': 'research/rational_pole_moments/code/moments.py',
    }
    for rel in modules.values():
        bind(R / rel)
    state = {'utc_start': now(), 'candidate': CANDIDATE, 'raw_sha256': RAW_SHA,
             'precision_bits': ctx.prec, 'saved_ball_digits': 650, 'inputs': inputs,
             'peer_implementation_imported': False, 'complete_plane_no_quadrature': True,
             'bound_is_angular_divergence_upper_not_exact_negative_norm': True}
    index = 1
    while (B / f'verification/start_v{index:02d}.json').exists():
        index += 1
    exclusive(B / f'verification/start_v{index:02d}.json', state)
    P = load('own_hardy_packed', R / modules['packed'])
    M = load('own_hardy_moments', R / modules['moments'])
    jet = P.J.ScaledRadial(raw)
    assert str(jet.c) == own['cl_exact'] == '4076476460239181/2251799813685248'
    assert str(jet.delta) == own['delta_exact'] == '1824676646553933/4076476460239181'
    F, backgrounds = P.residual(jet, log)
    del backgrounds
    record = fieldrecord(F)
    assert record == own['fields']['D0_0'], 'fresh exact residual differs from Cartesian-checked record'
    assert all(kind == 's' and n > 0 for ell, kind, n in F)
    modes = sorted({n for ell, kind, n in F})
    assert len(modes) == len(peer['modes']) == 160
    assert modes == [row['n'] for row in peer['modes']] == list(range(1, 320, 2))
    assert record['component_count'] == 1360
    log('F_RECONSTRUCTED', len(F), 'modes', len(modes), 'seconds', time.monotonic() - started)
    peerrows = {row['n']: row for row in peer['modes']}
    mode_records = []
    total_rF2, total_B2 = arb(0), arb(0)
    minimum = 10**9
    for n in modes:
        path = B / f'verification/mode_{n:03d}.json'
        branches = sorted((ell, A) for (ell, kind, m), A in F.items() if m == n)
        assert len(branches) == peerrows[n]['components']
        if path.exists():
            row = json.loads(path.read_text())
            assert row['inputs'] == inputs and row['candidate'] == CANDIDATE and row['n'] == n
            assert row['precision_bits'] == ctx.prec and row['component_count'] == len(branches)
            assert row['F_representation_sha256'] == record['representation_sha256']
            assert row['status'] == 'CONFIRMED complete own mode integral'
            S = sum((arb(g['integral_ball']) for g in row['groups']), arb(0))
            square = arb(row['rF_n_sq'])
            assert (arb.pi() / 2 * S).overlaps(square)
            assert square > 0 and square.rel_accuracy_bits() > 150
            for rel, h in row['inputs'].items():
                assert sha(R / rel) == h, rel
            log('MODE_REUSED', n, sha(path))
        else:
            mode_started = time.monotonic()
            groups = {}
            for ell, A in branches:
                for ell2, C in branches:
                    key = ell + ell2
                    groups[key] = groups.get(key, P.Rat()) + A * C
            groups = {ell: A for ell, A in groups.items() if A}
            S = arb(0)
            evidence = []
            for ell, A in sorted(groups.items()):
                numerator = A.numerator_v() * P.V**2
                order = 0
                while numerator and numerator[0] == 0:
                    numerator, remainder = divmod(numerator, P.T)
                    assert not remainder
                    order += 1
                assert numerator
                b = ell * jet.delta / 2 - 4 + order
                assert b > -1, (n, ell, 'nonintegrable group', str(b))
                factors = [(a, power) for a, power in zip(P.J.SCALES, A.powers) if power]
                value, decomposition = M.integral(b, numerator, factors)
                assert value.is_finite() and value.rel_accuracy_bits() > 150
                assert decomposition['exact_reconstruction']
                S += value
                evidence.append({'ell_sum': ell, 'endpoint_v_order': order, 'b': str(b),
                                 'degree_v': numerator.degree(), 'powers': list(A.powers),
                                 'numerator_v_sha256': polyhash(numerator),
                                 'integral_ball': value.str(650),
                                 'integral_accuracy_bits': value.rel_accuracy_bits(),
                                 'decomposition': decomposition})
            square = arb.pi() / 2 * S
            assert square > 0 and square.rel_accuracy_bits() > 150
            root = square.sqrt()
            row = {'utc': now(), 'status': 'CONFIRMED complete own mode integral',
                   'candidate': CANDIDATE, 'raw_sha256': RAW_SHA, 'n': n,
                   'precision_bits': ctx.prec, 'inputs': inputs,
                   'F_representation_sha256': record['representation_sha256'],
                   'component_count': len(branches), 'ordered_pair_count': len(branches)**2,
                   'group_count': len(evidence), 'groups': evidence,
                   'rF_n_sq': square.str(650), 'rF_n': root.str(650),
                   'H_n_UB': (root / n).str(650),
                   'minimum_group_accuracy_bits': min(g['integral_accuracy_bits'] for g in evidence),
                   'square_accuracy_bits': square.rel_accuracy_bits(),
                   'elapsed_seconds': time.monotonic() - mode_started}
            for key in ['rF_n_sq', 'rF_n', 'H_n_UB']:
                contains_wide(peerrows[n][key], arb(row[key]))
            for rel, h in inputs.items():
                assert sha(R / rel) == h, rel
            exclusive(path, row)
            log('MODE_DONE', n, 'components', len(branches), 'groups', len(evidence),
                'rF', root.str(30), 'seconds', row['elapsed_seconds'])
        for key in ['rF_n_sq', 'rF_n', 'H_n_UB']:
            contains_wide(peerrows[n][key], arb(row[key]))
        assert square.sqrt().overlaps(arb(row['rF_n']))
        assert (square.sqrt() / n).overlaps(arb(row['H_n_UB']))
        total_rF2 += square
        total_B2 += square / n**2
        minimum = min(minimum, row['minimum_group_accuracy_bits'], row['square_accuracy_bits'])
        mode_records.append({'n': n, 'record': str(path.relative_to(R)), 'sha256': sha(path),
                             'component_count': len(branches),
                             'peer_all_three_displayed_balls_contain_own': True})
    norm_rF, bound = total_rF2.sqrt(), total_B2.sqrt()
    contains_wide(peer['rF_check'], norm_rF)
    contains_wide(peer['H_upper_ball'], bound)
    accepted = acceptance['norms']['rF']
    assert P.J.ar(Q(accepted['accepted_lower_exact'])) < norm_rF.lower()
    assert norm_rF.upper() < P.J.ar(Q(accepted['accepted_upper_exact']))
    assert norm_rF.overlaps(arb(accepted['own_lower_ball']))
    endpoint = arb(peer['H_upper'])
    assert endpoint.is_finite() and endpoint.lower() > bound.upper(), 'peer long upper endpoint direction unresolved'
    upper = Q(int((bound.upper() * 10**30).ceil().unique_fmpz()) + 1, 10**30)
    assert P.J.ar(upper) > bound.upper()
    lower = Q(int((bound.lower() * 10**30).floor().unique_fmpz()) - 1, 10**30)
    assert P.J.ar(lower) < bound.lower()
    for rel, h in inputs.items():
        assert sha(R / rel) == h, rel
    state.update({'utc': now(), 'status': 'CONFIRMED complete angular-divergence upper bound',
                  'F': record, 'modes': mode_records, 'mode_count': len(modes),
                  'rF_square_ball': total_rF2.str(650), 'rF_ball': norm_rF.str(650),
                  'B_square_ball': total_B2.str(650), 'B_ball': bound.str(650),
                  'B_lower_exact': str(lower), 'B_upper_exact': str(upper),
                  'H_upper_exact': str(upper), 'minimum_accuracy_bits': minimum,
                  'peer_long_H_upper_endpoint_is_above_own_B': True,
                  'all160_modes_and480_peer_displays_checked': True,
                  'accepted_whole_plane_rF_normalization_reproduced': True,
                  'historical_peer_cache_or_execution_provenance_not_reconstructed': True,
                  'E2_assembly': 'OPEN in this checker; requires separately accepted G1 and P2',
                  'elapsed_seconds': time.monotonic() - started})
    exclusive(B / 'verification/result.json', state)
    log('CONFIRMED', 'H <=', str(upper), 'B', bound.str(50),
        'SHA256', sha(B / 'verification/result.json'), 'seconds', state['elapsed_seconds'])

if __name__ == '__main__':
    main()
