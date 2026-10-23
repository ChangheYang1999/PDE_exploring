"""High-precision independent canonical checks at the projection-defect peaks of167."""
import os
for k in ['OMP_NUM_THREADS','OPENBLAS_NUM_THREADS','MKL_NUM_THREADS','NUMEXPR_NUM_THREADS']:os.environ[k]='1'
from pathlib import Path
from datetime import datetime,timezone
from fractions import Fraction as F
import json,hashlib,time
import numpy as np
import torch
import mpmath as mp
from q_checkpoint_reader import QCheckpoint
from q_mp_primitives import MPQPrimitives,guard_digits,mf

def utc():return datetime.now(timezone.utc).isoformat()
def sha(p):return hashlib.sha256(Path(p).read_bytes()).hexdigest()
def strings(x,d):
 if isinstance(x,dict):return {k:strings(v,d)for k,v in x.items()}
 if isinstance(x,list):return [strings(v,d)for v in x]
 return mp.nstr(x,d) if x is not None else None

torch.set_num_threads(1);torch.serialization.add_safe_globals([np._core.multiarray.scalar,np.dtype,type(np.dtype('float64')),type(np.dtype('float32'))])
root=Path('research/dynamic_projection_audit/verification');audit=json.loads((root/'AUDIT.json').read_text());assert audit['status']=='COMPUTED'
out={'started_utc':utc(),'status':'RUNNING','input_sha256':sha(root/'AUDIT.json'),'code_sha256':sha(__file__),'cases':[]}
def save():out['updated_utc']=utc();(root/'MP_PEAKS.json').write_text(json.dumps(out,indent=2)+'\n')
for case in audit['cases']:
 if case['tau']==0:continue
 source=Path(case['frozen']);assert sha(source)==case['sha256'];q=QCheckpoint(source)
 row={'N':q.N,'M':q.M,'source':str(source),'source_sha256':sha(source),'points':[]};out['cases'].append(row)
 pr=case['rows'][-1]['projections'][0]
 for kind in ['nodes','between']:
  z=pr[kind]['annulus'];row['points'].append({'kind':kind,'point':z['defect_point'],'double_canonical_G':z['canonical_at_peak'],'double_projected_G':z['projected_at_peak'],'values':[]})
 for digits in [55,85]:
  with mp.workdps(digits+guard_digits(q.N,q.M,q.kappa)):
   m=MPQPrimitives(q.coeff,F(q.L),F(q.kappa),F(q.cl));cw=mf(case['cw']);cx=mf(case['cx'])
   for pt in row['points']:
    x,y=pt['point'];v=m.at(x,y);gx,gy=v['gradient'];ux,uy=v['U'];G=cw*v['rho']-(cx*mf(x)+ux)*gx-(cx*mf(y)+uy)*gy
    v.update(G=G,Gp_minus_G=mf(pt['double_projected_G'])-G,quadrature_G_minus_MP=mf(pt['double_canonical_G'])-G)
    pt['values'].append({'digits':digits,'work_digits':mp.mp.dps,'fields':strings(v,digits)})
   save();print(json.dumps({'utc':utc(),'N':q.N,'digits':digits}),flush=True)
 with mp.workdps(100):
  for pt in row['points']:
   a,b=[v['fields']for v in pt['values']]
   pt['precision_abs_G_difference']=str(abs(mp.mpf(a['G'])-mp.mpf(b['G'])))
 row['status']='COMPUTED';save()
out['status']='COMPUTED';out['finished_utc']=utc();save()
