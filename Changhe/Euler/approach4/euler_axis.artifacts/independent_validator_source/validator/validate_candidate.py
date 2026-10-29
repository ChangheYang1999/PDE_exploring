#!/usr/bin/env python3
"""One-command independent saved-coefficient validation, never optimization."""
import argparse,datetime,hashlib,json,os,time
from pathlib import Path
import numpy as np
from independent_fields import PotentialField
from independent_diagnostics import diagnose
from independent_artifacts import source_identity,verify_source_identity

def main():
    parser=argparse.ArgumentParser()
    parser.add_argument('candidate',type=Path)
    parser.add_argument('--output',required=True,type=Path)
    parser.add_argument('--level',choices=['pilot','medium','fine'],default='pilot')
    parser.add_argument('--skip-direct',action='store_true')
    args=parser.parse_args()
    allowed=Path(__file__).resolve().parent.parent
    output=args.output.resolve()
    if not output.is_relative_to(allowed):
        raise ValueError('output must remain within the verifier lane')
    if (output/'summary.json').exists():raise FileExistsError('preserving existing validation; choose a fresh output directory')
    output.mkdir(parents=True,exist_ok=True)
    identity=source_identity(allowed/'axisymmetric_euler_24h',__file__)
    start=time.time()
    before=hashlib.sha256(args.candidate.read_bytes()).hexdigest()
    field=PotentialField.load(args.candidate)
    summary,arrays=diagnose(field,level=args.level,include_direct=not args.skip_direct)
    after=hashlib.sha256(args.candidate.read_bytes()).hexdigest()
    if before!=after:raise RuntimeError('candidate changed during validation')
    verify_source_identity(allowed/'axisymmetric_euler_24h',identity)
    summary.update(candidate_path=str(args.candidate.resolve()),candidate_sha256=before,
                   completed_utc=datetime.datetime.now(datetime.timezone.utc).isoformat(),elapsed_seconds=time.time()-start,
                   cpu_affinity=sorted(os.sched_getaffinity(0)),source_sha256=identity)
    (output/'summary.json.tmp').write_text(json.dumps(summary,indent=2,allow_nan=False)+'\n')
    (output/'summary.json.tmp').replace(output/'summary.json')
    np.savez_compressed(output/'arrays.npz',**arrays)
    print(json.dumps({'output':str(output),'candidate_sha256':before,'elapsed_seconds':summary['elapsed_seconds'],
                      'worst_primitive_relative_rms':max(x['primitive_relative_rms'] for x in summary['shells']),
                      'worst_q_relative_rms':max(x['q']['relative_rms'] for x in summary['shells']),
                      'worst_eta_relative_rms':max(x['eta']['relative_rms'] for x in summary['shells'])}),flush=True)

if __name__=='__main__':main()
