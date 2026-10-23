"""Independent MP checks at all13 recorded annulus maximizing coordinates."""
import os
for k in ['OMP_NUM_THREADS','OPENBLAS_NUM_THREADS','MKL_NUM_THREADS','NUMEXPR_NUM_THREADS']:os.environ[k]='1'
from pathlib import Path
from datetime import datetime,timezone
import json,hashlib,traceback
import numpy as np
import mpmath as mp
import torch
from q_local_checkpoint import QLocalCheckpoint
from scalar_mp_hydrostatic_density import ScalarMPDensity
torch.set_num_threads(1)
R=Path('research/hydrostatic_224_function_difference');V=R/'verification';utc=lambda:datetime.now(timezone.utc).isoformat();sha=lambda p:hashlib.sha256(Path(p).read_bytes()).hexdigest();checks=[];bindings={};rows=[];metrics=[];start=utc()
def ck(n,b,e=None):
 checks.append(dict(name=n,passed=bool(b),evidence=e))
 if not b:raise AssertionError((n,e))
def bind(p,h=None):
 v=sha(p)
 if h:ck('hash '+str(p),v==h)
 bindings[str(p)]=v
 return Path(p)
def save(status,error=None):
 out=dict(status=status,started_utc=start,finished_utc=utc(),count=len(checks),checks=checks,bindings=bindings,rows=rows,metric_records=metrics,traceback=error,scope='MP recomputation at recorded finite maximizing coordinates; no proof of unchanged argmax, continuum norm or inverse.');tmp=V/'MAXIMIZER_MP.json.tmp';tmp.write_text(json.dumps(out,indent=2,allow_nan=False)+'\n');tmp.replace(V/'MAXIMIZER_MP.json')
try:
 for p in [__file__,R/'RESULT_REVIEW_RESOLUTION_PROOF.md',V/'RUN.json','independent_code/q_local_checkpoint.py','independent_code/q_checkpoint_reader.py','independent_code/scalar_mp_hydrostatic_density.py']:bind(p)
 run=json.loads((V/'RUN.json').read_text());ck('231 original complete',run['status']=='PASS' and len(run['checks'])==231 and all(c['passed']for c in run['checks']))
 for p,h in run['bindings'].items():bind(p,h)
 coords=sorted({(z['x'],z['y'])for pair in ['baseline','comparisons']for label in run[pair]for z in run[pair][label]['annulus'].values()if isinstance(z,dict) and 'x'in z});ck('13 unique coordinates',len(coords)==13);values={}
 for state in run['states']:
  n=state['N'];bind(state['source'],state['sha256']);
  with torch.serialization.safe_globals([np.ndarray,np._core.multiarray._reconstruct]):q=QLocalCheckpoint(state['source'])
  values[n]={}
  for idx,(x,y)in enumerate(coords):
   vv=[]
   for digits in [72,108]:
    with mp.workdps(digits):
     m=ScalarMPDensity(q.coeff,q.L,q.kappa,q.basis,q.tk);jet=m.jet(x,y);vv.append([mp.nstr(t,digits)for t in jet[:3]])
   with mp.workdps(108):
    a,b=[list(map(mp.mpf,v))for v in vv];rr=mp.sqrt(mp.mpf(x)**2+mp.mpf(y)**2);weights=[mp.sqrt(1+rr),1/mp.sqrt(1+rr),1/mp.sqrt(1+rr)];change=max(abs(u-v)/w for u,v,w in zip(a,b,weights));ck(str(n)+' MP precision '+str(idx),change<mp.mpf('1e-55'),mp.nstr(change,30));values[n][(x,y)]=b
   rows.append(dict(N=n,index=idx,x=x,y=y,precisions=[72,108],jets=vv,weighted_precision_change=mp.nstr(change,35)));save('RUNNING')
  print('DONE',n,utc(),flush=True)
 corrected={}
 with mp.workdps(108):
  for pair,(nold,nnew)in [('baseline',(160,192)),('comparisons',(192,224))]:
   corrected[pair]={}
   for label in run[pair]:
    corrected[pair][label]={}
    for key in ['field','gradient','pointwise_relative']:
     z=run[pair][label]['annulus'][key];coord=(z['x'],z['y']);a,b=values[nold][coord],values[nnew][coord];r=float(np.geomspace(1e-3,1e7,401)[z['index']//49])if label=='common_nominal'else float(np.hypot(*coord));rr=mp.mpf(r)
     if key=='field':value=abs(a[0]-b[0])/mp.sqrt(1+rr)
     elif key=='gradient':value=mp.sqrt((a[1]-b[1])**2+(a[2]-b[2])**2)*mp.sqrt(1+rr)
     else:
      ck(pair+label+' nonzero finer density',b[0]!=0);value=abs(a[0]-b[0])/abs(b[0])
     error=abs(value-mp.mpf(float(z['value'])));ck(pair+label+key+' numerical consistency',error<mp.mpf('2e-9'),mp.nstr(error,35));corrected[pair][label][key]=value;metrics.append(dict(pair=pair,convention=label,metric=key,coordinate=list(coord),index=z['index'],weight_radius=r,stored_value=z['value'],MP_value=mp.nstr(value,95),change=mp.nstr(error,35)))
  for label in run['comparisons']:
   for key in ['field','gradient','pointwise_relative']:
    before=corrected['baseline'][label][key];after=corrected['comparisons'][label][key];ck(label+key+' finite increase survives MP',after>before,dict(previous=mp.nstr(before,35),current=mp.nstr(after,35),ratio=mp.nstr(after/before,35)))
 ck('39 states/point evaluations and18metrics',len(rows)==39 and len(metrics)==18);save('PASS');print('PASS',len(checks),utc(),flush=True)
except Exception:
 save('FAIL',traceback.format_exc());raise
