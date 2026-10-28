"""Exact outward report intervals and origin-hypothesis checks."""
from pathlib import Path
from fractions import Fraction as F
from datetime import datetime,timezone
import json,hashlib
from flint import arb,ctx
ctx.prec=512
root=Path(__file__).resolve().parents[1]
r=json.loads((root/'evidence/bounds_audit.json').read_text())['outputs'][1]
def aa(x):return arb(x.numerator)/x.denominator if isinstance(x,F) else arb(x)
def bb(rec):return aa(F(rec['lower_exact'])).union(aa(F(rec['upper_exact'])))
c=bb(r['strain']);d=bb(r['defect']);k=F(1615536043799051,2**53)
clo=F('15.726087821623500282');chi=F('15.726087821623500289')
dlo=F('1.0301137738456e-8');dhi=F('1.0301137743913e-8')
assert aa(clo)<c<aa(chi) and aa(dlo)<d<aa(dhi)
assert bb(r['error'])<aa(F('2.728174e-18'))
checks=[]
for name,ell in [('held',1/aa(k)),('normalized',(1+c)/3)]:
 a=ell-c;b=ell+c;p=(2*b-1)/(b-a);q=(1-2*a)/(b-a)
 assert a<0<b and p>aa(F(1,2)) and q>aa(F(1,2))
 assert 1+2*ell-c<0<1+2*ell+c
 checks.append({'convention':name,'ell':ell.str(50),'a':a.str(50),'b':b.str(50),'p2':p.str(50),'q2':q.str(50),'origin_energy_xx':(1+2*ell-c).str(50),'origin_energy_yy':(1+2*ell+c).str(50)})
out={'date':datetime.now(timezone.utc).isoformat(),'status':'PASS','strain_interval':[str(clo),str(chi)],'defect_interval':[str(dlo),str(dhi)],'mathematical_error_upper':str(F('2.728174e-18')),'origin_checks':checks,'bits':ctx.prec,'script_sha256':hashlib.sha256(Path(__file__).read_bytes()).hexdigest()}
(root/'evidence/consequences.json').write_text(json.dumps(out,indent=2)+'\n');print(json.dumps(out,indent=2))
