"""Exact signed-frequency verification of saved same-runtime F boxes."""
import os
for k in ('OMP_NUM_THREADS','OPENBLAS_NUM_THREADS','MKL_NUM_THREADS'):os.environ[k]='1'
from pathlib import Path
from fractions import Fraction as Q
from collections import defaultdict
from datetime import datetime,timezone
import hashlib,json,sys
import numpy as np
assert not sys.flags.optimize
B=Path(__file__).resolve().parents[3];D=B/'research/radial_tm_instance';E=D/'evidence'
def sha(p):return hashlib.sha256(p.read_bytes()).hexdigest()
H=[defaultdict(Q) for j in range(262)]
for m in range(260):
 for nu in (1+2*m,1-2*m,3+2*m,3-2*m):
  j=(abs(nu)-1)//2
  H[j][m]+=Q(1 if nu>0 else -1,8)
assert H[0][0]==Q(1,4) and H[0][2]==Q(-1,8) and all(v==0 for m,v in H[0].items() if m not in (0,2))
checks=0;files={};margins=[]
for ci in (0,4102,7808):
 p=E/('selected_v3_cell_%04d.npz'%ci);files[str(p.relative_to(B))]=sha(p)
 d=np.load(p);tm,tr=d['T_mid'],d['T_rad'];fm,fr=d['F_mid'],d['F_rad']
 assert tm.shape==tr.shape==(8,260) and fm.shape==fr.shape==(261,8)
 assert all(np.isfinite(x).all() for x in (tm,tr,fm,fr)) and (tr>=0).all() and (fr>=0).all()
 for n in range(1,262):
  for k in range(8):
   weights=defaultdict(Q)
   for j,fac in ((n-1,Q(4-2*n,2)),(n,Q(4+2*n,2))):
    for m,c in H[j].items():
     weights[k,m]+=fac*c
     if k<7:weights[k+1,m]+=Q(k+1,2)*c
   mm=sum((w*Q(float(tm[j,m])) for (j,m),w in weights.items()),Q())
   rr=sum((abs(w)*Q(float(tr[j,m])) for (j,m),w in weights.items()),Q())
   outm,outr=Q(float(fm[n-1,k])),Q(float(fr[n-1,k]))
   margin=outr-abs(mm-outm)-rr
   assert margin>=0,(ci,n,k,margin)
   margins.append(margin);checks+=1
for p in (Path(__file__),D/'LINKAGE.md',E/'linkage_proof_first.json'):files[str(p.relative_to(B))]=sha(p)
assert sha(D/'LINKAGE.md')==json.loads((E/'linkage_proof_first.json').read_text())['proof_sha256']
r={'utc':datetime.now(timezone.utc).isoformat(),'status':'PASS_EXACT_SAVED_T_TO_F_IMAGES','checks':checks,'cells':[0,4102,7808],'modes':261,'orders':8,'minimal_margin':str(min(margins)),'zero_margins':sum(x==0 for x in margins),'files':files,'scope':'Finite saved T-box image only; no canonical spline input membership.'}
(E/'linkage_checks.json').write_text(json.dumps(r,indent=2)+'\n');print(json.dumps({k:v for k,v in r.items() if k!='files'}))
