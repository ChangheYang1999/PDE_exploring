from pathlib import Path
from fractions import Fraction
import subprocess,sys,json,os
ROOT=Path(__file__).resolve().parents[1];BASE=ROOT/'09_uniform_comparison/pass3';PY='python3';worker=int(sys.argv[1])
texts=sorted({json.loads(p.read_text())['alpha'] for p in (BASE/'data/local').glob('*.json')},key=Fraction)
env=dict(os.environ,PYTHONDONTWRITEBYTECODE='1',OPENBLAS_NUM_THREADS='1',OMP_NUM_THREADS='1')
for start in [worker*128,worker*128+64]:
 args=[PY,'code/certify_local_circles_multi.py','--alphas',*texts,'--start',str(start),'--stop',str(start+64),'--out-stem',f'09_uniform_comparison/pass3/verification/local/replay_{start}_{start+64}']
 print('RUN',args,flush=True);subprocess.run(args,cwd=ROOT,env=env,timeout=535,check=True)
for start in range(worker*32,512,64):
 args=[PY,'code/replay_uniform3_middle.py','--start',str(start),'--stop',str(start+32)]
 print('RUN',args,flush=True);subprocess.run(args,cwd=ROOT,env=env,timeout=535,check=True)
print('COMPLETE',worker,flush=True)
