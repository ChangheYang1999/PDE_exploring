from pathlib import Path
from datetime import datetime,timezone
import json
import sympy as s
x,y,z,u,v=s.symbols('x y z u v',real=True);H=s.Matrix([[x,y],[y,z]]);S=s.Matrix([[u,v],[v,-u]]);Om=s.Matrix([[0,z],[-z,0]])
checks=[]
def zero(name,expr):
 assert s.simplify(expr)==0,(name,expr)
 checks.append(name)
zero('skew quadratic contraction',(s.Matrix([x,y]).T*Om*s.Matrix([x,y]))[0])
zero('tracefree Hessian contraction',s.trace(S*H*H)-s.trace(H)*s.trace(S*H))
zero('symmetric skew orthogonality',s.trace((S+Om).T*(S+Om))-s.trace(S*S)-s.trace(Om.T*Om))
V,R=s.symbols('V R',nonnegative=True);lam=(1+3/s.sqrt(2)+s.sqrt((3/s.sqrt(2)-1)**2+81))/2
mat=s.Matrix([[1,s.Rational(9,2)],[s.Rational(9,2),3/s.sqrt(2)]])
zero('largest eigenvalue formula',(mat-lam*s.eye(2)).det())
assert s.Rational(1,2)+s.Rational(1,320000)<s.Rational(71,100)**2
assert 81*71<s.Rational(199,2)**2
checks+=['explicit conditional interval strict contradiction']
ell=s.symbols('ell',positive=True);k,j=s.symbols('k j',integer=True,positive=True)
zero('finite nodal strain cross multiplication',(2*j*ell-1)*(k-1)-(2*ell-1)*(k-j)-(j-1)*(2*k*ell-1))
zero('double nodal strain',ell+(2*ell-1)-(3*ell-1))
# Integration by parts constants are verified by an explicit vector-valued Gaussian example.
f=s.Matrix([s.exp(-x*x-y*y),x*s.exp(-x*x-y*y)])
Dx=f.diff(x);Dy=f.diff(y);I=(Dx.dot(Dx)+Dy.dot(Dy))**2
lap=f.diff(x,2)+f.diff(y,2);normD=Dx.dot(Dx)+Dy.dot(Dy)
term1=-f.dot(lap)*normD;term2=-f.dot(Dx)*s.diff(normD,x)-f.dot(Dy)*s.diff(normD,y)
integ=lambda expr:s.integrate(s.integrate(s.expand(expr),(x,-s.oo,s.oo)),(y,-s.oo,s.oo))
zero('vector fourth power integration by parts',integ(I-term1-term2))
zero('vector Laplace Hessian L2 identity',integ(lap.dot(lap)-f.diff(x,2).dot(f.diff(x,2))-2*f.diff(x,y).dot(f.diff(x,y))-f.diff(y,2).dot(f.diff(y,2))))
C=6+3*s.sqrt(2)/2
result={'utc':datetime.now(timezone.utc).isoformat(),'status':'PASS','checks':checks,'Lambda':float(lam),'old_origin_ell_threshold':float(1+1/(C*s.sqrt(2)-2)),'sharper_origin_ell_threshold':float(1+1/(lam*s.sqrt(2)-2)),'scope':'Exact tensor, spectral and interval identities plus an independent vector manufactured integration. General inequalities, cutoff limits and flow arguments are proved in PROOF.md.'}
out=Path('research/sharper_energy_strain_cap/verification');(out/'checks.json').write_text(json.dumps(result,indent=2)+'\n');print(json.dumps(result,indent=2),flush=True)
