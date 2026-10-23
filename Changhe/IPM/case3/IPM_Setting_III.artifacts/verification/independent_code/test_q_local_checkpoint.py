"""Independent mathematical gate for new-basis checkpoint reconstruction."""
import os
for k in ['OMP_NUM_THREADS','OPENBLAS_NUM_THREADS','MKL_NUM_THREADS','NUMEXPR_NUM_THREADS']:os.environ[k]='1'
from pathlib import Path
from datetime import datetime,timezone
from fractions import Fraction as F
import json,hashlib,time
import numpy as np
import mpmath as mp
from q_local_checkpoint import QLocalCheckpoint,exact_affine_chebyshev
from q_high_precision_density import MPQDensity
from q_checkpoint_reader import QCheckpoint
from q_mp_primitives import mf

root=Path('research/dynamic_local_reconstruction/verification');root.mkdir(parents=True,exist_ok=True)
result={'started_utc':datetime.now(timezone.utc).isoformat(),'status':'RUNNING','exact_cases':0,'states':[],'code_sha256':hashlib.sha256(Path('independent_code/q_local_checkpoint.py').read_bytes()).hexdigest()}
def save():
 result['updated_utc']=datetime.now(timezone.utc).isoformat();(root/'READER_GATE.json').write_text(json.dumps(result,indent=2)+'\n')
def val(c,x):
 a=F(0);b=F(0)
 for v in c[:0:-1]:a,b=v+2*x*a-b,a
 return c[0]+x*a-b
for n in range(1,13):
 c=[F((-1)**j*(j+1),j+3) for j in range(n)]
 for alpha,beta in [(F(1),F(0)),(F(8,7),F(-1,7)),(F(7,3),F(-4,3))]:
  cc=exact_affine_chebyshev(c,alpha,beta)
  for t in [F(-1),F(-2,3),F(0),F(5,7),F(1)]:
   assert val(cc,t)==val(c,alpha*t+beta);result['exact_cases']+=1
save()
paths=[Path('numerics/runs')/f'drY_C3.0_N{N}_tau0020.000.pt' for N in [64,96,128]]
legacy=Path('research/dynamic_rescaling_implementation/verification/dr_first_tau20/drA_C3.0_N64_tau0020.040.pt')
# Use any already frozen old-basis state if the spelling differs.
if not legacy.exists():
 old=list(Path('research/dynamic_rescaling_implementation/verification/dr_first_tau20').glob('*N64*pt'));legacy=old[0] if old else None
if legacy:
 a=QLocalCheckpoint(legacy);a.save_snapshot(root/'legacy_numeric.npz');b=QCheckpoint(root/'legacy_numeric.npz');x=np.array([.1,.4,1.,9.]);y=np.array([.3,.2,-1.,8.])
 assert np.array_equal(a.rho(x,y),b.rho(x,y));result['legacy_bitwise_density']='PASS'
for path in paths:
 if not path.exists():continue
 q=QLocalCheckpoint(path);row={'source':str(path),'sha256':q.meta['sha256'],'N':q.N,'M':q.M,'saved_nodes':q.node_reconstruction_details(),'checks':[]};result['states'].append(row);save()
 start=time.monotonic();coeff=q.exact_coefficients();row['exact_conversion_seconds']=time.monotonic()-start
 with mp.workdps(200):
  tk_mp=[float(-mp.cos(2*mp.pi*k/(2*q.N+1))) for k in range(q.N+1)]
  row['binary_grid_vs_correctly_rounded_mp_max']=max(abs(a-b)for a,b in zip(q.tk,tk_mp))
  row['binary_grid_different_entries']=int(sum(a!=b for a,b in zip(q.tk,tk_mp)))
  maxerr=mp.mpf(0);relerr=mp.mpf(0)
  for k in range(q.M):
   tk=mf(q.tk[k]);alpha=2/(1-tk);beta=-(1+tk)/(1-tk)
   for t in [mp.mpf(-1),mp.mpf('-.73'),mp.mpf('-.1'),mp.mpf('.62'),mp.mpf(1)]:
    a=MPQDensity.clenshaw(list(map(mf,q.coeff[k])),alpha*t+beta)[0]
    b=MPQDensity.clenshaw(list(map(mf,coeff[k])),t)[0]
    maxerr=max(maxerr,abs(a-b));relerr=max(relerr,abs(a-b)/(1+abs(a)))
  row['exact_conversion_mp_relative_difference']=mp.nstr(relerr,12);row['exact_conversion_mp_absolute_difference']=mp.nstr(maxerr,12)
  save();assert relerr<mp.mpf('1e-120')
 for x,y in [(0.,.7),(.23,.81),(3.,5.),(30.,40.)]:
  rho=float(q.rho(x,y));ex=float(q.rho(-x,y));oy=float(q.rho(x,-y))
  assert rho==ex and rho==-oy
 row['parities']='PASS';row['status']='PASS';save();print(json.dumps({'N':q.N,'seconds':row['exact_conversion_seconds'],'node_error':row['saved_nodes']}),flush=True)
result['status']='PASS';result['finished_utc']=datetime.now(timezone.utc).isoformat();save()
