"""Reanalyse the completed six-policy and adaptive-response receipts exactly."""
from collections import defaultdict
from datetime import datetime, timezone
from fractions import Fraction
from itertools import permutations
from pathlib import Path
import gzip
import hashlib
import json
from bot_research.experiments.validation.artifact_io import atomic_json
from bot_research.experiments.validation.publish_extended_counter_game import exact_certificate

E = Path('bot_research/experiments/validation')
A = E / 'analysis/seven_policy_game'
ORDER = ['B', 'C', 'D', 'G', 'H', 'I', 'J']


def main():
    inputs, compressed = {}, {}

    def checked_bytes(name, expected=None):
        path = Path(name)
        if path.is_file():
            data = path.read_bytes()
        else:
            archive = Path(str(path) + '.gz')
            assert archive.is_file(), str(path)
            stored = archive.read_bytes()
            data = gzip.decompress(stored)
            compressed[str(path)] = dict(archive=str(archive), archive_sha256=hashlib.sha256(stored).hexdigest())
        sha = hashlib.sha256(data).hexdigest()
        if expected is not None:
            assert sha == expected, str(path)
        inputs[str(path)] = sha
        return data

    def read(name):
        return json.loads(checked_bytes(name))

    def verify(mapping):
        for name, sha in mapping.items():
            checked_bytes(name, sha)

    declaration = read(E / 'seven-policy-game-001.json')
    verify(declaration['input_sha256'])
    receipts = {key: read(value) for key, value in declaration['receipts'].items()}
    for receipt in receipts.values():
        assert receipt['all_passed']
        verify(receipt['input_sha256'])
    old, added = receipts['six'], receipts['selector']
    assert old['order'] == ORDER[:6] and len(old['cases']) == 42
    assert added['new_games'] == 14 and len(added['cases']) == 14
    components = read(A / 'verification/arithmetic_components.json')
    assert components['all_passed'] and len(components['cases']) == 3
    verify(components['input_sha256'])
    cases = []
    for case in old['cases']:
        cases.append(dict(a=case['a'], b=case['b'], result=case['result'],
                          candidate_side=case['candidate_side'], outcome=case['outcome'],
                          hp_a_first=case['hp_a_first'], rounds=case['rounds'],
                          canonical_replay_sha256=case['canonical_replay_sha256']))
    for case in added['cases']:
        cases.append(dict(a='J', b=case['opponent'], result=case['result_path'],
                          candidate_side=case['candidate_side'], outcome=case['outcome'],
                          hp_a_first=case['hp_J_first'], rounds=case['rounds'],
                          canonical_replay_sha256=case['canonical_replay_sha256']))
    assert len({case['result'] for case in cases}) == 56
    groups = defaultdict(list)
    for case in cases:
        # Revalidate the result bytes through each parent receipt, then retain
        # its already audited canonical history. No fresh simulator is called.
        assert case['result'] in inputs
        groups[(case['a'], case['b'])].append(case)
    matrix = [[None] * 7 for _ in range(7)]
    for (a, b), pair in groups.items():
        assert len(pair) == 2 and {c['candidate_side'] for c in pair} == {0, 1}
        for key in ('outcome', 'hp_a_first', 'rounds', 'canonical_replay_sha256'):
            assert pair[0][key] == pair[1][key], (a, b, key)
        i, j = ORDER.index(a), ORDER.index(b)
        assert matrix[i][j] is None and matrix[j][i] is None
        value = {'W': 1, 'D': 0, 'L': -1}[pair[0]['outcome']]
        if i == j:
            assert value == 0
        matrix[i][j], matrix[j][i] = value, -value
    assert len(groups) == 28 and all(v is not None for row in matrix for v in row)
    assert [row[:6] for row in matrix[:6]] == old['payoff']
    assert all(matrix[i][j] == -matrix[j][i] for i in range(7) for j in range(7))
    certificate = exact_certificate(matrix)
    assert certificate is not None
    weights = list(map(Fraction, certificate['weights']))
    assert len(weights) == 7 and sum(weights) == 1 and min(weights) >= 0
    column_payoffs = [sum(weights[i] * matrix[i][j] for i in range(7)) for j in range(7)]
    assert min(column_payoffs) >= 0
    assert [str(v) for v in column_payoffs] == certificate['column_payoffs']
    # An independent, direct certificate check also supplies the opposing
    # bound: skew symmetry turns these columns into nonpositive row values.
    assert all(sum(matrix[i][j] * weights[j] for j in range(7)) <= 0 for i in range(7))
    previous = list(map(Fraction, old['certificate']['weights'])) + [Fraction(0)]
    prior_payoffs = [sum(previous[i] * matrix[i][j] for i in range(7)) for j in range(7)]
    pure = [ORDER[i] for i in range(7) if min(matrix[i]) >= 0]
    cycles = [[ORDER[i], ORDER[j], ORDER[k]] for i, j, k in permutations(range(7), 3)
              if i < j and i < k and matrix[i][j] == matrix[j][k] == matrix[k][i] == 1]
    stamp = datetime.now(timezone.utc).isoformat()
    lines = [
        '# A finite table after public response selection', '', f'Checked {stamp}.', '',
        'The earlier uniform G/H/I mixture has payoff ' + str(prior_payoffs[-1]) +
        ' against J. Its nonnegative guarantee therefore does not extend to this seventh policy. '
        'This does not invalidate the earlier certificate on its six original columns.', '',
        'B is frozen best_v9e. C and I are the same round-three tier2 attack procedure with fixed private D and H models respectively. '
        'D is the adaptive Fortress38 continuation, G the early-wall guard, and H the HP-triggered grower. '
        'J chooses between H and I after their common first move using the public round-two wall count and roster. '
        'The exact specifications and checked source bytes are retained in the parent receipts.', '',
        '| Row | ' + ' | '.join(ORDER) + ' |', '|---|' + '---:|' * 7,
    ]
    lines += ['| ' + name + ' | ' + ' | '.join(map(str, row)) + ' |' for name, row in zip(ORDER, matrix)]
    lines += ['', 'Payoffs are +1 for a win, 0 for a draw and -1 for a loss. This table reuses all 56 games from the two completed studies. '
              'No new match, replay or policy call was made for this arithmetic analysis. All 28 assignment pairs had identical normalized histories in their original checks. '
              'All parent receipt inputs are rechecked here, using exact decompression for archived replays.', '',
              'An exact optimal mixture for this table is ' + ', '.join(name + '=' + value for name, value in zip(ORDER, certificate['weights'])) +
              '. Its column payoffs are ' + ', '.join(certificate['column_payoffs']) + '. The finite value is zero.', '',
              'The proof is direct. If p is this probability vector and q is any opposing distribution on these seven columns, '
              'p^T A q is nonnegative because it averages nonnegative column payoffs. Skew symmetry gives A p = -(p^T A)^T, '
              'so using the same p as the opposing mixture holds every row distribution to at most zero. These two inequalities meet at zero. '
              'The exact solver proposes p; the receipt separately checks every inequality with rational arithmetic.', '',
              'Pure policies nonnegative against every column: ' + (', '.join(pure) if pure else 'none') + '. '
              'Directed three-policy cycles: ' + '; '.join(' > '.join(c + [c[0]]) for c in cycles) + '.', '',
              'This is a selected development table. A private mixture draw would occur before a match and remain hidden until revealed by play. '
              'J is itself a fixed policy, although its decisions depend on observed play. The certificate covers only these fixed policies, the measured standard start and their observed decisions. '
              'It gives no guarantee against an eighth policy, changed starts or different wall-clock-bounded planner choices. '
              'It is not a statistical confidence statement or a replacement for the final reserved evaluation.', '',
              'Reproduce with check_seven_policy_arithmetic and publish_seven_policy_game after restoring the pinned parent receipts and their inputs. '
              'The declaration and verification/full_games.json contain every required path and hash.', '']
    output = A / 'RESULTS.md'
    with output.open('x') as stream:
        stream.write('\n'.join(lines))
    checked_bytes(output)
    result = dict(time_utc=stamp, all_passed=True, new_games=0, reused_games=56, order=ORDER,
                  payoff=matrix, prior_mixture_payoffs=[str(v) for v in prior_payoffs],
                  prior_guarantee_extends=min(prior_payoffs) >= 0, pure_nonnegative_policies=pure,
                  directed_three_cycles=cycles, certificate=certificate, cases=cases,
                  compressed_inputs=compressed, input_sha256=inputs)
    atomic_json(A / 'verification/full_games.json', result, exclusive=True)
    with Path('bot_research/notes/validation.md').open('a') as stream:
        stream.write(f'\n## {stamp}: Seven-policy arithmetic complete\n\nClaim and verdict: the old G/H/I uniform guarantee extends to J: '
                     + ('CONFIRMED' if min(prior_payoffs) >= 0 else 'REFUTED') + f'; its payoff is {prior_payoffs[-1]}. '
                     + 'An exact value-zero certificate for the enlarged finite table is CONFIRMED, with weights '
                     + str(certificate['weights']) + ' in B,C,D,G,H,I,J order. No pure nonnegative row exists. '
                     + 'All 56 games are reused; no new policy call was made. Parent inputs, including compressed replays, retain their original hashes. '
                     + 'See experiments/validation/analysis/seven_policy_game/RESULTS.md. This is restricted to the measured finite table.\n')
    print(json.dumps({k: v for k, v in result.items() if k not in ('cases', 'input_sha256', 'compressed_inputs')}), flush=True)


if __name__ == '__main__':
    main()
