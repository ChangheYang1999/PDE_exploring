"""One-core sequence after the existing010 weak worker exits."""
from pathlib import Path
from datetime import datetime,timezone
from hashlib import sha256
import json,os,shutil,subprocess,time
ROOT=Path(__file__).resolve().parents[3]
BASE=ROOT/'research/scaled_dyadic_probes'
PID=3919081
EXPECTED=str(ROOT/'research/scaled_weak_backend/code/weak_v3.py')
PYTHON='python3'
ENV=os.environ.copy()
ENV.update(OMP_NUM_THREADS='1',OPENBLAS_NUM_THREADS='1',MKL_NUM_THREADS='1',PYTHONDONTWRITEBYTECODE='1',TMPDIR=str(ROOT/'tmp'))

def now():return datetime.now(timezone.utc).isoformat()
def emit(event,**kwargs):print(json.dumps({'utc':now(),'event':event,**kwargs}),flush=True)
def busy_original():
 p=Path(f'/proc/{PID}')
 if not p.exists():return False
 try:
  stat=(p/'stat').read_text();state=stat[stat.rfind(')')+2:].split()[0]
  command=(p/'cmdline').read_bytes().split(b'\0')
 except FileNotFoundError:return False
 if state=='Z':return False
 assert EXPECTED.encode() in command,(PID,command)
 return True

def budget():
 total=sum(os.lstat(Path(dp)/n).st_size for dp,dirs,names in os.walk(ROOT,followlinks=False) for n in names)
 free=shutil.disk_usage('.').free
 assert total<2_985_000_000 and free>=20_000_000_000,(total,free)
 return total,free

emit('waiting_for_existing_worker',pid=PID)
while busy_original():time.sleep(30)
weak=ROOT/'research/scaled_weak_backend/verification/C1-N1-010-d2w-j7-x3bal-legqs_n1.json'
assert weak.exists(),'010 worker ended without its second mode record'
emit('previous_worker_complete',result_sha256=sha256(weak.read_bytes()).hexdigest())
commands=[('far_pairing_audit',[PYTHON,'-B',str(ROOT/'research/far_pairing_audit/code/check.py')]),('scaled_modes13',[PYTHON,'-B',str(BASE/'code/check.py'),'C1-N1-007-d2w-j7-e2bal','C1-N1-010-d2w-j7-x3bal-legqs']),('remaining007_derivatives',[PYTHON,'-B',str(ROOT/'research/remaining_derivative_norms/code/check.py'),'--seconds','7200'])]
for label,command in commands:
 lane_bytes,free=budget();emit('start',label=label,command=command,lane_bytes=lane_bytes,build_free_bytes=free)
 begin=time.monotonic()
 with (BASE/'logs'/f'{label}_01.log').open('x') as out:
  result=subprocess.run(command,cwd=ROOT,env=ENV,stdout=out,stderr=subprocess.STDOUT)
 emit('finish',label=label,returncode=result.returncode,elapsed_seconds=time.monotonic()-begin)
 assert result.returncode==0,(label,result.returncode)
emit('all_complete')
