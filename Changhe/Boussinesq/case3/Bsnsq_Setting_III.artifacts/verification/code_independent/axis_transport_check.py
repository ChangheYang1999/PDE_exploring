"""Independent scalar-quadrature axis check against two-pass characteristics.
No numerics-lane code, modal inverse, or spline characteristic field is used.
"""
from pathlib import Path
from datetime import datetime,timezone
import hashlib,json,math,time
import numpy as np
import mpmath as mp
from scipy.integrate import quad
from gaussian_characteristics import GaussianFlow

class AxisQuadrature:
 def __init__(self,c=2.5,y0=2.85,s=1.,sign=1):
  self.c,self.y0,self.s,self.sign=c,y0,s,sign;self.beta=2*(c-1);self.mu=1+1.5*self.beta
  self.qH=(self.beta+1)/self.mu;self.gamma=(2*self.beta+1)/self.mu
  mp.mp.dps=55
  cm,ym,sm=mp.mpf(str(c)),mp.mpf(str(y0)),mp.mpf(str(s));am=1/(2*sm**2)
  def B(S):return -mp.expm1(-am*S)/S if S else am
  bp=mp.diff(B,ym**2)
  self.fac_mp=cm/(-2*ym*bp);self.u0_mp=self.fac_mp*B(ym**2)
  self.fac=float(self.fac_mp);self.u0=float(self.u0_mp)
  def wm(y):return self.beta*y+self.fac_mp*(B((y-ym)**2)-B(ym**2))
  # Factor w(y)=y*d(y) in high precision before reciprocal subtraction.
  cs=mp.taylor(lambda yy:self.sign*wm(self.sign*yy),mp.mpf(0),14)
  self.dcoeff=np.array([float(v) for v in cs[1:]])
  self.dcoeff[0]=self.mu
  self.series_radius=.035
  self.cache={0.:(0.,0.)}
 def w_over_y(self,y):
  if y<self.series_radius:return float(np.polynomial.polynomial.polyval(y,self.dcoeff))
  yy=self.sign*y;z=yy-self.y0;S=z*z;aa=1/(2*self.s*self.s)
  Q=self.fac*(-math.expm1(-aa*S)/S if S else aa)
  return (self.beta*yy+Q-self.u0)*self.sign/y
 def reciprocal_regular(self,y):
  d=self.w_over_y(y)
  if y<self.series_radius:
   change=np.polynomial.polynomial.polyval(y,self.dcoeff[1:])
   return -change/(self.mu*d)
  return (1/d-1/self.mu)/y
 def S(self,y,tol=2e-11):
  key=(float(y),tol)
  if key not in self.cache:
   v,e=quad(self.reciprocal_regular,0.,float(y),epsabs=tol,epsrel=tol,limit=160,points=[self.series_radius] if y>self.series_radius else None)
   self.cache[key]=(v,e)
  return self.cache[key]
 def values(self,y,tol=2e-10):
  if y==0:return {'F':1.,'G':4/self.beta,'S':0.,'quadrature_errors':[0.,0.]}
  S,e=self.S(y,tol/10);d=self.w_over_y(y);F=(d/self.mu)**2*math.exp(-2*self.mu*S)
  def integrand(u):return math.exp(-(self.beta+1)*self.S(y*u**(1/(1-self.qH)),tol/10)[0])
  I,err=quad(integrand,0.,1.,epsabs=tol,epsrel=tol,limit=100)
  G=2/(self.mu**2*(1-self.qH))*d*math.exp(-(2*self.beta+1)*S)*I
  return {'F':F,'G':G,'S':S,'quadrature_errors':[e,err]}

def main():
 start=time.monotonic();dest=Path('verification/gaussian_axis_check.json')
 out={'started_utc':datetime.now(timezone.utc).isoformat(),'scope':'Forced Gaussian axis and off-axis limits; not a B2 profile','source_sha256':hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),'runs':[]}
 def save():dest.write_text(json.dumps(out,indent=2)+'\n')
 for c in (2.5,2.25):
  flow=GaussianFlow(c=c)
  for sign in (-1,1):
   model=AxisQuadrature(c=c,sign=sign)
   for radius in (.3,1.,3.,10.):
    row={'c':c,'beta':flow.beta,'y':sign*radius,'axis':model.values(radius),'refined':model.values(radius,tol=2e-12),'off_axis':[]}
    for x in (.03,.01,.003):
     r=flow.evaluate([x,sign*radius],r_in=1e-5,rtol=5e-11)
     p={'x':x,'status':r['status'],'T':r.get('T')}
     if r['status']=='COMPLETE':p.update(F=r['Theta']/x**2,G=r['Omega']/x)
     row['off_axis'].append(p)
    # Independent differences in the one-dimensional equations.
    for h in (2e-3,1e-3):
     vals=[model.values(radius+j*h) for j in (-2,-1,1,2)]
     df=(vals[0]['F']-8*vals[1]['F']+8*vals[2]['F']-vals[3]['F'])/(12*h)
     dg=(vals[0]['G']-8*vals[1]['G']+8*vals[2]['G']-vals[3]['G'])/(12*h)
     w=lambda z:z*model.w_over_y(z)
     wp=(w(radius-2*h)-8*w(radius-h)+8*w(radius+h)-w(radius+2*h))/(12*h)
     F,G=row['axis']['F'],row['axis']['G'];rf=w(radius)*df-(2*wp-3*flow.beta-2)*F;rg=w(radius)*dg+(2*flow.beta+1-wp)*G-2*F
     row[f'fd_h{h}']={'R_F':rf,'R_G':rg}
    out['runs'].append(row);save();print(c,sign*radius,row,flush=True)
 out.update(ended_utc=datetime.now(timezone.utc).isoformat(),elapsed_seconds=time.monotonic()-start);save();print('COMPLETE',out['elapsed_seconds'],flush=True)
if __name__=='__main__':main()
