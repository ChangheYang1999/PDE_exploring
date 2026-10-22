"""Independent exact controls for local packet141, written after its proof."""
from pathlib import Path
from datetime import datetime,timezone
import sys,time,json
import sympy as s
start=time.monotonic();root=Path(sys.argv[1]);root.mkdir(parents=True,exist_ok=True)
x,y=s.symbols('x y',real=True);d,q=s.symbols('d q',nonzero=True,real=True);b=s.Function('b')(y)
checks=[]
def check(name,expr):
 z=s.simplify(s.expand(expr))
 if z!=0:raise AssertionError((name,z))
 checks.append({'name':name,'passed':True})
P=x*(b-2*y)+d*x**3*y/6
W1=2*x-s.diff(P,y);W2=2*y+s.diff(P,x);O=-s.diff(P,x,2)-s.diff(P,y,2);J=s.diff(W2,x)
Q=-s.diff(b,y,2)-d*y;A=(5-s.diff(b,y))*Q+b*s.diff(Q,y);C=d*(-Q/6+y*s.diff(Q,y)/2)
check('W1',W1-((4-s.diff(b,y))*x-d*x**3/6));check('W2',W2-b-d*x*x*y/2);check('Omega',O-x*Q);check('J',J-d*x*y)
check('divW',s.diff(W1,x)+s.diff(W2,y)-4)
F=s.expand(W1*s.diff(O,x)+W2*s.diff(O,y)+O);T=x*x*A/2+x**4*C/4
check('forcing decomposition',F-x*A-x**3*C);check('primitive Tx',s.diff(T,x)-F)
t=s.expand(W1*s.diff(T,x)+W2*s.diff(T,y))
tn=[s.S(0),(4-s.diff(b,y))*A+b*s.diff(A,y)/2,(4-s.diff(b,y))*C-d*A/6+b*s.diff(C,y)/4+d*y*s.diff(A,y)/4,-d*C/6+d*y*s.diff(C,y)/8,s.S(0)]
check('thermal polynomial',t-sum(x**(2*i)*tn[i]for i in range(1,4)))
vals={b.subs(y,0):0,s.diff(b,y).subs(y,0):4,s.diff(b,y,2).subs(y,0):-q}
for i,v in [(1,0),(2,-d*q/6),(3,d*d*q/36)]:check('center t'+str(i),tn[i].subs(y,0).subs(vals)-v)
E=s.expand(J*J*s.diff(t,y)-J*W2*s.diff(t,x,y)+(W2*s.diff(J,y)-J*s.diff(W2,y))*s.diff(t,x))
check('compatibility reduction',E/d-(x*(b-y*s.diff(b,y))*s.diff(t,x)-x*y*b*s.diff(t,x,y)+d*x*x*y*y*s.diff(t,y)-d*x**3*y*y*s.diff(t,x,y)/2))
coef=s.Poly(E/d,x)
for i in range(1,5):check('coefficient recurrence n='+str(i),coef.coeff_monomial(x**(2*i))-(-2*i*y*b*s.diff(tn[i],y)+2*i*(b-y*s.diff(b,y))*tn[i]+d*(2-i)*y*y*s.diff(tn[i-1],y)))
B=s.Function('B')(y);candidate=y/b
check('t2 ODE solution',-y*b*s.diff(candidate,y)+(b-y*s.diff(b,y))*candidate)
u,v,w=s.symbols('u v w',real=True);bp=4*y-q*y*y/2+u*y**3+v*y**4+w*y**5
check('y/b linear expansion',s.series(y/bp,y,0,2).removeO()-(s.Rational(1,4)+q*y/32))
check('b-yb prime limit',s.limit((bp-y*s.diff(bp,y))/y**2,y,0)-q/2)
check('forced t2 derivative',(-2*d*q/3)*(q/32)+d*q*q/48)
check('positive contradiction',3*q*(d*d*q/36)-d*(-d*q*q/48)-s.Rational(5,48)*d*d*q*q)
# Polynomial realizations directly evaluate the undivided compatibility formula.
trials=[]
for qq,dd,uu,vv in [(1,1,0,0),(2,-3,4,-1),(-5,2,s.Rational(7,3),8),(s.Rational(1,7),s.Rational(-2,5),0,3)]:
 pp=x*(2*y-qq*y*y/2+uu*y**3+vv*y**4)+dd*x**3*y/6
 ww1=2*x-s.diff(pp,y);ww2=2*y+s.diff(pp,x);oo=-s.diff(pp,x,2)-s.diff(pp,y,2)
 ff=s.expand(ww1*s.diff(oo,x)+ww2*s.diff(oo,y)+oo);tt=s.integrate(ff,(x,0,x));tr=s.expand(ww1*s.diff(tt,x)+ww2*s.diff(tt,y));jj=s.diff(ww2,x)
 ee=s.Poly(s.expand(jj*jj*s.diff(tr,y)-jj*ww2*s.diff(tr,x,y)+(ww2*s.diff(jj,y)-jj*s.diff(ww2,y))*s.diff(tr,x)),x,y)
 assert not ee.is_zero
 first=min(sum(k)for k,vv1 in ee.terms() if vv1!=0);trials.append({'q':str(qq),'d':str(dd),'b3':str(uu),'b4':str(vv),'first_nonzero_total_degree':first,'nonzero_coefficient_count':len(ee.terms())})
result={'utc':datetime.now(timezone.utc).isoformat(),'elapsed_seconds':time.monotonic()-start,'exact_count':len(checks),'checks':checks,'polynomial_trials':trials,'scope':'Exact algebra and four controls. The proof covers arbitrary smooth b with the stated center jet; finite polynomial tests are not a replacement for its ODE argument.'}
(root/'tests.json').write_text(json.dumps(result,indent=2)+'\n');print(json.dumps(result,indent=2),flush=True)
