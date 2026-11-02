"""Audit exact prescribed-history overlap before the pool C campaign.

No candidate or opponent policy is imported or called. Team scenario names are
reconstructed only when recorded generator and engine hashes match. The audit
covers declared histories, not equivalence of resulting positions or behavior.
"""
from __future__ import annotations

import argparse
from collections import Counter
from datetime import datetime, timezone
import hashlib
import json
from pathlib import Path
import re

from td_game.config import balanced_config
from td_game.engine import Engine
from bot_research.harness.scenarios import make_overrides
from bot_research.experiments.validation.artifact_io import atomic_json
from bot_research.experiments.validation.source_closure import static_closure

MANIFEST = Path('bot_research/experiments/validation/late_holdout_manifest.json')


def digest(raw):
    return hashlib.sha256(raw).hexdigest()


def identity(prefixes):
    """Keep action and round order; identify the two physical assignments."""
    if (not isinstance(prefixes, list) or len(prefixes) != 2 or
            any(not isinstance(p, list) for p in prefixes)):
        raise ValueError('Expected two ordered per-player prefixes.')
    for player in prefixes:
        for actions in player:
            if not isinstance(actions, list) or any(not isinstance(a, dict) for a in actions):
                raise ValueError('Expected lists of action dictionaries in every round.')
    return min(json.dumps(pair, sort_keys=True, separators=(',', ':'))
               for pair in (prefixes, list(reversed(prefixes))))


def reconstruct(name):
    if not re.fullmatch(r'(?:(?:mirror|asym):[0-9]+:[0-9]+|eco:[0-9]+)', name):
        raise ValueError('Unrecognized scenario grammar.')
    rounds = int(name.rsplit(':', 1)[1])
    if not 1 <= rounds <= 20:
        raise ValueError('Opening length outside audited range 1..20.')
    overrides = make_overrides(name)
    engine = Engine(balanced_config(), ('prefix_a', 'prefix_b'))
    prefixes = [[], []]
    for _ in range(rounds):
        actions = [overrides[i](engine.observation(i)) for i in (0, 1)]
        if any(not isinstance(a, list) for a in actions):
            raise ValueError('Scenario ended before its declared prefix length.')
        for i in (0, 1):
            prefixes[i].append(actions[i])
        records = engine.play_round(actions)
        if any(not event['accepted'] for record in records for event in record['event']
               if event['kind'] == 'action'):
            raise ValueError('A prescribed action was rejected by the original engine.')
        if engine.result is not None:
            raise ValueError('Scenario reached a terminal state during its prefix.')
    return prefixes


def main():
    parser = argparse.ArgumentParser()
    mode = parser.add_mutually_exclusive_group(required=True)
    mode.add_argument('--campaign')
    mode.add_argument('--cutoff', help='UTC timestamp for a preflight snapshot, not a final audit.')
    parser.add_argument('--output', required=True)
    args = parser.parse_args()
    snapshots = {}
    if args.campaign:
        directory = Path(args.campaign)
        raw = (directory / 'freeze.json').read_bytes()
        snapshots[str(directory / 'freeze.json')] = digest(raw)
        freeze = json.loads(raw)
        if freeze['pool'] != 'C':
            raise ValueError('Expected pool C freeze.')
        cutoff = datetime.fromisoformat(freeze['started_utc'])
        manifest_path = directory / 'sources' / MANIFEST
        raw = manifest_path.read_bytes()
        if digest(raw) != freeze['manifest_sha256']:
            raise ValueError('Archived reserve differs from campaign freeze.')
        preflight = False
    else:
        cutoff = datetime.fromisoformat(args.cutoff)
        manifest_path = MANIFEST
        raw = manifest_path.read_bytes()
        preflight = True
    if cutoff.tzinfo is None:
        raise ValueError('Cutoff must include a timezone.')
    snapshots[str(manifest_path)] = digest(raw)
    manifest = json.loads(raw)
    if manifest['pool'] != 'C':
        raise ValueError('Expected pool C manifest.')
    sources = set(static_closure({'td_game.config', 'td_game.engine',
                                 'bot_research.harness.scenarios'}))
    sources.update((Path('td_game/balanced.json'), Path('configs/balanced.json')))
    source_sha = {str(p): digest(p.read_bytes()) for p in sorted(sources)}
    if any(manifest['source_sha256'].get(p) != sha for p, sha in source_sha.items()):
        raise ValueError('Current prefix generator closure differs from reserve declaration.')
    targets, regenerated = {}, []
    for scenario in manifest['scenarios']:
        key = identity(scenario['prefixes'])
        if key in targets:
            raise ValueError('Duplicate normalized reserved prefix.')
        targets[key] = scenario['name']
        generated = reconstruct(scenario['generator'])
        if generated != scenario['prefixes']:
            raise ValueError('Reserved generator does not reproduce its exact declared history.')
        regenerated.append({'name': scenario['name'], 'prefix_sha256': digest(key.encode()),
                            'rounds_per_player': [len(p) for p in generated]})
    counts, overlaps, unknown, undated = Counter(), [], [], []
    def compare(prefixes, location):
        key = identity(prefixes)
        counts['complete_prescribed_histories_compared'] += 1
        if key in targets:
            overlaps.append(dict(location, reserved_scenario=targets[key]))
    for jobs_path in sorted(Path('bot_research/runs/validation').glob('*/jobs.json')):
        metadata = jobs_path.parent / 'freeze.json'
        started = None
        if metadata.exists():
            data = metadata.read_bytes()
            started = json.loads(data).get('started_utc')
            if started and datetime.fromisoformat(started) >= cutoff:
                continue
            snapshots[str(metadata)] = digest(data)
        if not started:
            undated.append({'path': str(jobs_path), 'reason': 'Missing campaign start; checked conservatively.'})
        data = jobs_path.read_bytes()
        snapshots[str(jobs_path)] = digest(data)
        counts['validation_campaigns'] += 1
        for job in json.loads(data):
            counts['registered_validation_jobs'] += 1
            if 'prefixes' in job:
                try:
                    compare(job['prefixes'], {'source': str(jobs_path), 'job': job['id'],
                        'recorded_start': started, 'kind': 'explicit_prefix'})
                except (ValueError, TypeError) as exc:
                    unknown.append({'source': str(jobs_path), 'job': job['id'], 'reason': str(exc)})
                counts['registered_jobs_with_prefixes'] += 1
            elif job.get('condition', {}).get('scenario') not in (None, 'standard'):
                unknown.append({'source': str(jobs_path), 'job': job['id'],
                                'reason': 'Named scenario without explicit prefixes.'})
    cache = {}
    for lane in ('lead', 'defense', 'economy'):
        for path in sorted(Path('bot_research/runs', lane).glob('*/results.jsonl')):
            data = path.read_bytes()
            snapshots[str(path)] = digest(data)
            counts['team_stream_snapshots'] += 1
            for index, line in enumerate(data.splitlines()):
                try:
                    row = json.loads(line)
                except json.JSONDecodeError:
                    unknown.append({'source': str(path), 'line': index + 1,
                                    'reason': 'Incomplete JSON line in snapshot.'})
                    continue
                match = re.search(r'(\d{8}T\d{6})-', Path(row.get('log') or '').name)
                stamp = None
                if match:
                    stamp = datetime.strptime(match.group(1), '%Y%m%dT%H%M%S').replace(tzinfo=timezone.utc)
                    if stamp >= cutoff:
                        continue
                counts['team_rows_considered'] += 1
                name = row.get('scenario')
                if name is None:
                    counts['standard_team_rows'] += 1
                    continue
                location = {'source': str(path), 'line': index + 1,
                            'recorded_start': stamp.isoformat() if stamp else None,
                            'scenario_generator': name, 'record_sha256': digest(line),
                            'kind': 'reconstructed_declared_scenario'}
                if stamp is None:
                    undated.append(dict(location, reason='Missing recorded start; checked conservatively.'))
                # Historical harness rows do not register the unchanged balanced JSON
                # files. Their hashes are still checked against the reserve declaration.
                missing = [p for p, sha in source_sha.items() if p.endswith('.py') and
                           row.get('sources', {}).get(p) != sha]
                if missing:
                    unknown.append(dict(location, reason='Recorded generator/engine closure differs or is absent.',
                                        unmatched_sources=missing))
                    continue
                try:
                    if name not in cache:
                        cache[name] = reconstruct(name)
                    compare(cache[name], location)
                    counts['team_named_scenario_rows_reconstructed'] += 1
                except (ValueError, TypeError) as exc:
                    unknown.append(dict(location, reason=str(exc)))
    output = {'time_utc': datetime.now(timezone.utc).isoformat(),
        'checker_sha256': digest(Path(__file__).read_bytes()), 'preflight_only': preflight,
        'cutoff_utc': cutoff.isoformat(), 'pool': 'C', 'candidate_or_opponent_calls': 0,
        'input_snapshot_sha256': snapshots, 'generator_source_sha256': source_sha,
        'reserved_histories_regenerated_exactly': regenerated, 'checked': dict(counts),
        'distinct_team_generators_reconstructed': sorted(cache), 'overlaps': overlaps,
        'no_exact_complete_history_overlap_found': not overlaps,
        'all_recognized_records_resolved': not unknown, 'unresolved_inputs': unknown,
        'undated_inputs_checked_conservatively': undated,
        'limits': [
            'Complete ordered action histories only, normalized under swapping both players. Common initial actions or equivalent resulting positions are not excluded.',
            'Coverage is registered validation jobs and recognized team result streams. Unlogged executions and other formats are outside this audit.',
            'Named team scenarios are reconstructed from matching recorded Python sources; team replay submissions are not audited here.',
            'Original balanced JSON files are checked against the reserve declaration; historical harness source lists do not register those JSON files.',
            'Registered jobs may not have run. Undated records are included conservatively, and append-only stream hashes describe only the captured bytes.',
            'The final cutoff is campaign start, not a claim that reserve definitions were inaccessible during development.',
            'A preflight snapshot must be repeated after the candidate freeze; it is not a final separation result.'
        ]}
    atomic_json(args.output, output, exclusive=True)
    print(json.dumps({k: output[k] for k in ('time_utc', 'preflight_only', 'checked',
          'no_exact_complete_history_overlap_found', 'all_recognized_records_resolved')}))


if __name__ == '__main__':
    main()
