"""Own smooth first-integral counterexample; deliberately not a B2 profile.
All one-dimensional integrals are finite Gauss-Legendre quadratures.  No
numerics-lane source is imported.  The exact construction is research/20.
"""
import numpy as np
from numpy.polynomial.legendre import leggauss

class Counterexample:
 def __init__(self,order=64,a0=1.):
  z,w=leggauss(order);self.z=(z+1)/2;self.w=w/2;self.a0=a0
  s=1+self.z;raw=np.exp(-1/((s-1)*(2-s)));self.normalization=raw@self.w
  weight=raw*self.w/self.normalization
  self.mom=np.array([weight.sum(),weight@s,weight@(s*s),weight@np.log(s)])
  self.mom[0]=1.
 def density(self,s):
  s=np.asarray(s);v=np.zeros_like(s,dtype=float);mask=(s>1)&(s<2);t=s[mask]
  v[mask]=np.exp(-1/((t-1)*(2-t)))/self.normalization;return v
 def moments(self,r):
  r=np.asarray(r);shape=r.shape;flat=r.ravel();out=np.zeros((len(flat),4));out[flat>=2]=self.mom
  indices=np.flatnonzero((flat>1)&(flat<2))
  for off in range(0,len(indices),4096):
   k=indices[off:off+4096];span=flat[k]-1;s=1+span[:,None]*self.z[None,:]
   wt=self.density(s)*self.w[None,:]*span[:,None]
   out[k,0]=wt.sum(axis=1);out[k,1]=(wt*s).sum(axis=1);out[k,2]=(wt*s*s).sum(axis=1);out[k,3]=(wt*np.log(s)).sum(axis=1)
  return out.reshape(shape+(4,))
 def y_functions(self,y):
  y=np.asarray(y);r=np.abs(y);m=self.moments(r);c0,c1,c2=np.moveaxis(m[...,:3],-1,0)
  h=r*c0+self.mom[1]-c1
  H=np.sign(y)*(.5*r*r*c0+.5*c2+r*(self.mom[1]-c1))
  hp=np.sign(y)*c0;hpp=self.density(r)
  g=self.mom[1]/h;gp=-g*hp/h;gpp=g*(2*(hp/h)**2-hpp/h)
  f=4*H/h-2*y;fp=2-4*H*hp/h**2
  fpp=-4*hp/h-4*H*hpp/h**2+8*H*hp*hp/h**3
  return g,gp,gpp,f,fp,fpp
 def chi(self,I):
  I=np.asarray(I);r=np.abs(I);m=self.moments(r);eta=m[...,0];q=np.zeros_like(r);mask=r>1
  q[mask]=eta[mask]*np.log(r[mask])-m[...,3][mask]
  c=np.exp(-2*q);cp=np.zeros_like(r);cpp=np.zeros_like(r)
  rr=r[mask];ee=eta[mask];cc=c[mask]
  cp[mask]=np.sign(I[mask])*(-2*ee*cc/rr)
  cpp[mask]=cc*((4*ee*ee+2*ee)/(rr*rr)-2*self.density(rr)/rr)
  return c,cp,cpp
 def temperature(self,I):
  I=np.asarray(I);r=np.abs(I);m=self.moments(1+(r-.25)/.75);eta=m[...,0]
  # F=a0[r^2(1-eta)+ integral_(1)^t (.75s-.5)^2 b(s) ds].
  val=self.a0*(r*r*(1-eta)+.5625*m[...,2]-.75*m[...,1]+.25*m[...,0])
  der=2*self.a0*I*(1-eta);return val,der
 def fields(self,x,y):
  x,y=np.broadcast_arrays(np.asarray(x,dtype=float),np.asarray(y,dtype=float))
  g,gp,gpp,f,fp,fpp=self.y_functions(y);I=x*g;Iy=x*gp;Iyy=x*gpp;c,cp,cpp=self.chi(I)
  psi=x*f*c;ux=-x*(fp*c+f*cp*Iy);uy=f*(c+I*cp)
  pxx=f*g*(2*cp+I*cpp)
  pyy=x*(fpp*c+2*fp*cp*Iy+f*cpp*Iy*Iy+f*cp*Iyy)
  om=-pxx-pyy;theta,td=self.temperature(I)
  return {'Psi':psi,'Omega':om,'Theta':theta,'U1':ux,'U2':uy,'Theta_x':td*g,'Theta_y':td*Iy,'I':I}
 def omega(self,x,y):return self.fields(x,y)['Omega']
 def psi(self,x,y):return self.fields(x,y)['Psi']
 def theta(self,x,y):return self.fields(x,y)['Theta']
 def velocity(self,p):
  p=np.asarray(p);v=self.fields(p[:,0],p[:,1]);return np.column_stack((v['U1'],v['U2']))
