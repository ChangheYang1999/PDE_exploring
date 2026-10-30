"""Wait for the existing lane job, then run one bounded derivative stage."""
from pathlib import Path
from datetime import datetime,timezone
import os,time,subprocess,json,hashlib
ROOT=Path(__file__).resolve().parents[3]
BASE=ROOT/'research/remaining_derivative_norms'
pid=3008786
print(datetime.now(timezone.utc).isoformat(),'waiting for',pid,flush=True)
while True:
 try:
  command=Path(f'/proc/{pid}/cmdline').read_bytes()
  state=Path(f'/proc/{pid}/stat').read_text().split()[2]
  if b'successor_dyadic_probes/code/check.py' not in command or state=='Z':break
 except FileNotFoundError:break
 time.sleep(5)
free=os.statvfs('.');assert free.f_bavail*free.f_frsize>=20_000_000_000
print(datetime.now(timezone.utc).isoformat(),'starting one derivative stage',flush=True)
cmd=['python3','-B',str(BASE/'code/check.py'),'--seconds','430']
start=time.monotonic();child=subprocess.Popen(cmd,env={**os.environ,'OMP_NUM_THREADS':'1','OPENBLAS_NUM_THREADS':'1','TMPDIR':str(ROOT/'tmp')})
ret=child.wait()
row={'utc':datetime.now(timezone.utc).isoformat(),'child_pid':child.pid,'returncode':ret,'elapsed_seconds':time.monotonic()-start,'code_sha256':hashlib.sha256((BASE/'code/check.py').read_bytes()).hexdigest()}
with (BASE/'verification/stage01_exit.json').open('x') as f:json.dump(row,f,indent=2);f.write('\n')
print(row,flush=True)
