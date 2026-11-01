from pathlib import Path
from datetime import datetime,timezone
import os,subprocess,time,json,sys
os.sched_setaffinity(0,{18})
os.environ.update(OMP_NUM_THREADS='1',OPENBLAS_NUM_THREADS='1',MKL_NUM_THREADS='1')
for name,args in [('boundary_sensitivity350_audit',['--through','350']),('sample350_amplification',[])]:
 start=time.monotonic()
 with Path(f'scratch/{name}_350.log').open('a') as f:
  p=subprocess.Popen([sys.executable,'-B',f'code/{name}.py']+args,stdout=f,stderr=subprocess.STDOUT)
  print(json.dumps(dict(started=datetime.now(timezone.utc).isoformat(timespec='seconds'),name=name,pid=p.pid)),flush=True)
  rc=p.wait()
 print(json.dumps(dict(finished=datetime.now(timezone.utc).isoformat(timespec='seconds'),name=name,returncode=rc,actual_elapsed_s=time.monotonic()-start)),flush=True)
 if rc:raise SystemExit(rc)
