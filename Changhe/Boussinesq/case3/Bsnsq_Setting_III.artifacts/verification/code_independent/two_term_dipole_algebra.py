"""Independent exact algebra for the dipole obstruction; no solver imports."""
from pathlib import Path
from datetime import datetime,timezone
import json,time
import sympy as s
start=time.monotonic()
nu,A,B,r,th=s.symbols('nu A B r th',real=True,nonzero=True)
m=1-2*nu
C=A/(1-(2-nu)**2)
psi=C*r**(2-nu)*s.cos(th)
omega=A*r**(-nu)*s.cos(th)
lap=s.diff(psi,r,2)+s.diff(psi,r)/r+s.diff(psi,th,2)/r**2
ur=-s.diff(psi,th)/r;ut=s.diff(psi,r)
adv=ur*s.diff(omega,r)+ut*s.diff(omega,th)/r
hp=C*A/nu*s.sin(th)-B/m
lhs=m*s.cos(th)*hp-s.sin(th)*s.diff(hp,th)
rhs=-2*C*A*s.sin(th)*s.cos(th)-B*s.cos(th)
checks={'poisson_sign':s.simplify(-lap-omega),'radial_velocity':s.simplify(ur-C*r**(1-nu)*s.sin(th)),'angular_velocity':s.simplify(ut-(2-nu)*C*r**(1-nu)*s.cos(th)),'advection':s.simplify(adv+2*C*A*r**(-2*nu)*s.sin(th)*s.cos(th)),'particular_solution':s.simplify(lhs-rhs)}
c2=C.subs(nu,s.Rational(1,2));h2=2*c2*A*s.sin(th)
checks['beta2_particular']=s.simplify(-s.sin(th)*s.diff(h2,th)+2*c2*A*s.sin(th)*s.cos(th))
assert all(v==0 for v in checks.values()), checks
out={'utc':datetime.now(timezone.utc).isoformat(),'method':'SymPy exact differentiation of independently derived homogeneous stream and angular equation','zeros':{k:str(v) for k,v in checks.items()},'status':'PASSED','elapsed_seconds':time.monotonic()-start}
Path('research/52_two_term_dipole_obstruction/verification/algebra.json').write_text(json.dumps(out,indent=2)+'\n')
print(json.dumps(out,indent=2))
