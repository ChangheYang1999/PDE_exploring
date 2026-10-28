"""Single-threaded checkpoint queue; every mathematical child has a 535-second limit."""
from pathlib import Path
from datetime import datetime,timezone
import os,subprocess,json,time
ROOT=Path(__file__).resolve().parents[1]
PY='python3'
ENV=dict(os.environ,PYTHONDONTWRITEBYTECODE='1',OPENBLAS_NUM_THREADS='1',OMP_NUM_THREADS='1')
STATUS=ROOT/'data/shift2_half_queue_status.json';results=[]
def run(args,log,output=None):
 if output and (ROOT/output).exists():
  print(datetime.now(timezone.utc).isoformat(),'SKIP',output,flush=True);return True
 print(datetime.now(timezone.utc).isoformat(),'START',args,flush=True)
 start=time.monotonic();ok=False
 try:
  with (ROOT/log).open('w') as f:
   p=subprocess.run([PY]+args,cwd=ROOT,stdout=f,stderr=subprocess.STDOUT,timeout=535,env=ENV)
  ok=p.returncode==0;error=None if ok else 'returncode '+str(p.returncode)
 except subprocess.TimeoutExpired:error='535-second child timeout'
 row=dict(time_utc=datetime.now(timezone.utc).isoformat(),args=args,log=log,ok=ok,error=error,elapsed_seconds=time.monotonic()-start)
 results.append(row);STATUS.write_text(json.dumps(results,indent=2)+'\n')
 print(row['time_utc'],'DONE' if ok else 'FAILED',args,error,flush=True);return ok
base='11_lattice_pole_constraints/axis_projection_stieltjes/verification'
for alpha,K,tag,ny,left in [('1/2','1021/1000','a50_n32768_m512_v2_focus',512,'-18')]:
 okay=True
 for sign in [1,-1]:
  for start in range(0,32768,8192):
   stop=start+8192;name=f'{base}/{tag}_s{sign}_r{start}_{stop}'
   args=['code/certify_axis_projection_stieltjes_v2.py','--alpha',alpha,'--b','3/4','--shift=-3/20','--K',K,'--sign',str(sign),'--nx','32768','--ny',str(ny),'--left',left,'--vleft','-8','--vright','8','--start',str(start),'--stop',str(stop),'--out',name+'.json']
   okay=run(args,name+'.log',name+'.json') and okay
 if okay:run(['code/combine_projection_lower.py',tag],f'{base}/{tag}_combination.log')
print(datetime.now(timezone.utc).isoformat(),'QUEUE COMPLETE',flush=True)
