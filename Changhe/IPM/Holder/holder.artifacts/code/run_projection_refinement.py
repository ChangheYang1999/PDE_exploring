"""Checkpointed bounded chunks for a single-core projection-cusp refinement queue."""
from pathlib import Path
from datetime import datetime,timezone
import subprocess,json,sys
ROOT=Path(__file__).resolve().parents[1];PY='python3';BASE=ROOT/'11_lattice_pole_constraints/axis_projection_stieltjes/verification'
worker=int(sys.argv[1]);assert worker in [0,1]
sign=1 if worker==0 else -1;prefix='a50_n32768_m256_v2'
for start in range(0,32768,8192):
 stop=start+8192;name=f'{prefix}_s{sign}_r{start}_{stop}';out=BASE/(name+'.json');log=BASE/(name+'.log')
 if out.exists():print(datetime.now(timezone.utc).isoformat(),'SKIP',name,flush=True);continue
 cmd=[PY,str(ROOT/'code/certify_axis_projection_stieltjes_v2.py'),'--alpha','1/2','--b','3/4','--shift=-3/20','--K','1021/1000','--sign',str(sign),'--nx','32768','--ny','256','--start',str(start),'--stop',str(stop),'--out',str(out.relative_to(ROOT))]
 print(datetime.now(timezone.utc).isoformat(),'START',name,flush=True)
 with log.open('w') as f:
  r=subprocess.run(cmd,cwd=ROOT,stdout=f,stderr=subprocess.STDOUT,timeout=535)
 assert r.returncode==0,(name,r.returncode)
 print(datetime.now(timezone.utc).isoformat(),'DONE',name,flush=True)
print(datetime.now(timezone.utc).isoformat(),'COMPLETE',flush=True)
