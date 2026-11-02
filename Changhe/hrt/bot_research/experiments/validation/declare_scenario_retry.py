"""Declare a paired, longer retry of timed-out known-prefix cases.

All original attempts must finish first. The manifest keeps each selected
case verbatim, so a successful other seat is a repeat control, not a new
condition. It cannot silently drop a timed-out case or replace its policy.
"""
import argparse
import hashlib
import json
from pathlib import Path
from bot_research.experiments.validation.artifact_io import atomic_json
from bot_research.experiments.validation.final_validation import now


def digest(path):
    return hashlib.sha256(Path(path).read_bytes()).hexdigest()


def main():
    p = argparse.ArgumentParser()
    p.add_argument('--input-dir',required=True)
    p.add_argument('--source-manifest',required=True)
    p.add_argument('--output',required=True)
    p.add_argument('--timeout',type=int,default=450)
    a = p.parse_args()
    d = Path(a.input_dir)
    freeze = json.loads((d/'freeze.json').read_text())
    assert digest(a.source_manifest)==freeze['manifest_sha256']
    assert all(Path(name).is_file() and digest(name)==expected
               for name,expected in freeze['source_sha256'].items())
    jobs = json.loads((d/'jobs.json').read_text())
    evidence = {str(d/name):digest(d/name) for name in ('freeze.json','jobs.json')}
    evidence[a.source_manifest] = digest(a.source_manifest)
    failures, successful = [], []
    for job in jobs:
        path = d/'results'/(job['id']+'.json')
        failure = path.with_suffix('.failure.json')
        if failure.exists():
            data = json.loads(failure.read_text())
            assert 'timeout_seconds' in data, 'Review non-timeout failures separately.'
            evidence[str(failure)] = digest(failure)
            failures.append(job['condition'])
        elif path.exists():
            successful.append(job['condition'])
        else:
            raise ValueError('Finish all original attempts before declaring retries.')
    assert failures, 'No timeout requires retry.'
    source = json.loads(Path(a.source_manifest).read_text())
    selected_ids = {c['candidate_id'] for c in failures}
    selected = [c for c in source['cases'] if c['candidate']['id'] in selected_ids]
    assert {c['candidate']['id'] for c in selected}==selected_ids
    out = dict(declared_utc=now(),purpose=f'Paired retries of recorded known-prefix timeouts with {a.timeout} seconds per match; successful other seats are repeat controls.',
        cases=selected,retry_of_directory=a.input_dir,requested_timeout_seconds=a.timeout,
        prior_failed_conditions=failures,
        repeat_control_conditions=[c for c in successful if c['candidate_id'] in selected_ids],
        original_evidence_sha256=evidence,original_source_sha256=freeze['source_sha256'],
        scope='No new independent condition. Combine with the base campaign under retry-aware strict accounting. Original failures remain visible.')
    atomic_json(a.output,out,exclusive=True)
    print(json.dumps(dict(declared_utc=out['declared_utc'],paired_cases=len(selected),prior_timeouts=len(failures),
                         repeat_controls=len(out['repeat_control_conditions']))))


if __name__=='__main__':
    main()
