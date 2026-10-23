#!/usr/bin/env python3
"""Record immutable hashes for a fresh reproduction's expected v1 failure.

Standard library only; no numerical engine is imported and no result is
modified. The record is required before auditing a separately passing recovery.
"""
import hashlib
import json
from pathlib import Path
import time

ROOT=Path(__file__).resolve().parent


def digest(path):return hashlib.sha256(Path(path).read_bytes()).hexdigest()


def main():
    target=ROOT/'provenance/global_derivative_v1_failure.json'
    if target.exists():raise FileExistsError('Preserved failure manifest already exists')
    path=ROOT/'results/derivatives/global/checks.json'
    failed=json.loads(path.read_text())
    if (failed.get('completed') is not True or failed.get('passed') is not False
        or len(failed.get('raw_checks',[]))!=31
        or not all(row.get('passed') is True for row in failed['raw_checks'])
        or 'normal system is unresolved' not in failed.get('feasible_chart_failure','')):
        raise ValueError('The expected complete original global v1 failure was not recorded')
    arrays=Path(failed['arrays_path']).resolve()
    if ROOT not in arrays.parents or digest(arrays)!=failed['arrays_sha256']:
        raise ValueError('Failed numerical arrays are absent, outside the workspace, or changed')
    record={'schema':'absolute_global_derivative_v1_preserved_failure_v1','created_epoch':time.time(),
        'record_path':str(path),'record_sha256':digest(path),
        'arrays_path':str(arrays),'arrays_sha256':digest(arrays),
        'completed':True,'passed':False,'raw_checks':31,'all_raw_passed':True,
        'failure':failed['feasible_chart_failure'],'resource_run':failed['resource_run'],
        'source_sha256':failed['source_sha256'],'acceptance_requires_separate_recovery':True}
    target.parent.mkdir(parents=True,exist_ok=True)
    with target.open('x') as stream:json.dump(record,stream,indent=2);stream.write('\n')
    print(json.dumps({'preserved_failure_manifest':str(target),'numerical_execution':False}))


if __name__=='__main__':main()
