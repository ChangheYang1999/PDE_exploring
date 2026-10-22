"""Independent exact controls for packet139 and the lead's new local example."""
from pathlib import Path
from datetime import datetime,timezone
import sys,time,json
import sympy as s
started=time.monotonic();root=Path(sys.argv[1]);root.mkdir(exist_ok=True,parents=True)
x,y=s.symbols('x y',real=True);a=s.symbols('a',positive=True);q=s.symbols('q',real=True)
b=a-q*y/2;A=b+x*x/2;V=y*A;J=s.diff(V,x)
t=2*A*s.log(A/b)-x*x
checks=[]
def check(name,v):
 v=s.simplify(s.expand(v))
 if v!=0:raise AssertionError((name,v))
 checks.append({'name':name,'passed':True})
check('J=xy',J-x*y)
check('x ODE',A*s.diff(t,x)-x*t-x**3)
check('mixed ODE',x*s.diff(t,y)-A*s.diff(t,x,y)-s.diff(A,y)*s.diff(t,x))
M=J**2*s.diff(t,y)-J*V*s.diff(t,x,y)+(V*s.diff(J,y)-J*s.diff(V,y))*s.diff(t,x)
check('scalar compatibility kernel',M)
check('axis value',t.subs(x,0));check('even parity',t.subs(x,-x)-t)
check('fourth derivative',s.diff(t,x,4).subs({x:0,y:0})-6/a)
P=(a-2)*x*y-q*x*y*y/2+x**3*y/6
check('stream W2 realization',2*y+s.diff(P,x)-V)
check('stream center strain',s.diff(P,x,y).subs({x:0,y:0})-(a-2))
O=-s.diff(P,x,2)-s.diff(P,y,2)
check('stream vorticity',O-(q*x-x*y))
P=P.subs(a,4);W=s.Matrix([2*x-s.diff(P,y),2*y+s.diff(P,x)])
F=s.expand(W.dot(s.Matrix([s.diff(O,x),s.diff(O,y)]))+O)
T=s.integrate(F,(x,0,x));actual=s.expand(W.dot(s.Matrix([s.diff(T,x),s.diff(T,y)])))
check('actual residual on y0',actual.subs(y,0)-(-q*x**4/6+q*x**6/36))
check('actual residual first degree3',s.Poly(actual,x,y).coeff_monomial(x*x*y)-(3*q*q-10))
# Explicit stream example newly inserted into lead 4.32, recomputed here.
beta,a0=s.symbols('beta a0',positive=True);q0=4*a0/beta;c=1+beta/2;k=beta-2
P=c*x*y-q0*x*y*y/2
W=s.Matrix([beta*x-s.diff(P,y),beta*y+s.diff(P,x)])
O=-s.diff(P,x,2)-s.diff(P,y,2)
F=s.expand(W.dot(s.Matrix([s.diff(O,x),s.diff(O,y)]))+O)
T=s.integrate(F,(x,0,x));tlead=s.expand(W.dot(s.Matrix([s.diff(T,x),s.diff(T,y)]))-k*T)
check('lead flat-J thermal residual',tlead-4*a0*a0*x*x*y*(12*a0*y+5*beta*beta+2*beta)/beta**3)
check('lead flat-J',s.diff(W[1],x))
check('lead center omega slope',s.diff(O,x).subs({x:0,y:0})-q0)
result={'utc':datetime.now(timezone.utc).isoformat(),'elapsed_seconds':time.monotonic()-started,'exact_count':len(checks),'checks':checks,'actual_scalar_stream_thermal_residual':str(actual),'lead_flatJ_residual':str(s.factor(tlead)),'scope':'The freely chosen scalar kernel is not claimed to be the normalized primitive residual. That distinction is checked by separately computing the latter. The lead flat-J example is local only.'}
(root/'tests.json').write_text(json.dumps(result,indent=2)+'\n');print(json.dumps(result,indent=2),flush=True)
