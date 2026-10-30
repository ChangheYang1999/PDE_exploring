"""Serial priority checks while the sole scaled worker is explicitly stopped."""
from pathlib import Path
from datetime import datetime,timezone
import os,signal,time,subprocess,json
ROOT=Path(__file__).resolve().parents[3];BASE=ROOT/'research/successor_monomial_probes'
pid=3919081;start=time.monotonic();rows=[];paused=False
now=lambda:datetime.now(timezone.utc).isoformat()
env=dict(os.environ,OMP_NUM_THREADS='1',OPENBLAS_NUM_THREADS='1',MKL_NUM_THREADS='1',PYTHONDONTWRITEBYTECODE='1',TMPDIR=str(ROOT/'tmp'))
jobs=[['research/affine_taylor_lift_audit/code/check.py'],
      ['research/successor_monomial_probes/code/check.py','C1-N1-007-d2w-j7-e2bal'],
      ['research/successor_monomial_probes/code/check.py','C1-N1-013-pairU-from007'],
      ['research/candidate_audits/code/points.py','C1-N1-013-pairU-from007','1/10','73/100'],
      ['research/candidate_audits/code/uniform_point.py','C1-N1-013-pairU-from007'],
      ['research/candidate_audits/code/point_extensions.py','C1-N1-013-pairU-from007']]
try:
    proc=Path(f'/proc/{pid}')
    if proc.exists():
        assert b'weak_v3.py' in (proc/'cmdline').read_bytes()
        os.kill(pid,signal.SIGSTOP);paused=True
        for i in range(100):
            state=(proc/'status').read_text().split('State:\t')[1].splitlines()[0]
            if state.startswith('T'):break
            time.sleep(.01)
        assert state.startswith('T')
    print('START',now(),'paused',pid,paused,flush=True)
    for i,job in enumerate(jobs):
        tick=time.monotonic();stamp=now();log=BASE/f'logs/serial01_{i+1:02d}.log'
        args=['taskset','-c','57','nice','-n','19','python3','-B',*job]
        with log.open('x') as f:r=subprocess.run(args,cwd=ROOT,env=env,stdin=subprocess.DEVNULL,stdout=f,stderr=subprocess.STDOUT,timeout=540)
        row={'start_utc':stamp,'finish_utc':now(),'argv':args,'returncode':r.returncode,'elapsed_seconds':time.monotonic()-tick,'log':str(log.relative_to(ROOT))};rows.append(row)
        print(json.dumps(row),flush=True)
        if r.returncode:break
finally:
    resumed=False
    if paused:
        try:os.kill(pid,signal.SIGCONT);resumed=True
        except ProcessLookupError:pass
    out={'utc':now(),'scaled_worker_pid':pid,'was_paused':paused,'resumed':resumed,'elapsed_seconds':time.monotonic()-start,'jobs':rows}
    with (BASE/'verification/queue01_finished.json').open('x') as f:json.dump(out,f,indent=2);f.write('\n')
    print('FINISHED',now(),'resumed',resumed,'seconds',out['elapsed_seconds'],flush=True)
