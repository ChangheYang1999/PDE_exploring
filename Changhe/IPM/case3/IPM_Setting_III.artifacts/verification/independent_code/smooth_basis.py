"""Cartesian-smooth coefficient representation for an independent solver.

No numerics-lane code is used. The radial map is analytic in x*x+y*y at
finite points and resolves the first natural far-field correction.
"""
import numpy as np
from numpy.polynomial import chebyshev as C
from scipy.special import roots_jacobi


class SmoothBasis:
    def __init__(self, radial=12, angular=8, exponent=1/3, length=1.):
        if not 0<exponent<1:raise ValueError('Need a sublinear positive exponent')
        self.N=int(radial);self.M=int(angular);self.p=float(exponent);self.L=float(length)
        self.a=(1-self.p)/2
        self.size=(self.N+1)*self.M
        self.dc=C.chebder(np.eye(self.N+1),axis=0)

    def geometry(self,x,y):
        x,y=np.broadcast_arrays(np.asarray(x,float),np.asarray(y,float))
        r=np.hypot(x,y);theta=np.arctan2(y,x)
        q=r/self.L
        logden=2*np.log(np.hypot(1.,q))
        w=np.exp(-self.a*logden)
        sigma=-np.expm1(-logden)
        t=1-2*w
        return x,y,r,theta,w,sigma,t

    def evaluate(self,x,y,gradient=False):
        x,y,r,theta,w,sigma,t=self.geometry(x,y)
        k=np.arange(self.M)
        radial=C.chebvander(t,self.N)
        cs=np.cos(theta[...,None]*2*k)
        sig=sigma[...,None]**k
        angular=sig*cs
        values=(y*w)[...,None,None]*angular[...,None]*radial[...,None,:]
        values=values.reshape(x.shape+(self.size,))
        if not gradient:return values
        drad=C.chebval(t,self.dc).transpose(tuple(range(1,t.ndim+1))+(0,))
        invr=np.divide(1.,r,out=np.zeros_like(r),where=r>0)
        den=self.L*self.L+r*r
        tp=2*(1-self.p)*r/den*w
        loghprime=invr[...,None]+(self.p-1)*r[...,None]/den[...,None]+2*k*self.L**2*invr[...,None]/den[...,None]
        h=(r*w)[...,None]*sig
        rhoprime=h[...,None]*(loghprime[...,None]*radial[...,None,:]+tp[...,None,None]*drad[...,None,:])
        rhoprime=rhoprime*(np.sin(theta)[...,None]*cs)[...,None]
        angularprime=np.cos(theta)[...,None]*cs-2*k*np.sin(theta)[...,None]*np.sin(theta[...,None]*2*k)
        thetaprime=h[...,None]*angularprime[...,None]*radial[...,None,:]
        gx=np.cos(theta)[...,None,None]*rhoprime-(np.sin(theta)*invr)[...,None,None]*thetaprime
        gy=np.sin(theta)[...,None,None]*rhoprime+(np.cos(theta)*invr)[...,None,None]*thetaprime
        gx=gx.reshape(x.shape+(self.size,));gy=gy.reshape(x.shape+(self.size,))
        if np.any(r==0):
            a0=self.center_slope()
            gx=np.where((r==0)[...,None],0.,gx)
            gy=np.where((r==0)[...,None],a0,gy)
        return values,gx,gy

    def center_slope(self):
        row=np.zeros((self.M,self.N+1));row[0]=(-1.)**np.arange(self.N+1)
        return row.reshape(-1)

    def axis_amplitude(self):
        return np.broadcast_to((self.L**(1-self.p)*(-1.)**np.arange(self.M))[:,None],(self.M,self.N+1)).copy().reshape(-1)

    def center_strain(self):
        # The strain is -a0/4 plus the sin(3 theta) moment. In u=w,
        # dr/r=-du/[2 a u (1-u^(1/a))]. Only angular modes k=1,2 enter.
        j=np.arange(self.N+1)
        integrals=np.zeros(self.N+1)
        even=(j%2==0);integrals[even]=1/(1-j[even]**2)
        row=(-self.center_slope()/4).reshape(self.M,self.N+1)
        if self.M>1:row[1]+=integrals/(4*self.a)
        if self.M>2:
            beta=1/self.a
            z,wt=roots_jacobi(max(self.N+2,32),0,beta)
            u=(z+1)/2;wt=wt/2**(beta+1)
            powered=wt@C.chebvander(1-2*u,self.N)
            row[2]-=(integrals-powered)/(4*self.a)
        return row.reshape(-1)

    def cubic_density_rows(self):
        # rho=a0*y+b*x*x*y+e*y*y*y+O(r^5).
        j=np.arange(self.N+1)
        endpoint=(-1.)**j
        endpoint_derivative=np.where(j==0,0.,(-1.)**(j-1)*j*j)
        common=self.a*(-endpoint+2*endpoint_derivative)/self.L**2
        brow=np.zeros((self.M,self.N+1));erow=brow.copy()
        brow[0]=common;erow[0]=common
        if self.M>1:
            brow[1]=endpoint/self.L**2;erow[1]=-endpoint/self.L**2
        return brow.reshape(-1),erow.reshape(-1)

    def quartic_stream_difference(self):
        # H=q1-q2=-beta3/2+4 int b5/r^4 dr, converted to u=w.
        row=np.zeros((self.M,self.N+1))
        if self.M>1:row[1]=-(-1.)**np.arange(self.N+1)/(4*self.L**2)
        beta=1/self.a
        def moment(power):
            z,wt=roots_jacobi(max(self.N+2,32),0,power)
            u=(z+1)/2
            return (wt/2**(power+1))@C.chebvander(1-2*u,self.N)
        if self.M>2:row[2]+=moment(beta)/(self.a*self.L**2)
        if self.M>3:row[3]-=(moment(beta)-moment(2*beta))/(self.a*self.L**2)
        return row.reshape(-1)

    def metadata(self):return {'radial':self.N,'angular':self.M,'exponent':self.p,'length':self.L}


class SmoothDensity:
    def __init__(self,basis,coefficients):
        self.basis=basis;self.coefficients=np.asarray(coefficients,float).reshape(-1)
        if len(self.coefficients)!=basis.size:raise ValueError('coefficient count')
    def rho(self,x,y):return self.basis.evaluate(x,y)@self.coefficients
    def gradient(self,x,y):
        _,xv,yv=self.basis.evaluate(x,y,True)
        return xv@self.coefficients,yv@self.coefficients
    def polar_density(self,r,theta):
        r=np.asarray(r);theta=np.asarray(theta)
        return self.rho(r[:,None]*np.cos(theta),r[:,None]*np.sin(theta))
