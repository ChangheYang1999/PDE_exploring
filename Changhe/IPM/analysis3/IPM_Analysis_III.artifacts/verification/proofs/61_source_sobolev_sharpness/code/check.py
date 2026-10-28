from pathlib import Path
from fractions import Fraction as Q
from datetime import datetime,timezone
import hashlib,json
import sympy as s
from flint import arb,ctx
ctx.prec=256
root=Path(__file__).resolve().parents[3]
source=root/'proofs/15_modal_source/evidence/source_512_result.json'
data=json.loads(source.read_text())['results']['whole']
def pair(name):return tuple(Q(data[name][k]) for k in ('lower_exact','upper_exact'))
A0,A1=pair('wprime');mu0,mu1=pair('mu');g0,g1=pair('g')
q=((1+g0)/A1,(1+g1)/A0)
d=(1+mu0/A1,1+mu1/A0)
fast=(Q(1,2)+(1+g0+mu0/2)/A1,Q(1,2)+(1+g1+mu1/2)/A0)
slow=(Q(1,2)+(1+A0/2)/mu1,Q(1,2)+(1+A1/2)/mu0)
def output(interval):
 out=[]
 for v in interval:
  x=arb(v.numerator)/v.denominator
  out.append({'exact':str(v),'decimal':x.str(35)})
 return out
A,mu,g=s.symbols('A mu g',positive=True)
a=g/(A-mu);qq=(1+g)/A;dd=1+mu/A
assert s.simplify(qq+dd-a+(a*mu-A-mu-1)/A)==0
assert s.simplify(qq+dd/2-(1+g+(A+mu)/2)/A)==0
assert fast[1]<slow[0]
minimum=(Q(10)-Q(101,100))*(1+(Q(10)+Q(101,100))/2)-Q(101,100)*30
assert minimum==Q(563599,20000)
res={'date':datetime.now(timezone.utc).isoformat(),'source_certificate_sha256':hashlib.sha256(source.read_bytes()).hexdigest(),'source_original_sha256':json.loads(source.read_text())['input_sha256'],'q':output(q),'d':output(d),'s_fast':output(fast),'s_slow':output(slow),'fast_active':True,'box_gap_exact':str(minimum),'scaling_identities':'PASS','interpretation':'exact rational consequences of the independently certified whole source interval'}
(root/'proofs/61_source_sobolev_sharpness/evidence/check.json').write_text(json.dumps(res,indent=2)+'\n')
for k in ('q','d','s_fast','s_slow'):print(k,[v['decimal'] for v in res[k]])
