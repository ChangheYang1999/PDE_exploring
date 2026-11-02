"""Build an empirical antisymmetric table from declared pairs and audited games."""
from collections import Counter, defaultdict
from fractions import Fraction
import argparse
import hashlib
import json
from pathlib import Path
from bot_research.experiments.validation.artifact_io import atomic_json
from bot_research.experiments.validation.final_validation import now


def digest(path):
    return hashlib.sha256(Path(path).read_bytes()).hexdigest()


def rational(value):
    value = Fraction(value)
    return dict(numerator=value.numerator, denominator=value.denominator)


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('--manifest', required=True)
    parser.add_argument('--strict', required=True)
    parser.add_argument('--replay', required=True)
    parser.add_argument('--output', required=True)
    args = parser.parse_args()
    manifest = json.loads(Path(args.manifest).read_text())
    strict = json.loads(Path(args.strict).read_text())
    replay = json.loads(Path(args.replay).read_text())
    policies = [p['id'] for p in manifest['policies']]
    specs = {p['id']: p['spec'] for p in manifest['policies']}
    n = len(policies)
    assert n > 1 and len(specs) == n
    assert not strict['unresolved'] and strict['valid_conditions'] == n*(n-1)
    assert not strict['repeat_disagreements']
    assert replay['all_passed'] and not replay['source_changed_during_run']
    assert replay['count'] == n*(n-1)
    replayed = {r['trajectory_sha256'] for r in replay['cases'] if r['passed']}
    hashes = {p: digest(p) for p in (args.manifest, args.strict, args.replay)}
    for p, h in manifest['input_sha256'].items():
        assert digest(p) == h, p
        hashes[p] = h
    groups = defaultdict(list)
    for case in strict['cases']:
        c = case['condition']
        a, b = c['candidate_id'], c['opponent_id']
        assert c['candidate_spec'] == specs[a] and c['opponent_spec'] == specs[b]
        assert policies.index(a) < policies.index(b)
        assert c['initial_state'] == 'standard' and c['engine_seed'] is None
        result = case['result_path']
        assert digest(result) == strict['input_sha256'][result]
        data = json.loads(Path(result).read_text())
        assert data['trajectory_sha256'] in replayed
        assert digest(data['replay_path']) == data['trajectory_sha256']
        hashes[result] = digest(result)
        hashes[data['replay_path']] = data['trajectory_sha256']
        groups[(a,b)].append(case)
    assert set(groups) == {(a,b) for i,a in enumerate(policies) for b in policies[i+1:]}
    a = [[Fraction(0) for _ in policies] for _ in policies]
    payoff = {'W': 1, 'D': 0, 'L': -1}
    reverse = {'W': 'L', 'D': 'D', 'L': 'W'}
    totals = {p:Counter() for p in policies}
    pairs = []
    for i, first in enumerate(policies):
        for j in range(i+1,n):
            second = policies[j]
            cases = sorted(groups[(first,second)], key=lambda c:c['condition']['candidate_side'])
            assert [c['condition']['candidate_side'] for c in cases] == [0,1]
            value = Fraction(sum(payoff[c['outcome']] for c in cases),2)
            a[i][j],a[j][i] = value,-value
            for c in cases:
                totals[first][c['outcome']] += 1
                totals[second][reverse[c['outcome']]] += 1
            pairs.append(dict(first=first,second=second,first_payoff=rational(value),
                same_normalized_trajectory=len({c['canonical_replay_sha256'] for c in cases})==1,
                same_outcome=len({c['outcome'] for c in cases})==1,
                games=[dict(side=c['condition']['candidate_side'],outcome=c['outcome'],
                    hp_first_policy_first=c['hp_candidate_first'],rounds=c['rounds'],
                    result_path=c['result_path'],runtime_seconds=c['runtime_seconds'],
                    canonical_replay_sha256=c['canonical_replay_sha256']) for c in cases]))
    assert all(sum(totals[p].values())==2*(n-1) for p in policies)
    output = dict(time_utc=now(), policies=policies, policy_specs=specs,
        matrix=[[rational(v) for v in row] for row in a], all_replays_passed=True,
        pairs=pairs, outcomes={p:dict(totals[p]) for p in policies},
        input_sha256=hashes, checker_sha256=digest(__file__),
        diagonal='Defined as zero; self-play was not run.',
        scope='The reverse entries reuse the same paired games with opposite payoff. This is an empirical finite game, not a full-game equilibrium or a future expectation for policies with clock-dependent decisions.')
    atomic_json(args.output, output, exclusive=True)
    print(json.dumps(dict(policies=policies,matrix=[[str(v) for v in row] for row in a],
                         outcomes=output['outcomes'],all_passed=True)))


if __name__ == '__main__':
    main()
