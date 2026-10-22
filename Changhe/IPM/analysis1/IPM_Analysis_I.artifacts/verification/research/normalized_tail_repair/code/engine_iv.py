"""Independent iv180 Laurent synthetic divisions for the exact tail repair.
No JS/TS, servers/listeners/tunnels, RLScience or Lean/Lake.
"""
import json,hashlib,math
from fractions import Fraction as F
from pathlib import Path
from mpmath import iv
import numpy as np
B=Path(__file__).resolve().parents[3]
def sha(p):return hashlib.sha256(p.read_bytes()).hexdigest()
def a(q):q=F(q);return iv.mpf(q.numerator)/q.denominator
def ep(t):
 sg,m,e,bc=t;assert bc>=0
 return F(-int(m) if sg else int(m))*F(2)**int(e)
def box(x):
 lo,hi=map(ep,x._mpi_);assert lo<=hi
 return {'lower_exact':str(lo),'upper_exact':str(hi),'display':str(x)}
def haszero(x):lo,hi=map(ep,x._mpi_);return lo<=0<=hi
def divide(poly,root):
 out=[iv.mpf(0)]*(len(poly)-1);out[-1]=poly[-1]
 for j in range(len(out)-2,-1,-1):out[j]=poly[j+1]+root*out[j+1]
 rem=poly[0]+root*out[0];assert haszero(rem)
 return out,rem

def evaluate():
 iv.dps=180
 p=B/'research/outer_leading_cancellation/evidence/leading_iv_audit.json';data=json.loads(p.read_text());assert data['status']=='PASS'
 archive=Path('numerics/data/trial_v2_h0.008.npz');assert sha(archive)=='a069d85d102e17340778042f85c003705716ba799c0f68873d10c1c582ea4874'
 with np.load(archive,allow_pickle=False) as z:k=F(float(z['k']));L=F(float(z['L']));t=F(float(z['knots'][-1]))
 assert 0<k<F(1,3);eps=[]
 for j,row in enumerate(data['residual_coefficients']):
  assert row['q']==j;lo,hi=map(F,(row['value']['lower_exact'],row['value']['upper_exact']));assert lo<=hi;eps.append(iv.mpf([a(lo).a,a(hi).b]))
 assert len(eps)==522
 M=520;poly=[iv.mpf(0) for _ in range(2*M+4)]
 for j,x in enumerate(eps):poly[M+2+j]+=x;poly[M+1-j]-=x
 remainders=[]
 for root in (-1,-1,1):poly,rem=divide(poly,root);remainders.append(box(rem))
 poly=[4*x for x in poly];assert len(poly)==2*M+1
 q=[poly[M]]+[2*poly[M+m] for m in range(1,M+1)]
 for m in range(1,M+1):assert haszero(poly[M-m]-poly[M+m])
 rawN=sum((abs(x) for x in q),iv.mpf(0))
 # Reconstruct the sin(3theta) coefficient from the quotient, not eps[1].
 rawI=(2*q[0]+q[1]-q[2]-q[3])/8;assert haszero(rawI-eps[1])
 beta=2*k-1;alpha=(3-k)/2;factor=(a(k)/a(1-k))/(iv.exp(a(t))**a(beta));N=rawN*factor;I=rawI*factor
 # Independent Beta(9,9) product, no factorial implementation.
 bb=F(1,9)
 for j in range(1,9):bb*=F(j,9+j)
 jb=F(3,2)*bb;Jupper=1/(1-beta);bmax=F(1,4)**8
 C=(N*(a(2)**a(alpha))+abs(I)*(a(4)*a(bmax)/a(jb))*a(Jupper)*(a(5)**a(alpha)))/(a(L)**a(3-k))
 public=json.loads((B/'research/normalized_tail_repair/source/public_bounds.json').read_text())
 Cpublic=(a(public['N_upper'])*a(2)**a(alpha)+a(public['I_abs_upper'])*(a(4)*a(bmax)/a(jb))*a(Jupper)*a(5)**a(alpha))/a(L)**a(3-k)
 vals={'C_from_public_N_I':Cpublic,'raw_N':rawN,'raw_I':rawI,'physical_factor':factor,'N':N,'I_H':I,'C':C,'B':a(bb),'J_b':a(jb),'J_chi_upper':a(Jupper)}
 out={'method':'iv180 three Laurent synthetic divisions, independently extracted NPZ scalars and Beta product','dps':180,'source':{'path':str(p.relative_to(B)),'sha256':sha(p)},'source_archive':{'path':str(archive),'sha256':sha(archive)},'scalars':{'k':str(k),'L':str(L),'tplus':str(t),'beta':str(beta),'alpha':str(alpha)},'values':{key:box(x) for key,x in vals.items()},'raw_quotient_sha256':hashlib.sha256(json.dumps([box(x) for x in q],sort_keys=True).encode()).hexdigest(),'witnesses':[{'m':m,'q_raw':box(q[m])} for m in (0,1,2,3,7,31,64,127,255,259,519,520)],'remainders':remainders,'counts':{'input_sines':522,'quotient_coefficients':521,'synthetic_division_coefficients':1043+1042+1041,'symmetry_diagnostics':520,'remainder_diagnostics':3,'strain_coefficient_diagnostics':1}}
 return out,q
