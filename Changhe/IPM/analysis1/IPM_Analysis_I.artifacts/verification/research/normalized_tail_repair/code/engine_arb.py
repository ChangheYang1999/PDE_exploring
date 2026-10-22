"""Arb512 exact collected inverse sine recurrence for the exact tail repair norm.
No JS/TS, servers/listeners/tunnels, RLScience or Lean/Lake.
"""
import json,hashlib,math
from fractions import Fraction as F
from pathlib import Path
from flint import arb,ctx
B=Path(__file__).resolve().parents[3]
def sha(p):return hashlib.sha256(p.read_bytes()).hexdigest()
def a(q):q=F(q);return arb(q.numerator)/q.denominator
def dy(x):m,e=x.man_exp();return F(int(m))*F(2)**int(e)
def box(x):
 assert x.is_finite();lo,hi=dy(x.lower()),dy(x.upper());assert lo<=hi
 return {'lower_exact':str(lo),'upper_exact':str(hi),'display':x.str(40)}
def evaluate():
 ctx.prec=512;ctx.threads=1
 p=B/'research/outer_leading_cancellation/evidence/leading_result.json';v=json.loads(p.read_text());k=F(v['scalars_exact']['k']);L=F(v['scalars_exact']['L']);t=F(v['scalars_exact']['tb']);assert 0<k<F(1,3)
 eps=[]
 for j,row in enumerate(v['residual_coefficients']):
  assert row['q']==j;z=row['value'];lo,hi=F(z['lower_exact']),F(z['upper_exact']);assert lo<=hi;eps.append(a(lo).union(a(hi)))
 assert len(eps)==522
 M=520
 # Exact collected integer coefficients avoid exponential interval wrapping.
 def c(d):return (-1 if d%2 else 1)*(d//2+1)
 q=[4*sum((c(j-1)*eps[j] for j in range(1,M+2)),arb(0))]
 for m in range(1,M+1):q.append(8*sum((c(j-m-1)*eps[j] for j in range(m+1,M+2)),arb(0)))
 compatibility=eps[0]-(2*q[0]-q[2])/8;assert compatibility.contains(0)
 rawN=sum((abs(qm) for qm in q[:M+1]),arb(0));rawI=eps[1]
 beta=2*k-1;alpha=(3-k)/2;factor=a(k/(1-k))*a(-beta*t).exp();N=factor*rawN;I=factor*rawI
 bb=F(math.factorial(8)**2,math.factorial(17));jb=3*bb/2;bstar=F(1,2**16);Jupper=1/(1-beta)
 C=(a(k-3)*a(L).log()).exp()*(a(2)**a(alpha)*N+a(4*bstar*Jupper/jb)*abs(I)*a(5)**a(alpha))
 public=json.loads((B/'research/normalized_tail_repair/source/public_bounds.json').read_text())
 Cpublic=(a(k-3)*a(L).log()).exp()*(a(2)**a(alpha)*a(public['N_upper'])+a(4*bstar*Jupper/jb)*a(public['I_abs_upper'])*a(5)**a(alpha))
 vals={'C_from_public_N_I':Cpublic,'raw_N':rawN,'raw_I':rawI,'physical_factor':factor,'N':N,'I_H':I,'C':C,'B':a(bb),'J_b':a(jb),'J_chi_upper':a(Jupper),'compatibility':compatibility}
 out={'method':'Arb512 exact collected integer inverse sine forms and coefficient L1 bound','bits':512,'source':{'path':str(p.relative_to(B)),'sha256':sha(p)},'scalars':{'k':str(k),'L':str(L),'tplus':str(t),'beta':str(beta),'alpha':str(alpha)},'values':{key:box(x) for key,x in vals.items()},'raw_quotient_sha256':hashlib.sha256(json.dumps([box(x) for x in q[:M+1]],sort_keys=True).encode()).hexdigest(),'witnesses':[{'m':m,'q_raw':box(q[m])} for m in (0,1,2,3,7,31,64,127,255,259,519,520)],'counts':{'input_sines':522,'quotient_coefficients':521,'collected_integer_terms':135981,'compatibility_diagnostics':1}}
 return out,q[:M+1]
