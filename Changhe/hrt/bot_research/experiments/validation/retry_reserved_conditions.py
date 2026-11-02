"""Retry explicitly failed reserved conditions without discarding first attempts.

The candidate, opponents, prefixes and source hashes remain unchanged. Only
the per-match wall-time allowance and evidence destination may differ.
"""
from __future__ import annotations
import argparse
import copy
import hashlib
import json
from pathlib import Path
import subprocess
import sys
import time
from bot_research.experiments.validation.artifact_io import atomic_json, public_diagnostic
from bot_research.experiments.validation.final_validation_strict import (
    archive_sources, drift, execution_context, now, read_result, summarize)


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('--campaign', required=True)
    parser.add_argument('--ids', nargs='+', required=True)
    parser.add_argument('--output-dir', required=True)
    parser.add_argument('--match-timeout', type=float, default=500)
    parser.add_argument('--max-seconds', type=float, default=50)
    parser.add_argument('--resume', action='store_true')
    args = parser.parse_args()
    if args.max_seconds <= 0 or args.match_timeout <= 0 or args.max_seconds + args.match_timeout > 580:
        parser.error('Positive time limits must sum to at most580 seconds.')
    source, out = Path(args.campaign), Path(args.output_dir)
    for path in (source, out):
        if path.is_absolute() or '..' in path.parts or path.parts[:3] != ('bot_research', 'runs', 'validation'):
            parser.error('Use relative validation campaign paths.')
    original = json.loads((source / 'freeze.json').read_text())
    originals = json.loads((source / 'jobs.json').read_text())
    if len(set(args.ids)) != len(args.ids):
        parser.error('Duplicate retry condition.')
    declared = {job['id']: job for job in originals}
    for name in args.ids:
        if name not in declared or not (source / 'results' / (name + '.failure.json')).is_file():
            parser.error('Retries must identify declared conditions with preserved failure records.')
    def check_sources():
        changed = drift(original['source_sha256'], original['source_root_modules'])
        if any(changed.values()):
            raise RuntimeError('Original frozen source changed: ' + repr(changed))
    check_sources()
    if args.resume:
        metadata = json.loads((out / 'freeze.json').read_text())
        jobs = json.loads((out / 'jobs.json').read_text())
        if metadata['source_sha256'] != original['source_sha256'] or metadata['retry_ids'] != args.ids:
            raise ValueError('Retry campaign differs from original source or declared conditions.')
        if metadata['match_timeout_seconds'] != args.match_timeout:
            raise ValueError('Retry timeout changed.')
    else:
        out.mkdir(parents=True, exist_ok=False)
        for name in ('jobs', 'results', 'replays'):
            (out / name).mkdir()
        metadata = copy.deepcopy(original)
        metadata.update(started_utc=now(), retry_of=str(source), retry_ids=args.ids,
                        original_freeze_sha256=hashlib.sha256((source / 'freeze.json').read_bytes()).hexdigest(),
                        match_timeout_seconds=args.match_timeout, runtime=execution_context(),
                        retry_runner_sha256=hashlib.sha256(Path(__file__).read_bytes()).hexdigest())
        archive_sources(metadata['source_sha256'], out)
        jobs = []
        for name in args.ids:
            job = copy.deepcopy(declared[name])
            job['replay_path'] = str(out / 'replays' / (name + '.jsonl'))
            jobs.append(job)
            atomic_json(out / 'jobs' / (name + '.json'), job, exclusive=True)
        atomic_json(out / 'freeze.json', metadata, exclusive=True)
        atomic_json(out / 'jobs.json', jobs, exclusive=True)
    started = time.perf_counter()
    for job in jobs:
        if time.perf_counter() - started >= args.max_seconds:
            break
        result = out / 'results' / (job['id'] + '.json')
        fail = out / 'results' / (job['id'] + '.failure.json')
        if result.exists() or fail.exists():
            continue
        check_sources()
        command = [sys.executable, '-B', '-m', 'bot_research.experiments.validation.isolated_match',
                   '--job', str(out / 'jobs' / (job['id'] + '.json')), '--output', str(result)]
        failure = None
        try:
            proc = subprocess.run(command, capture_output=True, text=True,
                                  timeout=args.match_timeout, check=False)
            if proc.returncode:
                failure = {'job': job['id'], 'time_utc': now(), 'returncode': proc.returncode,
                           'stderr': public_diagnostic(proc.stderr)[-12000:]}
            else:
                read_result(result, job, metadata['source_sha256'])
        except subprocess.TimeoutExpired:
            failure = {'job': job['id'], 'time_utc': now(), 'timeout_seconds': args.match_timeout}
        except (ValueError, KeyError, TypeError, OSError) as error:
            failure = {'job': job['id'], 'time_utc': now(), 'diagnostic': public_diagnostic(str(error))}
        if failure:
            atomic_json(fail, failure, exclusive=True)
        check_sources()
        status = summarize(out, jobs, metadata)
        print(json.dumps({'job': job['id'], 'completed_conditions': status['completed_conditions'],
                          'failed_conditions': status['failed_conditions']}), flush=True)
    print(json.dumps(summarize(out, jobs, metadata), sort_keys=True), flush=True)


if __name__ == '__main__':
    main()
