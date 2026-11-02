"""Check candidate entry points in bounded fresh processes, with resumable evidence.

Every result is checked by check_best_entrypoints on the original Engine. The wrapper
keeps failures separate and never rewrites an existing per-job audit.
"""
from __future__ import annotations
import argparse
from collections import Counter
import hashlib
import json
from pathlib import Path
import subprocess
import sys
import time
from bot_research.experiments.validation.artifact_io import atomic_json, public_diagnostic
from bot_research.experiments.validation.final_validation_strict import now


def digest(path):
    return hashlib.sha256(Path(path).read_bytes()).hexdigest()


def summarize(campaign, out, jobs, metadata):
    cases = []
    for job in jobs:
        name = job['id']
        result = campaign / 'results' / (name + '.json')
        audit = out / 'audits' / (name + '.json')
        failure = out / 'failures' / (name + '.json')
        row = {'job': name, 'result_path': str(result)}
        if failure.exists():
            row.update(status='failed', failure=json.loads(failure.read_text()))
        elif audit.exists():
            record = json.loads(audit.read_text())
            if record['count'] != 1 or not record['all_passed']:
                row.update(status='invalid_audit', audit_path=str(audit))
            elif not result.exists() or record['input_sha256'].get(str(result)) != digest(result):
                row.update(status='result_changed_after_audit', audit_path=str(audit))
            else:
                row.update(status='passed', audit_path=str(audit), audit_sha256=digest(audit),
                           runtime_seconds=record['runtime_seconds'])
        else:
            row['status'] = 'pending' if result.exists() else 'match_not_complete'
        cases.append(row)
    counts = dict(Counter(row['status'] for row in cases))
    summary = {'time_utc': now(), 'campaign': str(campaign), 'started_utc': metadata['started_utc'],
               'planned_jobs': len(jobs), 'counts': counts, 'all_passed': counts == {'passed': len(jobs)},
               'cases': cases, 'entrypoint_runtime_seconds_sum': sum(c.get('runtime_seconds', 0) for c in cases),
               'scope': 'Fresh direct/factory candidate regeneration and original-engine replay. Not new strength samples.'}
    atomic_json(out / 'summary.json', summary)
    return summary


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('--campaign', required=True)
    parser.add_argument('--module', default='bot_research.bots.best')
    parser.add_argument('--candidate-sha256', required=True)
    parser.add_argument('--output-dir', required=True)
    parser.add_argument('--shard', type=int, default=0)
    parser.add_argument('--shards', type=int, default=1)
    parser.add_argument('--max-seconds', type=float, default=240)
    parser.add_argument('--match-timeout', type=float, default=300)
    parser.add_argument('--resume', action='store_true')
    args = parser.parse_args()
    if not 0 <= args.shard < args.shards or args.max_seconds <= 0 or args.match_timeout <= 0 or args.max_seconds + args.match_timeout > 580:
        parser.error('Use valid shards and positive limits with sum <=580 seconds.')
    campaign, out = Path(args.campaign), Path(args.output_dir)
    for path in (campaign, out):
        if path.is_absolute() or '..' in path.parts or path.parts[:3] != ('bot_research', 'runs', 'validation'):
            parser.error('Campaign and output must be relative validation run directories.')
    all_jobs = json.loads((campaign / 'jobs.json').read_text())
    all_jobs = [j for j in all_jobs if j['bots'][j['condition']['candidate_side']].get('spec','').partition(':')[0] == args.module]
    if not all_jobs:
        raise ValueError('No matching candidate jobs.')
    candidate_path = args.module.replace('.', '/') + '.py'
    if digest(candidate_path) != args.candidate_sha256:
        raise ValueError('Candidate source differs from requested freeze.')
    jobs = [j for i,j in enumerate(all_jobs) if i % args.shards == args.shard]
    source_inputs = {str(campaign / 'jobs.json'): digest(campaign / 'jobs.json'),
                     str(campaign / 'freeze.json'): digest(campaign / 'freeze.json'),
                     str(Path(__file__).relative_to(Path.cwd())): digest(__file__),
                     'bot_research/experiments/validation/check_best_entrypoints.py': digest('bot_research/experiments/validation/check_best_entrypoints.py'),
                     candidate_path: args.candidate_sha256}
    if args.resume:
        metadata = json.loads((out / 'metadata.json').read_text())
        if metadata['inputs'] != source_inputs or metadata['shard'] != args.shard or metadata['shards'] != args.shards:
            raise ValueError('Replay campaign definition changed.')
        if args.match_timeout != metadata['match_timeout_seconds']:
            raise ValueError('Replay timeout changed; use a separate documented retry campaign.')
    else:
        out.mkdir(parents=True, exist_ok=False)
        for name in ('audits', 'failures', 'logs'):
            (out / name).mkdir()
        metadata = {'started_utc': now(), 'campaign': str(campaign), 'inputs': source_inputs,
                    'shard': args.shard, 'shards': args.shards, 'match_timeout_seconds': args.match_timeout}
        atomic_json(out / 'metadata.json', metadata, exclusive=True)
    started = time.perf_counter()
    for job in jobs:
        if time.perf_counter() - started >= args.max_seconds:
            break
        result = campaign / 'results' / (job['id'] + '.json')
        output = out / 'audits' / (job['id'] + '.json')
        failure_path = out / 'failures' / (job['id'] + '.json')
        if output.exists() or failure_path.exists() or not result.exists():
            continue
        command = [sys.executable, '-B', '-m', 'bot_research.experiments.validation.check_best_entrypoints',
                   '--campaign', str(campaign), '--job', job['id'], '--module', args.module,
                   '--candidate-sha256', args.candidate_sha256, '--output', str(output)]
        failure = None
        try:
            proc = subprocess.run(command, capture_output=True, text=True, timeout=args.match_timeout, check=False)
            (out / 'logs' / (job['id'] + '.log')).write_text(public_diagnostic(proc.stdout + proc.stderr))
            if proc.returncode:
                failure = {'time_utc': now(), 'returncode': proc.returncode,
                           'diagnostic': public_diagnostic(proc.stderr)[-12000:]}
        except subprocess.TimeoutExpired:
            failure = {'time_utc': now(), 'timeout_seconds': args.match_timeout}
        if failure:
            atomic_json(failure_path, failure, exclusive=True)
        summary = summarize(campaign, out, jobs, metadata)
        print(json.dumps({'job': job['id'], 'counts': summary['counts']}), flush=True)
    print(json.dumps(summarize(campaign, out, jobs, metadata), sort_keys=True), flush=True)


if __name__ == '__main__':
    main()
