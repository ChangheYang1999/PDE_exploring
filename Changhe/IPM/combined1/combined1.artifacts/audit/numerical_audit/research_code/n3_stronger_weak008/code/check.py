"""Independent complete first-sine envelope certificates for candidate008."""
from pathlib import Path
from datetime import datetime, timezone
from hashlib import sha256
import importlib.util, json, sys, time
from flint import arb, ctx, fmpq as Q
ROOT = Path(__file__).resolve().parents[3]
BASE = ROOT / 'research/n3_stronger_weak008'
NAME = 'C1-N1-008-d2w-j7-x3bal'
sys.set_int_max_str_digits(0)
spec = importlib.util.spec_from_file_location('n4_complete008_envelope', ROOT / 'research/large_index_weak/code/check.py')
L = importlib.util.module_from_spec(spec)
spec.loader.exec_module(L)
sha = lambda p: sha256(Path(p).read_bytes()).hexdigest()
now = lambda: datetime.now(timezone.utc).isoformat()

def main():
    started = time.monotonic()
    ctx.prec = 2048
    target = BASE / 'verification/result.json'
    assert not target.exists()
    frozen_manifest = BASE / 'source/MANIFEST.json'
    frozen = json.loads(frozen_manifest.read_text())
    for name, item in frozen['files'].items():
        assert sha(BASE / 'source' / name) == item['sha256']
    peer_path = BASE / 'source/N3_008_wlap.json'
    peer = json.loads(peer_path.read_text())
    directory = ROOT / 'research/candidate_audits/data' / NAME
    canonical = directory / 'canonical.json'
    audit_path = ROOT / 'research/candidate_audits/verification' / f'{NAME}.json'
    audit = json.loads(audit_path.read_text())
    assert audit['all_forbidden_zero'] and audit['B0n_exact']
    assert all(audit['snapshot_hashes_confirmed'].values())
    assert sha(canonical) == audit['canonical_sha256']
    assert peer['id'] == NAME and peer['source_sha256'] == audit['generator_sha256']
    model = L.Radial(canonical)
    assert model.state['source_sha256'] == peer['source_sha256']
    assert model.c == Q(peer['cl']) and model.c > 1
    snap = json.loads((directory / 'MANIFEST.json').read_text())
    assert len(snap['coefficient_files']) == 1
    item = snap['coefficient_files'][0]
    raw = directory / item['name']
    assert sha(raw) == item['sha256'] == peer['source_sha256']
    for line in (directory / 'SHA256SUMS').read_text().splitlines():
        digest, name = line.split(None, 1)
        name = name.lstrip('*')
        assert Path(name).name == name and sha(directory / name) == digest
    projection, counts = L.F.W.project(model, 1)
    prepared = [(ell, ell * model.delta / 2, p, p(L.U)) for ell, p in sorted(projection.items())]
    assert prepared and all(b > 0 and pv(L.U) == p for _, b, p, pv in prepared)
    background = L.ENV.groups(model, ['u1', 'u2'])
    gradient = L.ENV.groups(model, ['rho_x', 'rho_y'])
    paths = [Path(__file__), BASE / 'PROOF.md', frozen_manifest, peer_path,
             BASE / 'source/N3_candidate_pipeline.py', canonical, raw, audit_path,
             directory / 'MANIFEST.json', directory / 'SHA256SUMS',
             ROOT / 'research/large_index_weak/code/check.py',
             ROOT / 'research/large_index_weak/PROOF.md',
             ROOT / 'research/factored_monomial_audit/code/check.py',
             ROOT / 'research/factored_monomial_audit/verification/result.json',
             ROOT / 'research/far_pairing_audit/code/check_v2.py',
             ROOT / 'research/successor_weak_probes/code/check.py',
             ROOT / 'research/successor_weak_probes/PROOF.md',
             ROOT / 'research/angular_probe_audit/code/check.py',
             ROOT / 'research/optimized_probe_audit/code/check.py',
             ROOT / 'research/localized_weak_probe/code/evaluate.py',
             ROOT / 'research/localized_weak_probe/code/beta_scale.py',
             ROOT / 'research/radial_fourier/code/radial.py',
             ROOT / 'research/projected_residual/code/build.py',
             ROOT / 'research/whole_plane_norms/code/pipeline.py']
    inputs = {str(p.relative_to(ROOT)): sha(p) for p in paths}
    print('PREPARED', len(projection), 'branches', len(background), len(gradient), 'groups',
          'seconds', time.monotonic() - started, flush=True)
    rows = []
    for k in (512, 2048):
        tick = time.monotonic()
        other = peer['WEAK_a0'][str(k)]
        iv, it, branches = L.PAIR.whole(prepared, k)
        fields = L.F.construct(model, 1, k)
        point_checks = L.F.point_checks(model, fields, 1, k)
        iparts, parts_count = L.F.parts(model, fields[0], k)
        assert iv.overlaps(it) and iv.overlaps(iparts) and iparts.rel_accuracy_bits() > 150
        env = L.envelopes(model, background, gradient, k)
        A, B, C = env['A'], env['Benv'], env['Cenv']
        sup = lambda a, b: Q(a**a * b**b, (a+b)**(a+b))
        H = sup(k, 2) + 2*k*sup(k, 3) + 4*sup(k+1, 2)
        assert H == Q(other['H_k'])
        D = A+B+C
        radius = 2*abs(iv)/(D+(D*D+4*L.ar(H)*abs(iv)).sqrt())
        floor = Q(int((radius.lower()*10**18).floor().unique_fmpz())-1, 10**18)
        assert floor > 0 and L.ar(floor) < radius
        comparisons = {
            'signed_pairing_overlap': iv.overlaps(arb(other['I_k_signed'])),
            'absolute_pairing_above_printed_lower_endpoint': bool(abs(iv) >= arb(other['I_k_LB']).lower()),
            'A_below_printed_upper_endpoint': bool(A <= arb(other['A_k_UB']).upper()),
            'B_below_printed_upper_endpoint': bool(B <= arb(other['B_k_UB']).upper()),
            'C_below_printed_upper_endpoint': bool(C <= arb(other['C_k_UB']).upper()),
            'radius_above_printed_lower_endpoint': bool(radius >= arb(other['m_k_LB']).lower()),
            'gradient_bound_exact_match': True,
        }
        if other['I_k_signed_over_pi_exact'] is not None:
            comparisons['exact_peer_pairing_over_pi_overlap'] = iv.overlaps(arb.pi()*L.ar(Q(other['I_k_signed_over_pi_exact'])))
        assert all(comparisons.values()), (k, comparisons)
        values = {'pairing_v': iv, 'pairing_t': it, 'pairing_parts': iparts,
                  'A': A, 'B': B, 'C': C, 'D': D, 'radius': radius, 'H_enclosure': L.ar(H),
                  **{name: val for name, val in env.items() if name.endswith('2')}}
        rows.append({'K': k, **{name: val.str(100) for name, val in values.items()},
                     'H_exact_sha256': sha256(str(H).encode()).hexdigest(),
                     'strict_lower_exact': str(floor), 'strict_floor_verified': True,
                     'peer_arithmetic': other['arithmetic'], 'peer_comparisons': comparisons,
                     'branches': branches, 'point_checks': point_checks,
                     'parts_pairs': parts_count, 'elapsed_seconds': time.monotonic()-tick})
        print('DONE K', k, 'radius', radius.str(35), 'floor', floor,
              'seconds', rows[-1]['elapsed_seconds'], flush=True)
    assert all(sha(ROOT / rel) == digest for rel, digest in inputs.items())
    out = {'utc': now(), 'candidate': NAME, 'precision_bits': ctx.prec, 'inputs': inputs,
           'raw_sha256': peer['source_sha256'], 'canonical_sha256': sha(canonical),
           'peer_canonical_identity_scope': 'same immutable raw source; no serialization hash equality asserted',
           'projection_sha256': L.F.W.poly_hash(projection), 'projection_pairs': counts,
           'complete_projected_branches': len(projection), 'all_background_modes_retained': True,
           'whole_plane': True, 'foreign_code_executed': False, 'rows': rows,
           'elapsed_seconds': time.monotonic()-started,
           'verdict': 'CONFIRMED independent first-sine envelope distances under the exact PROOF hypotheses'}
    with target.open('x') as stream:
        json.dump(out, stream, indent=2)
        stream.write('\n')
    print('RESULT', sha(target), 'seconds', out['elapsed_seconds'], flush=True)

if __name__ == '__main__':
    main()
