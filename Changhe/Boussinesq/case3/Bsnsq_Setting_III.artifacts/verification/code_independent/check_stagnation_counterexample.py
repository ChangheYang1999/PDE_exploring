from pathlib import Path
from datetime import datetime,timezone
import time,json
import sympy as S
import numpy as np
from numpy.polynomial.legendre import leggauss
start=time.monotonic();root=Path('research/194_stagnation_grid_audit/verification');exact=[]
x,y,a,b,beta,d,rho=S.symbols('x y a b beta d rho',real=True)
P=-beta*b*(x-a)+beta*a*(y-b)+(beta+d)*(x-a)*(y-b)
chi=(1-((x-a)**2+(y-b)**2)/rho**2)**6;f=chi*P;U=S.Matrix([-S.diff(f,y),S.diff(f,x)]);W=beta*S.Matrix([x,y])+U;Om=-S.diff(f,x,2)-S.diff(f,y,2)
def ck(label,e):
 v=S.simplify(e);assert v==0,(label,v);exact.append(label)
ck('local divergence',S.diff(W[0],x)+S.diff(W[1],y)-2*beta)
for i in range(2):ck('zero component'+str(i),W[i].subs({x:a,y:b}))
for i in range(2):
 for j,z in enumerate([x,y]):ck('saddle derivative'+str((i,j)),S.diff(W[i],z).subs({x:a,y:b})-S.diag(-d,2*beta+d)[i,j])
ck('Poisson',-S.diff(f,x,2)-S.diff(f,y,2)-Om)
ck('curl sign',S.diff(U[1],x)-S.diff(U[0],y)+Om)
# Trace-zero derivative corrections are exactly Hamiltonian Hessians.
A,B,C=S.symbols('A B C');N=S.Matrix([[A,B],[C,-A]]);J=S.Matrix([[0,-1],[1,0]]);H=-J*N
for i in range(2):
 for j in range(2):ck('Hessian symmetric'+str((i,j)),H[i,j]-H[j,i]);ck('Hessian velocity'+str((i,j)),(J*H-N)[i,j])
for bb,dd in [(S.Rational(1,2),S.Rational(1,3)),(2,1),(3,2),(S.Rational(77,25),S.Rational(1,10))]:
 for aa,yy in [(1,2),(S.Rational(2,3),-1),(2,0)]:
  ww=W.subs({beta:bb,d:dd,a:aa,b:yy,x:aa,y:yy},simultaneous=True)
  for i in range(2):ck('rational saddle'+str((bb,dd,aa,yy,i)),ww[i])
# Direct physical full-plane Biot-Savart integral of the two compact sources.
pars={a:S.Integer(1),b:S.Integer(2),beta:S.Integer(3),d:S.Integer(1),rho:S.Rational(1,4)}
om=S.lambdify((x,y),Om.subs(pars),'numpy');fv=S.lambdify((x,y),U.subs(pars),'numpy')
physical=[]
for nr,na in [(20,96),(32,160),(48,256)]:
 g,w=leggauss(nr);rr=(g+1)/8;wr=w/8;ang=(np.arange(na)+.371)*2*np.pi/na;xx=1+rr[:,None]*np.cos(ang);yy=2+rr[:,None]*np.sin(ang);weight=wr[:,None]*rr[:,None]*2*np.pi/na;dens=om(xx,yy)
 points=[(1.,2.),(-1.,2.),(0.,0.),(3.,4.),(.3,-1.)]
 for target in points:
  X,Y=target;ux=uy=0.
  for sourcex,sgn in [(xx,1.),(-xx,-1.)]:
   dx=X-sourcex;dy=Y-yy;dist=dx*dx+dy*dy;ux+=float(np.sum(weight*sgn*dens*dy/dist)/(2*np.pi));uy-=float(np.sum(weight*sgn*dens*dx/dist)/(2*np.pi))
  want=np.array([-3.,-6.]) if target==(1.,2.) else (np.array([3.,-6.]) if target==(-1.,2.) else np.zeros(2))
  got=np.array([ux,uy]);err=float(np.max(abs(got-want)));assert err<2e-10,(nr,na,target,got,want,err);physical.append({'radial_nodes':nr,'angles':na,'target':target,'computed_U':got.tolist(),'expected_U':want.tolist(),'max_error':err})
wrong=[]
# Algebraic counter-comparisons, not executed code mutations.
for q in [S.Rational(1,3),2,3]:
 Wwrong=S.Matrix([q,2*q])+S.Matrix([q,2*q]);assert Wwrong!=S.zeros(2,1);wrong.append(str(q))
out={'status':'PASS','utc':datetime.now(timezone.utc).isoformat(),'exact_checks':len(exact),'physical_kernel_checks':len(physical),'algebraic_wrong_sign_comparisons':len(wrong),'physical':physical,'max_physical_error':max(x['max_error']for x in physical),'elapsed_seconds':time.monotonic()-start,'scope':'Exact local saddle/divergence/curl identities and tracezero-Hamiltonian correspondence. C5compact polynomial bump physical source, ordinary full-plane kernel, three independent radial/angular orders. Proof uses C-infinity cutoff. Wrong-sign comparisons algebraic only.'};(root/'controls.json').write_text(json.dumps(out,indent=2)+'\n');print(json.dumps(out,indent=2))
