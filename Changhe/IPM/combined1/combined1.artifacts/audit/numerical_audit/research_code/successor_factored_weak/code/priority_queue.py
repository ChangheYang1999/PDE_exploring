"""Temporarily pause the serial queue for the newly published014 audit."""
from pathlib import Path
from datetime import datetime,timezone
from hashlib import sha256
import json,os,signal,shutil,subprocess,time
ROOT=Path(__file__).resolve().parents[3];BASE=ROOT/'research/successor_factored_weak'
PYTHON='python3';NAME='C1-N1-014-pairB-from007'
QUEUE=286853;EXPECTED=str(ROOT/'research/scaled_dyadic_probes/code/serial_queue_v4.py').encode()
ENV=os.environ.copy();ENV.update(OMP_NUM_THREADS='1',OPENBLAS_NUM_THREADS='1',MKL_NUM_THREADS='1',PYTHONDONTWRITEBYTECODE='1',TMPDIR=str(ROOT/'tmp'))
now=lambda:datetime.now(timezone.utc).isoformat()
def emit(event,**kw):print(json.dumps({'utc':now(),'event':event,**kw}),flush=True)
def state(pid):
 text=Path(f'/proc/{pid}/stat').read_text();return text[text.rfind(')')+2:].split()[0]
def budget():
 size=sum(os.lstat(Path(d)/n).st_size for d,ds,ns in os.walk(ROOT,followlinks=False) for n in ns)
 free=shutil.disk_usage('.').free;assert size<2_985_000_000 and free>=20_000_000_000
 return {'lane_bytes':size,'build_free_bytes':free}
assert EXPECTED in Path(f'/proc/{QUEUE}/cmdline').read_bytes().split(b'\0')
paused=[];record={'started_utc':now(),'queue_pid':QUEUE,'commands':[]};begin=time.monotonic()
try:
 os.kill(QUEUE,signal.SIGSTOP);paused.append(QUEUE)
 while state(QUEUE)!='T':time.sleep(.01)
 children=[int(p) for p in Path(f'/proc/{QUEUE}/task/{QUEUE}/children').read_text().split()]
 assert len(children)<=1
 for pid in children:
  cmd=Path(f'/proc/{pid}/cmdline').read_bytes().split(b'\0')
  assert str(ROOT).encode() in b' '.join(cmd)
  if state(pid)!='Z':
   os.kill(pid,signal.SIGSTOP);paused.append(pid)
   while state(pid)!='T':time.sleep(.01)
 record['paused_pids']=paused[:];record['paused_utc']=now();emit('paused_existing_queue',pids=paused)
 commands=[('014_structure',[PYTHON,'-B',str(ROOT/'research/candidate_audits/code/audit.py'),NAME]),
 ('014_point',[PYTHON,'-B',str(ROOT/'research/candidate_audits/code/points.py'),NAME,'1/10','73/100']),
 ('014_uniform',[PYTHON,'-B',str(ROOT/'research/candidate_audits/code/uniform_point.py'),NAME]),
 ('014_extensions',[PYTHON,'-B',str(ROOT/'research/candidate_audits/code/point_extensions.py'),NAME]),
 ('014_factored',[PYTHON,'-B',str(BASE/'code/check.py')]),
 ('007_largeK',[PYTHON,'-B',str(ROOT/'research/large_index_weak/code/check.py')])]
 for label,command in commands:
  if label=='014_structure':assert not (ROOT/f'research/candidate_audits/verification/{NAME}.json').exists()
  emit('start',label=label,command=command,**budget());tick=time.monotonic()
  with (BASE/'logs'/f'{label}_01.log').open('x') as out:
   proc=subprocess.run(command,cwd=ROOT,env=ENV,stdout=out,stderr=subprocess.STDOUT,timeout=590)
  item={'label':label,'returncode':proc.returncode,'elapsed_seconds':time.monotonic()-tick,'completed_utc':now()}
  record['commands'].append(item);emit('finish',**item)
  assert proc.returncode==0,item
 record['all_complete']=True
finally:
 for pid in reversed(paused):
  try:os.kill(pid,signal.SIGCONT)
  except ProcessLookupError:pass
 record['resumed_utc']=now();record['pause_elapsed_seconds']=time.monotonic()-begin
 record['controller_sha256']=sha256(Path(__file__).read_bytes()).hexdigest()
 dest=BASE/'verification/priority_pause.json'
 with dest.open('x') as out:json.dump(record,out,indent=2);out.write('\n')
 emit('resumed_existing_queue',pids=paused,elapsed_seconds=record['pause_elapsed_seconds'])
