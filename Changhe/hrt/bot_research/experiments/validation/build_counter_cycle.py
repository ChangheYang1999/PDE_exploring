"""Construct an exact three-policy matrix from audited original-engine games."""
from __future__ import annotations
import argparse
from fractions import Fraction
import hashlib
import json
from pathlib import Path
from bot_research.experiments.validation.artifact_io import atomic_json
from bot_research.experiments.validation.final_validation import now


def digest(path):
    return hashlib.sha256(Path(path).read_bytes()).hexdigest()


def rational(value):
    value = Fraction(value)
    return {'numerator': value.numerator, 'denominator': value.denominator}


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('--audit', required=True)
    parser.add_argument('--replay-audit', required=True)
    parser.add_argument('--matrix', required=True)
    parser.add_argument('--certificate', required=True)
    args = parser.parse_args()
    audit = json.loads(Path(args.audit).read_text())
    replay = json.loads(Path(args.replay_audit).read_text())
    assert audit['valid_conditions'] == 18 and not audit['unresolved']
    assert replay['all_passed'] and replay['count'] == 18
    policies = ['economy13', 'guard_economy13', 'bluff_r3']
    specs = {}
    grouped = {}
    for case in audit['cases']:
        c = case['condition']
        specs.setdefault(c['candidate_id'], c['candidate_spec'])
        assert specs[c['candidate_id']] == c['candidate_spec']
        grouped.setdefault((c['candidate_id'], c['opponent_id']), []).append(case)
    assert set(grouped) == {(a, b) for a in policies for b in policies}
    matrix = []
    controls = []
    value = {'W': 1, 'D': 0, 'L': -1}
    for a in policies:
        row = []
        for b in policies:
            pair = grouped[(a, b)]
            assert sorted(c['condition']['candidate_side'] for c in pair) == [0, 1]
            assert len({c['canonical_replay_sha256'] for c in pair}) == 1
            row.append(Fraction(sum(value[c['outcome']] for c in pair), 2))
            controls.append({'row': a, 'column': b, 'hp_row_first': pair[0]['hp_candidate_first'],
                             'outcome': pair[0]['outcome'], 'rounds': pair[0]['rounds'],
                             'both_assignments_same_trajectory': True})
        matrix.append(row)
    assert matrix == [[0, -1, 1], [1, 0, -1], [-1, 1, 0]]
    for i, a in enumerate(policies):
        for j, b in enumerate(policies):
            assert matrix[i][j] == -matrix[j][i]
            # Reversing the named row/column also swaps the HP order.
            x = grouped[(a, b)][0]['hp_candidate_first']
            y = grouped[(b, a)][0]['hp_candidate_first']
            assert x == list(reversed(y))
    output = {'time_utc': now(), 'policies': policies, 'policy_specs': specs,
              'matrix': [[rational(v) for v in row] for row in matrix],
              'all_replays_passed': True, 'conditions': controls,
              'input_sha256': {p: digest(p) for p in (args.audit, args.replay_audit)},
              'checker_sha256': digest(__file__),
              'scope': 'Selected development counter cycle, standard initial state only. '
                       'A fixed finite empirical table, not a full-game equilibrium.'}
    atomic_json(args.matrix, output, exclusive=True)
    p = [Fraction(1, 3)] * 3
    margins = [sum(p[i] * matrix[i][j] for i in range(3)) for j in range(3)]
    certificate = {'time_utc': now(), 'policies': policies, 'matrix_path': args.matrix,
                   'matrix_sha256': digest(args.matrix), 'probabilities': [rational(v) for v in p],
                   'column_payoffs': [rational(v) for v in margins], 'exact_value': rational(0),
                   'scope': output['scope']}
    atomic_json(args.certificate, certificate, exclusive=True)
    print(json.dumps({'matrix': [[int(v) for v in row] for row in matrix],
                      'uniform_payoffs': [str(v) for v in margins], 'passed': True}))


if __name__ == '__main__':
    main()
