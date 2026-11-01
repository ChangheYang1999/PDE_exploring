"""Run additional finite audits sequentially after the current core18 queue."""
from pathlib import Path
from datetime import datetime,timezone
import json,os,shutil,subprocess,sys,time
sys.dont_write_bytecode=True
PY=sys.executable
receipt=Path('artifacts/storage/shift2_review_queue.json')
state=dict(waiting_for_pid=3802829,jobs=[])
def now():return datetime.now(timezone.utc).isoformat(timespec='seconds')
def save():receipt.write_text(json.dumps(state,indent=2)+'\n')
def active(pid):
    p=Path(f'/proc/{pid}/cmdline')
    return p.exists() and b'shift2_final_queue.py' in p.read_bytes()
def run(args,log):
    if shutil.disk_usage('.').free<20000000000:
        state['stopped_low_shared_disk']=now();save();raise SystemExit(1)
    start=time.monotonic();entry=dict(arguments=args,started_at_utc=now(),log=log);state['jobs'].append(entry);save()
    with open(log,'w') as out:
        child=subprocess.Popen([PY,'-u']+args,stdin=subprocess.DEVNULL,stdout=out,stderr=subprocess.STDOUT,env={**os.environ,'OMP_NUM_THREADS':'1','OPENBLAS_NUM_THREADS':'1','MKL_NUM_THREADS':'1'})
        entry['pid']=child.pid;save();entry['exit_status']=child.wait()
    entry['ended_at_utc']=now();entry['actual_elapsed_s']=time.monotonic()-start;save()
state['started_at_utc']=now();save()
while active(3802829):time.sleep(10)
run(['code/period_five_prefix_radii.py','--roots','6'],'research/182_period_five_prefix_radii/verification/producer.log')
run(['code/remaining_candidate_prefixes.py','--roots','5'],'research/181_remaining_candidate_prefixes/verification/root5_producer.log')
run(['code/four_ninths_numerical_audit.py','--roots','1,2,3,4'],'research/183_four_ninths_numerical_audit/verification/producer.log')
for index in [6,7]:
    p=Path(f'research/163_other_candidate_shaped_roots/verification/root{index}_checks.json')
    if p.exists() and json.loads(p.read_text()).get('all_index_lower_bound_proved'):
        run(['code/remaining_candidate_prefixes.py','--roots',str(index)],f'research/181_remaining_candidate_prefixes/verification/root{index}_producer.log')
    else:state.setdefault('pending_candidate_roots',[]).append(index);save()
run(['code/prefix_box_replay.py','--topics','176,178,179,181,182'],'research/174_adaptive_majorant_boxes/verification/prefix_box_replay.log')
state['ended_at_utc']=now();save()
