"""Check reserved parameter overlap in recorded development declarations.

This is an exact normalized-parameter audit, not a proof of behavioral novelty
or of the absence of every possible unrecorded execution. Shared families and
legal opening actions remain visible and are not treated as secret test data.
"""
from __future__ import annotations
import argparse
from collections import Counter
from dataclasses import asdict
from datetime import datetime
import hashlib
import inspect
import json
from pathlib import Path
import re
from urllib.parse import parse_qsl
from bot_research.bots.counters import pool
from bot_research.bots.counters.archetypes import Profile, PROFILES
from bot_research.experiments.validation.artifact_io import atomic_json
from bot_research.experiments.validation.final_validation_strict import now


def digest(raw):
    return hashlib.sha256(raw).hexdigest()


def canonical(description):
    if 'profile' in description:
        parameters = dict(description['profile'])
        if 'roster' in parameters:
            parameters['roster'] = tuple(parameters['roster'])
        return json.dumps({'family': 'Archetype', 'parameters': asdict(Profile(**parameters))}, sort_keys=True)
    module, colon, suffix = description['spec'].partition(':')
    if not colon:
        return json.dumps(description, sort_keys=True)
    name, _, query = suffix.lstrip('@').partition('?')
    parameters = {}
    for key, text in parse_qsl(query, keep_blank_values=True):
        try:
            parameters[key] = json.loads(text)
        except json.JSONDecodeError:
            parameters[key] = text
    if module == 'bot_research.bots.counters.pool':
        if name == 'archetype':
            label = parameters.pop('name', 'rush_t1')
            profile = parameters if parameters else asdict(PROFILES[label])
            return canonical({'profile': profile})
        if name == 'stacker':
            binding = inspect.signature(pool.stacker).bind(**parameters)
            binding.apply_defaults()
            p = binding.arguments
            return canonical({'profile': {'growth_rounds': p['growth_rounds'],
                'roster': [p['tier']], 'defense': 'splash' if p['initial_splash'] else '',
                'defense_count': int(p['initial_splash']), 'purchase_cap': p['batch_cap'],
                'factory_cap': 2000}})
        if name in ('turtle', 'mirror', 'random_legal'):
            binding = inspect.signature(getattr(pool, name)).bind(**parameters)
            binding.apply_defaults()
            parameters = dict(binding.arguments)
    if module == 'bot_research.bots.counters.archetypes' and name in PROFILES and not parameters:
        return canonical({'profile': asdict(PROFILES[name])})
    return json.dumps({'family': module + ':' + name, 'parameters': parameters}, sort_keys=True)


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('--campaign', required=True)
    parser.add_argument('--output', required=True)
    args = parser.parse_args()
    campaign = Path(args.campaign)
    freeze = json.loads((campaign / 'freeze.json').read_text())
    cutoff = datetime.fromisoformat(freeze['started_utc'])
    manifest_path = campaign / 'sources/bot_research/experiments/validation/holdout_manifest.json'
    manifest_raw = manifest_path.read_bytes()
    manifest = json.loads(manifest_raw)
    targets = {}
    for letter, field in (('A', 'pool_A_profiles'), ('B', 'pool_B_reserve_profiles')):
        descriptions = [{'profile': p} for p in manifest[field]]
        descriptions += [{'spec': p} for p in manifest[f'pool_{letter}_factory_specs']]
        for i, description in enumerate(descriptions):
            key = canonical(description)
            if key in targets:
                raise ValueError('Reserved pools contain duplicate normalized parameters.')
            targets[key] = f'{letter}-{i:02d}'
    checked = Counter()
    overlaps, inputs, skipped, undated = [], {}, [], []
    inputs[str(manifest_path)] = digest(manifest_raw)
    for jobs_path in sorted(Path('bot_research/runs/validation').glob('*/jobs.json')):
        directory = jobs_path.parent
        meta_path = directory / 'freeze.json'
        started = None
        if meta_path.exists():
            meta_raw = meta_path.read_bytes()
            metadata = json.loads(meta_raw)
            started = metadata.get('started_utc')
            if started and datetime.fromisoformat(started) >= cutoff:
                continue
            inputs[str(meta_path)] = digest(meta_raw)
        if not started:
            undated.append({'path': str(jobs_path),
                'reason': 'No recorded campaign start; checked conservatively.'})
            checked['undated_validation_campaigns'] += 1
        raw = jobs_path.read_bytes()
        inputs[str(jobs_path)] = digest(raw)
        checked['validation_campaigns'] += 1
        for job in json.loads(raw):
            checked['registered_validation_jobs'] += 1
            for slot, description in enumerate(job.get('bots', [])):
                checked['registered_validation_slots'] += 1
                identity = canonical(description)
                if identity in targets:
                    result = directory / 'results' / (job['id'] + '.json')
                    overlaps.append({'source': str(jobs_path), 'job': job['id'], 'slot': slot,
                        'reserved_id': targets[identity], 'description': description,
                        'result_exists_at_audit': result.exists(),
                        'recorded_campaign_start': started})
    # Lead-format tournament rows from all three other lanes. The timestamp is
    # the recorded replay filename, not the current mtime of an append-only log.
    for lane in ('lead', 'defense', 'economy'):
        for path in sorted(Path('bot_research/runs', lane).glob('*/results.jsonl')):
            raw = path.read_bytes()
            inputs[str(path)] = digest(raw)
            checked['team_result_stream_snapshots'] += 1
            for index, line in enumerate(raw.splitlines()):
                try:
                    row = json.loads(line)
                except json.JSONDecodeError:
                    skipped.append({'path': str(path), 'line': index + 1, 'reason': 'Incomplete JSON line in snapshot.'})
                    continue
                match = re.search(r'(\d{8}T\d{6})-', Path(row.get('log') or '').name)
                stamp = None
                if match:
                    stamp = datetime.strptime(match.group(1), '%Y%m%dT%H%M%S').replace(tzinfo=cutoff.tzinfo)
                    if stamp >= cutoff:
                        continue
                    checked['team_completed_rows_started_before_cutoff'] += 1
                else:
                    undated.append({'path': str(path), 'line': index + 1,
                        'reason': 'No recorded start timestamp; checked conservatively.'})
                    checked['team_completed_rows_undated'] += 1
                for slot, field in enumerate(('spec_a', 'spec_b')):
                    if field not in row:
                        continue
                    description = {'spec': row[field]}
                    checked['team_completed_slots_started_before_cutoff' if stamp is not None
                            else 'team_completed_slots_undated'] += 1
                    identity = canonical(description)
                    if identity in targets:
                        overlaps.append({'source': str(path), 'line': index + 1, 'slot': slot,
                            'reserved_id': targets[identity], 'description': description,
                            'recorded_start': stamp.isoformat() if stamp is not None else None,
                            'record_sha256': digest(line),
                            'result_exists_at_audit': True})
    output = {'time_utc': now(), 'checker_sha256': digest(Path(__file__).read_bytes()),
        'input_snapshot_sha256': inputs, 'cutoff_utc': cutoff.isoformat(),
        'reserved_normalized_parameter_sets': len(targets), 'checked': dict(checked),
        'overlaps': overlaps, 'no_exact_normalized_parameter_overlap_found': not overlaps,
        'skipped_unrecognized_inputs': skipped,
        'undated_inputs_checked_conservatively': undated,
        'limits': [
            'Exact parameter equality only; this does not prove distinct behavior on every reachable observation.',
            'Opponent implementations and common opening actions are shared with development.',
            'Coverage is registered validation jobs and recognized team tournament result streams, not all possible executions.',
            'Undated records are checked regardless of whether they were before or after the cutoff; any overlap needs a separate timing investigation.',
            'Team stream hashes describe the bytes read at audit time; append-only streams may later grow.',
            'Registered jobs may not have executed; any overlap is reported conservatively even without a result.',
            'The cutoff is the first final-validation match campaign start, not a claimed secret-data access boundary.'
        ]}
    atomic_json(args.output, output, exclusive=True)
    print(json.dumps({k: output[k] for k in ('checked', 'reserved_normalized_parameter_sets', 'overlaps', 'no_exact_normalized_parameter_overlap_found')}))


if __name__ == '__main__':
    main()
