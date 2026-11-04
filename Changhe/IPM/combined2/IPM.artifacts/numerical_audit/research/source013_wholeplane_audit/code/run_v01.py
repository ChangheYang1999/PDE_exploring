"""One finite local child for the independent whole-plane arithmetic audit."""
from pathlib import Path
from datetime import datetime,timezone
from hashlib import sha256
import os,subprocess,time,json,shutil
R=Path(__file__).resolve().parents[3];D=Path(__file__).resolve().parents[1];os.chdir(R)
assert os.sched_getaffinity(0)=={50} and os.getpriority(os.PRIO_PROCESS,0)>=19
assert all(os.environ.get(k)=='1' for k in ['OMP_NUM_THREADS','OPENBLAS_NUM_THREADS','MKL_NUM_THREADS'])
free=shutil.disk_usage(R).free;assert free>=20_000_000_000
start=datetime.now(timezone.utc);tick=time.monotonic()
log=D/'verification/run_v01.log';out=D/'verification/execution_v01.json'
assert not log.exists() and not out.exists()
argv=['research/source013_wholeplane_audit/code/check_v01.py'];status='COMPLETED';reason=None
with log.open('xb') as f:
 try:
  p=subprocess.run([os.sys.executable,'-B',*argv],stdout=f,stderr=subprocess.STDOUT,timeout=480);code=p.returncode
  if code:status='FAILED';reason='nonzero exit'
 except subprocess.TimeoutExpired:code=None;status='FAILED';reason='480 second timeout'
b=log.read_bytes();raw=sha256(b).hexdigest();red=b.replace(str(R).encode(),b'.')
if red!=b:log.write_bytes(red)
r=dict(status=status,reason=reason,exit_code=code,started_utc=start.isoformat(),finished_utc=datetime.now(timezone.utc).isoformat(),elapsed_seconds=time.monotonic()-tick,argv=argv,timeout_seconds=480,cpu=50,nice=19,threads=1,filesystem_free_before=free,log=str(log.relative_to(R)),log_sha256=sha256(red).hexdigest(),raw_log_sha256=raw,absolute_path_redaction=(red!=b),code_sha256=sha256((R/argv[0]).read_bytes()).hexdigest())
with out.open('x')as f:json.dump(r,f,indent=2);f.write('\n')
print(json.dumps(r))
