"""Audit saved endpoints using exact polynomial formulas and fresh Arb1536."""
import os
for k in ('OMP_NUM_THREADS','OPENBLAS_NUM_THREADS','MKL_NUM_THREADS','NUMEXPR_NUM_THREADS'):os.environ[k]='1'
import sys,json,hashlib,time
from fractions import Fraction as F
from pathlib import Path
from datetime import datetime,timezone
from flint import arb,ctx,fmpq
assert not sys.flags.optimize
B=Path(__file__).resolve().parents[3];E=B/'research/midrad_product/evidence';sha=lambda p:hashlib.sha256(Path(p).read_bytes()).hexdigest()
def aa(q):q=F(q);return arb(fmpq(q.numerator,q.denominator))
def ends(x):return [F(int(m))*F(2)**int(e) for m,e in [a.man_exp() for a in (x.lower(),x.upper())]]
def main():
 start=time.monotonic();ctx.prec=1536;ctx.threads=1;d=json.loads((E/'checks.json').read_text());assert d['status']=='PASS'
 assert d['proof_sha256']==sha(B/'research/midrad_product/PROOF.md') and d['code_sha256']==sha(B/'research/midrad_product/code/check_bounds.py')
 for p,h in d['source_pins'].items():assert sha(B/p)==h
 u=F(1,2**53);checks=0;identities=0
 assert [row['K'] for row in d['cases']]==[2,3,4,8,13,14,16,31,64,127,128,260,261,262,512,1000,1024]
 for row in d['cases']:
  K=row['K'];den=(1-K*u)*(1-2*K*u)
  x={'prop_margin':u*(K-2+u)/(1-K*u),'underflow_margin':(8*(K+1)*den-K*(4-6*u+3*u*u))/(2*den),'sum_margin':u-K*(K-1)*u*u,'weighted_margin':u-K*(K+1)*u*u}
  for n,q in x.items():
   assert q>0 and q==F(row['exact'][n]);identities+=1
   # Different fresh expression from the interval checker: exact rational first,
   # then Arb rational conversion. This independently tests serialized endpoints.
   a,b=ends(aa(q))
   for method in ('arb','iv'):
    lo=F(row['values'][method][n]['lower_exact']);hi=F(row['values'][method][n]['upper_exact']);assert 0<lo<=a<=q<=b<=hi,(K,n,method);checks+=1
 assert d['positive_exact_checks']==4095
 # Reconstruct the bookkeeping stream without importing the checker.
 dig=hashlib.sha256()
 for K in range(1,1025):
  den=(1-K*u)*(1-2*K*u)
  x={'prop_margin':u*(K-2+u)/(1-K*u),'underflow_margin':(8*(K+1)*den-K*(4-6*u+3*u*u))/(2*den),'sum_margin':u-K*(K-1)*u*u,'weighted_margin':u-K*(K+1)*u*u}
  dig.update((str(K)+':'+';'.join(n+'='+str(q) for n,q in x.items())+'\n').encode())
 assert dig.hexdigest()==d['coverage_sha256']
 obj={'utc':datetime.now(timezone.utc).isoformat(),'status':'PASS','fresh_precision':1536,'containments':checks,'selected_exact_identities':identities,'all_K_coverage_digest_verified':True,'input_sha256':sha(E/'checks.json'),'code_sha256':sha(__file__),'proof_sha256':sha(B/'research/midrad_product/PROOF.md'),'seconds':time.monotonic()-start,'scope':d['scope']};(E/'output_audit.json').write_text(json.dumps(obj,indent=2)+'\n');print(json.dumps(obj))
if __name__=='__main__':main()
