"""Original dyadics, Laurent rows, coordinate-scaled radial/tangential iv180.
No JS/TS, servers/listeners/tunnels, RLScience, or Lean/Lake.
"""
import os
for key in ('OMP_NUM_THREADS','OPENBLAS_NUM_THREADS','MKL_NUM_THREADS','NUMEXPR_NUM_THREADS'):os.environ[key]='1'
import json,hashlib,time,sys
from pathlib import Path
from fractions import Fraction as F
from datetime import datetime,timezone
import numpy as np
from mpmath import iv
assert not sys.flags.optimize
B=Path(__file__).resolve().parents[3];D=B/'research/single_tail_second_row';E=D/'evidence';P=B.parent/'ipmA-num/data/trial_v2_h0.008.npz'
def sha(p):return hashlib.sha256(p.read_bytes()).hexdigest()
def a(q):q=F(q);return iv.mpf(q.numerator)/q.denominator
def ep(t):sg,m,e,bc=t;assert bc>=0;return F(-int(m) if sg else int(m))*F(2)**int(e)
def box(x):
 lo,hi=map(ep,x._mpi_);assert lo<=hi
 return {'lower_exact':str(lo),'upper_exact':str(hi),'display':str(x)}
def interval(q):return iv.mpf([a(q['lower_exact']).a,a(q['upper_exact']).b])
def mul(x,y):
 z={}
 for i,q in x.items():
  for j,r in y.items():z[i+j]=z.get(i+j,F(0))+q*r
 return {i:q for i,q in z.items() if q}
def run():
 st=time.monotonic();iv.dps=180
 assert sha(P)=='a069d85d102e17340778042f85c003705716ba799c0f68873d10c1c582ea4874'
 with np.load(P,allow_pickle=False) as r:k=F(float(r['k']));t=F(float(r['knots'][-1]));coef=r['Aout'].copy()
 assert coef.shape==(260,10) and 0<k<F(1,4);beta=2*k-1;a2=3*k-2
 base=mul(mul({1:F(1,2),-1:F(1,2)},{1:F(1,2),-1:F(1,2)}),{1:F(1),-1:F(-1)})
 rows=[]
 for col in (0,1,2):
  cos={}
  for m in range(260):
   for freq in (2*m,-2*m):cos[freq]=cos.get(freq,F(0))+F(float(coef[m,col]))/2
  sine=mul(base,cos);d=[]
  for j in range(262):
   freq=2*j+1;q=sine.get(freq,F(0));assert sine.get(-freq,F(0))==-q;d.append(q)
  assert d[-1]==0;rows.append(d)
 norm=B/'research/modal_repair/evidence/independent_gauss_iv.json';nr=json.loads(norm.read_text());b=nr['values']['A00_correction'];z=iv.mpf([a(b['lower_exact_dyadic']).a,a(b['upper_exact_dyadic']).b])
 raw=B/'research/outer_leading_cancellation/evidence/leading_iv_audit.json';lead=json.loads(raw.read_text());assert lead['status']=='PASS'
 eps=[]
 for j,r in enumerate(lead['residual_coefficients']):assert r['q']==j;eps.append(interval(r['value']))
 assert len(eps)==522
 radius=iv.exp(a(t));d0=[a(x)+z*a(base.get(2*j+1,0)) for j,x in enumerate(rows[0])]
 # Common e^(3-a)t removed before the product. Unlike the primary's physical sums.
 h=[a(x)+(a(k)/a(1-k))*eps[j]/radius**3 for j,x in enumerate(rows[1])]
 def product(expa,expb,A,C):
  total=iv.mpf(0);terms=[]
  for n in range(1,262):
   m=2*n;aa=expa+1;assert m-aa>0 and m+aa>0
   fn=(a(aa-m)*A[n-1]+a(aa+m)*A[n])/2
   plus=fn/a(m-aa);minus=fn/a(m+aa);vr=-(plus+minus)/2;vt=(plus-minus)/2
   radial=a(expb)*vr*(C[n]-C[n-1])/2
   angular=vt*((m-1)*C[n-1]-(m+1)*C[n])/2
   val=radial+angular;total+=val
   if n in (1,2,3,64,128,260,261):terms.append({'n':n,'value':box(val)})
  return total,terms
 first,w1=product(k,beta,d0,h);second,w2=product(beta,k,h,d0)
 rawlinear=radius**3*a(a2/k-1)*a(rows[2][0]);rawfirst=radius**5*first;rawsecond=radius**5*second
 c20=(rawlinear+rawfirst+rawsecond)/radius**a(a2);h20=(a(k)/a(2-2*k))*c20
 out={'utc':datetime.now(timezone.utc).isoformat(),'status':'COMPUTED_REQUIRES_AUDIT','method':'iv180 original NPZ Laurent projection, normalized radial/tangential Green sums (2), separate coordinate scale','files':{str(p.relative_to(B)):sha(p) for p in (norm,raw,D/'PROOF.md',Path(__file__))},'source_archive':{'path':str(P),'sha256':sha(P)},'exact':{'k':str(k),'tplus':str(t),'beta':str(beta),'a2':str(a2),'rows':[[str(x) for x in row] for row in rows]},'values':{n:box(v) for n,v in {'C20':c20,'H20':h20,'linear':rawlinear/radius**a(a2),'first':rawfirst/radius**a(a2),'second':rawsecond/radius**a(a2),'z':z}.items()},'witnesses':[w1,w2],'counts':{'row_input_coefficients':780,'projected_sines':786,'leading_residual_inputs':522,'used_leading_residual_inputs':262,'Green_terms':522,'positive_denominators':1044,'antisymmetry_checks':786},'seconds':time.monotonic()-st}
 (E/'iv.json').write_text(json.dumps(out,indent=2)+'\n');print(json.dumps({n:v['display'] for n,v in out['values'].items()}));print(out['seconds'])
if __name__=='__main__':run()
