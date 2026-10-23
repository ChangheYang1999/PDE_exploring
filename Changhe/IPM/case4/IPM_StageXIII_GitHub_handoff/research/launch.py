#!/usr/bin/env python3
"""Run one explicitly chosen validation worker in a new guarded session."""
import argparse
import hashlib
import json
import os
from pathlib import Path
import subprocess
import time

ROOT=Path(__file__).resolve().parent
RUN=Path('/Users/caltech/research/IPM_R2_macpro_runs/verification_20261020_01')
REFERENCE=Path('/Users/caltech/research/IPM_R2_macpro_reference_20261020')


def main():
    p=argparse.ArgumentParser();p.add_argument('--label',required=True);p.add_argument('worker');p.add_argument('arguments',nargs=argparse.REMAINDER);a=p.parse_args()
    worker=(ROOT/a.worker).resolve()
    if ROOT not in worker.parents or not worker.is_file():raise ValueError('worker must be inside the absolute-loss workspace')
    manifest=json.loads((ROOT/'provenance/base_manifest.json').read_text())
    for name,sha in manifest.items():
        if hashlib.sha256((ROOT/'base'/name).read_bytes()).hexdigest()!=sha:raise ValueError('frozen dependency changed: '+name)
    cmd=[str(RUN/'native_venv/bin/python'),'-B',str(ROOT/'launch_tools/run_verified_stage11.py'),'--run-dir',str(RUN),'--reference-dir',str(REFERENCE),'--session-dir',str(ROOT/'resource_session'),'--work-dir',str(ROOT),'--label',a.label,'--',str(RUN/'native_venv/bin/python'),'-B',str(worker)]+a.arguments
    with (ROOT/'provenance/commands.jsonl').open('a') as f:
        f.write(json.dumps({'epoch':time.time(),'worker_sha256':hashlib.sha256(worker.read_bytes()).hexdigest(),'command':cmd})+'\n');f.flush();os.fsync(f.fileno())
    raise SystemExit(subprocess.call(cmd,cwd=ROOT,env=dict(os.environ,PYTHONDONTWRITEBYTECODE='1',LC_ALL='C',LANG='C')))


if __name__=='__main__':main()
