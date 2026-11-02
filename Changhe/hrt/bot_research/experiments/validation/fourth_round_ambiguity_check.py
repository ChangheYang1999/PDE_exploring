"""Protocol164: authenticated retained-game application; never load a policy.

The check command replays eight existing action histories with Engine. The
conditional continuation theorem is kept separate from measured premises.
"""
from copy import deepcopy
from datetime import datetime, timezone
from fractions import Fraction
from pathlib import Path
from urllib.parse import urlencode
import argparse
import gzip
import hashlib
import json
import time

from bot_research.experiments.validation.artifact_io import atomic_json, public_diagnostic
from bot_research.experiments.validation.replay_audit import audit_record_sequence, normalized
from bot_research.experiments.validation.required_sources import validate_required_sources
from bot_research.experiments.validation.source_closure import static_closure
from td_game.config import balanced_config
from td_game.engine import Engine

E = Path('bot_research/experiments/validation')
R = Path('bot_research/runs/validation')
A = E / 'analysis/fourth_round_ambiguity'
D = E / 'fourth-round-ambiguity-001.json'
SELF = E / 'fourth_round_ambiguity_check.py'
PARENTS = (
    E / 'analysis/delayed_signal_ambiguity/verification/full_check.json',
    E / 'analysis/blind_fourth_round/verification/full_games.json',
    E / 'analysis/fourth_round_wall_counter/verification/full_games.json',
)
PARENT_DECLARATIONS = (E / 'delayed-signal-ambiguity-001.json',
    E / 'blind-fourth-round-001.json', E / 'fourth-round-wall-counter-001.json')
ROOTS = {'G': 'bot_research.bots.counters.early_wall_guard',
         'U': 'bot_research.bots.counters.blind_fourth_round',
         'H': 'bot_research.bots.counters.hp_handoff',
         'V': 'bot_research.bots.counters.fourth_round_wall'}
DATA = ('early_wall_guard_001.json', 'maze_layouts_001.json',
        'screened_guard_001.json', 'screened_roster_guard_001.json',
        'staged_guards_001.json')
EDGE_KEYS = ('input_sha256', 'source_sha256', 'retained_input_sha256')


def now():
    return datetime.now(timezone.utc).isoformat()


def sha(raw):
    return hashlib.sha256(raw).hexdigest()


def stable(value):
    return sha(json.dumps(value, sort_keys=True, separators=(',', ':'), allow_nan=False).encode())


def specs():
    hp = dict(layout='empty', growth_rounds=6, bait=[], bait_round=2, tier='tier5',
              factory_cap=2000, purchase_cap=1000, replan_iters=5000,
              deadline=12, lead_from=8)
    query = lambda d: urlencode({k: json.dumps(v, separators=(',', ':')) for k, v in d.items()})
    return {'G': ROOTS['G'] + ':@make?' + query(dict(witness='guard00')),
            'U': ROOTS['U'] + ':@make', 'H': ROOTS['H'] + ':@make?' + query(hp),
            'V': ROOTS['V'] + ':@make'}


class Inputs:
    """Authenticate logical edges, resolving old sources only to bound archives."""
    def __init__(self):
        self.hashes, self.compressed, self.archives, self.aliases = {}, {}, {}, {}
        self.edges = 0

    def register(self, mapping):
        for name, digest in mapping.items():
            if not isinstance(name, str) or not isinstance(digest, str) or len(digest) != 64:
                raise ValueError('Malformed input hash edge.')
            pieces = name.split('/sources/')
            for index in range(1, len(pieces)):
                logical = '/sources/'.join(pieces[index:])
                self.archives.setdefault((logical, digest), set()).add(name)

    def raw(self, name):
        path = Path(name)
        if path.is_absolute() or '..' in path.parts:
            raise ValueError('Input path must be project relative.')
        if path.is_file():
            return path.read_bytes(), None
        packed_path = Path(str(path) + '.gz')
        packed = packed_path.read_bytes()
        raw = gzip.decompress(packed)
        return raw, dict(archive=str(packed_path), archive_sha256=sha(packed),
                         uncompressed_sha256=sha(raw), uncompressed_bytes=len(raw))

    def data(self, name, expected=None):
        name = str(name)
        candidates = [name] + sorted(self.archives.get((name, expected), ()))
        for candidate in dict.fromkeys(candidates):
            try:
                raw, packed = self.raw(candidate)
            except FileNotFoundError:
                continue
            digest = sha(raw)
            if expected is not None and digest != expected:
                continue
            if candidate in self.hashes and self.hashes[candidate] != digest:
                raise ValueError('Input drift: ' + candidate)
            self.hashes[candidate] = digest
            if packed:
                self.compressed[candidate] = packed
            if candidate != name:
                self.aliases[name + '@' + digest] = candidate
            return raw
        raise ValueError('Missing or changed exact input: ' + name)

    def edges_of(self, value):
        for key in EDGE_KEYS:
            mapping = value.get(key, {})
            self.register(mapping)
        for key in EDGE_KEYS:
            for name, digest in value.get(key, {}).items():
                self.data(name, digest)
                self.edges += 1

    def read(self, name, expected=None, edges=False):
        value = json.loads(self.data(name, expected))
        if edges:
            self.edges_of(value)
        return value

    def recheck(self):
        for name, digest in list(self.hashes.items()):
            raw, packed = self.raw(name)
            if sha(raw) != digest or packed != self.compressed.get(name):
                raise ValueError('Final input drift: ' + name)


def select(parents):
    chosen = []
    for side in (0, 1):
        filters = [
            (0, 'G', 'H', lambda c: c.get('member') == 'G' and c.get('opponent') == 'H' and c.get('member_side') == side),
            (1, 'U', 'H', lambda c: c.get('candidate') == 'U' and c.get('opponent') == 'H' and c.get('side') == side),
            (2, 'G', 'V', lambda c: c.get('candidate') == 'V' and c.get('opponent') == 'G' and c.get('side') == 1-side),
            (2, 'U', 'V', lambda c: c.get('candidate') == 'V' and c.get('opponent') == 'U' and c.get('side') == 1-side),
        ]
        for parent, arm, opponent, predicate in filters:
            matches = [c for c in parents[parent]['cases'] if predicate(c)]
            if len(matches) != 1:
                raise ValueError('Missing or duplicate full-spec role condition.')
            old = matches[0]
            if parent and not old.get('verified'):
                raise ValueError('Retained case did not pass its original audit.')
            chosen.append(dict(arm=arm, opponent=opponent, selector_side=side,
                               result=old['result'], parent=str(PARENTS[parent])))
    if len({c['result'] for c in chosen}) != 8:
        raise ValueError('Retained result reused for different conditions.')
    return chosen


def load_parents(inputs):
    values = [inputs.read(p) for p in PARENTS]
    declarations = [inputs.read(p) for p in PARENT_DECLARATIONS]
    for value in values + declarations:
        for key in EDGE_KEYS:
            inputs.register(value.get(key, {}))
    for value in values + declarations:
        inputs.edges_of(value)
    if not values[0].get('audit_completed_successfully') or not all(v.get('audit_completed') for v in values[1:]):
        raise ValueError('A parent audit is incomplete; scientific hypothesis failure alone is allowed.')
    expected = specs()
    for declaration, labels in zip(declarations, (('G', 'H'), ('U', 'H'), ('G', 'U', 'H', 'V'))):
        for label in labels:
            # H is not a declared opponent in163, but remains in its source closure.
            if label == 'H' and declaration is declarations[2]:
                continue
            if declaration['policies'][label]['spec'] != expected[label]:
                raise ValueError('Parent full policy specification mismatch: ' + label)
    return values


def authenticate_case(inputs, case):
    path = Path(case['result'])
    root = path.parent.parent
    row = inputs.read(path)
    freeze = inputs.read(root / 'freeze.json')
    archived = {str(root / 'sources' / p): h for p, h in freeze['source_sha256'].items()}
    inputs.register(archived)
    for p, h in archived.items():
        inputs.data(p, h)
    # The original archive, rather than today's audit helper, authenticates old code.
    inputs.edges_of(freeze)
    manifest = inputs.read(E / (root.name + '.json'), freeze['manifest_sha256'], edges=True)
    jobs = inputs.read(root / 'jobs.json')
    job = inputs.read(root / 'jobs' / (path.stem + '.json'))
    matches = [j for j in jobs if j['id'] == job['id']]
    if matches != [job]:
        raise ValueError('Original job receipt mismatch or duplication.')
    condition = row['condition']
    if condition != job['condition'] or row['bot_specs'] != job['names'] or row['replay_path'] != job['replay_path']:
        raise ValueError('Result/job identity mismatch.')
    if condition.get('initial_state') != 'standard' or condition.get('engine_seed') is not None or condition.get('pool') != 'development' or not condition.get('strength_score_eligible'):
        raise ValueError('Nonstandard or ineligible condition.')
    physical = [specs()[case['arm']], specs()[case['opponent']]]
    if case['selector_side']:
        physical.reverse()
    if job['bots'] != [{'spec': s} for s in physical]:
        raise ValueError('Exact full-spec physical-seat join failed.')
    candidate_side = condition['candidate_side']
    if condition['candidate_spec'] != physical[candidate_side] or condition['opponent_spec'] != physical[1-candidate_side]:
        raise ValueError('Candidate/opponent condition mismatch.')
    winner = row['result']['winner']
    expected_outcome = 'D' if winner is None else ('W' if winner == candidate_side else 'L')
    if row['candidate_outcome'] != expected_outcome:
        raise ValueError('Winner/outcome mismatch.')
    if any(row['bot_errors']) or any(row['rejected_actions']) or row['source_changed_during_match']:
        raise ValueError('Original match has an error, rejection or source drift.')
    for field in ('source_sha256', 'source_sha256_at_end'):
        loaded = row[field]
        if not loaded or any(freeze['source_sha256'].get(p) != h for p, h in loaded.items()):
            raise ValueError('Loaded source attestation mismatch.')
    validate_required_sources(row, job, freeze['source_sha256'])
    roots = {ROOTS[case['arm']], ROOTS[case['opponent']], ROOTS['H']}
    for p in static_closure(roots):
        if str(p).startswith(('td_game/', 'td_bots/', 'bot_research/bots/', 'bot_research/experiments/lead/')):
            digest = sha(inputs.data(p))
            if freeze['source_sha256'].get(str(p)) != digest:
                raise ValueError('Current policy/engine closure differs from original: ' + str(p))
    for name, digest in freeze['source_sha256'].items():
        if name.startswith('td_game/') or (name.startswith('bot_research/bots/counters/data/') and name.endswith('.json')):
            inputs.data(name, digest)
    audits = {}
    for kind in ('strict', 'replay', 'data', 'fresh'):
        audit = inputs.read(R / (root.name + '-' + kind + '.json'), edges=True)
        if kind == 'strict':
            passed = audit.get('valid_conditions') == len(jobs) and audit.get('attempt_counts') == {'valid': len(jobs)} and not audit.get('unresolved')
        else:
            passed = audit.get('all_passed') is True
        if not passed:
            raise ValueError('Original campaign audit incomplete: ' + kind)
        if kind == 'fresh':
            selected = [c for c in audit['cases'] if c.get('result') == str(path)]
            if len(selected) != 1 or not selected[0].get('exact'):
                raise ValueError('Missing exact original fresh reproduction.')
            rounds = selected[0]['rounds']
            if len(rounds) != row['rounds'] or any(len(r['calls']) != 2 or {c['side'] for c in r['calls']} != {0, 1} or not all(c['exact'] for c in r['calls']) for r in rounds):
                raise ValueError('Incomplete original external-call evidence.')
        audits[kind] = passed
    raw = inputs.data(row['replay_path'], row['trajectory_sha256'])
    records = [json.loads(line) for line in raw.splitlines()]
    return row, records, audits


def active_sources():
    paths = set(static_closure({'bot_research.experiments.validation.fourth_round_ambiguity_check'} | set(ROOTS.values())))
    paths.update(Path('bot_research/bots/counters/data') / name for name in DATA)
    paths.update((Path('td_game/balanced.json'), Path('configs/balanced.json')))
    return {str(p): sha(p.read_bytes()) for p in sorted(paths)}


def require_active(inputs, expected):
    current = active_sources()
    if current != expected:
        raise ValueError('Active executable or policy/data closure drift; archive fallback is forbidden.')
    for name, digest in expected.items():
        # Direct file bytes, not Inputs archive resolution, authenticate running code.
        if sha(Path(name).read_bytes()) != digest:
            raise ValueError('Active physical input changed: ' + name)
        inputs.data(name, digest)


def declare(review):
    inputs = Inputs()
    active = active_sources()
    require_active(inputs, active)
    parents = load_parents(inputs)
    cases = select(parents)
    for case in cases:
        authenticate_case(inputs, case)
    for p in static_closure({'bot_research.experiments.validation.fourth_round_ambiguity_check'} | set(ROOTS.values())):
        inputs.data(p)
    for name in DATA:
        inputs.data(Path('bot_research/bots/counters/data') / name)
    for name in ('td_game/balanced.json', 'configs/balanced.json'):
        inputs.data(name)
    prep = inputs.read(A / 'verification/source_preparation_003.json')
    inputs.edges_of(prep)
    if any(prep['input_sha256'].get(name) != digest for name, digest in active.items()):
        raise ValueError('Active sources differ from the reviewed preparation receipt.')
    for p in (A / 'PROOF.md', A / 'PROTOCOL.md', A / 'verification/source_inputs_001.json',
              E / 'reviews/fourth-round-ambiguity-proof-review-001.md', Path(review)):
        value = inputs.data(p)
        if str(p).endswith('source_inputs_001.json'):
            inputs.edges_of(json.loads(value))
    inputs.recheck()
    require_active(inputs, active)
    atomic_json(D, dict(declared_utc=now(), kind='Post-result retained-record application',
        new_games=0, policy_imports=0, policy_constructors=0, policy_decisions=0,
        source_review=review, active_source_sha256=active, policies={k: {'spec': v} for k, v in specs().items()}, cases=cases,
        input_sha256=inputs.hashes, compressed_inputs=inputs.compressed,
        archive_aliases=inputs.aliases, checked_input_edges=inputs.edges,
        scope='Eight existing games; normalized fixed-seat public prefix; conditional full-continuation payoff coupling remains an assumption.'), exclusive=True)
    print(json.dumps(dict(time_utc=now(), declared=True, cases=8, input_files=len(inputs.hashes))), flush=True)


def normalize_observation(obs, side):
    value = deepcopy(obs)
    for index in (0, 1):
        value['players'][index]['name'] = 'selector' if index == side else 'opponent'
    return value


def public_prefix(row, records, side, accounting):
    engine = Engine(balanced_config(), tuple(row['bot_specs']))
    observations, rounds = [], []
    for rnd in (1, 2, 3, 4):
        observations.append(normalize_observation(engine.observation(side), side))
        if rnd < 4:
            pair = records[2*rnd:2*rnd+2]
            if len(pair) != 2:
                raise ValueError('Retained game ended before the full three-round prefix.')
            actions = [[e['action'] for e in rec['event'] if e['kind'] == 'action'] for rec in pair]
            accounting['attempted_round_steps'] += 1
            generated = normalized(engine.play_round(actions))
            accounting['completed_round_steps'] += 1
            if generated != pair:
                raise ValueError('Opening replay mismatch.')
            accounting['exact_round_steps'] += 1
            pair = deepcopy(pair)
            for index in (0, 1):
                pair[index]['snapshot']['name'] = 'selector' if index == side else 'opponent'
            rounds.append(pair)
    return dict(observations=observations, rounds=rounds)


def opening_values(prefix, side):
    expected = [(100, 4, 40, 97, 5, 22), (175, 9, 40, 174, 9, 22), (267, 14, 42, 291, 17, 22)]
    errors = []
    for rnd, (pair, values) in enumerate(zip(prefix['rounds'], expected), 1):
        ours, theirs = pair[side]['snapshot'], pair[1-side]['snapshot']
        found = tuple(ours[k] for k in ('gold', 'n_factories', 'length_path')) + tuple(theirs[k] for k in ('gold', 'n_factories', 'length_path'))
        if found != values or any(p['snapshot']['hp'] != 800 or p['snapshot']['roster'] for p in pair):
            errors.append(dict(round=rnd, expected=list(values), actual=list(found), snapshots=[p['snapshot'] for p in pair]))
    return errors


def payoff(row, side):
    winner = row['result']['winner']
    return 0 if winner is None else (1 if winner == side else -1)


def first_difference(left, right, key='$'):
    if type(left) is not type(right):
        return dict(key=key, expected=left, actual=right)
    if isinstance(left, dict):
        if set(left) != set(right):
            return dict(key=key, expected_keys=sorted(left), actual_keys=sorted(right))
        for k in sorted(left):
            diff = first_difference(left[k], right[k], key + '.' + k)
            if diff:
                return diff
    elif isinstance(left, list):
        if len(left) != len(right):
            return dict(key=key, expected_length=len(left), actual_length=len(right))
        for i, (x, y) in enumerate(zip(left, right)):
            diff = first_difference(x, y, key + '[' + str(i) + ']')
            if diff:
                return diff
    elif left != right:
        return dict(key=key, expected=left, actual=right)
    return None


def rational_certificate(q):
    if q not in (-1, 0, 1):
        raise ValueError('Payoff q outside WDL range.')
    p, h, value = Fraction(2, q+3), Fraction(q+1, q+3), Fraction(q-1, q+3)
    if not (1-2*p == (q+1)*p-1 == -h+q*(1-h) == 2*h-1 == value):
        raise ValueError('Exact primal/dual equality failed.')
    return dict(q=q, probability_G=str(p), probability_H=str(h), value=str(value),
                optimal_probability_unique=q > -1, all_probabilities_optimal=q == -1,
                deterministic_worst_payoff=-1, primal_dual_equalities_verified=True)


def verdict(values, expected_count):
    return 'REFUTED' if any(v is False for v in values) else ('CONFIRMED' if len(values) == expected_count and all(values) else 'OPEN')


def check():
    begin = time.perf_counter()
    inputs = Inputs()
    declaration = inputs.read(D)
    require_active(inputs, declaration['active_source_sha256'])
    inputs.register(declaration['input_sha256'])
    inputs.edges_of(declaration)
    parents = load_parents(inputs)
    if declaration['cases'] != select(parents) or declaration['policies'] != {k: {'spec': v} for k, v in specs().items()}:
        raise ValueError('Declaration conditions changed.')
    checked, prefixes, errors = [], {}, []
    opening_accounting = dict(attempted_round_steps=0, completed_round_steps=0, exact_round_steps=0)
    for case in declaration['cases']:
        entry = dict(case, verified=False)
        try:
            row, records, audits = authenticate_case(inputs, case)
            audit = audit_record_sequence(row, records)
            side = case['selector_side']
            entry.update(verified=True, payoff=payoff(row, side), rounds=row['rounds'],
                hp_selector_first=row['hp'][::1 if side == 0 else -1], engine_replay=audit,
                original_audits=audits, original_candidate_side=row['condition']['candidate_side'])
            if row['rounds'] <= 3:
                # The complete terminal replay independently verified this failure
                # to reach decision four. It is an empirical contrary premise.
                entry.update(exact_opening=False, verified_early_terminal=True,
                             terminal_round=row['rounds'])
            else:
                try:
                    prefix = public_prefix(row, records, side, opening_accounting)
                    key = (case['arm'], case['opponent'], side)
                    failures = opening_values(prefix, side)
                    digest = stable(prefix)
                    prefixes[key] = prefix
                    entry.update(prefix_sha256=digest, exact_opening=not failures, opening_failures=failures)
                except Exception as exc:
                    # An unexpected audit exception is not a scientific refutation.
                    entry['opening_audit_error'] = public_diagnostic(str(exc))
                    errors.append(dict(result=case['result'], phase='opening reconstruction',
                                       error=entry['opening_audit_error']))
        except Exception as exc:
            entry['error'] = public_diagnostic(str(exc))
            errors.append(dict(result=case['result'], error=entry['error']))
        checked.append(entry)
        atomic_json(A / 'verification' / ('case-' + case['arm'] + '-' + case['opponent'] + '-side' + str(case['selector_side']) + '.json'), entry, exclusive=True)
    comparisons = []
    for side in (0, 1):
        reference = prefixes.get(('G', 'H', side))
        for arm, opponent in (('G', 'H'), ('U', 'H'), ('G', 'V'), ('U', 'V')):
            candidate = prefixes.get((arm, opponent, side))
            valid = reference is not None and candidate is not None
            diff = first_difference(reference, candidate) if valid else None
            comparisons.append(dict(arm=arm, opponent=opponent, selector_side=side,
                same_complete_normalized_prefix=(diff is None) if valid else None,
                first_difference=diff))
    h1_values = [c['same_complete_normalized_prefix'] for c in comparisons if c['same_complete_normalized_prefix'] is not None]
    h1_values += [c['exact_opening'] for c in checked if 'exact_opening' in c]
    h1 = verdict(h1_values, 16)
    matrices, certificates, premise_values = {}, {}, []
    for side in (0, 1):
        matrix = {a: {} for a in ('G', 'U')}
        for c in checked:
            if c['selector_side'] == side and c['verified']:
                matrix[c['arm']][c['opponent']] = c['payoff']
        matrices[str(side)] = matrix
        tests = []
        for arm, opponent, expected in (('G', 'H', -1), ('U', 'H', 1), ('U', 'V', -1)):
            if opponent in matrix[arm]:
                tests.append(matrix[arm][opponent] == expected)
        premise_values.extend(tests)
        q = matrix['G'].get('V')
        compatible = len(tests) == 3 and all(tests) and q in (-1, 0, 1)
        certificates[str(side)] = dict(measured_table_compatible=compatible,
            empirical_table_verdict=verdict(tests, 3),
            exact_certificate=rational_certificate(q) if compatible else None,
            continuation_coupling='ASSUMED, not established universally by retained histories')
    h2 = verdict(premise_values, 6)
    # Local fixtures use data only. They neither construct nor call any policy.
    for q in (-1, 0, 1):
        rational_certificate(q)
    fixture_checks = [bool(first_difference({'gold': 1}, {'gold': 2})),
        bool(first_difference([{'action': 'a'}, {'action': 'b'}], [{'action': 'b'}, {'action': 'a'}])),
        payoff({'result': {'winner': 0}}, 0) == 1 and payoff({'result': {'winner': 0}}, 1) == -1,
        payoff({'result': {'winner': None}}, 0) == payoff({'result': {'winner': None}}, 1) == 0]
    if not all(fixture_checks):
        raise ValueError('A data-only checker fixture failed.')
    integrity_errors = []
    try:
        inputs.recheck()
        require_active(inputs, declaration['active_source_sha256'])
    except Exception as exc:
        integrity_errors.append(dict(error=public_diagnostic(str(exc))))
        errors.extend(integrity_errors)
    tentative = None
    if integrity_errors:
        tentative = dict(hypotheses={'H1': h1, 'H2': h2}, matrices=deepcopy(matrices),
                         rational_certificates=deepcopy(certificates),
                         scope='Tentative local calculations only; global identity check failed.')
        h1 = h2 = 'OPEN'
        for item in certificates.values():
            item.update(measured_table_compatible=False, empirical_table_verdict='OPEN',
                        exact_certificate=None, integrity_invalidated=True)
    completed = len(checked) == 8 and all(c['verified'] for c in checked) and not errors
    application = completed and h1 == h2 == 'CONFIRMED'
    stamp = now()
    receipt = dict(time_utc=stamp, audit_completed_successfully=completed,
        all_passed=application, hypotheses={'H1': h1, 'H2': h2},
        measured_premises_compatible=application, conditional_theorem_status='PROVED under its stated hypotheses',
        full_continuation_coupling='OPEN as a universal property; assumed by the theorem',
        new_games=0, policy_imports=0, policy_constructors=0, policy_decisions=0,
        retained_games=8, complete_engine_replays=sum(c['verified'] for c in checked),
        additional_opening_replay_rounds=opening_accounting['completed_round_steps'],
        opening_replay_accounting=opening_accounting, cases=checked, comparisons=comparisons,
        matrices=matrices, rational_certificates=certificates,
        representative_prefixes={str(s): prefixes.get(('G', 'H', s)) for s in (0, 1)},
        all_prefix_sha256={str(k): stable(v) for k, v in prefixes.items()},
        errors=errors, integrity_errors=integrity_errors, tentative_before_integrity_check=tentative,
        active_source_sha256=declaration['active_source_sha256'], input_sha256=inputs.hashes, compressed_inputs=inputs.compressed,
        archive_aliases=inputs.aliases, checked_input_edges=inputs.edges,
        fixtures=['exact primal-dual equality for all three q', 'gold difference', 'action order', 'seat reversal', 'draw'],
        elapsed_seconds=time.perf_counter()-begin,
        scope='Post-result eight-game compatibility check; no new selector and no population or universal deadline claim.')
    lines = ['# Fourth-decision ambiguity: retained evidence', '', 'Checked UTC: ' + stamp + '.', '',
        'Audit completion: ' + str(completed) + '. H1 complete normalized prefix: ' + h1 + '. H2 required payoff entries: ' + h2 + '.', '',
        'Eight retained conditions were prescribed. The receipt preserves every audited outcome, role inversion, failure and missing premise. No policy was imported, constructed or called by this checker. Complete Engine replay uses only existing recorded actions.', '',
        '| Selector seat | G/H | U/H | G/V | U/V | Conditional value |', '| --- | ---: | ---: | ---: | ---: | --- |']
    for side in ('0', '1'):
        m = matrices[side]
        cert = certificates[side]['exact_certificate']
        lines.append('| ' + side + ' | ' + ' | '.join(str(m[a].get(o, 'OPEN')) for a, o in (('G','H'),('U','H'),('G','V'),('U','V'))) + ' | ' + (cert['value'] if cert else 'OPEN') + ' |')
    lines += ['', ('The measured premises are compatible with the conditional theorem.' if application else 'The prescribed empirical application is not established; inspect the hypothesis verdicts and retained failures.'), '',
        'Every displayed value still assumes correctly advanced member state and complete selected-continuation payoff coupling. Finite recorded games do not prove that future clock-limited planners reproduce the same continuation under different shadow work or load. Each physical seat has its own matrix and q. A failed measured payoff premise does not invalidate the conditional theorem.', '',
        'Selection is restricted to G or U after their common opening, with commitment by decision four using normalized identity-free public information. This is not a strength claim for a new selector, an impossibility theorem for other policies, or a held-out population result. Earlier private-state audits are authenticated retained evidence, not freshly rerun private transitions here.']
    with (A / 'RESULTS.md').open('x') as stream:
        stream.write('\n'.join(lines) + '\n')
    receipt['results_sha256'] = sha((A / 'RESULTS.md').read_bytes())
    atomic_json(A / 'verification/full_check.json', receipt, exclusive=True)
    print(json.dumps(dict(time_utc=stamp, audit_completed=completed, H1=h1, H2=h2, retained_games=8, policy_decisions=0)), flush=True)


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('command', choices=('declare', 'check'))
    parser.add_argument('--review')
    args = parser.parse_args()
    try:
        if args.command == 'declare':
            if not args.review:
                raise ValueError('A concrete source-review receipt is required.')
            declare(args.review)
        else:
            check()
    except Exception as exc:
        stamp = datetime.now(timezone.utc).strftime('%Y%m%dT%H%M%S%fZ')
        atomic_json(A / 'verification' / ('failure-' + args.command + '-' + stamp + '.json'),
            dict(time_utc=now(), command=args.command, audit_completed_successfully=False,
                 policy_decisions=0, error=public_diagnostic(str(exc))), exclusive=True)
        raise SystemExit(public_diagnostic(str(exc)))
