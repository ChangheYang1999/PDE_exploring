"""Physical rows and collected frequency-one Green form in Arb512.
No JS/TS, servers/listeners/tunnels, RLScience, or Lean/Lake.
"""
import os
for key in ('OMP_NUM_THREADS','OPENBLAS_NUM_THREADS','MKL_NUM_THREADS','NUMEXPR_NUM_THREADS'):os.environ[key]='1'
import json,hashlib,time,sys
from pathlib import Path
from fractions import Fraction as F
from datetime import datetime,timezone
from flint import arb,ctx
assert not sys.flags.optimize
B=Path(__file__).resolve().parents[3];D=B/'research/single_tail_second_row';E=D/'evidence'
def sha(p):return hashlib.sha256(p.read_bytes()).hexdigest()
def a(q):q=F(q);return arb(q.numerator)/q.denominator
def ep(x):m,e=x.man_exp();return F(int(m))*F(2)**int(e)
def box(x):
 assert x.is_finite();lo,hi=ep(x.lower()),ep(x.upper());assert lo<=hi
 return {'lower_exact':str(lo),'upper_exact':str(hi),'display':x.str(45)}
def interval(q):return a(q['lower_exact']).union(a(q['upper_exact']))
def run():
 st=time.monotonic();ctx.prec=512;ctx.threads=1
 source=B/'data_exact/modal_v2.json';assert sha(source)=='57f67a53c1ee5c8fd5ede8480428f1a5584123ac4e54b6d3530d091ea2a67ca6'
 data=json.loads(source.read_text());ar=data['arrays'];assert ar['Aout']['shape']==[260,10]
 exact=lambda x:F(float.fromhex(x));k=exact(data['scalars_hex']['k']);t=exact(ar['knots']['hex'][-1]);beta=2*k-1;a2=3*k-2
 assert 0<k<F(1,4)
 rows=[]
 for col in (0,1,2):
  d=[F(0)]*262
  for m in range(260):
   c=exact(ar['Aout']['hex'][m*10+col])
   for freq in (1+2*m,1-2*m,3+2*m,3-2*m):d[(abs(freq)-1)//2]+=F(1 if freq>0 else -1,8)*c
  assert d[261]==0;rows.append(d)
 norm=B/'research/modal_repair/evidence/scalar_result.json';nr=json.loads(norm.read_text());z=arb(nr['A00_correction']['ball'])
 assert a('-1.198605236453734890460334164888e-20')<z and z<a('-1.198605236453734890460334164887e-20')
 raw=B/'research/outer_leading_cancellation/evidence/leading_result.json';lead=json.loads(raw.read_text());assert F(lead['scalars_exact']['k'])==k and F(lead['scalars_exact']['tb'])==t
 eps=[]
 for j,r in enumerate(lead['residual_coefficients']):assert r['q']==j;eps.append(interval(r['value']))
 assert len(eps)==522
 d0=[a((3-k)*t).exp()*(a(x)+(z/4 if j in (0,1) else 0)) for j,x in enumerate(rows[0])]
 h=[a((3-beta)*t).exp()*a(x)+a(k/(1-k))*a(-beta*t).exp()*eps[j] for j,x in enumerate(rows[1])]
 def product(expa,expb,A,C):
  total=arb(0);terms=[]
  for n in range(1,262):
   m=2*n;aa=expa+1;den=m*m-aa*aa;assert den>0
   fn=(a(aa-m)*A[n-1]+a(aa+m)*A[n])/2
   val=fn/(2*a(den))*(a(m*(expa+expb+1)-aa)*C[n-1]-a(m*(expa+expb+1)+aa)*C[n]);total+=val
   if n in (1,2,3,64,128,260,261):terms.append({'n':n,'value':box(val)})
  return total,terms
 first,w1=product(k,beta,d0,h);second,w2=product(beta,k,h,d0)
 linear=a((3-a2)*t).exp()*a((a2/k-1)*rows[2][0]);c20=linear+first+second;h20=a(k/(2*(1-k)))*c20
 files={str(p.relative_to(B)):sha(p) for p in (source,norm,raw,D/'PROOF.md',Path(__file__))}
 out={'utc':datetime.now(timezone.utc).isoformat(),'status':'COMPUTED_REQUIRES_AUDIT','method':'Arb512 physical rows, signed four-frequency projection, collected Green product (3)','files':files,'exact':{'k':str(k),'tplus':str(t),'beta':str(beta),'a2':str(a2),'rows':[[str(x) for x in row] for row in rows]},'values':{n:box(v) for n,v in {'C20':c20,'H20':h20,'linear':linear,'first':first,'second':second,'z':z}.items()},'witnesses':[w1,w2],'counts':{'row_input_coefficients':780,'projected_sines':786,'leading_residual_inputs':522,'used_leading_residual_inputs':262,'Green_terms':522,'positive_denominators':522},'seconds':time.monotonic()-st}
 (E/'arb.json').write_text(json.dumps(out,indent=2)+'\n');print(json.dumps({n:v['display'] for n,v in out['values'].items()}));print(out['seconds'])
if __name__=='__main__':run()
