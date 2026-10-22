"""Exact feasibility arithmetic, independently recomputed in mpmath.iv."""
import os
os.environ['PYTHONDONTWRITEBYTECODE']='1'
from pathlib import Path
from fractions import Fraction as F
from datetime import datetime,timezone
import json,hashlib
from mpmath import iv
iv.dps=100
BASE=Path(__file__).resolve().parents[3];E=BASE/'research/conormal_saddle/evidence'
def sha(p):return hashlib.sha256(Path(p).read_bytes()).hexdigest()
def iq(v):v=F(v);return iv.mpf(v.numerator)/v.denominator
def ends(v):
 out=[]
 for sign,m,e,bc in v._mpi_:
  assert bc>=0
  out.append((-1 if sign else 1)*F(int(m))*F(2)**int(e))
 return out
p=json.loads((E/'inputs.json').read_text());assert sha(BASE/p['modal_input'])==p['modal_sha256'];assert sha(BASE/p['reviewed_lead_snapshot'])==p['lead_sha256']
z=json.loads((BASE/p['modal_input']).read_text());k=F.from_float(float.fromhex(z['scalars_hex']['k']));assert k==F(p['k_exact'])
a,b,s,alpha=(F(p[v+'_exact']) for v in ('a','b','s','alpha'))
A=2/k-1;D=2*A+1;b0=(A+3)/2;beta3=(6*A+1)/D;delta=b*D-a*A-b0
f={'A':A,'D':D,'b0':b0,'beta3':beta3,'delta':delta,'s_minus_3_minus_alpha':s-3-alpha,'b_minus_s':b-s,'beta3_plus_half_minus_b':beta3+F(1,2)-b,'a_minus_lower':a-(b*D-b0)/A,'13halves_minus_a':F(13,2)-a,'beta3_minus_5halves_minus_alpha':beta3-F(5,2)-alpha}
assert all(f[x]>0 for x in f if x!='delta');assert delta<0
# Use direct k formulas instead of the A,D forms for an independent route.
ki=iq(k);ai,bi,si,al=map(iq,(a,b,s,alpha));Ai=(2-ki)/ki;Di=(4-ki)/ki;B0=(1+ki)/ki;B3=(12-5*ki)/(4-ki)
r={'A':Ai,'D':Di,'b0':B0,'beta3':B3,'delta':((4-ki)*bi-(2-ki)*ai-1-ki)/ki,'s_minus_3_minus_alpha':si-3-al,'b_minus_s':bi-si,'beta3_plus_half_minus_b':B3+iq(F(1,2))-bi,'a_minus_lower':ai-((4-ki)*bi-1-ki)/(2-ki),'13halves_minus_a':iq(F(13,2))-ai,'beta3_minus_5halves_minus_alpha':B3-iq(F(5,2))-al}
results={}
for key,exact in f.items():
 lo,hi=ends(r[key]);assert lo<=exact<=hi,key
 if key=='delta':assert hi<0
 else:assert lo>0
 results[key]={'exact':str(exact),'iv_lower_exact':str(lo),'iv_upper_exact':str(hi),'iv_display':str(r[key])}
# Polynomial identities at rational test parameters with different denominators.
identities=0
for A0 in [F(1,7),F(7,2),A,F(31,3)]:
 for al0 in [F(1,17),alpha,F(3,4)]:
  for nu in [F(1,9),F(1,2),F(1)]:
   d=2*A0+1;bb=F(5,2)+al0;aa=F(9,2)+nu
   assert bb*d-aa*A0-(A0+3)/2==A0*(2*al0-nu)+1+al0
   assert (1+(4+nu)*A0)-(2+al0)*d==A0*(nu-2*al0)-(1+al0)
   assert 2*(4+nu)-2*aa==-1
   identities+=3
out={'utc':datetime.now(timezone.utc).isoformat(),'status':'PASS','source_sha256':sha(__file__),'input_sha256':sha(E/'inputs.json'),'modal_sha256':p['modal_sha256'],'lead_sha256':p['lead_sha256'],'exact_and_iv_checks':len(results),'rational_identity_fixture_checks':identities,'results':results,'scope':'Algebraic feasibility only. No trace embedding, bounded coupling, global inverse or existence result.'}
(E/'feasibility_audit.json').write_text(json.dumps(out,indent=2)+'\n');print(json.dumps({'utc':out['utc'],'status':out['status'],'checks':len(results),'delta':str(delta),'delta_iv':str(r['delta'])}))
