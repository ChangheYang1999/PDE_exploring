"""Independent evaluation of the published nodal density representation.
DCT coefficient reconstruction and Cartesian FD, no collocation solver imports.
"""
import hashlib
from pathlib import Path
import numpy as np
from scipy.fft import dct
from numpy.polynomial.chebyshev import chebval2d, chebder, chebval


class NodalDensity:
    def __init__(self,filename):
        self.filename=str(filename)
        self.md5=hashlib.md5(Path(filename).read_bytes()).hexdigest()
        with np.load(filename) as f:
            self.b=f['b'].copy()
            self.N=int(f['N']);self.M=int(f['M'])
            self.L=float(f['L']);self.cl=float(f['c_l']);self.beta=float(f['beta'])
            self.qnodes=f['q'].copy();self.thetanodes=f['theta'].copy()
            self.C=float(f['C']) if 'C' in f else None
        self.k=1/self.cl
        co=dct(self.b[::-1],type=1,axis=0)/self.N
        co[[0,-1],:]*=.5
        co=dct(co,type=2,axis=1)/self.M
        co[:,0]*=.5
        self.co=co
        self.p3=6+2/(2*self.cl-1)
        self.centre_fractional=None

    def map_inverse(self,theta):
        theta=np.asarray(theta)
        s=theta.copy();lo=np.zeros_like(s);hi=np.full_like(s,np.pi/2)
        for i in range(32):
            f=s+.5*self.beta*np.sin(2*s)-theta
            lo=np.where(f<0,s,lo);hi=np.where(f>0,s,hi)
            new=s-f/(1+self.beta*np.cos(2*s))
            new=np.where((new<lo)|(new>hi),(lo+hi)/2,new)
            s=np.where(np.abs(f)<2e-15,s,new)
        return s

    def bvalues(self,q,theta):
        q,theta=np.broadcast_arrays(q,theta)
        z=2*q-1;c=np.cos(2*self.map_inverse(theta))
        out=np.empty(q.size)
        for a in range(0,q.size,4096):
            sl=slice(a,min(a+4096,q.size))
            out[sl]=chebval2d(z.ravel()[sl],c.ravel()[sl],self.co)
        return out.reshape(q.shape)

    def __call__(self,x,y):
        x,y=np.broadcast_arrays(np.asarray(x,dtype=float),np.asarray(y,dtype=float))
        r2=x*x+y*y;logbase=np.log1p(r2/self.L**2)
        q=-np.expm1(-.5*(1-self.k)*logbase)
        theta=np.arctan2(np.abs(y),np.abs(x))
        b=self.bvalues(q,theta)
        return x*x*y*np.exp(.5*(self.k-3)*logbase)*b

    def center_a_quadratic(self,theta):
        # a(r,theta)=1+r^2 A2(theta)+O(r^4).  Smoothness requires A2 to be a quadratic form on S1.
        cq=2*chebder(self.co,axis=0)
        bq=chebval(np.cos(2*self.map_inverse(theta)),chebval(-1.,cq))
        return ((1-self.k)*bq+(self.k-3))/(2*self.L**2)


if __name__=='__main__':
    import json,sys
    f=NodalDensity(sys.argv[1])
    q,t=np.meshgrid(f.qnodes,f.thetanodes,indexing='ij')
    vals=f.bvalues(q,t)
    theta=(np.arange(512)+.5)*np.pi/(2*512)
    aq=f.center_a_quadratic(theta)
    basis=np.stack((np.ones_like(theta),np.cos(2*theta)),axis=1)
    fit=np.linalg.lstsq(basis,aq,rcond=None)[0]
    leak=aq-basis@fit
    result={'source':f.filename,'md5':f.md5,'node_max_error':float(np.max(np.abs(vals-f.b))),
      'angular_mapping_max_error':float(np.max(np.abs(f.map_inverse(theta)+f.beta/2*np.sin(2*f.map_inverse(theta))-theta))),
      'a2_quadratic_coefficients':fit.tolist(),'a2_nonquadratic_max':float(np.max(np.abs(leak))),
      'a2_nonquadratic_rms':float(np.sqrt(np.mean(leak**2))),'a2_range':[float(np.min(aq)),float(np.max(aq))],
      'parity_at_1_2':[float(f(1.,2.)-f(-1.,2.)),float(f(1.,2.)+f(1.,-2.))]}
    print(json.dumps(result,indent=2))
    if len(sys.argv)>2:Path(sys.argv[2]).write_text(json.dumps(result,indent=2)+'\n')
