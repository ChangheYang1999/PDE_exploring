"""Reserved validation, fresh interpreter for every paired condition.

Use only after final freeze. Each invocation is bounded and may be resumed.
Source drift aborts the campaign. Failures never contribute a strength score.
"""
from __future__ import annotations
import argparse
import hashlib
import json
import os
import platform
import subprocess
import sys
import time
from collections import Counter
from datetime import datetime, timezone
from pathlib import Path
from bot_research.experiments.validation.artifact_io import atomic_json, public_diagnostic
from bot_research.experiments.validation.source_closure import job_source_roots, static_closure
from bot_research.experiments.validation.required_sources import validate_required_sources


def now():
    return datetime.now(timezone.utc).isoformat()


def digest(path):
    return hashlib.sha256(Path(path).read_bytes()).hexdigest()


def freeze_sources(root_modules):
    # Freeze the actual declared entry points and their static dependencies.
    # Unrelated research can continue without contaminating this campaign.
    paths = set(static_closure(set(root_modules) | {'bot_research.experiments.validation.final_validation_strict'}))
    paths.update(Path(p) for p in (
        'td_game/balanced.json', 'configs/balanced.json',
        'bot_research/experiments/validation/holdout_manifest.json'))
    return {str(p): digest(p) for p in sorted(paths) if p.is_file()}


def drift(frozen, root_modules):
    current = freeze_sources(root_modules)
    return {'added': sorted(current.keys() - frozen.keys()),
            'removed': sorted(frozen.keys() - current.keys()),
            'changed': sorted(p for p in current.keys() & frozen.keys() if current[p] != frozen[p])}


def archive_sources(frozen, directory):
    """Save exactly the bytes whose hashes were frozen; abort a concurrent edit."""
    for name, expected in frozen.items():
        source = Path(name)
        if source.is_absolute() or '..' in source.parts:
            raise ValueError('Source archive requires relative paths.')
        contents = source.read_bytes()
        if hashlib.sha256(contents).hexdigest() != expected:
            raise RuntimeError(f'Source changed before archival: {name}')
        target = directory / 'sources' / source
        target.parent.mkdir(parents=True, exist_ok=True)
        with target.open('xb') as stream:
            stream.write(contents)


def execution_context():
    return {'python_version': platform.python_version(), 'implementation': platform.python_implementation(),
            'platform': platform.system(), 'machine': platform.machine(),
            'cpu_affinity': sorted(os.sched_getaffinity(0)), 'nice': os.getpriority(os.PRIO_PROCESS, 0),
            'thread_limits': {k: os.environ.get(k) for k in
                ('OMP_NUM_THREADS', 'OPENBLAS_NUM_THREADS', 'MKL_NUM_THREADS')},
            'bytecode_disabled': bool(sys.dont_write_bytecode)}


def make_jobs(candidate, pool, manifest, directory, stress):
    profiles = manifest['pool_A_profiles' if pool == 'A' else 'pool_B_reserve_profiles']
    opponents = [{'profile': p} for p in profiles] + [{'spec': s} for s in manifest[f'pool_{pool}_factory_specs']]
    scenarios = [None] + (manifest['legal_opening_scenarios'] if stress else [])
    jobs = []
    for scenario in scenarios:
        scenario_name = 'standard' if scenario is None else scenario['name']
        for i, opponent in enumerate(opponents):
            for side in (0, 1):
                name = f'holdout_{pool}_{i:02d}'
                bots = [{'spec': candidate}, opponent]
                names = [candidate, name]
                if side:
                    bots.reverse()
                    names.reverse()
                job_id = f'{scenario_name}-{i:02d}-side{side}'
                job = {'id': job_id, 'names': names, 'bots': bots,
                       'replay_path': str(directory / 'replays' / f'{job_id}.jsonl'),
                       'condition': {'scenario': scenario_name, 'candidate_side': side,
                           'opponent': opponent, 'engine_seed': None, 'pool': pool,
                           'initial_state': 'standard' if scenario is None else 'legal prescribed round-one actions',
                           'strength_score_eligible': scenario is None}}
                if scenario is not None:
                    shared = scenario.get('both_players_round_1')
                    prefix = [[shared if shared is not None else scenario['candidate_round_1']],
                              [shared if shared is not None else scenario['opponent_round_1']]]
                    job['prefixes'] = prefix if side == 0 else list(reversed(prefix))
                jobs.append(job)
    return jobs


def read_result(path, job, frozen=None):
    result = json.loads(path.read_text())
    expected = 'D' if result['result']['winner'] is None else (
        'W' if result['result']['winner'] == job['condition']['candidate_side'] else 'L')
    if result['candidate_outcome'] != expected:
        raise ValueError('Candidate outcome disagrees with the engine winner.')
    if result['condition'] != job['condition']:
        raise ValueError('Result condition differs from prescribed job.')
    for name in ('bot_errors', 'rejected_actions', 'source_changed_during_match'):
        if name not in result:
            raise ValueError(f'Missing result field: {name}')
    if frozen is not None:
        for field in ('source_sha256', 'source_sha256_at_end'):
            loaded = result.get(field)
            if not isinstance(loaded, dict):
                raise ValueError(f'Missing loaded-source attestation: {field}')
            unknown = sorted(set(loaded) - set(frozen))
            differing = sorted(name for name, value in loaded.items()
                               if name in frozen and value != frozen[name])
            if unknown or differing:
                raise ValueError(f'Loaded sources differ from freeze: unknown={unknown}, changed={differing}')
    if frozen is not None:
        validate_required_sources(result, job, frozen)
    return result


def summarize(directory, jobs, metadata):
    scores = Counter()
    stress = Counter()
    failures = []
    invalid = []
    completed = []
    resolved = set()
    for job in jobs:
        path = directory / 'results' / f"{job['id']}.json"
        fail = directory / 'results' / f"{job['id']}.failure.json"
        if fail.exists():
            try:
                failure = json.loads(fail.read_text())
            except (ValueError, OSError):
                failure = {'job': job['id'], 'diagnostic': 'Unreadable failure record.'}
            failure['result_also_exists'] = path.exists()
            failures.append(failure)
            resolved.add(job['id'])
            continue
        if not path.exists():
            continue
        resolved.add(job['id'])
        try:
            result = read_result(path, job, metadata.get('source_sha256'))
        except (ValueError, OSError, KeyError, TypeError) as exc:
            failures.append({'job': job['id'], 'diagnostic': public_diagnostic(str(exc)),
                             'invalid_result_file': True})
            continue
        completed.append(result)
        if any(result['bot_errors']) or any(result['rejected_actions']) or result['source_changed_during_match']:
            invalid.append(job['id'])
            continue
        target = scores if job['condition']['strength_score_eligible'] else stress
        target[result['candidate_outcome']] += 1
    out = {'updated_utc': now(), 'candidate': metadata['candidate'], 'pool': metadata['pool'],
           'standard_initial_state': dict(scores), 'continuation_stress': dict(stress),
           'score_excludes_failed_or_invalid_conditions': True,
           'planned_conditions': len(jobs), 'completed_conditions': len(completed),
           'resolved_conditions': len(resolved), 'failed_conditions': failures,
           'conditions_with_errors_or_rejections_or_drift': invalid,
           'complete': len(resolved) == len(jobs),
           'all_completed_successfully': len(completed) == len(jobs) and not failures and not invalid,
           'interpretation': metadata['interpretation']}
    atomic_json(directory / 'summary.json', out)
    with (directory / 'matches.jsonl').open('w') as stream:
        for row in completed:
            stream.write(json.dumps(row, sort_keys=True) + '\n')
    return out


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('--candidate', default='bot_research.bots.best:decide')
    parser.add_argument('--pool', choices=('A', 'B'), required=True)
    parser.add_argument('--output-dir', required=True)
    parser.add_argument('--continuation-stress', action='store_true')
    parser.add_argument('--resume', action='store_true')
    parser.add_argument('--max-seconds', type=float, default=240)
    parser.add_argument('--match-timeout', type=float, default=300)
    args = parser.parse_args()
    if args.max_seconds <= 0 or args.match_timeout <= 0 or args.max_seconds + args.match_timeout > 580:
        parser.error('Positive invocation limit plus one match must stay below 580 seconds.')
    directory = Path(args.output_dir)
    if directory.is_absolute() or '..' in directory.parts or directory.parts[:3] != ('bot_research', 'runs', 'validation'):
        parser.error('Use a relative output directory under bot_research/runs/validation/.')
    manifest_path = Path('bot_research/experiments/validation/holdout_manifest.json')
    if args.resume:
        metadata = json.loads((directory / 'freeze.json').read_text())
        if (metadata['candidate'], metadata['pool'], metadata['stress']) != (args.candidate, args.pool, args.continuation_stress):
            parser.error('Resume settings differ from frozen campaign.')
        if args.max_seconds + metadata['match_timeout_seconds'] > 580:
            parser.error('Invocation limit plus the frozen match timeout exceeds 580 seconds.')
        jobs = json.loads((directory / 'jobs.json').read_text())
    else:
        directory.mkdir(parents=True, exist_ok=False)
        for subdir in ('jobs', 'results', 'replays'):
            (directory / subdir).mkdir()
        manifest = json.loads(manifest_path.read_text())
        jobs = make_jobs(args.candidate, args.pool, manifest, directory, args.continuation_stress)
        root_modules = job_source_roots(jobs)
        metadata = {'started_utc': now(), 'candidate': args.candidate, 'pool': args.pool,
                    'freeze_schema': 2, 'source_root_modules': root_modules,
                    'stress': args.continuation_stress, 'source_sha256': freeze_sources(root_modules),
                    'manifest_sha256': digest(manifest_path), 'match_timeout_seconds': args.match_timeout,
                    'interpretation': manifest['interpretation_limit'], 'runtime': execution_context(),
                    'execution': 'one fresh Python process per match; both assignments; original Engine'}
        archive_sources(metadata['source_sha256'], directory)
        atomic_json(directory / 'freeze.json', metadata, exclusive=True)
        atomic_json(directory / 'jobs.json', jobs, exclusive=True)
        for job in jobs:
            atomic_json(directory / 'jobs' / f"{job['id']}.json", job, exclusive=True)
    changed = drift(metadata['source_sha256'], metadata['source_root_modules'])
    if any(changed.values()):
        raise RuntimeError(f'Frozen sources changed: {changed}')
    started = time.perf_counter()
    for job in jobs:
        result_path = directory / 'results' / f"{job['id']}.json"
        failure_path = directory / 'results' / f"{job['id']}.failure.json"
        if result_path.exists() or failure_path.exists():
            continue
        changed = drift(metadata['source_sha256'], metadata['source_root_modules'])
        if any(changed.values()):
            raise RuntimeError(f'Frozen sources changed: {changed}')
        if time.perf_counter() - started >= args.max_seconds:
            break
        command = [sys.executable, '-B', '-m', 'bot_research.experiments.validation.isolated_match',
                   '--job', str(directory / 'jobs' / f"{job['id']}.json"), '--output', str(result_path)]
        failure = None
        try:
            proc = subprocess.run(command, timeout=metadata['match_timeout_seconds'], capture_output=True, text=True, check=False)
            if proc.returncode:
                failure = {'job': job['id'], 'time_utc': now(), 'returncode': proc.returncode,
                           'stderr': public_diagnostic(proc.stderr)[-12000:]}
            else:
                try:
                    read_result(result_path, job, metadata['source_sha256'])
                except (ValueError, OSError, KeyError, TypeError) as exc:
                    failure = {'job': job['id'], 'time_utc': now(), 'invalid_or_missing_result': True,
                               'diagnostic': public_diagnostic(str(exc))}
        except subprocess.TimeoutExpired:
            failure = {'job': job['id'], 'time_utc': now(), 'timeout_seconds': metadata['match_timeout_seconds']}
        if failure:
            atomic_json(failure_path, failure, exclusive=True)
        changed = drift(metadata['source_sha256'], metadata['source_root_modules'])
        if any(changed.values()):
            raise RuntimeError(f'Frozen sources changed during match: {changed}')
        summary = summarize(directory, jobs, metadata)
        print(json.dumps({'finished': job['id'], 'standard': summary['standard_initial_state'],
                          'failures': len(summary['failed_conditions'])}), flush=True)
    print(json.dumps(summarize(directory, jobs, metadata), sort_keys=True), flush=True)


if __name__ == '__main__':
    main()
