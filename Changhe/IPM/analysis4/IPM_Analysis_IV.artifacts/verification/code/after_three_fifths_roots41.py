"""Wait for this lane's core18 audit, then run two finite diagnostics."""
from pathlib import Path
from datetime import datetime,timezone
import json,os,subprocess,sys,time,shutil
sys.dont_write_bytecode=True
ROOT=Path('artifacts/storage')
pid=1142859
receipt=ROOT/'after_three_fifths_roots41.json'
def stamp():return datetime.now(timezone.utc).isoformat(timespec='seconds')
state=dict(started_at_utc=stamp(),wait_for_pid=pid,jobs=[])
def save():receipt.write_text(json.dumps(state,indent=2)+'\n')
save()
while True:
    try:
        stat=Path(f'/proc/{pid}/stat').read_text().split()
        command=Path(f'/proc/{pid}/cmdline').read_bytes()
    except FileNotFoundError:break
    if stat[2]=='Z' or b'three_fifths_high_order_audit.py' not in command:break
    time.sleep(15)
for code,log in [('shifted_drift_fit_audit.py','shifted_drift_fit_audit.log'),('one_step_edge_audit.py','one_step_edge_audit.log')]:
    assert shutil.disk_usage('.').free>20_000_000_000
    row=dict(code='code/'+code,log='scratch/'+log,started_at_utc=stamp());state['jobs'].append(row);save();start=time.monotonic()
    with open(row['log'],'w') as out:
        p=subprocess.Popen([sys.executable,'-u','code/'+code],stdin=subprocess.DEVNULL,stdout=out,stderr=subprocess.STDOUT,env={**os.environ,'OMP_NUM_THREADS':'1','OPENBLAS_NUM_THREADS':'1','MKL_NUM_THREADS':'1'})
        row['pid']=p.pid;save();row['exit_status']=p.wait()
    row.update(ended_at_utc=stamp(),actual_elapsed_s=time.monotonic()-start);save()
state['completed_at_utc']=stamp();save()
