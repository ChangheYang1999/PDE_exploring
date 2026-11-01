"""Sequential local audit queue; every result still requires explicit review."""
from pathlib import Path
from datetime import datetime,timezone
import json,os,shutil,subprocess,sys,time
sys.dont_write_bytecode=True
receipt=Path('artifacts/storage/shift3_review_queue.json')
def now():return datetime.now(timezone.utc).isoformat(timespec='seconds')
state=dict(started_at_utc=now(),jobs=[])
def save():receipt.write_text(json.dumps(state,indent=2)+'\n')
def run(args,log):
 assert shutil.disk_usage('.').free>20000000000
 row=dict(arguments=args,started_at_utc=now(),log=log);state['jobs'].append(row);save();start=time.monotonic()
 with open(log,'w') as out:
  p=subprocess.Popen([sys.executable,'-u']+args,stdin=subprocess.DEVNULL,stdout=out,stderr=subprocess.STDOUT,env={**os.environ,'OMP_NUM_THREADS':'1','OPENBLAS_NUM_THREADS':'1','MKL_NUM_THREADS':'1'})
  row['pid']=p.pid;save();row['exit_status']=p.wait()
 row['ended_at_utc']=now();row['actual_elapsed_s']=time.monotonic()-start;save();return row['exit_status']==0
save()
run(['code/delta_archive_checkpoint.py','research/102_edge_recurrence_reference/verification/float_edge1_20261031T075706Z/input_checkpoint.pkl.gz','research/102_edge_recurrence_reference/verification/float_edge1_20261031T0749Z/input_checkpoint.pkl.gz','--remove-original'],'artifacts/storage/float_edge1_delta.log')
for Q,index,tag,audit,prefix,at,pt in [(5,4,'tunedQ5','period_five_numerical_audit.py','period_five_prefix_radii.py','180_period_five_numerical_audit','182_period_five_prefix_radii'),(6,1,'tuned13','period_six_numerical_audit.py','period_six_prefix_radii.py','185_period_six_numerical_audit','186_period_six_prefix_radii'),(6,2,'tuned13','period_six_numerical_audit.py','period_six_prefix_radii.py','185_period_six_numerical_audit','186_period_six_prefix_radii'),(5,3,'tunedQ5','period_five_numerical_audit.py','period_five_prefix_radii.py','180_period_five_numerical_audit','182_period_five_prefix_radii')]:
 hp=Path(f'../a4-num/ckpt/{tag}_r{index}_p1024_H.json')
 if not hp.exists() or max(map(int,json.loads(hp.read_text())['obstruction']))<300:
  state.setdefault('not_ready',[]).append(dict(period=Q,root=index));save();continue
 if sum(p.stat().st_size for p in Path('.').rglob('*') if p.is_file())>2988000000:
  state['storage_stop']=now();save();break
 if run(['code/'+audit,'--roots',str(index)],f'research/{at}/verification/root{index}_producer.log'):
  d=json.loads(Path(f'research/{at}/verification/root{index}_checks.json').read_text())
  if d['all_checks_pass']:run(['code/'+prefix,'--roots',str(index)],f'research/{pt}/verification/root{index}_producer.log')
state['ended_at_utc']=now();save()
