"""iv180 independent positive geometric sums and NPZ source; no JS/TS, servers, RLScience, Lean/Lake."""
import os
for key in ('OMP_NUM_THREADS','OPENBLAS_NUM_THREADS','MKL_NUM_THREADS'):os.environ[key]='1'
import json,hashlib,sys,time
from pathlib import Path
from fractions import Fraction as Q
from datetime import datetime,timezone
import numpy as np
from mpmath import iv
assert not sys.flags.optimize
B=Path(__file__).resolve().parents[3];D=B/'research/tail_local_velocity';E=D/'evidence'
def sha(p):return hashlib.sha256(p.read_bytes()).hexdigest()
def aa(q):q=Q(q);return iv.mpf(q.numerator)/q.denominator
def dy(t):s,m,e,bc=t;return Q((-1)**s*int(m))*Q(2)**int(e)
def box(v):
 lo,hi=map(dy,v._mpi_);assert lo<=hi
 return {'lower_exact':str(lo),'upper_exact':str(hi),'display':str(v)}
def fall(n,j):
 r=1
 for i in range(j):r*=n-i
 return r
def main():
 start=time.monotonic();iv.dps=180
 p=B.parent/'ipmA-num/data/trial_v2_h0.008.npz';assert sha(p)=='a069d85d102e17340778042f85c003705716ba799c0f68873d10c1c582ea4874'
 with np.load(p,allow_pickle=False) as z:
  k=Q(*float(z['k']).as_integer_ratio());t=Q(*float(z['knots'][-1]).as_integer_ratio())
 beta=2*k-1;N=Q(1918980991,50000000);assert N==Q('38.37961982')
 K=128;ratio=(1+Q(2,2*K+1))**3/4;assert ratio<Q(1,2)
 sums=[];tail=[];S=[]
 for j in range(4):
  lo=sum((Q(fall(2*m+3,j),4**m) for m in range(K)),Q(0));err=2*Q(fall(2*K+3,j),4**K)
  # Every future term ratio <= 1/2, proved with the common j<=3 ratio.
  sums.append(lo);tail.append(err);S.append(iv.mpf([aa(lo).a,aa(lo+err).b]))
 C=[aa(4*N)*s/(3-aa(beta)) for s in S]
 # Different evaluation path: integer inverse cube times positive 3000^(2k-1).
 power=iv.power(aa(3000),aa(2*k-1))/aa(3000**3)
 values={**{'C'+str(j):v for j,v in enumerate(C)},'u9':C[0]*9**3*power,'w9':C[1]*9**2*power,'power3000':power,'R_b':iv.exp(aa(t))}
 out={'utc':datetime.now(timezone.utc).isoformat(),'status':'COMPUTED_REQUIRES_AUDIT','method':'iv180; original NPZ dyadics,128-term positive sums with exact geometric tail; separately factored power','seconds':time.monotonic()-start,'exact':{'k':str(k),'tplus':str(t),'N':str(N),'beta':str(beta),'partial_S':list(map(str,sums)),'tails':list(map(str,tail)),'tail_ratio_ceiling':str(ratio),'K':K},'values':{s:box(v) for s,v in values.items()},'source_archive':{'path':str(p),'sha256':sha(p)},'files':{str(x.relative_to(B)):sha(x) for x in (D/'PROOF.md',Path(__file__))}}
 (E/'iv.json').write_text(json.dumps(out,indent=2)+'\n');print(json.dumps({k:out[k] for k in ('utc','status','seconds')}));print(json.dumps({k:v['display'] for k,v in out['values'].items()}))
if __name__=='__main__':main()
