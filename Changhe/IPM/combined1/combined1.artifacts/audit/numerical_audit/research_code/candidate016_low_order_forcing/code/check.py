"""Scalar forcing lower bounds from independently accepted G0 and G1 only."""
from pathlib import Path
from datetime import datetime, timezone
from hashlib import sha256
from fractions import Fraction as Q
import json, time
from flint import arb, ctx
R = Path(__file__).resolve().parents[3]
B = R / 'research/candidate016_low_order_forcing'
sha = lambda p: sha256(Path(p).read_bytes()).hexdigest()
now = lambda: datetime.now(timezone.utc).isoformat()
def ar(q):
    q = Q(q)
    return arb(q.numerator) / q.denominator
def lower(value, digits):
    scale = 10**digits
    q = Q(int((value.lower()*scale).floor().unique_fmpz()) - 1, scale)
    assert ar(q) < value.lower()
    return {'ball': value.str(100), 'strict_lower_exact': str(q)}
def main():
    ctx.prec = 1024; started = time.monotonic(); inputs = {}; checks = {}
    target = B / 'verification/result.json'; assert not target.exists()
    def bind(p, expected=None):
        p = Path(p); h = sha(p)
        assert expected is None or h == expected, (str(p), h, expected)
        rel = str(p.relative_to(R))
        assert rel not in inputs or inputs[rel] == h
        inputs[rel] = h
        return p
    def read(p, expected=None):
        return json.loads(bind(p, expected).read_text())
    prepared = read(B / 'verification/PROOF_FIRST.json')
    assert prepared['proof_written_before_checker']
    for rel, h in prepared['inputs'].items(): bind(R / rel, h)
    bind(Path(__file__))
    comp = read(B / 'source/components.json')
    accepted = read(R / comp['accepted_record'], comp['accepted_record_sha256'])
    assert accepted['verdict'].startswith('CONFIRMED') and all(accepted['checks'].values())
    for rel, h in accepted['inputs'].items(): bind(R / rel, h)
    audit = read(R / 'research/candidate016_registered_assembly/verification/result.json')
    assert audit['verdict'].startswith('CONFIRMED conditional') and all(audit['checks'].values())
    for rel, h in audit['inputs'].items(): bind(R / rel, h)
    parameters = read(B / 'source/parameters.json')
    assert sha(B / 'source/parameters.json') == sha(R / 'research/candidate016_registered_assembly/source/parameters.json')
    assert comp['candidate'] == accepted['candidate'] == audit['candidate'] == parameters['candidate'] == 'C1-N1-016-legqs25-quot013'
    assert comp['raw_sha256'] == accepted['raw_sha256'] == audit['raw_sha256'] == parameters['raw_sha256'] == 'a0345b4eee060ea8f6b0b6e21719cf606b04174704e0a26f516c645081208f42'
    checks['candidate_and_exact_parameter_binding'] = True
    lower_inputs = {}
    for key in ['G0', 'G1']:
        row = comp['components'][key]; a = accepted['norms'][key]
        q = Q(row['lower_exact'])
        assert 0 < q == Q(a['accepted_lower_exact']) and Q(row['upper_exact']) == Q(a['accepted_upper_exact'])
        assert ar(q) < arb(a['own_lower_ball']).lower()
        assert a['whole_plane_no_quadrature'] and a['peer_40digit_endpoint_balls_contain_own']
        lower_inputs[key] = q
    checks['both_strict_component_lower_endpoints'] = True
    previous = {row['framework']: row for row in audit['instances']}
    assert len(previous) == 10
    specifications = []
    for name, s, threshold, old_divisor in parameters['Ns']:
        specifications.append((name, 'Ns', s, 2**14, 2**18, threshold))
    name, s, threshold, old_divisor = parameters['legacy_X3']
    specifications.append((name, 'X3', s, 2**14, 2**18, threshold))
    for name, s, w1, w2, cw, threshold in parameters['XSW']:
        specifications.append((name, 'XSW', s, w1, w2, threshold))
    assert len(specifications) == 10
    rows = []
    for name, kind, ss, w1, w2, tt in specifications:
        s, threshold = Q(ss), Q(tt)
        assert s >= 0 and threshold > 0 and w1 > 0 and w2 > 0
        old = previous[name]
        assert (old['kind'], Q(old['s_exact']), Q(old['threshold_exact'])) == (kind, s, threshold)
        if kind == 'XSW': assert old['weights'] == [w1, w2]
        square = w1*lower_inputs['G1']**2 + w2*lower_inputs['G0']**2
        assert square > 0
        energy = ar(square).sqrt(); ratio = energy/ar(threshold)
        assert energy.is_finite() and ratio.is_finite() and ratio > 1
        assert ratio.rel_accuracy_bits() > 900
        e_lower = lower(energy, 12); r_lower = lower(ratio, 0)
        assert Q(r_lower['strict_lower_exact']) > 1
        rows.append({'framework': name, 'kind': kind, 's_exact': str(s), 'weights': [w1, w2],
                     'sufficient_threshold_exact': str(threshold), 'low_order_square_exact': str(square),
                     'forcing_lower_comparison': e_lower, 'threshold_ratio_lower_comparison': r_lower,
                     'sufficient_smallness_condition_fails': True})
    checks['all_ten_exact_registered_instances'] = True
    checks['exact_rebalanced_and_legacy_divisors'] = (Q(parameters['Ns'][2][2]) == Q(3, 327680) and Q(parameters['legacy_X3'][2]) == Q(1, 163840))
    checks['no_P2_H_or_fractional_upper_input_used'] = True
    checks['no_commutator_comparison_factor_used'] = True
    assert all(checks.values())
    for rel, h in inputs.items(): assert sha(R / rel) == h, rel
    output = {'utc': now(), 'candidate': comp['candidate'], 'raw_sha256': comp['raw_sha256'],
              'precision_bits': ctx.prec, 'inputs': inputs, 'checks': checks,
              'component_lower_inputs': {k: str(v) for k, v in lower_inputs.items()}, 'instances': rows,
              'minimal_strict_integer_factor': str(min(Q(row['threshold_ratio_lower_comparison']['strict_lower_exact']) for row in rows)),
              'scope': 'Actual candidate fails the ten specified sufficient scalar forcing conditions. No stationary-correction nonexistence theorem, dyadic implication, inverse, fractional upper norm or existence claim.',
              'unaccepted_N3_component_values_used': False, 'foreign_code_executed': False,
              'elapsed_seconds': time.monotonic()-started,
              'verdict': 'CONFIRMED strict registered scalar forcing obstructions from accepted whole-plane G0 and G1'}
    with target.open('x') as f: json.dump(output, f, indent=2); f.write('\n')
    print(output['utc'], output['verdict'], 'SHA256', sha(target), 'bindings', len(inputs), flush=True)
    for row in rows:
        print(row['framework'], row['forcing_lower_comparison']['strict_lower_exact'],
              'factor>', row['threshold_ratio_lower_comparison']['strict_lower_exact'], flush=True)
if __name__ == '__main__': main()
