#!/usr/bin/env python3
"""Terminate and resume a disposable validator; compare untouched holdout data."""
from pathlib import Path
import datetime,hashlib,json,os,subprocess,sys,time
import numpy as np
ROOT=Path(__file__).resolve().parents[1]

def main():
    stamp=datetime.datetime.now(datetime.timezone.utc).strftime('%Y%m%dT%H%M%S.%fZ')
    out=ROOT/'results'/'resume_tests'/stamp;out.mkdir(parents=True)
    fixture=ROOT/'checkpoints/MANUFACTURED_operator_fixture.json'
    command=[sys.executable,str(ROOT/'registered_candidate.py'),str(fixture),'--no-origin','--shells','-1','0','--pressure-lmax','10','--pressure-angle','28','--pressure-radial','20']
    start=time.time();checks=[];exception=None
    try:
        with (out/'interrupted.log').open('w') as log:
            proc=subprocess.Popen(command+['--output',str(out/'resumed')],cwd=ROOT.parent,stdout=log,stderr=subprocess.STDOUT,env=os.environ.copy())
            deadline=time.monotonic()+90
            while not (out/'resumed/progress.json').exists():
                if proc.poll() is not None:raise RuntimeError('validator ended before interruption point')
                if time.monotonic()>deadline:proc.kill();raise TimeoutError('first checkpoint did not arrive')
                time.sleep(.05)
            progress=json.loads((out/'resumed/progress.json').read_text())
            proc.terminate();returncode=proc.wait(timeout=10)
            checks.append({'name':'real_interruption_after_checkpoint','passed':returncode==-15,'returncode':returncode,
                           'completed_rows':len(progress['rows']),'utc':datetime.datetime.now(datetime.timezone.utc).isoformat()})
        for name,extra in [('resumed',['--resume']),('uninterrupted',[])]:
            with (out/(name+'.log')).open('w') as log:
                done=subprocess.run(command+['--output',str(out/name)]+extra,cwd=ROOT.parent,stdout=log,stderr=subprocess.STDOUT,timeout=120,check=False)
            checks.append({'name':name+'_exit','passed':done.returncode==0,'returncode':done.returncode})
            if done.returncode:raise RuntimeError(name+' failed')
        A=json.loads((out/'resumed/summary.json').read_text());B=json.loads((out/'uninterrupted/summary.json').read_text())
        checks.append({'name':'same_registered_rows','passed':A['rows']==B['rows']})
        checks.append({'name':'same_registered_aggregate','passed':A['aggregate']==B['aggregate']})
        with np.load(out/'resumed/arrays.npz',allow_pickle=False) as aa,np.load(out/'uninterrupted/arrays.npz',allow_pickle=False) as bb:
            different=[k for k in aa.files if k not in bb.files or not np.array_equal(aa[k],bb[k])]
            same=set(aa.files)==set(bb.files) and not different
            checks.append({'name':'bitwise_identical_arrays','passed':same,'array_count':len(aa.files),'different_arrays':different})
        # Existing completed results are immutable.
        with (out/'overwrite_attempt.log').open('w') as log:
            done=subprocess.run(command+['--output',str(out/'resumed'),'--resume'],cwd=ROOT.parent,stdout=log,stderr=subprocess.STDOUT,timeout=10,check=False)
        checks.append({'name':'completed_record_refuses_overwrite','passed':done.returncode!=0,'returncode':done.returncode})
    except Exception as exc:
        import traceback;traceback.print_exc();exception=repr(exc)
    result={'recorded_utc':datetime.datetime.now(datetime.timezone.utc).isoformat(),'elapsed_seconds':time.time()-start,
            'output':str(out),'checks':checks,'exception':exception,'all_passed':exception is None and all(c['passed'] for c in checks),
            'source_sha256':{'tests/test_validation_resume.py':hashlib.sha256(Path(__file__).read_bytes()).hexdigest()}}
    (out/'test_result.json').write_text(json.dumps(result,indent=2)+'\n')
    (ROOT/'results/validation_resume_tests.json').write_text(json.dumps(result,indent=2)+'\n')
    print(json.dumps(result),flush=True)
    raise SystemExit(0 if result['all_passed'] else 1)
if __name__=='__main__':main()
