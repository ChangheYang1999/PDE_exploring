"""Independent exact algebra for finite-regularity and concentration claims."""
import os
os.environ['OPENBLAS_NUM_THREADS']='1'
os.environ['MKL_NUM_THREADS']='1'
os.environ['OMP_NUM_THREADS']='1'
from pathlib import Path
from datetime import datetime,timezone
import json
import sympy as s
th,t,A,a,d=s.symbols('theta t A a d',real=True)
B=A-1;c=s.cos(th);sn=s.sin(th)
q=A*c*c+sn*sn
row=s.Matrix([[(d*q-1)/(B*sn*c),a*(d+1)/(B*sn),-a/(B*c)]])
M=s.Matrix.vstack(row,s.Matrix([[0,0,1]]),sn*row+s.Matrix([[-d*c,-(d+1)**2,0]]))
Rx=M.applyfunc(lambda z:s.simplify(s.limit(th*z,th,0,dir='+')))
expectx=s.Matrix([[(A*d-1)/B,a*(d+1)/B,0],[0,0,0],[0,0,0]])
assert s.simplify(Rx-expectx)==s.zeros(3)
S=s.diag(1,1,-1)
My=-S*M.subs(th,s.pi/2-t)*S
Ry=My.applyfunc(lambda z:s.simplify(s.limit(t*z,t,0,dir='+')))
expecty=s.Matrix([[-(d-1)/B,0,-a/B],[0,0,0],[(d-1)/B,0,a/B]])
assert s.simplify(Ry-expecty)==s.zeros(3)
z=s.symbols('z')
assert s.factor(Rx.charpoly(z).as_expr()-z*z*(z-(A*d-1)/B))==0
assert s.factor(Ry.charpoly(z).as_expr()-z*z*(z-(a-d+1)/B))==0
assert s.simplify(Ry*s.Matrix([1,0,-1])-(a-d+1)/B*s.Matrix([1,0,-1]))==s.zeros(3,1)
checks=[{'item':'coupled_polar_endpoint_residues','exact':True}]
for dv in [s.Rational(5,4),s.Rational(3,2),s.Rational(7,4)]:
    av=(dv-1)*(dv+3);Av=dv
    Theta=s.sin(th);Phi=-s.sin(2*th)/(2*(dv+3))
    eq1=(dv*(Av*c*c+sn*sn)-1)*Theta-(Av-1)*sn*c*s.diff(Theta,th)+av*((dv+1)*c*Phi-sn*s.diff(Phi,th))
    eq2=s.diff(Phi,th,2)-sn*s.diff(Theta,th)+dv*c*Theta+(dv+1)**2*Phi
    assert s.trigsimp(s.expand_trig(eq1))==0
    assert s.trigsimp(s.expand_trig(eq2))==0
    checks.append({'item':'smooth_angular_frozen_example','d':str(dv),'A':str(Av),'a':str(av),'exact':True})
for Av,av,al,dv in [(s.Rational(2),s.Rational(4),s.Rational(1,5),s.Rational(13,10)),(s.Rational(5),s.Rational(18),s.Rational(1,2),s.Rational(7,4))]:
    Bv=Av-1;q0=1+al
    assert q0<dv<min(2,av+1-Bv*q0)
    kx=(Av*dv-1)/Bv;ky=(av-dv+1)/Bv
    assert min(dv,kx,ky)>q0
    assert kx.q>1 and ky.q>1
    checks.append({'item':'strict_endpoint_interval','A':str(Av),'a':str(av),'alpha':str(al),'d':str(dv),'kx':str(kx),'ky':str(ky),'exact':True})
x,y,da=s.symbols('x y da',real=True)
r=s.symbols('r',positive=True)
f=da*(y+(3*x*x*y-y**3)/2)*s.exp(-x*x-y*y)
assert s.diff(f,y).subs({x:0,y:0})==da
assert s.diff(f,x,2,y).subs({x:0,y:0})/2==da/2
moment=s.integrate(da*r*s.exp(-r*r)/2,(r,0,s.oo))
assert moment==da/4
checks.append({'item':'concentrated_zero_strain_countertest','slope':'da','strain':str(-da/4+moment),'cubic':'da/(2 epsilon^2)','exact':True})
b,e,cf,q1,q2=s.symbols('b e cf q1 q2',real=True)
H=q1-q2
jet=(a-4*A)*b-3*a*H-4*a*cf
assert s.expand(jet.subs(q2,-b/3-q1)+2*(2*A*b+3*a*q1+2*a*cf))==0
checks.append({'item':'inner_forced_cubic_identity','exact':True})
result={'updated_utc':datetime.now(timezone.utc).isoformat(),'verdict':'PASS','scope':'Exact algebra only; endpoint series, compactness hypotheses and convergence arguments are supplied in the standalone proof.','checks':checks}
p=Path('research/finite_regularity_and_concentration/verification');p.mkdir(parents=True,exist_ok=True)
(p/'exact_checks.json').write_text(json.dumps(result,indent=2)+'\n')
print(json.dumps(result,indent=2))
