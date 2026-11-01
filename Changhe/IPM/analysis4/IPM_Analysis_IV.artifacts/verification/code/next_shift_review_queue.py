"""Continue prepared audits after the existing tail-evaluation queue finishes."""
from pathlib import Path
from datetime import datetime,timezone
import json,os,shutil,subprocess,sys,time
sys.dont_write_bytecode=True
receipt=Path('artifacts/storage/next_shift_review_queue.json')
def now():return datetime.now(timezone.utc).isoformat(timespec='seconds')
state=dict(started_at_utc=now(),waiting_for_pid=3985544,jobs=[])
def save():receipt.write_text(json.dumps(state,indent=2)+'\n')
def run(args,log):
    assert shutil.disk_usage('.').free>20000000000
    assert sum(p.stat().st_size for p in Path('.').rglob('*') if p.is_file())<2991000000
    entry=dict(arguments=args,started_at_utc=now(),log=log);state['jobs'].append(entry);save();start=time.monotonic()
    with open(log,'w') as out:
        child=subprocess.Popen([sys.executable,'-u']+args,stdin=subprocess.DEVNULL,stdout=out,stderr=subprocess.STDOUT,env={**os.environ,'OMP_NUM_THREADS':'1','OPENBLAS_NUM_THREADS':'1','MKL_NUM_THREADS':'1'})
        entry['pid']=child.pid;save();entry['exit_status']=child.wait()
    entry['ended_at_utc']=now();entry['actual_elapsed_s']=time.monotonic()-start;save()
    return entry['exit_status']==0
save()
while True:
    p=Path('/proc/3985544/cmdline')
    if not p.exists() or b'run_tail_after_queue.py' not in p.read_bytes():break
    time.sleep(10)
for period,index,audit,prefix,topic_a,topic_p,tag in [(6,6,'period_six_numerical_audit.py','period_six_prefix_radii.py','185_period_six_numerical_audit','186_period_six_prefix_radii','tuned13'),(5,5,'period_five_numerical_audit.py','period_five_prefix_radii.py','180_period_five_numerical_audit','182_period_five_prefix_radii','tunedQ5')]:
    hp=Path(f'../a4-num/ckpt/{tag}_r{index}_p1024_H.json')
    if not hp.exists() or max(map(int,json.loads(hp.read_text())['obstruction']))<300:
        state.setdefault('not_ready',[]).append(dict(period=period,root=index));save();continue
    if run(['code/'+audit,'--roots',str(index)],f'research/{topic_a}/verification/root{index}_producer.log'):
        checked=Path(f'research/{topic_a}/verification/root{index}_checks.json')
        if checked.exists() and json.loads(checked.read_text()).get('all_checks_pass'):
            run(['code/'+prefix,'--roots',str(index)],f'research/{topic_p}/verification/root{index}_producer.log')
state['ended_at_utc']=now();save()
