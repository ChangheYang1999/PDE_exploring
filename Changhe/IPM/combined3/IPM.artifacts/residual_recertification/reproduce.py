#!/usr/bin/env python3
"""Replay the saved certificate, or regenerate its primary evidence outside the repo."""
import argparse, hashlib, json, os, shutil, subprocess, sys, tempfile
from pathlib import Path
from repository_paths import find_repository_root

def main():
    p=argparse.ArgumentParser(description=__doc__)
    p.add_argument('--repo-root',type=Path)
    p.add_argument('--regenerate',action='store_true')
    p.add_argument('--workdir',type=Path)
    p.add_argument('--workers',type=int,default=20)
    args=p.parse_args()
    here=Path(__file__).resolve().parent
    repo=find_repository_root(args.repo_root)
    env=dict(os.environ,IPM_REPOSITORY_ROOT=str(repo),PYTHONDONTWRITEBYTECODE='1')
    def run(name,*values):
        command=[sys.executable,'-B',str(here/name),*map(str,values)]
        print('RUN',json.dumps(command),flush=True)
        subprocess.run(command,check=True,env=env)
    bindings=json.loads((here/'source_bindings.json').read_text())
    for rel,expected in bindings['source_and_evaluator_sha256'].items():
        assert hashlib.sha256((repo/rel).read_bytes()).hexdigest()==expected,rel
    run('verify_manifest.py','--manifest',here/'manifest.json','--repo-root',repo,'--strict')
    if args.regenerate:
        work=(args.workdir.resolve() if args.workdir else Path(tempfile.mkdtemp(prefix='ipm-residual-fresh-')))
        if work==repo or repo in work.parents:
            raise SystemExit('Regenerate primary evidence in a temporary directory outside the repository.')
        if work.exists() and any(work.iterdir()):
            raise SystemExit('Regeneration requires an empty output directory: '+str(work))
        work.mkdir(parents=True,exist_ok=True)
        for script in here.glob('*.py'):shutil.copy2(script,work/script.name)
        ipm=repo/'Changhe/IPM'
        run('origin_certificate.py','--ipm-root',ipm,'--output',work/'origin_certificate.json')
        run('origin_large_certificate.py','--ipm-root',ipm,'--field-data',work/'origin_certificate.json','--radius','1/1000','--output',work/'origin_large_certificate.json')
        run('far_certificate.py','--degree',2,'--radius','100000000000000000000','--output',work/'far_certificate.json')
        run('far_certificate.py','--degree',6,'--radius','1000000','--prefix-input',work/'far_certificate.json','--output',work/'far_degree6.json')
        run('run_finite.py','--rmin','1/1000','--rmax','1000000','--precision',640,'--workers',args.workers,'--outdir',work/'finite_data_core')
        output=work/'validated_summary.json'
    else:
        work=here
        output=(args.workdir.resolve() if args.workdir else Path(tempfile.mkdtemp(prefix='ipm-residual-replay-')))/'replayed_summary.json'
        output.parent.mkdir(parents=True,exist_ok=True)
    run('assemble_certificate.py','--repo-root',repo,'--workdir',work,'--finite-dir','finite_data_core','--origin-file','origin_large_certificate.json','--far-file','far_degree6.json','--far-prefix-file','far_certificate.json','--precision',1024,'--output',output)
    result=json.loads(output.read_text())
    if result['status']!='PASS':raise SystemExit('Certificate failed: '+str(output))
    print('PASS:',output,flush=True)

if __name__=='__main__':main()
