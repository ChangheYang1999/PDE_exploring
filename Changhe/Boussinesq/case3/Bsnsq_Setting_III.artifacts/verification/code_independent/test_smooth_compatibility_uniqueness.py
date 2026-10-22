"""Independent exact controls for packet139; no solver or teammate imports."""
from pathlib import Path
from datetime import datetime, timezone
import json,time,sys
import sympy as s
import mpmath as mp
start=time.monotonic(); out=Path(sys.argv[1]);out.mkdir(parents=True,exist_ok=True)
x,y,k=s.symbols('x y k');V=s.Function('V')(x,y);t=s.Function('t')(x,y)
J=s.diff(V,x);B=s.diff(t,x)/J;A=t-V*B
M=J**2*s.diff(t,y)-J*V*s.diff(t,x,y)+(V*s.diff(J,y)+J*(k-s.diff(V,y)))*s.diff(t,x)
tests=[]
def check(name,expr):
 result=s.cancel(s.expand(expr));assert result==0,(name,result);tests.append({'name':name,'verdict':'PASS'})
check('generic quotient identity',M/J**2-s.diff(A,y)-k*B)
check('generic x differentiation',s.diff(M/J**2,x)+V*s.diff(B,x,y)+(s.diff(V,y)-k)*s.diff(B,x))
a,j=s.symbols('a j',nonzero=True);v=a*y+j*x*x/2;jv=s.diff(v,x)
def op(v,t,k):
 J=s.diff(v,x)
 return s.expand(J**2*s.diff(t,y)-J*v*s.diff(t,x,y)+(v*s.diff(J,y)+J*(k-s.diff(v,y)))*s.diff(t,x))
for n in range(1,9):check(f'threshold counterexample n={n}',op(v,x*x*y**(n-1),n*a))
for n in range(0,6):
 C=y**n;t0=v*s.diff(C,y)-k*C
 check(f'unnormalized kernel C=y^{n}',op(v,t0,k))
flat=x*x*s.exp(-1/y**2)
check('smooth flat residual formula',op(v,flat,k)-2*j*x*x*s.exp(-1/y**2)*(k-a-2*a/y**2))
# Degenerate J=0 makes M identically0 for any t: nondegeneracy is material.
check('degenerate J=0 blindness',op(a*y,x*x,k))
# Exact full stream-defined identities, including the local polynomial solution.
for beta in [s.Rational(1),s.Rational(2),s.Rational(9,4),s.Rational(3),s.Rational(7,2),s.Rational(10)]:
 c=1+beta/2;q=4/beta;kap=beta-2
 for sig in [-1,1]:
  for pert in [0,1]:
   psi=c*x*y-q*x**3/6
   if pert:psi+=s.Rational(sig,17)*(x**3-3*x*y**2)+s.Rational(1,31)*x*y**3+s.Rational(sig,43)*x**3*y**2
   om=-s.diff(psi,x,2)-s.diff(psi,y,2)
   w1=beta*x-s.diff(psi,y)+s.diff(psi,y).subs({x:0,y:0})
   w2=beta*y+s.diff(psi,x)-s.diff(psi,x).subs({x:0,y:0})
   def adv(f):return s.expand(w1*s.diff(f,x)+w2*s.diff(f,y))
   F=adv(om)+om;T=s.integrate(F,(x,0,x));tr=s.expand(adv(T)-kap*T)
   jj=s.diff(w2,x);D=s.expand((kap-s.diff(w1,x))*F-adv(F));Z=s.expand(w1*F*jj+w2*D)
   E=s.expand(jj*s.diff(Z,y)-Z*s.diff(jj,y)-kap*jj*D)
   check(f'B2 residual identity beta={beta} sign={sig} pert={pert}',E-op(w2,tr,kap))
   check(f'axis normalization beta={beta} sign={sig} pert={pert}',tr.subs(x,0))
   if not pert:
    check(f'exact polynomial primitive beta={beta} sign={sig}',T-x*x)
    check(f'exact polynomial thermal beta={beta} sign={sig}',tr)
   else:assert E!=0 and tr!=0
# Independent numerical derivatives of the smooth flat control, away from y=0.
mp.mp.dps=65
flat_checks=[]
for bb in [mp.mpf('2.25'),mp.mpf(3),mp.mpf('3.5')]:
 aa=1+3*bb/2;kk=bb-2;jj=mp.mpf('-1.7')
 for yy in [mp.mpf('.4'),mp.mpf('.6'),mp.mpf('-.7')]:
  xx=mp.mpf('.23');vv=lambda X,Y:aa*Y+jj*X*X/2;tt=lambda X,Y:X*X*mp.exp(-1/(Y*Y))
  vx=mp.diff(lambda X:vv(X,yy),xx);vy=mp.diff(lambda Y:vv(xx,Y),yy)
  tx=mp.diff(lambda X:tt(X,yy),xx);ty=mp.diff(lambda Y:tt(xx,Y),yy)
  txy=mp.diff(lambda Y:mp.diff(lambda X:tt(X,Y),xx),yy)
  j_y=mp.diff(lambda Y:mp.diff(lambda X:vv(X,Y),xx),yy)
  direct=vx*vx*ty-vx*vv(xx,yy)*txy+(vv(xx,yy)*j_y+vx*(kk-vy))*tx
  exact=2*jj*xx*xx*mp.exp(-1/(yy*yy))*(kk-aa-2*aa/(yy*yy))
  rel=abs(direct-exact)/max(abs(exact),mp.mpf('1e-100'))
  assert rel<mp.mpf('1e-60') and exact!=0
  flat_checks.append({'beta':str(bb),'x':str(xx),'y':str(yy),'M':str(direct),'relative_error':str(rel)})
res={'utc':datetime.now(timezone.utc).isoformat(),'elapsed_seconds':time.monotonic()-start,'exact_tests':tests,'exact_test_count':len(tests),'flat_finite_points':flat_checks,'scope':'Exact identities and manufactured tests, not a proof by computation or a global B2 candidate.'}
(out/'tests.json').write_text(json.dumps(res,indent=2)+'\n');print(json.dumps({'tests':len(tests),'flat_points':len(flat_checks),'elapsed':res['elapsed_seconds']},indent=2))
