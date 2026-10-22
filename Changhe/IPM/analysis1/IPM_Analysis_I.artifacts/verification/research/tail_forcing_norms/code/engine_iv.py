"""Original NPZ, beta moments and interval Simpson with proved remainder. No JS/TS, servers, RLScience, Lean/Lake."""
import os
for key in ('OMP_NUM_THREADS','OPENBLAS_NUM_THREADS','MKL_NUM_THREADS','NUMEXPR_NUM_THREADS'):os.environ[key]='1'
import json,hashlib,sys,time,math
from fractions import Fraction as Q
from pathlib import Path
from datetime import datetime,timezone
import numpy as np
from mpmath import iv
assert not sys.flags.optimize
B=Path(__file__).resolve().parents[3];D=B/'research/tail_forcing_norms';E=D/'evidence';P=B.parent/'ipmA-num/data/trial_v2_h0.008.npz'
def sha(p):return hashlib.sha256(p.read_bytes()).hexdigest()
def aa(q):q=Q(q);return iv.mpf(q.numerator)/q.denominator
def rf(t):
 sg,m,e,bc=t;assert bc>=0
 return Q(-int(m) if sg else int(m))*Q(2)**int(e)
def box(x):
 lo,hi=map(rf,x._mpi_);assert lo<=hi
 return {'lower_exact':str(lo),'upper_exact':str(hi),'display':str(x)}
def beta(m,n):return Q(math.factorial(m-1)*math.factorial(n-1),math.factorial(m+n-1))
def main():
 start=time.monotonic();iv.dps=180;assert sha(P)=='a069d85d102e17340778042f85c003705716ba799c0f68873d10c1c582ea4874'
 with np.load(P,allow_pickle=False) as raw:k=Q(*float(raw['k']).as_integer_ratio())
 assert 0<k<Q(1,4);p=2*k;a,ell=Q(1,4),Q(1,4);b=a+ell
 A=ell**9*(a*beta(5,5)+ell*beta(6,5))
 Bg=4*ell**7*(a*(beta(3,3)-4*beta(4,3)+4*beta(5,3))+ell*(beta(4,3)-4*beta(5,3)+4*beta(6,3)))
 # I_n=int_0^1 u^n/(1+u)du, I_0=log2 and I_n=1/n-I_(n-1).
 moments=[iv.ln(2)];rational=[Q(0)];logs=[Q(1)]
 for n in range(1,9):moments.append(aa(Q(1,n))-moments[-1]);rational.append(Q(1,n)-rational[-1]);logs.append(-logs[-1])
 Bang=aa(ell**8)*sum(((-1)**j*math.comb(4,j)*moments[4+j] for j in range(5)),iv.mpf(0));Bval=aa(Bg)+Bang
 Br=Bg+ell**8*sum(((-1)**j*math.comb(4,j)*rational[4+j] for j in range(5)),Q(0));Bl=ell**8*sum(((-1)**j*math.comb(4,j)*logs[4+j] for j in range(5)),Q(0))
 N=1024;h=ell/N;sumval=iv.mpf(0)
 for i in range(N+1):
  s=a+i*h;g=(s-a)**2*(b-s)**2;weight=1 if i in (0,N) else (4 if i%2 else 2)
  sumval+=weight*aa(g)*aa(s)**aa(p)
 simpson=aa(h/3)*sumval
 # Bound g^(m) by differentiating the two squared factors separately.
 G=[]
 for m in range(5):
  z=Q(0)
  for i in range(3):
   j=m-i
   if 0<=j<=2:z+=math.comb(m,i)*Q(math.factorial(2),math.factorial(2-i))*Q(math.factorial(2),math.factorial(2-j))*ell**(4-m)
  G.append(z)
 M=iv.mpf(0);fall=Q(1)
 for j in range(5):
  if j:fall*=p-(j-1)
  endpoint=b if p-j>=0 else a
  M+=math.comb(4,j)*aa(G[4-j]*abs(fall))*aa(endpoint)**aa(p-j)
 err=aa(ell*h**4/Q(180))*M;upper=rf(err._mpi_[1]);J=simpson+iv.mpf([-aa(upper).b,aa(upper).b])
 old=B/'research/far_residual_obstruction/evidence/iv.json';r=json.loads(old.read_text())['values']['E0'];lo,hi=Q(r['lower_exact']),Q(r['upper_exact']);assert lo<=hi<0;E0=iv.mpf([aa(lo).a,aa(hi).b]);CL=iv.sqrt(iv.pi)*(-E0)*J/iv.sqrt(aa(A));CD=iv.sqrt(iv.pi)*(-E0)*J/iv.sqrt(Bval)
 values={'A':aa(A),'B':Bval,'J':J,'C_L':CL,'C_D':CD,'E0':E0};assert all((values[x]>0) is True for x in ('A','B','J','C_L','C_D'))
 out={'utc':datetime.now(timezone.utc).isoformat(),'status':'COMPUTED_REQUIRES_OUTPUT_AUDIT','method':'iv180 independent beta moments, rational log recurrence and composite Simpson N1024 with full fourth derivative remainder','dps':180,'seconds':time.monotonic()-start,'exact':{'k':str(k),'A':str(A),'B_rational':str(Br),'B_log2':str(Bl),'G_derivative_bounds':list(map(str,G)),'N':N,'h':str(h)},'simpson':{'sum':box(simpson),'fourth_derivative_upper':box(M),'error_bound':box(err),'added_error_upper_exact':str(upper)},'values':{key:box(v) for key,v in values.items()},'files':{str(t.relative_to(B)):sha(t) for t in (old,Path(__file__),D/'PROOF.md')},'source_archive':{'path':str(P),'sha256':sha(P)}}
 (E/'iv.json').write_text(json.dumps(out,indent=2)+'\n');print(json.dumps({k:out[k] for k in ('utc','status','seconds')}));print(json.dumps({k:v['display'] for k,v in out['values'].items()}))
if __name__=='__main__':main()
