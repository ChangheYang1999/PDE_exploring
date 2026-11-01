"""Run the completed sin11 audit and full Q9 identity after the prefix queue."""
from pathlib import Path
from datetime import datetime,timezone
import json,os,subprocess,sys,time,fcntl
sys.dont_write_bytecode=True
STOP=datetime.fromisoformat('2026-11-01T00:45:00+00:00')
def stamp():return datetime.now(timezone.utc).isoformat(timespec='seconds')
def live(pid):
 try:return Path(f'/proc/{pid}/stat').read_text().split()[2]!='Z'
 except FileNotFoundError:return False
while live(3638904):time.sleep(15)
tasks=[('single_harmonic_finite_audit.py',['--M','11']),('single_harmonic_finite_fits.py',['--M','11']),('full_polar_response_comparison.py',['--Q','9'])]
for script,args in tasks:
 if datetime.now(timezone.utc)>=STOP:raise SystemExit(0)
 log=Path('scratch')/(script.removesuffix('.py')+'_Q9_sin11.log')
 with Path('scratch/core17.lock').open('a') as lock,log.open('a') as f:
  fcntl.flock(lock,fcntl.LOCK_EX);start=time.monotonic();p=subprocess.Popen(['taskset','-c','17','nice','-n','19',sys.executable,'-B','code/'+script]+args,stdout=f,stderr=subprocess.STDOUT)
  print(json.dumps(dict(at=stamp(),stage='start',script=script,pid=p.pid)),flush=True);rc=p.wait()
 print(json.dumps(dict(at=stamp(),stage='end',script=script,exit_code=rc,elapsed_s=time.monotonic()-start)),flush=True)
 if rc:raise SystemExit(rc)
peer=Path('../a4-num/notes/eval_single_sin11_49.json')
while not peer.exists():
 if datetime.now(timezone.utc)>=STOP:raise SystemExit(0)
 time.sleep(20)
with Path('scratch/core17.lock').open('a') as lock,Path('scratch/single_harmonic_residuals_sin11.log').open('a') as f:
 fcntl.flock(lock,fcntl.LOCK_EX);start=time.monotonic();p=subprocess.Popen(['taskset','-c','17','nice','-n','19',sys.executable,'-B','code/single_harmonic_residuals.py','--M','11'],stdout=f,stderr=subprocess.STDOUT)
 print(json.dumps(dict(at=stamp(),stage='start',script='single_harmonic_residuals.py',pid=p.pid)),flush=True);rc=p.wait()
print(json.dumps(dict(at=stamp(),stage='end',script='single_harmonic_residuals.py',exit_code=rc,elapsed_s=time.monotonic()-start)),flush=True)
raise SystemExit(rc)
