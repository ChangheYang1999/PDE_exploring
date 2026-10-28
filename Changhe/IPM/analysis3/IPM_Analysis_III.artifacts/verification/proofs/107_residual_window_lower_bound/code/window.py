import os
for key in ('OPENBLAS_NUM_THREADS','OMP_NUM_THREADS','MKL_NUM_THREADS','NUMEXPR_NUM_THREADS'):os.environ[key]='1'
from pathlib import Path
from fractions import Fraction as F
from datetime import datetime,timezone
import importlib.util,json,hashlib,time
from flint import arb,ctx
ROOT=Path(__file__).resolve().parents[1];LANE=ROOT.parents[1]
sp=importlib.util.spec_from_file_location('pointaudit',LANE/'proofs/105_residual_norm_point_audit/code/check_points.py');P=importlib.util.module_from_spec(sp);sp.loader.exec_module(P)
G=P.G;ANG=P.ANG;aa=P.aa

def linear(ep,k):
 out=G.EP()
 for e,p in ep.terms.items():
  c=(3+e)/k-1
  out.addterm(e,[aa(c)*v+(aa(F(i+1)/k)*p[i+1] if i+1<len(p) else arb(0)) for i,v in enumerate(p)])
 return out

def main():
 ctx.prec=512;ctx.threads=1;start=time.monotonic();d=G.M.Data();G.check_hash(d);cache=G.load_cache(d)
 H=G.density_eps(d,'outer');DH=[h.deriv() for h in H];LH=[linear(h,d.k) for h in H];Pe,Qe,_,_=G.outer_eps(d,cache);mm=ANG.moments(1044);mass=ANG.beta_mass();results=[]
 for rad in [F(0),F(1,10),F(1,100),F(1,1000),F(1,10000),F(1,100000)]:
  mid=F(10);left=mid-rad;right=mid+rad;assert left>d.tp
  s=aa(left-d.tp).union(aa(right-d.tp));rh=[P.evaluate(v,s) for v in H];drh=[P.evaluate(v,s) for v in DH]
  pp=[P.evaluate(v,s) for v in Pe];qq=[P.evaluate(v,s) for v in Qe];ll=[P.evaluate(v,s) for v in LH]
  sins=P.residual_sines(rh,drh,pp,qq,arb(0))
  for j in range(len(rh)):sins[j]+=rh[j]+ll[j]
  B=P.cofactor(sins);q=ANG.quotient(B);mean=sum((v*aa(mm[j]) for j,v in enumerate(q)),arb(0))
  dist=arb(0) if mean.contains(0) else arb(mean.abs_lower())
  omint=arb(0) if not rad else ((aa(F(27,4)*right)).exp()-(aa(F(27,4)*left)).exp())*aa(F(4,27))
  lower=arb(omint.lower())*arb(mass.lower())*dist**2
  result={'left':str(left),'right':str(right),'mean':G.rec(mean),'weight_integral':G.rec(omint),'norm_square_lower':G.rec(lower),'status':'POSITIVE' if lower>0 else 'ZERO_OR_POINT'};results.append(result)
  print(json.dumps({'date':datetime.now(timezone.utc).isoformat(),'rad':str(rad),'mean':mean.str(16),'norm_lower':lower.sqrt().str(16),'seconds':time.monotonic()-start}),flush=True)
 out={'date':datetime.now(timezone.utc).isoformat(),'bits':512,'input_sha256':d.sha,'code_sha256':hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),'results':results,'seconds':time.monotonic()-start,'status':'EXPLORATORY_INTERVAL_ENCLOSURES'}
 (ROOT/'evidence/windows.json').write_text(json.dumps(out,indent=2)+'\n')
if __name__=='__main__':main()
