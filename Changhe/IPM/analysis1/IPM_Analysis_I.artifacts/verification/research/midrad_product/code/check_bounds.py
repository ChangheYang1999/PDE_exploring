"""Exact composed-rounding inequalities, independently enclosed in two interval systems."""
import os
for k in ('OMP_NUM_THREADS','OPENBLAS_NUM_THREADS','MKL_NUM_THREADS','NUMEXPR_NUM_THREADS'):os.environ[k]='1'
import sys,json,hashlib,math,time
from fractions import Fraction as F
from pathlib import Path
from datetime import datetime,timezone
from flint import arb,ctx,fmpq
from mpmath import iv
assert not sys.flags.optimize
B=Path(__file__).resolve().parents[3];E=B/'research/midrad_product/evidence'
sha=lambda p:hashlib.sha256(Path(p).read_bytes()).hexdigest()
U=F(1,2**53)
def aa(q):q=F(q);return arb(fmpq(q.numerator,q.denominator))
def ii(q):q=F(q);return iv.mpf(q.numerator)/q.denominator
def ends(x):
 if isinstance(x,arb):return [F(int(m))*F(2)**int(e) for m,e in [a.man_exp() for a in (x.lower(),x.upper())]]
 return [(-1 if s else 1)*F(int(m))*F(2)**int(e) for s,m,e,_ in x._mpi_]
def rec(x):a,b=ends(x);return {'lower_exact':str(a),'upper_exact':str(b),'display':[float(a),float(b)]}
def exact(K):
 u=U;g=K*u/(1-K*u);G=2*K*u/(1-2*K*u);c=K/(2*(1-K*u))
 return {'prop_margin':(1-u)**2/(1-K*u)-1,'underflow_margin':4*(K+1)-c*(1+G+3*(1+G)*(1-u)**2),'sum_margin':(1+K*u)*(1-(K-1)*u)-1,'weighted_margin':(1+(K+1)*u)*(1-K*u)-1}
def main():
 start=time.monotonic();ctx.prec=512;ctx.threads=1;iv.dps=180;digest=hashlib.sha256();checks=0
 for K in range(1,1025):
  x=exact(K);u=U;g=K*u/(1-K*u);G=2*K*u/(1-2*K*u);c=K/(2*(1-K*u))
  assert G*(1-g)==2*g
  assert (1+G)*(1-u)**2*(1-g)==(1-u)**2/(1-K*u)
  assert c*(1+G+3*(1+G)*(1-u)**2)<=F(64*K,21)<4*(K+1)
  for n,q in x.items():
   if n!='prop_margin' or K>=2:assert q>0,(K,n);checks+=1
  assert F(math.nextafter(float(2*K*u)/float(1-2*K*u),math.inf))>=G
  assert F(float(2*K*u))==2*K*u and F(float(1-2*K*u))==1-2*K*u
  assert F(float((K-1)*u))==(K-1)*u and F(float(1-(K-1)*u))==1-(K-1)*u
  assert F(math.nextafter(float(1+K*u),math.inf))>=1+K*u
  assert 1+(K+1)*u<=F(math.nextafter(float(1+(K+1)*u),math.inf))<F(3,2)
  if K>1:assert F(math.nextafter(float((K-1)*u)/float(1-(K-1)*u),math.inf))>=(K-1)*u/(1-(K-1)*u)
  digest.update((str(K)+':'+';'.join(n+'='+str(q) for n,q in x.items())+'\n').encode())
 selected=[2,3,4,8,13,14,16,31,64,127,128,260,261,262,512,1000,1024];rows=[]
 for K in selected:
  values={}
  for method,cv in [('arb',aa),('iv',ii)]:
   u=cv(U);g=K*u/(1-K*u);G=2*K*u/(1-2*K*u);c=K/(2*(1-K*u))
   if method=='arb':
    out={'prop_margin':(1+G)*(1-u)**2*(1-g)-1,'underflow_margin':4*(K+1)-c*(1+G+3*(1+G)*(1-u)**2),'sum_margin':(1+K*u)*(1-(K-1)*u)-1,'weighted_margin':(1+(K+1)*u)*(1-K*u)-1}
   else:
    out={'prop_margin':((K-2)*u+u*u)/(1-K*u),'underflow_margin':4*(K+1)-K*(1+3*(1-u)**2)/(2*(1-K*u)*(1-2*K*u)),'sum_margin':u*(1-K*(K-1)*u),'weighted_margin':u*(1-K*(K+1)*u)}
   values[method]={n:rec(v) for n,v in out.items()}
   for n,q in exact(K).items():
    a,b=ends(out[n]);assert 0<a<=q<=b,(method,K,n)
  rows.append({'K':K,'exact':{n:str(q) for n,q in exact(K).items()},'values':values})
 obj={'utc':datetime.now(timezone.utc).isoformat(),'status':'PASS','code_sha256':sha(__file__),'proof_sha256':sha(B/'research/midrad_product/PROOF.md'),'source_pins':{'research/flow_certificate/evidence/source/midrad.py':sha(B/'research/flow_certificate/evidence/source/midrad.py'),'research/flow_certificate/evidence/source/cert_resid.py':sha(B/'research/flow_certificate/evidence/source/cert_resid.py')},'K_sum_range':[1,1024],'K_matrix_range':[2,1024],'positive_exact_checks':checks,'coverage_sha256':digest.hexdigest(),'coverage_hash_scope':'Deterministic bookkeeping only; exact inequalities and output audit provide evidence.','cases':rows,'seconds':time.monotonic()-start,'scope':'Conditional arithmetic theorem only; actual BLAS evaluation tree, powers and full flow remain open.'}
 (E/'checks.json').write_text(json.dumps(obj,indent=2)+'\n');print(json.dumps({n:v for n,v in obj.items() if n!='cases'}))
if __name__=='__main__':main()
