"""Exact-field finite radial sums; no publisher implementation is executed."""
from pathlib import Path
from datetime import datetime, timezone
from hashlib import sha256
import argparse, ast, importlib.util, json, sys, time
from flint import arb, arb_poly, ctx, fmpq as Q

ROOT = Path(__file__).resolve().parents[3]
BASE = ROOT/'research/scaled_pairing_quadrature'
JOINT = ROOT/'research/joint_scaled_factored_weak'
sys.path.insert(0, str(JOINT/'code'))
from fields_joint import ScaledRadial, SCALES, ar, field_hash
import weak as W
sys.set_int_max_str_digits(0)


def sha(path):
    return sha256(Path(path).read_bytes()).hexdigest()


def write(path, record):
    with path.open('x') as f:
        json.dump(record, f, indent=2)
        f.write('\n')


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('candidate')
    parser.add_argument('n', type=int)
    parser.add_argument('K', type=int, nargs='+')
    args = parser.parse_args()
    start = time.monotonic()
    ctx.prec = 2048
    assert Path(args.candidate).name == args.candidate
    assert args.n > 0 and args.n % 2
    assert len(args.K) == len(set(args.K))
    assert all(k >= (args.n-1)//2 for k in args.K)
    output = BASE/f'verification/{args.candidate}_n{args.n:03d}.json'
    assert not output.exists()
    directory = ROOT/'research/candidate_audits/data'/args.candidate
    manifestp = directory/'MANIFEST.json'
    manifest = json.loads(manifestp.read_text())
    assert manifest['id'] == args.candidate
    assert len(manifest['coefficient_files']) == 1
    entry = manifest['coefficient_files'][0]
    assert Path(entry['name']).name == entry['name']
    rawp = directory/entry['name']
    assert sha(rawp) == entry['sha256']
    data = json.loads(rawp.read_text())
    inputs = {}
    checks = []

    def bind(path):
        path = Path(path).resolve()
        assert path.is_relative_to(ROOT)
        inputs[str(path.relative_to(ROOT))] = sha(path)

    def record(path):
        obj = json.loads(Path(path).read_text())
        for rel, expected in obj.get('inputs', {}).items():
            assert sha(ROOT/rel) == expected, rel
            bind(ROOT/rel)
        bind(path)
        return obj

    for p in [rawp, manifestp, directory/'SHA256SUMS', Path(__file__),
              BASE/'PROOF.md', JOINT/'PROOF.md', JOINT/'code/weak.py',
              JOINT/'code/fields_joint.py',
              ROOT/'research/factored_pole_moments/code/moments.py',
              ROOT/'research/factored_pole_moments/PROOF.md']:
        bind(p)
    for line in (directory/'SHA256SUMS').read_text().splitlines():
        digest, name = line.split(None, 1)
        name = name.lstrip('*')
        assert Path(name).name == name and sha(directory/name) == digest
        bind(directory/name)
    checks.append('complete immutable snapshot files')
    for rel in ['research/joint_scaled_factored_weak/verification/fields.json',
                'research/joint_scaled_factored_weak/verification/scalar_joint.json',
                'research/joint_scaled_factored_weak/verification/candidate013.json',
                'research/factored_pole_moments/verification/result.json']:
        record(ROOT/rel)
    checks.append('exact field and positive-pole calibration bindings')
    original = record(ROOT/'research/weak_radial_quadrature/verification/candidate007.json')
    acceptp = ROOT/'research/weak_radial_quadrature/reviews/T4_193/ACCEPTANCE.json'
    accepted = json.loads(acceptp.read_text())
    assert accepted['own_source_sha256'] == sha(ROOT/'research/weak_radial_quadrature/verification/candidate007.json')
    assert accepted['checks'] == 210 and accepted['finite_sums'] == 70
    bind(acceptp)
    peer_manifestp = acceptp.parent/'MANIFEST.json'
    pm = json.loads(peer_manifestp.read_text())
    for name, row in pm['files'].items():
        p = peer_manifestp.parent/name
        assert sha(p) == row['sha256']
        bind(p)
    bind(peer_manifestp)
    checks.append('recorded radial nodes and independent N4-159 acceptance')
    source_manifestp = BASE/'source/MANIFEST.json'
    sm = json.loads(source_manifestp.read_text())
    for name, row in sm['files'].items():
        p = BASE/'source'/name
        assert sha(p) == row['sha256']
        bind(p)
    bind(source_manifestp)
    old = ROOT/'research/multiscale_generators/source/N1_ipm_eval.py'
    bind(old)
    function_trees = []
    for p in [old, BASE/'source/N1_ipm_eval.py']:
        tree = ast.parse(p.read_text())
        match = [node for node in tree.body if isinstance(node, ast.FunctionDef)
                 and node.name == 'whole_axis_radial']
        assert len(match) == 1
        function_trees.append(ast.dump(match[0], include_attributes=False))
    assert function_trees[0] == function_trees[1]
    checks.append('current and frozen radial function identity, source text only')
    source = (BASE/'source/N1_run_quot.py').read_text()
    assert source.index('parts, comp, Fd = prob.objective_parts(a); report') < source.index('a_exact, piv = OPT.finalize_exact')
    assert "'I_k_final_mesh': prob.last_Ik" in source
    checks.append('metadata pairings recorded before exact coefficient projection')
    objective = None
    if args.candidate == 'C1-N1-021-heldin14-legqs25p50':
        assert sha(rawp) == 'c6ed292b9f7129ad236f8441140745ec6accc3918d477ca2268e55bf7efc85c8'
        objective = record(ROOT/'research/candidate021_holdout/verification/result.json')
        assert objective['raw_sha256'] == sha(rawp)
        assert data['meta']['middle_order'] == 16
        assert data['meta']['angular_midpoint'] == 180
        assert len(data['meta']['pair_k']) == len(data['meta']['I_k_final_mesh']) == 81
        checks.append('actual021 full objective history and settings')
    directp = ROOT/'research/generator_sector_audit/verification'/f'{args.candidate}_direct.json'
    direct = json.loads(directp.read_text())
    assert direct['generator_sha256'] == sha(rawp)
    assert direct['B0n_exact'] and direct['leading_density_equal_state131']
    assert direct['c_equal_state131'] and direct['sector_summary']['all_forbidden_zero']
    bind(directp)
    model = ScaledRadial(rawp)
    assert model.c == Q(manifest['c_l_exact'])
    projection, pairs = W.project(model, args.n)
    phash = field_hash(projection)
    projection_seconds = time.monotonic()-start
    assert projection
    print('PROJECTED', args.candidate, args.n, 'groups', len(projection),
          'pairs', pairs, 'seconds', projection_seconds, flush=True)
    exact, moments, regressions = {}, {}, {}
    for k in args.K:
        value, groups = W.integrate_groups(projection, model.delta, Q(-1), k+1, f'I_K{k}')
        assert not value.contains(0) and value.rel_accuracy_bits() > 150
        exact[k] = value
        moments[k] = groups
        priorp = JOINT/f'verification/{args.candidate}_n{args.n:03d}_K{k:05d}.json'
        if priorp.exists():
            prior = record(priorp)
            assert prior['raw_sha256'] == sha(rawp)
            assert phash == prior['projection_sha256']
            assert value.overlaps(arb(prior['pairing']))
            regressions[str(k)] = {'exact_projection_hash_equal': True,
                                   'whole_plane_overlap': True,
                                   'prior_source': str(priorp.relative_to(ROOT)),
                                   'peer_scope': prior['status']}
    checks.append('every exact whole-plane pairing has convergent complete groups')
    if args.n == 19 and 1800 in args.K and args.candidate == 'C1-N1-021-heldin14-legqs25p50':
        assert '1800' in regressions
    parts = []
    for ell, A in sorted(projection.items()):
        assert ell*model.delta/2-1 > -1
        p = arb_poly([ar(q) for q in A.P])
        pv = arb_poly([ar(q) for q in A.numerator_v()])
        parts.append((ell, A, p, pv))
    rules = []
    for order in [16, 24, 32]:
        tick = time.monotonic()
        path = ROOT/f'research/weak_radial_quadrature/verification/nodes_mid{order}.json'
        assert original['inputs'][str(path.relative_to(ROOT))] == sha(path)
        bind(path)
        nodes_record = json.loads(path.read_text())
        assert nodes_record['order'] == order
        nodes = [(Q(r), Q(w)) for r, w in nodes_record['rational_radii_weights']]
        assert all(r > 0 and w > 0 for r, w in nodes)
        if order == 16:
            assert len(nodes) == 212
        sums = {k: arb(0) for k in args.K}
        count, minbits = 0, 10**9
        for r, w in nodes:
            t, v = ar(r*r/(1+r*r)), ar(1/(1+r*r))
            amplitude = arb(0)
            for ell, A, p, pv in parts:
                den = arb(1)
                for a, power in zip(SCALES, A.powers, strict=True):
                    if power:
                        den *= (1+ar(a)*v)**power
                assert den > 0
                left, right = p(t)/den, pv(v)/den
                assert left.overlaps(right)
                minbits = min(minbits, left.rel_accuracy_bits(), right.rel_accuracy_bits())
                count += 1
                amplitude += v**ar(ell*model.delta/2)*A.evaluate(t, v)
            assert not amplitude.contains(0)
            minbits = min(minbits, amplitude.rel_accuracy_bits())
            assert minbits > 100, (order, str(r), minbits)
            for k in args.K:
                sums[k] += ar(w)*t**(k+2)*amplitude
        rows = []
        for k in args.K:
            value = arb.pi()*sums[k]
            error = value-exact[k]
            assert value.rel_accuracy_bits() > 100
            metadata = None
            for pair, floatval in zip(data['meta'].get('pair_k', []),
                                      data['meta'].get('I_k_final_mesh', []), strict=True):
                actualpair = [1, pair] if isinstance(pair, int) else pair
                if actualpair == [args.n, k]:
                    assert metadata is None
                    metadata = floatval
            rows.append({'n': args.n, 'K': k,
                         'finite_sum_ball': value.str(100),
                         'whole_plane_ball': exact[k].str(100),
                         'error_vs_whole_plane_ball': error.str(100),
                         'relative_error_ball': (error/abs(exact[k])).str(65),
                         'analytic_objective_row': metadata is not None,
                         'metadata_preprojection_float': metadata,
                         'metadata_comparison_scope': 'FLOAT pre-exact-projection vector; not a pure floating-evaluation error'})
            print('RULE', order, args.n, k, 'I', exact[k].str(25),
                  'Q', value.str(25), 'error', error.str(25), flush=True)
        rules.append({'order': order, 'nodes': len(nodes),
                      'composition_checks': count, 'minimum_accuracy_bits': minbits,
                      'values': rows, 'elapsed_seconds': time.monotonic()-tick})
    out = {'utc': datetime.now(timezone.utc).isoformat(),
           'candidate': args.candidate, 'raw_sha256': sha(rawp),
           'n': args.n, 'K': args.K, 'precision_bits': ctx.prec,
           'projection_sha256': phash, 'projection_pairs': pairs,
           'projection_groups': len(projection),
           'whole_plane_moments': moments, 'prior_projection_checks': regressions,
           'checks': checks, 'rules': rules, 'inputs': inputs,
           'projection_elapsed_seconds': projection_seconds,
           'elapsed_seconds': time.monotonic()-start,
           'no_angular_quadrature': True,
           'whole_plane_pairing_no_radial_quadrature': True,
           'finite_rule_error_includes_omitted_domains': True,
           'publisher_code_executed': False,
           'status': 'OPEN independent actual finite-sum and continuum-pairing reproduction; candidate-specific only'}
    write(output, out)
    print('DONE', output, 'seconds', out['elapsed_seconds'], flush=True)


if __name__ == '__main__':
    main()
