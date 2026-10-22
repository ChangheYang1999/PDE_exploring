"""Original NPZ Laurent projection and iv180 radial powers. No JS/TS, servers, RLScience, Lean/Lake."""
import os
for key in ('OMP_NUM_THREADS','OPENBLAS_NUM_THREADS','MKL_NUM_THREADS','NUMEXPR_NUM_THREADS'):os.environ[key]='1'
import sys,json,hashlib,time
from pathlib import Path
from fractions import Fraction as Q
from datetime import datetime,timezone
import numpy as np
from mpmath import iv
assert not sys.flags.optimize
B=Path(__file__).resolve().parents[3];D=B/'research/single_tail_hminus1_obstruction';E=D/'evidence';P=B.parent/'ipmA-num/data/trial_v2_h0.008.npz'
def sha(p):return hashlib.sha256(p.read_bytes()).hexdigest()
def aa(q):q=Q(q);return iv.mpf(q.numerator)/q.denominator
def rf(t):
 s,m,e,bc=t;assert bc>=0
 return Q(-int(m) if s else int(m))*Q(2)**int(e)
def box(x):
 lo,hi=map(rf,x._mpi_);assert lo<=hi
 return {'lower_exact':str(lo),'upper_exact':str(hi),'display':str(x)}
def mul(a,b):
 out={}
 for i,x in a.items():
  for j,y in b.items():out[i+j]=out.get(i+j,Q(0))+x*y
 return {i:x for i,x in out.items() if x}
def main():
 start=time.monotonic();iv.dps=180;assert sha(P)=='a069d85d102e17340778042f85c003705716ba799c0f68873d10c1c582ea4874'
 with np.load(P,allow_pickle=False) as z:
  assert z['Aout'].shape==(260,10);col=[Q(*float(x).as_integer_ratio()) for x in z['Aout'][:,6]];k=Q(*float(z['k']).as_integer_ratio());t=Q(*float(z['knots'][-1]).as_integer_ratio());bo=Q(*float(z['bo']).as_integer_ratio())
 assert 0<k<Q(1,4) and bo>120
 # Laurent coefficients for 2i density angular factor, with w=exp(i theta).
 C={}
 for m,v in enumerate(col):
  for f in (2*m,-2*m):C[f]=C.get(f,Q(0))+v/2
 density=mul(mul(mul(C,{1:Q(1,2),-1:Q(1,2)}),{1:Q(1,2),-1:Q(1,2)}),{1:Q(1),-1:Q(-1)})
 sine=[density.get(2*j+1,Q(0)) for j in range(261)];assert all(density.get(-2*j-1,Q(0))==-sine[j] for j in range(261));assert all(f%2 and abs(f)<=521 for f in density)
 bd=sine[0];assert bd!=0;d=k-2;R=iv.exp(aa(t));scale=R**aa(3-d);Ld=aa(d/k-1)*scale*aa(bd)
 # Independent factored exponent comparisons, including the higher stream mode cutoff.
 pairs=[(0,0),(1,0),(2,0),(3,0),(4,0),(5,0),(0,1),(1,1),(2,1),(0,2)];exps=[(j+1)*k-j-2*l for j,l in pairs]+[3-bo];a3=4*k-3
 big=[]
 for j,y in enumerate(exps):
  for i,x in enumerate(exps):
   v=x+y-1;assert v!=d
   if v>a3:big.append([i,j,str(v)])
 assert sorted((i,j) for i,j,v in big)==[(0,0),(0,1),(1,0)]
 assert all((2*n+1)>x-1-a3 for x in exps for n in range(1,523))
 out={'utc':datetime.now(timezone.utc).isoformat(),'status':'COMPUTED_NONZERO_REQUIRES_AUDIT','method':'Original NPZ exact ratios, full Laurent projection and iv180 separately exponentiated radius power','dps':180,'seconds':time.monotonic()-start,'exact':{'k':str(k),'tplus':str(t),'bd':str(bd),'column6':list(map(str,col)),'sine_coefficients':list(map(str,sine)),'large_ordered_pairs':sorted(big)},'values':{'bd':box(aa(bd)),'Ld':box(Ld),'scale':box(scale)},'files':{str(q.relative_to(B)):sha(q) for q in (D/'PROOF.md',Path(__file__))},'source_archive':{'path':str(P),'sha256':sha(P)}}
 (E/'iv.json').write_text(json.dumps(out,indent=2)+'\n');print(json.dumps({'utc':out['utc'],'status':out['status'],'bd':str(bd),'Ld':out['values']['Ld']['display'],'seconds':out['seconds']}))
if __name__=='__main__':main()
