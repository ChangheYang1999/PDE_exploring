"""Re-execute recorded actions with the unchanged engine, without calling bots.

This checks match evidence, not whether a recorded action list was generated
by a particular policy. Source attestations and fresh bot runs cover that
separate question.
"""
from __future__ import annotations
import argparse
from collections import Counter
import hashlib
import json
from pathlib import Path
import time
from td_game.config import balanced_config
from td_game.engine import Engine
from bot_research.experiments.validation.artifact_io import atomic_json, public_diagnostic
from bot_research.experiments.validation.final_validation_strict import now
from bot_research.experiments.validation.source_closure import static_closure


def normalized(value):
    return json.loads(json.dumps(value, allow_nan=False))


def check(equal, message):
    if not equal:
        raise ValueError(message)


def audit_record_sequence(row, records):
    """Require the entire replay and its reported outcome to agree exactly."""
    check(type(row['rounds']) is int and 0 < row['rounds'] <= 50, 'Invalid round count.')
    check(len(records) == 2 * (row['rounds'] + 1), 'Incomplete or extra replay records.')
    check(len(row['bot_specs']) == 2, 'Two bot names are required.')
    config = balanced_config()
    check(row['rules'] == normalized(config.to_dict()), 'Reported rules differ from bundled rules.')
    engine = Engine(config, tuple(row['bot_specs']))
    check(records[:2] == normalized(engine.initial_records(tuple(row['bot_specs']))),
          'Initial records differ from the standard engine initial state.')
    accepted, rejected = [Counter(), Counter()], [Counter(), Counter()]
    bot_errors, history = [[], []], []
    for rnd in range(1, row['rounds'] + 1):
        pair = records[2 * rnd:2 * rnd + 2]
        check([r['player'] for r in pair] == [0, 1], 'Player records are out of order.')
        check(all(r['round'] == rnd for r in pair), 'Round records are out of order.')
        actions = [[e['action'] for e in r['event'] if e['kind'] == 'action'] for r in pair]
        errors = [[e['reason'] for e in r['event'] if e['kind'] == 'bot_error'] for r in pair]
        check(all(len(e) <= 1 for e in errors), 'Multiple bot errors for one call.')
        check(engine.result is None, 'Replay continues after the terminal round.')
        generated = normalized(engine.play_round(actions, [e[0] if e else None for e in errors]))
        check(pair == generated, f'Original engine disagrees with replay round {rnd}.')
        summary = {'round': rnd, 'players': []}
        for side, record in enumerate(generated):
            events = record['event']
            for event in events:
                if event['kind'] == 'action':
                    if event['accepted']:
                        key = event['action']['op'] + ':' + event['action'].get('type', '')
                        accepted[side][key] += 1
                    else:
                        rejected[side][event['reason']] += 1
                elif event['kind'] == 'bot_error':
                    bot_errors[side].append({'round': rnd, 'reason': event['reason']})
            snapshot = record['snapshot']
            player = {k: snapshot[k] for k in ('hp', 'gold', 'n_factories', 'n_turrets', 'n_walls', 'length_path')}
            player['roster'] = dict(Counter(e['type'] for e in snapshot['roster']))
            player['combat'] = next(e for e in events if e['kind'] == 'combat')
            player['income'] = next(e for e in events if e['kind'] == 'income')
            summary['players'].append(player)
        history.append(summary)
    hp = [p.hp for p in engine.players]
    check(engine.result is not None, 'Replay has no terminal result.')
    check(row['result'] == engine.result, 'Reported result differs from replay.')
    check(row['hp'] == hp, 'Reported final HP differs from replay.')
    check(row['hp_difference_p0'] == hp[0] - hp[1], 'Reported HP difference is inconsistent.')
    check(row['accepted_actions'] == [dict(c) for c in accepted], 'Accepted-action totals differ.')
    check(row['rejected_actions'] == [dict(c) for c in rejected], 'Rejected-action totals differ.')
    check(row['bot_errors'] == bot_errors, 'Bot-error totals differ.')
    check(row['history'] == history, 'Reported round history differs.')
    check(all(t['calls'] == row['rounds'] for t in row['decision_seconds']), 'Decision-call count differs.')
    digest = hashlib.sha256()
    for record in records:
        digest.update(json.dumps(record, sort_keys=True, separators=(',', ':'), allow_nan=False).encode())
        digest.update(b'\n')
    check(row['trajectory_sha256'] == digest.hexdigest(), 'Reported replay digest differs.')
    condition = row.get('condition', {})
    for side_field, outcome_field in (('candidate_side', 'candidate_outcome'), ('counter_side', 'counter_outcome')):
        if side_field in condition and outcome_field in row:
            side = condition[side_field]
            check(side in (0, 1), 'Invalid outcome perspective.')
            expected = 'D' if engine.result['winner'] is None else ('W' if engine.result['winner'] == side else 'L')
            check(row[outcome_field] == expected, 'Reported perspective outcome differs.')
    return {'rounds': engine.round, 'hp': hp, 'result': engine.result,
            'records': len(records), 'trajectory_sha256': digest.hexdigest()}


def audit_row(row):
    path = Path(row['replay_path'])
    check(not path.is_absolute() and '..' not in path.parts and path.parts[:1] == ('bot_research',),
          'Replay path must stay in the project research folder.')
    raw = path.read_bytes()
    check(hashlib.sha256(raw).hexdigest() == row['trajectory_sha256'], 'Replay bytes differ from recorded digest.')
    return audit_record_sequence(row, [json.loads(line) for line in raw.splitlines()])


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('--inputs', nargs='+', required=True, help='Result JSON files or result JSONL streams.')
    parser.add_argument('--output', required=True)
    args = parser.parse_args()
    paths = set(static_closure({'bot_research.experiments.validation.replay_audit'}))
    paths.add(Path('td_game/balanced.json'))
    source_hashes = {str(p): hashlib.sha256(p.read_bytes()).hexdigest() for p in paths}
    started = time.perf_counter()
    cases, input_hashes = [], {}
    for name in args.inputs:
        path = Path(name)
        input_hashes[name] = hashlib.sha256(path.read_bytes()).hexdigest()
        rows = [json.loads(s) for s in path.read_text().splitlines()] if path.suffix == '.jsonl' else [json.loads(path.read_text())]
        for index, row in enumerate(rows):
            case = {'input': name, 'row_index': index, 'condition': row.get('condition', {})}
            try:
                case.update(audit_row(row))
                case['passed'] = True
            except (ValueError, KeyError, TypeError, OSError) as error:
                case.update(passed=False, diagnostic=public_diagnostic(str(error)))
            cases.append(case)
            print(json.dumps({'input': name, 'index': index, 'passed': case['passed']}), flush=True)
    changed = [p for p, h in source_hashes.items() if hashlib.sha256(Path(p).read_bytes()).hexdigest() != h]
    result = {'time_utc': now(), 'runtime_seconds': time.perf_counter() - started,
              'source_sha256': source_hashes, 'source_changed_during_run': changed,
              'input_sha256': input_hashes, 'cases': cases, 'count': len(cases),
              'all_passed': all(c['passed'] for c in cases) and not changed,
              'scope': 'Unchanged-engine replay of recorded actions; not a new policy match or an independent strength sample.'}
    atomic_json(args.output, result, exclusive=True)
    print(json.dumps({k: result[k] for k in ('count', 'runtime_seconds', 'all_passed', 'source_changed_during_run')}))
    check(result['all_passed'], 'Replay audit failed; inspect the saved diagnostics.')


if __name__ == '__main__':
    main()
