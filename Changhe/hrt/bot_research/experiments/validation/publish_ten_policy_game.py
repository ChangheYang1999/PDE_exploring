"""Recheck all inputs, assemble the fixed ten-policy game and certify its value."""
from collections import defaultdict
from datetime import datetime, timezone
from fractions import Fraction
from itertools import permutations
from pathlib import Path
import gzip
import hashlib
import json
import time
from bot_research.experiments.validation.artifact_io import atomic_json
from bot_research.experiments.validation.compare_recorded_controls import checked_row
from bot_research.experiments.validation.finite_table_certificate import propose, verify as verify_certificate
from bot_research.experiments.validation.publish_extended_counter_game import norm
E = Path('bot_research/experiments/validation')
R = Path('bot_research/runs/validation')
A = E/'analysis/ten_policy_game'
ORDER = ['B', 'C', 'D', 'G', 'H', 'I', 'J', 'L', 'M', 'N']


def main():
    start = time.perf_counter()
    inputs, compressed = {}, {}
    def checked_bytes(name, expected=None):
        path = Path(name)
        if path.is_file():
            data = path.read_bytes()
        else:
            archive = Path(str(path)+'.gz')
            stored = archive.read_bytes()
            data = gzip.decompress(stored)
            compressed[str(path)] = dict(archive=str(archive), archive_sha256=hashlib.sha256(stored).hexdigest())
        digest = hashlib.sha256(data).hexdigest()
        assert expected is None or digest == expected, str(path)
        if str(path) in inputs:
            assert inputs[str(path)] == digest
        inputs[str(path)] = digest
        return data
    def read(path):
        return json.loads(checked_bytes(path))
    def verify_pins(mapping):
        for path, digest in mapping.items():
            checked_bytes(path, digest)
    declaration = read(E/'ten-policy-game-declaration-001.json')
    assert declaration['order'] == ORDER and declaration['new_games'] == 34 and declaration['reused_games'] == 76
    verify_pins(declaration['input_sha256'])
    verify_pins(declaration['parent_sha256'])
    old = read(E/'analysis/eight_policy_game/verification/full_games.json')
    assert old['all_passed'] and old['order'] == ORDER[:8] and len(old['cases']) == 72
    verify_pins(old['input_sha256'])
    for area, count in [('screened_roster_guarded_policy', 6), ('screened_guard_transfer', 24)]:
        parent = read(E/'analysis'/area/'verification/full_check.json')
        assert parent['new_games'] == count
        verify_pins(parent['input_sha256'])
    component = read(A/'verification/arithmetic_components.json')
    assert component['all_passed'] and len(component['cases']) == 4
    assert all(component['rejected_invalid_cases'].values())
    verify_pins(component['input_sha256'])
    policies = declaration['policies']
    cases = [dict(case, reused=True) for case in old['cases']]
    def append(a, b, filename, reused):
        row = checked_row(filename, inputs)
        condition = row['condition']
        assert norm(condition['candidate_spec']) == norm(policies[a]['spec'])
        assert norm(condition['opponent_spec']) == norm(policies[b]['spec'])
        cases.append(dict(a=a, b=b, result=filename, candidate_side=condition['candidate_side'],
                          outcome=row['outcome'], hp_a_first=row['hp_candidate_first'],
                          rounds=row['rounds'], canonical_replay_sha256=row['canonical_replay_sha256'],
                          reused=reused))
    for item in declaration['reused_extra']:
        append(item['a'], item['b'], item['result'], True)
    fresh_calls = 0
    for campaign in declaration['campaigns']:
        name, expected = campaign['name'], campaign['expected']
        root = R/name
        manifest = read(E/(name+'.json'))
        verify_pins(manifest['input_sha256'])
        audits = {k: read(R/(name+'-'+k+'.json')) for k in ('strict', 'replay', 'data', 'fresh')}
        strict = audits['strict']
        assert strict['valid_conditions'] == strict['expected_conditions'] == expected
        assert strict['attempt_counts'] == {'valid': expected}
        assert not strict['unresolved'] and not strict['repeat_disagreements']
        assert audits['replay']['all_passed'] and audits['replay']['count'] == expected
        assert audits['data']['all_passed']
        fresh = audits['fresh']
        assert fresh['games'] == expected
        assert all(fresh[k] for k in ('all_passed', 'all_replayed', 'all_actions_legal', 'all_observations_unchanged'))
        verify_pins(fresh['input_sha256'])
        fresh_calls += fresh['checked_calls']
        freeze = read(root/'freeze.json')
        verify_pins({str(root/'sources'/p): h for p, h in freeze['source_sha256'].items()})
        for job in read(root/'jobs.json'):
            append(campaign['a'], job['condition']['opponent_id'], str(root/'results'/(job['id']+'.json')), False)
    assert len(cases) == len({c['result'] for c in cases}) == 110
    assert sum(not c['reused'] for c in cases) == 34
    assert fresh_calls == sum(2*c['rounds'] for c in cases if not c['reused'])
    groups = defaultdict(list)
    for case in cases:
        assert case['result'] in inputs
        groups[(case['a'], case['b'])].append(case)
    matrix = [[None]*10 for _ in ORDER]
    for (a, b), pair in groups.items():
        assert len(pair) == 2 and {r['candidate_side'] for r in pair} == {0, 1}
        for key in ('outcome', 'hp_a_first', 'rounds', 'canonical_replay_sha256'):
            assert pair[0][key] == pair[1][key], (a, b, key)
        i, j = ORDER.index(a), ORDER.index(b)
        assert matrix[i][j] is None and matrix[j][i] is None
        value = {'W': 1, 'D': 0, 'L': -1}[pair[0]['outcome']]
        if i == j:
            assert value == 0
        matrix[i][j], matrix[j][i] = value, -value
    assert len(groups) == 55 and all(v is not None for row in matrix for v in row)
    assert [row[:8] for row in matrix[:8]] == old['payoff']
    previous = list(map(Fraction, old['certificate']['weights'])) + [Fraction(0)]*2
    assert previous == [Fraction(1, 5) if k in ('B', 'G', 'H', 'J', 'L') else Fraction(0) for k in ORDER]
    prior_payoffs = [sum(previous[i]*matrix[i][j] for i in range(10)) for j in range(10)]
    h1 = min(prior_payoffs[8:]) >= 0
    gaps = [matrix[9][j]-matrix[0][j] for j in range(8)]
    h2 = min(gaps) >= 0 and max(gaps) > 0
    certificate = propose(matrix)
    if certificate is not None:
        assert verify_certificate(matrix, certificate['weights'])
    pure = [ORDER[i] for i in range(10) if min(matrix[i]) >= 0]
    cycles = [[ORDER[i], ORDER[j], ORDER[k]] for i, j, k in permutations(range(10), 3)
              if i < j and i < k and matrix[i][j] == matrix[j][k] == matrix[k][i] == 1]
    stamp = datetime.now(timezone.utc).isoformat()
    result = dict(time_utc=stamp, runtime_seconds=time.perf_counter()-start, all_passed=True,
                  order=ORDER, policies=policies, payoff=matrix, new_games=34, reused_games=76,
                  fresh_calls=fresh_calls, assignment_pairs=55, h1=h1, h2=h2,
                  prior_mixture_payoffs=list(map(str, prior_payoffs)), N_minus_B=gaps,
                  certificate=certificate, pure_nonnegative_policies=pure,
                  directed_three_cycles=cycles, cases=cases, input_sha256=inputs,
                  compressed_inputs=compressed)
    lines = ['# Ten fixed policies after the screened counter', '', f'Checked {stamp}.', '',
             'M is the guarded screened-order counter with frozen Fortress38 continuation. N is AS1C, frozen best_v9e with attack_share=1.0 and catch_up_share=0.5. B,C,D,G,H,I,J,L retain the exact definitions in the preceding eight-policy table.', '',
             f'H1, the earlier uniform B/G/H/J/L mixture remains nonnegative against both additions: {"CONFIRMED" if h1 else "REFUTED"}. Its M and N column payoffs are {prior_payoffs[8]} and {prior_payoffs[9]}.',
             f'H2, N weakly improves on B against every old column and strictly improves somewhere: {"CONFIRMED" if h2 else "REFUTED"}. N minus B on B,C,D,G,H,I,J,L is {gaps}.', '',
             '| Row | '+' | '.join(ORDER)+' |', '| --- |'+' ---: |'*10]
    lines += ['| '+a+' | '+' | '.join(map(str, row))+' |' for a, row in zip(ORDER, matrix)]
    lines += ['', f'The table contains34 new games and76 reused records. All55 physical-assignment pairs have identical normalized complete histories. The new games pass strict accounting, unchanged-source/data checks, original-engine replay and {fresh_calls} fresh policy calls. Parent receipts and their inputs are rechecked, including exact decompression of older replays.', '']
    if certificate:
        lines += ['A verified rational certificate in B,C,D,G,H,I,J,L,M,N order is '+str(certificate['weights'])+'. Its exact column payoffs are '+str(certificate['column_payoffs'])+'. The finite value is zero. The proposal search is not claimed complete or the certificate unique.', '']
    else:
        lines += ['The proposal search did not produce a checked certificate. The certificate claim remains OPEN.', '']
    lines += ['Pure policies nonnegative against every column: '+(', '.join(pure) if pure else 'none')+'.',
              'Directed three-policy cycles: '+'; '.join(' > '.join(c+[c[0]]) for c in cycles)+'.', '',
              'This is selected development evidence on one start. Its34 new games are not34 independent population samples. Wall-clock cutoffs in some policies limit extrapolation from exact observed reproduction. A failure to extend an old mixture does not invalidate its earlier restricted certificate. No unrestricted equilibrium, general bot dominance or held-out claim follows. Final best.py and reserved pool D are unchanged.', '']
    with (A/'RESULTS.md').open('x') as stream:
        stream.write('\n'.join(lines))
    checked_bytes(A/'RESULTS.md')
    atomic_json(A/'verification/full_games.json', result, exclusive=True)
    with Path('bot_research/notes/validation.md').open('a') as stream:
        stream.write(f'\n## {stamp}: Ten-policy extension complete\n\nClaim and verdict: H1 old mixture extends to M/N {"CONFIRMED" if h1 else "REFUTED"}; H2 AS1C weakly improves on best_v9e across the eight old columns {"CONFIRMED" if h2 else "REFUTED"}. Method:34 new games,76 reused records,55 identical assignment pairs,{fresh_calls} fresh calls, exact rational certificate verification. Result: old mixture payoff versus M/N {prior_payoffs[8]}/{prior_payoffs[9]}; pure nonnegative policies {pure}. Full table and scope: experiments/validation/analysis/ten_policy_game/RESULTS.md. Selected development only; final bot and D unchanged.\n')
    print(json.dumps({k: result[k] for k in ('time_utc', 'runtime_seconds', 'new_games', 'fresh_calls', 'h1', 'h2', 'prior_mixture_payoffs', 'N_minus_B', 'certificate', 'pure_nonnegative_policies')}))


if __name__ == '__main__':
    main()
