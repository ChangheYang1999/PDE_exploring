"""Ball Hessian on a rectangle for the exact ideal-node binary interpolant.
This module encloses only the local PV hole; it does not certify the inverse.
"""
from pathlib import Path
from datetime import datetime,timezone
from fractions import Fraction
import math,json,hashlib,time,sys
import numpy as np
from flint import arb,arb_mat,ctx
MODULE_ROOT=Path(__file__).resolve().parents[1]
sys.path.insert(0,str(MODULE_ROOT.parent/"exact-data/code"))
from nodal_input import export as export_nodal,load as load_nodal

def binary(x):
 p,q=float(x).as_integer_ratio();return arb(p)/q

def ceil_abs(x):
 return int(x.abs_upper().ceil().unique_fmpz())

def dcheb(a):
 n=len(a)-1
 if n<1:return [arb(0)]
 d=[arb(0) for _ in range(n)]
 d[-1]=2*n*a[-1]
 if n>=2:d[-2]=2*(n-1)*a[-2]
 for j in range(n-3,-1,-1):d[j]=d[j+2]+2*(j+1)*a[j+1]
 d[0]/=2
 return d

def diffco(co,axis):
 if axis==1:return [dcheb(row) for row in co]
 return list(map(list,zip(*[dcheb(list(col)) for col in zip(*co)])))

def clenshaw(a,z):
 p=arb(0);q=arb(0)
 for c in a[:0:-1]:p,q=c+2*z*p-q,p
 return a[0]+z*p-q

def cosbasis(z,n):
 assert z>-1 and z<1, 'interval polynomial evaluation requires interior coordinates'
 t=z.acos();return [(t*j).cos() for j in range(n)]

def values(coefficients,z,c):
 # Summing enclosed cosine values avoids the exponential interval wrapping of
 # Clenshaw near +/-1. No floating value is used to contract an interval.
 tz=cosbasis(z,max(len(co) for co in coefficients));tc=cosbasis(c,max(len(co[0]) for co in coefficients))
 result=[]
 for co in coefficients:
  inner=[sum((v*tc[j] for j,v in enumerate(row)),arb(0)) for row in co]
  result.append(sum((a*b for a,b in zip(tz,inner)),arb(0)))
 return result

def value(co,z,c):return values([co],z,c)[0]

def tensor_coefficients(b):
 N=b.shape[0]-1;M=b.shape[1];pi=arb.pi()
 def wt(j):return arb(1)/2 if j in (0,N) else arb(1)
 R=arb_mat([[(2*wt(n)*wt(j)/N)*(pi*n*j/N).cos() for j in range(N+1)] for n in range(N+1)])
 A=arb_mat([[((arb(1) if m==0 else arb(2))/M)*(pi*m*(2*a+1)/(2*M)).cos() for m in range(M)] for a in range(M)])
 B=arb_mat([[binary(x) for x in row] for row in b[::-1]])
 C=R*B*A
 return [[C[n,m] for m in range(M)] for n in range(N+1)]

class EnclosedDensity:
 def __init__(self,filename=None,*,co=None,L=8,cl=6,beta=.9):
  if filename is not None:
   source=Path(filename).resolve()
   if source.suffix=='.json':
    exact_json=source;o,b,params,jhash=load_nodal(exact_json);source=Path(o['source'])
   else:
    exact_json=MODULE_ROOT/'data'/(source.stem+'.json');exact_json.parent.mkdir(parents=True,exist_ok=True)
    if not exact_json.exists():export_nodal(source,exact_json)
    o,b,params,jhash=load_nodal(exact_json)
    assert hashlib.sha256(source.read_bytes()).hexdigest()==o['source_sha256']
   self.source=str(source);self.md5=hashlib.md5(source.read_bytes()).hexdigest()
   self.input_json=str(exact_json);self.input_json_sha256=jhash;self.source_sha256=o['source_sha256']
   self.N=o['N'];self.M=o['M'];co=tensor_coefficients(b);L=params['L'];cl=params['c_l'];beta=params['beta']
  else:self.source='manufactured';self.md5=None;self.N=len(co)-1;self.M=len(co[0])
  self.L=binary(L);self.cl=binary(cl);self.k=1/self.cl;self.beta=binary(beta);self.beta_float=float(beta)
  assert self.L>0 and self.cl>1 and abs(self.beta)<1
  self.co=co;cz=diffco(co,0);cc=diffco(co,1);self.derivatives=[co,cz,cc,diffco(cz,0),diffco(cz,1),diffco(cc,1)]

 def hessian(self,point,epsilon=Fraction(1,10**7)):
  eps=arb(epsilon.numerator)/epsilon.denominator;x=binary(point[0])+arb(0,eps);y=binary(point[1])+arb(0,eps);assert x>0 and y>0
  theta=(y/x).atan();tm=math.atan2(point[1],point[0]);lo=0.;hi=math.pi/2
  for _ in range(60):
   sm=(lo+hi)/2
   if sm+self.beta_float*math.sin(2*sm)/2<tm:lo=sm
   else:hi=sm
  s0=binary((lo+hi)/2);res=s0+self.beta*(2*s0).sin()/2-theta;rad=res.abs_upper()/(1-abs(self.beta));s=s0+arb(0,rad)
  r2=x*x+y*y;D=self.L*self.L+r2;ell=(1+r2/(self.L*self.L)).log();omq=(-(1-self.k)*ell/2).exp();q=1-omq;z=2*q-1;c=(2*s).cos();ss=(2*s).sin();den=1+self.beta*c;assert den>0
  ct=-2*ss/den;ctt=-4*c/(den*den)-4*self.beta*ss*ss/(den**3)
  tx=-y/r2;ty=x/r2;t2=[[2*x*y/(r2*r2),(y*y-x*x)/(r2*r2)],[(y*y-x*x)/(r2*r2),-2*x*y/(r2*r2)]];tg=[tx,ty];X=[x,y]
  zi=[2*(1-self.k)*omq*xx/D for xx in X];ci=[ct*t for t in tg]
  zij=[[2*(1-self.k)*omq*((1 if i==j else 0)/D-(3-self.k)*X[i]*X[j]/(D*D)) for j in range(2)] for i in range(2)]
  cij=[[ctt*tg[i]*tg[j]+ct*t2[i][j] for j in range(2)] for i in range(2)]
  b,bz,bc,bzz,bzc,bcc=values(self.derivatives,z,c)
  bi=[bz*zi[i]+bc*ci[i] for i in range(2)]
  bij=[[bzz*zi[i]*zi[j]+bzc*(zi[i]*ci[j]+ci[i]*zi[j])+bcc*ci[i]*ci[j]+bz*zij[i][j]+bc*cij[i][j] for j in range(2)] for i in range(2)]
  pref=x*x*y*((self.k-3)*ell/2).exp();ti=[2/x+(self.k-3)*x/D,1/y+(self.k-3)*y/D]
  tij=[[(self.k-3)*((1 if i==j else 0)/D-2*X[i]*X[j]/(D*D))-(2/(x*x) if i==j==0 else 1/(y*y) if i==j==1 else 0) for j in range(2)] for i in range(2)]
  H=[[pref*((ti[i]*ti[j]+tij[i][j])*b+ti[i]*bi[j]+ti[j]*bi[i]+bij[i][j]) for j in range(2)] for i in range(2)]
  bound=sum(ceil_abs(v) for row in H for v in row);error=Fraction(bound)*epsilon**2/4
  return {'point':point,'epsilon_exact':str(epsilon),'Hessian_balls':[[v.str(25) for v in row] for row in H],'Hessian_operator_bound_integer':bound,'local_hole_U_bound_exact':str(error),'local_hole_U_bound_float':float(error),'angle_inverse_radius':rad.str(25)},H

def test():
 ctx.prec=192
 # Exact Chebyshev derivative identities T0'=0,T1'=1,T2'=4z,T3'=12z²-3.
 expected=[[0],[1],[0,4],[3,0,6]]
 for n,e in enumerate(expected):
  a=[arb(0)]*(n+1);a[-1]=arb(1);d=dcheb(a);assert len(d)==len(e) and all(x==y for x,y in zip(d,e))
 # A single high-order term: direct cosine encloses exactly the mathematical
 # polynomial on the interval, while the naive interval Clenshaw wraps badly.
 z=arb('-.9995','1e-8');a=[arb(0)]*121;a[-1]=arb(1)/10**8
 stable=value([[v] for v in a],z,arb(0));assert stable.abs_upper()<arb('1.1e-8')
 for zz in ['-.99950001','-.9995','-.99949999']:
  assert (stable-(arb(zz).acos()*120).cos()/10**8).contains(0)
 # Constant nodal data must reconstruct the constant exactly inside the balls.
 co=tensor_coefficients(np.ones((9,4)))
 assert co[0][0].contains(1)
 assert all(co[i][j].contains(0) for i in range(9) for j in range(4) if i or j)
 # A mixed ideal-node polynomial has exact binary samples: T1(z)*T2(c).
 mixed=np.array([[-.5,1.,-.5],[0.,0.,0.],[.5,-1.,.5]])
 cm=tensor_coefficients(mixed)
 assert all(cm[i][j].contains(1 if i==1 and j==2 else 0) for i in range(3) for j in range(3))
 # Independent closed radial-factor differentiation at a point, no finite differences.
 obj=EnclosedDensity(co=[[arb(1)]],L=2,cl=6,beta=.9);row,H=obj.hessian([1.,.5],Fraction(0))
 x=arb(1);y=arb(1)/2;S=1+(x*x+y*y)/4;p=(arb(1)/6-3)/2
 w=S**p;wx=p*S**(p-1)*x/2;wy=p*S**(p-1)*y/2
 wxx=p*S**(p-1)/2+p*(p-1)*S**(p-2)*x*x/4;wxy=p*(p-1)*S**(p-2)*x*y/4;wyy=p*S**(p-1)/2+p*(p-1)*S**(p-2)*y*y/4
 exact=[[2*y*w+4*x*y*wx+x*x*y*wxx,2*x*w+2*x*y*wy+x*x*wx+x*x*y*wxy],[2*x*w+2*x*y*wy+x*x*wx+x*x*y*wxy,2*x*x*wy+x*x*y*wyy]]
 assert all((H[i][j]-exact[i][j]).contains(0) for i in range(2) for j in range(2))
 # Polynomial b=z*c exercises both mixed coordinate derivatives. Independent SymPy chain rule on beta=0.
 import sympy as sp
 X,Y=sp.symbols('X Y',positive=True);rad2=X*X+Y*Y;q=1-(1+rad2/4)**(-sp.Rational(5,12));c=(X*X-Y*Y)/rad2;rho=X*X*Y*(1+rad2/4)**(-sp.Rational(17,12))*(2*q-1)*c
 obj=EnclosedDensity(co=[[arb(0),arb(0)],[arb(0),arb(1)]],L=2,cl=6,beta=0);_,H=obj.hessian([1.,.5],Fraction(0))
 for i,u in enumerate([X,Y]):
  for j,v in enumerate([X,Y]):
   val=sp.diff(rho,u,v).subs({X:1,Y:sp.Rational(1,2)}).evalf(60)
   # Decimal comparison is a diagnostic in addition to the exact constant-field overlap above.
   assert abs(float(H[i][j])-float(val))<1e-13
 print('MANUFACTURED_HESSIAN_CHECKS_PASS')

if __name__=='__main__':
 import sys
 if '--test' in sys.argv:test()
 else:
  ctx.prec=192;d=EnclosedDensity(sys.argv[1]);row,H=d.hessian([float(sys.argv[2]),float(sys.argv[3])]);row.update(date=datetime.now(timezone.utc).isoformat(),source=d.source,md5=d.md5,precision_bits=ctx.prec)
  print(json.dumps(row,indent=2))
