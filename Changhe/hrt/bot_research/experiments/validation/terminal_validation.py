"""Prospective pool D runner. Use only for an explicitly frozen late revision.

The manifest predates every candidate evaluation on this reserve. Scripted
histories are candidate-relative; no policy is called during its own prefix.
"""
from __future__ import annotations
import argparse
from copy import deepcopy
import json
from pathlib import Path
import subprocess
import sys
import time
from bot_research.experiments.validation.artifact_io import atomic_json, public_diagnostic
from bot_research.experiments.validation.final_validation_strict import (
    archive_sources, digest, execution_context, now, read_result, summarize)
from bot_research.experiments.validation.source_closure import job_source_roots, static_closure

MANIFEST = Path('bot_research/experiments/validation/terminal_holdout_manifest.json')


def make_jobs(candidate, pool, manifest, directory, stress):
    if pool != 'D' or manifest['pool'] != 'D':
        raise ValueError('This runner is only for the predeclared terminal reserve.')
    opponents = ([{'profile': p} for p in manifest['profiles']] +
                 [{'spec': s} for s in manifest['factory_specs']])
    scenarios = [None] + (manifest['scenarios'] if stress else [])
    jobs = []
    for scenario in scenarios:
        name = 'standard' if scenario is None else scenario['name']
        for i, opponent in enumerate(opponents):
            for side in (0, 1):
                bots = [{'spec': candidate}, deepcopy(opponent)]
                names = [candidate, f'holdout_D_{i:02d}']
                if side:
                    bots.reverse()
                    names.reverse()
                identifier = f'{name}-{i:02d}-side{side}'
                condition = dict(scenario=name, candidate_side=side, opponent=deepcopy(opponent),
                    engine_seed=None, pool='D', strength_score_eligible=scenario is None,
                    initial_state='standard' if scenario is None else 'candidate-relative legal prescribed prefix')
                job = dict(id=identifier, names=names, bots=bots, condition=condition,
                           replay_path=str(directory / 'replays' / (identifier + '.jsonl')))
                if scenario is not None:
                    prefixes = deepcopy(scenario['prefixes'])
                    if len(prefixes) != 2 or not all(isinstance(p, list) for p in prefixes):
                        raise ValueError('Every scenario needs two explicit per-player prefixes.')
                    job['prefixes'] = prefixes if side == 0 else list(reversed(prefixes))
                    condition['prefix_lengths_candidate_first'] = [len(p) for p in prefixes]
                    condition['prefix_policy_calls'] = 'skipped'
                jobs.append(job)
    if stress and len(jobs) != manifest['planned_conditions']:
        raise ValueError('Job count differs from the original declaration.')
    return jobs


def freeze_sources(roots, manifest):
    paths = set(static_closure(set(roots) | {
        'bot_research.experiments.validation.terminal_validation'}))
    paths.update(map(Path, manifest['source_sha256']))
    paths.update((MANIFEST, Path(manifest['prefix_check']),
                  Path('td_game/balanced.json'), Path('configs/balanced.json')))
    return {str(p): digest(p) for p in sorted(paths)}


def check_sources(metadata):
    changed = [name for name, expected in metadata['source_sha256'].items()
               if not Path(name).is_file() or digest(name) != expected]
    if changed:
        raise RuntimeError('Frozen sources changed: ' + repr(changed))


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('--candidate', required=True)
    parser.add_argument('--candidate-sha256', required=True)
    parser.add_argument('--output-dir', required=True)
    parser.add_argument('--resume', action='store_true')
    parser.add_argument('--max-seconds', type=float, default=480)
    parser.add_argument('--match-timeout', type=float, default=300)
    args = parser.parse_args()
    if not 0 < args.match_timeout < args.max_seconds <= 520:
        parser.error('Require 0 < match timeout < bounded invocation <= 520 seconds.')
    directory = Path(args.output_dir)
    if (directory.is_absolute() or '..' in directory.parts or
        directory.parts[:3] != ('bot_research', 'runs', 'validation')):
        parser.error('Use a relative validation output directory.')
    candidate_file = Path(args.candidate.partition(':')[0].replace('.', '/') + '.py')
    if digest(candidate_file) != args.candidate_sha256:
        raise ValueError('Candidate bytes do not match the explicit late freeze.')
    manifest = json.loads(MANIFEST.read_text())
    if args.resume:
        metadata = json.loads((directory / 'freeze.json').read_text())
        jobs = json.loads((directory / 'jobs.json').read_text())
        if (metadata['candidate'] != args.candidate or
            metadata['candidate_sha256'] != args.candidate_sha256 or
            metadata['manifest_sha256'] != digest(MANIFEST) or
            metadata['match_timeout_seconds'] != args.match_timeout):
            raise ValueError('Resume settings differ from the original freeze.')
        if jobs != make_jobs(args.candidate, 'D', manifest, directory, True):
            raise ValueError('Saved jobs differ from the declared reserve.')
    else:
        for name, expected in manifest['source_sha256'].items():
            if digest(name) != expected:
                raise ValueError('Reserved source changed since declaration: ' + name)
        if digest(manifest['prefix_check']) != manifest['prefix_check_sha256']:
            raise ValueError('Reserved prefix evidence changed.')
        jobs = make_jobs(args.candidate, 'D', manifest, directory, True)
        roots = job_source_roots(jobs)
        frozen = freeze_sources(roots, manifest)
        metadata = dict(started_utc=now(), candidate=args.candidate,
            candidate_sha256=args.candidate_sha256, pool='D', stress=True,
            freeze_schema=3, source_root_modules=roots, source_sha256=frozen,
            manifest_path=str(MANIFEST), manifest_sha256=digest(MANIFEST),
            match_timeout_seconds=args.match_timeout, runtime=execution_context(),
            interpretation=manifest['interpretation_limit'],
            execution='Fresh interpreter per condition; original Engine; explicit candidate-relative prefixes; skipped prefix policy calls.')
        directory.mkdir(parents=True, exist_ok=False)
        for subdir in ('jobs', 'results', 'replays'):
            (directory / subdir).mkdir()
        archive_sources(frozen, directory)
        atomic_json(directory / 'freeze.json', metadata, exclusive=True)
        atomic_json(directory / 'jobs.json', jobs, exclusive=True)
        for job in jobs:
            atomic_json(directory / 'jobs' / (job['id'] + '.json'), job, exclusive=True)
    check_sources(metadata)
    started = time.perf_counter()
    for job in jobs:
        result = directory / 'results' / (job['id'] + '.json')
        failed = directory / 'results' / (job['id'] + '.failure.json')
        if result.exists() or failed.exists():
            continue
        if args.max_seconds - (time.perf_counter() - started) < args.match_timeout + 2:
            break
        check_sources(metadata)
        command = [sys.executable, '-B', '-m', 'bot_research.experiments.validation.isolated_match',
                   '--job', str(directory / 'jobs' / (job['id'] + '.json')), '--output', str(result)]
        failure = None
        try:
            process = subprocess.run(command, capture_output=True, text=True,
                                     timeout=args.match_timeout, check=False)
            if process.returncode:
                failure = dict(job=job['id'], time_utc=now(), returncode=process.returncode,
                               stderr=public_diagnostic(process.stderr)[-12000:])
            else:
                read_result(result, job, metadata['source_sha256'])
        except subprocess.TimeoutExpired:
            failure = dict(job=job['id'], time_utc=now(), timeout_seconds=args.match_timeout)
        except (OSError, ValueError, KeyError, TypeError) as error:
            failure = dict(job=job['id'], time_utc=now(), diagnostic=public_diagnostic(str(error)))
        if failure is not None:
            atomic_json(failed, failure, exclusive=True)
        check_sources(metadata)
        summary = summarize(directory, jobs, metadata)
        print(json.dumps(dict(finished=job['id'], resolved=summary['resolved_conditions'],
                              failures=len(summary['failed_conditions']))), flush=True)
    print(json.dumps(summarize(directory, jobs, metadata), sort_keys=True), flush=True)


if __name__ == '__main__':
    main()
