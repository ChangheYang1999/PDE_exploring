"""One short serialized diagnostic, with unconditional frozen-middle restart."""
import os,signal,subprocess,time,json,hashlib
from pathlib import Path
from datetime import datetime,timezone
os.environ['PYTHONDONTWRITEBYTECODE']='1'
for key in ('OMP_NUM_THREADS','OPENBLAS_NUM_THREADS','MKL_NUM_THREADS','NUMEXPR_NUM_THREADS'):os.environ[key]='1'
B=Path(__file__).resolve().parents[3];E=B/'research/full_t_linkage/evidence';worker=1600700;source=B/'research/middle_second/code/run_full.py'
assert hashlib.sha256(source.read_bytes()).hexdigest()=='ba4297039dc6d2e4592df8155e5873b9baa9f4b81a3df9de0c9a88a54c1e3d32'
cmd=Path(f'/proc/{worker}/cmdline').read_bytes().replace(b'\0',b' ').decode();assert 'python3 research/middle_second/code/run_full.py --tag full_q16 --primary-tag full_q16' in cmd
start=datetime.now(timezone.utc).isoformat();os.kill(worker,signal.SIGTERM)
for _ in range(50):
 p=Path(f'/proc/{worker}/stat')
 if not p.exists() or p.read_text().split(') ')[1][0]=='Z':break
 time.sleep(.1)
else:raise RuntimeError('Middle did not stop; no second computation launched')
rc=None
try:
 with (E/'smoke_sequence.log').open('w') as f:
  for command in [['python3','research/full_t_linkage/code/check_coefficients.py','--tag','smoke','--spans','0'],['python3','research/full_t_linkage/code/audit_coefficients.py','--tag','smoke','--allow-partial'],['python3','research/full_t_linkage/code/replay_spans.py','--tag','smoke']]:
   run=subprocess.run(command,cwd=B,stdout=f,stderr=subprocess.STDOUT,timeout=95);rc=run.returncode
   if rc:break
finally:
 now=datetime.now(timezone.utc);log=B/'research/middle_second/evidence'/('resume_'+now.strftime('%Y%m%dT%H%M%SZ')+'.log')
 with log.open('a') as f:p=subprocess.Popen(['timeout','20h','python3','research/middle_second/code/run_full.py','--tag','full_q16','--primary-tag','full_q16'],cwd=B,stdout=f,stderr=subprocess.STDOUT,start_new_session=True)
 data={'start_utc':start,'end_utc':now.isoformat(),'smoke_rc':rc,'old_worker_pid':worker,'middle_timeout_pid':p.pid,'middle_log':str(log.relative_to(B)),'middle_source_sha256':hashlib.sha256(source.read_bytes()).hexdigest()};(E/'smoke_serial.json').write_text(json.dumps(data,indent=2)+'\n')
 with (B/'RUN_STATUS.md').open('a') as f:f.write('\n'+now.isoformat()+':99 short smoke ended rc'+str(rc)+'; frozen middle resumed timeoutPID'+str(p.pid)+' log'+str(log.relative_to(B))+'. DO NOT signal old worker1600700.\n')
 print(json.dumps(data),flush=True)
if rc:raise SystemExit(rc)
