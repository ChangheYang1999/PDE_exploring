"""Direct physical coefficient chain rule, independent of Cartesian stencils."""
import numpy as np
from numpy.polynomial.chebyshev import chebder,chebval2d
from scipy.fft import dct

def gradients(d,V,pts):
 x,y=np.asarray(pts).T;K=V.shape[1]
 values=np.zeros((d.N+1,d.M,K));values[1:]=V[:-2].reshape(d.N,d.M,K)
 co=dct(values[::-1],type=1,axis=0)/d.N;co[[0,-1]]*=.5;co=dct(co,type=2,axis=1)/d.M;co[:,0]*=.5
 rr=x*x+y*y;D=d.L**2+rr;ell=np.log1p(rr/d.L**2);q=-np.expm1(-.5*(1-d.k)*ell)
 z=2*q-1;s=d.map_inverse(np.arctan2(y,x));c=np.cos(2*s)
 def ev(a):return chebval2d(z,c,a)
 b=ev(d.co);bq=ev(2*chebder(d.co,axis=0));bqq=ev(4*chebder(d.co,m=2,axis=0))
 bc=ev(chebder(d.co,axis=1));bqc=ev(2*chebder(chebder(d.co,axis=0),axis=1))
 db=ev(co);dbq=ev(2*chebder(co,axis=0));dbc=ev(chebder(co,axis=1));dk=(-V[-2]/d.cl**2)[:,None]
 B=b-(1-q)*bq;F=db+dk*ell/2*B
 Fq=dbq+dk*ell/2*(2*bq-(1-q)*bqq);Fc=dbc+dk*ell/2*(bc-(1-q)*bqc);Fl=dk*B/2
 pref=x*x*y*np.exp((d.k-3)*ell/2);dctheta=-2*np.sin(2*s)/(1+d.beta*np.cos(2*s))
 bg=[];dg=[]
 for axis,coord in enumerate([x,y]):
  ell_j=2*coord/D;q_j=(1-d.k)*(1-q)*coord/D
  theta_j=(-y if axis==0 else x)/rr;c_j=dctheta*theta_j
  logpref_j=(2/x if axis==0 else 1/y)+(d.k-3)*coord/D
  bg.append(pref*(logpref_j*b+bq*q_j+bc*c_j))
  dg.append(pref*(logpref_j*F+Fq*q_j+Fc*c_j+Fl*ell_j))
 return np.stack(bg,axis=-1),np.stack(dg,axis=-1).transpose(1,0,2)
