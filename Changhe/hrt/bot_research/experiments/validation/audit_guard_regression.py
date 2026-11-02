"""Snapshot the scope of the overwritten and restored owned guard module."""
from copy import deepcopy
from datetime import datetime, timezone
import argparse
import hashlib
import json
from pathlib import Path
import time
from td_game.config import balanced_config
from td_game.engine import Engine
from bot_research.bots.counters.guard_continuation import GuardContinuation
from bot_research.bots.counters.relevant_turret_guard import RelevantTurretGuard
from bot_research.bots.counters.defense_strength_guard import DefenseStrengthGuard
from bot_research.bots.counters.exposure_guard import ExposureGuard
from bot_research.experiments.validation.artifact_io import atomic_json, public_diagnostic
from bot_research.experiments.validation.source_closure import static_closure

MODULE = 'bot_research/bots/counters/guard_continuation.py'
GOOD = '8e26d302ec1999eaa2021303d5a2eee9f51a822c16ed0b5f2635cd84630ca984'
BAD = 'da0de97c9c6ac1da20c4a84080c2aedf456f9e33c6de8283491443b650257af0'

def digest(path):
    return hashlib.sha256(Path(path).read_bytes()).hexdigest()

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('--output', required=True)
    args = parser.parse_args()
    started = time.perf_counter()
    sources = {str(p): digest(p) for p in static_closure(
        {'bot_research.experiments.validation.audit_guard_regression'})}
    sources['td_game/balanced.json'] = digest('td_game/balanced.json')
    assert sources[MODULE] == GOOD
    freezes, streams = [], []
    for path in sorted(Path('bot_research/runs/validation').glob('*/freeze.json')):
        obj = json.loads(path.read_text())
        value = obj.get('source_sha256', {}).get(MODULE)
        if value is not None:
            freezes.append(dict(path=str(path), sha256=digest(path), started_utc=obj.get('started_utc'),
                                module_sha256=value, matches_restored=value == GOOD))
    for lane in ('lead', 'defense', 'economy'):
        for path in sorted(Path('bot_research/runs', lane).glob('*/results.jsonl')):
            raw = path.read_bytes()
            end = raw.rfind(b'\n') + 1
            prefix = raw[:end]
            anomalous, dependent_errors, other_errors, malformed = [], [], [], []
            counts = {'rows': 0, 'good_hash': 0, 'bad_hash': 0, 'other_hash': 0, 'no_hash': 0}
            for index, line in enumerate(prefix.splitlines()):
                if not line.strip():
                    continue
                try:
                    row = json.loads(line)
                except json.JSONDecodeError as error:
                    malformed.append(dict(index=index, error=str(error)))
                    continue
                counts['rows'] += 1
                value = row.get('sources', {}).get(MODULE)
                counts['good_hash' if value == GOOD else 'bad_hash' if value == BAD else 'no_hash' if value is None else 'other_hash'] += 1
                specs = [row.get('spec_a', ''), row.get('spec_b', '')]
                errors = [row.get('error')] if row.get('error') else []
                errors += [item for player in row.get('players', []) for item in player.get('bot_errors', [])]
                related = any(any(name in spec for name in ('guard_continuation:', 'relevant_turret_guard:', 'defense_strength_guard:', 'exposure_guard:')) for spec in specs)
                record = dict(row_index=index, specs=specs, scenario=row.get('scenario'),
                              log=row.get('log'), module_sha256=value, source_changed=row.get('source_changed'),
                              errors=json.loads(public_diagnostic(json.dumps(errors))))
                if value is not None and value != GOOD:
                    anomalous.append(record)
                if errors:
                    if related or 'continuation' in str(errors):
                        dependent_errors.append(record)
                    else:
                        other_errors.append(dict(row_index=index, error=json.loads(public_diagnostic(json.dumps(errors)))))
            with path.open('rb') as stream:
                stable = stream.read(end) == prefix
            assert stable, f'Existing prefix changed: {path}'
            streams.append(dict(path=str(path), snapshot_utc=datetime.now(timezone.utc).isoformat(),
                                complete_prefix_bytes=end, complete_prefix_sha256=hashlib.sha256(prefix).hexdigest(),
                                ignored_partial_bytes=len(raw)-end, existing_prefix_unchanged=stable, counts=counts,
                                anomalous_hash_rows=anomalous, dependent_error_rows=dependent_errors,
                                unrelated_error_rows=other_errors, malformed_rows=malformed))
    factories = [(name, lambda value=name: GuardContinuation(continuation=value))
                 for name in ('economy13', 'economy15', 'fortress21')]
    factories += [('relevant_turret_guard', RelevantTurretGuard),
                  ('defense_strength_guard', DefenseStrengthGuard), ('exposure_guard', ExposureGuard)]
    checks = []
    for name, factory in factories:
        for side in (0, 1):
            policy = factory()
            engine = Engine(balanced_config(), ('old-guard-0', 'old-guard-1'))
            rows = []
            for rnd in range(1, 4):
                observation = engine.observation(side)
                before = deepcopy(observation)
                actions = policy.decide(observation)
                assert observation == before
                pair = [[], []]
                pair[side] = actions
                records = engine.play_round(pair)
                assert all(e['accepted'] for record in records for e in record['event'] if e['kind'] == 'action')
                rows.append(dict(round=rnd, actions=actions))
            checks.append(dict(policy=name, side=side, rounds=rows))
    assert all(digest(p) == h for p, h in sources.items())
    result = dict(time_utc=datetime.now(timezone.utc).isoformat(), runtime_seconds=time.perf_counter()-started,
                  source_sha256=sources, restored_sha256=GOOD, incompatible_sha256=BAD,
                  affected_validation_freezes=freezes, team_stream_snapshots=streams,
                  restored_constructor_checks=checks,
                  total_streams=len(streams), total_rows=sum(s['counts']['rows'] for s in streams),
                  bad_hash_rows=sum(s['counts']['bad_hash'] for s in streams),
                  other_hash_rows=sum(s['counts']['other_hash'] for s in streams),
                  dependent_error_rows=sum(len(s['dependent_error_rows']) for s in streams),
                  scope='Complete newline-terminated prefixes of the listed result streams only. Later appends, absent streams, unsaved failures, and already-running processes are not ruled out. Hash presence records loaded modules and does not establish the exact in-memory implementation. Recorded errors and wrong-hash rows must be excluded, not scored as losses. Fresh-process original-engine prefixes check restored constructors, legal actions and observation immutability, not full-game strength.')
    atomic_json(args.output, result, exclusive=True)
    print(json.dumps({k: result[k] for k in ('time_utc','runtime_seconds','total_streams','total_rows','bad_hash_rows','other_hash_rows','dependent_error_rows')}), flush=True)
    for stream in streams:
        if stream['anomalous_hash_rows'] or stream['dependent_error_rows']:
            print(json.dumps({k:stream[k] for k in ('path','counts','anomalous_hash_rows','dependent_error_rows')}), flush=True)

if __name__ == '__main__':
    main()
