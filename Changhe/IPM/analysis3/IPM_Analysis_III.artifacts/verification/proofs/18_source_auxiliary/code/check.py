from pathlib import Path
from fractions import Fraction as F
from datetime import datetime,timezone
import hashlib,json,itertools
from flint import arb,ctx
import sympy as s
ctx.prec=384
p=Path(__file__).resolve().parents[1]
x=F(31,10)
slow=[];fast=[];ds=[]
for A,mu,g in itertools.product([F(10),F(51,5)],[F(99,100),F(101,100)],[F(29),F(30)]):
 slow.append(1+A/2+(F(1,2)-x)*mu)
 fast.append(1+(F(1,2)-x)*A+mu/2+g)
 ds.append(1+(A+mu)/2-F(1687,500))
assert min(slow)==F(1687,500) and min(fast)==F(159,40) and min(ds)==F(3121,1000)
th=s.symbols('theta',real=True)
ang=s.integrate(s.cos(th)**4*s.sin(th)**2,(th,0,2*s.pi))
assert ang==s.pi/8
C=1/(8*(arb.pi()*(arb(31)/10-1)*(arb(31)/10-2)).sqrt())
out={'time_utc':datetime.now(timezone.utc).isoformat(),'slow_box_margin':str(min(slow)),'fast_box_margin':str(min(fast)),'d_lower_bound':str(min(ds)),'angular_integral':str(ang),'sharp_strain_H3.1_norm':C.str(70),'proof_sha256':hashlib.sha256((p/'PROOF.md').read_bytes()).hexdigest(),'status':'PASS for exact box and sharp-strain arithmetic'}
(p/'evidence'/'check.json').write_text(json.dumps(out,indent=2)+'\n');print(json.dumps(out,indent=2))
