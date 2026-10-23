"""Independent rational power polynomials and implicit Cartesian reference."""
from fractions import Fraction as F
import mpmath as mp

def add(a,b):
 c=[F(0)]*max(len(a),len(b))
 for i,v in enumerate(a):c[i]+=v
 for i,v in enumerate(b):c[i]+=v
 while len(c)>1 and not c[-1]:c.pop()
 return c

def mul(a,b):
 c=[F(0)]*(len(a)+len(b)-1)
 for i,x in enumerate(a):
  for j,y in enumerate(b):c[i+j]+=x*y
 return c

def power_polynomial(coeff,alpha=F(1),beta=F(0)):
 old=[F(1)];cur=[beta,alpha];out=[F(0)];rows=[old]
 if len(coeff)>1:rows.append(cur)
 for j in range(1,len(coeff)-1):
  nxt=add([2*z for z in mul([beta,alpha],cur)],[-z for z in old]);old,cur=cur,nxt;rows.append(cur)
 for c,row in zip(coeff,rows):out=add(out,[F(c)*v for v in row])
 return out

def global_polynomials(data):
 rows=[]
 for k,row in enumerate(data['coefficients']):
  t=F(data['tk'][k]);rows.append(power_polynomial([F(z)for z in row],2/(1-t),-(1+t)/(1-t)))
 return rows

def reference(polynomials,x,y,dps=90):
 with mp.workdps(dps):
  x,y=mp.mpf(float(x)),mp.mpf(float(y));s=x*x+y*y;lo=mp.mpf(0);hi=mp.mpf(1)
  for unused in range(mp.mp.prec+24):
   w=(lo+hi)/2
   if 16*s*w**4+w-1>0:hi=w
   else:lo=w
  w=(lo+hi)/2 if s else mp.mpf(1);D=1+64*s*w**3;ws=-16*w**4/D;wss=-(128*w**3*ws+192*s*w*w*ws*ws)/D
  pp=[[mp.mpf(z.numerator)/z.denominator for z in row]for row in polynomials]
  def G(a,b,c):
   t=1-2*c;H=[mp.mpf(1),a*a-b*b,a**4-6*a*a*b*b+b**4];z=mp.mpf(0)
   for k,row in enumerate(pp):z+=(16*c**4)**k*H[k]*mp.polyval(row[::-1],t)
   return b*c*z
  args=(x,y,w);gw=mp.diff(G,args,(0,0,1));gx=mp.diff(G,args,(1,0,0))+2*x*ws*gw;gy=mp.diff(G,args,(0,1,0))+2*y*ws*gw
  gxx=mp.diff(G,args,(2,0,0))+4*x*ws*mp.diff(G,args,(1,0,1))+4*x*x*ws*ws*mp.diff(G,args,(0,0,2))+(2*ws+4*x*x*wss)*gw
  a=[G(*args),gx,gy,gxx];return dict(values=[float(z)for z in a],working_precision_decimal=[mp.nstr(z,dps-10)for z in a])

def slowjet(x,y):
 import numpy as np
 x,y=np.broadcast_arrays(np.asarray(x,float),np.asarray(y,float));a=1+x*x+y*y
 return np.stack([y*a**(-.25),-.5*x*y*a**(-1.25),a**(-.25)-.5*y*y*a**(-1.25),-.5*y*a**(-1.25)+1.25*x*x*y*a**(-2.25)],axis=-1)

def slow_reference(x,y,r,dps):
 with mp.workdps(dps):
  x,y,r=map(mp.mpf,[x,y,r]);a=1+x*x;A=a+y*y;B=a+r*r
  I=lambda q:y*a**(-q)*mp.hyp2f1(mp.mpf('.5'),q,mp.mpf('1.5'),-y*y/a)
  i=I(mp.mpf('.25'));j=I(mp.mpf('1.25'));z=dict(V=[x*A**(-mp.mpf('.25')),-i+x*x*j/2],Phi=-x*i,dV2_dy=-A**(-mp.mpf('.25'))+x*x*A**(-mp.mpf('1.25'))/2,tail_V=[x*B**(-mp.mpf('.25')),y*(-B**(-mp.mpf('.25'))+x*x*B**(-mp.mpf('1.25'))/2)])
  return {k:[float(a)for a in v]if isinstance(v,list)else float(v)for k,v in z.items()}
