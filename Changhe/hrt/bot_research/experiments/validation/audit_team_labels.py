"""Recount declared historical result streams and replay unequal-HP draws.

This is an independent reporting audit. A count from a historical stream is
not a fresh frozen-policy evaluation. Errors and rejected-action games are
reported separately; absent logs prevent the affected replay claim.
"""
from __future__ import annotations
import argparse
from collections import Counter, defaultdict
import hashlib
import json
from pathlib import Path
import time
from td_game.config import balanced_config
from td_game.engine import Engine
from bot_research.experiments.validation.artifact_io import atomic_json
from bot_research.experiments.validation.final_validation import now
from bot_research.experiments.validation.replay_audit import check, normalized
from bot_research.experiments.validation.source_closure import static_closure


def digest(path):
    return hashlib.sha256(Path(path).read_bytes()).hexdigest()


def invalid_reasons(row):
    reasons = []
    if row.get('error'):
        return ['harness_error']
    if row.get('source_changed'):
        reasons.append('source_changed')
    if any(row['scenario_errors']):
        reasons.append('scenario_error')
    if any(player['bot_errors'] for player in row['players']):
        reasons.append('bot_error')
    if any(player['n_rejected'] for player in row['players']):
        reasons.append('rejected_action')
    return reasons


def replay(row, inputs, sources):
    if row['log'] is None:
        return {'status': 'unavailable', 'reason': 'Historical stream has no saved replay path.'}
    path = Path(row['log'])
    check(not path.is_absolute() and '..' not in path.parts and path.parts[:1] == ('bot_research',),
          'Require a relative research replay path.')
    inputs[str(path)] = digest(path)
    for name in ('engine', 'combat', 'actions', 'config', 'state', 'pathfinding'):
        source = 'td_game/' + name + '.py'
        check(row['sources'].get(source) == sources[source], 'Historical engine attestation differs.')
    records = [json.loads(line) for line in path.read_text().splitlines()]
    check(len(records) == 2*(row['rounds']+1), 'Incomplete historical replay.')
    names = row['spec_a'], row['spec_b']
    engine = Engine(balanced_config(), names)
    initial = normalized(engine.initial_records(names))
    extra = dict(research_specs=list(names), research_scenario=row['scenario'])
    if row.get('metadata'):
        extra['research_metadata'] = row['metadata']
    for record in initial:
        record['match'].update(extra)
    check(records[:2] == initial, 'Historical initial records differ.')
    for rnd in range(1, row['rounds']+1):
        pair = records[2*rnd:2*rnd+2]
        check([r['round'] for r in pair] == [rnd, rnd] and [r['player'] for r in pair] == [0, 1],
              'Historical replay ordering differs.')
        check(engine.result is None, 'Historical replay continues after termination.')
        actions = [[e['action'] for e in r['event'] if e['kind'] == 'action'] for r in pair]
        check(normalized(engine.play_round(actions)) == pair, 'Original engine replay differs.')
    check(engine.result == {'winner': row['winner'], 'reason': row['reason']}, 'Historical result differs.')
    check([p.hp for p in engine.players] == [row['hp_a'], row['hp_b']], 'Historical HP differ.')
    return dict(status='passed', replay_path=str(path), rounds=engine.round,
                result=engine.result, hp=[p.hp for p in engine.players])


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('--inputs', nargs='+', required=True)
    parser.add_argument('--output', required=True)
    args = parser.parse_args()
    started = time.perf_counter()
    sources = {str(p): digest(p) for p in static_closure(
        {'bot_research.experiments.validation.audit_team_labels'})}
    sources['td_game/balanced.json'] = digest('td_game/balanced.json')
    inputs, campaigns = {}, []
    for name in args.inputs:
        path = Path(name)
        raw = path.read_bytes()
        inputs[name] = hashlib.sha256(raw).hexdigest()
        rows = [json.loads(line) for line in raw.splitlines()]
        groups = defaultdict(lambda: dict(winner_based=Counter(), margin_sign=Counter()))
        invalid, mismatches = [], []
        for index, row in enumerate(rows):
            reasons = invalid_reasons(row)
            if reasons:
                invalid.append(dict(row_index=index, reasons=reasons, error=row.get('error')))
                continue
            side, winner = row['candidate_side'], row['winner']
            check(side in (0, 1) and winner in (None, 0, 1), 'Invalid player index.')
            check(row['hp_diff_a'] == row['hp_a']-row['hp_b'], 'Historical HP difference inconsistent.')
            spec = row['spec_a'] if side == 0 else row['spec_b']
            true = 'D' if winner is None else ('W' if winner == side else 'L')
            margin = row['hp_diff_a']*(1 if side == 0 else -1)
            sign = 'D' if margin == 0 else ('W' if margin > 0 else 'L')
            groups[spec]['winner_based'][true] += 1
            groups[spec]['margin_sign'][sign] += 1
            if true != sign:
                entry = dict(row_index=index, candidate=spec, scenario=row['scenario'],
                             winner_based=true, margin_sign=sign, margin=margin)
                entry['original_engine_replay'] = replay(row, inputs, sources)
                mismatches.append(entry)
        campaigns.append(dict(input=name, total_rows=len(rows), valid_reported_rows=len(rows)-len(invalid),
                              groups=dict(groups), invalid_rows=invalid, mismatches=mismatches))
        print(json.dumps(dict(input=name, rows=len(rows), invalid=len(invalid),
                              label_disagreements=len(mismatches))), flush=True)
    changed = [p for p, h in {**inputs, **sources}.items() if digest(p) != h]
    check(not changed, 'Audit input or source changed during the check.')
    output = dict(time_utc=now(), runtime_seconds=time.perf_counter()-started,
                  source_sha256=sources, input_sha256=inputs, campaigns=campaigns,
                  source_changed_during_run=changed,
                  scope='Historical reporting audit, not a new strength trial. Valid reported rows exclude recorded harness errors, bot errors, rejected actions, scenario errors and source drift. Only outcome-versus-margin disagreements with saved logs receive original-engine replays. Missing logs and invalid rows remain explicit.')
    atomic_json(args.output, output, exclusive=True)


if __name__ == '__main__':
    main()
