"""Exact independent polynomial/Gaussian check of the potential energy matrix."""
from fractions import Fraction as F
from math import prod
from datetime import datetime,timezone
from pathlib import Path
import json

def add(*ps):
 out={}
 for p in ps:
  for k,v in p.items():out[k]=out.get(k,F(0))+v
 return {k:v for k,v in out.items() if v}
def scale(p,c):return {k:v*c for k,v in p.items() if v*c}
def mul(p,q):
 out={}
 for (i,j),v in p.items():
  for (a,b),w in q.items():out[i+a,j+b]=out.get((i+a,j+b),F(0))+v*w
 return {k:v for k,v in out.items() if v}
def deriv(p,axis):
 out={}
 for k,v in p.items():
  if k[axis]:
   n=list(k);n[axis]-=1;out[tuple(n)]=v*k[axis]
 return out
x={(1,0):F(1)};y={(0,1):F(1)};one={(0,0):F(1)}
def gd(p,axis):return add(deriv(p,axis),scale(mul(p,[x,y][axis]),-2))
def gm(p):
 return sum(v*F(prod(range(1,i,2)),4**(i//2))*F(prod(range(1,j,2)),4**(j//2)) for (i,j),v in p.items() if i%2==j%2==0)
P={(0,1):F(1),(2,1):F(1,5),(0,3):F(-3,10)}
px=gd(P,0);py=gd(P,1);h=scale(add(gd(px,0),gd(py,1)),-1);hx=gd(h,0);hy=gd(h,1)
uh1=scale(gd(px,1),-1);uh2=gd(px,0)
checks=[]
for cl,a0,b,e,q1 in [(F(3),F(20),F(-2),F(3),F(1)),(F(3,2),F(7,2),F(1,3),F(-2,5),F(1,7)),(F(2),F(-8),F(2),F(1),F(-1))]:
 c=1-cl;q2=-b/3-q1
 rho={(0,1):a0,(2,1):b,(0,3):e};psi={(1,1):c,(3,1):q1,(1,3):q2}
 u1=scale(deriv(psi,1),-1);u2=deriv(psi,0);v1=add(scale(x,cl),u1);v2=add(scale(y,cl),u2)
 rhox=deriv(rho,0);rhoy=deriv(rho,1)
 Lh=add(mul(v1,hx),mul(v2,hy),scale(h,-1),mul(uh1,rhox),mul(uh2,rhoy))
 direct=-gm(mul(Lh,P))
 m11=add(scale(one,1+2*cl),deriv(u1,0),rhoy)
 m22=add(scale(one,1+2*cl),deriv(u2,1))
 cross=add(deriv(u1,1),deriv(u2,0),scale(rhox,-1))
 energy=gm(add(mul(m11,mul(px,px)),mul(cross,mul(px,py)),mul(m22,mul(py,py))))
 assert direct==energy
 assert m11.get((0,0),0)==3*cl+a0 and m22.get((0,0),0)==cl+2
 assert direct!=energy-cl*gm(add(mul(px,px),mul(py,py)))
 checks.append({'cl':str(cl),'a0':str(a0),'b':str(b),'e':str(e),'q1':str(q1),'q2':str(q2),'integral_over_pi_half':str(direct),'energy_equal':True,'center_matrix':[str(3*cl+a0),str(cl+2)],'wrong_dilation_coefficient_fails':True})
p=Path('research/phi_energy/verification/exact_gaussian_tests.json')
p.write_text(json.dumps({'utc':datetime.now(timezone.utc).isoformat(),'method':'Exact Fraction polynomial differentiation, Gaussian factors and moment integration; polynomial backgrounds need not satisfy transport','checks':checks},indent=2)+'\n')
print(len(checks),'exact Phi energy examples passed')
