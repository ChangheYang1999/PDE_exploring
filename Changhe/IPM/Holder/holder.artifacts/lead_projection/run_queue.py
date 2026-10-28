"""Sequential bounded chunks of the projection-cusp lower sums (lead copy of the verifier's runner)."""
from pathlib import Path
from datetime import datetime,timezone
import subprocess,sys
HERE=Path(__file__).resolve().parent;PY=sys.executable
alpha,b,shift,K,nx,ny,chunk,prefix=sys.argv[1:9];nx=int(nx);chunk=int(chunk);extra=sys.argv[9:]  # extra: e.g. --vleft=-6 --vright=3
BASE=HERE/'verification';BASE.mkdir(exist_ok=True)
for sign in [1,-1]:
 for start in range(0,nx,chunk):
  stop=min(nx,start+chunk);name=f'{prefix}_s{sign}_r{start}_{stop}';out=BASE/(name+'.json');log=BASE/(name+'.log')
  if out.exists():print(datetime.now(timezone.utc).isoformat(),'SKIP',name,flush=True);continue
  cmd=[PY,str(HERE/'cert_v2_copy.py'),'--alpha',alpha,'--b',b,f'--shift={shift}','--K',K,'--sign',str(sign),'--nx',str(nx),'--ny',ny,'--start',str(start),'--stop',str(stop),'--out',str(out)]+extra
  print(datetime.now(timezone.utc).isoformat(),'START',name,flush=True)
  with log.open('w') as f:
   r=subprocess.run(cmd,cwd=HERE,stdout=f,stderr=subprocess.STDOUT,timeout=3000)
  assert r.returncode==0,(name,r.returncode)
  print(datetime.now(timezone.utc).isoformat(),'DONE',name,flush=True)
print(datetime.now(timezone.utc).isoformat(),'COMPLETE',flush=True)
