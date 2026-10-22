"""Serialize one short artifact smoke before resuming the priority middle run."""
import os,signal,subprocess,time,json,hashlib
from pathlib import Path
from datetime import datetime,timezone
B=Path(__file__).resolve().parents[3];E=B/'research/full_green_linkage/evidence'
worker=1494774;source=B/'research/middle_second/code/run_full.py'
assert hashlib.sha256(source.read_bytes()).hexdigest()=='ba4297039dc6d2e4592df8155e5873b9baa9f4b81a3df9de0c9a88a54c1e3d32'
cmd=Path(f'/proc/{worker}/cmdline').read_bytes().replace(b'\0',b' ').decode()
assert 'python3 research/middle_second/code/run_full.py --tag full_q16 --primary-tag full_q16' in cmd
start=datetime.now(timezone.utc).isoformat();os.kill(worker,signal.SIGTERM)
for _ in range(50):
 p=Path(f'/proc/{worker}/stat')
 if not p.exists() or p.read_text().split(') ')[1][0]=='Z':break
 time.sleep(.1)
else:raise RuntimeError('Middle did not terminate; no second computation launched')
rc=None
try:
 with (E/'smoke_v2_sequence.log').open('w') as f:
  commands=[['python3','research/full_green_linkage/code/check_boundaries.py','--tag','smoke_v2','--spans','0'],['python3','research/full_green_linkage/code/audit_boundaries.py','--tag','smoke_v2','--allow-partial'],['python3','research/full_green_linkage/code/replay_spans.py','--tag','smoke_v2','--allow-partial']]
  for command in commands:
   run=subprocess.run(command,cwd=B,stdout=f,stderr=subprocess.STDOUT,timeout=95);rc=run.returncode
   if rc:break
finally:
 now=datetime.now(timezone.utc);log=B/'research/middle_second/evidence'/('resume_'+now.strftime('%Y%m%dT%H%M%SZ')+'.log')
 with log.open('a') as f:
  p=subprocess.Popen(['timeout','20h','python3','research/middle_second/code/run_full.py','--tag','full_q16','--primary-tag','full_q16'],cwd=B,stdout=f,stderr=subprocess.STDOUT,start_new_session=True)
 data={'start_utc':start,'end_utc':now.isoformat(),'smoke_rc':rc,'old_worker_pid':worker,'middle_timeout_pid':p.pid,'middle_log':str(log.relative_to(B)),'middle_source_sha256':hashlib.sha256(source.read_bytes()).hexdigest()}
 (E/'smoke_v2_serial.json').write_text(json.dumps(data,indent=2)+'\n')
 with (B/'RUN_STATUS.md').open('a') as f:f.write('\n'+now.isoformat()+':98shortsmoke ended rc'+str(rc)+'; frozenmiddle resumed timeoutPID'+str(p.pid)+' log'+str(log.relative_to(B))+'. DO NOT signal old worker1494774.\n')
 print(json.dumps(data),flush=True)
if rc:raise SystemExit(rc)
