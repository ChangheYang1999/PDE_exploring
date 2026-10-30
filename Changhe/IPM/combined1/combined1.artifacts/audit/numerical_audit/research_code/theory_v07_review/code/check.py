"""Source-bound numerical consistency checks of the published theory_v07."""
from pathlib import Path
from fractions import Fraction as Q
from hashlib import sha256
from datetime import datetime, timezone
import json
import re
import time

R = Path(__file__).resolve().parents[3]
B = R / 'research/theory_v07_review'
ROOT = R.parent


def ball(s):
    m = re.fullmatch(r'\[([^\s]+) \+/- ([^\]]+)\]', s)
    assert m, s
    a, e = map(Q, m.groups())
    assert e >= 0
    return a - e, a + e


def historical_prefix(data, expected):
    h = sha256()
    offset = 0
    for line in data.splitlines(keepends=True):
        h.update(line)
        offset += len(line)
        if h.hexdigest() == expected:
            return offset
    return None


def main():
    start = time.monotonic()
    inputs, checks = {}, {}

    def bind(p, expected=None):
        p = Path(p)
        d = p.read_bytes()
        h = sha256(d).hexdigest()
        assert expected is None or h == expected, (str(p), h, expected)
        inputs[str(p.relative_to(R))] = h
        return d

    def read(p, expected=None):
        return json.loads(bind(p, expected))

    prep = read(B / 'verification/PREPARE.json')
    bind(B / 'PROOF.md', prep['proof_sha256'])
    bind(Path(__file__))
    report = bind(B / 'source/theory_v07.md', prep['report_sha256']).decode()
    assert len(report.splitlines()) == 710
    appendix = report.split('## Appendix H.')[1]
    pairs = re.findall(r'- ([0-9a-f]{64})\s+(c1-[^\s]+)', appendix)
    assert len(pairs) > 60 and len({p for _, p in pairs}) == len(pairs)
    source_rows = []
    for expected, rel in pairs:
        p = ROOT / rel
        data = p.read_bytes()
        actual = sha256(data).hexdigest()
        mode, offset = 'current_full_match', None
        if actual != expected:
            offset = historical_prefix(data, expected)
            if offset is not None:
                mode = 'historical_byte_prefix_match'
            else:
                mode = 'historical_version_OPEN_current_mutable_file_changed'
                if rel == 'c1-coord/NOTES_FOR_TEAM.md':
                    first = data.find(b'\n## ')
                    assert first > 0
                    header = data[:first]
                    for m in re.finditer(rb'\n## ', data):
                        if sha256(header + data[m.start():]).hexdigest() == expected:
                            mode = 'historical_newest_first_suffix_match'
                            offset = m.start()
                            break
        source_rows.append({'path': rel, 'publication_sha256': expected,
                            'current_sha256': actual, 'binding': mode,
                            'historical_boundary_bytes': offset})
    checks['all_appendix_H_entries_inspected'] = len(source_rows)
    ownledger = next(x for x in source_rows if x['path'] == 'c1-n4/VERIFY_REPORT.md')
    assert ownledger['binding'] in ['historical_byte_prefix_match', 'current_full_match']
    checks['own_ledger_through332_historical_hash_reproduced'] = True
    floors = {7: Q('0.004769166867')}
    weak_rows = []
    for n in [16, 20, 21, 22]:
        d = read(R / f'research/candidate{n:03d}_weak_peer/verification/result.json')
        assert d['verdict'].startswith('CONFIRMED')
        row, = [v for v in d['rows'] if (v['n'], v['K']) == (19, 1800)]
        floors[n] = Q(row['strict_floor'])
        lo, hi = ball(row['radius_recomputed'])
        assert 0 < floors[n] < lo <= hi
        weak_rows.append({'candidate': n, 'floor_exact': str(floors[n]),
                          'accepted_utc': d['utc'], 'root_lower': str(lo), 'root_upper': str(hi)})
    checks['four_accepted_19_1800_floors_rebound'] = True
    assert floors[21] == Q('0.001864696854799172')
    assert floors[22] == Q('0.00135251075726327')
    ceilings = {'TB-sharp': Q('0.0000037930'), 'sharpw': Q('0.0000028496'), 'graded': Q(25, 54684)}
    quoted = {7: ['1257', '1673', '10.43'], 21: ['491.6', '654.3', '4.078'], 22: ['356.5', '474.6', '2.958']}
    ratios = []
    for n, vals in quoted.items():
        for (name, b), text in zip(ceilings.items(), vals):
            ratio = floors[n] / b
            assert Q(text) <= ratio
            assert text in report, text
            ratios.append({'candidate': n, 'ceiling': name, 'ceiling_exact': str(b),
                           'lower_ratio_exact': str(ratio), 'quoted_lower_ratio': text,
                           'quoted_is_conservative': True})
    checks['nine_ratio_displays_conservative'] = True
    margins = {str(n): str(floors[n] - ceilings['graded']) for n in [16, 20, 21, 22]}
    assert Q('0.00101318') <= Q(margins['16']) < Q('0.00101319')
    assert Q('0.00139820') <= Q(margins['20']) < Q('0.00139821')
    checks['016_020_margin_displays_conservative'] = True
    diff = read(R / 'research/reference_difference/verification/C1-N1-022-legqs25-m16to23_minus_C1-N1-016-legqs25-quot013_2048_v4.json',
                '0ed0a3752073ca302f7737b121cdfecfc8b0bcec7ae8149a040f8262e0b686ac')
    assert diff['potential_prefix_equal']
    lo, hi = ball(diff['norm']['norm_ball'])
    assert Q('0.0088109875626067588') < lo < hi < Q('0.0088109875626067589')
    tau = Q(diff['norm']['tau_upper_exact'])
    assert hi < tau
    for row in diff['screens']:
        margin = Q(row['d_minus_b'])
        assert margin == floors[16] - Q(row['b'])
        assert lo > margin and tau > margin
        assert not row['tau_below_margin']
    checks['022_difference_computed_all_three_screens_fail'] = True
    assert 'this family is not yet checked' in report
    assert '(P) and tau are not yet computed.' in report
    assert 'N4-331: c1-n4 accepts T4-403 (022 structure' in report
    assert 'N4-325: under the general compatibility conditions (P)' in report
    assert 'the smallest 7.75277e-4' in report
    assert '023 (016 with 252 radius-100 functions' in report and 'No result is certified.' in ' '.join(report.split())
    checks['two_internal_stale_sentences_identified'] = True
    checks['every_registered_snapshot_margin_needs_certified_floor_scope'] = True
    shape = read(R / 'research/candidate022_shape_peer/verification/result.json',
                 '81f34093ebb36d8e4386696e2f53d2768d96a391f1530903988e3cc197d5f6bd')
    point = read(R / 'research/candidate022_peer/verification/result.json',
                 'c598de89cc54260b85c7bc3ff8572f796b8135fe143e774021c707f5e235cf2b')
    for d in [shape, point]:
        assert d['verdict'].startswith('CONFIRMED')
    checks['331_333_334_independent022_scope_accepted'] = True
    assembly = read(R / 'research/candidate016_registered_assembly/verification/result.json',
                    '5aa239d93ec070349790eb2f7845d5799367a0c94dc1db72525c0967a0cac823')
    assert assembly['no_full_plane_integral_computed_here']
    assert assembly['actual_component_acceptance'].startswith('OPEN')
    assert 'conditional arithmetic' in report and 'legacy X3 displayed ratio is REFUTED' in report
    checks['016_conditional_assembly_remains_conditional'] = True
    assert Q(999745, 2) == Q('499872.5')
    assert Q(1, 999745) < Q('0.00000100026')
    checks['two_endpoint_Newton_safe_roundings'] = True
    assert 'if K = 0 the majorant\nis linear and t* = eta' in report
    checks['zero_K_case_explicit'] = True
    out = {'utc': datetime.now(timezone.utc).isoformat(), 'report_sha256': prep['report_sha256'],
           'checks': checks, 'check_count': len(checks), 'source_entries': source_rows,
           'binding_counts': {s: sum(r['binding'] == s for r in source_rows) for s in sorted({r['binding'] for r in source_rows})},
           'inputs': inputs, 'floors': weak_rows, 'ratios': ratios, 'graded_margins_exact': margins,
           '022_difference': {'norm': diff['norm']['norm_ball'], 'tau_upper_exact': str(tau),
                             'independent_numerical_replay': 'OPEN', 'all_three_sufficient_screens_fail': True},
           'repairs': [
               {'section': '2.1 T4-369', 'verdict': 'REFUTED stale status', 'replacement': 'Abstract rank in T4-369; actual022 binding accepted by N4-321, T4-403 and N4-331.'},
               {'section': '5.6(e)', 'verdict': 'REFUTED stale status', 'replacement': '(P) and tau computed in N4-325; independent numerical replay OPEN; all three transfer screens fail.'},
               {'section': '5.6(d)', 'verdict': 'qualification required', 'replacement': 'Margins concern references with certified distance floors; registration alone supplies no floor (011 FLOAT, 023 untested at publication).'}],
           'ACK': 'Full published710-line report read. Section7 requested022 acceptance completed333/334. Section6 request1:023 next;016 independent norm production continues. No current closure target for R-TAIL or extra background hypotheses.',
           'foreign_code_executed': False, 'new_integrals_computed': False,
           'elapsed_seconds': time.monotonic() - start,
           'verdict': 'CONFIRMED checked numerical ratios, provenance and conditional scope; REFUTED two stale status sentences; margin scope qualification required; other theoretical statements not independently audited here'}
    p = B / 'verification/result.json'
    assert not p.exists()
    p.write_text(json.dumps(out, indent=2) + '\n')
    print(out['utc'], len(checks), 'checks', out['binding_counts'], 'SHA256', sha256(p.read_bytes()).hexdigest(), 'seconds', out['elapsed_seconds'])


if __name__ == '__main__':
    main()
