"""Declare and audit the finite Q/S wall-timing transfer comparison.

Declaration reads sources and prior evidence only. The check phase replays
recorded actions but never constructs or calls a policy. Fresh external-policy
checks are separate, explicitly declared check_fixed_game_histories jobs.
"""
from copy import deepcopy
from datetime import datetime, timezone
from pathlib import Path
from urllib.parse import urlencode
import argparse
import hashlib
import json
import time

from bot_research.experiments.validation.artifact_io import atomic_json, public_diagnostic
from bot_research.experiments.validation.source_closure import static_closure

E = Path('bot_research/experiments/validation')
R = Path('bot_research/runs/validation')
A = E / 'analysis/wall_timing_transfer'
D = E / 'wall-timing-transfer-001.json'
CANDIDATES = ['Q', 'S']
NEW_OPPONENTS = ['F44', 'F45', 'V29', 'V29_g1', 'V31_g1f', 'H']
OLD_OPPONENTS = ['G', 'N']
ORDER = NEW_OPPONENTS + OLD_OPPONENTS
AUDIT_KINDS = ('strict', 'replay', 'data', 'fresh')
DATA = [Path('bot_research/bots/counters/data') / name for name in (
    'early_wall_guard_001.json', 'maze_layouts_001.json', 'screened_guard_001.json',
    'screened_roster_guard_001.json', 'staged_guards_001.json')]
PRIOR = {
    'Q': (E / 'reserved-wall-counter-001.json',
          E / 'analysis/reserved_wall_counter/verification/full_games.json'),
    'S': (E / 'late-reserved-wall-counter-001.json',
          E / 'analysis/late_reserved_wall_counter/verification/full_games.json'),
}
RUNNER_ROOTS = {'bot_research.experiments.validation.' + name for name in (
    'wall_timing_transfer_check', 'wall_timing_transfer_pipeline',
    'run_data_development', 'isolated_match',
    'audit_development_strict', 'replay_audit', 'audit_data_archives',
    'check_fixed_game_histories', 'required_sources', 'source_closure')}


def now():
    return datetime.now(timezone.utc).isoformat()


def safe_path(path):
    path = Path(path)
    if path.is_absolute() or '..' in path.parts or not path.parts:
        raise ValueError('An evidence path must be project-relative.')
    return path


def sha(path):
    return hashlib.sha256(safe_path(path).read_bytes()).hexdigest()


def read(path):
    return json.loads(safe_path(path).read_text())


def require(condition, message):
    if not condition:
        raise ValueError(message)


def pin(path, pins, expected=None):
    path = safe_path(path)
    actual = sha(path)
    require(expected is None or actual == expected, 'Changed input: ' + str(path))
    require(str(path) not in pins or pins[str(path)] == actual,
            'Input changed during this invocation: ' + str(path))
    pins[str(path)] = actual
    return path


def checked_read(path, pins, expected=None):
    return read(pin(path, pins, expected))


def make_spec(module, **parameters):
    query = urlencode([(key, json.dumps(value, separators=(',', ':')))
                       for key, value in parameters.items()])
    return module + ':@make' + ('?' + query if query else '')


def policy_specs():
    econ = dict(free_fallback='zero', foreign_attack_from=11, doom='next',
                fac_cap=400, sat_reach=True, replan=True, foreign_sat_from=11,
                replan_gain=400, replan_base=True, own_in_layout='replan',
                own_min_s=1200, min_cap=3000, active_cap=4000, fill=True,
                fill_reserve=True, fill_threat=True)
    modules = 'bot_research.bots.'
    specs = {
        'Q': make_spec(modules + 'counters.reserved_wall_guard'),
        'S': make_spec(modules + 'counters.late_reserved_wall_guard'),
        'F44': make_spec(modules + 'defense.frozen.v44.fortress'),
        'F45': make_spec(modules + 'defense.frozen.v45.fortress'),
        'V29': make_spec(modules + 'economy.frozen.v29.econ29', **econ),
        'V29_g1': make_spec(modules + 'economy.frozen.v29.econ29', **econ, attack_from=7),
        'V31_g1f': make_spec(modules + 'economy.frozen.v31.econ31', **econ,
                            attack_from=7, fill_own=True),
        'H': make_spec(modules + 'counters.hp_handoff', layout='empty', growth_rounds=6,
                       bait=[], bait_round=2, tier='tier5', factory_cap=2000,
                       purchase_cap=1000, replan_iters=5000, deadline=12, lead_from=8),
        'G': make_spec(modules + 'counters.early_wall_guard', witness='guard00'),
        'N': make_spec('bot_research.experiments.lead.frozen.best_v9e',
                       attack_share=1.0, catch_up_share=0.5),
    }
    return {key: dict(id=key, spec=value) for key, value in specs.items()}


def identity(condition):
    return (condition['candidate_id'], condition['opponent_id'], condition['candidate_side'])


def validate_condition(condition, candidate, opponent, side, policies):
    expected = dict(candidate_id=candidate, opponent_id=opponent, candidate_side=side,
                    candidate_spec=policies[candidate]['spec'],
                    opponent_spec=policies[opponent]['spec'], initial_state='standard',
                    engine_seed=None, pool='development', strength_score_eligible=True)
    require(all(condition.get(key) == value for key, value in expected.items()),
            'Condition differs from the fixed policy/seat specification.')


def retained_controls(policies):
    """Pin original archives directly; never require old helpers to be current."""
    pins, controls = {}, []
    for candidate, (declaration_path, receipt_path) in PRIOR.items():
        old_declaration = checked_read(declaration_path, pins)
        receipt = checked_read(receipt_path, pins)
        require(receipt.get('all_passed') is True, 'Prior receipt did not complete its audits.')
        pin(declaration_path, pins, receipt['input_sha256'][str(declaration_path)])
        require(old_declaration['policies'][candidate] == policies[candidate],
                'Prior candidate specification differs.')
        for opponent in OLD_OPPONENTS:
            require(old_declaration['policies'][opponent] == policies[opponent],
                    'Prior opponent specification differs.')
            for side in (0, 1):
                matches = [case for case in receipt['cases']
                           if case['opponent'] == opponent and case['side'] == side]
                require(len(matches) == 1, 'Prior control is missing or duplicated.')
                case = matches[0]
                result_path = safe_path(case['result'])
                root = result_path.parent.parent
                row = checked_read(result_path, pins, receipt['input_sha256'][str(result_path)])
                freeze_path = root / 'freeze.json'
                freeze = checked_read(freeze_path, pins, receipt['input_sha256'][str(freeze_path)])
                jobs_path = root / 'jobs.json'
                checked_read(jobs_path, pins, receipt['input_sha256'][str(jobs_path)])
                job_path = root / 'jobs' / result_path.name
                checked_read(job_path, pins, receipt['input_sha256'][str(job_path)])
                replay_path = safe_path(row['replay_path'])
                pin(replay_path, pins, receipt['input_sha256'][str(replay_path)])
                validate_condition(row['condition'], candidate, opponent, side, policies)
                require(case['replay'] == str(replay_path), 'Prior replay path differs.')
                audit_paths = {}
                for kind in AUDIT_KINDS:
                    path = R / (root.name + '-' + kind + '.json')
                    pin(path, pins, receipt['input_sha256'][str(path)])
                    audit_paths[kind] = str(path)
                # Each pin addresses the original archived bytes. These are
                # retained separately, outside new campaign input_sha256 maps,
                # so run_data_development does not nest copies of old archives.
                for source, expected in freeze['source_sha256'].items():
                    pin(root / 'sources' / safe_path(source), pins, expected)
                # Reused Q/S and G/N must still mean the same policy code and
                # data, even though unrelated old checker sources may differ.
                policy_roots = {policies[key]['spec'].partition(':')[0]
                                for key in (candidate, opponent)}
                for source in set(static_closure(policy_roots)) | set(DATA):
                    require(freeze['source_sha256'].get(str(source)) == sha(source),
                            'Retained policy dependency differs: ' + str(source))
                controls.append(dict(candidate=candidate, opponent=opponent, side=side,
                    result=str(result_path), replay=str(replay_path), root=str(root),
                    declaration=str(declaration_path), receipt=str(receipt_path),
                    audits=audit_paths, original_archived_inputs=len(freeze['source_sha256'])))
    require(len(controls) == 8, 'Exactly eight retained controls are required.')
    return controls, pins


def declare(reviews):
    require(reviews, 'Supply at least one completed static review with --review.')
    policies = policy_specs()
    controls, retained = retained_controls(policies)
    modules = RUNNER_ROOTS | {policy['spec'].partition(':')[0] for policy in policies.values()}
    paths = set(static_closure(modules)) | set(DATA) | {
        A / 'PROOF.md', A / 'PROTOCOL.md', Path('td_game/balanced.json'), Path('configs/balanced.json')}
    paths.update(safe_path(path) for path in reviews)
    pins = {str(path): sha(path) for path in sorted(paths)}
    stamp = now()
    campaigns = []
    manifests = []
    for index in range(3):
        opponents = NEW_OPPONENTS[2 * index:2 * index + 2]
        name = f'wall-timing-transfer-{index:02d}-001'
        path = E / (name + '.json')
        manifest = dict(declared_utc=stamp, candidates=[policies[key] for key in CANDIDATES],
            opponents=[policies[key] for key in opponents], expected_conditions=8,
            additional_source_modules=sorted(RUNNER_ROOTS), input_sha256=pins,
            purpose='Selected Q/S timing transfer; standard start; no reserved D.')
        manifests.append((path, manifest))
        campaigns.append(dict(name=name, manifest=str(path), opponents=opponents, expected=8))
    require(not D.exists() and all(not path.exists() for path, _ in manifests),
            'Declaration paths already exist; never overwrite a declaration.')
    for path, manifest in manifests:
        atomic_json(path, manifest, exclusive=True)
    for campaign in campaigns:
        campaign['manifest_sha256'] = sha(campaign['manifest'])
    declaration = dict(declared_utc=stamp, protocol=160, new_games=24, retained_games=8,
        total_records=32, matched_conditions=16, new_policy_calls_before_declaration=0,
        prior_Q_S_calls_exist=True, policies=policies, candidates=CANDIDATES, order=ORDER,
        new_opponents=NEW_OPPONENTS, campaigns=campaigns, retained_controls=controls,
        input_sha256=pins, retained_input_sha256=retained, static_roots=sorted(modules),
        explicit_data=[str(path) for path in DATA], reviews=[str(safe_path(p)) for p in reviews],
        hypotheses={
            'H1': 'S WDL is at least Q WDL in every one of 16 fixed opponent/seat conditions.',
            'H2': 'Complete canonical histories agree in both seats for all 12 new policy pairs.',
            'H3': 'All 32 games reach round four and satisfy the exact opening and tier4 purchase.'},
        reuse_scope='Prior protocols 155 and 158; original archives retained directly; no new control policy calls.')
    atomic_json(D, declaration, exclusive=True)
    print(json.dumps(dict(time_utc=stamp, new_games=24, retained_games=8,
                         active_pins=len(pins), retained_pins=len(retained))), flush=True)


def verify_declaration(inputs):
    declaration = checked_read(D, inputs)
    require(declaration['policies'] == policy_specs(), 'Declared specifications changed.')
    require(declaration['new_games'] == 24 and declaration['total_records'] == 32,
            'Wrong declared size.')
    for field in ('input_sha256', 'retained_input_sha256'):
        for path, expected in declaration[field].items():
            pin(path, inputs, expected)
    for path in static_closure(set(declaration['static_roots'])):
        require(str(path) in declaration['input_sha256'], 'Static dependency absent from declaration.')
    for path in DATA:
        require(str(path) in declaration['input_sha256'], 'Explicit data absent from declaration.')
    for campaign in declaration['campaigns']:
        pin(campaign['manifest'], inputs, campaign['manifest_sha256'])
    return declaration


def canonical_records(records, side):
    """Keep all game fields except match labels and physical interleave indices."""
    rows = deepcopy(records)
    for row in rows:
        row.pop('match', None)
        row['player'] ^= side
        row['snapshot']['name'] = 'candidate' if row['player'] == 0 else 'opponent'
        for event in row['event']:
            event.pop('order', None)
        if row.get('result') is not None and row['result']['winner'] is not None:
            row['result']['winner'] ^= side
    rows.sort(key=lambda row: (row['round'], row['player']))
    return rows


def canonical_sha(records):
    return hashlib.sha256(json.dumps(records, sort_keys=True, separators=(',', ':'),
                                     allow_nan=False).encode()).hexdigest()


def opening_check(records, candidate, side, rounds, witness):
    walls = [dict(type='wall', x=x, y=y) for x, y in witness['walls']]
    turrets = witness['turrets']
    wall_actions = [dict(op='build_wall', x=x, y=y) for x, y in witness['walls']]
    turret_actions = [dict(op='build_turret', **turret) for turret in turrets]
    factory = dict(op='buy_factory')
    q = candidate == 'Q'
    expected = {
        1: dict(actions=[factory] * 5, gold=97, n_factories=5, length_path=22, buildings=[]),
        2: dict(actions=wall_actions + [factory] * 3 if q else [factory] * 4,
                gold=177 if q else 174, n_factories=8 if q else 9,
                length_path=40 if q else 22, buildings=walls if q else []),
        3: dict(actions=([] if q else wall_actions) + turret_actions + [factory] * (3 if q else 2),
                gold=264 if q else 261, n_factories=11, length_path=42, buildings=walls + turrets),
    }
    details, violations = [], []
    for rnd in range(1, 5):
        if rnd > rounds:
            violations.append(dict(round=rnd, reason='round_not_reached'))
            details.append(dict(round=rnd, reached=False))
            continue
        record = records[2 * rnd + side]
        events, snapshot = record['event'], record['snapshot']
        action_events = [event for event in events if event['kind'] == 'action']
        actions = [event['action'] for event in action_events]
        income = next(event for event in events if event['kind'] == 'income')
        combat = next(event for event in events if event['kind'] == 'combat')
        checks = {'all_actions_accepted': all(event['accepted'] for event in action_events)}
        if rnd <= 3:
            target = expected[rnd]
            checks.update(actions=actions == target['actions'], empty_roster=snapshot['roster'] == [],
                no_outgoing_hits=combat['outgoing_hits'] == 0,
                no_outgoing_spawns=combat['spawned'] == 0, no_hit_bounty=income['hits'] == 0)
            checks.update({key: snapshot[key] == value for key, value in target.items() if key != 'actions'})
            checks.update(path_income=income['path'] == target['length_path'],
                          factory_income=income['factories'] == 15 * target['n_factories'],
                          n_walls=snapshot['n_walls'] == sum(b['type'] == 'wall' for b in target['buildings']),
                          n_turrets=snapshot['n_turrets'] == sum(b['type'] != 'wall' for b in target['buildings']))
        else:
            checks.update(actions=actions == [dict(op='buy_minion', type='tier4')],
                purchase_cost=sum(event.get('cost', 0) for event in action_events) == 260,
                before_income_gold=snapshot['gold'] - income['total'] == (4 if q else 1),
                n_factories=snapshot['n_factories'] == 11, buildings=snapshot['buildings'] == walls + turrets,
                length_path=snapshot['length_path'] == 42,
                roster=snapshot['roster'] == [dict(id=0, type='tier4', bought_round=4,
                    expires_after_round=15, remaining_rounds=11)])
        violations.extend(dict(round=rnd, reason=key) for key, passed in checks.items() if not passed)
        details.append(dict(round=rnd, reached=True, actions=actions, snapshot=snapshot,
                            income=income, combat=combat, checks=checks))
    return dict(passed=not violations, reached_round_four=rounds >= 4,
                violations=violations, rounds=details)


def verify_archive(root, freeze, inputs, compare_current):
    for source, expected in freeze['source_sha256'].items():
        source_path = safe_path(source)
        pin(root / 'sources' / source_path, inputs, expected)
        if compare_current:
            pin(source_path, inputs, expected)


def audit_campaign(campaign, declaration, inputs):
    """Read all audit receipts and retain every problem instead of asserting success."""
    root = R / campaign['name']
    result = dict(name=campaign['name'], expected=8, errors=[], receipts={}, checked_calls=0)
    audits = {}
    for kind in AUDIT_KINDS:
        path = R / (campaign['name'] + '-' + kind + '.json')
        try:
            audit = checked_read(path, inputs)
            audits[kind] = audit
            result['receipts'][kind] = str(path)
            for field in ('input_sha256', 'inputs', 'source_sha256'):
                for source, expected in audit.get(field, {}).items():
                    pin(source, inputs, expected)
        except Exception as error:
            result['errors'].append(dict(stage=kind, diagnostic=public_diagnostic(str(error))))
    try:
        freeze = checked_read(root / 'freeze.json', inputs)
        require(freeze['manifest_sha256'] == campaign['manifest_sha256'], 'Campaign manifest mismatch.')
        for path, expected in declaration['input_sha256'].items():
            require(freeze['source_sha256'].get(path) == expected, 'Campaign omitted a declared input.')
        verify_archive(root, freeze, inputs, compare_current=True)
        jobs = checked_read(root / 'jobs.json', inputs)
        require(len(jobs) == 8, 'Campaign must contain eight jobs.')
        expected_keys = {(candidate, opponent, side) for candidate in CANDIDATES
                         for opponent in campaign['opponents'] for side in (0, 1)}
        require({identity(job['condition']) for job in jobs} == expected_keys, 'Campaign job grid differs.')
        for job in jobs:
            candidate, opponent, side = identity(job['condition'])
            validate_condition(job['condition'], candidate, opponent, side, declaration['policies'])
            require('prefixes' not in job, 'Only standard starts are declared.')
        result['jobs'] = jobs
        strict, replay, data, fresh = [audits[kind] for kind in AUDIT_KINDS]
        for receipt, module in ((strict, 'audit_development_strict'), (data, 'audit_data_archives')):
            checker_path = str(E / (module + '.py'))
            require(receipt['checker_sha256'] == declaration['input_sha256'][checker_path],
                    'Audit checker identity differs: ' + module)
        replay_roots = {'bot_research.experiments.validation.replay_audit'}
        for source in set(static_closure(replay_roots)) | {Path('td_game/balanced.json')}:
            require(replay['source_sha256'].get(str(source)) == declaration['input_sha256'][str(source)],
                    'Replay audit omitted a declared source.')
        for source, expected in freeze['source_sha256'].items():
            require(fresh['input_sha256'].get(source) == expected,
                    'Fresh policy audit omitted a frozen source.')
        require(strict['valid_conditions'] == strict['expected_conditions'] == 8, 'Strict count mismatch.')
        require(strict['attempt_counts'] == {'valid': 8} and not strict['unresolved']
                and not strict['repeat_disagreements'], 'Strict audit has failed or repeated attempts.')
        require(len(strict['attempts']) == len(strict['cases']) == 8, 'Strict receipt omits attempts.')
        expected_results = {str(root / 'results' / (job['id'] + '.json')) for job in jobs}
        require({case['result_path'] for case in strict['cases']} == expected_results,
                'Strict cases differ from campaign jobs.')
        require(replay['all_passed'] and replay['count'] == 8 and not replay['source_changed_during_run'],
                'External replay audit failed.')
        require(len(replay['cases']) == 8 and all(case['passed'] for case in replay['cases']),
                'External replay receipt has a failed or missing case.')
        replay_conditions = {identity(case['condition']) for case in replay['cases']}
        require(replay_conditions == expected_keys, 'External replay grid differs.')
        require(data['all_passed'] and len(data['campaigns']) == 1, 'Data audit failed or wrong campaign count.')
        data_case = data['campaigns'][0]
        require(data_case['campaign'] == str(root) and data_case['results'] == 8
                and data_case['all_passed'], 'Data audit is for a different campaign.')
        require(set(data_case['explicit_data']) >= {str(path) for path in DATA}, 'Missing explicit data audit.')
        require(fresh['games'] == 8 and all(fresh[key] for key in (
            'all_passed', 'all_replayed', 'all_actions_legal', 'all_observations_unchanged')),
            'Fresh policy audit failed.')
        require(len(fresh['cases']) == 8 and {case['result'] for case in fresh['cases']} == expected_results,
                'Fresh policy audit case grid differs.')
        counted = 0
        for case in fresh['cases']:
            row = checked_read(case['result'], inputs)
            require(case['condition'] == row['condition'] and case['exact'], 'Fresh case identity/actions differ.')
            require(len(case['rounds']) == row['rounds'], 'Fresh case omits a decision round.')
            for rnd, detail in enumerate(case['rounds'], 1):
                require(detail['round'] == rnd and len(detail['calls']) == 2,
                        'Fresh round numbering or call count differs.')
                require({call['side'] for call in detail['calls']} == {0, 1}
                        and all(call['exact'] for call in detail['calls']), 'Fresh external actions differ.')
                counted += 2
        require(fresh['checked_calls'] == counted, 'Fresh external call total differs.')
        result['checked_calls'] = counted
    except Exception as error:
        result['errors'].append(dict(stage='cross_receipt_checks', diagnostic=public_diagnostic(str(error))))
    result['passed'] = not result['errors']
    # Raw failed attempts remain in their hashed receipts; repeat them here for visibility.
    result['attempts'] = audits.get('strict', {}).get('attempts', [])
    result['unresolved'] = audits.get('strict', {}).get('unresolved', [])
    result['fresh_reported_calls'] = audits.get('fresh', {}).get('checked_calls')
    return result


def inspect_case(candidate, opponent, side, path, declaration, inputs, witness, retained=None):
    from bot_research.experiments.validation.compare_recorded_controls import checked_row
    from bot_research.experiments.validation.replay_audit import audit_record_sequence

    detail = dict(candidate=candidate, opponent=opponent, side=side, result=str(path),
                  origin='retained' if retained else 'new', audit_passed=False, errors=[])
    root = path.parent.parent
    failure = root / 'results' / (path.stem + '.failure.json')
    try:
        if failure.exists():
            detail['result_also_exists'] = path.exists()
            detail['errors'].append('A computational failure record exists for this declared attempt.')
            detail['failure_record'] = checked_read(failure, inputs)
        row = checked_read(path, inputs)
        validate_condition(row['condition'], candidate, opponent, side, declaration['policies'])
        job = checked_read(root / 'jobs' / path.name, inputs)
        jobs = checked_read(root / 'jobs.json', inputs)
        require(sum(item == job for item in jobs) == 1, 'Job receipt does not occur exactly once.')
        require(job['condition'] == row['condition'] and 'prefixes' not in job, 'Job condition differs.')
        expected_bots = [{'spec': declaration['policies'][candidate]['spec']},
                         {'spec': declaration['policies'][opponent]['spec']}]
        require(job['bots'] == (expected_bots if side == 0 else expected_bots[::-1]),
                'Job external-policy specifications differ.')
        require(job['names'] == ([candidate, opponent] if side == 0 else [opponent, candidate]),
                'Job public names differ.')
        require(row['bot_specs'] == job['names'], 'Result names differ from prescribed job.')
        require(row['replay_path'] == job['replay_path'], 'Replay path differs from job.')
        row_inputs = {}
        clean = checked_row(str(path), row_inputs)
        for source, expected in row_inputs.items():
            pin(source, inputs, expected)
        freeze = checked_read(root / 'freeze.json', inputs)
        if retained:
            verify_archive(root, freeze, inputs, compare_current=False)
            # Engine files are authoritative current rules and must also equal
            # the original archived engine used by this retained control.
            for source, expected in freeze['source_sha256'].items():
                if source.startswith('td_game/'):
                    pin(source, inputs, expected)
            old_receipt = checked_read(retained['receipt'], inputs)
            require(old_receipt['all_passed'], 'Retained receipt did not pass its original audits.')
            matching = [case for case in old_receipt['cases'] if case['result'] == str(path)]
            require(len(matching) == 1 and matching[0]['opponent'] == opponent
                    and matching[0]['side'] == side and matching[0]['outcome'] == clean['outcome']
                    and matching[0]['rounds'] == row['rounds'], 'Control is not the cited original case.')
            policy_roots = {declaration['policies'][key]['spec'].partition(':')[0]
                            for key in (candidate, opponent)}
            for source in set(static_closure(policy_roots)) | set(DATA):
                require(freeze['source_sha256'].get(str(source)) == sha(source),
                        'Retained policy dependency differs: ' + str(source))
            for kind, audit_path in retained['audits'].items():
                old_audit = checked_read(audit_path, inputs, old_receipt['input_sha256'][audit_path])
                if kind != 'strict':
                    require(old_audit['all_passed'], 'A retained audit did not pass.')
            detail['retained_receipt'] = retained['receipt']
            detail['original_archive_verified'] = True
        replay_path = pin(row['replay_path'], inputs, row['trajectory_sha256'])
        records = [json.loads(line) for line in replay_path.read_text().splitlines()]
        replay = audit_record_sequence(row, records)
        require(all(rec.get('result') is None for rec in records[:-2]) and
                records[-2]['result'] == records[-1]['result'] == row['result'] and
                row['result'] is not None, 'Terminal boundary differs.')
        opening = opening_check(records, candidate, side, row['rounds'], witness)
        canonical = canonical_records(records, side)
        detail.update(replay=str(replay_path), rounds=row['rounds'], outcome=clean['outcome'],
            hp_candidate_first=clean['hp_candidate_first'], terminal_replay=replay,
            opening=opening, canonical_replay_sha256=canonical_sha(canonical))
        detail['audit_passed'] = not detail['errors']
        return detail, canonical
    except Exception as error:
        detail['errors'].append(public_diagnostic(str(error)))
        return detail, None


def aggregate_verdict(values):
    if any(value is False for value in values):
        return 'REFUTED'
    if values and all(value is True for value in values):
        return 'CONFIRMED'
    return 'OPEN'


def check():
    started = time.perf_counter()
    inputs = {}
    declaration = verify_declaration(inputs)
    witness = next(w for w in read(DATA[0])['witnesses'] if w['id'] == 'guard00')
    cases, canonical, campaign_audits = [], {}, []
    for campaign in declaration['campaigns']:
        audit = audit_campaign(campaign, declaration, inputs)
        campaign_audits.append(audit)
        root = R / campaign['name']
        # Enumerate the declared grid even if jobs.json or all results are missing.
        index = 0
        for candidate in CANDIDATES:
            for opponent in campaign['opponents']:
                for side in (0, 1):
                    path = root / 'results' / f'case{index:04d}.json'
                    case, history = inspect_case(candidate, opponent, side, path,
                                                declaration, inputs, witness)
                    case['campaign_audits_passed'] = audit['passed']
                    case['verified'] = case['audit_passed'] and audit['passed']
                    cases.append(case)
                    canonical[candidate, opponent, side] = history
                    index += 1
    for control in declaration['retained_controls']:
        key = control['candidate'], control['opponent'], control['side']
        case, history = inspect_case(*key, safe_path(control['result']), declaration,
                                    inputs, witness, retained=control)
        case['verified'] = case['audit_passed']
        cases.append(case)
        canonical[key] = history
    require(len(cases) == 32 and len({(c['candidate'], c['opponent'], c['side']) for c in cases}) == 32,
            'The final accounting must retain all 32 unique cases.')
    by = {(case['candidate'], case['opponent'], case['side']): case for case in cases}
    comparisons = []
    for opponent in ORDER:
        for side in (0, 1):
            q, s = by['Q', opponent, side], by['S', opponent, side]
            usable = q['verified'] and s['verified']
            ranks = {'L': -1, 'D': 0, 'W': 1}
            passed = ranks[s['outcome']] >= ranks[q['outcome']] if usable else None
            comparisons.append(dict(opponent=opponent, side=side, Q=q['result'], S=s['result'],
                Q_outcome=q.get('outcome'), S_outcome=s.get('outcome'), verified=usable,
                S_never_lower=passed, origin=q['origin']))
    pairs = []
    for candidate in CANDIDATES:
        for opponent in NEW_OPPONENTS:
            x, y = by[candidate, opponent, 0], by[candidate, opponent, 1]
            usable = x['verified'] and y['verified']
            first, second = canonical[candidate, opponent, 0], canonical[candidate, opponent, 1]
            equal = first == second if usable else None
            divergence = None
            if equal is False:
                index = next((i for i in range(min(len(first), len(second)))
                              if first[i] != second[i]), min(len(first), len(second)))
                divergence = dict(index=index, seat0=first[index] if index < len(first) else None,
                                  seat1=second[index] if index < len(second) else None)
            pairs.append(dict(candidate=candidate, opponent=opponent, verified=usable,
                same_complete_history=equal, first_divergence=divergence,
                same_outcome=x.get('outcome') == y.get('outcome') if usable else None))
    h1 = aggregate_verdict([case['S_never_lower'] for case in comparisons])
    h2 = aggregate_verdict([pair['same_complete_history'] for pair in pairs])
    h3 = aggregate_verdict([case['opening']['passed'] if case['verified'] else None for case in cases])
    integrity_errors = []
    for path, expected in inputs.items():
        try:
            require(sha(path) == expected, 'Changed checked input: ' + path)
        except Exception as error:
            integrity_errors.append(public_diagnostic(str(error)))
    audits_complete = all(case['verified'] for case in cases) and not integrity_errors
    if integrity_errors:
        h1 = h2 = h3 = 'OPEN'
    fresh_calls = sum(audit['checked_calls'] for audit in campaign_audits)
    expected_calls = sum(2 * case['rounds'] for case in cases
                         if case['origin'] == 'new' and 'rounds' in case)
    if audits_complete:
        require(fresh_calls == expected_calls, 'Final fresh external call count differs.')
    hypotheses = dict(H1=h1, H2=h2, H3=h3)
    stamp = now()
    result = dict(time_utc=stamp, elapsed_seconds=time.perf_counter() - started,
        audit_completed=audits_complete, all_passed=audits_complete and all(v == 'CONFIRMED' for v in hypotheses.values()),
        hypotheses=hypotheses, new_games_declared=24, retained_games_declared=8,
        total_cases=32, matched_conditions=16, new_seat_pairs=12,
        verified_cases=sum(case['verified'] for case in cases), cases=cases,
        comparisons=comparisons, pairs=pairs, campaign_audits=campaign_audits,
        fresh_external_calls_verified=fresh_calls, fresh_external_calls_expected_from_new_records=expected_calls,
        current_checker_policy_calls=0, retained_control_new_policy_calls=0,
        complete_engine_replays=sum('terminal_replay' in case for case in cases),
        integrity_errors=integrity_errors, input_sha256=inputs,
        scope='Selected fixed standard-start comparison. Reused controls and paired assignments are not independent samples.')
    lines = ['# Wall timing transfer on eight fixed opponents', '', f'Checked {stamp}.', '',
        f'Audit completion: {"COMPLETE" if audits_complete else "INCOMPLETE"}. '
        f'Verified records: {result["verified_cases"]}/32. H1 {h1}; H2 {h2}; H3 {h3}.', '',
        'H1 compares S and Q separately in each of 16 opponent/seat conditions. '
        'H2 compares the two complete normalized histories for each of 12 new policy pairs. '
        'H3 requires all 32 games to reach round four and satisfy the declared opening. '
        'An early terminal result refutes H3, while a missing or unaudited result leaves its condition open.', '',
        '| Opponent | Seat | Q WDL, HP | S WDL, HP | S WDL at least Q | Evidence |',
        '| --- | ---: | --- | --- | --- | --- |']
    for comparison in comparisons:
        opponent, side = comparison['opponent'], comparison['side']
        cells = []
        for candidate in CANDIDATES:
            case = by[candidate, opponent, side]
            hp = case.get('hp_candidate_first')
            cells.append(case.get('outcome', 'unavailable') +
                         (f' {hp[0]}:{hp[1]}' if hp is not None else ''))
        verdict = aggregate_verdict([comparison['S_never_lower']])
        lines.append(f'| {opponent} | {side} | {cells[0]} | {cells[1]} | {verdict} | {comparison["origin"]} |')
    lines += ['', f'Fresh external decisions verified in the new campaign receipts: {fresh_calls}. '
        'This checker made zero policy calls and separately replayed recorded actions on the unchanged engine. '
        'The eight prior G/N controls retain their original source archives and receipts; they are not new games.', '',
        'Per-case opening violations, early terminal games, computational failures, audit errors and first '
        'paired-history divergences are retained in verification/full_games.json. '
        'A refuted hypothesis does not make a completed engine audit fail, and completed audits do not prove a hypothesis.', '',
        'The source proof establishes conditional opening arithmetic only. Opponent reactions, HP differences '
        'and later wall-clock cutoffs prevent an unconditional full-game equivalence theorem. '
        'These selected conditions establish no unseen-strength or global-optimality claim. '
        'The final candidate and reserved D inputs are unchanged.']
    with (A / 'RESULTS.md').open('x') as stream:
        stream.write('\n'.join(lines) + '\n')
    result['results_sha256'] = sha(A / 'RESULTS.md')
    atomic_json(A / 'verification/full_games.json', result, exclusive=True)
    print(json.dumps({key: result[key] for key in (
        'time_utc', 'audit_completed', 'all_passed', 'hypotheses',
        'verified_cases', 'fresh_external_calls_verified', 'complete_engine_replays')}), flush=True)
    return 0 if audits_complete else 2


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('mode', choices=['declare', 'check'])
    parser.add_argument('--review', action='append', default=[])
    args = parser.parse_args()
    if args.mode == 'declare':
        declare(args.review)
        return
    try:
        status = check()
    except Exception as error:
        # A top-level integrity/schema failure must leave an explicit durable
        # diagnostic without replacing any earlier attempt or success receipt.
        stamp = datetime.now(timezone.utc).strftime('%Y%m%dT%H%M%S%fZ')
        path = A / 'verification' / ('check-failure-' + stamp + '.json')
        atomic_json(path, dict(time_utc=now(), audit_completed=False,
            hypotheses=dict(H1='OPEN', H2='OPEN', H3='OPEN'),
            diagnostic=public_diagnostic(str(error)), checker_sha256=sha(Path(__file__).relative_to(Path.cwd()))
            if Path(__file__).is_absolute() else sha(__file__)), exclusive=True)
        print(json.dumps(dict(audit_completed=False, failure_receipt=str(path))), flush=True)
        raise SystemExit(2) from error
    raise SystemExit(status)


if __name__ == '__main__':
    main()
