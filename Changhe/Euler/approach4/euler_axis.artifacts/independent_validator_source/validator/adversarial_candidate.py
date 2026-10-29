#!/usr/bin/env python3
import argparse,datetime,hashlib,json,time
from pathlib import Path
from independent_fields import PotentialField
from independent_adversarial import adversarial_audit
from independent_artifacts import source_identity,verify_source_identity

def main():
    parser=argparse.ArgumentParser()
    parser.add_argument('candidate',type=Path)
    parser.add_argument('--output',required=True,type=Path)
    parser.add_argument('--seed',type=int,default=828718)
    parser.add_argument('--sample-power',type=int,default=12)
    args=parser.parse_args()
    output=args.output.resolve();root=Path(__file__).resolve().parent
    if not output.is_relative_to(root.parent):raise ValueError('output outside verifier lane')
    if output.exists():raise FileExistsError('preserving existing adversarial record; choose a fresh output path')
    identity=source_identity(root,__file__)
    before=hashlib.sha256(args.candidate.read_bytes()).hexdigest();start=time.time()
    field=PotentialField.load(args.candidate)
    result=adversarial_audit(field,seed=args.seed,sample_power=args.sample_power)
    if before!=hashlib.sha256(args.candidate.read_bytes()).hexdigest():raise RuntimeError('candidate changed during evaluation')
    verify_source_identity(root,identity)
    result.update(candidate_sha256=before,candidate_path=str(args.candidate.resolve()),
                  completed_utc=datetime.datetime.now(datetime.timezone.utc).isoformat(),elapsed_seconds=time.time()-start,
                  source_sha256=identity)
    output.parent.mkdir(parents=True,exist_ok=True)
    tmp=output.with_suffix(output.suffix+'.tmp');tmp.write_text(json.dumps(result,indent=2,allow_nan=False)+'\n');tmp.replace(output)
    print(json.dumps({'output':str(output),'elapsed_seconds':result['elapsed_seconds'],'candidate_sha256':before}))
if __name__=='__main__':main()
