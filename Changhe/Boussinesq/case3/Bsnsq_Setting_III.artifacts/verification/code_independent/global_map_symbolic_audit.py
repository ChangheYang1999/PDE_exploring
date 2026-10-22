from pathlib import Path
from datetime import datetime,timezone
import time,json,hashlib
import sympy as s
start=time.monotonic();xi,eta=s.symbols('xi eta',real=True);la,mu,beta,a=s.symbols('lambda mu beta a',positive=True)
x=s.Function('x')(xi,eta);y=s.Function('y')(xi,eta)
DX=s.Matrix([[s.diff(x,xi),s.diff(x,eta)],[s.diff(y,xi),s.diff(y,eta)]])
W=DX*s.Matrix([la*xi,mu*eta]);g=DX.T*DX
pull=g*s.Matrix([la*xi,mu*eta]);curlpull=s.diff(pull[1],xi)-s.diff(pull[0],eta)
curlphys=(s.diff(y,eta)*s.diff(W[1],xi)-s.diff(y,xi)*s.diff(W[1],eta)+s.diff(x,eta)*s.diff(W[0],xi)-s.diff(x,xi)*s.diff(W[0],eta))/DX.det()
explicit=(la-mu)*g[0,1]+la*xi*(s.diff(g[0,1],xi)-s.diff(g[0,0],eta))+mu*eta*(s.diff(g[1,1],xi)-s.diff(g[0,1],eta))
checks={}
checks['pullback_with_general_determinant']=s.simplify(curlpull-DX.det()*curlphys)
checks['metric_expansion']=s.simplify(curlpull-explicit)
H=s.Function('H')(xi,eta)
dg=s.Matrix([[-2*s.diff(H,xi,eta),s.diff(H,xi,2)-s.diff(H,eta,2)],[s.diff(H,xi,2)-s.diff(H,eta,2),2*s.diff(H,xi,eta)]])
dp=dg*s.Matrix([la*xi,mu*eta]);lap=s.diff(H,xi,2)+s.diff(H,eta,2)
checks['hamiltonian_first_variation']=s.simplify(s.diff(dp[1],xi)-s.diff(dp[0],eta)-la*xi*s.diff(lap,xi)-mu*eta*s.diff(lap,eta)-(la-mu)*(s.diff(H,xi,2)-s.diff(H,eta,2)))
lam=(beta-2)/2;m=(3*beta+2)/2;kprime=-4*a/(beta*(beta+6))
Xp=s.Matrix([xi,eta-kprime*xi**2]);Jp=Xp.jacobian([xi,eta]);Wp=Jp*s.Matrix([lam*xi,m*eta]);gp=Jp.T*Jp;pp=gp*s.Matrix([lam*xi,m*eta]);om=-s.diff(pp[1],xi)+s.diff(pp[0],eta)
checks['shear_det']=s.simplify(Jp.det()-1)
checks['shear_omega']=s.simplify(om-4*a*xi/beta)
checks['shear_vorticity_equation']=s.simplify(lam*xi*s.diff(om,xi)+m*eta*s.diff(om,eta)+om-2*a*xi)
r,theta,aa,bb=s.symbols('r theta aa bb',positive=True);q=s.Function('q')(theta);h=s.Function('h')(theta)
zz=s.Matrix([r**aa*q,r**bb*h]);jac=zz.jacobian([r,theta]).det()/r
checks['weighted_angular_area']=s.simplify(jac-r**(aa+bb-2)*(aa*q*s.diff(h,theta)-bb*s.diff(q,theta)*h))
Jrot=s.Matrix([[0,-1],[1,0]]);reflect=s.diag(-1,1)
checks['reflection_anticommutator']=sum((reflect*Jrot+Jrot*reflect).applyfunc(s.simplify))
path=Path('research/64_global_source_map_adjoint/verification/symbolic_results.json')
out={'written_utc':datetime.now(timezone.utc).isoformat(),'elapsed_seconds':time.monotonic()-start,'sympy':s.__version__,'code_sha256':hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),'checks':{k:str(v) for k,v in checks.items()},'passed':all(v==0 for v in checks.values()),'scope':'Algebraic identities only. The standalone informal proof supplies domain, convergence and asymptotic arguments.'}
path.write_text(json.dumps(out,indent=2)+'\n');print(json.dumps(out,indent=2));assert out['passed']
