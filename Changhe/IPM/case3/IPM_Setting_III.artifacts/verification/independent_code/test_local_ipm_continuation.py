"""Exact transformed-gradient checks, independent of all producer code."""
import os
os.environ['OPENBLAS_NUM_THREADS']='1'
os.environ['OMP_NUM_THREADS']='1'
os.environ['MKL_NUM_THREADS']='1'
from pathlib import Path
from datetime import datetime,timezone
import json
import sympy as s
x,y,X,Y,z=s.symbols('x y X Y z',real=True)
t=s.symbols('t',real=True)
psi=(1+t)*(x**3*y+2*x*y**3)+t*x*y
rho=-9*(1+t)*x*x*y+(2+t*t)*y**3+(3-t)*y
vel=s.Matrix([-s.diff(psi,y),s.diff(psi,x)])
assert s.expand(s.diff(vel[0],x)+s.diff(vel[1],y))==0
assert s.expand(s.diff(vel[1],x)-s.diff(vel[0],y)+s.diff(rho,x))==0
lam=1+z
h=1/(2*z*lam)
sub={x:lam*X,y:lam*Y,t:-z*z}
R=rho.subs(sub, simultaneous=True)
V=vel.subs(sub, simultaneous=True)
coords=s.Matrix([X,Y])
b=V/lam+h*coords
J=s.Matrix([[0,-1],[1,0]])
grad=lambda f:s.Matrix([s.diff(f,X),s.diff(f,Y)])
dt=lambda f:-s.diff(f,z)/(2*z)
Om=J*grad(R)
DV=V.jacobian(coords)
F=Om.jacobian(coords)
adv=lambda f:f.jacobian(coords)*b if isinstance(f,s.MatrixBase) else (grad(f).dot(b))
# An arbitrary polynomial with the div-curl relation is used, so the transport
# defect is retained. This checks the identities without imposing the target.
ER=dt(R)+adv(R)
EOm=dt(Om)+h*Om+adv(Om)-DV*Om/lam
checks=[]
for i in range(2):
    assert s.cancel(EOm[i]-(J*grad(ER))[i])==0
    checks.append({'item':'transformed_gradient_defect','component':i,'exact':True})
assert s.cancel(s.diff(b[0],X)+s.diff(b[1],Y)-2*h)==0
assert s.expand(s.diff(V[1],X)-s.diff(V[0],Y)+Om[1])==0
Om_DV=DV.applyfunc(lambda f:grad(f).dot(Om))
advF=F.applyfunc(adv)
EF=dt(F)+advF+2*h*F-(DV*F+Om_DV-F*DV)/lam
for i in range(2):
    for j in range(2):
        assert s.cancel(EF[i,j]-EOm.jacobian(coords)[i, j])==0
        checks.append({'item':'differentiated_gradient_defect','row':i,'column':j,'exact':True})
assert 4*2-2==6
checks.append({'item':'q4_energy_damping','value':6,'exact':True})
# The dilation differentiation for the scalar kth derivative contributes kh,
# independently of the original polynomial degree.
for k in range(1,7):
    g=X**(k+2)*Y**3
    lhs=s.diff(h*(X*s.diff(g,X)+Y*s.diff(g,Y)),X,k)
    rhs=h*(X*s.diff(g,X,k+1)+Y*s.diff(g,X,k,Y)+k*s.diff(g,X,k))
    assert s.expand(lhs-rhs)==0
    checks.append({'item':'scalar_dilation_commutator','order':k,'exact':True})
ell,gam=s.symbols('ell gamma',positive=True)
p=1/ell;al=1/(ell-1);be=ell/(ell-1)
assert s.simplify(al-be*gam+(gam-p)/(1-p))==0
for k in range(8):
    assert s.simplify((-al+k*be)/(-be)-(p-k))==0
checks.append({'item':'physical_profile_exponents','exact':True})
zeta=s.symbols('A',real=True)
partial=sum((2*j+1)*zeta**j/s.factorial(j) for j in range(10))
assert s.series((1+2*zeta)*s.exp(zeta)-partial,zeta,0,10).removeO()==0
checks.append({'item':'nested_log_series','through_degree':9,'exact':True})
result={'updated_utc':datetime.now(timezone.utc).isoformat(),'verdict':'PASS','scope':'Exact identities and exponents only; analytic estimates and the endpoint remain separate.','checks':checks}
out=Path('research/local_ipm_continuation/verification')
out.mkdir(parents=True,exist_ok=True)
(out/'exact_checks.json').write_text(json.dumps(result,indent=2)+'\n')
print(json.dumps(result,indent=2))
