"""Wait for the existing core18 queue, then evaluate the prepared exact tail bounds."""
from pathlib import Path
from datetime import datetime,timezone
import json,os,subprocess,sys,time
sys.dont_write_bytecode=True
receipt=Path('artifacts/storage/tail_after_queue.json')
def now():return datetime.now(timezone.utc).isoformat(timespec='seconds')
state=dict(started_at_utc=now(),waiting_for_pid=3890226)
def save():receipt.write_text(json.dumps(state,indent=2)+'\n')
save()
while True:
    p=Path('/proc/3890226/cmdline')
    if not p.exists() or b'shift2_review_queue.py' not in p.read_bytes():break
    time.sleep(10)
start=time.monotonic();state['child_started_at_utc']=now();save()
with open('research/184_explicit_prefix_tail_bounds/verification/producer.log','w') as out:
    child=subprocess.Popen([sys.executable,'-u','code/explicit_prefix_tail_bounds.py'],stdin=subprocess.DEVNULL,stdout=out,stderr=subprocess.STDOUT,env={**os.environ,'OMP_NUM_THREADS':'1','OPENBLAS_NUM_THREADS':'1','MKL_NUM_THREADS':'1'})
    state['child_pid']=child.pid;save();state['exit_status']=child.wait()
state['ended_at_utc']=now();state['actual_child_elapsed_s']=time.monotonic()-start;save()
