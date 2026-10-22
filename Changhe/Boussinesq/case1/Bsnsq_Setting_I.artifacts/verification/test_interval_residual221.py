from pathlib import Path
from fractions import Fraction as F
from math import factorial
from datetime import datetime,timezone
import hashlib,json,sys,os
for k in ['OMP_NUM_THREADS','OPENBLAS_NUM_THREADS','MKL_NUM_THREADS']:os.environ[k]='1'
import sympy as sp
from interval_residual221 import Jet,I,B,P,cheb_basis,cheb_derivative_bound,physical,Field
if sys.flags.optimize:raise RuntimeError('optimized checks prohibited')
checks=[]
def ck(label,b):
 if not b:raise RuntimeError(label)
 checks.append(label)
def R(x):return F(int(sp.numer(x)),int(sp.denom(x)))
x,h,z=sp.symbols('x h z');poly=(1+x+2*h+x*h)**4
X,H=Jet.var(F(1,3),0),Jet.var(F(2,7),1);j=(1+X+2*H+X*H)**4
for i,k in j.c:ck('polynomial '+str((i,k)),j.c[i,k].contains(R(sp.diff(poly,x,i,h,k).subs({x:sp.Rational(1,3),h:sp.Rational(2,7)}))/F(factorial(i)*factorial(k))))
rat=1/(2+x+h+x*h);jr=1/(2+X+H+X*H)
for i,k in jr.c:ck('reciprocal '+str((i,k)),jr.c[i,k].contains(R(sp.diff(rat,x,i,h,k).subs({x:sp.Rational(1,3),h:sp.Rational(2,7)}))/F(factorial(i)*factorial(k))))
for n in range(1,19):
 t=sp.chebyshevt(n,z)
 for k in range(1,6):ck('Cheb exact endpoint '+str((n,k)),cheb_derivative_bound(n,k)==R(sp.diff(t,z,k).subs(z,1)))
# Two interval bases, checked at three exact rational points in each interval.
for mid in [F(-1,3),F(2,5)]:
 width=F(1,2**60);c=I(I.of(mid-width).lo,I.of(mid+width).hi);jb=Jet.var(c,0);basis=cheb_basis(jb,97)
 for n in [0,1,2,7,18,64,96]:
  t=sp.chebyshevt(n,z)
  for k in range(5):
   d=sp.diff(t,z,k)/factorial(k)
   for off in [-width,F(0),width]:ck('Cheb interval '+str((mid,n,k,off)),basis[n].c[k,0].contains(R(d.subs(z,sp.Rational(mid+off)))))
# Independent physical derivatives of the stream function, without W-derived U.
G=x*h*(1+x*x/7+h*h/11);a=600;A=sp.diff(G,x,h);C=sp.diff(G,x,2);Y=sp.diff(G,x);S=3*x*Y+h*sp.diff(G,h)-6*G
Dx=lambda f:sp.diff(f,x)-C/A*sp.diff(f,h);Dy=lambda f:sp.diff(f,h)/A
U1=-Dy(S);U2=Dx(S);om=-Dx(Dx(S))-Dy(Dy(S));ox=Dx(om);oy=Dy(om);tx=-a*C/A;ty=a/A
expr=dict(A=A,C=C,y=Y,U1=U1,U2=U2,Omega=om,Omega_x=ox,Omega_y=oy,Theta=a*h,Theta_x=tx,Theta_y=ty)
for xx,hh in [(F(1,5),F(2,5)),(F(3,7),F(4,9)),(F(2),F(1,3))]:
 X,H=Jet.var(xx,0),Jet.var(hh,1);gg=X*H*(1+X*X/7+H*H/11);f=physical(gg,X,H,a);subst={x:sp.Rational(xx),h:sp.Rational(hh)}
 for key,v in expr.items():ck('physical '+str((xx,hh,key)),f[key].contains(R(v.subs(subst))))
 exact={k:R(v.subs(subst))for k,v in expr.items()};w1=3*xx+exact['U1'];w2=3*exact['y']+exact['U2'];res=w1*exact['Omega_x']+w2*exact['Omega_y']+exact['Omega']-exact['Theta_x'];nn=abs(w1*exact['Omega_x'])+abs(w2*exact['Omega_y'])+abs(exact['Omega'])+abs(exact['Theta_x']);n2=abs(exact['U1']*exact['Omega_x'])+abs(exact['U2']*exact['Omega_y'])+abs(3*(xx*exact['Omega_x']+exact['y']*exact['Omega_y'])+exact['Omega'])+abs(exact['Theta_x'])
 for k,v in [('R',res),('N',nn),('N2',n2),('D',res/(xx*exact['y'])),('prompt_ratio',abs(res)/nn),('grouped_ratio',abs(res)/n2),('R_Theta',0)]:ck('residual '+str((xx,hh,k)),f[k].contains(v))
# Refusal tests preserve domains rather than falsely extending the formula.
for label,fn in [('Cheb domain',lambda:cheb_basis(Jet.var(F(11,10),0),4)),('negative sixth',lambda:Jet.const(-1).inv_sixth()),('zero reciprocal',lambda:Jet.const(I(-1,1)).reciprocal())]:
 try:fn()
 except (ValueError,ArithmeticError):ck(label,True)
 else:ck(label,False)
now=datetime.now(timezone.utc).isoformat();paths=[Path(__file__),'code/interval_residual221.py','code/dyadic_root220.py','research/interval_residual221/PROOF.md'];out={'utc':now,'status':'PASS_EXACT_MANUFACTURED_TAYLOR_AND_PHYSICAL_CHECKS','check_count':len(checks),'checks':checks,'scope':'Exact rational symbolic oracles and finite interval tests. Candidate fields not evaluated.','hashes':{str(Path(p).resolve()):hashlib.sha256(Path(p).read_bytes()).hexdigest()for p in paths}};Path('research/interval_residual221/verification/machinery.json').write_text(json.dumps(out,indent=2)+'\n');print(now,out['status'],len(checks))
