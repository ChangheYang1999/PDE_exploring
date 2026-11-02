"""Retry failed pool C conditions, retaining their original failures.

The declared source, opponent, prefix and candidate are fixed. The only
permitted differences are wall-time allowance and output destinations.
"""
from __future__ import annotations
import argparse
from copy import deepcopy
import hashlib
import json
from pathlib import Path
import subprocess
import sys
import time
from bot_research.experiments.validation.artifact_io import atomic_json, public_diagnostic
from bot_research.experiments.validation.final_validation_strict import (
    archive_sources, execution_context, now, read_result, summarize)
from bot_research.experiments.validation.late_validation import check_sources, make_jobs, MANIFEST


def digest(path):
    return hashlib.sha256(Path(path).read_bytes()).hexdigest()


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('--campaign', required=True)
    parser.add_argument('--ids', nargs='+', required=True)
    parser.add_argument('--output-dir', required=True)
    parser.add_argument('--paired-controls', action='store_true')
    parser.add_argument('--match-timeout', type=float, default=500)
    parser.add_argument('--max-seconds', type=float, default=40)
    parser.add_argument('--resume', action='store_true')
    args = parser.parse_args()
    if args.max_seconds <= 0 or args.match_timeout <= 0 or args.max_seconds + args.match_timeout > 560:
        parser.error('Positive invocation limit plus one match must be at most 560 seconds.')
    source, out = Path(args.campaign), Path(args.output_dir)
    for path in (source, out):
        if path.is_absolute() or '..' in path.parts or path.parts[:3] != ('bot_research', 'runs', 'validation'):
            parser.error('Use relative validation campaign paths.')
    original = json.loads((source / 'freeze.json').read_text())
    originals = json.loads((source / 'jobs.json').read_text())
    if original['pool'] != 'C' or not original['stress']:
        raise ValueError('Expected an original complete-design pool C campaign.')
    if digest(MANIFEST) != original['manifest_sha256']:
        raise ValueError('The original pool C declaration changed.')
    if originals != make_jobs(original['candidate'], 'C', json.loads(MANIFEST.read_text()), source, True):
        raise ValueError('Original jobs differ from the reserved declaration.')
    declared = {j['id']: j for j in originals}
    if len(set(args.ids)) != len(args.ids):
        parser.error('Duplicate retry condition.')
    selected = set(args.ids)
    for name in args.ids:
        if name not in declared or not (source / 'results' / (name + '.failure.json')).is_file():
            parser.error('Every requested retry must have a preserved original failure record.')
        if args.paired_controls:
            stem, side = name.rsplit('-side', 1)
            if side not in ('0', '1') or stem + '-side' + str(1-int(side)) not in declared:
                raise ValueError('Cannot identify the matching physical-assignment control.')
            selected.add(stem + '-side' + str(1-int(side)))
    selected_ids = [j['id'] for j in originals if j['id'] in selected]
    check_sources(original)
    if args.resume:
        metadata = json.loads((out / 'freeze.json').read_text())
        jobs = json.loads((out / 'jobs.json').read_text())
        if (metadata['source_sha256'] != original['source_sha256'] or
            metadata['retry_ids'] != args.ids or metadata['selected_ids'] != selected_ids or
            metadata['match_timeout_seconds'] != args.match_timeout or
            metadata['original_freeze_sha256'] != digest(source / 'freeze.json')):
            raise ValueError('Retry arguments differ from the saved declaration.')
    else:
        out.mkdir(parents=True, exist_ok=False)
        for name in ('jobs', 'results', 'replays'):
            (out / name).mkdir()
        metadata = deepcopy(original)
        metadata.update(started_utc=now(), retry_of=str(source), retry_ids=args.ids,
            selected_ids=selected_ids, paired_controls=args.paired_controls,
            original_freeze_sha256=digest(source / 'freeze.json'),
            match_timeout_seconds=args.match_timeout, runtime=execution_context(),
            retry_runner_sha256=digest(__file__))
        archive_sources(metadata['source_sha256'], out)
        jobs = []
        for name in selected_ids:
            job = deepcopy(declared[name])
            job['replay_path'] = str(out / 'replays' / (name + '.jsonl'))
            jobs.append(job)
            atomic_json(out / 'jobs' / (name + '.json'), job, exclusive=True)
        atomic_json(out / 'freeze.json', metadata, exclusive=True)
        atomic_json(out / 'jobs.json', jobs, exclusive=True)
    expected = []
    for name in selected_ids:
        job = deepcopy(declared[name])
        job['replay_path'] = str(out / 'replays' / (name + '.jsonl'))
        expected.append(job)
    if jobs != expected:
        raise ValueError('Saved retry jobs changed original conditions.')
    started = time.perf_counter()
    for job in jobs:
        if time.perf_counter() - started >= args.max_seconds:
            break
        result = out / 'results' / (job['id'] + '.json')
        fail = out / 'results' / (job['id'] + '.failure.json')
        if result.exists() or fail.exists():
            continue
        check_sources(original)
        command = [sys.executable, '-B', '-m', 'bot_research.experiments.validation.isolated_match',
            '--job', str(out / 'jobs' / (job['id'] + '.json')), '--output', str(result)]
        failure = None
        try:
            proc = subprocess.run(command, capture_output=True, text=True,
                timeout=args.match_timeout, check=False)
            if proc.returncode:
                failure = dict(job=job['id'], time_utc=now(), returncode=proc.returncode,
                    stderr=public_diagnostic(proc.stderr)[-12000:])
            else:
                read_result(result, job, metadata['source_sha256'])
        except subprocess.TimeoutExpired:
            failure = dict(job=job['id'], time_utc=now(), timeout_seconds=args.match_timeout)
        except (ValueError, KeyError, TypeError, OSError) as error:
            failure = dict(job=job['id'], time_utc=now(), diagnostic=public_diagnostic(str(error)))
        if failure is not None:
            atomic_json(fail, failure, exclusive=True)
        check_sources(original)
        status = summarize(out, jobs, metadata)
        print(json.dumps(dict(job=job['id'], completed=status['completed_conditions'],
            failures=len(status['failed_conditions']))), flush=True)
    print(json.dumps(summarize(out, jobs, metadata), sort_keys=True), flush=True)


if __name__ == '__main__':
    main()
