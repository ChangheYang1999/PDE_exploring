from pathlib import Path
from datetime import datetime,timezone
import os,subprocess,time,sys,json
os.sched_setaffinity(0,{17})
os.environ.update(OMP_NUM_THREADS='1',OPENBLAS_NUM_THREADS='1',MKL_NUM_THREADS='1')
def alive(pid):
 try:return Path(f'/proc/{pid}/stat').read_text().split()[2]!='Z'
 except FileNotFoundError:return False
while alive(3904509):time.sleep(10)
t=time.monotonic();p=subprocess.Popen([sys.executable,'-B','code/single_nine_exact_limit.py'],stdout=open('scratch/single_nine_exact_limit.log','w'),stderr=subprocess.STDOUT)
print(json.dumps(dict(at=datetime.now(timezone.utc).isoformat(),pid=p.pid)),flush=True)
rc=p.wait();print(json.dumps(dict(at=datetime.now(timezone.utc).isoformat(),exit_code=rc,actual_elapsed_s=time.monotonic()-t)),flush=True)
