"""Exact checks for the independently proved outgoing beta2 construction."""
from pathlib import Path
from datetime import datetime,timezone
import json,hashlib,sys,time
import sympy as s
root=Path(sys.argv[1]);root.mkdir(parents=True,exist_ok=True)
start=time.monotonic();out={'started_utc':datetime.now(timezone.utc).isoformat(),'checks':[]}
def check(name,value):
    q=s.simplify(value)
    passed=all(e==0 for e in q) if isinstance(q,s.MatrixBase) else q==0
    out['checks'].append({'name':name,'difference':str(q),'pass':passed})
    if not passed: raise AssertionError((name,q))
x,Y=s.symbols('x Y',real=True);chi=s.Function('chi')(x);a=chi+x*s.diff(chi,x);v=2*x*(1-chi)
stream=2*x*Y*chi
W=s.Matrix([2*x-s.diff(stream,Y),2*Y+s.diff(stream,x)])
check('endpoint W',W-s.Matrix([v,2*Y*(1+a)]))
omega=-s.diff(stream,x,2)-s.diff(stream,Y,2)
check('endpoint vorticity',omega+2*Y*s.diff(a,x))
f=W[0]*s.diff(omega,x)+W[1]*s.diff(omega,Y)+omega
check('endpoint residual',f+2*Y*(v*s.diff(a,x,2)+(3+2*a)*s.diff(a,x)))
rho=Y/v
check('backward wedge ratio',-W[0]*s.diff(rho,x)-W[1]*s.diff(rho,Y)-(s.diff(v,x)-2*(1+a))*rho)
ell=s.symbols('ell',real=True);h=s.sqrt(1+ell**2/16)
tau=s.Matrix([1,ell/4])/h;n=s.Matrix([-ell/4,1])/h;theta_prime=ell/h
check('orthonormal frame norm tau',(tau.T*tau)[0]-1)
check('orthonormal frame norm n',(n.T*n)[0]-1)
check('orthonormal frame cross',(tau.T*n)[0])
check('arc DW tensor',(4*n+ell*tau)*n.T-s.Matrix([[0,0],[-ell,4]]))
check('arc temperature gradient',theta_prime*(tau-ell*n/4)-s.Matrix([ell,0]))
check('arc compatibility',ell*(1-theta_prime*tau[1]/4)-theta_prime*tau[0])
check('endpoint matrix',((4*n+ell*tau)*n.T).subs(ell,0)-s.diag(0,4))
y,kappa,a0,m1,m2=s.symbols('y kappa a0 m1 m2',positive=True)
rr=kappa*y*(12*m2/y**3+16*m2**2/y**5-2*a0*m1**2/y**2)
limit=s.limit(y*s.sqrt(1+kappa**2)*rr,y,s.oo)
check('exterior ray nonzero limit',limit+2*a0*m1**2*kappa*s.sqrt(1+kappa**2))
out.update(status='PASS',ended_utc=datetime.now(timezone.utc).isoformat(),elapsed_seconds=time.monotonic()-start)
for key,path in [('code',Path(__file__)),('proof',Path('research/158_beta2_outgoing_residual/PROOF.md'))]:
    out[key+'_sha256']=hashlib.sha256(path.read_bytes()).hexdigest()
(root/'results.json').write_text(json.dumps(out,indent=2)+'\n')
print(json.dumps(out,indent=2))
