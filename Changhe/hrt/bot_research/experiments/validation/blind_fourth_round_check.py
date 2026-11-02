"""Declare, journal fresh component audits, and publish the four-condition U control test.

Declare performs source/evidence reads only. Mechanism is the only mode here
that constructs or calls policies. Check replays recorded actions only.
"""
from copy import deepcopy
from datetime import datetime, timezone
from pathlib import Path
import argparse
import hashlib
import json
import os
import time

from bot_research.experiments.validation.artifact_io import atomic_json, public_diagnostic
from bot_research.experiments.validation.source_closure import static_closure
from bot_research.experiments.validation.wall_timing_transfer_check import (
    DATA, AUDIT_KINDS, now, safe_path, sha, read, require, pin, checked_read,
    make_spec, identity, validate_condition, verify_archive, canonical_records,
    canonical_sha, aggregate_verdict, inspect_case as inspect_original_case)

E = Path('bot_research/experiments/validation')
R = Path('bot_research/runs/validation')
A = E / 'analysis/blind_fourth_round'
D = E / 'blind-fourth-round-001.json'
NAME = 'blind-fourth-round-00-001'
ROOT = R / NAME
ORDER = ['H', 'S']
GRID = [('U', opponent, side) for opponent in ORDER for side in (0, 1)]
RUNNER_ROOTS = {'bot_research.experiments.validation.' + name for name in (
    'blind_fourth_round_check', 'blind_fourth_round_pipeline', 'run_data_development',
    'isolated_match', 'audit_development_strict', 'replay_audit', 'audit_data_archives',
    'check_fixed_game_histories', 'policy_value_snapshot', 'required_sources', 'source_closure')}
COUNTER_KEYS = ('actual_U', 'reference_G', 'reference_L4')
NESTED_KEYS = ('internal_G', 'internal_L4', 'internal_H_model', 'reference_H_model')


def policy_specs():
    stem = 'bot_research.bots.counters.'
    return {key: dict(id=key, spec=spec) for key, spec in {
        'U': make_spec(stem + 'blind_fourth_round'),
        'H': make_spec(stem + 'hp_handoff', layout='empty', growth_rounds=6, bait=[],
                       bait_round=2, tier='tier5', factory_cap=2000, purchase_cap=1000,
                       replan_iters=5000, deadline=12, lead_from=8),
        'S': make_spec(stem + 'late_reserved_wall_guard'),
        'T': make_spec(stem + 'third_round_wait'),
        'G': make_spec(stem + 'early_wall_guard', witness='guard00'),
    }.items()}


def retained_controls(policies):
    """Require completed T auditing, independently of its scientific verdicts."""
    pins, controls = {}, []
    declaration_path = E / 'third-round-wait-001.json'
    receipt_path = E / 'analysis/third_round_wait/verification/full_games.json'
    prior = checked_read(declaration_path, pins)
    receipt = checked_read(receipt_path, pins)
    require(prior['protocol'] == 161 and receipt['audit_completed'] is True,
            'Protocol161 controls require completed trustworthy auditing.')
    require(receipt['new_games_declared'] == 4 and receipt['verified_new_cases'] == 4,
            'Protocol161 did not verify all four declared T cases.')
    # Preserve every completed parent receipt edge, including original archives,
    # declaration, reviews, durable member audit and earlier retained controls.
    # Scientific H1-H4 truth is deliberately not a condition for retaining T.
    for p, h in receipt['input_sha256'].items():
        pin(p, pins, h)
    pin(declaration_path, pins, receipt['input_sha256'][str(declaration_path)])
    pin(E / 'analysis/third_round_wait/RESULTS.md', pins, receipt['results_sha256'])
    require(all(prior['policies'][k] == policies[k] for k in ('T', 'H', 'S', 'G')),
            'Original T/H/S/G specs differ.')
    root = R / 'third-round-wait-00-001'
    require(len(prior['campaigns']) == 1 and prior['campaigns'][0]['name'] == root.name,
            'Unexpected original T campaign.')
    old_campaign = prior['campaigns'][0]
    pin(old_campaign['manifest'], pins, old_campaign['manifest_sha256'])
    freeze_path = root / 'freeze.json'
    freeze = checked_read(freeze_path, pins, receipt['input_sha256'][str(freeze_path)])
    require(freeze['manifest_sha256'] == old_campaign['manifest_sha256'], 'Original freeze manifest differs.')
    for p, h in prior['input_sha256'].items():
        require(freeze['source_sha256'].get(p) == h, 'Original freeze omitted a declared source.')
    verify_archive(root, freeze, pins, compare_current=False)
    roots = {policies[k]['spec'].partition(':')[0] for k in ('T', 'H', 'S', 'G')}
    for source in set(static_closure(roots)) | set(DATA):
        require(freeze['source_sha256'].get(str(source)) == sha(source),
                'Original control policy/data dependency differs: ' + str(source))
    for source, expected in freeze['source_sha256'].items():
        if source.startswith('td_game/'):
            pin(source, pins, expected)
    audits = {}
    for kind in AUDIT_KINDS:
        audit_path = R / (root.name + '-' + kind + '.json')
        audit = checked_read(audit_path, pins, receipt['input_sha256'][str(audit_path)])
        if kind == 'strict':
            require(audit['valid_conditions'] == audit['expected_conditions'] == 4
                    and audit['attempt_counts'] == {'valid': 4} and not audit['unresolved'],
                    'Original T strict audit incomplete.')
        else:
            require(audit['all_passed'], 'Original T audit failed.')
        audits[kind] = str(audit_path)
    mechanism_path = R / (root.name+'-mechanism.json')
    member_audit = checked_read(mechanism_path, pins, receipt['input_sha256'][str(mechanism_path)])
    require(member_audit['all_passed'] and member_audit['audit_completed'], 'Original T member audit failed.')
    for index, (_, opponent, side) in enumerate(GRID):
        path = root / 'results' / f'case{index:04d}.json'
        matching = [c for c in receipt['cases'] if c['result'] == str(path)]
        require(len(matching) == 1 and matching[0]['candidate'] == 'T'
                and matching[0]['opponent'] == opponent and matching[0]['side'] == side
                and matching[0]['verified'], 'Original T case or physical side differs.')
        row = checked_read(path, pins, receipt['input_sha256'][str(path)])
        validate_condition(row['condition'], 'T', opponent, side, policies)
        for other in (root/'jobs.json', root/'jobs'/path.name, safe_path(row['replay_path'])):
            pin(other, pins, receipt['input_sha256'][str(other)])
        controls.append(dict(candidate='T', opponent=opponent, side=side, U_side=side,
            reference_side=side, result=str(path), replay=row['replay_path'], root=str(root),
            declaration=str(declaration_path), receipt=str(receipt_path), audits=audits,
            mechanism_receipt=str(mechanism_path)))
    return controls, pins


def declare(reviews):
    require(reviews, 'Supply a completed independent static review using --review.')
    policies = policy_specs()
    controls, retained = retained_controls(policies)
    modules = RUNNER_ROOTS | {p['spec'].partition(':')[0] for p in policies.values()}
    paths = set(static_closure(modules)) | set(DATA) | {
        A/'PROOF.md', A/'PROTOCOL.md', A/'INDEX.md', A/'verification/source_review.json',
        Path('td_game/balanced.json'), Path('configs/balanced.json')}
    paths.update(safe_path(p) for p in reviews)
    pins = {str(p): sha(p) for p in sorted(paths)}
    manifest_path = E / (NAME + '.json')
    require(not D.exists() and not manifest_path.exists(), 'Never replace an existing declaration.')
    stamp = now()
    manifest = dict(declared_utc=stamp, candidates=[policies['U']],
        opponents=[policies[k] for k in ORDER], expected_conditions=4,
        additional_source_modules=sorted(RUNNER_ROOTS), input_sha256=pins,
        purpose='Four selected U/H,S standard-start controls; no new retained T or reserved policy calls.')
    atomic_json(manifest_path, manifest, exclusive=True)
    campaign = dict(name=NAME, manifest=str(manifest_path), manifest_sha256=sha(manifest_path),
                    opponents=ORDER, expected=4)
    atomic_json(D, dict(declared_utc=stamp, protocol=162, new_games=4, retained_games=4,
        total_records=8, new_U_calls_before_declaration=0, policies=policies, order=ORDER,
        campaigns=[campaign], retained_controls=controls, input_sha256=pins,
        retained_input_sha256=retained, static_roots=sorted(modules),
        explicit_data=[str(p) for p in DATA], reviews=[str(safe_path(p)) for p in reviews],
        hypotheses=dict(H1='Both complete U/H histories equal matching-seat completed T/H histories.',
            H2='Both U/S cases reach round4 and satisfy exact Claim3 actions, states and private mechanism.',
            H3='T payoff is at least U payoff in all four matched opponent/physical-seat conditions.',
            H4='T payoff is strictly greater than U payoff against S in each physical seat.'),
        mechanism_scope='Only the four new U histories; references consume their actual observations. '
                        'No control T decisions or extra standalone H decisions.',
        fresh_scope='Ordinary both-policy fresh audit separately from additional U/reference-member audit.'), exclusive=True)
    print(json.dumps(dict(time_utc=stamp, new_games=4, retained_games=4,
                         active_pins=len(pins), retained_pins=len(retained))), flush=True)


def verify_declaration(inputs):
    declaration = checked_read(D, inputs)
    require(declaration['policies'] == policy_specs() and declaration['protocol'] == 162,
            'Declared policy specifications or protocol differ.')
    require(declaration['new_games'] == 4 and declaration['retained_games'] == 4
            and declaration['total_records'] == 8 and declaration['order'] == ORDER, 'Declared grid differs.')
    for field in ('input_sha256', 'retained_input_sha256'):
        for path, expected in declaration[field].items():
            pin(path, inputs, expected)
    for path in set(static_closure(set(declaration['static_roots']))) | set(DATA):
        require(str(path) in declaration['input_sha256'], 'Unpinned active source/data: ' + str(path))
    require(len(declaration['campaigns']) == 1, 'Exactly one new campaign is declared.')
    campaign = declaration['campaigns'][0]
    require(campaign['name'] == NAME and campaign['opponents'] == ORDER and campaign['expected'] == 4,
            'Campaign identity differs.')
    manifest = checked_read(campaign['manifest'], inputs, campaign['manifest_sha256'])
    require(manifest['input_sha256'] == declaration['input_sha256']
            and manifest['candidates'] == [declaration['policies']['U']]
            and manifest['opponents'] == [declaration['policies'][k] for k in ORDER], 'Manifest grid differs.')
    require([(c['candidate'], c['opponent'], c['side'], c['U_side'], c['reference_side'])
             for c in declaration['retained_controls']]
            == [('T', opponent, side, side, side) for opponent in ORDER for side in (0, 1)],
            'Retained T matching physical-side grid differs.')
    return declaration


def finish_hashes(inputs):
    errors = []
    for path, expected in inputs.items():
        try:
            require(sha(path) == expected, 'Changed checked input: ' + path)
        except Exception as error:
            errors.append(public_diagnostic(str(error)))
    return errors


def actions(record):
    return [event['action'] for event in record['event'] if event['kind'] == 'action']


def opening_check(records, opponent, side, rounds, witness):
    """The exact successful-call opening claims, independently from policy traces."""
    factory = dict(op='buy_factory')
    wall_actions = [dict(op='build_wall', x=x, y=y) for x, y in witness['walls']]
    walls = [dict(type='wall', x=x, y=y) for x, y in witness['walls']]
    splash = dict(type='splash', x=1, y=3)
    splash_action = dict(op='build_turret', **splash)
    h_splash = dict(type='splash', x=10, y=1)
    u_actions = [wall_actions + [factory] * 4, [factory] * 5,
                 [splash_action] + [factory] * 5,
                 ([dict(op='buy_minion', type='tier2')] * 6 + [factory]
                  if opponent == 'H' else [factory] * 13)]
    o_actions = [[factory] * 5, [factory] * 4,
                 [factory] * 8 if opponent == 'H' else wall_actions + [splash_action] + [factory] * 2,
                 [dict(op='build_turret', **h_splash)] + [factory] * 11
                 if opponent == 'H' else [dict(op='buy_minion', type='tier4')]]
    u_values = [(100, 4, 40, 800), (175, 9, 40, 800), (267, 14, 42, 800),
                (304, 15, 42, 800) if opponent == 'H' else (454, 27, 42, 740)]
    o_values = [(97, 5, 22, 800), (174, 9, 22, 800),
                (291, 17, 22, 800) if opponent == 'H' else (261, 11, 42, 800),
                (453, 28, 22, 728) if opponent == 'H' else (213, 11, 42, 800)]
    violations, details = [], []
    for rnd in range(1, 5):
        if rnd > rounds:
            violations.append(dict(round=rnd, reason='round_not_reached'))
            details.append(dict(round=rnd, reached=False))
            continue
        round_details = []
        for role, physical in enumerate((side, 1-side)):
            record = records[2*rnd + physical]
            snapshot = record['snapshot']
            gold, factories, length, hp = (u_values if role == 0 else o_values)[rnd-1]
            buildings = (walls + ([] if rnd < 3 else [splash])) if role == 0 else (
                ([] if rnd < 4 else [h_splash]) if opponent == 'H' else
                ([] if rnd < 3 else walls + [splash]))
            roster = []
            if rnd == 4 and ((opponent == 'H' and role == 0) or (opponent == 'S' and role == 1)):
                kind = 'tier2' if opponent == 'H' else 'tier4'
                roster = [dict(id=i, type=kind, bought_round=4, expires_after_round=15, remaining_rounds=11)
                          for i in range(6 if kind == 'tier2' else 1)]
            expected = dict(gold=gold, n_factories=factories, length_path=length, hp=hp,
                            buildings=buildings, roster=roster,
                            n_walls=sum(b['type'] == 'wall' for b in buildings),
                            n_turrets=sum(b['type'] != 'wall' for b in buildings))
            income = next(e for e in record['event'] if e['kind'] == 'income')
            combat = next(e for e in record['event'] if e['kind'] == 'combat')
            hits = 0 if rnd < 4 else ((6 if role == 0 else 0) if opponent == 'H' else role)
            incoming = 0 if rnd < 4 else ((0 if role == 0 else 6) if opponent == 'H' else 1-role)
            dealt = hits * (12 if opponent == 'H' else 60)
            damaged = incoming * (12 if opponent == 'H' else 60)
            checks = dict(actions=actions(record) == (u_actions if role == 0 else o_actions)[rnd-1],
                all_actions_accepted=all(e['accepted'] for e in record['event'] if e['kind'] == 'action'),
                snapshot={k: v for k, v in snapshot.items() if k != 'name'} == expected,
                income=income == dict(kind='income', path=length, factories=factories*15,
                                     hits=hits*5, total=length+factories*15+hits*5),
                combat=all(combat[k] == value for k, value in dict(outgoing_hits=hits,
                    incoming_hits=incoming, damage_dealt=dealt, base_damage=damaged,
                    spawned=hits, killed=0, cleared=0).items()))
            violations.extend(dict(round=rnd, role=role, reason=k) for k, good in checks.items() if not good)
            round_details.append(dict(role=role, actions=actions(record), snapshot=snapshot,
                                      income=income, combat=combat, checks=checks))
        details.append(dict(round=rnd, reached=True, players=round_details))
    return dict(passed=not violations, reached_round_four=rounds >= 4,
                violations=violations, rounds=details)


def inspect_new_case(index, declaration, inputs, witness):
    candidate, opponent, side = GRID[index]
    path = ROOT / 'results' / f'case{index:04d}.json'
    detail, history = inspect_original_case(candidate, opponent, side, path, declaration, inputs, witness)
    if history is not None:
        records = [json.loads(s) for s in safe_path(detail['replay']).read_text().splitlines()]
        detail['opening'] = opening_check(records, opponent, side, detail['rounds'], witness)
    return detail, history


def audit_campaign(declaration, inputs):
    campaign = declaration['campaigns'][0]
    result = dict(name=NAME, expected=4, errors=[], receipts={}, checked_calls=0)
    audits = {}
    for kind in AUDIT_KINDS:
        path = R / (NAME + '-' + kind + '.json')
        try:
            audit = checked_read(path, inputs)
            audits[kind] = audit
            result['receipts'][kind] = str(path)
            for field in ('input_sha256', 'inputs', 'source_sha256'):
                for p, h in audit.get(field, {}).items():
                    pin(p, inputs, h)
        except Exception as error:
            result['errors'].append(dict(stage=kind, diagnostic=public_diagnostic(str(error))))
    try:
        freeze = checked_read(ROOT / 'freeze.json', inputs)
        require(freeze['manifest_sha256'] == campaign['manifest_sha256'], 'Freeze manifest differs.')
        for p, h in declaration['input_sha256'].items():
            require(freeze['source_sha256'].get(p) == h, 'Freeze omitted a declared active input.')
        verify_archive(ROOT, freeze, inputs, compare_current=True)
        jobs = checked_read(ROOT / 'jobs.json', inputs)
        require(len(jobs) == 4 and [identity(job['condition']) for job in jobs] == GRID, 'Four-job order differs.')
        for job in jobs:
            validate_condition(job['condition'], *identity(job['condition']), declaration['policies'])
            require('prefixes' not in job, 'Only standard starts are declared.')
        strict, replay, data, fresh = [audits[k] for k in AUDIT_KINDS]
        for receipt, module in ((strict, 'audit_development_strict'), (data, 'audit_data_archives')):
            require(receipt['checker_sha256'] == declaration['input_sha256'][str(E / (module+'.py'))],
                    'Audit checker source differs.')
        for p in set(static_closure({'bot_research.experiments.validation.replay_audit'})) | {Path('td_game/balanced.json')}:
            require(replay['source_sha256'].get(str(p)) == declaration['input_sha256'][str(p)], 'Replay source edge absent.')
        for p, h in freeze['source_sha256'].items():
            require(fresh['input_sha256'].get(p) == h, 'Fresh source edge absent.')
        require(strict['valid_conditions'] == strict['expected_conditions'] == 4
                and strict['attempt_counts'] == {'valid': 4} and not strict['unresolved']
                and not strict['repeat_disagreements'], 'Strict attempt accounting failed.')
        require(len(strict['attempts']) == len(strict['cases']) == 4, 'Strict omitted attempts.')
        expected_paths = {str(ROOT / 'results' / (job['id']+'.json')) for job in jobs}
        require({c['result_path'] for c in strict['cases']} == expected_paths, 'Strict cases differ.')
        require(replay['all_passed'] and replay['count'] == 4 and not replay['source_changed_during_run']
                and len(replay['cases']) == 4 and all(c['passed'] for c in replay['cases'])
                and {identity(c['condition']) for c in replay['cases']} == set(GRID), 'Replay cases differ or fail.')
        require(data['all_passed'] and len(data['campaigns']) == 1, 'Data audit failed.')
        dc = data['campaigns'][0]
        require(dc['campaign'] == str(ROOT) and dc['results'] == 4 and dc['all_passed']
                and set(dc['explicit_data']) >= {str(p) for p in DATA}, 'Data campaign/count/certificates differ.')
        require(fresh['games'] == 4 and all(fresh[k] for k in (
            'all_passed', 'all_replayed', 'all_actions_legal', 'all_observations_unchanged')),
            'Fresh audit failed.')
        require(len(fresh['cases']) == 4 and {c['result'] for c in fresh['cases']} == expected_paths,
                'Fresh cases differ.')
        counted = 0
        for case in fresh['cases']:
            row = checked_read(case['result'], inputs)
            require(case['condition'] == row['condition'] and case['exact']
                    and len(case['rounds']) == row['rounds'], 'Fresh case incomplete or different.')
            for rnd, detail in enumerate(case['rounds'], 1):
                require(detail['round'] == rnd and len(detail['calls']) == 2
                        and {c['side'] for c in detail['calls']} == {0, 1}
                        and all(c['exact'] for c in detail['calls']), 'Fresh round/action count differs.')
                counted += 2
        require(fresh['checked_calls'] == counted, 'Fresh successful external call count differs.')
        result['checked_calls'] = counted
    except Exception as error:
        result['errors'].append(dict(stage='cross_receipt_checks', diagnostic=public_diagnostic(str(error))))
    result['passed'] = not result['errors']
    result['attempts'] = audits.get('strict', {}).get('attempts', [])
    result['unresolved'] = audits.get('strict', {}).get('unresolved', [])
    result['fresh_reported_calls'] = audits.get('fresh', {}).get('checked_calls')
    return result


def journal_event(stream, **values):
    stream.write(json.dumps(dict(time_utc=now(), **values), sort_keys=True, allow_nan=False) + '\n')
    stream.flush()
    os.fsync(stream.fileno())


def state_digest(value):
    return hashlib.sha256(repr(value).encode()).hexdigest()


def mutable_container_ids(value, seen=None):
    """Only inspect ordinary captured containers; never mutate policy state."""
    if seen is None:
        seen = set()
    if not isinstance(value, (dict, list, tuple)) or id(value) in seen:
        return set()
    seen.add(id(value))
    result = {id(value)} if isinstance(value, (dict, list)) else set()
    values = list(value.keys()) + list(value.values()) if isinstance(value, dict) else value
    for child in values:
        result.update(mutable_container_ids(child, seen))
    return result


def independent_snapshots(proposed, trace):
    values = [proposed, trace['submitted_actions']]
    values.extend(trace['proposed_actions'].values())
    values.extend(trace['discarded_proposals'].values())
    containers = [mutable_container_ids(value) for value in values]
    return all(not (first & second) for i, first in enumerate(containers) for second in containers[i+1:])


def forecast_geometry(saved, forecast, cfg):
    """Reconstruct only the existing forecast; this makes no policy decision."""
    from bot_research.bots.counters.visible_search import player_from_snapshot
    from td_game.actions import apply_action
    from td_game.pathfinding import shortest_path

    enemy = player_from_snapshot(saved['players'][1-saved['player']])
    accepted = [apply_action(enemy, action, saved['round'], cfg)['accepted'] for action in forecast]
    route = shortest_path(cfg.globals.width, cfg.globals.height,
        {(b.x, b.y) for b in enemy.buildings}, cfg.globals.spawn, cfg.globals.base)
    require(route is not None, 'Forecast map has no route.')
    adjacent = [list(cell) for cell in route[:-1] if max(abs(cell[0]-10), abs(cell[1]-1)) == 1]
    return dict(all_actions_accepted=all(accepted), hp=enemy.hp, gold=enemy.gold,
        n_factories=enemy.n_factories,
        buildings=[dict(type=b.type, x=b.x, y=b.y) for b in enemy.buildings],
        active_roster=[entry.type for entry in enemy.roster if entry.active(saved['round'])],
        path=[list(cell) for cell in route], length_path=len(route)-1,
        Y_adjacent_path_cells=adjacent,
        Y_exposure_damage=len(adjacent)*cfg.turrets['splash'].damage,
        tier2_hp=cfg.minions['tier2'].hp,
        initial_affordable_tier2=saved['players'][saved['player']]['gold']//cfg.minions['tier2'].cost)


def mechanism():
    """Additional fresh U/reference calls only on the four declared new histories."""
    begin = time.perf_counter()
    inputs = {}
    declaration = verify_declaration(inputs)
    from bot_research.bots.counters.blind_fourth_round import BlindFourthRound
    from bot_research.bots.counters.early_wall_guard import EarlyWallGuard
    from bot_research.bots.counters.wall_signal_repair import WallSignalRepair
    from bot_research.bots.counters.visible_search import player_from_snapshot
    from bot_research.experiments.validation.policy_value_snapshot import freeze_state
    from bot_research.experiments.validation.replay_audit import normalized
    from td_game.actions import apply_action
    from td_game.config import balanced_config
    from td_game.engine import Engine

    freeze = checked_read(ROOT / 'freeze.json', inputs)
    for p, h in declaration['input_sha256'].items():
        require(freeze['source_sha256'].get(p) == h, 'Mechanism freeze omitted a declared input.')
    verify_archive(ROOT, freeze, inputs, compare_current=True)
    witness = next(w for w in read(DATA[0])['witnesses'] if w['id'] == 'guard00')
    outdir = R / (NAME + '-mechanism')
    outdir.mkdir(exist_ok=False)
    journal_path = outdir / 'calls.jsonl'
    checkpoints, cases = [], []
    with journal_path.open('x') as journal:
        journal_event(journal, event='audit_started', declaration=str(D), declared_cases=4)
        for index, (_, opponent, side) in enumerate(GRID):
            detail = dict(index=index, opponent=opponent, side=side,
                result=str(ROOT / 'results' / f'case{index:04d}.json'), passed=False,
                completed=False, rounds=[], errors=[], attempted={k: 0 for k in COUNTER_KEYS},
                successful={k: 0 for k in COUNTER_KEYS}, nested_successful={k: 0 for k in NESTED_KEYS},
                nested_attempt_counts_complete=True)
            cases.append(detail)
            selector = refs = None
            stage = 'load_case'
            try:
                case, _ = inspect_new_case(index, declaration, inputs, witness)
                require(case['audit_passed'], 'New case replay/source validation failed: ' + repr(case['errors']))
                row = checked_read(detail['result'], inputs)
                records = [json.loads(s) for s in safe_path(case['replay']).read_text().splitlines()]
                detail['condition'], detail['expected_rounds'] = row['condition'], row['rounds']
                detail['replay'] = case['replay']
                cfg = balanced_config()
                engine = Engine(cfg, tuple(row['bot_specs']))
                require(normalized(engine.initial_records(tuple(row['bot_specs']))) == records[:2], 'Initial records differ.')
                stage = 'construct_fresh_instances'
                journal_event(journal, event='construct_started', case=index)
                selector = BlindFourthRound()
                refs = {'G': EarlyWallGuard(witness='guard00'), 'L4': WallSignalRepair()}
                refs['L4'].attack_round = 4
                require(freeze_state(vars(selector.g)) == freeze_state(vars(refs['G']))
                        and freeze_state(vars(selector.l4)) == freeze_state(vars(refs['L4'])), 'Initial component states differ.')
                journal_event(journal, event='construct_completed', case=index)
                expected_selected = expected_tau = None

                def invoke(label, policy, saved, rnd):
                    nonlocal stage
                    stage = label
                    detail['attempted'][label] += 1
                    ordinal = detail['attempted'][label]
                    journal_event(journal, event='call_started', case=index, round=rnd,
                                  label=label, ordinal=ordinal)
                    arg = deepcopy(saved)
                    started = time.perf_counter()
                    try:
                        proposal = policy.decide(arg)
                    except Exception as error:
                        journal_event(journal, event='call_failed', case=index, round=rnd,
                            label=label, ordinal=ordinal, seconds=time.perf_counter()-started,
                            diagnostic=public_diagnostic(str(error)))
                        raise
                    detail['successful'][label] += 1
                    journal_event(journal, event='call_completed', case=index, round=rnd,
                        label=label, ordinal=ordinal, seconds=time.perf_counter()-started,
                        actions=proposal, observation_unchanged=arg == saved)
                    return proposal, arg == saved

                for rnd in range(1, row['rounds']+1):
                    obs = engine.observation(side)
                    saved = deepcopy(obs)
                    enemy = saved['players'][1-side]
                    present = bool(enemy['buildings'] or enemy['roster'])
                    selected_before = expected_selected
                    if expected_selected is None and rnd == 4:
                        expected_selected, expected_tau = 'L4', rnd
                    called = ['G', 'L4'] if expected_selected is None else [expected_selected]
                    returned = expected_selected or 'G'
                    members = {'G': selector.g, 'L4': selector.l4}
                    before = {k: freeze_state(vars(v)) for k, v in members.items()}
                    lengths = {k: len(v.trace) for k, v in members.items()}
                    repair_length = len(selector.l4.repair_trace)
                    model_round = selector.l4.model.last_round
                    proposed, unchanged = invoke('actual_U', selector, saved, rnd)
                    reference_proposals = {}
                    ref_unchanged = True
                    for name in called:
                        value, immutable = invoke('reference_' + name, refs[name], saved, rnd)
                        reference_proposals[name] = value
                        ref_unchanged = ref_unchanged and immutable
                    stage = 'compare_round'
                    pair = records[2*rnd:2*rnd+2]
                    actual = [actions(record) for record in pair]
                    expected_trace = dict(round=rnd, player=side, selected_before=selected_before,
                        selected=expected_selected, selection_round=expected_tau,
                        opponent_buildings=len(enemy['buildings']), opponent_roster=len(enemy['roster']),
                        presence=present, member_calls=called, returned_member=returned,
                        proposed_actions=reference_proposals,
                        discarded_proposals={k: v for k, v in reference_proposals.items() if k != returned},
                        submitted_actions=reference_proposals[returned])
                    checks = dict(observation_unchanged=unchanged and ref_unchanged and obs == saved,
                        captured_snapshots_independent=independent_snapshots(proposed, selector.trace[-1]),
                        actual_actions_exact=proposed == actual[side],
                        selected_reference_actions_exact=proposed == reference_proposals[returned],
                        trace=selector.trace[-1] == expected_trace and len(selector.trace) == rnd,
                        bookkeeping=selector.last_round == rnd and selector.player == side
                            and selector.selected == expected_selected and selector.selection_round == expected_tau,
                        reference_states=all(freeze_state(vars(members[k])) == freeze_state(vars(refs[k])) for k in members),
                        inactive_state_unchanged=all(freeze_state(vars(members[k])) == before[k] for k in members if k not in called),
                        component_trace_increments=all(len(members[k].trace)-lengths[k] == int(k in called) for k in members),
                        repair_trace_increment=len(selector.l4.repair_trace)-repair_length == int('L4' in called),
                        model_round=selector.l4.model.last_round == (rnd if 'L4' in called else model_round),
                        model_player=selector.l4.model.player == 1-side,
                        model_state=freeze_state(vars(selector.l4.model)) == freeze_state(vars(refs['L4'].model)))
                    own = player_from_snapshot(saved['players'][side])
                    checks['actual_actions_legal'] = all(apply_action(own, action, rnd, cfg)['accepted'] for action in proposed)
                    checks['reference_proposals_legal'] = True
                    for value in reference_proposals.values():
                        own = player_from_snapshot(saved['players'][side])
                        checks['reference_proposals_legal'] &= all(apply_action(own, a, rnd, cfg)['accepted'] for a in value)
                    checks['engine_replay'] = normalized(engine.play_round(actual)) == pair
                    # Completed trace transitions count nested successes. The H
                    # counts are nested subsets and are not external decisions.
                    detail['nested_successful'] = dict(internal_G=len(selector.g.trace),
                        internal_L4=len(selector.l4.trace), internal_H_model=selector.l4.model.last_round,
                        reference_H_model=refs['L4'].model.last_round)
                    forecast = deepcopy(selector.l4.trace[-1]['predicted_actions']) if 'L4' in called else None
                    record = dict(round=rnd, checks=checks, passed=all(checks.values()),
                        expected_member_calls=called, trace=deepcopy(selector.trace[-1]),
                        reference_proposals=deepcopy(reference_proposals),
                        component_state_sha256={k: state_digest(freeze_state(vars(v))) for k, v in members.items()},
                        reference_state_sha256={k: state_digest(freeze_state(vars(v))) for k, v in refs.items()},
                        model_last_round=selector.l4.model.last_round, model_player=selector.l4.model.player,
                        predicted_H_actions=forecast, actual_opponent_actions=actual[1-side],
                        forecast_input_snapshot=deepcopy(enemy) if rnd == 4 else None,
                        round4_forecast_geometry=forecast_geometry(saved, forecast, cfg) if rnd == 4 else None,
                        L4_timing_trace=deepcopy(selector.l4.trace[-1]) if 'L4' in called else None,
                        L4_repair_trace=deepcopy(selector.l4.repair_trace[-1]) if 'L4' in called else None,
                        predicted_H_actions_equal_actual_opponent=(forecast == actual[1-side]) if forecast is not None else None,
                        successful=deepcopy(detail['successful']), nested_successful=deepcopy(detail['nested_successful']))
                    detail['rounds'].append(record)
                    checkpoint = outdir / f'case{index:04d}-round{rnd:04d}.json'
                    atomic_json(checkpoint, record, exclusive=True)
                    checkpoints.append(str(checkpoint))
                    journal_event(journal, event='round_completed', case=index, round=rnd,
                                  checkpoint=str(checkpoint), passed=record['passed'])
                require(engine.result == row['result'], 'Mechanism terminal result differs.')
                n = row['rounds']
                d = expected_tau-1 if expected_tau is not None else n
                expected_g = n if expected_selected in (None, 'G') else d
                expected_l = n if expected_selected in (None, 'L4') else d
                counts_ok = (detail['successful'] == dict(actual_U=n, reference_G=expected_g, reference_L4=expected_l)
                    and detail['attempted'] == detail['successful']
                    and detail['nested_successful'] == dict(internal_G=expected_g, internal_L4=expected_l,
                        internal_H_model=expected_l, reference_H_model=expected_l))
                detail.update(completed=True, selected=expected_selected, selection_round=expected_tau,
                    deferred_rounds=d, counts_ok=counts_ok,
                    passed=counts_ok and all(r['passed'] for r in detail['rounds']))
            except Exception as error:
                detail['errors'].append(dict(stage=stage, diagnostic=public_diagnostic(str(error))))
                if selector is not None:
                    detail['nested_successful'].update(internal_G=len(selector.g.trace),
                        internal_L4=len(selector.l4.trace), internal_H_model=selector.l4.model.last_round)
                if refs is not None:
                    detail['nested_successful']['reference_H_model'] = refs['L4'].model.last_round
                detail['nested_attempt_counts_complete'] = False
                journal_event(journal, event='case_failed', case=index, stage=stage,
                    errors=detail['errors'], attempted=detail['attempted'], successful=detail['successful'],
                    nested_successful_lower_bounds=detail['nested_successful'], nested_attempt_counts_complete=False)
            case_path = outdir / f'case{index:04d}.json'
            atomic_json(case_path, detail, exclusive=True)
            checkpoints.append(str(case_path))
            journal_event(journal, event='case_finished', case=index, passed=detail['passed'], receipt=str(case_path))
        journal_event(journal, event='audit_finished', cases=len(cases))
    for path in [str(journal_path)] + checkpoints:
        pin(path, inputs)
    integrity_errors = finish_hashes(inputs)
    result = dict(time_utc=now(), elapsed_seconds=time.perf_counter()-begin, games=4,
        all_passed=all(c['passed'] for c in cases) and not integrity_errors,
        audit_completed=all(c['completed'] for c in cases) and not integrity_errors,
        cases=cases, journal=str(journal_path), checkpoints=checkpoints,
        attempted={k: sum(c['attempted'][k] for c in cases) for k in COUNTER_KEYS},
        successful={k: sum(c['successful'][k] for c in cases) for k in COUNTER_KEYS},
        nested_successful={k: sum(c['nested_successful'][k] for c in cases) for k in NESTED_KEYS},
        nested_attempt_counts_complete=all(c['nested_attempt_counts_complete'] for c in cases),
        integrity_errors=integrity_errors, input_sha256=inputs,
        scope='Additional fresh U and independent G/L4 references on exactly four actual new histories. '
              'Nested calls are subsets, not additional external calls. Forecast accuracy is diagnostic. '
              'Shared globals, clocks and alias identity are outside logical-state snapshots.')
    atomic_json(R / (NAME+'-mechanism.json'), result, exclusive=True)
    print(json.dumps({k: result[k] for k in ('time_utc', 'all_passed', 'audit_completed', 'successful', 'nested_successful')}), flush=True)
    return 0 if result['all_passed'] else 2


def inspect_mechanism(declaration, inputs):
    """Authenticate the durable journal, case grid, checkpoints and count claims."""
    result = dict(passed=False, authenticated=False, errors=[], cases=[], successful={}, nested_successful={})
    path = R / (NAME+'-mechanism.json')
    try:
        receipt = checked_read(path, inputs)
        for p, h in receipt['input_sha256'].items():
            pin(p, inputs, h)
        for p, h in declaration['input_sha256'].items():
            require(receipt['input_sha256'].get(p) == h, 'Mechanism omitted an active input.')
        require(receipt['input_sha256'].get(str(D)) == sha(D), 'Mechanism declaration edge absent.')
        freeze = checked_read(ROOT / 'freeze.json', inputs)
        for p, h in freeze['source_sha256'].items():
            require(receipt['input_sha256'].get(p) == h, 'Mechanism omitted frozen source.')
        require(receipt['games'] == 4 and len(receipt['cases']) == 4, 'Mechanism must retain four cases.')
        journal_path = safe_path(receipt['journal'])
        require(journal_path == R / (NAME+'-mechanism') / 'calls.jsonl', 'Unexpected mechanism journal.')
        require(str(journal_path) in receipt['input_sha256'], 'Mechanism journal not pinned.')
        events = [json.loads(line) for line in journal_path.read_text().splitlines()]
        require(events and events[0]['event'] == 'audit_started' and events[-1]['event'] == 'audit_finished',
                'Mechanism journal has no complete audit boundary.')
        for event in events:
            if event['event'] in ('call_started', 'call_completed', 'call_failed'):
                require(type(event.get('case')) is int and 0 <= event['case'] < 4
                        and event.get('label') in COUNTER_KEYS, 'Journal contains an undeclared call.')
        expected_checkpoints = set()
        for index, case in enumerate(receipt['cases']):
            _, opponent, side = GRID[index]
            expected_path = str(ROOT / 'results' / f'case{index:04d}.json')
            require(case['index'] == index and case['opponent'] == opponent and case['side'] == side
                    and case['result'] == expected_path, 'Mechanism case identity differs.')
            case_path = R / (NAME+'-mechanism') / f'case{index:04d}.json'
            require(str(case_path) in receipt['input_sha256'] and checked_read(case_path, inputs) == case,
                    'Mechanism case checkpoint differs.')
            expected_checkpoints.add(str(case_path))
            by_label = {label: {'call_started': [], 'call_completed': [], 'call_failed': []} for label in COUNTER_KEYS}
            for event in events:
                if event.get('case') == index and event['event'] in ('call_started', 'call_completed', 'call_failed'):
                    require(event['label'] in by_label, 'Unknown journal call label.')
                    by_label[event['label']][event['event']].append(event)
            for label, kinds in by_label.items():
                starts, done, failed = [kinds[k] for k in ('call_started', 'call_completed', 'call_failed')]
                require(len(starts) == case['attempted'][label] and len(done) == case['successful'][label],
                        'Mechanism journal call accounting differs.')
                require([e['ordinal'] for e in starts] == list(range(1, len(starts)+1)), 'Attempt ordinals differ.')
                start_keys = {(e['round'], e['ordinal']) for e in starts}
                completion_keys = [(e['round'], e['ordinal']) for e in done + failed]
                require(len(set(completion_keys)) == len(completion_keys)
                        and set(completion_keys) <= start_keys, 'Missing or duplicated attempted call edges.')
                if case['completed']:
                    require(not failed and len(done) == len(starts), 'Completed case contains unfinished/failed calls.')
            row = checked_read(expected_path, inputs)
            require(receipt['input_sha256'].get(expected_path) == sha(expected_path)
                    and receipt['input_sha256'].get(row['replay_path']) == sha(row['replay_path']),
                    'Mechanism result/replay edges absent.')
            require(case.get('condition') == row['condition'] and case.get('expected_rounds') == row['rounds'],
                    'Mechanism condition or complete-stream round count differs.')
            records = [json.loads(s) for s in safe_path(row['replay_path']).read_text().splitlines()]
            expected_selected = expected_tau = None
            g_calls = l_calls = 0
            for rnd, detail in enumerate(case['rounds'], 1):
                require(detail['round'] == rnd and rnd <= row['rounds'], 'Mechanism round numbering differs.')
                checkpoint = R / (NAME+'-mechanism') / f'case{index:04d}-round{rnd:04d}.json'
                require(str(checkpoint) in receipt['input_sha256'] and checked_read(checkpoint, inputs) == detail,
                        'Mechanism round checkpoint differs.')
                expected_checkpoints.add(str(checkpoint))
                enemy = records[2*(rnd-1)+(1-side)]['snapshot']
                present = bool(enemy['buildings'] or enemy['roster'])
                if rnd == 4:
                    require(detail['forecast_input_snapshot'] == enemy,
                            'Round-four forecast input is not the actual completed opponent snapshot.')
                if expected_selected is None and rnd == 4:
                    expected_selected, expected_tau = 'L4', rnd
                called = ['G', 'L4'] if expected_selected is None else [expected_selected]
                g_calls += int('G' in called)
                l_calls += int('L4' in called)
                require(detail['expected_member_calls'] == called, 'Mechanism member-call schedule differs.')
                require(detail['successful'] == dict(actual_U=rnd, reference_G=g_calls, reference_L4=l_calls),
                        'Mechanism cumulative external/reference count differs.')
                require(detail['nested_successful'] == dict(internal_G=g_calls, internal_L4=l_calls,
                    internal_H_model=l_calls, reference_H_model=l_calls), 'Mechanism nested call count differs.')
                require(detail['passed'] == all(detail['checks'].values()), 'Mechanism round success flag differs.')
                completed = [e for e in events if e.get('case') == index and e.get('round') == rnd
                             and e['event'] == 'call_completed']
                require([e['label'] for e in completed] == ['actual_U'] + ['reference_'+k for k in called],
                        'Journal ordered call schedule differs.')
                require(completed[0]['actions'] == detail['trace']['submitted_actions']
                        and {e['label'].removeprefix('reference_'): e['actions'] for e in completed[1:]}
                        == detail['reference_proposals'], 'Journal proposals differ from round checkpoint.')
            if case['completed']:
                require(len(case['rounds']) == row['rounds'] and case['selected'] == expected_selected
                        and case['selection_round'] == expected_tau, 'Mechanism complete case truncated or wrong branch.')
                require(case['successful'] == dict(actual_U=row['rounds'], reference_G=g_calls, reference_L4=l_calls)
                        and case['attempted'] == case['successful'] and case['counts_ok'], 'Mechanism final count formula failed.')
                require(case['passed'] == all(r['passed'] for r in case['rounds']), 'Mechanism case success differs.')
        require(set(receipt['checkpoints']) == expected_checkpoints
                and len(receipt['checkpoints']) == len(expected_checkpoints), 'Mechanism checkpoint coverage differs.')
        for field, keys in (('attempted', COUNTER_KEYS), ('successful', COUNTER_KEYS), ('nested_successful', NESTED_KEYS)):
            require(receipt[field] == {k: sum(c[field][k] for c in receipt['cases']) for k in keys},
                    'Mechanism aggregate counts differ: ' + field)
        require(receipt['all_passed'] == (all(c['passed'] for c in receipt['cases']) and not receipt['integrity_errors']),
                'Mechanism aggregate pass flag differs.')
        require(receipt['audit_completed'] == (all(c['completed'] for c in receipt['cases']) and not receipt['integrity_errors']),
                'Mechanism aggregate completion flag differs.')
        result.update(authenticated=True, passed=receipt['all_passed'], receipt=str(path),
            cases=receipt['cases'], attempted=receipt['attempted'], successful=receipt['successful'],
            nested_successful=receipt['nested_successful'], journal=receipt['journal'],
            nested_attempt_counts_complete=receipt['nested_attempt_counts_complete'])
    except Exception as error:
        result['errors'].append(public_diagnostic(str(error)))
        # Even an interrupted audit with no final receipt retains every journal
        # and checkpoint already written. These are partial evidence, not passes.
        partial = R / (NAME+'-mechanism')
        if partial.exists():
            for item in sorted(partial.iterdir()):
                if item.is_file() and item.suffix in ('.json', '.jsonl'):
                    pin(item, inputs)
            result['partial_artifacts'] = [str(p) for p in sorted(partial.iterdir()) if p.is_file()]
    return result


def prefix_mechanism(case, opponent):
    """Exact first-four U private-state mechanism; H prediction accuracy is separate."""
    if case is None or len(case['rounds']) < 4:
        return None
    factory = dict(op='buy_factory')
    witness = next(w for w in read(DATA[0])['witnesses'] if w['id'] == 'guard00')
    walls = [dict(type='wall', x=x, y=y) for x, y in witness['walls']]
    x_turret, y_turret = dict(type='splash', x=1, y=3), dict(type='splash', x=10, y=1)
    checks = []
    for rnd, record in enumerate(case['rounds'][:4], 1):
        trace = record['trace']
        checks.append(record['passed'])
        if rnd <= 3:
            checks.extend([trace['member_calls'] == ['G', 'L4'], trace['selected'] is None,
                trace['selection_round'] is None, record['model_last_round'] == rnd,
                trace['returned_member'] == 'G'])
            if rnd <= 2:
                checks.append(trace['proposed_actions']['G'] == trace['proposed_actions']['L4'])
            else:
                checks.append(trace['proposed_actions']['L4'] == [factory]*8
                              and trace['discarded_proposals'] == {'L4': [factory]*8})
        else:
            predicted = [dict(op='build_turret', type='splash', x=10, y=1)] + [factory]*(11 if opponent == 'H' else 10)
            timing = dict(round=4, predicted_actions=predicted, attack_count=6 if opponent == 'H' else 0,
                          attack_tier='tier2', forecast_attack_gain=72 if opponent == 'H' else 0,
                          forecast_residual_damage=0)
            repair = dict(round=4, original_predicted_damage=0, replacement_predicted_damage=None,
                          selected=False, proposed_construction=[], proposed_actions_legal=None)
            if opponent == 'H':
                route = [[x, 0] for x in range(12)] + [[11, y] for y in range(1, 12)]
                adjacent = [[9, 0], [10, 0], [11, 0], [11, 1], [11, 2]]
            else:
                route = ([[x, 0] for x in range(12)] + [[11, y] for y in (1, 2)]
                    + [[x, 2] for x in range(10, -1, -1)] + [[0, y] for y in (3, 4)]
                    + [[x, 4] for x in range(1, 12)] + [[11, y] for y in range(5, 12)])
                adjacent = [[9, 0], [10, 0], [11, 0], [11, 1], [11, 2], [10, 2], [9, 2]]
            geometry = dict(all_actions_accepted=True, hp=800, gold=11 if opponent == 'H' else 1,
                n_factories=28 if opponent == 'H' else 21,
                buildings=[y_turret] if opponent == 'H' else walls+[x_turret, y_turret],
                active_roster=[], path=route, length_path=22 if opponent == 'H' else 44,
                Y_adjacent_path_cells=adjacent, Y_exposure_damage=50 if opponent == 'H' else 70,
                tier2_hp=70, initial_affordable_tier2=6)
            checks.append(record['round4_forecast_geometry'] == geometry)
            checks.extend([trace['member_calls'] == ['L4'], trace['selected'] == 'L4',
                trace['selection_round'] == 4, trace['returned_member'] == 'L4',
                trace['discarded_proposals'] == {}, record['model_last_round'] == 4,
                record['nested_successful']['internal_G'] == 3,
                record['nested_successful']['internal_L4'] == 4,
                record['predicted_H_actions'] == predicted,
                record['L4_timing_trace'] == timing, record['L4_repair_trace'] == repair])
    return all(checks)


def comparison(first, second, usable):
    equal = first == second if usable else None
    divergence = None
    if equal is False:
        i = next((j for j in range(min(len(first), len(second))) if first[j] != second[j]), min(len(first), len(second)))
        divergence = dict(record_index=i, first=first[i] if i < len(first) else None,
                          second=second[i] if i < len(second) else None)
    return equal, divergence


def inspect_control(old, declaration, inputs, witness):
    """Replay original T without requiring its scientific hypotheses to hold."""
    path = safe_path(old['result'])
    case, history = inspect_original_case('T', old['opponent'], old['side'], path,
                                          declaration, inputs, witness)
    case.update(origin='retained', U_side=old['U_side'], reference_side=old['reference_side'])
    try:
        require(case['audit_passed'], 'Original T direct record replay failed.')
        old_receipt = checked_read(old['receipt'], inputs)
        require(old_receipt['audit_completed'] is True, 'Original T required auditing did not complete.')
        for source, expected in old_receipt['input_sha256'].items():
            pin(source, inputs, expected)
        matching = [c for c in old_receipt['cases'] if c['result'] == str(path)]
        require(len(matching) == 1 and matching[0]['candidate'] == 'T'
                and matching[0]['opponent'] == old['opponent'] and matching[0]['side'] == old['side']
                and matching[0]['verified'] and matching[0]['outcome'] == case['outcome']
                and matching[0]['rounds'] == case['rounds'], 'Original T receipt case differs.')
        root = safe_path(old['root'])
        freeze = checked_read(root/'freeze.json', inputs)
        verify_archive(root, freeze, inputs, compare_current=False)
        for source, expected in freeze['source_sha256'].items():
            if source.startswith('td_game/'):
                pin(source, inputs, expected)
        roots = {declaration['policies'][k]['spec'].partition(':')[0] for k in ('T', old['opponent'])}
        for source in set(static_closure(roots)) | set(DATA):
            require(freeze['source_sha256'].get(str(source)) == sha(source),
                    'Retained T policy/data dependency differs: ' + str(source))
        for kind, audit_path in old['audits'].items():
            audit = checked_read(audit_path, inputs, old_receipt['input_sha256'][audit_path])
            if kind == 'strict':
                require(audit['valid_conditions'] == audit['expected_conditions'] == 4
                        and audit['attempt_counts'] == {'valid': 4} and not audit['unresolved'],
                        'Original T strict audit incomplete.')
            else:
                require(audit['all_passed'], 'Original T audit failed.')
        member_audit = checked_read(old['mechanism_receipt'], inputs,
                                   old_receipt['input_sha256'][old['mechanism_receipt']])
        require(member_audit['audit_completed'] and member_audit['all_passed'], 'Original T member audit failed.')
        case.update(verified=True, retained_receipt=old['receipt'], original_archive_verified=True,
                    opening=matching[0]['opening'], retained_mechanism_verified=matching[0]['mechanism_verified'])
    except Exception as error:
        case['verified'] = False
        case['errors'].append(public_diagnostic(str(error)))
    return case, history


def check():
    started = time.perf_counter()
    inputs = {}
    declaration = verify_declaration(inputs)
    (A/'verification').mkdir(exist_ok=True)
    witness = next(w for w in read(DATA[0])['witnesses'] if w['id'] == 'guard00')
    campaign = audit_campaign(declaration, inputs)
    mechanism_audit = inspect_mechanism(declaration, inputs)
    mechanisms = {(c['opponent'], c['side']): c for c in mechanism_audit['cases']}
    cases, histories = [], {}
    for index, (_, opponent, side) in enumerate(GRID):
        case, history = inspect_new_case(index, declaration, inputs, witness)
        case['campaign_audits_passed'] = campaign['passed']
        case['verified'] = case['audit_passed'] and campaign['passed']
        member_case = mechanisms.get((opponent, side)) if mechanism_audit['authenticated'] else None
        case['mechanism_verified'] = bool(member_case and member_case['passed'])
        case['prefix_mechanism'] = prefix_mechanism(member_case, opponent)
        if case['verified'] and not case['opening']['passed']:
            opening_condition = False
        elif case['verified']:
            opening_condition = case['prefix_mechanism']
        else:
            opening_condition = None
        # H opening is supporting evidence. H2 is exactly the two S cases.
        case['opening_and_mechanism_condition'] = opening_condition
        case['H2_condition'] = opening_condition if opponent == 'S' else None
        cases.append(case)
        histories['U', opponent, side] = history
    controls = []
    for old in declaration['retained_controls']:
        case, history = inspect_control(old, declaration, inputs, witness)
        controls.append(case)
        histories['T', old['opponent'], old['side']] = history
    require(len(cases) == len(controls) == 4, 'Keep all eight declared new/control cases.')
    by = {(c['opponent'], c['side']): c for c in cases}
    old_by = {(c['opponent'], c['side']): c for c in controls}
    payoffs = {'W': 1, 'D': 0, 'L': -1}
    transfers = []
    for opponent in ORDER:
        for side in (0, 1):
            new, old = by[opponent, side], old_by[opponent, side]
            usable = new['verified'] and old['verified']
            equal, divergence = comparison(histories['U', opponent, side], histories['T', opponent, side], usable)
            u = payoffs[new['outcome']] if usable else None
            t = payoffs[old['outcome']] if usable else None
            transfers.append(dict(opponent=opponent, U_side=side, reference_T_side=old['reference_side'],
                new_result=new['result'], old_result=old['result'], verified=usable,
                same_complete_history=equal, first_divergence=divergence,
                U_payoff=u, T_payoff=t, T_minus_U=t-u if usable else None,
                T_at_least_U=t >= u if usable else None,
                T_strictly_greater_than_U=t > u if usable else None))
    pairs = []
    for opponent in ORDER:
        x, y = by[opponent, 0], by[opponent, 1]
        usable = x['verified'] and y['verified']
        equal, divergence = comparison(histories['U', opponent, 0], histories['U', opponent, 1], usable)
        pairs.append(dict(opponent=opponent, verified=usable, same_complete_history=equal,
            same_outcome=x.get('outcome') == y.get('outcome') if usable else None, first_divergence=divergence))
    verdicts = dict(
        H1=aggregate_verdict([c['same_complete_history'] for c in transfers if c['opponent'] == 'H']),
        H2=aggregate_verdict([c['H2_condition'] for c in cases if c['opponent'] == 'S']),
        H3=aggregate_verdict([c['T_at_least_U'] for c in transfers]),
        H4=aggregate_verdict([c['T_strictly_greater_than_U'] for c in transfers if c['opponent'] == 'S']))
    integrity_errors = finish_hashes(inputs)
    if integrity_errors:
        verdicts = {k: 'OPEN' for k in verdicts}
    audit_completed = (all(c['verified'] for c in cases+controls)
                       and mechanism_audit['passed'] and not integrity_errors)
    expected_fresh = 2*sum(c['rounds'] for c in cases if 'rounds' in c)
    if campaign['passed']:
        require(campaign['checked_calls'] == expected_fresh, 'Final ordinary fresh call count differs.')
    stamp = now()
    result = dict(time_utc=stamp, elapsed_seconds=time.perf_counter()-started,
        audit_completed=audit_completed, all_passed=audit_completed and all(v == 'CONFIRMED' for v in verdicts.values()),
        hypotheses=verdicts, new_games_declared=4, retained_games_declared=4, total_cases=8,
        verified_new_cases=sum(c['verified'] for c in cases), verified_retained_cases=sum(c['verified'] for c in controls),
        cases=cases, retained_controls=controls, transfers=transfers, pairs=pairs,
        campaign_audit=campaign, mechanism_audit=mechanism_audit,
        original_new_game_external_calls=sum(2*c['rounds'] for c in cases if c['verified']),
        ordinary_fresh_external_calls_verified=campaign['checked_calls'],
        ordinary_fresh_external_calls_expected=expected_fresh,
        additional_audit_successful_calls=mechanism_audit.get('successful', {}),
        additional_audit_attempted_calls=mechanism_audit.get('attempted', {}),
        nested_successful_calls=mechanism_audit.get('nested_successful', {}),
        final_checker_policy_calls=0, retained_control_new_policy_calls=0,
        complete_engine_replays=sum('terminal_replay' in c for c in cases+controls),
        integrity_errors=integrity_errors, input_sha256=inputs,
        scope='Four selected standard-start U games and four matching-seat completed T controls. '
              'No complete payoff table, unrestricted bound or held-out strength claim. '
              'Additional references consume actual public histories; discarded proposals are not engine actions. '
              'All nested call counts are separately labelled subsets.')
    lines = ['# Unconditional L4 continuation compared with the T choice', '', f'Checked {stamp}.', '',
        f'Audit completion: {"COMPLETE" if audit_completed else "INCOMPLETE"}. '
        + '; '.join(k+' '+v for k, v in verdicts.items()) + '.', '',
        '| Opponent | Candidate seat | U WDL | T WDL | T minus U | Both verified |',
        '| --- | ---: | --- | --- | ---: | --- |']
    for comparison_case in transfers:
        opponent, side = comparison_case['opponent'], comparison_case['U_side']
        new, old = by[opponent, side], old_by[opponent, side]
        lines.append(f'| {opponent} | {side} | {new.get("outcome", "unavailable")} | '
                     f'{old.get("outcome", "unavailable")} | {comparison_case["T_minus_U"]} | '
                     f'{comparison_case["verified"]} |')
    lines += ['', 'H1 compares the two complete U/H streams to their matching-seat T/H streams. '
        'H2 requires both U/S games to reach round four with the exact Claim3 opening and audited private mechanism. '
        'H3 requires T payoff at least U payoff in every one of the four matched settings. '
        'H4 separately requires strict T improvement against S in each physical seat. '
        'U both-seat history comparisons are descriptive and are retained separately.', '',
        'The U/S mechanism checks the actual-public-state H forecast splash(10,1) plus ten factories, '
        'zero attack count and forecast gain, zero forecast residual damage, absence of repair replacement, '
        'thirteen submitted U factories and one tier4 from S. Full first-four actions, snapshots, rosters, '
        'maps, paths, income and combat are checked. The U/H first-four calculation is supporting evidence. '
        'Its whole-history equality is tested separately by H1.', '',
        f'Ordinary fresh external decisions verified: {campaign["checked_calls"]}. '
        f'Additional successful entrypoint calls: {json.dumps(mechanism_audit.get("successful", {}), sort_keys=True)}. '
        f'Nested successful component/model calls: {json.dumps(mechanism_audit.get("nested_successful", {}), sort_keys=True)}. '
        'Nested calls are subsets and are not added to ordinary external-call counts. '
        'Four completed original T controls are reused with zero new T-control-policy calls.', '',
        'The component audit records each attempted call before invocation, completed/failed calls immediately, '
        'and completed rounds in individual checkpoints. An interrupted call can remain pending. '
        'The existing ordinary fresh checker buffers detailed calls until completion; interrupted ordinary fresh '
        'runs retain child output and existing match artifacts but may lack detailed per-call receipts. '
        'This limitation does not apply retroactively to the separate durable component journal.', '',
        'Forecasted H actions are compared with actual opponent actions only as a diagnostic. '
        'The explicit round-four forecast contents in H2 are a separate mechanism predicate. '
        'Full private-state agreement compares fresh references on actual U observations, including '
        'the discarded L4 proposal in round three. It does not assert standalone L4 history transfer. '
        'U never selects G permanently, and presence cannot alter its member-call schedule.', '',
        'All four new cases and four T controls remain in the fixed grid. Missing evidence, exceptions, '
        'early termination, opening violations and first history divergences are preserved in verification/full_games.json '
        'and referenced receipts. H1/H3/H4 use authenticated complete game histories; H2 additionally uses '
        'the first-four component audit. Overall audit completion also requires the complete component audit. '
        'The original T controls require completed evidence auditing, independently of the scientific hypothesis verdicts for T.', '',
        'Later planning deadlines and shared caches prevent unconditional cross-execution history equivalence. '
        'Logical-state snapshots omit module globals, clocks and alias identity. These selected development '
        'conditions establish neither unrestricted dominance nor a complete matrix or global game value.']
    with (A/'RESULTS.md').open('x') as stream:
        stream.write('\n'.join(lines)+'\n')
    result['results_sha256'] = sha(A/'RESULTS.md')
    atomic_json(A/'verification/full_games.json', result, exclusive=True)
    print(json.dumps({k: result[k] for k in ('time_utc', 'audit_completed', 'all_passed', 'hypotheses',
        'verified_new_cases', 'verified_retained_cases', 'ordinary_fresh_external_calls_verified')}), flush=True)
    return 0 if audit_completed else 2


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('mode', choices=['declare', 'mechanism', 'check'])
    parser.add_argument('--review', action='append', default=[])
    args = parser.parse_args()
    if args.mode == 'declare':
        declare(args.review)
        return
    try:
        status = mechanism() if args.mode == 'mechanism' else check()
    except Exception as error:
        verification = A / 'verification'
        verification.mkdir(exist_ok=True)
        stamp = datetime.now(timezone.utc).strftime('%Y%m%dT%H%M%S%fZ')
        failure = verification / (args.mode+'-failure-'+stamp+'.json')
        atomic_json(failure, dict(time_utc=now(), audit_completed=False, mode=args.mode,
            hypotheses={k: 'OPEN' for k in ('H1', 'H2', 'H3', 'H4')},
            diagnostic=public_diagnostic(str(error)), checker_sha256=sha(E/'blind_fourth_round_check.py')),
            exclusive=True)
        print(json.dumps(dict(audit_completed=False, failure_receipt=str(failure))), flush=True)
        raise SystemExit(2) from error
    raise SystemExit(status)


if __name__ == '__main__':
    main()
