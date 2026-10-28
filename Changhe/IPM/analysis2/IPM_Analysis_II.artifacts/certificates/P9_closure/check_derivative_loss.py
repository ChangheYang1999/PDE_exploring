from pathlib import Path
from datetime import datetime,timezone
import sympy as s
import json
x,y=s.symbols('x y',real=True)
q=x*x+y*y
chi=q**3*s.exp(-q)
psi=s.diff(chi,x,y)
phi=-s.diff(s.diff(chi,x,2)+s.diff(chi,y,2),y)
u1=-s.diff(psi,y);u2=s.diff(psi,x)
c=s.simplify(s.diff(psi,x,y).subs({x:0,y:0}))
b=s.simplify(s.diff(phi,y).subs({x:0,y:0}))
quad=s.expand(u1*s.diff(phi,x)+u2*s.diff(phi,y))
values={'center_jet':str(b),'strain':str(c),'velocity_y_at_0_1':str(s.simplify(u2.subs({x:0,y:1}))),'rho_y_at_0_1':str(s.simplify(s.diff(phi,y).subs({x:0,y:1}))),'quadratic_at_0_1':str(s.simplify(quad.subs({x:0,y:1})))}
assert b==0 and c==0
assert s.simplify(quad.subs({x:0,y:1})-768*s.exp(-2))==0
assert s.simplify(-s.diff(psi,x,2)-s.diff(psi,y,2)-s.diff(phi,x))==0
out={'utc':datetime.now(timezone.utc).isoformat(timespec='seconds'),'values':values,'canonical_Poisson_identity':True,'status':'PASS'}
Path(__file__).with_suffix('.json').write_text(json.dumps(out,indent=2)+'\n')
print(json.dumps(out,indent=2))
