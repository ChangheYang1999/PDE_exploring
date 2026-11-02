"""Check retained two-round ambiguity and its conditional restricted game.

No policy is instantiated. Replayed actions come from twelve existing records.
The optimization is exact rational arithmetic on a measured two-by-two matrix.
"""
from copy import deepcopy
from datetime import datetime, timezone
from fractions import Fraction
from pathlib import Path
import argparse
import gzip
import hashlib
import json
import time

from bot_research.experiments.validation.artifact_io import atomic_json
from bot_research.experiments.validation.final_validation_strict import read_result
from bot_research.experiments.validation.replay_audit import audit_record_sequence, normalized
from bot_research.experiments.validation.source_closure import static_closure
from td_game.config import balanced_config
from td_game.engine import Engine

E = Path('bot_research/experiments/validation')
A = E / 'analysis/delayed_signal_ambiguity'
D = E / 'delayed-signal-ambiguity-001.json'
PARENTS = [
    E / 'ten-policy-game-declaration-001.json',
    E / 'analysis/ten_policy_game/verification/full_games.json',
    E / 'two-round-wall-selector-001.json',
    E / 'analysis/two_round_wall_selector/verification/full_games.json',
    E / 'analysis/two_round_wall_selector/verification/context_supplement.json',
    E / 'late-reserved-wall-counter-001.json',
    E / 'analysis/late_reserved_wall_counter/verification/full_games.json',
]


def now():
    return datetime.now(timezone.utc).isoformat()


def sha(raw):
    return hashlib.sha256(raw).hexdigest()


class Inputs:
    def __init__(self):
        self.hashes = {}
        self.compressed = {}
        self.edges = 0

    def data(self, name, expected=None):
        path = Path(name)
        assert not path.is_absolute() and '..' not in path.parts, str(path)
        if path.is_file():
            raw = path.read_bytes()
        else:
            archive = Path(str(path) + '.gz')
            packed = archive.read_bytes()
            raw = gzip.decompress(packed)
            self.compressed[str(path)] = dict(archive=str(archive), archive_sha256=sha(packed))
        digest = sha(raw)
        assert expected is None or expected == digest, str(path)
        assert str(path) not in self.hashes or self.hashes[str(path)] == digest, str(path)
        self.hashes[str(path)] = digest
        return raw

    def read(self, name, edges=False):
        value = json.loads(self.data(name))
        if edges:
            for key in ('input_sha256', 'source_sha256'):
                for p, h in value.get(key, {}).items():
                    self.data(p, h)
                    self.edges += 1
        return value

    def recheck(self):
        for p, h in list(self.hashes.items()):
            self.data(p, h)


def selected_cases(ten, r, s):
    cases = []
    for member in ('G', 'L'):
        old = [c for c in ten['cases'] if (c['a'], c['b']) == (member, 'H')]
        assert len(old) == 2
        cases.extend(dict(member=member, opponent='H', result=c['result'], role='baseline') for c in old)
        new = [c for c in s['cases'] if c['opponent'] == member]
        assert len(new) == 2
        cases.extend(dict(member=member, opponent='S', result=c['result'], role='baseline') for c in new)
    rh = [c for c in r['cases'] if c['opponent'] == 'H']
    rs = [c for c in s['cases'] if c['opponent'] == 'R']
    assert len(rh) == len(rs) == 2
    cases.extend(dict(member='R', opponent='H', result=c['result'], role='selector control') for c in rh)
    cases.extend(dict(member='R', opponent='S', result=c['result'], role='selector control') for c in rs)
    assert len(cases) == len({c['result'] for c in cases}) == 12
    return cases


def declare():
    inputs = Inputs()
    parents = [inputs.read(p, edges=True) for p in PARENTS]
    ten, r, s = parents[1], parents[3], parents[6]
    assert all(p['all_passed'] for p in (ten, r, s))
    policies = {k: parents[2]['policies'][k] for k in ('G', 'L', 'H', 'R')}
    policies['S'] = parents[5]['policies']['S']
    for k in ('G', 'L', 'H'):
        assert policies[k] == parents[0]['policies'][k] == ten['policies'][k]
    cases = selected_cases(ten, r, s)
    for c in cases:
        path = Path(c['result'])
        row = inputs.read(path)
        root = path.parent.parent
        freeze = inputs.read(root / 'freeze.json', edges=True)
        for source, digest in freeze['source_sha256'].items():
            inputs.data(root / 'sources' / source, digest)
        inputs.data(root / 'jobs' / (path.stem + '.json'))
        inputs.data(row['replay_path'], row['trajectory_sha256'])
    roots = {'bot_research.experiments.validation.delayed_signal_ambiguity_check'}
    for p in static_closure(roots):
        inputs.data(p)
    for p in (A / 'PROOF.md', A / 'PROTOCOL.md',
              E / 'reviews/delayed-signal-ambiguity-review-001.md'):
        inputs.data(p)
    inputs.recheck()
    atomic_json(D, dict(declared_utc=now(), kind='Post-result analysis of already measured histories',
        new_games=0, policy_decisions=0, policies=policies, cases=cases,
        input_sha256=inputs.hashes, compressed_inputs=inputs.compressed,
        checked_input_edges=inputs.edges,
        limitations='Conditional continuation coupling; restricted G/L selection by round three; normalized names; not a population claim.'), exclusive=True)
    print(json.dumps(dict(time_utc=now(), cases=len(cases), inputs=len(inputs.hashes), policy_decisions=0)), flush=True)


def normalized_observation(obs, side):
    value = deepcopy(obs)
    for index in (0, 1):
        value['players'][index]['name'] = 'selector' if index == side else 'opponent'
    return value


def public_prefix(row, records, side):
    engine = Engine(balanced_config(), tuple(row['bot_specs']))
    observations, rounds = [], []
    for rnd in (1, 2, 3):
        observations.append(normalized_observation(engine.observation(side), side))
        if rnd < 3:
            pair = records[2 * rnd:2 * rnd + 2]
            actions = [[e['action'] for e in rec['event'] if e['kind'] == 'action'] for rec in pair]
            assert normalized(engine.play_round(actions)) == pair
            pair = deepcopy(pair)
            for index in (0, 1):
                pair[index]['snapshot']['name'] = 'selector' if index == side else 'opponent'
            rounds.append(pair)
    return dict(observations=observations, rounds=rounds)


def stable_digest(value):
    return sha(json.dumps(value, sort_keys=True, separators=(',', ':'), allow_nan=False).encode())


def payoff(row, side):
    winner = row['result']['winner']
    return 0 if winner is None else (1 if winner == side else -1)


def opening_values(prefix, side):
    expected = [(100, 4, 40, 97, 5, 22), (175, 9, 40, 174, 9, 22)]
    for pair, values in zip(prefix['rounds'], expected):
        ours, theirs = pair[side]['snapshot'], pair[1-side]['snapshot']
        found = tuple(ours[k] for k in ('gold', 'n_factories', 'length_path')) + tuple(theirs[k] for k in ('gold', 'n_factories', 'length_path'))
        if found != values or any(p['snapshot']['hp'] != 800 or p['snapshot']['roster'] for p in pair):
            return False
    return True


def check():
    begin = time.perf_counter()
    inputs = Inputs()
    declaration = inputs.read(D, edges=True)
    inputs.data(Path(__file__).relative_to(Path.cwd()))
    policies = declaration['policies']
    checked, prefixes = [], {}
    for case in declaration['cases']:
        path = Path(case['result'])
        root = path.parent.parent
        freeze = inputs.read(root / 'freeze.json', edges=True)
        for source, digest in freeze['source_sha256'].items():
            inputs.data(root / 'sources' / source, digest)
        job = inputs.read(root / 'jobs' / (path.stem + '.json'))
        inputs.data(path)
        row = read_result(path, job, freeze['source_sha256'])
        assert not any(row['bot_errors']) and not any(row['rejected_actions']) and not row['source_changed_during_match']
        assert row['condition']['initial_state'] == 'standard' and row['condition']['engine_seed'] is None
        candidate, opponent = (row['condition'][k] for k in ('candidate_spec', 'opponent_spec'))
        if candidate == policies[case['member']]['spec']:
            assert opponent == policies[case['opponent']]['spec']
            side = row['condition']['candidate_side']
        else:
            assert candidate == policies[case['opponent']]['spec'] and opponent == policies[case['member']]['spec']
            side = 1 - row['condition']['candidate_side']
        records = [json.loads(line) for line in inputs.data(row['replay_path'], row['trajectory_sha256']).splitlines()]
        audit = audit_record_sequence(row, records)
        assert row['rounds'] >= 3
        prefix = public_prefix(row, records, side)
        key = (case['member'], case['opponent'], side)
        assert key not in prefixes
        prefixes[key] = prefix
        checked.append(dict(**case, member_side=side, payoff=payoff(row, side),
            hp_member_first=row['hp'][::1 if side == 0 else -1], replay=audit,
            prefix_sha256=stable_digest(prefix), exact_opening_values=opening_values(prefix, side)))
    comparisons = []
    for side in (0, 1):
        reference = prefixes[('G', 'H', side)]
        for member, opponent in (('G','H'),('G','S'),('L','H'),('L','S'),('R','H'),('R','S')):
            comparisons.append(dict(member=member, opponent=opponent, side=side,
                same_complete_normalized_prefix=prefixes[(member, opponent, side)] == reference))
    h1 = all(c['same_complete_normalized_prefix'] for c in comparisons) and all(c['exact_opening_values'] for c in checked)
    expected = {'G': {'H': -1, 'S': 0}, 'L': {'H': 1, 'S': -1}}
    matrices = {}
    for side in (0, 1):
        matrices[str(side)] = {m: {o: next(c['payoff'] for c in checked if (c['member'],c['opponent'],c['member_side']) == (m,o,side)) for o in ('H','S')} for m in ('G','L')}
    h2 = all(m == expected for m in matrices.values())
    s_parent = inputs.read(PARENTS[-1], edges=True)
    r_parent = inputs.read(PARENTS[3], edges=True)
    h3 = len(s_parent['selector_traces']) == 2 and all(t['all_actions_agree'] and t['all_selected_values_agree'] for t in s_parent['selector_traces'])
    h3 = h3 and all(t['same_history'] for t in s_parent['transfers'])
    h3 = h3 and all(c['selected'] == 'L' and c['selection_round'] == 3 and c['same_selected_old_history'] for c in r_parent['cases'] if c['opponent'] == 'H')
    p, q, value = Fraction(2, 3), Fraction(1, 3), Fraction(-1, 3)
    rational = dict(probability_G=str(p), probability_H=str(q), value=str(value), verified=False)
    if h2:
        assert 1 - 2*p == p - 1 == -q == 2*q - 1 == value
        assert min(1, -1) == min(-1, 0) == -1
        rational['verified'] = True
    fixture = deepcopy(prefixes[('G', 'H', 0)])
    fixture['observations'][2]['players'][1]['gold'] += 1
    assert fixture != prefixes[('G', 'H', 0)]
    fixture = deepcopy(prefixes[('G', 'H', 0)])
    fixture['rounds'][0][0]['event'][0], fixture['rounds'][0][0]['event'][1] = fixture['rounds'][0][0]['event'][1], fixture['rounds'][0][0]['event'][0]
    assert fixture != prefixes[('G', 'H', 0)]
    assert payoff({'result': {'winner': 0}}, 0) == 1 and payoff({'result': {'winner': 0}}, 1) == -1
    assert payoff({'result': {'winner': None}}, 0) == payoff({'result': {'winner': None}}, 1) == 0
    stamp = now()
    lines = ['# Two indistinguishable opening rounds', '', f'Checked {stamp}.', '',
        f'H1 identical normalized public prefixes: {"CONFIRMED" if h1 else "REFUTED"}.',
        f'H2 the declared two-by-two payoff table in both physical seats: {"CONFIRMED" if h2 else "REFUTED"}.',
        f'H3 retained R/L state and complete-control checks: {"CONFIRMED" if h3 else "REFUTED"}.', '',
        'Twelve previously recorded games were replayed to their exact terminal boundaries on the unchanged engine: eight G/L baselines against H/S and four R controls. No policy was instantiated and no new match was run. Exact specifications, source/data hashes and recorded legal actions were checked. The first three observations and both completed early rounds were compared in each fixed physical seat after changing only player snapshot names; H1 above gives the outcome of that comparison.', '',
        '| Member | H, seat0 | H, seat1 | S, seat0 | S, seat1 |', '| --- | ---: | ---: | ---: | ---: |']
    for m in ('G', 'L'):
        lines.append('| ' + m + ' | ' + ' | '.join(str(matrices[str(side)][m][o]) for o,side in (('H',0),('H',1),('S',0),('S',1))) + ' |')
    lines.extend(['',
        ('The conditional theorem applies to this measured table: a selector restricted to committing to G or L by round three has value -1/3, uniquely at probability 2/3 of G, provided its selected continuation is coupled to reproduce the corresponding baseline payoff. The dual mixture puts probability 1/3 on H and 2/3 on S. These are exact rational equalities.' if h1 and h2 and h3 else 'At least one measured premise fails. The conditional theorem remains a theorem, but its empirical application is OPEN.'), '',
        'The public-prefix comparison uses direct engine replay. Logical member-state equality is evidence from the earlier R audits, whose retained bytes are checked here; it was not freshly rerun in this calculation. General continuation coupling is an explicit hypothesis, not an unconditional property established by these twelve histories. Wall-clock planning, extra shadow work or other scheduling changes may affect future decisions.', '',
        'The result is restricted to the stated opening, information set, two members and commitment deadline. Later commitment, a different opening, a third response, identity side channels or reselection falls outside the claim. Nothing here changes best_v9e or uses reserved D. Read PROOF.md, then PROTOCOL.md and verification/full_check.json.'])
    with (A / 'RESULTS.md').open('x') as f:
        f.write('\n'.join(lines) + '\n')
    inputs.data(A / 'RESULTS.md')
    inputs.recheck()
    atomic_json(A / 'verification/full_check.json', dict(time_utc=stamp, audit_completed_successfully=True, all_passed=h1 and h2 and h3,
        h1=h1, h2=h2, h3=h3, conditional_application=h1 and h2 and h3,
        new_games=0, policy_decisions=0, reused_games=12, cases=checked,
        comparisons=comparisons, representative_prefixes={str(side): prefixes[('G','H',side)] for side in (0,1)},
        matrices=matrices, rational_certificate=rational, input_sha256=inputs.hashes,
        compressed_inputs=inputs.compressed, checked_input_edges=inputs.edges,
        fixtures=['gold-sensitive prefix comparison', 'action-order-sensitive comparison', 'payoff perspective reversal', 'draw perspective'],
        elapsed_seconds=time.perf_counter()-begin), exclusive=True)
    print(json.dumps(dict(time_utc=stamp, h1=h1, h2=h2, h3=h3, reused_games=12, new_games=0, policy_decisions=0, inputs=len(inputs.hashes))), flush=True)


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('command', choices=('declare', 'check'))
    args = parser.parse_args()
    (declare if args.command == 'declare' else check)()
