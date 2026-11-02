"""Retire a partial timeout-limited campaign and retry every original condition.

Unlike the completed-campaign selector, this retains all unstarted cases.
It permits no condition or policy selection based on observed outcomes.
Call only after the previous bounded runner has exited.
"""
import argparse
from datetime import datetime, timezone
import hashlib
import json
from pathlib import Path

from bot_research.experiments.validation.artifact_io import atomic_json


def digest(path):
    return hashlib.sha256(Path(path).read_bytes()).hexdigest()


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('--input-dir', required=True)
    parser.add_argument('--source-manifest', required=True)
    parser.add_argument('--output', required=True)
    parser.add_argument('--timeout', type=int, required=True)
    args = parser.parse_args()
    directory = Path(args.input_dir)
    freeze = json.loads((directory/'freeze.json').read_text())
    assert digest(args.source_manifest) == freeze['manifest_sha256']
    assert freeze['match_timeout'] < args.timeout <= 500
    assert all(digest(p) == h for p, h in freeze['source_sha256'].items())
    jobs = json.loads((directory/'jobs.json').read_text())
    source = json.loads(Path(args.source_manifest).read_text())
    evidence = {str(directory/n): digest(directory/n) for n in ('freeze.json', 'jobs.json', 'summary.json')}
    evidence[args.source_manifest] = digest(args.source_manifest)
    attempts = []
    for job in jobs:
        result = directory/'results'/(job['id']+'.json')
        failure = directory/'results'/(job['id']+'.failure.json')
        replay = Path(job['replay_path'])
        if failure.exists():
            data = json.loads(failure.read_text())
            assert 'timeout_seconds' in data, 'Review non-timeout failures separately.'
            evidence[str(failure)] = digest(failure)
            status = 'timeout'
        elif result.exists():
            evidence[str(result)] = digest(result)
            status = 'completed_repeat_control'
        else:
            status = 'incomplete' if replay.exists() else 'unstarted'
        if replay.exists():
            evidence[str(replay)] = digest(replay)
        attempts.append(dict(job=job['id'], condition=job['condition'], prior_status=status))
    assert sum(a['prior_status'] == 'timeout' for a in attempts) >= 3
    output = dict(source)
    output.update(declared_utc=datetime.now(timezone.utc).isoformat(),
        purpose='Retry all originally declared known-prefix conditions with a longer uniform wall-time allowance after at least three consecutive 300-second timeouts; no condition selection.',
        retry_of_directory=args.input_dir, requested_timeout_seconds=args.timeout,
        original_evidence_sha256=evidence, original_attempts=attempts,
        target_source='bot_research/bots/best.py', target_sha256=digest('bot_research/bots/best.py'),
        scope='All original cases and both assignments are retained verbatim. Prior partial and failed attempts remain visible. This is a computational-budget revision, not additional independent evidence.')
    assert output['cases'] == source['cases']
    atomic_json(args.output, output, exclusive=True)
    print(json.dumps(dict(time_utc=output['declared_utc'], cases=len(output['cases']),
        prior_statuses={s:sum(a['prior_status']==s for a in attempts) for s in sorted({a['prior_status'] for a in attempts})})), flush=True)


if __name__ == '__main__':
    main()
